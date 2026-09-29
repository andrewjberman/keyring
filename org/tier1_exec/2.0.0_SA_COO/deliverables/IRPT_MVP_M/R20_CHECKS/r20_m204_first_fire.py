"""Round 20 (~M) check IBM20-204-AC1: the first SCHEDULED fire (2026-09-29) is read back per firm, and the enable
ledger is CLOSED. A firm whose SSM command succeeded must show its served manifest VersionId MOVED; a failed firm must
show it UNCHANGED (the CTO's and CRO's condition). Every command id must be a non-qa scheduled command on the runner.

Run from the repo (or worktree) root. Prints READ-BACK <firm=status...> or NOT-READ: <reason>.
"""
import glob
import json
import os
import sys

import boto3

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_R4_FIRST_FIRE_20260929.json"
LEDGER = "org/critical_paths/change_management/*_irpt-holdings-schedule-enable-m-20260929_deploy_completion.md"
FIRMS = ("49financial", "inflection", "cottonwood")
INSTANCE = "i-02448edb624a7a7cf"


def main():
    if not os.path.exists(PATH):
        print("NOT-READ: %s absent" % PATH)
        return 1
    with open(PATH, encoding="utf-8") as fh:
        rows = {r.get("firm"): r for r in json.load(fh).get("firms") or []}
    if set(rows) != set(FIRMS):
        print("NOT-READ: firms %s" % sorted(rows))
        return 1
    ssm = boto3.client("ssm", region_name="us-east-1")
    out = []
    for firm in FIRMS:
        r = rows[firm]
        inv = ssm.get_command_invocation(CommandId=r.get("command_id", ""), InstanceId=INSTANCE)
        cmd = ssm.list_commands(CommandId=r["command_id"])["Commands"][0]
        if cmd.get("Comment") != "irpt holdings refresh %s 2026-09-29" % firm:
            print("NOT-READ: %s command %s comment %r is not the scheduled non-qa fire" % (firm, r["command_id"], cmd.get("Comment")))
            return 1
        moved = r.get("served_version_before") != r.get("served_version_after")
        ok = inv["Status"] == "Success"
        if ok != moved or not r.get("served_version_before") or not r.get("served_version_after"):
            print("NOT-READ: %s status %s but served VersionId moved=%s" % (firm, inv["Status"], moved))
            return 1
        if ok and not r.get("revision"):
            print("NOT-READ: %s succeeded but names no published revision" % firm)
            return 1
        out.append("%s=%s" % (firm, inv["Status"]))
    entries = glob.glob(LEDGER)
    if len(entries) != 1:
        print("NOT-READ: %d enable ledger entries" % len(entries))
        return 1
    with open(entries[0], encoding="utf-8") as fh:
        if "**Status:** CLOSED" not in fh.read():
            print("NOT-READ: enable ledger not CLOSED")
            return 1
    print("READ-BACK " + " ".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
