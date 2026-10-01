"""Style-read preview (ETFS_RIVALS FWD-10 / PRD G9) over captured daily holdings. Local files only, no network.

Per fund over one research window: the trade schedule (0.2% floor, 5-share floor, pro-rata flow removed, cash and
currency lines excluded, share-changing corporate actions removed where dividend history is supplied), then the G9
measures:
  timing_concentration   share of trade notional in the fund's top 4 weeks
  reconstitution_share   share of entries+exits in the fund's single busiest calendar month (and which month)
  breadth                median share of held positions traded per report pair
  book_touched           distinct securities traded / distinct securities held in the window
  median_trade_size_pct  median |discretionary shares| / prior shares over adds and trims
  turnover               trade notional / mean book value (window)
  trade_count            context only

Sources: Bloomberg census directories (one JSON per requested date, multi-fund rows keyed by ORIG_IDS), or an issuer
FilePoint archive (pipe-delimited .txt per date) for a fund Bloomberg does not carry.

Usage (workspace root):
  python style_read_preview.py --start 2025-10-01 --end 2026-09-29 \
      --bbg .runtime/etfs-rivals-idvz-20260930/daily --bbg .runtime/amgt-reconn-daily-census-20260929 \
      --bbg .runtime/etfs-rivals-pfoe-home-20260930/daily --issuer GQGU=.runtime/amgt-reconn-daily-census-20260929/gqgu \
      --dividends .runtime/etfs-rivals-idvz-20260930/dividends.json --out .runtime/style_read_preview.json
"""
import argparse
import collections
import csv
import datetime
import glob
import io
import json
import os
import re
import statistics

CASHLIKE = re.compile(r"(Curncy$|CASH|MONEY|MMF|^\d{7}[A-Z]? US Equity$)", re.IGNORECASE)
SHARE_CHANGING = {"Stock Split", "Stock Dividend", "Bonus", "Spinoff", "Rights Issue"}
TOL = 0.002
MIN_SHARES = 5


def load_bbg(directory, snaps):
    for path in sorted(glob.glob(os.path.join(directory, "20*.json"))):
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
        if doc.get("anchor") != "ID":
            continue
        header = doc["rows"][0]
        req = doc["requested_date"]
        for row in doc["rows"][1:]:
            rec = dict(zip(header, row))
            fund = str(rec.get("ORIG_IDS", "")).split()[0]
            sec = rec.get("ID")
            qty = rec.get("POSITION")
            if not fund or not sec:
                continue
            day = snaps[fund].setdefault(req, [collections.Counter(), {}, {}])
            day[0][str(rec.get("REPORT_DATE"))[:10]] += 1
            if isinstance(qty, (int, float)) and not CASHLIKE.search(str(sec)):
                day[1][sec] = day[1].get(sec, 0) + qty
                mv = rec.get("REPORTED_MKT_VAL")
                if isinstance(mv, (int, float)):
                    day[2][sec] = day[2].get(sec, 0) + mv


def load_issuer(fund, directory, snaps):
    for path in sorted(glob.glob(os.path.join(directory, "*.txt"))):
        req = os.path.basename(path)[:10]
        with open(path, encoding="utf-8", errors="replace") as fh:
            rows = [r for r in csv.DictReader(io.StringIO(fh.read()), delimiter="|") if r.get("fund_ticker") == fund]
        day = snaps[fund].setdefault(req, [collections.Counter(), {}, {}])
        for r in rows:
            day[0][req] += 1
            if r.get("security_group") in ("Cash", "Currency") or not r.get("security_cusip"):
                continue
            sec = r["security_cusip"]
            day[1][sec] = day[1].get(sec, 0) + float(r.get("quantity") or 0)
            day[2][sec] = day[2].get(sec, 0) + float(r.get("market_value") or 0)


def reports(days):
    out, seen = [], set()
    for req in sorted(days):
        rep = days[req][0].most_common(1)[0][0] if days[req][0] else req
        if rep not in seen and days[req][1]:
            seen.add(rep)
            out.append((rep, days[req][1], days[req][2]))
    return out


def measure(fund, days, start, end, share_ex):
    reps = [r for r in reports(days) if start <= r[0] <= end]
    week_notional = collections.Counter()
    month_events = collections.Counter()
    sizes, breadth, traded, held = [], [], set(), set()
    notional_total = 0.0
    trades = entries_exits = removed = 0
    book_values = []
    for (a, pa, ma), (b, pb, mb) in zip(reps, reps[1:]):
        held.update(pb)
        book_values.append(sum(mb.values()))
        both = [k for k in pa if k in pb and pa[k] > 0]
        if len(both) < 5:
            continue
        flow = statistics.median(pb[k] / pa[k] for k in both)
        n_traded = 0
        week = datetime.date.fromisoformat(b).isocalendar()[:2]
        for k in both:
            res = pb[k] - flow * pa[k]
            if abs(res) <= max(TOL * pa[k], MIN_SHARES):
                continue
            if any(a < ex <= b for ex in share_ex.get(k, [])):
                removed += 1
                continue
            px = (mb.get(k) or 0) / pb[k] if pb[k] else 0
            notional = abs(res) * px
            week_notional[week] += notional
            notional_total += notional
            sizes.append(abs(res) / pa[k])
            traded.add(k)
            n_traded += 1
            trades += 1
        for k in [x for x in pb if x not in pa] + [x for x in pa if x not in pb]:
            value = abs((mb.get(k) if k in pb else ma.get(k)) or 0)
            week_notional[week] += value
            notional_total += value
            month_events[b[:7]] += 1
            traded.add(k)
            entries_exits += 1
            trades += 1
        breadth.append(n_traded / len(both))
    top4 = sum(v for _, v in week_notional.most_common(4))
    busiest = month_events.most_common(1)[0] if month_events else (None, 0)
    return {
        "fund": fund, "reports_in_window": len(reps),
        "trade_count": trades, "entries_exits": entries_exits, "corporate_action_events_removed": removed,
        "timing_concentration": round(top4 / notional_total, 3) if notional_total else None,
        "reconstitution_share": round(busiest[1] / entries_exits, 3) if entries_exits else None,
        "busiest_month": busiest[0],
        "breadth_median": round(statistics.median(breadth), 4) if breadth else None,
        "book_touched": round(len(traded) / len(held), 3) if held else None,
        "median_trade_size_pct": round(100 * statistics.median(sizes), 2) if sizes else None,
        "turnover": round(notional_total / statistics.mean(book_values), 2) if book_values and statistics.mean(book_values) else None,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--start", required=True)
    ap.add_argument("--end", required=True)
    ap.add_argument("--bbg", action="append", default=[])
    ap.add_argument("--issuer", action="append", default=[], help="FUND=directory")
    ap.add_argument("--dividends", action="append", default=[])
    ap.add_argument("--only", default="")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    snaps = collections.defaultdict(dict)
    for d in args.bbg:
        load_bbg(d, snaps)
    for spec in args.issuer:
        fund, directory = spec.split("=", 1)
        snaps.pop(fund, None)
        load_issuer(fund, directory, snaps)
    share_ex = collections.defaultdict(list)
    for path in args.dividends:
        with open(path, encoding="utf-8") as fh:
            for sec, val in json.load(fh)["data"].items():
                for row in val.get("DVD_HIST_ALL") or []:
                    if row.get("Dividend Type") in SHARE_CHANGING and row.get("Ex-Date"):
                        share_ex[sec].append(str(row["Ex-Date"])[:10])
    only = {x for x in args.only.split(",") if x}
    results = [measure(f, snaps[f], args.start, args.end, share_ex) for f in sorted(snaps) if not only or f in only]
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=1)
    for r in results:
        print(json.dumps(r))


if __name__ == "__main__":
    main()
