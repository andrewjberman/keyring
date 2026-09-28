"""Round 19 (~M) check IBM19-2-AC3: the R4 ENABLE half is filled from the QA fire -- no {{slot}} left, and it
names the re-minted members-sha256 and the three SUCCESS QA command ids it measured (amendment 1).

Run from the repo (or worktree) root. Prints FILLED or NOT-FILLED: <reason>.
"""
import os
import re
import sys

import boto3

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_R4_ENABLE_20260928.md"


def main():
    if not os.path.exists(PATH):
        print("NOT-FILLED: %s absent" % PATH)
        return 1
    with open(PATH, encoding="utf-8") as fh:
        text = fh.read()
    slots = re.findall(r"\{\{[^}]*\}\}", text)
    if slots:
        print("NOT-FILLED: %d slot(s) left, first %r" % (len(slots), slots[0]))
        return 1
    if "83f6a81aab34" in text.split("members-sha256", 1)[-1][:200]:
        print("NOT-FILLED: members-sha256 still names the 2026-09-25 mint")
        return 1
    cids = set(re.findall(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", text))
    if "members-sha256" not in text or len(cids) < 3:
        print("NOT-FILLED: needs the members-sha256 line and 3 QA command ids (found %d ids)" % len(cids))
        return 1
    # Amendment 1: the half must name a SUCCESS qa command per firm (a failed fire is not an enable basis).
    ssm = boto3.client("ssm", region_name="us-east-1")
    ok = set()
    for page in ssm.get_paginator("list_commands").paginate(InstanceId="i-02448edb624a7a7cf"):
        for cmd in page.get("Commands") or []:
            if (cmd.get("Comment") or "").startswith("irpt holdings refresh qa ") and cmd["Status"] == "Success":
                ok.add(cmd["CommandId"])
    named = cids & ok
    if len(named) < 3:
        print("NOT-FILLED: the half names %d Success qa command id(s); 3 needed (%d Success qa commands exist)"
              % (len(named), len(ok)))
        return 1
    print("FILLED (%d Success qa command ids)" % len(named))
    return 0


if __name__ == "__main__":
    sys.exit(main())
