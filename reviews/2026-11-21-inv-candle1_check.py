"""INVERSION: candle-1 stop (rOrig) vs 3-layer stop (rMultiple), net of costs, day-clustered CIs.
Run from the bus root: python -I reviews/2026-11-21-inv-candle1_check.py"""
import os, sys, json, statistics as st
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
g = {"__name__": "lib", "__file__": os.path.join(ROOT, "analyze.py")}
exec(open(os.path.join(ROOT, "analyze.py"), encoding="utf-8").read(), g)
pairs, *_ = g["build_pairs"]()
COST, _day_ci, _day = g["COST_TICKS"], g["_day_ci"], g["_day"]

def cost(r, tk):
    return COST.get(r["sigId"].split("-")[0], COST["default"]) / tk

rows = []
for r in pairs:
    if not (r["resolved"] and r["kind"] == "INV" and r.get("rOrig") is not None and r.get("rMultiple") is not None):
        continue
    so, sl = r.get("slOrigTk"), r.get("slTk")
    if not so or so <= 0 or not sl or sl <= 0 or r.get("entry") is None or r.get("sl") is None:
        continue
    tick = abs(r["entry"] - r["sl"]) / sl
    atr_tk = (r["atr1m"] / tick) if r.get("atr1m") and tick > 0 else None
    win = r.get("resOrig") in ("TP1", "TP2")
    # MAE before the candle-1 resolution: first MAE checkpoint at or after barsResolveOrig
    # (includes bars after the exit, so it is an upper bound -> survival is a lower bound)
    b = r.get("barsResolveOrig") or 0
    mae = r.get("maeTk")
    for k, v in zip((1, 3, 5, 10, 20), r.get("maeCurve") or []):
        if v is not None and b <= k:
            mae = v; break
    survive = win and mae is not None and mae <= so - 2
    c = cost(r, so)
    if r.get("resOrig") == "SL" or (win and not survive):
        r_slip = -(so + 1) / so
    else:
        r_slip = r["rOrig"] - 1 / so
    rows.append(dict(day=_day(r), tf=r["tf"], side=r["side"], so=so, atr=atr_tk,
                     stopAtr=(so / atr_tk) if atr_tk else None,
                     r3=r["rMultiple"] - cost(r, sl), rc=r["rOrig"] - c, rcs=r_slip - c,
                     w3=r["result"] in ("TP1", "TP2"), wc=win, ws=survive))

def summ(rs):
    if len(rs) < 8:
        return {"n": len(rs)}
    ci = lambda f: _day_ci([(x["day"], x[f]) for x in rs])
    d = _day_ci([(x["day"], x["rc"] - x["r3"]) for x in rs])
    n = len(rs)
    return {"n": n, "days": len({x["day"] for x in rs}),
            "layer3_net": ci("r3"), "candle1_net": ci("rc"), "candle1_net_slip1": ci("rcs"),
            "delta_net": d,
            "median_r3": round(st.median(x["r3"] for x in rs), 3),
            "median_rc": round(st.median(x["rc"] for x in rs), 3),
            "median_rcs": round(st.median(x["rcs"] for x in rs), 3),
            "wr3": round(100 * sum(x["w3"] for x in rs) / n, 1),
            "wrc": round(100 * sum(x["wc"] for x in rs) / n, 1),
            "wrc_slip1": round(100 * sum(x["ws"] for x in rs) / n, 1),
            "wins_surviving_slip1_pct": round(100 * sum(x["ws"] for x in rs) / max(1, sum(x["wc"] for x in rs)), 1),
            "top1pct_share_of_sum_rc": round(sum(sorted((x["rc"] for x in rs), reverse=True)[:max(1, n // 100)])
                                              / sum(x["rc"] for x in rs), 2) if sum(x["rc"] for x in rs) > 0 else None}

out = {"n_rows": len(rows)}
so = sorted(x["so"] for x in rows)
q = lambda p: so[int(p * (len(so) - 1))]
out["slOrigTk_dist"] = {"p10": q(.1), "p25": q(.25), "p50": q(.5), "p75": q(.75), "p90": q(.9),
                        "le1": sum(1 for v in so if v <= 1), "le3": sum(1 for v in so if v <= 3),
                        "le5": sum(1 for v in so if v <= 5)}
sa = sorted(x["stopAtr"] for x in rows if x["stopAtr"] is not None)
out["stopAtr1m_dist"] = {"p10": round(sa[len(sa) // 10], 2), "p50": round(sa[len(sa) // 2], 2),
                         "p90": round(sa[9 * len(sa) // 10], 2)}
filt = {"none": lambda x: True, "ge0.3atr": lambda x: (x["stopAtr"] or 0) >= 0.3,
        "ge0.5atr": lambda x: (x["stopAtr"] or 0) >= 0.5}
for fn, f in filt.items():
    sub = [x for x in rows if f(x)]
    out[fn] = {"ALL": summ(sub)}
    for k in sorted({f"{x['tf']}m/{x['side']}" for x in sub}):
        out[fn][k] = summ([x for x in sub if f"{x['tf']}m/{x['side']}" == k])
json.dump(out, open(os.path.join(ROOT, "reviews", "2026-11-21-inv-candle1_check.json"), "w"), indent=1)
for fn in filt:
    for k, s in out[fn].items():
        if s.get("n", 0) >= 8:
            print(fn, k, s["n"], "3cap", s["layer3_net"]["mean"], s["layer3_net"]["ci90"], "| c1", s["candle1_net"]["mean"],
                  s["candle1_net"]["ci90"], "| c1+slip", s["candle1_net_slip1"]["mean"], s["candle1_net_slip1"]["ci90"],
                  "| delta", s["delta_net"]["mean"], s["delta_net"]["ci90"], "| med", s["median_r3"], s["median_rc"], s["median_rcs"],
                  "| WR", s["wr3"], s["wrc"], s["wrc_slip1"], "| surv", s["wins_surviving_slip1_pct"], "| top1%", s["top1pct_share_of_sum_rc"])
print(out["slOrigTk_dist"], out["stopAtr1m_dist"], out["n_rows"])
