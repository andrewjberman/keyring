"""Daily Bloomberg Excel BQL holdings census for any ETF set (research probe, no schedule).

Generalises bbg_daily_coverage_census.py (the PFOE-group census) with arguments, and raises
the per-sheet read range for larger books. One multi-fund dated request per trading day;
each day's raw response is kept as <out>/<date>.json. Resumable: dates already captured are
skipped. Excel is a probe-owned DispatchEx instance, closed in `finally`.

Usage (from the workspace root):
  python bbg_daily_coverage_census_multi.py --tickers IDVZ,TXUE,BIDD,CGIC,INEQ,SCHY \
      --start 2024-09-30 --end 2026-09-29 --out .runtime/etfs-rivals-idvz-20260930/daily
"""
import argparse
import collections
import datetime
import gc
import json
import pathlib
import sys
import time

import pythoncom
import pywintypes
import win32com.client
import win32process

sys.path.insert(0, str(pathlib.Path.cwd()))
from lib.trading_calendar import calendar_source, trading_days_between  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--tickers", required=True)
parser.add_argument("--start", required=True)
parser.add_argument("--end", required=True)
parser.add_argument("--out", required=True, type=pathlib.Path)
parser.add_argument("--max-rows", type=int, default=2000)
args = parser.parse_args()

OUT = args.out.resolve()
OUT.mkdir(parents=True, exist_ok=True)
dates = trading_days_between(args.start, args.end)
tickers = [t.strip() for t in args.tickers.split(",") if t.strip()]
universe = "[" + ",".join(repr(t + " US Equity") for t in tickers) + "]"
todo = [d for d in dates if not (OUT / (str(d) + ".json")).exists()]
READ_RANGE = "A1:P%d" % args.max_rows
excel = None
book = None
sheets = []
meta = {
    "started": datetime.datetime.now().astimezone().isoformat(),
    "calendar": calendar_source(),
    "date_count": len(dates),
    "tickers": tickers,
}


def com(call):
    deadline = time.monotonic() + 30
    while True:
        try:
            return call()
        except pywintypes.com_error as e:
            if e.hresult not in [-2147418111, -2147417846] or time.monotonic() > deadline:
                raise
            pythoncom.PumpWaitingMessages()
            time.sleep(0.2)


def pump(seconds):
    """Pump COM messages for `seconds` so Bloomberg's asynchronous results can land."""
    stop = time.monotonic() + seconds
    while time.monotonic() < stop:
        pythoncom.PumpWaitingMessages()
        time.sleep(0.03)


try:
    excel = win32com.client.DispatchEx("Excel.Application")
    excel.Visible = False
    excel.DisplayAlerts = False
    meta["pid"] = win32process.GetWindowThreadProcessId(excel.Hwnd)[1]
    (OUT / "run.json").write_text(json.dumps(meta, indent=2))
    with (OUT / "runs.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(meta) + "\n")
    print("PID", meta["pid"], flush=True)
    excel.Workbooks.Open("C:/blp/API/Office Tools/BloombergUI.xla")
    excel.RegisterXLL("C:/blp/API/Office Tools/blpxladdin.xll")
    excel.RegisterXLL("C:/blp/API/Office Tools/brtdwrap.xll")
    book = excel.Workbooks.Add()
    for i in range(20):
        sh = book.Worksheets.Add()
        sh.Name = f"probe{i:02}"
        sheets.append(sh)
    print("START", len(dates), "trading dates;", len(todo), "not yet captured", flush=True)
    for offset in range(0, len(todo), 20):
        batch = todo[offset:offset + 20]
        for sh, d in zip(sheets, batch):
            com(lambda: sh.Cells.ClearContents())
            query = f"get(id()) for(holdings({universe},dates={d}))"
            formula = '=BQL.Query("' + query.replace('"', '""') + '","showallcols=true")'
            com(lambda: setattr(sh.Range("A1"), "Formula", formula))
        com(lambda: excel.Calculate())
        started = time.monotonic()
        status = {}
        while time.monotonic() - started < 45:
            pump(1)
            com(lambda: excel.Calculate())
            status = {str(d): com(lambda: sh.Range("A1").Text) for sh, d in zip(sheets, batch)}
            if time.monotonic() - started >= 3 and not any("Requesting" in v or "Getting" in v for v in status.values()):
                break
        counts = collections.Counter()
        for sh, d in zip(sheets, batch):
            anchor = com(lambda: sh.Range("A1").Text)
            if com(lambda: sh.UsedRange.Rows.Count) > args.max_rows:
                raise RuntimeError("Range cap exceeded on %s" % d)
            vals = com(lambda: sh.Range(READ_RANGE).Value)
            rows = [list(row) for row in vals if any(v is not None for v in row)]
            rows = [row[:max(i + 1 for i, v in enumerate(row) if v is not None)] for row in rows]
            result = {
                "requested_date": str(d),
                "at": datetime.datetime.now().astimezone().isoformat(),
                "query": f"get(id()) for(holdings({universe},dates={d}))",
                "anchor": anchor,
                "rows": rows,
            }
            if anchor == "ID":
                h = rows[0]
                rr = [dict(zip(h, r)) for r in rows[1:]]
                if not all(str(r.get("DATES"))[:10] == str(d) for r in rr):
                    raise RuntimeError("Requested-date provenance mismatch on %s" % d)
                counts.update(r["ORIG_IDS"].split()[0] for r in rr)
            (OUT / (str(d) + ".json")).write_text(json.dumps(result, default=str), encoding="utf-8")
        print("BATCH", min(offset + len(batch), len(todo)), "/", len(todo), str(batch[0]), str(batch[-1]),
              "rows", dict(counts), "errors", sum(v != "ID" for v in status.values()), flush=True)
    meta["completed"] = datetime.datetime.now().astimezone().isoformat()
    (OUT / "run.json").write_text(json.dumps(meta, indent=2))
finally:
    if book is not None:
        book.Close(SaveChanges=False)
    if excel is not None:
        excel.Quit()
    sheets.clear()
    book = None
    excel = None
    gc.collect()
