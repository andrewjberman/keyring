#!/usr/bin/env python3
"""e91_shipped_check.py -- MDPF_SECCLASS SC-e-91 deploy check: the served BD gold C_06 equals the repo bytes of the drained code and is not
the rollback object. READ-ONLY (head-object). Run from the repo root being graded (box/dell1 at or after e270f70be4).

Prints  E91-SHIPPED ok=<bool> c06=<served|repo|MATCH|DIFF> control=<MATCH|MISMATCH> d04=<same|MOVED> d03=<same|MOVED>
ok is True when the served C_06 ETag equals the repo file's md5 AND differs from the rollback ETag (8e1b350f..., the object served at the
2026-10-12T06:18:21Z ADVI FB-f-9 mode move, VersionId 5xAeM.OWYUSxd7gHYSF6SKmR.ZTmo.PP); control is the positive control that the repo md5
differs from that rollback ETag (else the check cannot discriminate). d04 and d03 are INFORMATIONAL here (the act names one key): each
reads `same` when its served ETag equals its repo md5 (as at 2026-10-12T06:18Z), `MOVED` otherwise; the order's watch set is the gate.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
BUCKET = "opal-data-bd"
GOLD = "data/black_diamond/scripts/gold/"
C06 = "C_06.client_mix_timeseries.py"
ROLLBACK_ETAG = "8e1b350fc55607bddd1ac84329cb1a98"


def head(key):
    aws = str(ROOT / ".tools" / ("aws.cmd" if sys.platform == "win32" else "aws"))
    out = subprocess.run([aws, "s3api", "head-object", "--bucket", BUCKET, "--key", key, "--output", "json"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        return None
    return json.loads(out.stdout)["ETag"].strip('"')


def md5(name):
    return hashlib.md5((ROOT / GOLD / name).read_bytes()).hexdigest()


def main():
    repo = md5(C06)
    served = head("code/gold/" + C06)
    control_ok = repo != ROLLBACK_ETAG
    match = served is not None and served == repo and served != ROLLBACK_ETAG
    d04 = "same" if head("code/gold/D_04.client_portal_summary.py") == md5("D_04.client_portal_summary.py") else "MOVED"
    d03 = "same" if head("code/gold/D_03.composition_artifacts.py") == md5("D_03.composition_artifacts.py") else "MOVED"
    ok = bool(match and control_ok)
    print(f"E91-SHIPPED ok={ok} c06={(served or 'NONE')[:8]}|{repo[:8]}|{'MATCH' if match else 'DIFF'} "
          f"control={'MATCH' if control_ok else 'MISMATCH'} d04={d04} d03={d03}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
