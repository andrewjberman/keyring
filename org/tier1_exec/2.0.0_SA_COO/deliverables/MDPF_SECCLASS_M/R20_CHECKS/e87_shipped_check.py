#!/usr/bin/env python3
"""e87_shipped_check.py -- MDPF_SECCLASS SC-e-87 deploy check: the three served BD gold scripts equal the repo bytes and none is a rollback
object. READ-ONLY (head-object). Run from the repo root being graded.

Prints  E87-SHIPPED ok=<bool> d04=<served|repo|MATCH|DIFF> c06=<...> d03=<...> control=<MATCH|MISMATCH> lib=<unmoved|MOVED>
ok is True when each served ETag equals the repo file's md5 AND differs from that key's pre-ship ETag (the rollback target); control is
the positive control that each repo md5 differs from its rollback ETag (else the check cannot discriminate); lib confirms the SC-e-79 lib
did not move (ETag eb9bb852...).
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
BUCKET = "opal-data-bd"
GOLD = "data/black_diamond/scripts/gold/"
ROLLBACK = {  # pre-ship ETag (md5), VersionId in the half request's rollback table
    "D_04.client_portal_summary.py": "23d2f2ae5797834638bbda5b9e5eb584",
    "C_06.client_mix_timeseries.py": "d7eb83b655b63143c24552bdfff197ad",
    "D_03.composition_artifacts.py": "84f9bf8e9ececc0712b0a6e3f67694f4",
}
LIB_KEY, LIB_ETAG = "code/gold/lib/etf_classifier.py", "eb9bb85208c96fa15ede01cf3618782d"


def head(key):
    aws = str(ROOT / ".tools" / ("aws.cmd" if sys.platform == "win32" else "aws"))
    out = subprocess.run([aws, "s3api", "head-object", "--bucket", BUCKET, "--key", key, "--output", "json"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        return None
    return json.loads(out.stdout)["ETag"].strip('"')


def main():
    verdicts, ok_all, control_ok = {}, True, True
    for name, rb in ROLLBACK.items():
        repo = hashlib.md5((ROOT / GOLD / name).read_bytes()).hexdigest()
        served = head("code/gold/" + name)
        control_ok = control_ok and repo != rb
        match = served is not None and served == repo and served != rb
        ok_all = ok_all and match
        verdicts[name.split(".")[0].split("_")[0] + name.split(".")[0].split("_")[1]] = (
            f"{(served or 'NONE')[:8]}|{repo[:8]}|{'MATCH' if match else 'DIFF'}")
    lib = head(LIB_KEY)
    lib_ok = lib == LIB_ETAG
    ok = ok_all and control_ok and lib_ok
    v = verdicts
    print(f"E87-SHIPPED ok={ok} d04={v['D04']} c06={v['C06']} d03={v['D03']} control={'MATCH' if control_ok else 'MISMATCH'} "
          f"lib={'unmoved' if lib_ok else 'MOVED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
