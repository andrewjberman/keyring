"""Round 23 (~M) check IBM23-231-AC1 (row S208): every irpt-m-* branch has a per-file disposition.

Reads the census JSON the cell writes. The census must name EVERY local branch matching irpt-m-* (measured here with
git, not taken from the census), give each one a disposition in {WORLD-DONE, SUPERSEDED, DRAIN, RETIRE}, and give
every file in that branch's net diff against CLOUD (git diff $(merge-base CLOUD b) b) its own row with a disposition
and evidence. A DRAIN branch must list the exact files to carry. Read-only.

Run from the repo (or worktree) root. Prints CENSUS-COMPLETE <branches> <files> or NOT-COMPLETE: <reason>.
"""
import json
import os
import subprocess
import sys

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R23_M_BRANCH_CENSUS_20260929.json"
BRANCH_STATES = {"WORLD-DONE", "SUPERSEDED", "DRAIN", "RETIRE"}
FILE_STATES = {"PRESENT", "SUPERSEDED", "CARRY", "DROP"}


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def main():
    if not os.path.exists(PATH):
        print("NOT-COMPLETE: %s absent" % PATH)
        return 1
    live = sorted(b for b in git("branch", "--format=%(refname:short)", "--list", "irpt-m-*").split() if b)
    with open(PATH, encoding="utf-8") as fh:
        rows = {r.get("branch"): r for r in json.load(fh).get("branches") or []}
    missing = sorted(set(live) - set(rows))
    if missing:
        print("NOT-COMPLETE: branches without a disposition: %s" % missing)
        return 1
    nfiles = 0
    for b in live:
        r = rows[b]
        if r.get("disposition") not in BRANCH_STATES or not r.get("evidence"):
            print("NOT-COMPLETE: %s disposition %r / evidence %r" % (b, r.get("disposition"), bool(r.get("evidence"))))
            return 1
        mb = git("merge-base", "CLOUD", b).strip()
        files = sorted(f for f in git("diff", "--name-only", mb, b).splitlines() if f)
        got = {f.get("path"): f for f in r.get("files") or []}
        gap = [f for f in files if f not in got]
        if gap:
            print("NOT-COMPLETE: %s files without a row: %s" % (b, gap[:5]))
            return 1
        for f in files:
            if got[f].get("disposition") not in FILE_STATES or not got[f].get("evidence"):
                print("NOT-COMPLETE: %s %s disposition %r" % (b, f, got[f].get("disposition")))
                return 1
        carry = [f for f in files if got[f]["disposition"] == "CARRY"]
        if r["disposition"] == "DRAIN" and not carry:
            print("NOT-COMPLETE: %s is DRAIN but carries no file" % b)
            return 1
        if r["disposition"] != "DRAIN" and carry:
            print("NOT-COMPLETE: %s carries %d file(s) but is not DRAIN" % (b, len(carry)))
            return 1
        nfiles += len(files)
    print("CENSUS-COMPLETE %d branches %d files" % (len(live), nfiles))
    return 0


if __name__ == "__main__":
    sys.exit(main())
