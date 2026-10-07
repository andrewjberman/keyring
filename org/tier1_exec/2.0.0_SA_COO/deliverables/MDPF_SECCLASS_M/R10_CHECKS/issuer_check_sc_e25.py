#!/usr/bin/env python3
"""issuer_check_sc_e25.py -- MDPF_SECCLASS round 8 issuer check for cell SC-e-25 (FWD-12, C-SECTOR measurement).

Modes (one verdict token each; run from the repo root; read-only against S3):
  values  -- the newest M/SECTOR_INDUSTRY_GROUP_VALUES_*.json carries both sources (the Bloomberg characteristics file and
             the served ETF holding artifact), each with its S3 key, a row denominator > 0 and the distinct values of the
             sector and the industry group; and the characteristics source's two value sets EQUAL a fresh read of the same
             partition's file (the seam probe against the real input). Prints SC-E25-VALUES ok=True|False.
  record  -- the newest M/C_SECTOR_FOUR_POSTULATE_RECORD_*.md carries, for each of the two attributes, the four postulates
             (i) MECE, (ii) SAME GRAIN, (iii) INTENT COHERENCE, (iv) STATE COHERENCE, and a token census line with its
             denominator. Prints SC-E25-RECORD ok=True|False.

Expected JSON shape (the worker's deliverable):
  {"measured_at": "...", "sources": {
      "characteristics": {"key": "s3://opal-data-etfs/bbg/<date>/characteristics.parquet", "rows": N,
                          "sector_values": [...], "industry_group_values": [...]},
      "served_holding":  {"key": "s3://opal-data-etfs/gold/holding/date=<date>/holding.parquet", "rows": N,
                          "sector_values": [...], "industry_group_values": [...]}}}
"""
import glob
import io
import json
import os
import re
import sys

M = os.path.join("org", "tier1_exec", "2.0.0_SA_COO", "deliverables", "MDPF_SECCLASS_M")


def newest(pattern):
    hits = sorted(glob.glob(os.path.join(M, pattern)))
    return hits[-1] if hits else None


def check_values():
    path = newest("SECTOR_INDUSTRY_GROUP_VALUES_*.json")
    if not path:
        return False, "no SECTOR_INDUSTRY_GROUP_VALUES_*.json"
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    src = doc.get("sources", {})
    for name in ("characteristics", "served_holding"):
        s = src.get(name)
        if not s:
            return False, f"source {name} missing"
        if not str(s.get("key", "")).startswith("s3://"):
            return False, f"source {name} has no s3 key"
        if not isinstance(s.get("rows"), int) or s["rows"] <= 0:
            return False, f"source {name} has no row denominator"
        for f in ("sector_values", "industry_group_values"):
            if not isinstance(s.get(f), list) or not s[f]:
                return False, f"source {name} field {f} empty"
    key = src["characteristics"]["key"]
    m = re.match(r"s3://([^/]+)/(.+)$", key)
    if not m:
        return False, f"bad characteristics key {key}"
    import boto3
    import pandas as pd
    body = boto3.client("s3", region_name="us-east-1").get_object(Bucket=m.group(1), Key=m.group(2))["Body"].read()
    df = pd.read_parquet(io.BytesIO(body))
    live_sector = sorted(set(df["GICS_SECTOR_NAME"].dropna().astype(str)))
    live_ig = sorted(set(df["GICS_INDUSTRY_GROUP_NAME"].dropna().astype(str)))
    if sorted(src["characteristics"]["sector_values"]) != live_sector:
        return False, f"sector values differ from a fresh read of {key}"
    if sorted(src["characteristics"]["industry_group_values"]) != live_ig:
        return False, f"industry group values differ from a fresh read of {key}"
    if src["characteristics"]["rows"] != len(df):
        return False, f'characteristics rows {src["characteristics"]["rows"]!s} != fresh read {len(df)}'
    return True, f"file={os.path.basename(path)!s} sector={len(live_sector)} industry_group={len(live_ig)} rows={len(df)}"


def check_record():
    path = newest("C_SECTOR_FOUR_POSTULATE_RECORD_*.md")
    if not path:
        return False, "no C_SECTOR_FOUR_POSTULATE_RECORD_*.md"
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    low = text.lower()
    for marker in ("mece", "same grain", "intent coherence", "state coherence"):
        if low.count(marker) < 2:
            return False, f"postulate '{marker}' not stated for both attributes"
    if not re.search(r"token census.*denominator", low) and not re.search(r"denominator.*token census", low):
        return False, "no token census line with its denominator"
    if "industry" not in low or "sector" not in low:
        return False, "both attributes are not named"
    return True, f"file={os.path.basename(path)}"


def main(argv):
    mode = argv[0] if argv else ""
    if mode == "values":
        ok, why = check_values()
        print(f"SC-E25-VALUES ok={ok} {why}")
    elif mode == "record":
        ok, why = check_record()
        print(f"SC-E25-RECORD ok={ok} {why}")
    else:
        print("usage: issuer_check_sc_e25.py values|record")
        return 2
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
