#!/usr/bin/env python3
"""s18_restore.py -- MDPF_SECCLASS-S18 leg C: restore each served key in S18_RESTORE_SET_20261003.tsv to its pre-04:00Z version.

Per key (CREATED-IN-RUN rows skipped -- a restore there is a delete, Andrew's word only):
  1. head-object: the key's CURRENT VersionId must still be the run's VersionId in the TSV. If anything wrote the key after the
     run, the key is REFUSED (never overwritten blind) and reported.
  2. --write only: copy-object from the restore-to VersionId onto the key (metadata COPY), then head-object read-back: the new
     current version's ETag equals the restore-to version's ETag.
Default is a DRY RUN (step 1 only). Prints counts; writes R9_CHECKS/S18_RESTORE_RESULT_<mode>.tsv (key, state, new VersionId).
Rollback: the same TSV's run VersionId column, copied back the same way.
"""
from __future__ import annotations

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import boto3
from botocore.config import Config

BUCKET = "opal-data-bd"
HERE = Path(__file__).resolve().parent
SET = HERE / "S18_RESTORE_SET_20261003.tsv"
s3 = boto3.client("s3", region_name="us-east-1", config=Config(retries={"max_attempts": 10, "mode": "adaptive"}))


def rows():
    for line in SET.read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or not line.strip():
            continue
        key, restore_to, _rt_at, run_ver, _run_at = line.split("\t")
        yield key, restore_to, run_ver


def one(args):
    key, restore_to, run_ver, write = args
    if restore_to == "CREATED-IN-RUN":
        return key, "SKIP-CREATED", "-"
    cur = s3.head_object(Bucket=BUCKET, Key=key)
    if cur["VersionId"] != run_ver:
        return key, "REFUSED-REWRITTEN", cur["VersionId"]
    if not write:
        return key, "WOULD-RESTORE", "-"
    target = s3.head_object(Bucket=BUCKET, Key=key, VersionId=restore_to)
    r = s3.copy_object(Bucket=BUCKET, Key=key, CopySource={"Bucket": BUCKET, "Key": key, "VersionId": restore_to},
                       MetadataDirective="COPY")
    back = s3.head_object(Bucket=BUCKET, Key=key)
    ok = back["VersionId"] == r["VersionId"] and back["ETag"] == target["ETag"]
    return key, ("RESTORED" if ok else "READBACK-MISMATCH"), r["VersionId"]


def main(write: bool) -> int:
    work = [(k, rt, rv, write) for k, rt, rv in rows()]
    with ThreadPoolExecutor(8) as pool:
        res = list(pool.map(one, work))
    counts = {}
    for _, state, _ in res:
        counts[state] = counts.get(state, 0) + 1
    out = HERE / ("S18_RESTORE_RESULT_%s.tsv" % ("WRITE" if write else "DRYRUN"))
    out.write_text("".join("%s\t%s\t%s\n" % r for r in sorted(res)), encoding="utf-8")
    print(("WRITE" if write else "DRY RUN"), "keys", len(res), counts)
    for k, state, v in res:
        if state in ("REFUSED-REWRITTEN", "READBACK-MISMATCH"):
            print("  ", state, k, v)
    print("WROTE", out)
    bad = counts.get("REFUSED-REWRITTEN", 0) + counts.get("READBACK-MISMATCH", 0)
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    sys.exit(main(ap.parse_args().write))
