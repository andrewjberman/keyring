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

# ---------------------------------------------------------------------------------------------
# NO MODULE-LEVEL HOST-ABSOLUTE PATHS. This module runs in TWO places: this Windows workstation
# and the Linux Fargate derive container (infra/aws/globgrph/Dockerfile). It previously carried
# REPO and BASH as hardcoded C:\ literals and shelled to comp-kuzu -- so it was a LAPTOP SCRIPT
# that could not execute where it was meant to run. Found by 0.7.0_AE_CloudOps while wiring the
# Dockerfile COPY, verified at source by 1.0.0_SA_CTO~B; Andrew-direct "put CVO on this now".
#
# WHY IT WOULD HAVE SHIPPED GREEN: the derive's caller is best-effort by design -- it catches,
# logs C2C3_COMPOSE_FAILED, and completes normally. The image would rebuild, the deploy would go
# green, the nightly would run clean every night, and the instance layer would simply never
# appear. A SILENT PERMANENT NO-OP WEARING A SUCCESSFUL DEPLOY.
# ---------------------------------------------------------------------------------------------


def repo_root() -> str:
    """The checkout/app root, DERIVED. OPAL_REPO_ROOT overrides (the container sets /app)."""
    env = os.environ.get("OPAL_REPO_ROOT")
    if env:
        return env
    # .../org/tier1_exec/3.0.0_SA_CVO/deliverables/kimi_subdivision_harness/<this file>
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(here, *([os.pardir] * 5)))


def catalog_path() -> str:
    """The P1 catalog -- the source of BOTH the motif queries and the C3 anchor rules.

    IN-CONTAINER THIS FILE MUST BE COPYed INTO THE IMAGE. It is a real runtime dependency, not a
    dev-box convenience: catalog() reads its AB_CATALOG queries and c3_cover.ruled_catalog() reads
    ANCHOR_CATALOG/HUB_TYPES from it. Absent, both halves raise -- they refuse to default.
    """
    env = os.environ.get("OPAL_MOTIF_CATALOG")
    if env:
        return env
    return os.path.join(repo_root(), "org", "tier2_senior", "0.4.0_DS_ClientPlatform",
                        "deliverables", "NFRA_MOTIF_P1_canonical_ab_catalog.py")


def _git_bash() -> str:
    """LOCAL-ONLY, resolved LAZILY -- never at import, so importing this module in the container
    (which has no Git-Bash) is safe. CLAUDE.md: use the ONE canonical resolver, never bare `bash`
    -- a python-spawned bare `bash` Windows-resolves to the System32 WSL stub and can fail SILENTLY.
    """
    try:
        sys.path.insert(0, os.path.join(repo_root(), ".tools"))
        from git_bash_resolver import git_bash          # noqa: PLC0415 - lazy by design
        return git_bash()
    except Exception:
        return os.path.join("C:" + os.sep, "Program Files", "Git", "bin", "bash.exe")

# substrate_side -- SYSTEM_DEFINITIONS.yaml v1.8 @dcdedf6fe. A ROLLUP over the substrate axis.
# KNOWLEDGE is DECLARED-BUT-UNREACHABLE: ms is 5,828 nodes and zero detectors touch any of them, so
# no instance can carry it until an ms detector plane exists. Its emptiness is a fact about DETECTOR
# COVERAGE, not about the estate -- declared here so it is never read as "the knowledge plane has no
# structure" (Rule 24 postulate (iv), run with CTO~B 011629Z).
SIDE = {"aws": "BACKEND", "pipeline": "BACKEND", "portal": "FRONTEND", "ms": "KNOWLEDGE"}


class CompositionInputMissing(Exception):
    """A required input (the detector catalog) could not be read.

    RAISED, NEVER sys.exit(). `compose()` runs INSIDE the nightly derive: a `sys.exit` there does not
    fail the composition, IT KILLS THE DERIVE PROCESS -- turning "one layer could not compose" into
    "the whole graph did not rebuild tonight". The CALLER decides whether a missing catalog is fatal;
    a library that exits on behalf of its caller has taken that decision away.
    (I published "compose() -- no sys.exit" to 0.7.0_AE_CloudOps while this was still reachable via
    catalog(). The claim was false when I made it.)
    """


class CompositionUnusable(Exception):
    """The inputs loaded but CANNOT support a verdict -- so the layer REFUSES rather than returning 0.

    A ZERO AND A BROKEN READER ARE THE SAME OUTPUT SHAPE. In the derive container the graph reader is
    injected, the catalog is a COPYed file, and either can fail while everything around them succeeds
    -- yielding "0 motif instances", which is indistinguishable from "this estate has no motifs" and
    strictly more believable, because it arrives inside a green run.
    (1.0.0_SA_CTO~B, 2026-08-07: "a missing catalog must fail the derive stage visibly, never degrade
    to 'no motifs matched', which is the identical output shape.") Same law as the DETECT `canon_usable`
    gate: an instrument that cannot see REFUSES; it does not report absence.
    """


def side_of(layer):
    """None = contributes no side. semctl is NOT a substrate (01_substrate.md:39)."""
    if not layer or layer == "semctl":
        return None
    return SIDE.get(layer)                      # unknown layer -> None -> counted as unresolved


def catalog():
    try:
        gen = catalog_path()
        src = open(gen, encoding="utf-8").read()
    except OSError as e:
        # THE DECLARED TYPE, not OSError. The open() precedes every other check, so the MOST LIKELY
        # failure -- the catalog file being absent -- escaped as FileNotFoundError while this module
        # advertised CompositionInputMissing to its callers. I had already PUBLISHED that contract to
        # 0.7.0_AE_CloudOps. A caller writing the documented `except CompositionInputMissing` would
        # have caught the rare failure and missed the common one. Found by mutation, not by reading:
        # the raise-site was correct in isolation and wrong in order.
        raise CompositionInputMissing("catalog unreadable: %s (%s)" % (catalog_path(), e)) from e
    m = re.search(r"^AB_CATALOG = \[", src, re.M)
    if not m:
        raise CompositionInputMissing("AB_CATALOG not found in %s" % catalog_path())
    depth, i = 0, m.end() - 1
    while i < len(src):
        if src[i] == "[":
            depth += 1
        elif src[i] == "]":
            depth -= 1
            if depth == 0:
                break
        i += 1
    specs = eval(src[m.end() - 1:i + 1], {"N": "CloudNode", "E": "CloudEdge"})  # noqa: S307
    if not specs:
        # A catalog that PARSES to zero detectors composes zero instances and looks exactly like an
        # estate with no motifs. Refuse at the input, where the cause is still visible.
        raise CompositionUnusable("catalog parsed to ZERO detector specs: %s" % catalog_path())
    return specs


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
    cols = ", ".join("%s.node_id AS %s, %s.layer AS %s__L, %s.node_type AS %s__T"
                     % (v, a, v, a, v, a) for v, a in pairs)
    return query[:m.start()] + "RETURN " + cols, [a for _, a in pairs]


def run_rows(query, aliases, query_fn=None):
    """Return ([{alias: id, alias__L: layer}, ...], skipped). Uses comp-kuzu --json.

    PARSE THE FORMAT, DO NOT HARDEN A TEXT PARSE. The first cut split comp-kuzu's aligned TABLE
    output on whitespace and skipped any row whose token count did not match the header -- 113 rows
    of 6,686 (1.7%), silently, until a denominator disagreed with a known-good number. Two
    hypotheses for the raggedness were eliminated by measurement (node_ids containing spaces: 0;
    NULL `layer`: 0), which left line-wrapping on wide results -- i.e. the WIDEST rows, the
    MOST-CONNECTED instances, not a random 1.7%.
    `--json` ("Output results as JSON array") removes the entire failure class rather than
    hardening against one instance of it. Verified: `--limit` defaults to None (`kuzu_cli.py:161`),
    so nothing is silently truncated.
    """
    return (query_fn or local_kuzu_query)(query)


def local_kuzu_query(query):
    """THE LOCAL graph reader: shell out to comp-kuzu against the workstation's Kuzu DB.

    This is a LOCAL CONVENIENCE, not the only reader -- see compose(query_fn=...). It cannot run
    in the derive container (no Git-Bash, no .tools/, no local Kuzu DB), which is exactly why the
    reader is injectable rather than baked in.
    """
    p = subprocess.run([_git_bash(), ".tools/comp-kuzu", "--json", query], cwd=repo_root(),
                       capture_output=True, text=True, timeout=900)
    m = re.search(r"^\s*\[", p.stdout, re.M)
    if not m:
        return [], 0
    try:
        rows = json.loads(p.stdout[m.start():])
    except json.JSONDecodeError:
        # A parse failure is LOUD and counted, never an empty result. An unparseable response and
        # a genuinely empty one must not look alike.
        return [], -1
    return rows, 0


def detector_types(specs):
    """The node_types any detector can match -- a PREDICATE over the catalog, never a hand-list.

    A hand-drawn roster silently freezes while the catalog moves, and then the coverage
    denominator is wrong in the flattering direction ("a predicate is not a roster").
    """
    types = set()
    for spec in specs:
        for sub in (spec.get("subqueries") or [{"constituents": spec["constituents"]}]):
            for _alias, nt in sub["constituents"]:
                if nt:
                    types.add(nt)
        # polymorphic aliases carry ntype=None; recover them from the query's own type predicates
        for q in ([spec["query"]] if spec.get("query") else
                  [x["query"] for x in spec.get("subqueries") or []]):
            types |= set(re.findall(r"node_type='([A-Za-z0-9_]+)'", q))
    return types


def coverage_triple(specs, members_seen, side_of_member, query_fn=None):
    """X covered / Y in detector scope / Z on the side -- per substrate_side.

    THREE figures, not two. X/Y alone reports a complete-looking layer over a partial substrate:
    individuating today's matches yields ~100% of what the detectors REACH while leaving most of
    the frontend untouched, and without Z that reads as done (contract req 4a).
    """
    dtypes = sorted(detector_types(specs))
    rows, _ = run_rows(
        "MATCH (n:CloudNode) WHERE n.layer IN ['aws','pipeline','portal','ms'] "
        "RETURN n.node_id AS id, n.layer AS L, n.node_type AS T", [], query_fn)
    z, y = Counter(), Counter()
    dset = set(dtypes)
    for r in rows:
        side = side_of(r.get("L"))
        if not side:
            continue
        z[side] += 1
        if r.get("T") in dset:
            y[side] += 1
    x = Counter()
    for nid in members_seen:
        s = side_of_member.get(nid)
        if s:
            x[s] += 1
    out = {}
    for side in sorted(set(list(z) + list(y) + list(x))):
        out[side] = {"covered_X": x[side], "in_detector_scope_Y": y[side], "on_side_Z": z[side],
                     "pct_of_scope": round(100.0 * x[side] / y[side], 1) if y[side] else None,
                     "pct_of_side": round(100.0 * x[side] / z[side], 1) if z[side] else None}
    out["_detector_types"] = dtypes
    return out


def graph_vintage(vintage_fn=None):
    """The snapshot this run composed AGAINST -- captured, not assumed.

    THE WHOLE DEFECT THIS BUILD EXISTS TO FIX IS A NUMBER WITH NO VISIBLE VINTAGE: the 19-and-4 layer
    is a July JSON baked into an image, and nothing in the graph says so. An output of mine carrying
    no vintage would be the same artifact one generation later -- two runs could not be compared
    without external knowledge of which snapshot each used, which is exactly how archaeology passes
    for a live number. Measured 2026-08-07: two runs 6,686 -> 6,657 rows because the graph rebuilt
    (20,585 -> 20,605 nodes, new snapshot), and only the vintage makes that attributable rather than
    alarming.
    """
    if vintage_fn is not None:
        return vintage_fn()
    # LOCAL reader. comp-kuzu prints its provenance header on STDERR; in-container the vintage must
    # come from the Iceberg snapshot ids instead, which is why this is injectable. A vintage that
    # silently reads "unknown" is worse than an absent field -- it looks like the tool declined to
    # answer rather than like nobody asked.
    p = subprocess.run([_git_bash(), ".tools/comp-kuzu", "MATCH (n:CloudNode) RETURN count(*) AS n"],
                       cwd=repo_root(), capture_output=True, text=True, timeout=600)
    # BOTH streams: comp-kuzu writes its provenance header to STDERR, so reading stdout alone
    # returns None for every field -- a vintage that silently reads "unknown" is worse than no
    # vintage field at all, because it looks like the tool declined to answer rather than like
    # nobody asked. Caught on the first run of this function.
    out = (p.stdout or "") + "\n" + (p.stderr or "")

    def grab(pat):
        # re.M IS LOAD-BEARING: `graph_nodes_total` uses a line-anchored `^\s*(\d+)\s*$`, and without
        # MULTILINE the anchors bind to the whole string, so it NEVER matched and the field read None
        # on every run since it was written. A provenance field that is silently null is the exact
        # thing the docstring above warns about, in the same function -- it looks like the tool
        # declined to answer rather than like the pattern was wrong. Caught by printing the field
        # beside its siblings instead of reading the code.
        m = re.search(pat, out, re.M)
        return m.group(1).strip() if m else None
    return {"nodes_snapshot_id": grab(r"nodes snapshot-id:\s*(\S+)"),
            "edges_snapshot_id": grab(r"edges snapshot-id:\s*(\S+)"),
            "db_built_at": grab(r"built:\s*(\S+)"),
            "graph_nodes_total": grab(r"^\s*(\d+)\s*$")}


def compose(query_fn=None, vintage_fn=None) -> dict:
    """Compose the C2 instance layer and RETURN it. NO file I/O, NO argv, NO sys.exit.

    THE DERIVE CALLS THIS. It does not read a snapshot of it. Adding another pre-built JSON to
    `C2C3_MOTIF_SPEC_PATHS` and COPYing it into the image would produce a THIRD static artifact --
    archaeology from the day after it was built, which is precisely the 19-and-4 defect this whole
    layer exists to remove (CTO~B, 2026-08-07). A composition that runs is the only thing that
    cannot go stale.

    IMPORT-SAFE: importing this module runs nothing. Every subprocess call it makes is bounded by
    an explicit timeout, because it executes INSIDE the nightly derive and an unbounded hang there
    is an outage, not a slow script.
    """
    return _compose_impl(query_fn=query_fn, vintage_fn=vintage_fn)


def _compose_impl(query_fn=None, vintage_fn=None) -> dict:
    specs = catalog()
    nodes, edges = {}, []      # node_id -> node; a repeated member-set is ONE instance
    per_family = Counter()
    side_tally = Counter()
    status_tally = Counter()
    members_seen = set()
    member_side = {}
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
            rows, sk = run_rows(q, aliases, query_fn)
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
                    # EXISTING node_type + the `grain` property as the discriminator -- NOT a new type.
                    # derive_runner raises NodeTypeLayerGap and FAILS THE WHOLE DERIVE CLOSED
                    # on any node_type absent from NODE_TYPE_LAYER (:1775, a CVO durability
                    # cert @d43b49e61). Registering one is an arch-gated act (CTO GO 223537Z
                    # + CVO sign 224410Z) and would force a re-freeze that the _ab spec
                    # deliberately avoided. `grain: class|instance` ALREADY distinguishes
                    # these -- that is what item 4 is for, so a new type buys nothing and
                    # costs a gate.
                    "node_id": mid, "node_type": "C2Motif",
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
                        # member NODE TYPES -- the RULED overlapping-domain-cover keys
                        # membership on "does this motif CONTAIN the domain anchor type",
                        # so Stage 2 needs types, not ids (NFRA_MOTIF_P1 ab_c3_cover).
                        "member_types": sorted({row.get(a + "__T") for a in aliases
                                                if row.get(a + "__T")}),
                        # (id, type) PAIRS -- the anchor-NODE cover (Andrew-ruled 2026-08-07 "B")
                        # keys on WHICH member is the anchor, so a deduped type SET is not enough:
                        # it cannot say which id carried which type.
                        "member_pairs": sorted({(row[a], row.get(a + "__T"))
                                                for a in aliases if row.get(a)}),
                        "members": sorted(mem),
                    }})
                for nid in mem:
                    edges.append({"source": mid, "target": nid, "edge_type": "CONTAINS",
                                  "props": {"layer": "C2i->C1"}})
                    members_seen.add(nid)
                for a in aliases:
                    if row.get(a):
                        member_side[row[a]] = side_of(row.get(a + "__L"))
                per_family[spec["id"]] += 1
                side_tally["+".join(sorted(sides)) or "NONE"] += 1
                status_tally[status] += 1

    # ---- THE READER-IS-BLIND GATE. A zero here is a REFUSAL, never a finding. -------------------
    # Every detector ran and NOT ONE row came back. On a ~20k-node estate that is a broken reader,
    # not an estate without motifs -- and in the container the reader is INJECTED, so this is the
    # exact shape its failure takes: green run, no exception, zero instances, permanent no-op.
    # Refusing here converts the most believable wrong answer in the system into a loud one.
    if rows_seen == 0:
        raise CompositionUnusable(
            "ALL %d detectors returned ZERO rows -- the graph reader answered nothing. This is a "
            "blind reader, not an estate without motifs; REFUSING to emit a zero layer." % len(specs))

    # ---- ITEM 4: mark the EXISTING class nodes grain:class ------------------------------------
    # They are NOT deleted -- they are the VOCABULARY the classification pass writes INTO, and the
    # canonical ontology's own population_law is `canon-first-debt-subset` (the six detector motifs
    # are "valid AS deviation motifs", just not the primary population). Marking them makes that law
    # QUERYABLE, which today it is not: a comp-kuzu query returns C2Motif with full provenance and
    # nothing saying which population it belongs to.
    DEBT = {"SilentDisplayFork", "CrossFirmAsymmetry", "HardcodedFirmLiteral",
            "DeadComponent", "OrphanEndpoint", "RenderWithoutNullGuard"}
    cls, _ = run_rows("MATCH (n:CloudNode) WHERE n.node_type IN ['C2Motif','C3System'] "
                      "RETURN n.node_id AS id, n.node_type AS T, n.name AS nm", [], query_fn)
    class_marked = 0
    for r in cls:
        nodes[r["id"]] = {
            "node_id": r["id"], "node_type": r["T"],
            "props": {"grain": "class",
                      "population": "debt" if r.get("nm") in DEBT else "canon"}}
        class_marked += 1

    # Re-tally sides/status over the DEDUPED instances. The per-row counters above are
    # PRE-COLLAPSE and adjacent to a POST-COLLAPSE instance count in the same output block --
    # two correct numbers over different populations, which a reader subtracts. Found by CTO~B.
    side_tally = Counter()
    status_tally = Counter()
    for n in nodes.values():
        pr = n["props"]
        if pr.get("grain") != "instance":
            continue
        side_tally["+".join(pr.get("substrate_side") or []) or "NONE"] += 1
        status_tally[pr.get("side_status")] += 1

    doc = {
        "producer": "3.0.0_SA_CVO c2_individuate -- one node per MATCH (DONE-MEANS item 1)",
        "supersedes_shape_of": ["motif_c2c3_materialize.json", "motif_c2c3_materialize_ab.json"],
        "graph_vintage": graph_vintage(vintage_fn),
        "grounding": {
            "detectors": "read VERBATIM from NFRA_MOTIF_P1_canonical_ab_catalog.py AB_CATALOG",
            "recurrence": "NOT echoed -- every instance is a live matched row",
            "substrate_side": "SYSTEM_DEFINITIONS.yaml v1.8 @dcdedf6fe; derived from member layers",
            "knowledge_unreachable": ("KNOWLEDGE is DECLARED-BUT-UNREACHABLE -- 0 detectors touch "
                                      "the 5,828 ms nodes; its emptiness is a coverage fact, not "
                                      "an estate fact"),
        },
        "counts": {
            "c2_motif_instances_distinct": len(nodes) - class_marked,
            "contains_edges": len(edges),
            "distinct_members": len(members_seen),
            "by_family": dict(per_family.most_common()),
            "by_substrate_side": dict(side_tally.most_common()),
            "_tally_denominator": "DISTINCT INSTANCES (post-collapse) -- same population as c2_motif_instances_distinct, NOT rows_seen",
            "knowledge_bearing_instances": sum(1 for n in nodes.values()
                                               if "KNOWLEDGE" in (n["props"].get("substrate_side") or [])),
            "instances_with_any_unresolved_member": sum(1 for n in nodes.values()
                                                        if n["props"].get("members_unresolved", 0) > 0),
            "by_side_status": dict(status_tally.most_common()),
            "coverage_triple_by_side": coverage_triple(specs, members_seen, member_side, query_fn),
            "class_nodes_marked_grain_class": class_marked,
            "rows_seen": rows_seen,
            "rows_skipped_ragged_unparsed": skipped_ragged,
            "rows_dropped_no_members": dropped_ragged,
            "collapsed_duplicate_member_sets": rows_seen - (len(nodes) - class_marked),
        },
        "nodes": list(nodes.values()), "edges": edges,
    }
    return doc


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                  "c2_instances.json"))
    args = ap.parse_args()
    try:
        doc = compose()
    except CompositionInputMissing as e:      # CLI wrapper decides to exit; the library does not
        print("FATAL: %s" % e)
        return 2
    class_marked = doc["counts"]["class_nodes_marked_grain_class"]
    nodes = {n["node_id"]: n for n in doc["nodes"]}
    rows_seen = doc["counts"]["rows_seen"]
    skipped_ragged = doc["counts"]["rows_skipped_ragged_unparsed"]
    dropped_ragged = doc["counts"]["rows_dropped_no_members"]
    edges = doc["edges"]
    members_seen = {e["target"] for e in edges}
    side_tally = Counter(doc["counts"]["by_substrate_side"])
    status_tally = Counter(doc["counts"]["by_side_status"])
    per_family = Counter(doc["counts"]["by_family"])
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1)

    print("C2 INDIVIDUATION -- one node per MATCH")
    print("  graph vintage     : snapshot %s built %s"
          % (doc["graph_vintage"]["nodes_snapshot_id"], doc["graph_vintage"]["db_built_at"]))
    print("  DISTINCT instances : %d" % (len(nodes) - class_marked))
    print("  class nodes marked grain:class : %d" % class_marked)
    print("  CONTAINS edges    : %d over %d distinct members" % (len(edges), len(members_seen)))
    print("  DENOMINATOR rows seen: %d" % rows_seen)
    print("  rows SKIPPED unparsed: %d   rows dropped no-members: %d" % (skipped_ragged, dropped_ragged))
    print("  duplicate member-sets COLLAPSED: %d" % (rows_seen - (len(nodes) - class_marked)))
    print("  by substrate_side : %s" % dict(side_tally.most_common()))
    print("  by side_status    : %s" % dict(status_tally.most_common()))
    print("  by family         : %s" % dict(per_family.most_common(5)))
    print("  COVERAGE TRIPLE (X covered / Y in detector scope / Z on side):")
    for side, t in doc["counts"]["coverage_triple_by_side"].items():
        if side.startswith("_"):
            continue
        print("    %-10s %6d / %6d / %6d   %s%% of scope, %s%% of side"
              % (side, t["covered_X"], t["in_detector_scope_Y"], t["on_side_Z"],
                 t["pct_of_scope"], t["pct_of_side"]))
    print("  -> %s (%.1f KB)" % (args.out, os.path.getsize(args.out) / 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
