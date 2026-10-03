#!/usr/bin/env python3
"""s18_restore_set.py -- MDPF_SECCLASS-S18 (CTO batch 213 item 1): the per-key restore list for the served keys the 2026-10-03
04:00Z BD gold run wrote (as_of 10-01), each with the VersionId it held before 04:00Z.

Input: the keys under opal-data-bd platinum/ and gold/ whose current LastModified falls in the run window (04:00:00Z-06:05:00Z),
re-listed here. SERVED keys = platinum/** (the serving tier) + gold/views/** + gold/artifacts/** + gold/firm_mix_views.json +
gold/firm_mix_views_daily.json + gold/firm_composition.json. For each served key, list_object_versions gives the run's version
(newest in the window) and the newest version strictly before the window (the restore target); a key whose first version is in
the window is CREATED (restoring it means deleting it -- Andrew's word only, listed separately).
Read-only. Writes R9_CHECKS/S18_RESTORE_SET_20261003.tsv and prints the counts.
"""
from __future__ import annotations

import datetime
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import boto3
from botocore.config import Config

BUCKET = "opal-data-bd"
LO = datetime.datetime(2026, 10, 3, 4, 0, 0, tzinfo=datetime.timezone.utc)
HI = datetime.datetime(2026, 10, 3, 6, 5, 0, tzinfo=datetime.timezone.utc)
SERVED_PREFIXES = ("platinum/", "gold/views/", "gold/artifacts/")
SERVED_KEYS = {"gold/firm_mix_views.json", "gold/firm_mix_views_daily.json", "gold/firm_composition.json"}
OUT = Path(__file__).resolve().parent / "S18_RESTORE_SET_20261003.tsv"
s3 = boto3.client("s3", region_name="us-east-1", config=Config(retries={"max_attempts": 8, "mode": "adaptive"}))


def window_keys():
    keys = []
    for pre in ("platinum/", "gold/"):
        tok = None
        while True:
            kw = {"Bucket": BUCKET, "Prefix": pre}
            if tok:
                kw["ContinuationToken"] = tok
            r = s3.list_objects_v2(**kw)
            for o in r.get("Contents", []):
                k = o["Key"]
                if LO <= o["LastModified"] <= HI and (k.startswith(SERVED_PREFIXES) or k in SERVED_KEYS):
                    keys.append(k)
            if not r.get("IsTruncated"):
                break
            tok = r["NextContinuationToken"]
    return keys


def versions_of(key):
    vs, kw = [], {"Bucket": BUCKET, "Prefix": key}
    while True:
        r = s3.list_object_versions(**kw)
        vs += [v for v in r.get("Versions", []) if v["Key"] == key]
        if not r.get("IsTruncated") or len(vs) > 40:
            break
        kw.update(KeyMarker=r["NextKeyMarker"], VersionIdMarker=r["NextVersionIdMarker"])
    vs.sort(key=lambda v: v["LastModified"], reverse=True)
    run = next((v for v in vs if LO <= v["LastModified"] <= HI), None)
    prior = next((v for v in vs if v["LastModified"] < LO), None)
    return key, run, prior


def main() -> int:
    keys = window_keys()
    print("served keys written in the window:", len(keys), flush=True)
    with ThreadPoolExecutor(8) as pool:
        rows = list(pool.map(versions_of, keys))
    created = [k for k, run, prior in rows if prior is None]
    with OUT.open("w", encoding="utf-8", newline="\n") as f:
        f.write("# S18 restore set: key, restore-to VersionId (pre-04:00Z), its LastModified, the run's VersionId, its LastModified\n")
        for k, run, prior in sorted(rows):
            f.write("\t".join([k, prior["VersionId"] if prior else "CREATED-IN-RUN",
                               prior["LastModified"].isoformat() if prior else "-",
                               run["VersionId"] if run else "-", run["LastModified"].isoformat() if run else "-"]) + "\n")
    print("restore by copy-object (a prior version exists):", len(rows) - len(created))
    print("created in the run (no prior version; restoring = delete, Andrew's word):", len(created))
    for k in created[:20]:
        print("   CREATED", k)
    print("WROTE", OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
