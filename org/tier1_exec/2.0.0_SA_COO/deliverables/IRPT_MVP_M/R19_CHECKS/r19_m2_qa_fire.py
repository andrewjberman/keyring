"""Round 19 (~M) check IBM19-2-AC2: one QA fire of irpt-holdings-refresh-lambda reached Success at all three
firms on the runner (SSM commands tagged "irpt holdings refresh qa <firm> 2026-09-28").

Prints QA-FIRED <command ids> or NOT-FIRED: <reason>.
"""
import sys

import boto3

INSTANCE = "i-02448edb624a7a7cf"
FIRMS = ("49financial", "inflection", "cottonwood")
DAY = "2026-09-28"


def main():
    ssm = boto3.client("ssm", region_name="us-east-1")
    found = {}
    total = 0
    for page in ssm.get_paginator("list_commands").paginate(InstanceId=INSTANCE):
        for cmd in page.get("Commands") or []:
            total += 1
            comment = cmd.get("Comment") or ""
            for firm in FIRMS:
                if comment == "irpt holdings refresh qa %s %s" % (firm, DAY):
                    found.setdefault(firm, []).append((cmd["Status"], cmd["CommandId"]))
    scanned = sum(len(v) for v in found.values())
    ok = {f: [c for s, c in found.get(f, []) if s == "Success"] for f in FIRMS}
    missing = [f for f in FIRMS if not ok[f]]
    if missing:
        print("NOT-FIRED: no Success qa command for %s (qa commands seen: %d of %d on the instance, %s)"
              % (missing, scanned, total, found))
        return 1
    print("QA-FIRED " + " ".join("%s=%s" % (f, ok[f][0]) for f in FIRMS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
