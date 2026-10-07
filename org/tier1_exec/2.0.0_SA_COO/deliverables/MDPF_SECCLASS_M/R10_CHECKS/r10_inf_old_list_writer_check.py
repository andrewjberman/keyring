"""Round 8 (~M1) check for SC-e-37 (criterion SC8-e37-AC1): the old list stops growing in the Inflection tree.

Passes when:
  1. data/inf/scripts/classification/classify_assets.py, run as `python classify_assets.py --upload` from its own
     folder with AWS unreachable, exits 3 and prints a `RETIRED:` line (its write path to bd-securities is closed);
  2. its read-only library entry `get_classifications` is still importable (readers are SC-e-38's, not this cell's);
  3. data/inf/scripts/gold/orion-gold-dispatch.sh has no non-comment line naming classify_assets (control: the
     Inflection gold chain never called it; measured 2026-10-07).

Prints `OLD-LIST-WRITERS-RETIRED tree=inf ...` or `NOT-RETIRED tree=inf ...`. Edits nothing; calls no AWS service.
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r10_old_list_writer_guard import (
    dead_aws_env,
    live_refs,
    repo_root,
    run_retired,
)

CLS = "data/inf/scripts/classification"
WRITER = CLS + "/classify_assets.py"
DISPATCH = "data/inf/scripts/gold/orion-gold-dispatch.sh"


def library_importable(root):
    code = "import classify_assets as m; print('LIB-OK' if callable(getattr(m, 'get_classifications', None)) else 'LIB-GONE')"
    r = subprocess.run([sys.executable, "-c", code], cwd=os.path.join(root, CLS), env=dead_aws_env(),
                       capture_output=True, text=True, timeout=30, check=False)
    return "LIB-OK" in r.stdout


def main():
    root = repo_root()
    ok, detail = run_retired(os.path.join(root, WRITER))
    lib = library_importable(root)
    refs = live_refs(os.path.join(root, DISPATCH), "classify_assets")
    print("  {} {} ({})".format("OK " if ok else "BAD", WRITER, detail))
    good = ok and lib and refs == 0
    print(f'{"OLD-LIST-WRITERS-RETIRED" if good else "NOT-RETIRED"!s} tree=inf writer_retired={"yes" if ok else "no"!s} library={"ok" if lib else "BAD"!s} dispatch_live_refs={int(refs)}')
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main())
