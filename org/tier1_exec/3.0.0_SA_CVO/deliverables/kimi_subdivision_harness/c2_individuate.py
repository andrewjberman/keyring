#!/usr/bin/env python3
"""C2 INDIVIDUATION -- emit one node per MATCH, not one per DETECTOR.

DONE-MEANS item 1 of the C2/C3.i production goal (Andrew-direct 2026-08-07; roles agreed with
1.0.0_SA_CTO~B 011425Z).

THE DEFECT THIS CLOSES
  `NFRA_MOTIF_P1_canonical_ab_catalog.py:188` -- `recurrence += len(rows)  # each matched path row
  is one instance of the idiom` -- iterates every match and then DISCARDS the rows, emitting ONE
  node for the DETECTOR. So `BDataflowMotif CONTAINS 1336` is a CATEGORY holding 1,336 motifs that
  were never individuated, and `CONTAINS` became a CLASSIFICATION edge rather than a structural one.
  Measured consequence: the graph carries 19 C2Motif + 4 C3System, which is exactly
  6+13 and 1+3 -- the node counts of two hand-authored JSON deliverables (CTO~B, 011425Z).

WHAT CHANGES: the OUTPUT SHAPE ONLY. The detectors are real, run live, and are not touched -- their
queries are read from the catalog verbatim. This is not new composition; it is not discarding the
composition that already happens.

OUTPUT: the SAME envelope `derive_runner.py` already loads (`nodes`/`edges`, node_id/node_type/props),
so the existing loader consumes it unchanged and the productionisation path stays short.

READ-ONLY against the estate. Writes one JSON to --out. Nothing is deployed by this script.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter

REPO = r"C:\Users\AndrewBerman\Desktop\ajb_workspace"
GEN = os.path.join(REPO, "org", "tier2_senior", "0.4.0_DS_ClientPlatform",
                   "deliverables", "NFRA_MOTIF_P1_canonical_ab_catalog.py")
BASH = r"C:\Program Files\Git\bin\bash.exe"

# substrate_side -- SYSTEM_DEFINITIONS.yaml v1.8 @dcdedf6fe. A ROLLUP over the substrate axis.
# KNOWLEDGE is DECLARED-BUT-UNREACHABLE: ms is 5,828 nodes and zero detectors touch any of them, so
# no instance can carry it until an ms detector plane exists. Its emptiness is a fact about DETECTOR
# COVERAGE, not about the estate -- declared here so it is never read as "the knowledge plane has no
# structure" (Rule 24 postulate (iv), run with CTO~B 011629Z).
SIDE = {"aws": "BACKEND", "pipeline": "BACKEND", "portal": "FRONTEND", "ms": "KNOWLEDGE"}


def side_of(layer):
    """None = contributes no side. semctl is NOT a substrate (01_substrate.md:39)."""
    if not layer or layer == "semctl":
        return None
    return SIDE.get(layer)                      # unknown layer -> None -> counted as unresolved


def catalog():
    src = open(GEN, encoding="utf-8").read()
    m = re.search(r"^AB_CATALOG = \[", src, re.M)
    if not m:
        sys.exit("AB_CATALOG not found in %s" % GEN)
    depth, i = 0, m.end() - 1
    while i < len(src):
        if src[i] == "[":
            depth += 1
        elif src[i] == "]":
            depth -= 1
            if depth == 0:
                break
        i += 1
    return eval(src[m.end() - 1:i + 1], {"N": "CloudNode", "E": "CloudEdge"})  # noqa: S307


def with_layers(query):
    """Add a `<alias>__L` layer column beside every `<var>.node_id AS <alias>`.

    One query, not two: fetching ids and layers separately would let the graph advance between
    them, and a member whose layer came from a different vintage is a silent mis-derivation.
    """
    m = re.search(r"\bRETURN\b(.+)$", query, re.S)
    if not m:
        return None, []
    pairs = re.findall(r"(\w+)\.node_id\s+AS\s+(\w+)", m.group(1))
    if not pairs:
        return None, []
    cols = ", ".join("%s.node_id AS %s, %s.layer AS %s__L" % (v, a, v, a) for v, a in pairs)
    return query[:m.start()] + "RETURN " + cols, [a for _, a in pairs]


def run_rows(query, aliases):
    """Return [{alias: id, alias__L: layer}, ...]. Parses comp-kuzu's table output."""
    p = subprocess.run([BASH, ".tools/comp-kuzu", query], cwd=REPO,
                       capture_output=True, text=True, timeout=900)
    lines = p.stdout.splitlines()
    hdr = None
    # `-+` per column, NOT `-{2,}`: comp-kuzu sizes the rule to column width, so a 1-char column
    # renders as a single dash. Requiring 2+ silently drops those rows (measured 2026-08-07).
    for i, ln in enumerate(lines):
        if re.match(r"^-+(\s+-+)*\s*$", ln) and i > 0:
            hdr = lines[i - 1].split()
            start = i + 1
    if hdr is None:
        return []
    out, skipped = [], 0
    for ln in lines[start:]:
        if not ln.strip() or ln.strip().startswith("("):
            continue
        parts = ln.split()
        if len(parts) != len(hdr):
            # A ragged row is NEVER padded-and-guessed -- but it is also never dropped SILENTLY.
            # This counter exists because the first run emitted 6,573 against a known-good 6,686
            # and the 113 had nowhere to be reported. An unexplained delta is a finding; an
            # uncounted skip makes it unfindable.
            skipped += 1
            continue
        out.append(dict(zip(hdr, parts)))
    return out, skipped


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                  "c2_instances.json"))
    args = ap.parse_args()

    specs = catalog()
    nodes, edges = {}, []      # node_id -> node; a repeated member-set is ONE instance
    per_family = Counter()
    side_tally = Counter()
    status_tally = Counter()
    members_seen = set()
    dropped_ragged = 0
    skipped_ragged = 0
    rows_seen = 0

    for spec in specs:
        subs = spec.get("subqueries") or [{"query": spec["query"],
                                           "constituents": spec["constituents"]}]
        for sub in subs:
            q, aliases = with_layers(sub["query"])
            if q is None:
                continue
            rows, sk = run_rows(q, aliases)
            skipped_ragged += sk
            for row in rows:
                rows_seen += 1
                mem = [row[a] for a in aliases if row.get(a)]
                if not mem:
                    dropped_ragged += 1
                    continue
                sides, unresolved = set(), 0
                for a in aliases:
                    s = side_of(row.get(a + "__L"))
                    if s:
                        sides.add(s)
                    else:
                        unresolved += 1
                # TWO FIELDS, not one enum. substrate_side answers "which side is this" (a fact
                # about the ESTATE); side_status answers "did we find out" (a fact about OUR
                # DERIVATION). Mixing them is Rule 24 (iii) -- the same shape as DETECT_FAILED
                # smuggled in beside a zero-candidate count. Split ruled with CTO~B 011629Z.
                status = ("RESOLVED" if unresolved == 0
                          else "UNRESOLVED" if unresolved == len(aliases) else "PARTIAL")
                # Deterministic id: same members -> same instance across runs, so a re-run is
                # comparable and duplicate matches collapse rather than inflating the count.
                mid = "motifi:%s:%s" % (
                    spec["id"], hashlib.sha1("|".join(sorted(mem)).encode()).hexdigest()[:12])
                nodes[mid] = ({
                    "node_id": mid, "node_type": "C2MotifInstance",
                    "props": {
                        "grain": "instance",            # the discriminator whose ABSENCE put class
                        "family": spec["id"],           # and instance nodes in one table (Rule 24 ii)
                        "motif_type": spec["ntype"],
                        "plane": spec["plane"],
                        "shape_matched": spec["idiom"],
                        "substrate_side": sorted(sides),        # SET, may be empty
                        "side_status": status,
                        "members_unresolved": unresolved,
                        "members_total": len(aliases),
                    }})
                for nid in mem:
                    edges.append({"source": mid, "target": nid, "edge_type": "CONTAINS",
                                  "props": {"layer": "C2i->C1"}})
                    members_seen.add(nid)
                per_family[spec["id"]] += 1
                side_tally["+".join(sorted(sides)) or "NONE"] += 1
                status_tally[status] += 1

    doc = {
        "producer": "3.0.0_SA_CVO c2_individuate -- one node per MATCH (DONE-MEANS item 1)",
        "supersedes_shape_of": ["motif_c2c3_materialize.json", "motif_c2c3_materialize_ab.json"],
        "grounding": {
            "detectors": "read VERBATIM from NFRA_MOTIF_P1_canonical_ab_catalog.py AB_CATALOG",
            "recurrence": "NOT echoed -- every instance is a live matched row",
            "substrate_side": "SYSTEM_DEFINITIONS.yaml v1.8 @dcdedf6fe; derived from member layers",
            "knowledge_unreachable": ("KNOWLEDGE is DECLARED-BUT-UNREACHABLE -- 0 detectors touch "
                                      "the 5,828 ms nodes; its emptiness is a coverage fact, not "
                                      "an estate fact"),
        },
        "counts": {
            "c2_motif_instances_distinct": len(nodes),
            "contains_edges": len(edges),
            "distinct_members": len(members_seen),
            "by_family": dict(per_family.most_common()),
            "by_substrate_side": dict(side_tally.most_common()),
            "by_side_status": dict(status_tally.most_common()),
            "rows_seen": rows_seen,
            "rows_skipped_ragged_unparsed": skipped_ragged,
            "rows_dropped_no_members": dropped_ragged,
            "collapsed_duplicate_member_sets": rows_seen - len(nodes),
        },
        "nodes": list(nodes.values()), "edges": edges,
    }
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1)

    print("C2 INDIVIDUATION -- one node per MATCH")
    print("  DISTINCT instances : %d   (was 19 class nodes)" % len(nodes))
    print("  CONTAINS edges    : %d over %d distinct members" % (len(edges), len(members_seen)))
    print("  DENOMINATOR rows seen: %d" % rows_seen)
    print("  rows SKIPPED unparsed: %d   rows dropped no-members: %d" % (skipped_ragged, dropped_ragged))
    print("  duplicate member-sets COLLAPSED: %d" % (rows_seen - len(nodes)))
    print("  by substrate_side : %s" % dict(side_tally.most_common()))
    print("  by side_status    : %s" % dict(status_tally.most_common()))
    print("  by family         : %s" % dict(per_family.most_common(5)))
    print("  -> %s (%.1f KB)" % (args.out, os.path.getsize(args.out) / 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
