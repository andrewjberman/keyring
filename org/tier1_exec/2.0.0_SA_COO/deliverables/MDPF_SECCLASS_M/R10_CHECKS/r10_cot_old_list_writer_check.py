"""Round 8 (~M1) check for SC-e-36 (criterion SC8-e36-AC1): the old list stops growing in the Cottonwood tree.

Passes when:
  1. data/cot/scripts/gold/gold_dispatch.sh has no non-comment line carrying the word B_01b, and `bash -n` accepts it;
  2. data/cot/scripts/gold/B_01b.classify_new_securities.py, run as `python B_01b.classify_new_securities.py --upload`
     from its own folder with AWS unreachable, exits 3 and prints a `RETIRED:` line.

Prints `OLD-LIST-WRITERS-RETIRED tree=cot ...` or `NOT-RETIRED tree=cot ...`. Edits nothing; calls no AWS service.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r10_old_list_writer_guard import (
    bash_syntax_ok,
    live_refs,
    repo_root,
    run_retired,
)

GOLD = "data/cot/scripts/gold"
WRITERS = [GOLD + "/B_01b.classify_new_securities.py"]


def main():
    root = repo_root()
    dispatch = os.path.join(root, GOLD, "gold_dispatch.sh")
    refs = live_refs(dispatch, "B_01b")
    syntax = bash_syntax_ok(dispatch)
    results = [(w,) + run_retired(os.path.join(root, w)) for w in WRITERS]
    retired = sum(1 for _, ok, _ in results if ok)
    for w, ok, detail in results:
        print("  {} {} ({})".format("OK " if ok else "BAD", w, detail))
    good = refs == 0 and syntax and retired == len(WRITERS)
    print(f'{"OLD-LIST-WRITERS-RETIRED" if good else "NOT-RETIRED"!s} tree=cot dispatch_live_refs={int(refs)} dispatch_syntax={"ok" if syntax else "BAD"!s} writers_retired={int(retired)}/{len(WRITERS)}')
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main())
