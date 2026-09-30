"""Round 5 (~M) check SC5-e11-AC2: the CUSIP guard's dry-run against the LIVE tables (read only).

Reads the live etf-classifications (denominator = rows read) and the live bd-securities (rows read), applies the
seeder's own guard (seed_bd_securities.is_cusip_row, imported, not re-typed) and prints:
  CUSIP-GUARD etf_rows=<n> cusip_rows=<n> bd_rows=<n> bd_delta_from_cusip=<n>
  CUSIP-GUARD-PLANNED planned=<n> would_copy_to_bd=<n>
bd_delta_from_cusip = etf-classifications rows with a CUSIP: key that the seeder would let through AND that bd-securities
does not already hold (the new bd-securities rows the seeder would mint from CUSIP keys). would_copy_to_bd = planned
rows (R2_CUSIP_CENSUS_20260930.json 'rows') that the guard does not skip. Both must be 0; a nonzero exits 1 (a refusal).
Only Scan is called; nothing is written. Run from the repo (or worktree) root.
"""
import importlib.util
import json
import os
import sys

import boto3

ROOT = os.getcwd()
SEEDER = os.path.join(ROOT, "data/black_diamond/scripts/classification/seed_bd_securities.py")
CENSUS = os.path.join(ROOT, "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_CUSIP_CENSUS_20260930.json")


def _scan_keys(table):
    keys, last = [], None
    while True:
        kw = {"ExclusiveStartKey": last} if last else {}
        resp = table.scan(**kw)
        keys.extend(i.get("ticker", "") for i in resp.get("Items", []))
        last = resp.get("LastEvaluatedKey")
        if not last:
            return keys


def main():
    spec = importlib.util.spec_from_file_location("seed_bd_securities", SEEDER)
    seeder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(seeder)

    ddb = boto3.resource("dynamodb", region_name=seeder.REGION)
    etf_keys = _scan_keys(ddb.Table(seeder.SOURCE_TABLE))
    bd_keys = set(_scan_keys(ddb.Table(seeder.TARGET_TABLE)))
    bd_rows = len(bd_keys)

    cusip_rows = sum(1 for k in etf_keys if seeder.is_cusip_row({"ticker": k}))
    # the rows the seeder would copy (guard applied) that carry a CUSIP: key and are new to bd-securities
    would_write = [k for k in etf_keys if not seeder.is_cusip_row({"ticker": k})]
    bd_delta = sum(1 for k in would_write if k.startswith(seeder.CUSIP_KEY_PREFIX) and k not in bd_keys)
    print("CUSIP-GUARD etf_rows=%d cusip_rows=%d bd_rows=%d bd_delta_from_cusip=%d"
          % (len(etf_keys), cusip_rows, bd_rows, bd_delta))

    with open(CENSUS, encoding="utf-8") as fh:
        planned = json.load(fh)["rows"]
    would_copy = sum(1 for r in planned if not seeder.is_cusip_row(r))
    print("CUSIP-GUARD-PLANNED planned=%d would_copy_to_bd=%d" % (len(planned), would_copy))
    # negative control (stderr): with the guard removed, every CUSIP:-keyed planned row would copy
    unguarded = sum(1 for r in planned if r.get("ticker", "").startswith(seeder.CUSIP_KEY_PREFIX))
    sys.stderr.write("control: unguarded planned copy would be %d" % unguarded + chr(10))
    return 0 if (bd_delta == 0 and would_copy == 0) else 1


if __name__ == "__main__":
    sys.exit(main())
