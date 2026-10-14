#!/usr/bin/env python3
"""e102_shipped_check.py -- MDPF_SECCLASS SC-e-102 deploy check: the served BD gold C_06 equals the repo bytes of the drained code (sorted-keys
writer) and is not the rollback object; D_03, D_04 and gold_dispatch.sh are unmoved. READ-ONLY (head-object, and one get-object of the served
mix daily summary for the informational sorted-keys read). Run from the repo root being graded (box/dell1 at or after b5f6b816a4).

Prints  E102-SHIPPED ok=<bool> c06=<served|repo|MATCH|DIFF> control=<MATCH|MISMATCH> dispatch=<same|MOVED> d03=<same|MOVED> d04=<same|MOVED> mds_sorted=<bool>
ok is True when the served C_06 ETag equals the repo md5 AND differs from the rollback ETag (f847d8d105025ffbee94b1aa5092faf6, the 2026-10-13T06:22:23Z
SC-e-97 ship) AND gold_dispatch.sh, D_03 and D_04 still read their repo md5s (the act names one key; any other code key moving is a STOP). control is the
positive control that the repo md5 differs from the rollback ETag (else the check cannot discriminate). mds_sorted is INFORMATIONAL here: the served
mix daily summary's body equals its own sorted-key dump (it reads False until a C_06 run has written it after the ship; leg Q' grades it).
"""
import hashlib
import importlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
BUCKET = "opal-data-bd"
GOLD = "data/black_diamond/scripts/gold/"
C06 = "C_06.client_mix_timeseries.py"
D04 = "D_04.client_portal_summary.py"
D03 = "D_03.composition_artifacts.py"
DISPATCH = "gold_dispatch.sh"
ROLLBACK_C06 = "f847d8d105025ffbee94b1aa5092faf6"
K_MDS = "gold/views/mix_daily_summary.json"


def aws(args):
    exe = str(ROOT / ".tools" / ("aws.cmd" if sys.platform == "win32" else "aws"))
    return subprocess.run([exe] + args, capture_output=True)


def head(key):
    out = aws(["s3api", "head-object", "--bucket", BUCKET, "--key", key, "--output", "json"])
    if out.returncode != 0:
        return None
    return json.loads(out.stdout)["ETag"].strip('"')


def md5(name):
    return hashlib.md5((ROOT / GOLD / name).read_bytes()).hexdigest()


def mds_sorted():
    sys.path.insert(0, str(ROOT / GOLD))
    pd = importlib.import_module("lib.platinum_dest")
    bucket, key = pd.source(K_MDS, "canonical")
    out = aws(["s3api", "get-object", "--bucket", bucket, "--key", key, "--output", "json", str(ROOT / ".scratch_e102_mds.json")])
    if out.returncode != 0:
        return False
    p = ROOT / ".scratch_e102_mds.json"
    try:
        body = p.read_bytes()
        again = json.dumps(json.loads(body), sort_keys=True, separators=(",", ":")).encode("utf-8")
        return hashlib.md5(body).hexdigest() == hashlib.md5(again).hexdigest()
    finally:
        p.unlink(missing_ok=True)


def main():
    r06 = md5(C06)
    s06 = head("code/gold/" + C06)
    control_ok = r06 != ROLLBACK_C06
    m06 = s06 is not None and s06 == r06 and s06 != ROLLBACK_C06
    disp = "same" if head("code/gold/" + DISPATCH) == md5(DISPATCH) else "MOVED"
    d03 = "same" if head("code/gold/" + D03) == md5(D03) else "MOVED"
    d04 = "same" if head("code/gold/" + D04) == md5(D04) else "MOVED"
    ok = bool(m06 and control_ok and disp == "same" and d03 == "same" and d04 == "same")
    print(f"E102-SHIPPED ok={ok} c06={(s06 or 'NONE')[:8]}|{r06[:8]}|{'MATCH' if m06 else 'DIFF'} "
          f"control={'MATCH' if control_ok else 'MISMATCH'} dispatch={disp} d03={d03} d04={d04} mds_sorted={mds_sorted()}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
