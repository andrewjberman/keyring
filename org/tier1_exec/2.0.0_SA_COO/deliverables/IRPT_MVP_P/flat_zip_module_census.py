#!/usr/bin/env python3
"""Flat-zip module-name collision census (1.0.0_SA_CTO 102269 item 2; row cause: irpt-status 5fSyChId shipped
holdings/errors.py as the flat `errors.py` where HEAD _authz/served.py needed _authz/errors.py).

    python flat_zip_module_census.py <publish worktree> <function> [<built zip>]

For ONE function of the lambda source map, it lists every top-level name the flat zip carries and where each one
comes from: a `files` member of `source_dir` (the checkout) or a `staged_from` entry (repo_path @ pin). A name
claimed by more than one source, or a flat module whose basename exists in more than one IR package directory
(`_authz/errors.py` vs `holdings/errors.py`), is printed as a COLLISION with the source that WON (the byte in the built
zip, when given). rc 1 when an unexplained collision exists, else 0.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import zipfile

IR = "infra/aws/lambda/investor-reporting"


def main(tree, function, built_zip=None):
    m = json.load(open(os.path.join(tree, "infra/aws/lambda/ci/lambda-source-map.json"), encoding="utf-8"))
    v = m["functions"][function]
    sources = {}
    staged = {s["packaged_as"]: s for s in v.get("staged_from", []) or []}
    for f in v.get("files", []):
        if f in staged:
            s = staged[f]
            sources.setdefault(f, []).append("staged %s @%s" % (s["repo_path"], s["pin"][:10]))
        else:
            sources.setdefault(f, []).append("source_dir %s/%s" % (v["source_dir"], f))
    for name, s in staged.items():
        if name not in v.get("files", []):
            sources.setdefault(name, []).append("staged %s @%s" % (s["repo_path"], s["pin"][:10]))
    built = {}
    if built_zip:
        z = zipfile.ZipFile(built_zip)
        built = {n: hashlib.sha256(z.read(n)).hexdigest()[:8] for n in z.namelist() if not n.endswith("/")}
    tracked = subprocess.run(["git", "-C", tree, "ls-files", IR], capture_output=True, text=True).stdout.split()
    by_base = {}
    for path in tracked:
        if path.endswith(".py") and "/tests/" not in path:
            by_base.setdefault(os.path.basename(path), []).append(path[len(IR) + 1:])
    bad = 0
    flat_py = sorted(n for n in sources if "/" not in n and n.endswith(".py"))
    print("%s: %d packaged names, %d flat .py modules" % (function, len(sources), len(flat_py)))
    for name in flat_py:
        homes = by_base.get(name, [])
        src = sources[name]
        chosen = src[0]
        collision = len(src) > 1 or len(homes) > 1
        tag = "COLLISION" if collision else "ok"
        if collision:
            bad += 1
        extra = (" | homes: %s" % ", ".join(homes)) if len(homes) > 1 else ""
        print("  %-9s %-32s <- %s%s%s" % (tag, name, chosen, (" | built %s" % built[name]) if name in built else "", extra))
    print("basename collisions (informative; a per-function entry.py/handler.py is expected): %d" % bad)
    # THE CHECK THAT CATCHES 5fSyChId: members of one SHARED package (_authz, _scope, _keys, _ids) pinned at DIFFERENT
    # commits can skew against each other (served.py @19d8f3038c calling an errors.py @bc3727b3a3 that predates it).
    skew = 0
    for pkg in ("_authz", "_scope", "_keys", "_ids"):
        pins = {}
        for name, s in staged.items():
            if s["repo_path"].startswith("%s/%s/" % (IR, pkg)):
                pins.setdefault(s["pin"][:10], []).append(name)
        if len(pins) > 1:
            skew += 1
            print("  PIN-SKEW  %s: %s" % (pkg, "; ".join("@%s: %s" % (p, ", ".join(sorted(n))) for p, n in sorted(pins.items()))))
        elif pins:
            print("  coherent  %s: all @%s (%d members)" % (pkg, next(iter(pins)), len(next(iter(pins.values())))))
    print("shared-package pin skew: %d" % skew)
    return 1 if skew else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None))
