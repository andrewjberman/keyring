"""Is a path a PACKAGED MEMBER of mdpf-gold-lambda? -- the pre-commit question.

"Commit is the deploy" is TRUE of the S3 code plane and FALSE of the zip, and the
floor runs the zip. So a commit to any packaged member re-stales the lambda and
costs a rebuild. The member set spans SIX directories, and a rule phrased around
`data/mdpf/scripts/gold/` covers only 11 of 22.

Reads the PACKAGE literal out of build_package.py by AST -- the FORWARD-looking
source of truth (what the next build WOULD package), never a hand-kept list, and
never the sidecar manifest (which records what WAS packaged last time).

Usage: python .tools/mdpf-gold-packaged-check.py <path> [<path> ...]
       git diff --name-only | xargs python .tools/mdpf-gold-packaged-check.py
Exit:  0 nothing packaged   1 at least one packaged member touched
"""
from __future__ import annotations

import ast
import pathlib
import sys

BUILDER = pathlib.Path("infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/build_package.py")


def packaged_paths() -> set:
    tree = ast.parse(BUILDER.read_text(encoding="utf-8"))
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(getattr(t, "id", None) == "PACKAGE" for t in node.targets):
            continue
        out = set()
        for elt in node.value.elts:
            # (zip_name, repo_path)
            out.add(ast.literal_eval(elt.elts[1]))
        return out
    raise SystemExit("BLOCKED: PACKAGE not found in build_package.py -- refusing to "
                     "answer, because an empty set would read as 'nothing packaged'")


def main() -> int:
    paths = packaged_paths()
    args = [a.replace("\\", "/").lstrip("./") for a in sys.argv[1:]]
    if not args:
        print(f"OK: {len(paths)} packaged member(s). Pass paths to check.")
        for p in sorted(paths):
            print(f"   {p}")
        return 0
    hits = [a for a in args if a in paths]
    print(f"checked {len(args)} path(s) against {len(paths)} packaged member(s)")
    for h in hits:
        print(f"  PACKAGED  {h}")
    if hits:
        print(f"WARN: {len(hits)} packaged member(s) touched -- committing these RE-STALES "
              f"mdpf-gold-lambda. A rebuild + safe-apply is owed before the zip matches source.")
        return 1
    print("OK: no packaged members touched -- the gold lambda zip is unaffected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
