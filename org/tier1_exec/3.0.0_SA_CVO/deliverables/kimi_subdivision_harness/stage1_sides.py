#!/usr/bin/env python3
"""STAGE 1 SIDE-DERIVATION, measured against the live graph. READ-ONLY -- writes nothing.

Runs each canonical detector's OWN query (one row = one motif instance, per the generator's
`recurrence += len(rows)  # each matched path row = one instance of the idiom`), but rewrites the
RETURN clause to yield each constituent's `layer` instead of its node_id, aggregated.

That gives the per-instance substrate_side distribution WITHOUT composing anything -- the first
instance-grain crossing count, which does not exist today.

substrate_side (SYSTEM_DEFINITIONS v1.8): BACKEND = {aws, pipeline} / FRONTEND = {portal} /
KNOWLEDGE = {ms}. semctl contributes NO side. Unknown/absent layer -> counted `side_unresolved`.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from collections import Counter

REPO = r"C:\Users\AndrewBerman\Desktop\ajb_workspace"
GEN = os.path.join(REPO, "org", "tier2_senior", "0.4.0_DS_ClientPlatform",
                   "deliverables", "NFRA_MOTIF_P1_canonical_ab_catalog.py")

SIDE = {"aws": "BACKEND", "pipeline": "BACKEND", "portal": "FRONTEND", "ms": "KNOWLEDGE"}


def side_of(layer):
    if layer is None or layer == "" or layer == "semctl":
        return None                      # semctl contributes no side, by SYSTEM_DEFINITIONS
    return SIDE.get(layer, "UNRESOLVED")


def catalog():
    """Lift AB_CATALOG out of the generator by exec'ing only its literal, no imports."""
    src = open(GEN, encoding="utf-8").read()
    m = re.search(r"^AB_CATALOG = \[", src, re.M)
    if not m:
        sys.exit("AB_CATALOG not found")
    depth, i = 0, m.end() - 1
    while i < len(src):
        if src[i] == "[":
            depth += 1
        elif src[i] == "]":
            depth -= 1
            if depth == 0:
                break
        i += 1
    lit = src[m.end() - 1:i + 1]
    ns = {"N": "CloudNode", "E": "CloudEdge"}     # the two real tables
    return eval(lit, ns)                          # noqa: S307 - our own repo file, literal only


def layerize(query):
    """Rewrite `RETURN a.node_id AS x, b.node_id AS y` -> layer columns + count, aggregated."""
    m = re.search(r"\bRETURN\b(.+)$", query, re.S)
    if not m:
        return None
    pairs = re.findall(r"(\w+)\.node_id\s+AS\s+(\w+)", m.group(1))
    if not pairs:
        return None
    cols = ", ".join("%s.layer AS L%d" % (var, i) for i, (var, _) in enumerate(pairs))
    return query[:m.start()] + "RETURN " + cols + ", count(*) AS n"


def run(q):
    p = subprocess.run([r"C:\Program Files\Git\bin\bash.exe", ".tools/comp-kuzu", q],
                       cwd=REPO, capture_output=True, text=True, timeout=600)
    return p.stdout


def parse(out, ncols):
    """comp-kuzu prints a header, a dashed rule, then rows. Take rows after the rule."""
    lines = out.splitlines()
    start = None
    for i, ln in enumerate(lines):
        # `-+` per column, NOT `-{2,}`: comp-kuzu sizes the rule to the column width, so a
        # single-digit count renders as a ONE-CHAR rule (`---  ---  -`). Requiring 2+ dashes
        # dropped every result whose count was 1-9 -- i.e. exactly the RARE combinations, which
        # is where a cross-side instance would live. Measured: it silently lost a-serve's CDN
        # subquery (9 rows) and returned [] with no error.
        if re.match(r"^-+(\s+-+)*\s*$", ln):
            start = i + 1
    if start is None:
        return []
    rows = []
    for ln in lines[start:]:
        if not ln.strip() or ln.strip().startswith("("):
            continue
        parts = ln.split()
        if len(parts) < 2:
            continue
        try:
            n = int(parts[-1])
        except ValueError:
            continue
        layers = parts[:-1]
        if len(layers) != ncols:                 # NULL layers collapse columns -- pad, never guess
            layers = layers + [None] * (ncols - len(layers))
        rows.append((layers, n))
    return rows


def main():
    specs = catalog()
    print("detectors in catalog: %d" % len(specs))
    print()
    per_detector = []
    tot_inst = 0
    tot_cross = 0
    side_tally = Counter()
    for spec in specs:
        subs = spec.get("subqueries") or [{"query": spec["query"],
                                           "constituents": spec["constituents"]}]
        inst = 0
        cross = 0
        combos = Counter()
        for sub in subs:
            lq = layerize(sub["query"])
            if lq is None:
                continue
            ncols = len(re.findall(r"AS L\d+", lq))
            for layers, n in parse(run(lq), ncols):
                sides = sorted({s for s in (side_of(lay) for lay in layers) if s})
                key = "+".join(sides) if sides else "NONE"
                combos[key] += n
                inst += n
                if len(sides) > 1:
                    cross += n
                side_tally[key] += n
        per_detector.append((spec["id"], inst, cross, combos))
        tot_inst += inst
        tot_cross += cross
        print("  %-14s instances=%-6d cross-side=%-6d  %s"
              % (spec["id"], inst, cross,
                 dict(combos.most_common(4))))
    print()
    print("=" * 78)
    print("STAGE 1 SIDE-DERIVATION -- MEASURED, instance grain")
    print("=" * 78)
    print("  TOTAL MOTIF INSTANCES        : %d" % tot_inst)
    print("  CROSS-SIDE INSTANCES         : %d (%.1f%%)"
          % (tot_cross, 100.0 * tot_cross / max(tot_inst, 1)))
    print()
    print("  by substrate_side combination:")
    for k, v in side_tally.most_common():
        print("    %-24s %7d  (%.1f%%)" % (k, v, 100.0 * v / max(tot_inst, 1)))
    print()
    print("  (class grain today: 19 motif nodes, exactly 1 cross-side)")


if __name__ == "__main__":
    main()
