"""Round 19 (~M) check IBM19-2-AC1: the three Holdings packages are re-minted (members-sha256 moved off the
2026-09-25 mint, equal at all three firms) and the mint ledger is CLOSED.

Run from the repo (or worktree) root. Prints REMINTED <sha12> or NOT-REMINTED: <reason>.
"""
import glob
import sys

import boto3

OLD = "83f6a81aab346c482acb66a3b7a58731fbffa8a4f9854d2ec66326db11d84196"
FIRMS = ("49financial", "inflection", "cottonwood")
LEDGER = "org/critical_paths/change_management/*_irpt-holdings-packages-m-20260928_deploy_completion.md"


def main():
    s3 = boto3.client("s3", region_name="us-east-1")
    shas = {}
    for firm in FIRMS:
        head = s3.head_object(Bucket="opal-data-%s" % firm,
                              Key="irpt/%s/code/gold/investor-reporting-holdings.tar.gz" % firm)
        shas[firm] = (head.get("Metadata") or {}).get("members-sha256")
    if None in shas.values() or len(set(shas.values())) != 1:
        print("NOT-REMINTED: members-sha256 per firm %s" % shas)
        return 1
    sha = shas[FIRMS[0]]
    if sha == OLD:
        print("NOT-REMINTED: members-sha256 still %s (the 2026-09-25 mint)" % OLD[:12])
        return 1
    entries = glob.glob(LEDGER)
    if len(entries) != 1:
        print("NOT-REMINTED: %d ledger entries for irpt-holdings-packages-m-20260928" % len(entries))
        return 1
    with open(entries[0], encoding="utf-8") as fh:
        if "**Status:** CLOSED" not in fh.read():
            print("NOT-REMINTED: ledger entry not CLOSED")
            return 1
    print("REMINTED %s" % sha[:12])
    return 0


if __name__ == "__main__":
    sys.exit(main())
