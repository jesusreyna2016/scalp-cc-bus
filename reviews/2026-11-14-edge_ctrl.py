"""Scalp CC edge vs control. Usage: python -I edge_ctrl.py <bus_dir> <bars_dir> <out_json>"""
import json, glob, os, sys, math, random, bisect, collections as C
from datetime import datetime, timezone, timedelta

BUS, BARS, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
K_CTRL = 5
random.seed(20261114)
DST_END = datetime(2026, 11, 1, 6, 0, tzinfo=timezone.utc).timestamp()

def ny_hour(ts):
    off = -4 if ts < DST_END else -5
    return (datetime.fromtimestamp(ts, timezone.utc) + timedelta(hours=off)).hour

# ---- bars ----
bars = C.defaultdict(dict)
for f in sorted(glob.glob(os.path.join(BARS, '*.json'))):
    d = json.load(open(f, encoding='utf-8'))
    for sym, arr in d['symbols'].items():
        for b in arr:
            bars[sym][int(b[0])] = b
B = {}
for sym, m in bars.items():
    ts = sorted(m)
    B[sym] = (ts, [m[t] for t in ts])

# ---- dataset (Pine outcomes) + signal ts / tick ----
ds = {}
for l in open(os.path.join(BUS, 'dataset.jsonl'), encoding='utf-8'):
    r = json.loads(l)
    if r['sigId'].startswith('TEST'):
        continue
    ds[(r['recvDate'], r['sigId'])] = r
sig = {}
for f in sorted(glob.glob(os.path.join(BUS, 'signals', '*.jsonl'))):
    day = os.path.basename(f)[:10]
    for l in open(f, encoding='utf-8'):
        try:
            e = json.loads(l)
        except Exception:
            continue
        raw = e.get('raw') or {}
        try:
            ts = int(e['ts']) / 1000.0
            en, sl, slTk = float(raw['entry']), float(raw['sl']), float(raw['slTk'])
            tick = abs(en - sl) / slTk if slTk > 0 else None
        except Exception:
            continue
        sig[(day, e['sigId'])] = (ts, e.get('sym'), tick)

def path(sym, t0, nb):
    ts, arr = B.get(sym, ([], []))
    i = bisect.bisect_left(ts, t0)
    if i >= len(ts) or ts[i] - t0 > 360:
        return None
    out = []
    tmax = ts[i] + nb * 300 + 3600  # allow the daily break inside the horizon
    while i < len(ts) and len(out) < nb and ts[i] <= tmax:
        out.append(arr[i]); i += 1
    return out if len(out) >= max(2, nb // 2) else None

def sim(p, side, slP, tpP, rr):
    """first touch on 5m bars; same-bar SL+TP = SL (conservative). returns (R, res, ambiguous)"""
    en = p[0][1]
    s = 1 if side == 'LONG' else -1
    sl, tp = en - s * slP, en + s * tpP
    for b in p:
        h, lo = b[2], b[3]
        hs = lo <= sl if s == 1 else h >= sl
        ht = h >= tp if s == 1 else lo <= tp
        if hs and ht:
            return -1.0, 'SL', 1
        if hs:
            return -1.0, 'SL', 0
        if ht:
            return rr, 'TP', 0
    return s * (p[-1][4] - en) / slP, 'TO', 0

rows = []
miss = C.Counter()
days_by_sym = C.defaultdict(set)
for sym, (ts, _) in B.items():
    for t in ts:
        days_by_sym[sym].add(int(t // 86400))
for key, r in ds.items():
    s = sig.get(key)
    if not s:
        miss['nosig'] += 1; continue
    t0, sym, tick = s
    sym = sym or r['sigId'].split('-')[0]
    if sym not in B or not tick:
        miss['nobars_sym'] += 1; continue
    slTk, tpTk = r.get('slTk'), r.get('tp1Tk')
    if not slTk or not tpTk or slTk <= 0 or tpTk <= 0:
        miss['geom'] += 1; continue
    nb = max(2, math.ceil(40 * int(r['tf']) / 5))
    p = path(sym, t0, nb)
    if not p:
        miss['nopath'] += 1; continue
    slP, tpP, rr = slTk * tick, tpTk * tick, tpTk / slTk
    real = sim(p, r['side'], slP, tpP, rr)
    mir = sim(p, 'SHORT' if r['side'] == 'LONG' else 'LONG', slP, tpP, rr)
    hr = ny_hour(t0)
    d0 = int(t0 // 86400)
    ctr = []
    cand_days = [d for d in range(d0 - 10, d0 + 11) if d != d0 and d in days_by_sym[sym]]
    tries = 0
    while len(ctr) < K_CTRL and tries < 60 and cand_days:
        tries += 1
        d = random.choice(cand_days)
        tc = d * 86400 + (t0 % 86400) + random.choice([-1, 1]) * random.randint(0, 11) * 300
        if ny_hour(tc) != hr:
            continue
        pc = path(sym, tc, nb)
        if not pc:
            continue
        ctr.append(sim(pc, r['side'], slP, tpP, rr))
    if len(ctr) < 2:
        miss['noctrl'] += 1; continue
    pine_R = r['rMultiple']
    pine_win = 1 if r['result'] in ('TP1', 'TP2') else 0
    cost2 = 2.0 / slTk  # 2 ticks round trip, in R
    rows.append(dict(
        day=datetime.fromtimestamp(t0, timezone.utc).strftime('%Y-%m-%d'),
        sym=sym, tf=r['tf'], kind=r['kind'], side=r['side'], tier=r['tier'], kz=r['kz'],
        slTk=slTk, rr=rr, pineR=pine_R, pineWin=pine_win, pineRes=r['result'],
        realR=real[0], realWin=1 if real[1] == 'TP' else 0, amb=real[2],
        mirR=mir[0], mirWin=1 if mir[1] == 'TP' else 0,
        ctrR=sum(c[0] for c in ctr) / len(ctr), ctrWin=sum(1 for c in ctr if c[1] == 'TP') / len(ctr),
        ctrAmb=sum(c[2] for c in ctr) / len(ctr), cost=cost2,
        nullWin=slTk / (slTk + tpTk)))
json.dump({'rows': rows, 'miss': miss}, open(OUT, 'w'))
print('rows', len(rows), dict(miss))
