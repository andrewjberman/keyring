#!/usr/bin/env python3
"""C3.i STRUCTURE COVER at INSTANCE grain -- keyed on the ANCHOR NODE.

DONE-MEANS item 2. Andrew-direct 2026-08-07, ruling on the open question: **"I would absolutely
say B"** -- a C3.i structure keys on the ANCHOR NODE, not the anchor TYPE.

WHY THE RULING MATTERS, in one measurement:
  anchor TYPE  ->    5 systems, FIXED FOREVER regardless of how the estate grows
  anchor NODE  ->  hundreds, scaling with the estate
Under TYPE, `sys-bd-medallion` and `sys-inf-medallion` -- two firms' entirely separate refineries --
collapse into ONE `object-data` system. **A structure that cannot tell two firms apart cannot support
a risk surface on the semantic plane**, which is what the friction battery is for.

WHAT IS REUSED, NOT REWRITTEN: `ANCHOR_CATALOG` and `HUB_TYPES` are read from
`NFRA_MOTIF_P1_canonical_ab_catalog.py` at runtime. The overlapping-domain-cover MODEL is CTO-ruled
(@f7f21f406) and already implemented there; this changes the KEY it groups on and nothing else.
Copying the catalog would let it drift -- a predicate, not a roster.

NOT connected-components: that over-merges to one supersystem and was already surfaced (@fbfa06590a).

READ-ONLY. Consumes c2_instances.json, writes c3_structures.json. Nothing is deployed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
# ONE definition of the derived accessors, imported -- never a second copy that can drift from C2's.
# These replaced module-level hardcoded C:\ literals: this module runs BOTH on the workstation and
# in the Linux derive container, and the container has no C: drive, no Git-Bash, no comp-kuzu.
from c2_individuate import _git_bash, catalog_path, repo_root   # noqa: E402 - after sys.path setup
PROMOTE_MIN = 2          # P1: "Promote a domain to a C3System only at >= 2 member motifs"


class CoverInputMissing(Exception):
    """Same law as c2_individuate.CompositionInputMissing: RAISE, never sys.exit() -- this runs
    inside the nightly derive and an exit here kills the derive, not the cover."""


def ruled_catalog():
    """ANCHOR_CATALOG + HUB_TYPES, read from the ruled implementation rather than re-typed."""
    try:
        gen = catalog_path()
        src = open(gen, encoding="utf-8").read()
    except OSError as e:
        # DECLARED TYPE, not FileNotFoundError. Measured 2026-08-07: the open() precedes every
        # other check, so an absent catalog raised OSError and a caller catching the documented
        # exception would NOT have caught it. A contract that names the wrong exception is a
        # contract for a failure that does not happen.
        raise CoverInputMissing("catalog unreadable: %s (%s)" % (catalog_path(), e)) from e
    ns: dict = {}
    # Both shapes: ANCHOR_CATALOG is a multi-line dict, HUB_TYPES a single-line set with a trailing
    # comment. The first cut matched only the multi-line form and EXITED LOUD on HUB_TYPES -- the
    # right failure, because an empty HUB_TYPES would have let LAMBDA/EC2 ANCHOR a domain and merged
    # every system into one. A silent default here would have reproduced the connected-components
    # over-merge through a different door.
    for name in ("ANCHOR_CATALOG", "HUB_TYPES"):
        m = (re.search(r"^%s = (\{.*?\n\})" % name, src, re.S | re.M)
             or re.search(r"^%s = (\{[^\n}]*\})" % name, src, re.M))
        if not m:
            raise CoverInputMissing("%s not found in %s -- REFUSING to default" % (name, catalog_path()))
        try:
            ns[name] = eval(m.group(1))                              # noqa: S307 - own repo, literal
        except SyntaxError as e:
            # Same escape as c2_individuate.catalog(): a TRUNCATED catalog raises SyntaxError past
            # the declared contract. Fixed in both halves together -- a fix applied to one of two
            # identical call sites is the residue that gets found months later by the half nobody
            # touched.
            raise CoverInputMissing(
                "%s is CORRUPT or TRUNCATED (%s in %s) -- does not parse. In-container this usually "
                "means a partial COPY, not a bad catalog." % (name, e, gen)) from e
    # The ruled model's own invariant, re-asserted here rather than trusted: HUB types create
    # overlap and never DEFINE a domain, so a hub anchor would merge every system into one.
    for dom, anc in ns["ANCHOR_CATALOG"].items():
        assert not (set(anc) & set(ns["HUB_TYPES"])), "anchor catalog must exclude hub types: " + dom
    return ns["ANCHOR_CATALOG"], ns["HUB_TYPES"]


def compose(c2_doc: dict, live_snap_fn=None) -> dict:
    """Compose C3.i structures FROM AN IN-MEMORY C2 ENVELOPE. Pure: no file I/O, no argv, no exit.

    THE DERIVE CALLS THIS WITH `c2_individuate.compose()`'s RETURN VALUE. It does not read a
    snapshot of it. Making C2 pure while leaving the C2->C3 hop file-mediated moved the staleness
    rather than removing it: measured on my own artifacts, `c3_structures.json` was written 69
    MINUTES BEFORE the `c2_instances.json` it claims to derive from -- structures composed from a
    PREVIOUS instance layer, which is this project's own defect at 69-minute resolution.
    """
    return _cover_impl(c2_doc, live_snap_fn)


def _cover_impl(doc: dict, live_snap_fn=None) -> dict:
    anchors_by_domain, hub_types = ruled_catalog()
    instances = [n for n in doc["nodes"] if n["props"].get("grain") == "instance"]

    # ---- INPUT FRESHNESS. Carrying a vintage forward is honest; not CHECKING it is not. ------
    # This whole build exists because a July artifact was consumed as if it were current. Stamping
    # the input's snapshot on the output preserves provenance but WARNS NOBODY -- a reader sees a
    # coherent, correctly-provenanced structure layer and no signal that it describes a graph that
    # has since moved. The freshness verdict is therefore EMITTED, not just printed.
    if live_snap_fn is not None:
        live_snap = live_snap_fn()      # in-container: the Iceberg snapshot id, not a comp-kuzu header
    else:
        # LOCAL reader. comp-kuzu prints its provenance header on STDERR -- reading stdout alone
        # returns None for every field, and a vintage that silently reads "unknown" looks like the
        # tool declined to answer rather than like nobody asked.
        live = subprocess.run([_git_bash(), ".tools/comp-kuzu",
                               "MATCH (n:CloudNode) RETURN count(*) AS n"],
                              cwd=repo_root(), capture_output=True, text=True, timeout=600)
        live_out = (live.stdout or "") + "\n" + (live.stderr or "")
        lm = re.search(r"nodes snapshot-id:\s*(\S+)", live_out)
        live_snap = lm.group(1).strip() if lm else None
    in_snap = (doc.get("graph_vintage") or {}).get("nodes_snapshot_id")
    # NORMALISE BEFORE COMPARING. A snapshot id arrives as a STRING from the comp-kuzu header regex
    # and as an INT from pyiceberg's `current_snapshot().snapshot_id`. Comparing them raw makes
    # `6445636748001840083 == "6445636748001840083"` FALSE, so the verdict reads STALE on every
    # production run WHILE PRINTING TWO IDENTICAL NUMBERS -- a self-contradicting message that would
    # be read as a real staleness event and send someone re-running a healthy composition.
    # Every earlier test injected strings on BOTH sides, so the mismatch was structurally unreachable
    # until the reader was executed against a real Iceberg catalog (2026-08-07).
    if live_snap is not None:
        live_snap = str(live_snap)
    if in_snap is not None:
        in_snap = str(in_snap)
    if live_snap is None or in_snap is None:
        freshness = "UNVERIFIABLE -- a snapshot id is missing; treat this layer as UNDATED"
    elif live_snap == in_snap:
        freshness = "CURRENT -- input composed against the live graph snapshot"
    else:
        freshness = ("STALE -- input snapshot %s, live graph is now %s. These structures describe a "
                     "graph that has MOVED. Re-run c2_individuate before trusting any count."
                     % (in_snap, live_snap))
    print("  INPUT FRESHNESS   : %s" % freshness)

    # (domain, anchor_node_id) -> {instance ids}. An instance may join SEVERAL systems: the cover is
    # many-to-many BY DESIGN (overlap-allowed), which is the property a partition cannot represent.
    groups: dict = defaultdict(set)
    side_of_group: dict = defaultdict(set)
    anchor_type_of: dict = {}
    orphan = 0
    for n in instances:
        pairs = n["props"].get("member_pairs") or []
        hit = False
        for nid, ntype in pairs:
            if ntype in hub_types:
                continue                      # hubs are overlap-creators, NEVER anchors
            for domain, anc in anchors_by_domain.items():
                if ntype in anc:
                    key = (domain, nid)
                    groups[key].add(n["node_id"])
                    side_of_group[key] |= set(n["props"].get("substrate_side") or [])
                    anchor_type_of[key] = ntype
                    hit = True
        if not hit:
            orphan += 1                       # contains no catalog anchor -- an HONEST coverage flag

    nodes, edges = [], []
    promoted, unpromoted = 0, 0
    by_domain = Counter()
    by_side = Counter()
    for (domain, nid), members in sorted(groups.items()):
        if len(members) < PROMOTE_MIN:
            unpromoted += 1                   # single-motif domain -- stays C2, NOT forced into a system
            continue
        sid = "sysi:%s:%s" % (domain, hashlib.sha1(nid.encode()).hexdigest()[:12])
        sides = sorted(side_of_group[(domain, nid)])
        nodes.append({
            "node_id": sid,
            "node_type": "C3System",          # REGISTERED type + grain, never a new node_type:
            "props": {                        # derive_runner fails the whole derive closed otherwise
                "grain": "instance",
                "domain": domain,
                "anchor_node": nid,
                "anchor_type": anchor_type_of[(domain, nid)],
                "model": "OVERLAPPING-DOMAIN-COVER (anchor-NODE keyed, Andrew-ruled 2026-08-07)",
                "member_motif_count": len(members),
                "substrate_side": sides,
            }})
        for m in sorted(members):
            edges.append({"source": sid, "target": m, "edge_type": "CONTAINS",
                          "props": {"layer": "C3->C2"}})
        promoted += 1
        by_domain[domain] += 1
        by_side["+".join(sides) or "NONE"] += 1

    out = {
        "producer": "3.0.0_SA_CVO c3_cover -- anchor-NODE overlapping-domain-cover (DONE-MEANS item 2)",
        # Same top-level placement as C2, for the same reason: the derive's stamp reads
        # doc.get("nodes_snapshot_id") at the ENVELOPE level. Carried from the C2 input, so a C3
        # structure is stamped with the snapshot its own members were composed against.
        "nodes_snapshot_id": (doc.get("graph_vintage") or {}).get("nodes_snapshot_id"),
        "edges_snapshot_id": (doc.get("graph_vintage") or {}).get("edges_snapshot_id"),
        "graph_vintage": doc.get("graph_vintage"),   # carried through: a system inherits its input's
        "input_freshness": freshness,                # ...and the verdict rides WITH it, not just stdout
        # TRUE NUMBERS THAT READ AS DEFECTS -- the C3 half. `by_substrate_side` is the single most
        # misdiagnosable figure this layer produces, and two other seats independently predicted it
        # would be read as broken frontend detectors. Carried IN the artifact so the explanation
        # travels with the number instead of living in messages between three agents.
        "reading_notes": {
            "by_substrate_side reads {BACKEND: N} with NO FRONTEND":
                "CORRECT AND STRUCTURAL. Do NOT diagnose this as broken frontend detectors or as a "
                "reader dropping the portal layer. A C3 structure inherits the sides of its member "
                "motifs, and no motif is cross-side because the two sides are DISCONNECTED "
                "COMPONENTS -- 28 cross-side edges estate-wide, all converging on ONE node with "
                "ZERO onward edges. The discriminating question is never 'is the reader dropping "
                "layers' but 'does a spanning path exist', and it is measured: no. See "
                "deliverables/SUBSTRATE_SIDES_ARE_DISCONNECTED_20260807.md.",
            "instances_with_no_catalog_anchor is large (~1,100 of ~6,100)":
                "An HONEST COVERAGE FLAG, not a failure. These motif instances contain no node type "
                "in the P1 ANCHOR_CATALOG, so no domain claims them. The cover REFUSES to invent an "
                "anchor for them rather than forcing them into a system.",
            "domains_unpromoted_single_motif is non-zero":
                "BY DESIGN (PROMOTE_MIN=2). A domain with one member motif stays C2 and is never "
                "promoted to a C3 structure. Not a dropped structure.",
            "this layer is always ONE derive behind":
                "STATED PROPERTY, not a defect. It composes from the LAST COMMITTED graph while the "
                "current derive is still building the next one. Compare it against the estate state "
                "of the derive that PRODUCED it -- that is what nodes_snapshot_id is for. Comparing "
                "against 'now' manufactures a false NOT-LIVE.",
        },
        "grounding": {                                # vintage or it is a number with no provenance
            "model": "OVERLAPPING-DOMAIN-COVER, CTO-ruled @f7f21f406; NOT connected-components "
                     "(over-merges to 1 supersystem, @fbfa06590a)",
            "key": "ANCHOR NODE, Andrew-ruled 2026-08-07 ('I would absolutely say B')",
            "anchor_catalog": "read at runtime from NFRA_MOTIF_P1_canonical_ab_catalog.py",
            "promote_min": PROMOTE_MIN,
        },
        "counts": {
            "c3_structures_promoted": promoted,
            "domains_unpromoted_single_motif": unpromoted,
            "instances_with_no_catalog_anchor": orphan,
            "instances_considered": len(instances),
            "contains_edges": len(edges),
            "by_domain": dict(by_domain.most_common()),
            "by_substrate_side": dict(by_side.most_common()),
        },
        "nodes": nodes, "edges": edges,
    }
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="src", default=os.path.join(HERE, "c2_instances.json"))
    ap.add_argument("--out", default=os.path.join(HERE, "c3_structures.json"))
    args = ap.parse_args()
    try:
        out = compose(json.load(open(args.src, encoding="utf-8")))
    except CoverInputMissing as e:
        print("FATAL: %s" % e)
        return 2
    promoted = out["counts"]["c3_structures_promoted"]
    unpromoted = out["counts"]["domains_unpromoted_single_motif"]
    orphan = out["counts"]["instances_with_no_catalog_anchor"]
    instances = [1] * out["counts"]["instances_considered"]
    edges = out["edges"]
    by_domain = Counter(out["counts"]["by_domain"])
    by_side = Counter(out["counts"]["by_substrate_side"])
    json.dump(out, open(args.out, "w", encoding="utf-8"), indent=1)

    print("C3.i COVER -- anchor-NODE keyed (Andrew-ruled B)")
    print("  C3 STRUCTURES PROMOTED     : %d      (was 4 class nodes; anchor-TYPE would give 5)"
          % promoted)
    print("  unpromoted (single motif)  : %d      -- stay C2, never forced into a system" % unpromoted)
    print("  instances with NO anchor   : %d of %d  -- honest coverage flag, not a failure"
          % (orphan, len(instances)))
    print("  CONTAINS edges             : %d" % len(edges))
    print("  by domain                  : %s" % dict(by_domain.most_common()))
    print("  by substrate_side          : %s" % dict(by_side.most_common()))
    print("  -> %s" % args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
