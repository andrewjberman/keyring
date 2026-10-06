"""SC-e-20 amendment 2 before/after read: the Black Diamond (49 Financial) client mix and firm composition with
`multi_asset` in the class lists.

READ ONLY. Writes nothing to S3 or DynamoDB (every call below is a get/list/read; the C_06 and D_03 write helpers are never
called). Two parts, both run in process on the EDITED code:

  1. C_06.process_date on the latest s3://opal-data-bd/gold/canonical/holdings/<date>.parquet, for every relationship
     that holds a multi_asset position. BEFORE = the live gold/entities/clients point (the client entity JSON) for the
     partition date, or its latest point, read only; AFTER = the edited code's published mix. Prints shares and sums.
  2. D_03's own steps 1-5 (holdings_lots, ghost exclusion, AP gate, classify_series, canonical AUA, _build_composition)
     for the firm scope. BEFORE = the live gold/views/firm_composition.json total and class sum; AFTER = the edited
     builder's class sum against its total, and the gap.

Last line: BD-MIX-CHECK ok=<True|False> holders=<n> after_sums_to_1=<n> composition_gap_after=<dollars>
ok=True only if every holder's after-sum is within 0.001 of 1, every holder holding multi_asset in the raw partition is
published, the after composition class sum equals its total within $0.01, and every input was read. An unreadable input
prints ERROR and exits 2; ok=True is never printed on a partial read.

    python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/bd_mix_multi_asset_check.py
"""
from __future__ import annotations

import importlib.util
import json
import sys
from io import BytesIO
from pathlib import Path

import pandas as pd

TOL = 0.001
COMP_TOL = 0.01


def _gold_dir() -> Path:
    for parent in Path(__file__).resolve().parents:
        cand = parent / "data" / "black_diamond" / "scripts" / "gold"
        if cand.is_dir():
            return cand
    raise SystemExit("ERROR: data/black_diamond/scripts/gold not found above " + __file__)


def _load(gold: Path, name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, gold / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _fail(msg: str):
    print("ERROR: " + msg)
    print("BD-MIX-CHECK ok=False holders=0 after_sums_to_1=0 composition_gap_after=nan  (INPUT UNREADABLE: no verdict)")
    raise SystemExit(2)


def _fmt(mix: dict) -> str:
    return ", ".join("%s=%.6f" % (k, v) for k, v in mix.items() if v)


def _before_point(c06, rel_id: str, date: str):
    """The live published mix point (read only): the point for `date`, else the latest one. (point_date, shares) or (None, why)."""
    try:
        body = c06.s3.get_object(Bucket=c06.S3_BUCKET, Key=c06.client_timeseries_key(rel_id))["Body"].read()
    except Exception as exc:  # a failed read is reported, never read as an empty mix
        return None, "READ-FAILED %s" % type(exc).__name__
    entries = json.loads(body).get("mix", [])
    if not entries:
        return None, "NO-MIX-ENTRIES"
    pick = next((e for e in entries if e.get("date") == date), None) or sorted(entries, key=lambda e: e.get("date", ""))[-1]
    return pick.get("date"), {k: v for k, v in pick.items() if k not in ("date", "total_mv") and isinstance(v, (int, float))}


def part_one(gold: Path):
    c06 = _load(gold, "bd_c06_check", "C_06.client_mix_timeseries.py")
    print("C_06 classes emitted by the edited code:", c06.MIX_ASSET_CLASSES)
    keys = c06._list_positions_cube_keys()
    if not keys:
        _fail("no partitions under s3://%s/%s" % (c06.S3_BUCKET, c06.CANONICAL_HOLDINGS_PREFIX))
    key = keys[-1]
    date = c06._parse_date(key)
    print("partition: s3://%s/%s  (latest of %d)" % (c06.S3_BUCKET, key, len(keys)))
    (acct_rel_dict, _u, ap_last_seen, ins_ids, ins_days, ghost_ids, _adv, _cp) = c06.load_static_tables()
    pos = pd.read_parquet(BytesIO(c06._get_s3().get_object(Bucket=c06.S3_BUCKET, Key=key)["Body"].read()))
    # process_date reads the partition from this cache (same bytes it would fetch itself); it works on a copy.
    c06._shared["cube_cache"] = {key: pos.copy()}
    result = c06.process_date(key, date, None, acct_rel_dict, ap_last_seen, verbose=True,
                              insurance_account_ids=ins_ids, insurance_gate_days=ins_days, ghost_account_ids=ghost_ids)
    print("relationships published for the partition: %d" % len(result))

    # Raw cross-check: every relationship holding a multi_asset position in the partition, before any gate.
    raw = pos.copy()
    raw["account_id"] = raw["account_id"].astype(str)
    raw["relationship_id"] = raw["account_id"].map(acct_rel_dict)
    raw = raw.dropna(subset=["relationship_id"])
    raw = raw[raw["market_value"] > 0]
    cls = c06.classify_series(raw["ticker"], raw["asset_name"])
    raw_holders = sorted(set(raw.loc[cls["asset_class"] == "multi_asset", "relationship_id"]))
    pub_holders = sorted(r for r, v in result.items() if v["mix"].get("multi_asset", 0.0) > 0)
    unpublished = [r for r in raw_holders if r not in result]
    print("raw partition: %d relationship(s) hold a multi_asset position; published with a multi_asset share: %d; "
          "holding multi_asset but NOT published (gated or skipped): %d" % (len(raw_holders), len(pub_holders), len(unpublished)))
    for r in unpublished:
        print("   NOT PUBLISHED: %s" % r)

    sums_ok = 0
    for rel_id in pub_holders:
        bdate, before = _before_point(c06, rel_id, date)
        after = result[rel_id]["mix"]
        total = sum(after.values())
        print("-- %s" % rel_id)
        if bdate is None:
            print("   BEFORE: n/a (%s)" % before)
        else:
            print("   BEFORE (%s) shares: %s" % (bdate, _fmt(before)))
            print("   BEFORE sum   : %.6f" % sum(before.values()))
        print("   AFTER  shares: %s" % _fmt(after))
        print("   AFTER  sum   : %.6f   multi_asset share: %.6f" % (total, after.get("multi_asset", 0.0)))
        sums_ok += abs(total - 1.0) <= TOL
    return len(pub_holders), sums_ok, len(unpublished)


def part_two(gold: Path):
    d03 = _load(gold, "bd_d03_check", "D_03.composition_artifacts.py")
    from lib.exclusions import apply_ap_gate, apply_ghost_exclusion, build_ap_last_seen, load_ghost_account_ids, load_insurance_config
    print("D_03 labels in the edited code:", list(d03._ASSET_CLASS_LABELS))
    # BEFORE: the live served firm composition (read only)
    try:
        live = json.loads(d03.s3.get_object(Bucket=d03.BUCKET, Key=d03.FIRM_COMPOSITION)["Body"].read())
    except Exception as exc:
        _fail("cannot read live s3://%s/%s (%s)" % (d03.BUCKET, d03.FIRM_COMPOSITION, type(exc).__name__))
    live_total = float(live["total_market_value"])
    live_sum = sum(float(m["market_value"]) for m in live["mix"])
    print("BEFORE live %s data_as_of=%s generated_at=%s" % (d03.FIRM_COMPOSITION, live.get("data_as_of"), live.get("generated_at")))
    print("   live total_market_value = %.2f   live class sum = %.2f   live gap = %.2f   classes: %s"
          % (live_total, live_sum, live_total - live_sum, [m["asset_class"] for m in live["mix"]]))

    # AFTER: D_03's own steps 1-5, in process, nothing written
    hkey = d03._find_latest_holdings_lots()
    if not hkey:
        _fail("no holdings_lots snapshot")
    print("holdings_lots: s3://%s/%s" % (d03.BUCKET, hkey))
    lots = d03._read_parquet(hkey, columns=["account_id", "relationship_id", "ticker", "asset_name", "cusip", "market_value", "is_open"])
    lots = lots[lots["is_open"].fillna(False)].copy()
    data_as_of = hkey.rsplit("/", 1)[-1].replace(".parquet", "")
    lots = apply_ghost_exclusion(lots, load_ghost_account_ids(), label="bd_mix_check")
    ap_last_seen = build_ap_last_seen(d03.s3, d03.BUCKET)
    ins_ids, ins_days = load_insurance_config()
    lots = apply_ap_gate(lots, ap_last_seen, data_as_of, insurance_ids=ins_ids, insurance_gate_days=ins_days, label="bd_mix_check")
    # classify_series is a pure per-row function of (ticker, asset_name, cusip) with one DynamoDB read per unresolved row, so it
    # is called once per DISTINCT triple here and mapped back to the 500k rows: the same per-row result, minutes instead of hours.
    keys = ["ticker", "asset_name", "cusip"]
    gid = lots.groupby(keys, dropna=False, sort=False).ngroup()
    first = ~gid.duplicated()
    rep = lots[first]
    cls = d03.classify_series(rep["ticker"], rep["asset_name"], rep["cusip"])
    cls.index = gid[first].values
    print("D_03 classify_series: %d distinct (ticker, name, cusip) triples over %d open lots" % (len(rep), len(lots)))
    for c in cls.columns:
        lots[c] = gid.map(cls[c])
    rel_aua, firm_aua = d03._load_canonical_aua_lookup()
    if firm_aua is None:
        _fail("account_performance unreadable: the canonical AUA the composition scales to")
    comp = d03._build_composition(lots, scope={"firm_id": d03.FIRM_ID}, data_as_of=data_as_of, canonical_aua=firm_aua)
    if comp is None:
        _fail("edited _build_composition returned empty")
    after_total = float(comp["total_market_value"])
    after_sum = sum(float(m["market_value"]) for m in comp["mix"])
    gap = after_total - after_sum
    print("AFTER (edited D_03, data_as_of=%s): total_market_value = %.2f   class sum = %.2f   gap = %.2f"
          % (data_as_of, after_total, after_sum, gap))
    for m in comp["mix"]:
        print("   %-13s %-13s %18.2f  pct=%.6f" % (m["asset_class"], m["label"], m["market_value"], m["pct"]))
    return gap


def main() -> int:
    gold = _gold_dir()
    sys.path.insert(0, str(gold))
    try:
        holders, sums_ok, unpublished = part_one(gold)
    except SystemExit:
        raise
    except Exception as exc:
        _fail("C_06 part could not complete: %s: %s" % (type(exc).__name__, exc))
    try:
        gap = part_two(gold)
    except SystemExit:
        raise
    except Exception as exc:
        _fail("D_03 part could not complete: %s: %s" % (type(exc).__name__, exc))
    ok = holders > 0 and sums_ok == holders and unpublished == 0 and abs(gap) <= COMP_TOL
    print("BD-MIX-CHECK ok=%s holders=%d after_sums_to_1=%d composition_gap_after=%.2f" % (ok, holders, sums_ok, gap))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
