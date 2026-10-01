"""Scripted Bloomberg pull (R-21): two-year dividend history (DVD_HIST_ALL) for every security a
fund group held in a captured daily holdings census. Research evidence only, no schedule.

Reuses the shared client integrations/bloomberg/mcp/blp_client.reference_data (DAPI refdata).
Cash and currency lines are skipped. The raw responses are written once, then read by the
matcher (dividend_trade_match.py).

Usage (from the workspace root, in the Bloomberg Python env):
  python dividend_history_pull.py --census .runtime/etfs-rivals-idvz-20260930/daily \
      --start 20240901 --end 20260930 --out .runtime/etfs-rivals-idvz-20260930/dividends.json
"""
import argparse
import glob
import json
import os
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path.cwd()))
from integrations.bloomberg.mcp import blp_client  # noqa: E402

CASHLIKE = re.compile(r"(Curncy$|CASH|MONEY|MMF|^\d{7}[A-Z]? US Equity$)", re.IGNORECASE)

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--census", required=True)
parser.add_argument("--start", required=True)
parser.add_argument("--end", required=True)
parser.add_argument("--out", required=True)
parser.add_argument("--batch", type=int, default=50)
args = parser.parse_args()

securities = set()
for path in sorted(glob.glob(os.path.join(args.census, "20*.json"))):
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    if doc.get("anchor") != "ID":
        continue
    header = doc["rows"][0]
    for row in doc["rows"][1:]:
        rec = dict(zip(header, row))
        sec = rec.get("ID")
        if sec and not CASHLIKE.search(str(sec)):
            securities.add(str(sec))
securities = sorted(securities)
print("SECURITIES", len(securities), flush=True)

result = {"start": args.start, "end": args.end, "securities": len(securities), "data": {}}
overrides = {"DVD_START_DT": args.start, "DVD_END_DT": args.end}
for i in range(0, len(securities), args.batch):
    batch = securities[i:i + args.batch]
    got = blp_client.reference_data(batch, ["DVD_HIST_ALL"], overrides=overrides, timeout_s=90)
    result["data"].update(got)
    errors = sum(1 for v in got.values() if "__error__" in v or "__field_errors__" in v)
    print("BATCH", i + len(batch), "/", len(securities), "returned", len(got), "errors", errors, flush=True)
missing = [s for s in securities if s not in result["data"]]
result["missing"] = missing
with open(args.out, "w", encoding="utf-8") as fh:
    json.dump(result, fh, default=str)
print("DONE returned", len(result["data"]), "missing", len(missing), flush=True)
