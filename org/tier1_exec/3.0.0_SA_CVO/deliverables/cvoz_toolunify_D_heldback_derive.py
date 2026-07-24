#!/usr/bin/env python3
"""CVO~Z held-back control derivation for NFRA_TOOLUNIFY lane ~D.

PRE-REGISTERED: run and SEALED before ~D's deliverable is read, so the control cannot
be contaminated by their output. The published floor (3 FPs + nerves_resolve.py:73 FN)
measures whether ~D handled the cases they were TOLD about. This derives cases they were
NOT told about, which is the only thing that measures the INSTRUMENT rather than the author.

Method (deliberately DIFFERENT from ~D's, so it is an independent oracle, not a re-run):
  1. resolve each .tools/comp-* wrapper's depth-1 backing python (what the OLD audit saw)
  2. walk the transitive local-import closure of that backing
  3. flag any artifact read that appears ONLY at depth >= 2

A tool in DEPTH2_ONLY is invisible to a depth-1 method BY CONSTRUCTION. If ~D's classifier
is genuinely import-closure based it must surface these; if it special-cased the published
four, it will miss them -- and it will miss them while its scorecard reads PASS.
"""
from __future__ import annotations

import ast
import json
import os
import re
import sys

# org/tier1_exec/3.0.0_SA_CVO/deliverables/<this> -> 5 levels up is the workspace root.
WS = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))
TOOLS = os.path.join(WS, ".tools")
GRAPHDIR = os.path.join(WS, "org", "modules", "graph")

# Artifact-shaped reads we care about (extension-agnostic: the predecessor's PROJECTION set
# was hardcoded to 3 .json names and missed .parquet caches entirely).
ARTIFACT_RE = re.compile(r"['\"]([A-Za-z0-9_.\-]+\.(?:json|parquet|yaml|yml|db|jsonl))['\"]")
# Writes -- the producer-vs-consumer discriminator the old audit could not make.
WRITE_RE = re.compile(r"json\.dump|\.write_text\(|open\([^)]*['\"][wa]['\"]")


def depth1_backing(wrapper: str) -> list[str]:
    try:
        txt = open(wrapper, encoding="utf-8", errors="replace").read()
    except OSError:
        return []
    out = []
    for m in re.finditer(r'python[0-9.]*\s+"?([^"\n]*?\.py)"?', txt):
        p = m.group(1)
        if "comp_log_auto" in p:
            continue
        p = p.replace("$WORKSPACE", WS).replace("${WORKSPACE}", WS).replace('"', "")
        if not os.path.isabs(p):
            cand = os.path.join(WS, p)
            p = cand if os.path.exists(cand) else p
        out.append(p)
    return out


def local_imports(pyfile: str) -> list[str]:
    """Local sibling modules imported by pyfile, resolved to paths in org/modules/graph."""
    try:
        tree = ast.parse(open(pyfile, encoding="utf-8", errors="replace").read())
    except (OSError, SyntaxError):
        return []
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            mods.add(node.module.split(".")[-1])
        elif isinstance(node, ast.Import):
            for a in node.names:
                mods.add(a.name.split(".")[-1])
    out = []
    for m in mods:
        cand = os.path.join(GRAPHDIR, m + ".py")
        if os.path.exists(cand) and os.path.abspath(cand) != os.path.abspath(pyfile):
            out.append(cand)
    return out


def artifacts_in(pyfile: str) -> tuple[set[str], set[str]]:
    """(reads, writes) artifact basenames referenced in pyfile, skipping comments."""
    reads, writes = set(), set()
    try:
        txt = open(pyfile, encoding="utf-8", errors="replace").read()
    except OSError:
        return reads, writes
    for line in txt.splitlines():
        s = line.strip()
        if s.startswith("#") or not ARTIFACT_RE.search(line):
            continue
        names = set(ARTIFACT_RE.findall(line))
        if WRITE_RE.search(line):
            writes |= names
        else:
            reads |= names
    return reads, writes


def closure(entry: str, seen: set[str] | None = None, depth: int = 0, maxd: int = 4):
    """Yield (pyfile, depth) over the transitive local-import closure."""
    seen = seen if seen is not None else set()
    key = os.path.abspath(entry)
    if key in seen or depth > maxd or not os.path.exists(entry):
        return
    seen.add(key)
    yield entry, depth
    for imp in local_imports(entry):
        yield from closure(imp, seen, depth + 1, maxd)


def main() -> int:
    wrappers = []
    for w in sorted(os.listdir(TOOLS)):
        if not w.startswith("comp-") or w.endswith((".py", ".sh")):
            continue
        wrappers.append(os.path.join(TOOLS, w))
    wrappers.append(os.path.join(TOOLS, "pipescript"))

    rows = {}
    for w in wrappers:
        name = os.path.basename(w)
        d1 = depth1_backing(w)
        if not d1:
            continue
        shallow_reads: set[str] = set()
        deep_reads: dict[str, list[str]] = {}
        writes: set[str] = set()
        for entry in d1:
            for pyf, depth in closure(entry):
                r, wr = artifacts_in(pyf)
                writes |= wr
                if depth == 0:
                    shallow_reads |= r
                else:
                    for a in r:
                        deep_reads.setdefault(a, []).append(
                            "%s@d%d" % (os.path.relpath(pyf, WS).replace("\\", "/"), depth)
                        )
        depth2_only = {a: v for a, v in deep_reads.items() if a not in shallow_reads}
        if depth2_only:
            rows[name] = {
                "depth1_backing": [os.path.relpath(p, WS).replace("\\", "/") for p in d1],
                "DEPTH2_ONLY_reads": depth2_only,
                "also_writes": sorted(writes),
            }

    out = {
        "control": "CVO~Z held-back set for NFRA_TOOLUNIFY lane ~D",
        "pre_registered": True,
        "denominator": {"wrappers_scanned": len(wrappers), "tools_with_depth2_only_reads": len(rows)},
        "note": (
            "Each entry reads an artifact ONLY at import depth >= 2. A depth-1 method cannot "
            "see these BY CONSTRUCTION. ~D was not told about any of them."
        ),
        "rows": rows,
    }
    print(json.dumps(out, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
