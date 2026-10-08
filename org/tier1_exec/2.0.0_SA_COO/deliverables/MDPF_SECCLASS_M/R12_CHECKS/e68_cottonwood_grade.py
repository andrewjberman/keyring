"""e68_cottonwood_grade.py -- MDPF_SECCLASS SC-e-68 ledger leg L2: grade Cottonwood's first mix rebuild after the CASH row write.

READ-ONLY (s3 get/list on opal-data-cot). The rule is CTO e68 half amendment 3 @555db9c729 (row MDPF_SECCLASS-D1-S6):
  (a) platinum/firm/mix_summary.json was rebuilt after the write (LastModified > 2026-10-08T03:12:55Z);
  (b) in every client composition REBUILT after the write that lists key CASH, its asset_class is cash (no fixed_income CASH line);
      compositions not rebuilt are counted apart and never graded;
  (c) the sum of mix_summary.mix[*].market_value equals composition.total_market_value within USD 1.00.
A miss on (b) or (c) is a same-day rollback (cash_row_write.py --rollback CASH_ROW_SNAPSHOT_20261008.json --write).
Prints  E68-GRADE verdict=<PASS|ROLLBACK|NOT-YET> ...   The verdict is read from stdout, never the exit code.
"""
import concurrent.futures as cf
import datetime as dt
import json
import sys

import boto3

BUCKET = "opal-data-cot"
FIRM_KEY = "platinum/firm/mix_summary.json"
WRITE_AT = dt.datetime(2026, 10, 8, 3, 12, 55, tzinfo=dt.timezone.utc)


def cash_lines(doc):
    out = []

    def walk(x):
        if isinstance(x, dict):
            if x.get("key") == "CASH":
                out.append((x.get("asset_class"), x.get("market_value") or 0))
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(doc)
    return out


def main():
    s3 = boto3.client("s3", region_name="us-east-1")
    head = s3.head_object(Bucket=BUCKET, Key=FIRM_KEY)
    firm_lm = head["LastModified"]
    firm = json.loads(s3.get_object(Bucket=BUCKET, Key=FIRM_KEY)["Body"].read())
    rebuilt = firm_lm > WRITE_AT
    mix_sum = sum((v or {}).get("market_value") or 0 for v in firm.get("mix", {}).values())
    total = (firm.get("composition") or {}).get("total_market_value")
    c_ok = total is not None and abs(mix_sum - total) <= 1.00

    objs = []
    for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix="platinum/clients/"):
        objs += [o for o in pg.get("Contents", []) if o["Key"].endswith("/composition.json")]
    fresh = [o for o in objs if o["LastModified"] > WRITE_AT]

    def read(o):
        return cash_lines(json.loads(s3.get_object(Bucket=BUCKET, Key=o["Key"])["Body"].read()))
    with cf.ThreadPoolExecutor(16) as ex:
        lines = list(ex.map(read, fresh))
    listing = [ln for ln in lines if ln]
    bad = sum(1 for ln in listing if any(c != "cash" for c, _ in ln))
    cash_mv = sum(m for ln in listing for c, m in ln if c == "cash")
    b_ok = bad == 0

    if not rebuilt:
        verdict = "NOT-YET"
    elif b_ok and c_ok:
        verdict = "PASS"
    else:
        verdict = "ROLLBACK"
    print(f"E68-GRADE verdict={verdict} firm_lastmodified={firm_lm.isoformat()} version={head.get('VersionId')} "
          f"data_as_of={firm.get('data_as_of')} (a)rebuilt={rebuilt} (b)fresh_compositions={len(fresh)} of {len(objs)} "
          f"listing_CASH={len(listing)} non_cash={bad} cash_mv={cash_mv:.2f} (c)mix_sum={mix_sum:.2f} total={total} "
          f"c_ok={c_ok}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
