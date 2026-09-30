"""Feasibility probe: can daily issuer holdings reveal trades once pro-rata fund flows are removed?

Model per fund, per consecutive pair of report dates:
  flow factor f   = median over held-both-days securities of q_t / q_{t-1}
                    (in-kind creations/redemptions scale every position ~pro rata)
  residual        = q_t - f * q_{t-1}
  trade event     = |residual| > max(TOL * q_{t-1}, MIN_SHARES), or an entry / exit;
                    TOL defaults to 0.2% (env TRADE_TOL)
Reads local archive files only; no network.

Run from the workspace root:
  python org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/scripts/trade_inference_probe.py BASG GQGU
"""
import csv
import glob
import io
import json
import os
import statistics
import sys
from collections import Counter

ROOT = ".runtime/amgt-reconn-daily-census-20260929"
TOL = float(os.environ.get("TRADE_TOL", "0.002"))  # 0.2% of prior shares (Andrew: trades can be 0.2% or more)
MIN_SHARES = 5  # in-kind baskets round to whole shares


def load(fund):
    days = {}
    for p in sorted(glob.glob(os.path.join(ROOT, fund.lower(), "*.txt"))):
        d = os.path.basename(p)[:10]
        with open(p, encoding="utf-8", errors="replace") as fh:
            txt = fh.read()
        rows = [r for r in csv.DictReader(io.StringIO(txt), delimiter="|") if r.get("fund_ticker") == fund]
        pos, cash = {}, 0.0
        for r in rows:
            q = float(r["quantity"] or 0)
            mv = float(r["market_value"] or 0)
            if r["security_group"] in ("Cash", "Currency") or not r["security_cusip"]:
                cash += mv
                continue
            k = r["security_cusip"]
            prev_q, prev_mv, _ = pos.get(k, (0, 0, ""))
            pos[k] = (prev_q + q, prev_mv + mv, r["security_ticker"])
        days[d] = (pos, cash)
    return days


def analyse(fund):
    days = load(fund)
    ds = sorted(days)
    pairs = n_pos = n_prorata = 0
    flow_days = 0
    trade_days = 0
    events = Counter()
    disp = []
    big = []
    for a, b in zip(ds, ds[1:]):
        pa = days[a][0]
        pb = days[b][0]
        both = [k for k in pa if k in pb and pa[k][0] > 0]
        if len(both) < 5:
            continue
        pairs += 1
        ratios = [pb[k][0] / pa[k][0] for k in both]
        f = statistics.median(ratios)
        if abs(f - 1) > 0.001:
            flow_days += 1
        disp.append(statistics.median(abs(r - f) for r in ratios))
        day_events = 0
        for k in both:
            n_pos += 1
            res = pb[k][0] - f * pa[k][0]
            if abs(res) <= max(TOL * pa[k][0], MIN_SHARES):
                n_prorata += 1
                continue
            kind = "add" if res > 0 else "trim"
            events[kind] += 1
            day_events += 1
            px = pb[k][1] / pb[k][0] if pb[k][0] else 0
            big.append((abs(res * px), b, pb[k][2], kind, round(res), round(f, 4)))
        for k in pb:
            if k not in pa:
                events["entry"] += 1
                day_events += 1
                big.append((pb[k][1], b, pb[k][2], "entry", round(pb[k][0]), round(f, 4)))
        for k in pa:
            if k not in pb:
                events["exit"] += 1
                day_events += 1
                big.append((pa[k][1], b, pa[k][2], "exit", -round(pa[k][0]), round(f, 4)))
        trade_days += day_events > 0
    big.sort(reverse=True)
    return {
        "fund": fund,
        "tolerance": TOL,
        "report_dates": len(ds),
        "first": ds[0],
        "last": ds[-1],
        "pairs": pairs,
        "pairs_with_flow_factor_ne_1": flow_days,
        "median_ratio_dispersion_around_f": round(statistics.median(disp), 6) if disp else None,
        "position_days": n_pos,
        "position_days_pro_rata": n_prorata,
        "pct_pro_rata": round(100 * n_prorata / n_pos, 2) if n_pos else None,
        "trade_events": dict(events),
        "pairs_with_any_trade": trade_days,
        "largest_10_by_est_notional_usd": [
            {"notional": round(x[0]), "date": x[1], "ticker": x[2], "kind": x[3], "shares": x[4], "flow_f": x[5]}
            for x in big[:10]
        ],
    }


if __name__ == "__main__":
    out = [analyse(f) for f in sys.argv[1:]]
    print(json.dumps(out, indent=1))
