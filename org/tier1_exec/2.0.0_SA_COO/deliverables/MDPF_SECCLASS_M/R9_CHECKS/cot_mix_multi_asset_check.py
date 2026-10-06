"""SC-e-20 before/after read: the Cottonwood client mix with `multi_asset` in the class list.

READ ONLY. Reads s3://opal-data-cot/gold/canonical/holdings/2026-10-05.parquet, the accounts dimension and the
ghost-account list the way C_06 does (C_06.load_static_tables), runs C_06.process_date in process (it writes nothing)
for four relationships, and prints per client the BEFORE shares (the live gold/entities/clients/<id>.json point for
2026-10-05, read only) and the AFTER shares from the edited code. Writes nothing to S3 or DynamoDB.

    python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/cot_mix_multi_asset_check.py
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

DATE = "2026-10-05"
CLIENTS = ["z09305578", "z09305621", "z09305679", "z09305703"]
TOL = 0.001


def _gold_dir() -> Path:
    for parent in Path(__file__).resolve().parents:
        cand = parent / "data" / "cot" / "scripts" / "gold"
        if cand.is_dir():
            return cand
    raise SystemExit("ERROR: data/cot/scripts/gold not found above " + __file__)


def _load_c06(gold: Path):
    sys.path.insert(0, str(gold))
    spec = importlib.util.spec_from_file_location("c06_check", gold / "C_06.client_mix_timeseries.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _before(c06, rel_id: str):
    """The live published point for DATE (read only), or None if the file or the date is absent."""
    from lib.s3_layout import client_timeseries_key
    try:
        body = c06.s3.get_object(Bucket=c06.S3_BUCKET, Key=client_timeseries_key(rel_id))["Body"].read()
    except Exception as exc:  # a failed read is reported, never read as an empty mix
        return None, "READ-FAILED %s" % type(exc).__name__
    for entry in json.loads(body).get("mix", []):
        if entry.get("date") == DATE:
            return {k: v for k, v in entry.items() if k not in ("date", "total_mv")}, ""
    return None, "NO-POINT-FOR-" + DATE


def _fmt(mix: dict) -> str:
    return ", ".join("%s=%.6f" % (k, v) for k, v in mix.items() if v)


def main() -> int:
    gold = _gold_dir()
    c06 = _load_c06(gold)
    print("classes emitted by the edited code:", c06.MIX_ASSET_CLASSES)
    acct_rel_dict, _unused, ghost_ids, _adv = c06.load_static_tables()
    key = c06.CANONICAL_HOLDINGS_PREFIX + DATE + ".parquet"
    print("partition: s3://%s/%s" % (c06.S3_BUCKET, key))
    result = c06.process_date(key, DATE, None, acct_rel_dict, verbose=True, ghost_account_ids=ghost_ids)
    print("relationships published for the partition: %d" % len(result))

    sums_ok = 0
    ma_present = 0
    for rel_id in CLIENTS:
        before, why = _before(c06, rel_id)
        after = (result.get(rel_id) or {}).get("mix")
        print("-- %s" % rel_id)
        if before is None:
            print("   BEFORE: n/a (%s)" % why)
        else:
            print("   BEFORE shares: %s" % _fmt(before))
            print("   BEFORE sum   : %.6f" % sum(before.get(c, 0.0) for c in before))
        if after is None:
            print("   AFTER : NOT PUBLISHED (client skipped or absent)")
            continue
        total = sum(after.values())
        print("   AFTER  shares: %s" % _fmt(after))
        print("   AFTER  sum   : %.6f   multi_asset share: %.6f" % (total, after.get("multi_asset", 0.0)))
        sums_ok += abs(total - 1.0) <= TOL
        ma_present += after.get("multi_asset", 0.0) > 0
    print("COT-MIX-CHECK clients=%d after_sums_to_1=%d multi_asset_share_present=%d"
          % (len(CLIENTS), sums_ok, ma_present))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
