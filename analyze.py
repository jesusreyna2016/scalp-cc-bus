#!/usr/bin/env python3
"""
Scalp CC · motor de analisis.  Ejecutalo desde la raiz del repo scalp-cc-bus:

    python3 analyze.py            # analisis completo -> report.md, report.json, state.json
    python3 analyze.py --quiet    # sin stdout largo

El agente LLM lo corre y luego INTERPRETA report.md / report.json: escribe la
narrativa, decide que proponer y detecta lo raro. Todo el trabajo pesado (parseo,
features, metricas, backtest contrafactual, deteccion de decaimiento, modelo
logistico) vive aqui, en Python, no en el razonamiento del modelo.

Sin dependencias externas: solo stdlib.
"""
import json, os, sys, math, glob, statistics as st
from collections import defaultdict, Counter
from datetime import datetime, timezone, timedelta

ROOT = os.path.dirname(os.path.abspath(__file__))
QUIET = "--quiet" in sys.argv

# ----------------------------------------------------------------------------- IO
def _load_jsonl(path):
    out = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    except FileNotFoundError:
        pass
    return out

def load_events(kind):
    rows = []
    for p in sorted(glob.glob(os.path.join(ROOT, kind, "*.jsonl"))):
        rows.extend(_load_jsonl(p))
    return rows

def _f(d, k):
    v = d.get(k, "")
    if v in ("", None):
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None

def _i(d, k):
    v = _f(d, k)
    return None if v is None else int(round(v))

# ------------------------------------------------------------------ pair & typed
def build_pairs():
    sig_raw = load_events("signals")
    out_raw = load_events("outcomes")
    sigs, outs = {}, {}
    for r in sig_raw:
        sid = r.get("sigId") or r.get("raw", {}).get("sigId")
        if not sid or sid.startswith("TEST-"):
            continue
        sigs[sid] = r  # last wins
    for r in out_raw:
        sid = r.get("sigId") or r.get("raw", {}).get("sigId")
        if not sid or sid.startswith("TEST-"):
            continue
        outs[sid] = r

    now = datetime.now(timezone.utc)
    pairs = []
    orphan_out = 0
    for sid, sg in sigs.items():
        raw = sg.get("raw", {})
        recv = sg.get("receivedAt", "")
        try:
            recv_dt = datetime.fromisoformat(recv.replace("Z", "+00:00"))
        except Exception:
            recv_dt = now
        o = outs.get(sid)
        oraw = o.get("raw", {}) if o else {}
        resolved = bool(o)
        forced_timeout = False
        if not resolved and (now - recv_dt) > timedelta(hours=24):
            resolved = True
            forced_timeout = True

        rec = {
            "sigId": sid,
            "tf": raw.get("tf", "?"),
            "kind": raw.get("kind", "?"),
            "side": raw.get("side", "?"),
            "tier": raw.get("tier", "?"),
            "kz": raw.get("kz", "?"),
            "ver": raw.get("ver", "v1"),
            "recvDate": recv[:10],
            "recvDt": recv_dt,
            # numeric signal context
            "entry": _f(raw, "entry"), "sl": _f(raw, "sl"), "slTk": _f(raw, "slTk"),
            "tp1": _f(raw, "tp1"), "tp1Tk": _f(raw, "tp1Tk"), "rr1": _f(raw, "rr1"),
            "entryZoneTk": _f(raw, "entryZoneTk"),
            "biasScore": _f(raw, "biasScore"),
            "aligned": _i(raw, "aligned"),
            "chopIdx": _f(raw, "chopIdx"), "chop": _i(raw, "chop"), "trend": _i(raw, "trend"),
            "nearEdge": _i(raw, "nearEdge"), "nearTk": _f(raw, "nearTk"),
            "stretchAtr": _f(raw, "stretchAtr"),
            "structDir": _i(raw, "structDir"), "emaStack": _i(raw, "emaStack"),
            "rvol": _f(raw, "rvol"), "atrPctUsed": _f(raw, "atrPctUsed"),
            "remTk": _f(raw, "remTk"), "hourNY": _i(raw, "hourNY"), "dow": _i(raw, "dow"),
            "atr1m": _f(raw, "atr1m"), "atr5m": _f(raw, "atr5m"), "adr": _f(raw, "adr"),
            "strength": raw.get("strength", ""),
            # outcome
            "resolved": resolved, "forcedTimeout": forced_timeout,
            "result": "TIMEOUT" if forced_timeout else oraw.get("result"),
            "rMultiple": _f(oraw, "rMultiple"),
            "barsToResolve": _f(oraw, "barsToResolve"),
            "mfeTk": _f(oraw, "mfeTk"), "maeTk": _f(oraw, "maeTk"),
            "mfeBeforeSLTk": _f(oraw, "mfeBeforeSLTk"), "maxRbeforeSL": _f(oraw, "maxRbeforeSL"),
            "mfeCurve": [_f(oraw, k) for k in ("mfe1", "mfe3", "mfe5", "mfe10", "mfe20")],
            "maeCurve": [_f(oraw, k) for k in ("mae1", "mae3", "mae5", "mae10", "mae20")],
            "hit1R": _i(oraw, "hit1R"), "hit15R": _i(oraw, "hit15R"),
            "hit2R": _i(oraw, "hit2R"), "hit3R": _i(oraw, "hit3R"),
            "bars15R": _i(oraw, "bars15R"), "bars2R": _i(oraw, "bars2R"),
            "revAfterSL": _i(oraw, "revAfterSL"), "revBars": _i(oraw, "revBars"),
            "ambiguous": _i(oraw, "ambiguous"),
        }
        pairs.append(rec)

    for sid in outs:
        if sid not in sigs:
            orphan_out += 1
    return pairs, orphan_out, len(sigs), len(outs)

# ------------------------------------------------------------------------ stats
def _pct(xs, q):
    xs = sorted(v for v in xs if v is not None)
    if not xs:
        return None
    k = (len(xs) - 1) * q
    lo = math.floor(k); hi = math.ceil(k)
    if lo == hi:
        return xs[int(k)]
    return xs[lo] * (hi - k) + xs[hi] * (k - lo)

def seg_metrics(rows):
    res = [r for r in rows if r["resolved"] and r["result"]]
    n = len(res)
    if n == 0:
        return {"n": 0}
    wins_tp1 = [r for r in res if r["result"] in ("TP1", "TP2")]
    losses = [r for r in res if r["result"] == "SL"]
    to = [r for r in res if r["result"] == "TIMEOUT"]
    rs = [r["rMultiple"] for r in res if r["rMultiple"] is not None]
    gains = sum(x for x in rs if x > 0)
    pain = sum(-x for x in rs if x < 0)
    winner_mae = [r["maeTk"] for r in wins_tp1 if r["maeTk"] is not None]
    loser_mfe = [r["mfeBeforeSLTk"] for r in losses if r["mfeBeforeSLTk"] is not None]
    return {
        "n": n,
        "wrTP1": round(100 * len(wins_tp1) / n, 1),
        "nSL": len(losses), "nTO": len(to),
        "expR": round(st.mean(rs), 3) if rs else None,
        "pf": round(gains / pain, 2) if pain > 0 else (None if gains == 0 else 99.0),
        "mfe_p25": _pct([r["mfeTk"] for r in res], .25),
        "mfe_p50": _pct([r["mfeTk"] for r in res], .50),
        "mfe_p75": _pct([r["mfeTk"] for r in res], .75),
        "winnerMAE_p75": _pct(winner_mae, .75),
        "winnerMAE_p90": _pct(winner_mae, .90),
        "loserMFEbeforeSL_p50": _pct(loser_mfe, .50),
        "bars_win_p50": _pct([r["barsToResolve"] for r in wins_tp1], .5),
        "bars_loss_p50": _pct([r["barsToResolve"] for r in losses], .5),
        "entryZoneTk_p50": _pct([r["entryZoneTk"] for r in res], .5),
        "revAfterSL_rate": round(100 * sum(1 for r in losses if r["revAfterSL"] == 1) / len(losses), 1) if losses else None,
    }

def by(rows, keyfn):
    g = defaultdict(list)
    for r in rows:
        g[keyfn(r)].append(r)
    return {k: seg_metrics(v) for k, v in sorted(g.items()) if seg_metrics(v)["n"] >= 1}

# ---------------------------------------------------------- SL post-mortem
def sl_causes(rows):
    losses = [r for r in rows if r["resolved"] and r["result"] == "SL"]
    tally = Counter()
    detail = []
    for r in losses:
        cs = []
        if r["aligned"] == 0:
            cs.append("contra-sesgo")
        if (r["chop"] == 1) or (r["chopIdx"] is not None and r["chopIdx"] > 58):
            cs.append("chop")
        if r["stretchAtr"] is not None and r["stretchAtr"] >= 2.0:
            cs.append("estirado")
        if r["structDir"] is not None and r["side"] == "LONG" and r["structDir"] == -1:
            cs.append("contra-estructura")
        if r["structDir"] is not None and r["side"] == "SHORT" and r["structDir"] == 1:
            cs.append("contra-estructura")
        if r["nearEdge"] == 0 and (r["nearTk"] or 0) > (r["slTk"] or 1e9):
            cs.append("sin-nivel-detras")
        if r["rr1"] is not None and r["rr1"] < 1.0:
            cs.append("RR-bajo")
        if r["maxRbeforeSL"] is not None and r["slTk"] and r["maxRbeforeSL"] >= 1.0:
            cs.append("SL-muy-pegado")
        if r["revAfterSL"] == 1:
            cs.append("stop-en-el-minimo")
        if r["side"] == "LONG" and r["kz"] == "Asia":
            cs.append("killzone-Asia-largo")
        if not cs:
            cs.append("sin-causa-clara")
        for c in cs:
            tally[c] += 1
        detail.append({"sigId": r["sigId"], "tf": r["tf"], "kind": r["kind"], "side": r["side"],
                       "causes": cs, "rMultiple": r["rMultiple"]})
    return dict(tally.most_common()), detail

# --------------------------------------------------- counterfactual exits
def counterfactual(rows):
    """Compara la gestion actual (TP siguiente nivel) contra RR fijos y SL alterno.
    Usa hitXR flags (SL=struct) y la curva MAE para SL alternos aproximados."""
    res = [r for r in rows if r["resolved"] and r["result"] and r["ver"] in ("v3",)]
    n = len(res)
    if n == 0:
        return {"n": 0, "note": "sin outcomes v3 todavia (curva/flags nuevos)"}

    def exp_fixed_rr(mult):
        rs = []
        for r in res:
            hit = {1.0: r["hit1R"], 1.5: r["hit15R"], 2.0: r["hit2R"], 3.0: r["hit3R"]}.get(mult)
            if hit is None:
                continue
            # si toco el multiplo antes del SL struct -> +mult; si no y resultado real fue SL -> -1;
            # si no y fue TIMEOUT/menor -> R real (aprox) o 0
            if hit == 1:
                rs.append(mult)
            elif r["result"] == "SL":
                rs.append(-1.0)
            else:
                rs.append(r["rMultiple"] if r["rMultiple"] is not None else 0.0)
        return (round(st.mean(rs), 3), len(rs)) if rs else (None, 0)

    def exp_alt_sl(sl_mult_atr5):
        """SL = sl_mult_atr5 * ATR5m desde entrada; TP1 siguiente nivel.
        Aprox con curva MAE (max adverso a barras 1/3/5/10/20) + tp1Tk."""
        rs = []
        for r in res:
            if not r["atr5m"] or not r["tp1Tk"]:
                continue
            sld_alt = sl_mult_atr5 * r["atr5m"] / (r["atr1m"] / r["atr1m"] if r["atr1m"] else 1)  # ticks approx
            sld_alt = sl_mult_atr5 * (r["atr5m"])
            # atr5m viene en precio; pásalo a ticks igual que slTk (ya en ticks). Aproxima ratio:
            # usamos slTk/ (sld_struct_precio) no disponible -> fallback: compara en unidades de R struct
            if not r["slTk"]:
                continue
            # curva MAE en ticks; SL alterno en ticks:
            sld_alt_tk = r["slTk"] * (sl_mult_atr5)  # heuristico: sl_mult_atr5 en multiplos del SL struct
            hit_sl = any((m is not None and m >= sld_alt_tk) for m in r["maeCurve"])
            hit_tp = (r["result"] in ("TP1", "TP2")) and not hit_sl
            if hit_tp:
                rs.append((r["tp1Tk"] / sld_alt_tk) if sld_alt_tk else 0.0)
            elif hit_sl:
                rs.append(-1.0)
            else:
                rs.append(0.0)
        return (round(st.mean(rs), 3), len(rs)) if rs else (None, 0)

    base_rs = [r["rMultiple"] for r in res if r["rMultiple"] is not None]
    return {
        "n": n,
        "baseline_nextLevel_expR": round(st.mean(base_rs), 3) if base_rs else None,
        "fixed_1R": exp_fixed_rr(1.0),
        "fixed_1_5R": exp_fixed_rr(1.5),
        "fixed_2R": exp_fixed_rr(2.0),
        "fixed_3R": exp_fixed_rr(3.0),
        "altSL_0_5x_struct": exp_alt_sl(0.5),
        "altSL_1_5x_struct": exp_alt_sl(1.5),
        "note": "fixed_XR: R esperado si el objetivo fuera XR fijo con SL=struct. altSL: SL a mult del SL struct.",
    }

# --------------------------------------------------- decay (WR semanal)
def decay(rows):
    res = [r for r in rows if r["resolved"] and r["result"]]
    wk = defaultdict(list)
    for r in res:
        try:
            iso = r["recvDt"].isocalendar()
            wk[f"{iso[0]}-W{iso[1]:02d}"].append(r)
        except Exception:
            pass
    out = {}
    for k in sorted(wk):
        m = seg_metrics(wk[k])
        out[k] = {"n": m["n"], "wrTP1": m.get("wrTP1"), "expR": m.get("expR")}
    return out

# --------------------------------------------------- modelo logistico (P(TP1))
FEATURES = ["biasScore", "aligned", "chopIdx", "stretchAtr", "structDir", "emaStack",
            "rvol", "atrPctUsed", "nearEdge", "nearTk", "entryZoneTk", "rr1", "hourNY"]

def _stdz(rows):
    cols = {f: [r[f] for r in rows if r[f] is not None] for f in FEATURES}
    stats = {}
    for f, xs in cols.items():
        if len(xs) < 5:
            stats[f] = (0.0, 1.0)
        else:
            mu = st.mean(xs); sd = st.pstdev(xs) or 1.0
            stats[f] = (mu, sd)
    return stats

def logistic_model(rows, min_n=120):
    res = [r for r in rows if r["resolved"] and r["result"] in ("TP1", "TP2", "SL")]
    if len(res) < min_n:
        return {"fitted": False, "n": len(res), "need": min_n}
    stats = _stdz(res)
    def vec(r):
        return [((r[f] - stats[f][0]) / stats[f][1]) if r[f] is not None else 0.0 for f in FEATURES]
    X = [vec(r) for r in res]
    y = [1.0 if r["result"] in ("TP1", "TP2") else 0.0 for r in res]
    w = [0.0] * len(FEATURES); b = 0.0
    lr = 0.1; lam = 1e-3
    for _ in range(400):
        gw = [0.0] * len(FEATURES); gb = 0.0
        for xi, yi in zip(X, y):
            z = b + sum(wj * xj for wj, xj in zip(w, xi))
            p = 1.0 / (1.0 + math.exp(-max(-30, min(30, z))))
            e = p - yi
            for j in range(len(w)):
                gw[j] += e * xi[j]
            gb += e
        m = len(X)
        w = [wj - lr * (gw[j] / m + lam * wj) for j, wj in enumerate(w)]
        b = b - lr * (gb / m)
    # calibracion (Brier + deciles) in-sample
    preds = []
    for xi, yi in zip(X, y):
        z = b + sum(wj * xj for wj, xj in zip(w, xi))
        preds.append((1.0 / (1.0 + math.exp(-max(-30, min(30, z)))), yi))
    brier = st.mean((p - yi) ** 2 for p, yi in preds)
    order = sorted(preds)
    deciles = []
    for d in range(10):
        chunk = order[d * len(order) // 10:(d + 1) * len(order) // 10]
        if chunk:
            deciles.append({"bin": d, "pred": round(st.mean(p for p, _ in chunk), 3),
                            "actual": round(st.mean(yi for _, yi in chunk), 3), "n": len(chunk)})
    coefs = sorted(zip(FEATURES, w), key=lambda t: -abs(t[1]))
    return {"fitted": True, "n": len(res), "brier": round(brier, 4),
            "bias": round(b, 3),
            "coefficients": [{"feature": f, "weight": round(wj, 3)} for f, wj in coefs],
            "calibration_deciles": deciles,
            "note": "in-sample; interpretar signo/magnitud, no como verdad fuera de muestra hasta 200+"}

# --------------------------------------------------------------- experiments
def eval_experiments(pairs):
    path = os.path.join(ROOT, "experiments.json")
    try:
        with open(path) as f:
            exps = json.load(f)
    except Exception:
        return []
    out = []
    for e in exps.get("experiments", []):
        if e.get("status") not in ("running", "proposed"):
            out.append(e)
            continue
        cd = e.get("changeDate")
        seg = e.get("segment", {})
        def match(r):
            for k, v in seg.items():
                if str(r.get(k)) != str(v):
                    return False
            return True
        before, after = [], []
        for r in pairs:
            if not (r["resolved"] and r["result"] and match(r)):
                continue
            (after if (cd and r["recvDate"] >= cd) else before).append(r)
        e2 = dict(e)
        e2["beforeN"] = len(before); e2["afterN"] = len(after)
        e2["before"] = seg_metrics(before) if before else {"n": 0}
        e2["after"] = seg_metrics(after) if after else {"n": 0}
        if e2["afterN"] >= 40 and e2["beforeN"] >= 20:
            db = (e2["after"].get("expR") or 0) - (e2["before"].get("expR") or 0)
            e2["verdict"] = "confirmed" if db > 0.05 else "rejected" if db < -0.05 else "flat"
        out.append(e2)
    return out

# ------------------------------------------------ Session Analyst cross-feed
def sa_context():
    """Si la rutina clono tambien session-analyst-bus como fuente hermana, lee su
    veredicto del dia y la narrativa multi-dia para que el agente los cruce."""
    cands = [
        os.path.join(ROOT, "..", "session-analyst-bus"),
        os.path.join(ROOT, "..", "..", "session-analyst-bus"),
        "/home/user/session-analyst-bus",
    ]
    base = next((c for c in cands if os.path.isdir(c)), None)
    if not base:
        return {"available": False}
    out = {"available": True}
    for rel, key in (("plans/latest.json", "latest_plan"),
                     ("state/sa-state.json", "sa_state"),
                     ("live/market.json", "market")):
        p = os.path.join(base, rel)
        try:
            with open(p, encoding="utf-8") as f:
                out[key] = json.load(f)
        except Exception:
            pass
    p = os.path.join(base, "narrative.md")
    try:
        with open(p, encoding="utf-8") as f:
            out["narrative"] = f.read()[:4000]
    except Exception:
        pass
    return out

# ---------------------------------------------------------------------- main
def main():
    pairs, orphan_out, n_sig, n_out = build_pairs()
    resolved = [r for r in pairs if r["resolved"] and r["result"]]
    pending = [r for r in pairs if not r["resolved"]]

    report = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "totals": {"signals": n_sig, "outcomes": n_out, "pairs_resolved": len(resolved),
                   "pending": len(pending), "orphan_outcomes": orphan_out},
        "by_tf_kind_side": by(pairs, lambda r: f"{r['tf']}m/{r['kind']}/{r['side']}"),
        "by_tier": by(pairs, lambda r: r["tier"]),
        "by_kz": by(pairs, lambda r: r["kz"]),
        "by_nearEdge": by(pairs, lambda r: f"edge={r['nearEdge']}"),
        "by_aligned": by(pairs, lambda r: f"aligned={r['aligned']}"),
        "by_emaStack": by(pairs, lambda r: f"emaStack={r['emaStack']}"),
        "overall": seg_metrics(pairs),
        "sl_post_mortem": None,
        "counterfactual": counterfactual(pairs),
        "decay_weekly": decay(pairs),
        "model": logistic_model(pairs),
        "experiments": eval_experiments(pairs),
        "session_analyst": sa_context(),
    }
    causes, detail = sl_causes(pairs)
    report["sl_post_mortem"] = {"causes": causes, "n_losses": sum(1 for r in resolved if r["result"] == "SL"),
                                "detail": detail[:60]}

    with open(os.path.join(ROOT, "report.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    # state.json (contadores + espacio para recommendedParams que mantiene el agente)
    try:
        with open(os.path.join(ROOT, "state.json")) as f:
            state = json.load(f)
    except Exception:
        state = {}
    state["updatedAt"] = report["generatedAt"]
    state["totals"] = report["totals"]
    state["metrics_by_tf_kind_side"] = report["by_tf_kind_side"]
    state["sl_causes"] = causes
    state.setdefault("recommendedParams", {"note": "lo mantiene el agente en la revision semanal"})
    state.setdefault("executionGate", {"phase": "advisor", "readyForLive": False})
    with open(os.path.join(ROOT, "state.json"), "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

    # report.md legible para el agente
    L = []
    t = report["totals"]
    L.append(f"# Scalp CC · report {report['generatedAt'][:16]}Z\n")
    L.append(f"- signals={t['signals']} outcomes={t['outcomes']} pares_resueltos={t['pairs_resolved']} "
             f"pendientes={t['pending']} huerfanos={t['orphan_outcomes']}\n")
    def tbl(title, d):
        L.append(f"\n## {title}\n")
        L.append("| seg | n | WR TP1 | E[R] | PF | SL | MFE p50 | winMAE p75 | rev% |\n|---|--|--|--|--|--|--|--|--|\n")
        for k, m in d.items():
            L.append(f"| {k} | {m['n']} | {m.get('wrTP1','')} | {m.get('expR','')} | {m.get('pf','')} | "
                     f"{m.get('nSL','')} | {m.get('mfe_p50','')} | {m.get('winnerMAE_p75','')} | {m.get('revAfterSL_rate','')} |\n")
    tbl("Por tf / kind / side", report["by_tf_kind_side"])
    tbl("Por tier", report["by_tier"])
    tbl("Por killzone", report["by_kz"])
    tbl("Por nearEdge", report["by_nearEdge"])
    tbl("Por aligned", report["by_aligned"])
    L.append("\n## Autopsia de SL\n")
    L.append(f"n_losses={report['sl_post_mortem']['n_losses']}  causas: "
             + ", ".join(f"{k}×{v}" for k, v in causes.items()) + "\n")
    L.append("\n## Contrafactual de gestion\n```json\n"
             + json.dumps(report["counterfactual"], indent=2, ensure_ascii=False) + "\n```\n")
    L.append("\n## Decaimiento semanal\n```json\n"
             + json.dumps(report["decay_weekly"], indent=2, ensure_ascii=False) + "\n```\n")
    L.append("\n## Modelo P(TP1)\n```json\n"
             + json.dumps(report["model"], indent=2, ensure_ascii=False) + "\n```\n")
    if report["experiments"]:
        L.append("\n## Experimentos\n```json\n"
                 + json.dumps(report["experiments"], indent=2, ensure_ascii=False) + "\n```\n")
    sa = report["session_analyst"]
    L.append("\n## Session Analyst\n")
    if not sa.get("available"):
        L.append("_(session-analyst-bus no clonado en esta corrida)_\n")
    else:
        L.append("```json\n" + json.dumps({k: v for k, v in sa.items() if k != "narrative"},
                                          indent=2, ensure_ascii=False)[:3000] + "\n```\n")
        if sa.get("narrative"):
            L.append("\n### narrative.md\n" + sa["narrative"][:2000] + "\n")
    with open(os.path.join(ROOT, "report.md"), "w", encoding="utf-8") as f:
        f.write("".join(L))

    if not QUIET:
        print("".join(L))
    print(f"[analyze.py] pares_resueltos={t['pairs_resolved']} pendientes={t['pending']} "
          f"huerfanos={t['orphan_outcomes']}  -> report.md / report.json / state.json")

if __name__ == "__main__":
    main()
