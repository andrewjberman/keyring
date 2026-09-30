"""Round 21 (~M) check IBM21-211-AC1 after amendment 2 (CTO ruling S198): the cot tree carries the RUNNING login script as
non-graded EVIDENCE (a .txt capture), not as a build input.

The repo file infra/aws/ec2/bd-cot-auto-login/bd_49f_auto_login.js.running-capture.txt must be byte-for-byte the script the cot login box
runs (md5 28dd27a054b826cc3a87f6b4498d3b5a, 35,049 B, read on the box by 0.6.2_AE_PartnerETL~S for S166), and the
cell's read-back JSON must name an SSM command on i-0643a5bee8a8feabf whose output shows that same md5 on
/opt/bd-cot-auto-login/bd_49f_auto_login.js (no behaviour change: the box still runs those bytes).

Run from the repo (or worktree) root. Prints RUNNING-CAPTURE <md5> or NO-CAPTURE: <reason>.
"""
import hashlib
import json
import os
import sys

import boto3

REPO = "infra/aws/ec2/bd-cot-auto-login/bd_49f_auto_login.js.running-capture.txt"
READBACK = "org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND_R21_S166_RUNNING_VS_REPO_20260929.json"
MD5 = "28dd27a054b826cc3a87f6b4498d3b5a"
INSTANCE = "i-0643a5bee8a8feabf"


def main():
    if not os.path.exists(REPO):
        print("NO-CAPTURE: %s absent" % REPO)
        return 1
    with open(REPO, "rb") as fh:
        body = fh.read()
    got = hashlib.md5(body).hexdigest()
    if got != MD5 or len(body) != 35049:
        print("NO-CAPTURE: repo md5 %s / %d B, want %s / 35049 B" % (got, len(body), MD5))
        return 1
    if not os.path.exists(READBACK):
        print("NO-CAPTURE: running-path read-back %s absent" % READBACK)
        return 1
    with open(READBACK, encoding="utf-8") as fh:
        cid = json.load(fh).get("command_id", "")
    inv = boto3.client("ssm", region_name="us-east-1").get_command_invocation(CommandId=cid, InstanceId=INSTANCE)
    out = inv.get("StandardOutputContent") or ""
    if inv.get("Status") != "Success" or MD5 not in out:
        print("NO-CAPTURE: SSM %s status %s, running md5 in output: %s" % (cid, inv.get("Status"), MD5 in out))
        return 1
    print("RUNNING-CAPTURE %s" % MD5[:12])
    return 0


if __name__ == "__main__":
    sys.exit(main())
