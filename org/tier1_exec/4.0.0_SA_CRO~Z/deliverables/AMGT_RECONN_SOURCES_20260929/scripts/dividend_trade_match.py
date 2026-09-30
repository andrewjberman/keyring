"""Match inferred trade events against Bloomberg dividend history (local files only, no network).

For each fund in a daily holdings census: consecutive distinct reports, the pro-rata flow factor,
security-only add/trim events at a 0.2% floor (cash and currency lines excluded), then:
  - SHARE-CHANGING: a Stock Split / Stock Dividend / Bonus / Spinoff / Rights Issue ex-date inside
    the event's window (prior report, report] -- the event is a corporate action, not a trade;
  - CASH-DIVIDEND WINDOW: a cash-type ex-date inside the window, compared with the base rate of such
    windows among all position-windows, to show whether small adds cluster on dividend dates
    (the signature of scrip take-up, which Bloomberg does not type separately).

Usage (workspace root):
  python dividend_trade_match.py --census .runtime/etfs-rivals-idvz-20260930/daily \
      --dividends .runtime/etfs-rivals-idvz-20260930/dividends.json
"""
import argparse
import collections
import glob
import json
import os
import re
import statistics

CASHLIKE = re.compile(r"(Curncy$|CASH|MONEY|MMF|^\d{7}[A-Z]? US Equity$)", re.IGNORECASE)
SHARE_CHANGING = {"Stock Split", "Stock Dividend", "Bonus", "Spinoff", "Rights Issue"}
CASH_TYPES = {"Final", "Interim", "Regular Cash", "Special Cash", "Interest on Capital", "Income", "Memorial"}
TOL = 0.002
MIN_SHARES = 5

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--census", required=True)
parser.add_argument("--dividends", required=True)
args = parser.parse_args()

with open(args.dividends, encoding="utf-8") as fh:
    div = json.load(fh)["data"]
share_ex = collections.defaultdict(list)
cash_ex = collections.defaultdict(list)
for sec, val in div.items():
    for row in val.get("DVD_HIST_ALL") or []:
        ex = str(row.get("Ex-Date") or "")[:10]
        if not ex:
            continue
        kind = row.get("Dividend Type")
        if kind in SHARE_CHANGING:
            share_ex[sec].append((ex, kind))
        elif kind in CASH_TYPES:
            cash_ex[sec].append(ex)

snap = collections.defaultdict(dict)
for path in sorted(glob.glob(os.path.join(args.census, "20*.json"))):
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    if doc.get("anchor") != "ID":
        continue
    header = doc["rows"][0]
    for row in doc["rows"][1:]:
        rec = dict(zip(header, row))
        fund = str(rec["ORIG_IDS"]).split()[0]
        entry = snap[fund].setdefault(doc["requested_date"], [collections.Counter(), {}])
        entry[0][str(rec["REPORT_DATE"])[:10]] += 1
        sec = rec.get("ID")
        qty = rec.get("POSITION")
        if sec and isinstance(qty, (int, float)) and not CASHLIKE.search(str(sec)):
            entry[1][sec] = entry[1].get(sec, 0) + qty

out = {}
for fund, days in sorted(snap.items()):
    reports = []
    seen = set()
    for req in sorted(days):
        rep = days[req][0].most_common(1)[0][0]
        if rep not in seen:
            seen.add(rep)
            reports.append((rep, days[req][1]))
    events = 0
    share_changing = collections.Counter()
    small_adds = small_adds_in_cash_window = 0
    position_windows = windows_with_cash_ex = 0
    for (a, pa), (b, pb) in zip(reports, reports[1:]):
        both = [k for k in pa if k in pb and pa[k] > 0]
        if len(both) < 5:
            continue
        flow = statistics.median(pb[k] / pa[k] for k in both)
        for k in both:
            position_windows += 1
            in_cash = any(a < ex <= b for ex in cash_ex.get(k, []))
            windows_with_cash_ex += in_cash
            res = pb[k] - flow * pa[k]
            if abs(res) <= max(TOL * pa[k], MIN_SHARES):
                continue
            events += 1
            hit = [kind for ex, kind in share_ex.get(k, []) if a < ex <= b]
            if hit:
                share_changing[hit[0]] += 1
                continue
            rel = res / pa[k]
            if 0 < rel < 0.05:
                small_adds += 1
                small_adds_in_cash_window += in_cash
    base = windows_with_cash_ex / position_windows if position_windows else 0.0
    rate = small_adds_in_cash_window / small_adds if small_adds else 0.0
    out[fund] = {
        "security_events": events,
        "explained_by_share_changing_action": dict(share_changing),
        "explained_total": sum(share_changing.values()),
        "small_adds_under_5pct": small_adds,
        "small_adds_in_cash_dividend_window": small_adds_in_cash_window,
        "rate_small_adds_in_div_window": round(rate, 4),
        "base_rate_position_windows_with_div": round(base, 4),
        "lift": round(rate / base, 2) if base else None,
    }
print(json.dumps(out, indent=1))
