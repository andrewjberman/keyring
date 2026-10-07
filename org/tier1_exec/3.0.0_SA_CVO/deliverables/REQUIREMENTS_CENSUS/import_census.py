#!/usr/bin/env python3
"""Census of the third-party Python packages the workspace's own code imports (3.0.0_SA_CVO, 2026-10-07).

    python import_census.py <repo root> <out.json>

Reads every git-TRACKED .py file outside the vendored trees, parses it with `ast` (no code is executed), and collects
the top-level name of every `import x` / `from x import y` (relative imports skipped). A name is THIRD-PARTY when it is
not in the standard library (`sys.stdlib_module_names`) and not a first-party module (a tracked .py file's stem or a
tracked directory's name anywhere in the repo). Each third-party name is mapped to its distribution and installed
version with `importlib.metadata`; a name with no installed distribution is listed as NOT INSTALLED, never dropped.
Files that do not parse are counted and named. The denominators are printed.
"""
from __future__ import annotations

import ast
import collections
import importlib.metadata as md
import json
import os
import subprocess
import sys

# vendored or foreign trees: third-party code checked in, or another repo
EXCLUDE_PREFIXES = ("portal/", "archive/", "node_modules/")
EXCLUDE_PARTS = ("/layers/", "/node_modules/", "/site-packages/", "/_vendor/", "/vendor/", "/.venv/", "/venv/",
                 "/python/lib/", "/dist-packages/")


def area(path):
    p = path.split("/")
    if p[0] in (".tools", "lib", "sdk", "rcg", "integrations", "deck_generation", "docs", "workflows"):
        return p[0]
    if p[0] == ".claude":
        return ".claude/skills"
    if p[0] == "org":
        return "org/mcp" if len(p) > 1 and p[1] == "mcp" else "org"
    if p[0] == "data":
        return "data"
    if p[0] == "infra":
        return "infra/lambda" if "/lambda/" in path else "infra/other"
    return p[0] if len(p) > 1 else "(root)"


def main() -> int:
    root, out_path = sys.argv[1], sys.argv[2]
    tracked = subprocess.run(["git", "-C", root, "ls-files", "-z"], capture_output=True, check=True).stdout.decode(
        "utf-8", "replace").split("\0")
    py_all = [f for f in tracked if f.endswith(".py")]
    excluded = [f for f in py_all if f.startswith(EXCLUDE_PREFIXES) or any(x in "/" + f for x in EXCLUDE_PARTS)]
    # VENDORED-IN-PLACE: a third-party package checked in beside a Lambda's own code. Its files are exactly the ones
    # a tracked `<name>.dist-info/RECORD` lists, relative to the folder holding the dist-info. Where a dist-info has
    # no tracked RECORD, every sub-folder of its parent is treated as vendored (the parent's own .py files are kept).
    vendored, vendor_roots, no_record_roots = set(), set(), set()
    for f in tracked:
        parts = f.split("/")
        for i, d in enumerate(parts[:-1]):
            if d.endswith(".dist-info") or d.endswith(".egg-info"):
                vendor_roots.add("/".join(parts[:i]))
    for r in sorted(vendor_roots):
        prefix = r + "/" if r else ""
        records = [f for f in tracked if f.startswith(prefix) and f.endswith(".dist-info/RECORD")
                   and f[len(prefix):].count("/") == 1]
        if not records:
            no_record_roots.add(r)
        for rec in records:
            for line in open(os.path.join(root, rec), encoding="utf-8", errors="replace"):
                rel = line.split(",")[0].strip()
                if rel and not rel.startswith(".."):
                    vendored.add(prefix + rel)
    for f in py_all:
        for r in no_record_roots:
            prefix = r + "/" if r else ""
            if f.startswith(prefix) and "/" in f[len(prefix):]:
                vendored.add(f)
    in_place = [f for f in py_all if f in vendored and f not in set(excluded)]
    excluded = excluded + in_place
    files = [f for f in py_all if f not in set(excluded)]
    first_party = set()
    for f in tracked:
        if f in vendored or any(x in "/" + f for x in EXCLUDE_PARTS) or f.startswith(EXCLUDE_PREFIXES)                 or ".dist-info/" in f or ".egg-info/" in f:
            continue
        parts = f.split("/")
        for d in parts[:-1]:
            first_party.add(d)
        if f.endswith(".py"):
            first_party.add(os.path.splitext(parts[-1])[0])
    stdlib = set(sys.stdlib_module_names)
    uses = collections.defaultdict(lambda: collections.Counter())   # name -> area -> files
    examples = collections.defaultdict(list)
    unparsed = []
    for f in files:
        try:
            src = open(os.path.join(root, f), "rb").read()
            tree = ast.parse(src, filename=f)
        except (SyntaxError, ValueError, OSError) as exc:
            unparsed.append("%s: %s" % (f, type(exc).__name__))
            continue
        names = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names.update(a.name.split(".")[0] for a in node.names)
            elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                names.add(node.module.split(".")[0])
        for n in names:
            uses[n][area(f)] += 1
            if len(examples[n]) < 3:
                examples[n].append(f)
    dist_of = md.packages_distributions()
    third, shadowed = {}, {}
    for n, by_area in sorted(uses.items()):
        if n in stdlib or n.startswith("_"):
            continue
        dists = sorted(set(dist_of.get(n, [])))
        rec = {"import": n, "files": sum(by_area.values()), "by_area": dict(by_area), "examples": examples[n],
               "distributions": dists,
               "installed": {d: md.version(d) for d in dists}}
        if n in first_party:
            if dists:            # a first-party name that is ALSO an installed distribution: report, do not decide
                shadowed[n] = rec
            continue
        third[n] = rec
    result = {"python": sys.version.split()[0],
              "denominators": {"tracked_files": len(tracked), "tracked_py": len(py_all), "excluded_vendored_py": len(excluded), "of_which_vendored_in_place_py": len(in_place),
                               "vendor_roots": len(vendor_roots), "vendor_roots_without_record": len(no_record_roots),
                               "scanned_py": len(files), "unparsed": len(unparsed),
                               "distinct_import_names": len(uses), "third_party_names": len(third),
                               "third_party_not_installed": sum(1 for r in third.values() if not r["distributions"]),
                               "first_party_names_shadowing_an_installed_distribution": len(shadowed)},
              "excluded_rule": {"prefixes": EXCLUDE_PREFIXES, "path_parts": EXCLUDE_PARTS},
              "unparsed": unparsed, "third_party": third, "shadowed": shadowed}
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(result, fh, indent=1, sort_keys=True)
    print(json.dumps(result["denominators"], indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
