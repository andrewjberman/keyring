#!/usr/bin/env python3
"""e97_shipped_check.py -- MDPF_SECCLASS SC-e-97 deploy check: the served BD gold C_06 AND D_04 equal the repo bytes of the drained code and are not
the rollback objects; gold_dispatch.sh (the rule's runtime source) is unmoved. READ-ONLY (head-object). Run from the repo root being graded
(box/dell1 at or after 2e8d5c96ef).

Prints  E97-SHIPPED ok=<bool> c06=<served|repo|MATCH|DIFF> d04=<served|repo|MATCH|DIFF> control=<MATCH|MISMATCH> dispatch=<same|MOVED> d03=<same|MOVED>
ok is True when BOTH served ETags equal their repo md5s AND differ from the rollback ETags (C_06 2e35d043163cc18b135d7698cf11dc56, the
2026-10-12T09:55:03Z SC-e-91 ship; D_04 9d083669159ee8875b6489dea4fb2e37, the 2026-10-12T06:18:41Z ADVI FB-f-9 move) AND gold_dispatch.sh still reads
its repo md5 (the act names two keys; the rule's source moving is a STOP). control is the positive control that BOTH repo md5s differ from the
rollback ETags (else the check cannot discriminate). d03 is INFORMATIONAL.
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
D04 = "D_04.client_portal_summary.py"
D03 = "D_03.composition_artifacts.py"
DISPATCH = "gold_dispatch.sh"
ROLLBACK_C06 = "2e35d043163cc18b135d7698cf11dc56"
ROLLBACK_D04 = "9d083669159ee8875b6489dea4fb2e37"


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
    r06, r04 = md5(C06), md5(D04)
    s06, s04 = head("code/gold/" + C06), head("code/gold/" + D04)
    control_ok = r06 != ROLLBACK_C06 and r04 != ROLLBACK_D04
    m06 = s06 is not None and s06 == r06 and s06 != ROLLBACK_C06
    m04 = s04 is not None and s04 == r04 and s04 != ROLLBACK_D04
    disp = "same" if head("code/gold/" + DISPATCH) == md5(DISPATCH) else "MOVED"
    d03 = "same" if head("code/gold/" + D03) == md5(D03) else "MOVED"
    ok = bool(m06 and m04 and control_ok and disp == "same")
    print(f"E97-SHIPPED ok={ok} c06={(s06 or 'NONE')[:8]}|{r06[:8]}|{'MATCH' if m06 else 'DIFF'} "
          f"d04={(s04 or 'NONE')[:8]}|{r04[:8]}|{'MATCH' if m04 else 'DIFF'} "
          f"control={'MATCH' if control_ok else 'MISMATCH'} dispatch={disp} d03={d03}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
