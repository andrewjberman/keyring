"""Round 21 (~M) check IBM21-212-AC1 (row S165): the cot login box runs the retry-capable login, under a closed ledger.

Reads the cell's read-back JSON: an SSM command on i-0643a5bee8a8feabf, run AFTER the deploy, whose output shows
(a) BD_MAX_LOGIN_ATTEMPTS and BD_LOGIN_BACKOFF_MS set in /opt/bd-cot-auto-login/secret-ids.env and (b) the md5 of
/opt/bd-cot-auto-login/bd_49f_auto_login.js equal to the repo's cot-tree bd_49f_auto_login.js; and the deploy ledger
named in the JSON reads CLOSED.

Run from the repo (or worktree) root. Prints RETRY-LIVE <md5> or NOT-LIVE: <reason>.
"""
import glob
import hashlib
import json
import os
import sys

import boto3

REPO = "infra/aws/ec2/bd-cot-auto-login/bd_49f_auto_login.js"
READBACK = "org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND_R21_S165_RETRY_DEPLOY_20260929.json"
INSTANCE = "i-0643a5bee8a8feabf"


def main():
    if not os.path.exists(READBACK):
        print("NOT-LIVE: %s absent" % READBACK)
        return 1
    with open(READBACK, encoding="utf-8") as fh:
        data = json.load(fh)
    with open(REPO, "rb") as fh:
        want = hashlib.md5(fh.read()).hexdigest()
    if want == "28dd27a054b826cc3a87f6b4498d3b5a":
        print("NOT-LIVE: the repo .js is still the pre-retry bytes (28dd27a0)")
        return 1
    inv = boto3.client("ssm", region_name="us-east-1").get_command_invocation(
        CommandId=data.get("command_id", ""), InstanceId=INSTANCE)
    out = inv.get("StandardOutputContent") or ""
    missing = [t for t in ("BD_MAX_LOGIN_ATTEMPTS=", "BD_LOGIN_BACKOFF_MS=", want) if t not in out]
    if inv.get("Status") != "Success" or missing:
        print("NOT-LIVE: SSM %s status %s, missing in output %s" % (data.get("command_id"), inv.get("Status"), missing))
        return 1
    entries = glob.glob("org/critical_paths/change_management/*_%s_deploy_completion.md" % data.get("ledger_slug", "?"))
    if len(entries) != 1:
        print("NOT-LIVE: %d ledger entries for %r" % (len(entries), data.get("ledger_slug")))
        return 1
    with open(entries[0], encoding="utf-8") as fh:
        if "**Status:** CLOSED" not in fh.read():
            print("NOT-LIVE: ledger %s not CLOSED" % data.get("ledger_slug"))
            return 1
    print("RETRY-LIVE %s" % want[:12])
    return 0


if __name__ == "__main__":
    sys.exit(main())
