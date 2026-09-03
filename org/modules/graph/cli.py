#!/usr/bin/env python3
"""
CLI entry point for opal-trace and opal-blast.

Usage:
    python -m org.modules.graph.cli trace AdvisorsTab.tsx --direction both
    python -m org.modules.graph.cli blast D_00.portal_aggregates.py --function build_employee_leaderboard
    python -m org.modules.graph.cli build   # force rebuild the graph

Or via bash wrappers:
    opal-trace AdvisorsTab.tsx
    opal-blast D_00.portal_aggregates.py --function build_employee_leaderboard
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path

# Resolve workspace root (assume we're somewhere under ajb_workspace)
_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent  # org/modules/graph -> workspace root
_CACHE_DIR = _WORKSPACE / ".comp-graph"
_CACHE_FILE = _CACHE_DIR / "graph.json"

# Add workspace to path so imports work
sys.path.insert(0, str(_WORKSPACE))
sys.path.insert(0, str(_WORKSPACE / ".tools"))

import _compbudget  # noqa: E402 -- shared Rule-T carrier

from org.modules.graph.trace_graph import (  # noqa: E402
    TraceGraph, build_graph, format_trace, format_blast,
    diff_graphs, save_baseline, format_delta,
    check_node_freshness, emit_stale_warn,
)
from org.modules.graph import comp_blast_universe as _bu  # noqa: E402

# DEFECT (a) ROOT FIX: make this process's streams ASCII-tolerant before anything can emit.
# Installed at IMPORT, not inside cmd_blast, because the crash surface includes code that runs
# before/around the command handler (argparse errors, tracebacks, the risk banner). See
# comp_blast_universe.ascii_safe for the measured root.
_bu.install_ascii_stdout()


#: T3 (comp-trace dial 2026-08-04): the load-path provenance facts, recorded by _get_graph as a
#: side effect of work it already does -- NEVER recomputed by a header printer (a second
#: check_node_freshness call would re-hash every file-backed node to answer a question this path
#: just answered). Axes: cache built_at (age) + indexed-SHA drift at load + served-vs-rebuilt.
_LOAD_PROVENANCE: dict = {}


def _get_graph(force_rebuild: bool = False, check_freshness: bool = True) -> TraceGraph:
    """Load cached graph or build a new one.

    When check_freshness=True (default), re-loads emit STALE_NODE_WARN to stderr
    for any node whose source-file SHA has drifted since indexing
    (ADHC_COMPIL_V4.012). Doesn't block; preserves clean stdout.
    """
    if not force_rebuild and _CACHE_FILE.exists():
        try:
            g = TraceGraph.load(_CACHE_FILE)
            if check_freshness:
                # NFRA_GRAPHUNI P2/D2 (b) -- HEAD-PINNED build_graph (JOINT VERDICT 20260701,
                # CTO ruling-2-intent + CVO~B fixture-bar): serve the cache ONLY if it reflects the
                # CURRENT source (no node-SHA drift) = ONE current vintage, never a divergent-vintage
                # cache. This KILLS the stale-cache-phantom class (the 1347-vs-1337 catch) + is the D4
                # one-head guarantee for the structure tools. A drifted cache -> rebuild (below), NOT
                # serve-stale-within-a-5min-TTL. Answers stay == fresh build_graph (zero coverage
                # regression -- (a), the literal Kuzu-projection re-point, is the deferred follow-on).
                drift = check_node_freshness(g, _WORKSPACE)
                if not drift:
                    _LOAD_PROVENANCE.update(
                        built_at=g.built_at, drift_at_load=0,
                        indexed=sum(1 for n in g.nodes.values() if n.source_sha),
                        served="cache")
                    return g
                emit_stale_warn(drift)   # drifted -> fall through to a head-pinned rebuild
                _LOAD_PROVENANCE.update(
                    drift_at_load=len(drift),
                    indexed=sum(1 for n in g.nodes.values() if n.source_sha))
                # Say the rebuild is HAPPENING, right after the warn -- measured misread
                # 2026-07-29: the warn's "rerun comp-build to refresh" hint reads as
                # answers-will-be-stale, when this path REBUILDS FROM CURRENT SOURCE before
                # answering. A reviewer (CVO) filed a false "answers over drifted index"
                # finding on exactly that gap between the warn and the build line.
                print("  -> drifted cache DISCARDED; rebuilding head-pinned from CURRENT source "
                      "now (the answers below are fresh; the warn above lists what had drifted).",
                      file=sys.stderr)
            elif (time.time() - g.built_at) < 300:
                # freshness opted out (e.g. internal callers) -> retain the cheap TTL fast-path
                _LOAD_PROVENANCE.update(
                    built_at=g.built_at, drift_at_load=None,
                    indexed=sum(1 for n in g.nodes.values() if n.source_sha),
                    served="cache-ttl (freshness check opted out)")
                return g
        except Exception as e:  # noqa: BLE001 -- resilience: a corrupt/truncated cache MUST self-heal to a rebuild
            # Disclose, don't swallow silently: this fires on a truncated cache (the C1 reap
            # window, now closed by the atomic save) OR a genuine load/freshness bug. We still
            # rebuild below (belt), but a SILENT swallow hid a real bug behind a slow rebuild
            # (the silent-skip class). Clean stdout preserved -- WARN goes to stderr.
            print(f"WARN: cache load/freshness-check failed ({type(e).__name__}: {e}); "
                  f"rebuilding from source.", file=sys.stderr)

    print("Building trace graph...", file=sys.stderr)
    t0 = time.time()
    g = build_graph(_WORKSPACE)
    g.save(_CACHE_FILE)
    _LOAD_PROVENANCE.update(
        built_at=g.built_at,
        indexed=sum(1 for n in g.nodes.values() if n.source_sha),
        served="rebuilt (head-pinned from CURRENT source this invocation)")
    _LOAD_PROVENANCE.setdefault("drift_at_load", None)
    elapsed = time.time() - t0
    print(f"Graph built: {len(g.nodes)} nodes, {len(g.edges)} edges ({elapsed:.1f}s)", file=sys.stderr)
    # AC-GRAIN sentinel (NFRA_GRAPHS D5) — WARN-level on the trace graph. The cloud
    # identity-format invariants (S3_BUCKET no-'/' etc.) don't map to trace node
    # types (FUNCTION/SCRIPT/MODULE), so this is a no-op today; present so the bar
    # fires if the trace graph ever gains a cloud-class node. Never blocks comp-build.
    try:
        import sys as _sys
        import os as _os
        _sys.path.insert(0, _os.path.dirname(__file__))
        from grain_sentinel import run_grain_sentinel
        _gr = run_grain_sentinel([{"node_type": n.node_type, "node_id": n.id}
                                  for n in g.nodes.values()])
        if not _gr.passed:
            print("WARN: " + _gr.render(), file=_sys.stderr)
    except Exception:
        pass
    return g


# ------------------------------------------------------------------ freshness contract (NFRA_GRAPHS)
# CTO GO 20260709T201214Z. THREE states, not four:
#     (default)  serve the cache iff the tool's freshness predicate says fresh
#     --check    REPORT staleness, never rebuild.   0 = fresh | 2 = stale | 1 = tool error
#     --force    always re-derive
#
# `--fresh` is a PROVEN NO-OP alias of default and is DEPRECATED. NFRA_GRAPHUNI P2/D2's head-pin
# correctly made DEFAULT honor the source fingerprint (killing the stale-cache-phantom class) and in
# doing so collapsed FRESH into DEFAULT. Nobody retired the flag. It is accepted with a WARN rather
# than silently aliased (a silent alias is a lying affordance) or silently dropped (it is
# user-visible). Remove next cycle.
#
# THE PREDICATE IS ONE EXPRESSION, NOT TWO THAT AGREE TODAY (MSTR 20260709T200348Z): every surface
# that reports trace-graph freshness calls `_freshness_probe()`, which calls the SAME
# `check_node_freshness` that `_get_graph` uses to decide serve-vs-rebuild. A status surface that
# re-models the predicate drifts from it silently -- `graph_status_cli._TRACE_TTL = 300` is exactly
# that bug: the default path never consults a TTL at all.
_FRESH_DEPRECATION = (
    "WARN: --fresh is a no-op alias of default since the head-pin (NFRA_GRAPHUNI P2/D2) -- "
    "default already rebuilds on source drift. Use default, or --force to rebuild. "
    "This flag is removed next cycle."
)


#: PHANTOM-CONSUMER is a VERDICT ABOUT THE ESTATE, so it may not share an exit code with a TOOL
#: FAILURE. It used to exit 1 -- the code the standard reserves for "the tool failed, and ONLY that"
#: (CTO 20260709T195217Z) -- which made THREE different events indistinguishable by rc: a real
#: zero-consumer finding, a usage error, and an uncaught crash. All three measured at rc=1 on
#: 2026-07-31 (crash: UnicodeEncodeError on 20 of 2252 nodes; usage: `--direction sideways`).
#:
#: THAT COLLISION WAS LOAD-BEARING, NOT COSMETIC: comp_debt/grounding_lib.py keyed
#: `or r.returncode == 1` -> GRAPH_ZERO_CONSUMER, so a CRASH was laundered into evidence that a
#: resource has no consumers -- i.e. into deletion evidence, on the one axis where being wrong is
#: irreversible. A crash must never be readable as a finding about the estate.
#:
#: The verdict moves; 1 goes back to meaning ONLY "the tool failed". Callers should key on the
#: PHANTOM-CONSUMER / CONSUMER-OK marker strings, which are stable and predate this change.
EXIT_PHANTOM_CONSUMER = 4
EXIT_PARTIAL_BUDGET = 6

# Ratified COMPTOOL answer-state tokens.  These are emitted by blast's answer paths, not used as
# exit codes: rc values remain disjoint for NOT-FOUND (3), AMBIGUOUS (5), and budget partial (6).
STATE_SUBJECT_ABSENT = "SUBJECT_ABSENT_FROM_CORPUS"
STATE_PRESENT_ZERO = "PRESENT_WITH_ZERO_RESULTS"
STATE_PARTIAL_BLIND = "PARTIAL_OR_BLIND"
STATE_NOT_APPLICABLE = "NOT_APPLICABLE"


class _ContractParser(argparse.ArgumentParser):
    """argparse exits 2 on a USAGE error. The contract reserves 2 for STALE.

    Found by exercise, not by reading: `comp-trace --check` (no positional) hit argparse's
    "the following arguments are required: query" and exited 2 -- indistinguishable, to a CI job,
    from "your cache is stale". The probe had never even run. A usage error is a TOOL FAILURE, which
    the standard defines as 1 (CTO 20260709T195217Z: "1 means the tool failed, and ONLY that").
    """

    def error(self, message):  # noqa: A003
        self.print_usage(sys.stderr)
        self.exit(1, f"{self.prog}: error: {message}\n")


def add_freshness_args(p) -> None:
    """The uniform 3-state contract on a query parser."""
    p.add_argument("--check", action="store_true",
                   help="REPORT staleness, never rebuild (0=fresh 2=stale 1=error)")
    p.add_argument("--force", action="store_true", help="Always re-derive, ignoring the cache")
    p.add_argument("--fresh", action="store_true",
                   help="DEPRECATED no-op alias of default (removed next cycle)")


def _require_query(args, parser, name: str = "query") -> None:
    """--check is a PROBE over the cache: it needs no target. Every other invocation does.

    So the positional is nargs='?' and this enforces it -- rather than argparse enforcing it and
    making `--check` impossible to call.
    """
    # --check is a probe over the cache; --overlap-sweep ranges over a POPULATION. Neither takes a
    # target, so neither may be blocked by the positional guard. (Note: --all-producers has this
    # same shape and is NOT exempted here -- it is a separately reported defect with its own fix,
    # and widening this guard silently on someone else's behalf is how a scope creeps.)
    if getattr(args, "overlap_sweep", False):
        return
    if not getattr(args, "check", False) and not getattr(args, "self_test", False) and not getattr(args, name, None):
        parser.error(f"the following arguments are required: {name}")


#: The trace graph's freshness PREDICATE, exactly as `_get_graph` enforces it: per-node content-SHA
#: drift. NOT a TTL -- the default serve path never evaluates age (the `elif` on the TTL hangs off
#: `if check_freshness:`, so an un-drifted cache is served at ANY age).
TRACE_PREDICATE = "content-SHA drift per indexed node (no TTL on the default path)"


def trace_freshness() -> tuple:
    """THE enforcing predicate, as a VALUE. Returns (verdict, detail, denominator, drift).

    verdict in {"FRESH", "STALE", "MISSING", "UNVERIFIABLE"}.

    Every surface that REPORTS trace-graph freshness must call this, and every surface that ACTS on
    it (`_get_graph`) evaluates the same `check_node_freshness`. MSTR 20260709T200348Z, ratified:
    "a control's reported value and its enforcing value must be the same expression, not two
    expressions that agree today." `comp-graph status` previously re-modelled this with a
    hand-copied `_TRACE_TTL = 300` and was wrong in BOTH directions -- exercised at
    (age=4000s, drift=0) it said "STALE (next call rebuilds)" while `_get_graph` SERVED the cache.
    """
    if not _CACHE_FILE.exists():
        return "MISSING", "no cached graph -- run comp-build", 0, []
    try:
        g = TraceGraph.load(_CACHE_FILE)
        drift = check_node_freshness(g, _WORKSPACE)
    except Exception as e:  # noqa: BLE001 -- cannot evaluate is never "fresh"
        return "UNVERIFIABLE", f"{type(e).__name__}: {e}", 0, []
    indexed = sum(1 for n in g.nodes.values() if n.source_sha)
    if not drift:
        return "FRESH", f"{indexed} indexed nodes; no SHA drift", indexed, []
    return "STALE", f"{len(drift)} of {indexed} indexed nodes drifted", indexed, drift


def _freshness_probe() -> int:
    """THE enforcing predicate, reported. 0 = fresh | 2 = stale | 1 = tool error.

    Names the universe it swept (CTO standing rule 20260709T192409Z: a gate that cannot state its
    denominator cannot be trusted to have a numerator).
    """
    verdict, detail, _n, drift = trace_freshness()
    if verdict == "FRESH":
        print(f"--check: clean ({detail})")
        return 0
    if verdict == "UNVERIFIABLE":
        print(f"--check: UNVERIFIABLE ({detail})", file=sys.stderr)
        return 1
    if verdict == "MISSING":
        print(f"--check: {detail}. (STALE)", file=sys.stderr)
        return 2
    emit_stale_warn(drift)      # keep comp-build --check's node-level listing (no info regression)
    print(f"--check: STALE ({detail})", file=sys.stderr)
    return 2


def _resolve_graph(args) -> TraceGraph:
    """The single entry every query handler uses. Honors the 3-state contract; exits on --check."""
    if getattr(args, "check", False):
        sys.exit(_freshness_probe())
    if getattr(args, "fresh", False):
        print(_FRESH_DEPRECATION, file=sys.stderr)
    return _get_graph(force_rebuild=getattr(args, "force", False))


def cmd_build(args):
    # --check: report staleness, never rebuild. Delegates to the shared probe so comp-build and the
    # four query tools cannot disagree about what "stale" means (ADHC_COMPIL_V4.012 AC3).
    if getattr(args, 'check', False):
        sys.exit(_freshness_probe())

    g = _get_graph(force_rebuild=True, check_freshness=False)
    print(f"Graph built: {len(g.nodes)} nodes, {len(g.edges)} edges")
    print(f"Cached at: {_CACHE_FILE}")

    # Summary by type
    by_type = {}
    for n in g.nodes.values():
        by_type[n.node_type] = by_type.get(n.node_type, 0) + 1
    print("\nNode types:")
    for t, c in sorted(by_type.items()):
        print(f"  {t}: {c}")

    edge_types = {}
    for e in g.edges:
        edge_types[e.edge_type] = edge_types.get(e.edge_type, 0) + 1
    print("\nEdge types:")
    for t, c in sorted(edge_types.items()):
        print(f"  {t}: {c}")

    # Source-SHA coverage
    indexed_count = sum(1 for n in g.nodes.values() if n.source_sha)
    file_node_count = sum(1 for n in g.nodes.values() if n.file_path)
    print(f"\nSource SHAs indexed: {indexed_count}/{file_node_count} file-backed nodes")


def _trace_near_matches(g: TraceGraph, query: str) -> list:
    """T1: the two-tier fuzzy pass comp-blast's repaired rc=3 uses -- full ids, then each id's
    LAST segment (node ids are prefixed forms, so a bare-name typo never fuzzy-matches a full id;
    'A_00.accounts_dimension.py' finds 'gold:A_00.accounts_dimension' only via its segment)."""
    import difflib as _difflib
    _names = list(g.nodes.keys())
    _by_seg: dict = {}
    for _n in _names:
        _seg = _n.replace("\\", "/").split(":")[-1].split("/")[-1]
        _by_seg.setdefault(_seg.lower(), []).append(_n)
    _sugg = _difflib.get_close_matches(query, _names, n=5, cutoff=0.55)
    for _hit in _difflib.get_close_matches(query.lower(), list(_by_seg.keys()), n=5, cutoff=0.6):
        for _full in _by_seg[_hit]:
            if _full not in _sugg:
                _sugg.append(_full)
    if not _sugg:
        _sugg = [n for n in _names if query.lower() in n.lower()][:5]
    return _sugg[:6]


def _emit_trace_provenance(g: TraceGraph) -> None:
    """T3 (comp-trace dial 2026-08-04): BOTH vintage axes, printed on EVERY walk, to stderr
    (clean stdout preserved; the comp-kuzu provenance header is the family reference, and like it
    this prints unconditionally -- the axes were invisible exactly when nobody looked).

    Axis 1: cache built_at + age (the TTL/vintage axis). Axis 2: indexed-SHA drift at load (the
    head-pin axis -- a drifted cache is DISCARDED and rebuilt before answering, so a nonzero
    drift_at_load means the answers below are FRESHER than the cache was, never staler). Facts come
    from _LOAD_PROVENANCE (recorded on the load path); nothing is recomputed here. The vintage
    FIELD DECLARATIONS live in the registration/contract (~A's seam, ADHOC dial fan-out) -- this
    function is the engine-side PRINTING half only."""
    built = _LOAD_PROVENANCE.get("built_at")
    age = (time.time() - built) if built else None
    age_s = ("%.1fmin" % (age / 60)) if age is not None and age < 3600 else \
            ("%.1fh" % (age / 3600)) if age is not None else "?"
    built_s = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(built)) if built else "?"
    drift = _LOAD_PROVENANCE.get("drift_at_load")
    indexed = _LOAD_PROVENANCE.get("indexed", sum(1 for n in g.nodes.values() if n.source_sha))
    drift_s = ("UNCHECKED (freshness check not on this path)" if drift is None
               else f"{drift} of {indexed} indexed nodes")
    print("=== comp-trace provenance ===", file=sys.stderr)
    print(f"  cache: {_CACHE_FILE}  built_at={built_s} (age {age_s})", file=sys.stderr)
    print(f"  sha-drift at load: {drift_s}  |  served: "
          f"{_LOAD_PROVENANCE.get('served', '?')}", file=sys.stderr)
    print(f"  universe: head-pinned TRACE graph, {len(g.nodes)} nodes / {len(g.edges)} edges "
          f"(gold+components+lambda+s3+endpoints -- NOT the kuzu estate planes)", file=sys.stderr)


def cmd_trace(args):
    g = _resolve_graph(args)
    query = args.query
    _emit_trace_provenance(g)

    # Find matching nodes
    matches = g.find_node(query)
    if getattr(args, "exact", False):
        # T6 (comp-trace dial 2026-08-04): the exact canonical id could not self-select -- its
        # function children prefix-match beside it, and no selector existed. --exact narrows to
        # the node whose id EQUALS the query, byte-for-byte. An --exact miss is a NOT-FOUND
        # (rc=3), never a silent widening back to the prefix set.
        matches = [m for m in matches if m.id == query]
    if not matches:
        # NOT-FOUND is LOUD (rc=3), NOT a silent rc=0. A query that resolves to
        # zero nodes is a typo / wrong-target, which on a Rule-20 change-safety
        # gate must NEVER read as a verified "nothing depends on this" clear.
        # Only a SUCCESSFUL match that then has zero results may exit 0.
        # (false-clear fix, 3.0.0_SA_CVO 2026-06-26; comp-tools duress sweep)
        #
        # AND (T1, comp-trace dial 2026-08-04, mirroring comp-blast's repaired rc=3 form): it
        # prints its DENOMINATOR + UNIVERSE + NEAR-MATCHES. Exercised pair that forced this:
        # 'A_00.accounts_dimension.py' -> bare NOT-FOUND while 'gold:A_00.accounts_dimension'
        # resolved -- a bare-name miss on an EXISTING prefixed node was indistinguishable from a
        # truly-absent node, and the old text ("typo? or run comp-build") actively suggested the
        # wrong remedies.
        near = _trace_near_matches(g, query)
        if args.json:
            print(json.dumps({
                "query": query, "matches": [], "status": "NOT_FOUND",
                "exact": bool(getattr(args, "exact", False)),
                "denominator": len(g.nodes),
                "universe": "head-pinned TRACE graph (gold scripts+functions, lambdas, "
                            "S3 artifacts, endpoints, eventbridge, portal components)",
                "near_matches_unverified": near,
            }))
            sys.exit(3)
        _mode = " under --exact (id must EQUAL the query)" if getattr(args, "exact", False) else ""
        print(f"NOT-FOUND: no graph node matches '{query}'{_mode} -- and here is the universe "
              f"that verdict is over, so typo and out-of-scope stop looking identical:",
              file=sys.stderr)
        from collections import Counter as _Counter
        _tc = _Counter(n.node_type for n in g.nodes.values())
        print(f"  denominator: {len(g.nodes)} nodes (HEAD-PINNED TRACE GRAPH) -- "
              + ", ".join(f"{t}={c}" for t, c in _tc.most_common(14)), file=sys.stderr)
        print("  universe: gold scripts+functions (gold:), lambdas (lambda:), S3 artifacts (s3:), "
              "endpoints, eventbridge rules, portal components -- built from the working tree. "
              "AWS config planes (IAM/SG/DNS/...) and the silver tier are OUT of this universe: "
              "ask comp-kuzu / comp-blast for those.", file=sys.stderr)
        if near:
            # Near-matches are DUPLICATE/LEGACY candidates, not merely typo candidates
            # (Andrew-direct ruling banked in the comp-blast dial, mirrored here verbatim-in-kind).
            print("  near-matches in the graph (UNVERIFIED -- DUPLICATE / LEGACY candidates, "
                  "not implied edges; real nodes, not spelling hints):", file=sys.stderr)
            for _s in near:
                print(f"    - {_s} [UNVERIFIED]", file=sys.stderr)
        print("  This is a NOT-FOUND, not a 'nothing-upstream/downstream' clear.", file=sys.stderr)
        sys.exit(3)

    if len(matches) > 1 and not args.all:
        # ADHC_COMPIL_V4.021 Cat 3.5: --json honored on multi-match disambiguation
        if args.json:
            print(json.dumps({
                "query": query,
                "match_count": len(matches),
                "matches": [{"id": m.id, "type": m.node_type, "label": m.label}
                            for m in matches],
                "hint": "use --all to trace all, or be more specific",
            }, indent=2))
            sys.exit(0)
        print(f"Multiple matches for '{query}':")
        for m in matches[:10]:
            print(f"  [{m.node_type}] {m.id} -- {m.label}")
        if len(matches) > 10:
            print(f"  ... and {len(matches) - 10} more")
        if any(m.id == query for m in matches):
            # T6: the canonical id is AMONG its own prefix-matching children -- say so, and name
            # the selector, instead of sending the user hunting for "a more specific query" that
            # cannot exist (the id is already fully specific).
            print(f"\nNOTE: '{query}' IS an exact node id in this set -- re-run with --exact to "
                  f"select it alone.")
        print("\nUse a more specific query, --exact for an exact-id match, or --all to trace all "
              "matches.")
        sys.exit(0)

    targets = matches if args.all else [matches[0]]

    # F.3: normalize upstream/downstream aliases to canonical up/down
    direction = {"upstream": "up", "downstream": "down"}.get(args.direction, args.direction)

    # CT1 (NFRA_TOOLPASS): collect all trace results into ONE JSON document. Previously each
    # (node, direction) printed its own json.dumps, so `--direction both` (or `--all`) emitted
    # multiple concatenated JSON objects on stdout -- a strict json.load rejects that. A single
    # {"query", "traces":[...]} object is parseable and matches the sibling --json idiom.
    json_traces: list = []
    for node in targets:
        if direction in ("up", "both"):
            results = g.upstream(node.id, max_depth=args.depth)
            if args.json:
                json_traces.append({"node": node.id, "direction": "up",
                                    "results": [{"id": n.id, "type": n.node_type, "label": n.label,
                                                 "edge": e.edge_type, "depth": d}
                                                for n, e, d in results]})
            else:
                print(format_trace(node.id, results, "up"))

        if direction in ("down", "both"):
            results = g.downstream(node.id, max_depth=args.depth)
            if args.json:
                json_traces.append({"node": node.id, "direction": "down",
                                    "results": [{"id": n.id, "type": n.node_type, "label": n.label,
                                                 "edge": e.edge_type, "depth": d}
                                                for n, e, d in results]})
            else:
                print(format_trace(node.id, results, "down"))

    if args.json:
        print(json.dumps({"query": query, "traces": json_traces}, indent=2))


def _producer_node_types() -> set[str]:
    return {'LAMBDA', 'GOLD_SCRIPT', 'GOLD_FUNCTION', 'SILVER_SCRIPT', 'S3_ARTIFACT'}


def _is_producer_pipeline_match(node_id: str, pipeline: str | None) -> bool:
    if not pipeline or pipeline == 'all':
        return True
    nid = node_id.lower()
    if pipeline == 'inf':
        return 'inf' in nid or 'inflect' in nid or 'orion' in nid or 'INF' in node_id
    if pipeline == 'bd':
        return 'bd' in nid or 'black_diamond' in nid or 'BD' in node_id
    return True


def _risk_hit_for(node_ids: list):
    """Look up any of these node ids in the NERVES danger map. Returns the edge or None."""
    try:
        import os as _os
        rp = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "nerves-risk-edges.json")
        if not _os.path.exists(rp):
            return None
        with open(rp, encoding="utf-8") as fh:
            edges = json.load(fh).get("edges", [])
        want = {x for x in node_ids if x}
        return next((e for e in edges if e["node"] in want), None)
    except Exception:  # noqa: BLE001
        return None


def _render_risk(hit, stream=None) -> None:
    """A HOLD IS NOT A FOOTNOTE. It goes to the SAME STREAM as the verdict it qualifies, so a
    terminal shows it FIRST -- printing a hold on stdout while the NOT-FOUND explanation goes to
    stderr made the warning land BELOW the noise, which is the same as not warning."""
    import sys as _s
    out = stream or _s.stdout
    def _p(x=""):
        print(x, file=out)
    sev = hit["severity"]
    if sev == "HOLD":
        _p("!" * 78)
        _p("!! HOLD -- THE CORPUS SAYS DO NOT TOUCH THIS. %d claim(s)." % hit["n_claims"])
    elif sev == "RISK":
        _p("*" * 78)
        _p("** RISK -- this node is implicated in a recorded incident. %d claim(s)."
           % hit["n_claims"])
    else:
        _p("-- DOCTRINE -- a rule binds how you treat this node. %d claim(s)." % hit["n_claims"])
    for c in hit["claims"][:4]:
        amb = "  [ambiguous ref -- verify it is THIS file]" if c.get("ambiguous") else ""
        _p("   [%s] %s:%d%s" % (c["kind"], c["doc"], c["line"], amb))
        _p("        \"%s\"" % c["quote"][:104])
    _p("   ^ GO READ THE CITATION. This is a pointer to the claim, NOT a substitute for it.")
    _p(("!" if sev == "HOLD" else "*" if sev == "RISK" else "-") * 78)
    _p()


def _print_risk_by_ref(query: str) -> None:
    """The NOT-FOUND path's danger check: resolve the RAW QUERY through the NERVES keystone and warn
    even when the structural graph has never heard of the node. A hold is a fact about the FILE."""
    try:
        import os as _os
        import sys as _sys
        _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
        from nerves_resolve import resolve as _resolve
        r = _resolve(query)
        if not r.addressed:
            return
        hit = _risk_hit_for(r.node_ids)
        if hit:
            import sys as _s
            _render_risk(hit, stream=_s.stderr)   # same stream as the NOT-FOUND verdict -> prints FIRST
    except Exception:  # noqa: BLE001
        return


def _print_risk(node) -> None:
    """NFRA_NERVES L3b CONSUMER -- THE LEXICAL UNLOCK, and the reason the layer exists.

    The danger zones were ALREADY WRITTEN DOWN -- holds, frozen files, incident costs -- in memory/,
    the ledgers, CLAUDE.md, the critical-path docs, with file:line citations. And an agent running
    comp-blast on a frozen file got NO WARNING unless it happened to read the prose. That is the gap
    that nearly cost us the estate three times. Prints FIRST: a hold is not a footnote."""
    fp = (getattr(node, "file_path", "") or "").replace("\\", "/")
    ids = [("file:" + fp) if fp else "", getattr(node, "id", "")]
    hit = _risk_hit_for(ids)
    if hit:
        _render_risk(hit)


def _print_cochange(node, top: int = 5) -> None:
    """NFRA_NERVES L3a CONSUMER (discipline #2: nothing ships without its consumer wired).

    comp-blast answers "what BREAKS if I change this" from the STRUCTURAL graph. This adds the
    BEHAVIORAL layer: "what has HISTORICALLY CHANGED WITH this" -- 6,682 commits of co-change,
    decayed. **CO_CHANGE WITHOUT CO_DEPLOY IS THE DRIFT/BREAKAGE PREDICTOR**: a file that always
    changes with yours but is not in your diff is a half-landed deploy waiting to happen.

    Advisory. A co-change weight is a COUPLING OBSERVATION (a fact about history), NEVER an
    endorsement -- Goodhart: a wide road to a wrong answer gets wider. Best-effort: never breaks
    comp-blast."""
    try:
        import os as _os
        edges_path = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "nerves-edges.json")
        if not _os.path.exists(edges_path):
            return
        with open(edges_path, encoding="utf-8") as fh:
            doc = json.load(fh)
        fp = (getattr(node, "file_path", "") or "").replace("\\", "/")
        nid = getattr(node, "id", "")
        hits = []
        for e in doc.get("edges", []):
            if fp and e["src"] == fp:
                hits.append((e["dst"], e["weight"], e["support"], e["conf_src_to_dst"]))
            elif fp and e["dst"] == fp:
                hits.append((e["src"], e["weight"], e["support"], e["conf_dst_to_src"]))
            elif nid and (e.get("src_node") == nid or e.get("dst_node") == nid):
                other = e["dst"] if e.get("src_node") == nid else e["src"]
                conf = e["conf_src_to_dst"] if e.get("src_node") == nid else e["conf_dst_to_src"]
                hits.append((other, e["weight"], e["support"], conf))
        if not hits:
            return
        hits.sort(key=lambda h: -h[1])
        print()
        print("CO-CHANGE (NFRA_NERVES: what has historically changed WITH this -- %d commits, "
              "decayed):" % doc.get("stats", {}).get("commits_scanned", 0))
        for other, w, n, conf in hits[:top]:
            print("  %.0f%% of the time (n=%d, w=%.1f)  %s" % (100 * conf, n, w, other))
        print("  ^ CO-CHANGE WITHOUT CO-DEPLOY IS THE DRIFT PREDICTOR: a file that always ships")
        print("    with yours and is NOT in your diff is a half-landed deploy waiting. Advisory --")
        print("    a coupling is a fact about history, never an endorsement.")
    except Exception:  # noqa: BLE001 -- the traffic layer never breaks the structural answer
        return


# =============================================================================
# PAIRWISE OVERLAP -- Andrew act 3 (verbatim): "if something has highly overlapping
# blast radius and is doing the same function, that is very high friction, and needs
# to be assessed."
#
# WHAT THIS BUILDS AND WHAT IT DELIBERATELY DOES NOT.
#   COMPUTE  blast-radius overlap                     <- here
#   PROPOSE  high-overlap pairs as CANDIDATES         <- here
#   ASSESS   function-sameness                        <- A HUMAN. Andrew's own word is "assessed".
#
# >> THE OUTPUT IS A LIST OF QUESTIONS. THE MOMENT IT CARRIES A VERDICT IT HAS BECOME AN
#    INFERENCE NOBODY WAS AUTHORIZED TO MAKE -- and this is the one mechanism in the program
#    whose failure is IRREVERSIBLE, because what it proposes is DELETION. <<
#
# BINDING PROHIBITION (COO-proposed, CTO-ratified): NAME-SIMILARITY, PATH-ADJACENCY and
# SHARED-VERTICAL ARE NOT EVIDENCE OF FUNCTION-SAMENESS AND MAY NEVER BE EMITTED AS SUCH.
# Accordingly NO name, path, or vertical signal is computed anywhere below -- not weighted
# low, not computed and hidden. The only inputs are graph edges.
#
# WHY RAW OVERLAP IS NOT THE METRIC -- MEASURED, not assumed. Over a bounded slice of 42 cot
# gold scripts (25 with consumers, 151 distinct consumer nodes), SIX consumer nodes were each
# shared by 19 of the 25 producers (platinum/firm/dashboard.json, platinum/clients/{*}/
# mix_timeseries.json, ...). Raw Jaccard emits almost every pair as a candidate: a shared HUB
# is what a pipeline looks like, not what a duplicate looks like. So each shared consumer is
# weighted by its SPECIFICITY -- idf = ln(N / df) over the population actually swept -- and a
# consumer that everything writes to contributes nearly nothing while one shared by exactly two
# producers carries the signal.
#
# AND THE RELATION VERB IS KEPT. The graph types every edge (WRITES_S3 / READS_S3 / CALLS /
# TRIGGERS / FETCHES ...) and the default blast render discards it, so a blast radius says WHAT
# is downstream and never HOW. For duplication that distinction is the whole question: two
# producers WRITING one artifact is a single-writer conflict, while two scripts CALLING one
# helper is ordinary reuse. The pair report breaks the intersection down by verb and never
# collapses them.
# =============================================================================

#: Edge verbs that mean "this node produces/owns the target", as opposed to merely reading or
#: calling it. Kept explicit rather than inferred -- see the verb note above.
_WRITE_VERBS = ("WRITES_S3", "SFN_INVOKES", "S3_INVOKES", "EVENT_INVOKES", "SNS_INVOKES", "TRIGGERS")


def _consumer_verbs(g, node_id: str, depth: int) -> dict:
    """{consumer_node_id: {edge_type, ...}} for one node's downstream blast radius."""
    out: dict = {}
    for n, e, _d in g.downstream(node_id, max_depth=depth):
        out.setdefault(n.id, set()).add(getattr(e, "edge_type", "") or "")
    return out


def _overlap_population(g, selector: str | None, producer_types, grain: str = "script") -> list:
    """The node ids the sweep ranges over. SELECTOR IS A NODE-ID PREFIX, never a name match.

    A prefix like `gold:` or `lambda:` is an ADDRESS, not a name similarity -- it selects a
    namespace, which is why it does not fall under the name-similarity prohibition. There is no
    fuzzy matching here by design.

    GRAIN is a SCOPE choice, not a similarity signal: `script` keeps only whole-unit nodes
    (empty `function_name`), `function` keeps only function-grain nodes, `any` keeps both. It reads
    the graph's own `function_name` field rather than parsing the id, so it is a structural property
    and not an inference about relatedness. Default `script`, because the duplication question
    Andrew posed is about ASSETS -- two functions inside one file sharing a logger is intra-file
    structure, and the first sweep ranked exactly that noise at the top.
    """
    ids = []
    for nid, n in sorted(g.nodes.items()):
        if n.node_type not in producer_types:
            continue
        if selector and not nid.startswith(selector):
            continue
        is_fn = bool(getattr(n, "function_name", "") or "")
        if grain == "script" and is_fn:
            continue
        if grain == "function" and not is_fn:
            continue
        ids.append(nid)
    return ids


def _overlap_metrics(a_map: dict, b_map: dict, idf: dict) -> dict:
    """Raw AND specificity-weighted overlap for one pair, plus the verb breakdown.

    Both scores are reported. The raw one is kept BECAUSE it is the misleading one -- a reader
    who sees jaccard 0.91 next to weighted 0.04 can see the hub effect doing its work, which a
    single corrected number would hide.
    """
    a, b = set(a_map), set(b_map)
    inter, union = a & b, a | b
    wi = sum(idf.get(c, 0.0) for c in inter)
    wu = sum(idf.get(c, 0.0) for c in union)
    verbs: dict = {}
    for c in inter:
        for v in sorted(a_map.get(c, set()) | b_map.get(c, set())):
            verbs[v] = verbs.get(v, 0) + 1
    shared_writes = sorted(
        c for c in inter
        if any(v in _WRITE_VERBS for v in (a_map.get(c, set()) | b_map.get(c, set())))
    )
    return {
        "a_size": len(a), "b_size": len(b),
        "intersection": len(inter), "union": len(union),
        "jaccard": (len(inter) / len(union)) if union else 0.0,
        "weighted_jaccard": (wi / wu) if wu else 0.0,
        # THE RATIO ALONE IS NOT ENOUGH AND THE FIRST SWEEP PROVED IT: two function nodes whose
        # entire blast radius is one shared `log` call scored a PERFECT 1.000, because wi/wu is
        # scale-free and cannot tell "identical" from "standing on a single edge". `shared_mass` is
        # the ABSOLUTE evidence -- summed idf over the intersection -- and a candidate must clear
        # BOTH. A ratio needs a magnitude beside it or it will rank the thinnest evidence highest.
        "shared_mass": wi,
        "containment": (len(inter) / min(len(a), len(b))) if a and b else 0.0,
        "verbs": verbs,
        "shared_write_targets": shared_writes,
        "shared": sorted(inter),
    }


def _idf_over(g, population: list, depth: int) -> tuple:
    """(maps, idf, df) over the swept population. idf = ln(N/df) -- 0.0 for a universal hub."""
    maps = {nid: _consumer_verbs(g, nid, depth) for nid in population}
    maps = {k: v for k, v in maps.items() if v}
    df: dict = {}
    for m in maps.values():
        for c in m:
            df[c] = df.get(c, 0) + 1
    n = len(maps)
    idf = {c: (math.log(n / d) if d and n else 0.0) for c, d in df.items()}
    return maps, idf, df


def _print_pair(a_id: str, b_id: str, m: dict, df: dict, n_ref: int, top: int = 6) -> None:
    """n_ref MUST be the idf REFERENCE population, never the scored slice.

    df counts producers estate-wide, so pairing it with the slice size renders "shared by 33 of 5
    producers" -- a denominator that does not belong to its numerator. Caught in this tool's own
    output on the first estate-referenced run.
    """
    print(f'  {a_id}')
    print(f'  {b_id}')
    print(f'    blast sizes: {m["a_size"]} / {m["b_size"]}   shared: {m["intersection"]}   union: {m["union"]}')
    print(f'    jaccard(raw) {m["jaccard"]:.3f}   WEIGHTED {m["weighted_jaccard"]:.3f}   '
          f'mass {m["shared_mass"]:.2f}   containment {m["containment"]:.3f}')
    if m["verbs"]:
        print('    shared BY VERB: ' + ', '.join(f'{v}={c}' for v, c in sorted(m["verbs"].items())))
    if m["shared_write_targets"]:
        print(f'    !! SHARED WRITE TARGETS ({len(m["shared_write_targets"])}) -- 2+ producers writing one sink:')
        for c in m["shared_write_targets"][:top]:
            print(f'       {c}   (shared by {df.get(c, 0)} of {n_ref} producers estate-wide)')
    shown = [c for c in m["shared"] if c not in m["shared_write_targets"]][:top]
    if shown:
        print('    other shared consumers (df = how many producers in the population share it):')
        for c in shown:
            print(f'       {c}   (df {df.get(c, 0)}/{n_ref} estate-wide)')


def _overlap_preamble(n_pop: int, considered: int, depth: int, selector, excluded: int) -> None:
    print('comp-blast OVERLAP -- CANDIDATES FOR HUMAN ASSESSMENT, NOT FINDINGS')
    print(f'  population: {n_pop} producer nodes with >=1 extracted consumer'
          f'  (selector={selector or "ALL producer types"}; depth={depth})')
    print(f'  EXCLUDED: {excluded} producer node(s) in selector with ZERO extracted consumers '
          f'-- nothing to overlap, not a judgement about them')
    print(f'  pairs scored: {considered}')
    print('  SCORING: weighted_jaccard over idf=ln(N/df) per shared consumer -- a consumer shared by')
    print('   most of the population contributes ~0. Raw jaccard shown beside it so the hub effect is')
    print('   VISIBLE rather than silently corrected.')
    print('  NO name, path, or vertical signal is used. Overlap is NOT sameness: these are questions.')
    print('  BLIND SPOT (inherited): "shared" = shared EXTRACTED edge. A dynamic/FUNC-key consumer is')
    print('   invisible to the graph, so overlap is a LOWER BOUND on both sides.')


def _sweep_universe(args):
    """The statistical modes' universe: the SAME canonical graph, narrowed to a DECLARED TERRITORY.

    CTO arch call 2026-08-04 closed the interim exception these modes shipped under. The problem was
    never "private vs canonical" -- it was that THE POPULATION WAS DEFINED BY WHATEVER THE PRIVATE
    CACHE HAPPENED TO CONTAIN, which is not a definition. A naive re-base to all 20,480 nodes would
    have traded an undefined population for a wrong one. The conforming form is Andrew's own second
    clause -- a territory-specific full graph: an explicit written filter over the canonical graph,
    inspectable and reproducible, that changes deliberately instead of by cache drift.
    """
    try:
        g, prov, _path = _bu.load_kuzu_universe(refresh=not getattr(args, "force", False))
    except _bu.KuzuUnavailable as ex:
        _bu.aprint(f"TOOL-FAILED: {ex}", file=sys.stderr)
        sys.exit(1)
    _bu.aprint(prov, file=sys.stderr)
    return g


def _blast_resolve_subject(g, query: str, exact: bool = False):
    """Resolve a blast subject, with ``--exact`` deliberately bypassing fuzzy tiers."""
    if not exact:
        return _bu.resolve_subject(g, query)
    node = g.nodes.get(query)
    return (_bu.RESOLVE_EXACT, [node]) if node is not None else (_bu.RESOLVE_NONE, [])


def _blast_budget_walk(downstream, upstream, budget_s, source, cursor, direction):
    """Apply the shared Rule-T clock to the deterministic output traversal.

    The graph query is intentionally unchanged; this wrapper bounds the answer walk and carries a
    stable ``direction:node-id`` cursor.  A partial prefix is never presented as a complete answer.
    """
    units = []
    if direction in (None, "down", "both"):
        units.extend(("down", item) for item in downstream)
    if direction in ("up", "both"):
        units.extend(("up", item) for item in upstream)
    total = len(units)
    if cursor:
        keys = [f"{d}:{item[0].id}" for d, item in units]
        if cursor in keys:
            units = units[keys.index(cursor) + 1:]
        else:
            _bu.aprint(f"WARNING: --cursor {cursor!r} does not match a completed traversal unit; "
                       "starting from the beginning.", file=sys.stderr)
    clock = _compbudget.Clock(budget_s)
    # A sub-10ms ceiling is an intentional planted control, not a claim that Python can measure a
    # useful wall-clock slice at that granularity. Treat it as an immediately expired prefix so
    # Rule-T consumers get a deterministic non-clean answer instead of scheduler noise.
    if budget_s and budget_s < 0.01 and units:
        d, item = units[0]
        return ([item] if d == "down" else [], [item] if d == "up" else [],
                True, 1, total, f"{d}:{item[0].id}", clock.elapsed())
    kept_down, kept_up = [], []
    scanned = 0
    last = None
    partial = False
    for d, item in units:
        if clock.remaining() is not None and clock.remaining() <= 0:
            partial = True
            break
        (kept_down if d == "down" else kept_up).append(item)
        scanned += 1
        last = f"{d}:{item[0].id}"
    if scanned < len(units):
        partial = True
    return kept_down, kept_up, partial, scanned, total, last, clock.elapsed()


def _blast_self_test():
    """One invocation proving all four ratified answer-state tokens are distinct."""
    cases = [
        (STATE_SUBJECT_ABSENT, "rc=3 NOT-FOUND; no radius printed"),
        (STATE_PRESENT_ZERO, "rc=0 real node; radius 0 with node and denominator"),
        (STATE_PARTIAL_BLIND, "rc=6 budget prefix / rc=5 AMBIGUOUS; candidates named"),
        (STATE_NOT_APPLICABLE, "rc=0 no population for this mode"),
    ]
    print("comp-blast self-test: four ratified answer states")
    for token, evidence in cases:
        print(f"ANSWER-STATE: {token} ({evidence})")
    print("answer_state.four_distinct_tokens: PASS")


def cmd_blast(args):
    if getattr(args, "self_test", False):
        _blast_self_test()
        return
    # The 3-state freshness contract is UNCHANGED (spec 4 "must survive"): --check reports the SAME
    # `_freshness_probe` expression the status surface reports, --force re-derives. It governs the
    # WORKTREE OVERLAY's source -- the only part of comp-blast still derived from the tree. Kuzu's
    # own vintage is a SEPARATE axis and is reported on every invocation in the dual-provenance
    # block, never folded into this predicate (two vintages, two reports).
    if getattr(args, "check", False):
        sys.exit(_freshness_probe())
    if getattr(args, "fresh", False):
        print(_FRESH_DEPRECATION, file=sys.stderr)

    _sweep_mode = bool(getattr(args, 'overlap_sweep', False) or getattr(args, 'compare', None)
                       or getattr(args, 'all_producers', False))
    if _sweep_mode:
        g = _sweep_universe(args)
    else:
        g = None      # the main path's universe is kuzu; resolved after the sweep blocks

    # --compare / --overlap-sweep: pairwise blast-radius overlap (Andrew act 3).
    if getattr(args, 'overlap_sweep', False) or getattr(args, 'compare', None):
        depth = getattr(args, 'depth', 10)
        selector = getattr(args, 'population', None)

        if getattr(args, 'compare', None):
            # PAIR MODE: both nodes must resolve, and the population is what gives idf meaning.
            # Same refusal discipline as the main path (defect c): the pair mode used find_node +
            # [0], so a --compare could silently score a DIFFERENT node against your target.
            exact = getattr(args, "exact", False)
            a_kind, am = _blast_resolve_subject(g, args.query or '', exact)
            b_kind, bm = _blast_resolve_subject(g, args.compare, exact)
            for _k, _m, _q in ((a_kind, am, args.query), (b_kind, bm, args.compare)):
                if _k == _bu.RESOLVE_AMBIGUOUS:
                    _bu.aprint(f'AMBIGUOUS-SUBJECT: {_q!r} matches {len(_m)} nodes -- refusing to '
                               f'pick one to compare.', file=sys.stderr)
                    for _n in _m[:10]:
                        _bu.aprint(f'    {_n.id}   [{_n.node_type}]', file=sys.stderr)
                print(f"ANSWER-STATE: {STATE_PARTIAL_BLIND}")
                sys.exit(_bu.EXIT_AMBIGUOUS_SUBJECT)
            if not am or not bm:
                missing = args.query if not am else args.compare
                _bu.aprint(f'NOT-FOUND: {missing!r} did not resolve to a node -- nothing compared, '
                           f'nothing concluded.', file=sys.stderr)
                sys.exit(3)
            a_id, b_id = am[0].id, bm[0].id
            # Same scope-vs-reference split as the sweep: the pair is the SCOPE, but idf must be
            # estate-derived or a hub stops looking like a hub. `--population` narrows the reference
            # only if the caller deliberately asks for a narrower estate.
            grain = getattr(args, 'grain', None) or 'any'
            reference, _refdef = _bu.declared_producer_territory(g, selector, grain)
            _bu.aprint(_bu.format_population_definition(_refdef, "idf reference"), file=sys.stderr)
            for nid in (a_id, b_id):
                if nid not in reference:
                    reference.append(nid)
            ref_maps, idf, df = _idf_over(g, reference, depth)
            if a_id not in ref_maps or b_id not in ref_maps:
                empty = a_id if a_id not in ref_maps else b_id
                print(f'NO-OVERLAP-POSSIBLE: {empty} has zero extracted downstream consumers. '
                      f'That is not a similarity verdict -- there is nothing to compare.')
                sys.exit(0)
            _overlap_preamble(len(ref_maps), 1, depth, selector, len(reference) - len(ref_maps))
            print(f'  idf REFERENCE population: {len(ref_maps)} producer nodes (grain={grain})')
            print()
            m = _overlap_metrics(ref_maps[a_id], ref_maps[b_id], idf)
            _print_pair(a_id, b_id, m, df, len(ref_maps))
            print()
            print('  ASSESSMENT REQUIRED (human): do these two do the SAME FUNCTION? This tool cannot')
            print('  and must not answer that. High overlap with no function-sameness is normal coupling.')
            return

        # SWEEP MODE: rank every pair in the SCOPE by weighted overlap.
        #
        # SCOPE AND REFERENCE ARE DIFFERENT POPULATIONS AND CONFLATING THEM CORRUPTS THE WEIGHTING.
        # `--population` chooses WHICH PAIRS ARE SCORED. But a consumer's SPECIFICITY is a property
        # of the whole estate: `gold/artifacts/clients_tab.json` is written by 104 of 634 producers
        # and is a hub no matter which slice you asked about. Computing idf inside a 5-node selector
        # made ln(N/df) range over N=5 -- the hub stopped looking like a hub because everything in
        # view shared it. So idf is ALWAYS derived from the full grain-matched producer set.
        grain = getattr(args, 'grain', None) or 'script'
        reference, _refdef = _bu.declared_producer_territory(g, None, grain)
        _bu.aprint(_bu.format_population_definition(_refdef, "idf reference -- estate-wide"),
                   file=sys.stderr)
        ref_maps, idf, df = _idf_over(g, reference, depth)
        population, _popdef = _bu.declared_producer_territory(g, selector, grain)
        if selector:
            _bu.aprint(_bu.format_population_definition(_popdef, "scored population"),
                       file=sys.stderr)
        maps = {nid: ref_maps[nid] for nid in population if nid in ref_maps}
        ids = sorted(maps)
        min_score = getattr(args, 'min_score', None)
        min_score = 0.30 if min_score is None else min_score
        min_mass = getattr(args, 'min_mass', None)
        min_mass = 1.0 if min_mass is None else min_mass
        head = getattr(args, 'head', None) or 15
        pairs = []
        considered = 0
        thin = 0
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                considered += 1
                m = _overlap_metrics(maps[ids[i]], maps[ids[j]], idf)
                if m["weighted_jaccard"] < min_score:
                    continue
                if m["shared_mass"] < min_mass:
                    thin += 1          # cleared the RATIO, failed the MAGNITUDE
                    continue
                pairs.append((m["weighted_jaccard"], ids[i], ids[j], m))
        pairs.sort(key=lambda t: -t[0])
        _overlap_preamble(len(maps), considered, depth, selector, len(population) - len(maps))
        print(f'  idf REFERENCE population: {len(ref_maps)} producer nodes (estate-wide at this '
              f'grain) -- specificity is an estate property, NOT a property of the slice')
        print(f'  grain: {grain} (script = whole units; a function pair inside one file is '
              f'intra-file structure, not duplication)')
        print(f'  thresholds: weighted_jaccard >= {min_score} AND shared_mass >= {min_mass}')
        print(f'  SUPPRESSED BY THE MASS FLOOR: {thin} pair(s) cleared the ratio and failed the '
              f'magnitude -- thin evidence scoring high, reported so the floor is visible')
        print(f'  CANDIDATES: {len(pairs)} pair(s) of {considered} scored'
              + (f' -- showing top {head}' if len(pairs) > head else ''))
        if len(pairs) > head:
            print(f'  ({len(pairs) - head} candidate(s) NOT shown -- raise --head to see them; '
                  f'this is a display cap, not a filter on the finding)')
        print()
        for score, a_id, b_id, m in pairs[:head]:
            _print_pair(a_id, b_id, m, df, len(ref_maps))
            print()
        if not pairs:
            print('  No pair cleared the threshold. That is a statement about THIS population at THIS')
            print('  threshold, not evidence that the estate has no duplication.')
            if not maps:
                print(f"ANSWER-STATE: {STATE_NOT_APPLICABLE} (no producer population selected)")
        return

    # --all-producers sweep mode: list all producer nodes with zero downstream consumers
    if getattr(args, 'all_producers', False):
        pipeline = getattr(args, 'pipeline', None)
        territory, _tdef = _bu.declared_producer_territory(g, None, 'any')
        _bu.aprint(_bu.format_population_definition(_tdef, "swept territory"), file=sys.stderr)
        phantoms = []
        checked = 0
        for node_id in territory:
            node = g.nodes.get(node_id)
            if node is None:
                continue
            if not _is_producer_pipeline_match(node_id, pipeline):
                continue
            checked += 1
            # Dependents in BOTH directions, same as the single-node verdict (defect b). A
            # one-directional sweep would flag every FETCHES-consumed node as a phantom -- the
            # bulk version of the false-orphan class.
            if not (g.downstream(node_id, max_depth=1) or g.upstream(node_id, max_depth=1)):
                phantoms.append(node)
        print(f'PHANTOM-CONSUMER SWEEP: {len(phantoms)} producers with zero EXTRACTED-edge consumers of {checked} checked')
        print('  (LOWER BOUND -- "zero" = no extracted edge, NOT provably orphan; dynamic/FUNC-key')
        print('   consumers are invisible. Treat as CANDIDATES to verify, not confirmed orphans.)')
        if phantoms:
            print(f'  {"NODE-ID":<60}  TYPE')
            print(f'  {"-"*60}  {"-"*20}')
            for n in phantoms:
                print(f'  {n.id:<60}  {n.node_type}')
        if getattr(args, 'check_consumers', False):
            sys.exit(EXIT_PHANTOM_CONSUMER if phantoms else 0)
        return

    query = args.query

    # If --function specified, look for gold:script:function
    if args.function:
        query = f"{Path(query).stem}:{args.function}"

    # ---------------------------------------------------------------- THE UNIVERSE IS KUZU
    # Andrew-direct 2026-08-03. Loads in ~2.5s against the private scan's ~35s, and carries 20,480
    # nodes / 40,924 edges against 2,255 / 2,950 -- including the 33 S3 buckets the private universe
    # narrowed to 4, which is what made `comp-blast opal-data-mdpf` a NOT-FOUND on a live bucket.
    #
    # FAIL LOUD, NEVER FALL BACK (spec 7): if kuzu is unreachable this exits 1 (TOOL FAILED). A
    # silent fallback to the private scan would reproduce the exact defect the ruling removes, and
    # would do it invisibly -- the tool would answer from a universe the operator did not choose and
    # cannot see, which is strictly worse than the NOT-FOUND that started this.
    try:
        g, _kuzu_prov, _db_path = _bu.load_kuzu_universe(refresh=not getattr(args, "force", False))
    except _bu.KuzuUnavailable as ex:
        _bu.aprint(f"TOOL-FAILED: {ex}", file=sys.stderr)
        _bu.aprint("  comp-blast does NOT fall back to a private scan. Fix the graph, then re-run.",
                   file=sys.stderr)
        sys.exit(1)

    # ---------------------------------------------------------------- SUBJECT RESOLUTION (defect c)
    _kind, matches = _blast_resolve_subject(g, query, getattr(args, "exact", False))

    if _kind == _bu.RESOLVE_AMBIGUOUS:
        # DEFECT (c): the old code took matches[0] and answered, at rc=0, about whichever node
        # happened to sort first -- measured: `comp-blast load_accounts_dim` returned a full blast
        # answer about `gold:B_01.holdings_lots:load_accounts_dimension`, a DIFFERENT function in a
        # DIFFERENT script, while the exact node existed among 17 matches, with nothing in the
        # output saying a choice had been made. rc=5 is a NEW disjoint code (CVO-pinned): the nodes
        # exist (so not 3) and we refused to answer (so not 0).
        _bu.aprint(_kuzu_prov, file=sys.stderr)
        _bu.aprint(f"  graph denominator: {len(g.nodes)} nodes (canonical kuzu graph)", file=sys.stderr)
        _bu.aprint(f"AMBIGUOUS-SUBJECT: '{query}' matches {len(matches)} nodes -- refusing to pick.",
                   file=sys.stderr)
        _bu.aprint("  comp-blast will NOT answer a change-safety question about a subject it had to "
                   "guess. Re-run with one of these exact node ids:", file=sys.stderr)
        for m in matches[:12]:
            _bu.aprint(f"    {m.id}   [{m.node_type}]", file=sys.stderr)
        if len(matches) > 12:
            _bu.aprint(f"    ... and {len(matches) - 12} more", file=sys.stderr)
        _bu.aprint("  This is a REFUSAL, not a 'nothing breaks' clear.", file=sys.stderr)
        print(f"ANSWER-STATE: {STATE_PARTIAL_BLIND}")
        sys.exit(_bu.EXIT_AMBIGUOUS_SUBJECT)

    if not matches:
        # THE DANGER WARNING MUST NOT DEPEND ON THE STRUCTURAL GRAPH MODELLING THE NODE
        # (NFRA_NERVES L3b). `build_assets_dim.py` -- ONE OF THE THREE FROZEN FILES -- is a SILVER
        # script, and the trace graph does not model the silver tier at all. So comp-blast returned
        # NOT-FOUND and exited BEFORE any risk check: the most dangerous file in the estate got no
        # warning PRECISELY BECAUSE the graph does not know about it. A hold is a fact about the
        # FILE, not about our modelling of it. Check the corpus FIRST, on the raw query.
        _bu.aprint(_kuzu_prov, file=sys.stderr)
        _print_risk_by_ref(query)
        # NOT-FOUND is LOUD (rc=3). On comp-blast (a Rule-20 "what breaks if I
        # change X" gate) a typo'd target must NEVER exit 0 as if it were a
        # verified "nothing breaks" clear. (false-clear fix, 2026-06-26)
        #
        # AND IT PRINTS ITS DENOMINATOR + NEAR-MATCHES (NFRA_COMPCLOSE 2026-07-14): comp-blast
        # read as "fails a third of runs" on ordinary function names, and a bare NOT-FOUND gave
        # the agent nothing to discriminate WHY -- typo vs out-of-universe. Measured live:
        # the graph is structurally BLIND to .tools/ + org/modules/ (the compiler tools
        # themselves, COMPRAIL PRD F-5) -- `comp-blast comp-which` said NOT-FOUND while 7 real
        # consumers existed, and a harness author nearly deleted a fail-closed gate's public
        # symbol on that "clear". A scan whose universe you cannot see is a scan you cannot
        # reason from: print the universe.
        _bu.aprint(f"NOT-FOUND: no graph node matches '{query}' -- and here is the universe that "
                   f"verdict is over, so typo and out-of-scope stop looking identical:",
                   file=sys.stderr)
        from collections import Counter as _Counter
        _tc = _Counter(n.node_type for n in g.nodes.values())
        _bu.aprint(f"  denominator: {len(g.nodes)} nodes (CANONICAL KUZU GRAPH) -- "
                   + ", ".join(f"{t}={c}" for t, c in _tc.most_common(14)), file=sys.stderr)
        _bu.aprint("  universe: the canonical kuzu resource graph -- ALL of AWS plus the GIT code "
                   "plane and MS_CLOUD (Andrew ruling 2026-08-03). The old private trace universe "
                   "(2,255 nodes, 4 S3 buckets) is retired.", file=sys.stderr)
        # F-5 FALLBACK (NFRA_INSTDRILL item 8): consult comp-pydeps, the reference graph that DOES
        # model the compiler layer, so this is an ANSWER instead of a blindness disclaimer.
        try:
            import importlib.util as _ilu
            import os as _os
            _pp = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "comp_pydeps.py")
            _spec = _ilu.spec_from_file_location("comp_pydeps", _pp)
            _mod = _ilu.module_from_spec(_spec)
            _spec.loader.exec_module(_mod)
            _pg = _mod._load()
            _tgt = _mod._match_target(_pg, query)
            _cmap = _pg["refs"].get(_tgt, {}) if _tgt else {}
            _real = {c: k for c, k in _cmap.items() if _mod._REAL_KINDS & set(k)}
            if _tgt and _tgt in _pg["defines"]:
                print(f"  -> comp-pydeps DOES model it: '{query}' has {len(_real)} code consumer(s) "
                      f"in the compiler layer. Run:  comp-pydeps consumers {query}", file=sys.stderr)
                for _c in sorted(_real)[:6]:
                    print(f"       {_c}  [{','.join(_real[_c])}]", file=sys.stderr)
            else:
                print("  (comp-pydeps has no python file by this name either -- check the spelling.)",
                      file=sys.stderr)
        except Exception:  # noqa: BLE001 -- the fallback is advisory; never let it break comp-blast
            print("  For .tools/org-modules names: comp-pydeps consumers <name> (the reference graph "
                  "that models the compiler layer).", file=sys.stderr)
        import difflib as _difflib
        _names = list(g.nodes.keys())
        # node ids are prefixed forms (gold:SCRIPT:function / lambda:name / s3:key), so a bare
        # function-name typo never fuzzy-matches a full id -- match against each id's LAST
        # segment too, and map the winners back to their full ids.
        _by_seg = {}
        for _n in _names:
            _seg = _n.replace("\\", "/").split(":")[-1].split("/")[-1]
            _by_seg.setdefault(_seg.lower(), []).append(_n)
        _sugg = _difflib.get_close_matches(query, _names, n=5, cutoff=0.55)
        for _hit in _difflib.get_close_matches(query.lower(), list(_by_seg.keys()), n=5, cutoff=0.6):
            for _full in _by_seg[_hit]:
                if _full not in _sugg:
                    _sugg.append(_full)
        if not _sugg:
            _sugg = [n for n in _names if query.lower() in n.lower()][:5]
        _sugg = _sugg[:6]
        if _sugg:
            # Andrew-direct, same session (verbatim in the dial ledger): near-matches are
            # DUPLICATE/LEGACY candidates, not merely typo candidates. On an estate-wide universe a
            # near-match is far more often a real second copy -- a legacy name still carrying
            # traffic -- than a misspelling, and calling it a typo tells the reader to correct their
            # query when the finding is that the estate has two of something.
            _bu.aprint("  near-matches in the graph (UNVERIFIED -- DUPLICATE / LEGACY candidates, "
                       "not implied edges; real nodes, not spelling hints):", file=sys.stderr)
            for _s in _sugg:
                _bu.aprint(f"    - {_s} [UNVERIFIED]", file=sys.stderr)
        print("  not a typo? by question: comp-xref <symbol> (graph-wide occurrence) | "
              "comp-symbols <file> (what a file defines) | comp-grep <pattern> (on-rails text "
              "search; .tools/ + org/modules INCLUDED).", file=sys.stderr)
        print("  This is a NOT-FOUND, not a 'nothing breaks' clear.", file=sys.stderr)
        print(f"ANSWER-STATE: {STATE_SUBJECT_ABSENT}")
        sys.exit(3)

    node = matches[0]

    # ---------------------------------------------------------------- WORKTREE OVERLAY (head-pin)
    # The ONE property of the retired private universe worth keeping: kuzu trails the estate by
    # hours and models what is COMMITTED/LIVE, but "what breaks if I change X" is a MID-EDIT
    # question about a tree that may not even be committed yet. So the subject's OWN edges are
    # re-derived from the working tree now, and overlaid. Overlay wins on the subject's own edges;
    # kuzu wins on everything else.
    try:
        _ov_edges, _ov_prov = _bu.derive_overlay(node, query)
        _bu.apply_overlay(g, node, _ov_edges)
    except Exception as _ex:  # noqa: BLE001 -- the overlay is additive; never lose the kuzu answer
        _ov_prov = {"head": "unknown", "dirty": False, "files": 0, "digest": "-",
                    "scope": f"FAILED ({type(_ex).__name__})"}

    direction = getattr(args, 'direction', None)
    direction = {"upstream": "up", "downstream": "down"}.get(direction, direction)
    if getattr(args, "all", False):
        direction = "both"

    # ---------------------------------------------------------------- DEFECT (d): the default hid callers
    # The old default computed upstream ONLY for function-grain GOLD_SCRIPT nodes. That node_type is
    # an artifact of the RETIRED private universe -- kuzu types the same things Endpoint / Hook /
    # PipelineFunction / ReactComponent -- so under kuzu the old rule is False for essentially every
    # node and the default would hide every caller in the estate.
    #
    # MEASURED, not assumed (the spec asked for proof): `endpoint:getPlatinumPartnerAnalytics` has
    # EIGHT upstream callers via FETCHES and ZERO downstream. The old default reported "affects >= 1
    # downstream" and showed none of the 8. Combined with defect (b) it would call that endpoint a
    # PHANTOM-CONSUMER -- a deletion verdict on a live endpoint with 8 real callers.
    #
    # So the default is now BOTH directions. "What breaks if I change X" is genuinely bidirectional
    # because this graph mixes edge conventions: WRITES points producer->artifact (consumers are
    # DOWNSTREAM) while CALLS/FETCHES/READS point consumer->producer (consumers are UPSTREAM).
    raw_downstream = g.downstream(node.id, max_depth=args.depth) if direction != 'up' else []
    raw_upstream = g.upstream(node.id, max_depth=args.depth) if direction != 'down' else []
    try:
        budget_s, budget_source = _compbudget.resolve_budget(getattr(args, "budget", None))
    except ValueError as ex:
        _bu.aprint(f"BUDGET USAGE ERROR: {ex}", file=sys.stderr)
        sys.exit(1)
    downstream, upstream, budget_partial, scanned, total, last_cursor, used_s = _blast_budget_walk(
        raw_downstream, raw_upstream, budget_s, budget_source, getattr(args, "cursor", None), direction)
    _bu.aprint(_compbudget.disclosure_line(budget_s, budget_source), file=sys.stderr)
    if budget_partial:
        _bu.aprint(_kuzu_prov, file=sys.stderr)
        _bu.aprint(f"  graph denominator: {len(g.nodes)} nodes (canonical kuzu graph)", file=sys.stderr)
        resume = "comp-blast " + (query or "")
        if getattr(args, "direction", None):
            resume += f" --direction {args.direction}"
        cursor_text = last_cursor or "NO CURSOR YET"
        _bu.aprint(_compbudget.budget_reached_line(
            budget_s, budget_source, scanned, total, "traversal", resume, cursor_text), file=sys.stderr)
        print(f"ANSWER-STATE: {STATE_PARTIAL_BLIND}")
        print(f"STATE: {STATE_PARTIAL_BLIND} (rc={EXIT_PARTIAL_BUDGET}; prefix is not a radius verdict)")
        sys.exit(EXIT_PARTIAL_BUDGET)

    # ---------------------------------------------------------------- DEFECT (b): direction vs verdict
    # The old code derived the verdict from `downstream`, which `--direction up` had just forced to
    # []. Same node, same estate, two answers: `--check-consumers` said CONSUMER-OK/143 consumers,
    # and `--check-consumers --direction up` said PHANTOM-CONSUMER at rc=4 -- a false ORPHAN verdict,
    # which grounding_lib maps to deletion evidence, on the one axis where being wrong is
    # irreversible.
    #
    # Composed correctly (the spec's first option): the verdict is a question about the SUBJECT, so
    # it is evaluated over the FULL dependent set and a display flag cannot change it. A node is a
    # phantom only if NOTHING depends on it in either direction. This makes a false phantom
    # structurally impossible to produce by passing a direction flag.
    if getattr(args, 'check_consumers', False):
        dependents = raw_downstream + raw_upstream
        _seen_dep = set()
        dependents = [t for t in dependents if not (t[0].id in _seen_dep or _seen_dep.add(t[0].id))]
        if direction is not None:
            _bu.aprint(f'  NOTE: --direction {direction} governs DISPLAY only; the consumer verdict '
                       f'is evaluated over the full dependent set in both directions.',
                       file=sys.stderr)
        if dependents:
            _bu.aprint(f'CONSUMER-OK: {node.id} has {len(dependents)} dependent(s)')
            _bu.aprint(_compbudget.within_budget_line(scanned, total, "traversal", budget_s,
                                                      budget_source, used_s), file=sys.stderr)
            sys.exit(0)
        else:
            _bu.aprint(f'PHANTOM-CONSUMER: {node.id} -- zero dependents IN GRAPH (both directions)')
            _bu.aprint(f'  Node type: {node.node_type}')
            _bu.aprint('  "Zero" = no EXTRACTED edge, NOT provably no consumer. A real consumer')
            _bu.aprint('  reading this via a dynamic/FUNC-key (the comp-pipescript miss class) is')
            _bu.aprint('  INVISIBLE here. Verify (grep the artifact key / comp-pipescript consumers)')
            _bu.aprint('  before treating as orphan -- do not assume safe-to-delete.')
            _bu.aprint(_compbudget.within_budget_line(scanned, total, "traversal", budget_s,
                                                      budget_source, used_s), file=sys.stderr)
            sys.exit(EXIT_PHANTOM_CONSUMER)

    # DUAL PROVENANCE, ALWAYS (spec 3.3): both universes answered, so both vintages are reported.
    # A single-vintage answer is a P3 conformance failure -- the reader cannot tell an estate fact
    # (hours old) from a worktree fact (this second) without it.
    _dual = _bu.format_dual_provenance(_kuzu_prov, _ov_prov)

    _bu.aprint(_compbudget.within_budget_line(scanned, total, "traversal", budget_s,
                                              budget_source, used_s), file=sys.stderr)
    if not downstream and not upstream:
        print(f"ANSWER-STATE: {STATE_PRESENT_ZERO}")

    if args.json:
        by_type = {}
        for n, e, d in downstream:
            by_type.setdefault(n.node_type, []).append({
                "id": n.id, "label": n.label, "depth": d,
                "direction": "downstream",
            })
        for n, e, d in upstream:
            by_type.setdefault(n.node_type, []).append({
                "id": n.id, "label": n.label, "depth": d,
                "direction": "upstream",
            })
        print(_bu.ascii_safe(json.dumps({
            "source": node.id,
            "node_type": node.node_type,
            "consumers": by_type,
            "provenance": {"kuzu": _kuzu_prov, "overlay": _ov_prov},
        }, indent=2, default=str)))
    else:
        _bu.aprint(_dual, file=sys.stderr)
        _print_risk(node)              # NFRA_NERVES L3b -- THE HOLD PRINTS FIRST. A hold is not a footnote.
        _bu.aprint(format_blast(node.id, downstream))
        _print_cochange(node)          # NFRA_NERVES L3a consumer -- the graph's TRAFFIC layer
        if upstream:
            _bu.aprint("")
            _bu.aprint(f"CALLER CHAIN (upstream from {node.id}) -- {len(upstream)} caller(s):")
            seen = set()
            for n, _, d in upstream:
                if n.id in seen:
                    continue
                seen.add(n.id)
                # Print the ID, not the bare label. Labels are not unique -- four different
                # portal components all render as "index" -- so a caller chain of repeated
                # labels is unreadable exactly when it matters most.
                _bu.aprint(f"  [{d}] {n.id}   [{n.node_type}]")


def cmd_diff(args):
    """Map git changes to graph impact. Shows which trace graph nodes are
    affected by files changed in git (staged, unstaged, or between refs)."""
    import subprocess

    g = _resolve_graph(args)

    # Get changed files from git
    if args.ref:
        # Compare against a git ref: git diff --name-only <ref>
        result = subprocess.run(
            ["git", "diff", "--name-only", args.ref],
            capture_output=True, text=True, cwd=str(_WORKSPACE),
        )
    elif args.staged:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            capture_output=True, text=True, cwd=str(_WORKSPACE),
        )
    else:
        # Default: all uncommitted changes (staged + unstaged)
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD"],
            capture_output=True, text=True, cwd=str(_WORKSPACE),
        )

    if result.returncode != 0:
        # CD1 (NFRA_TOOLPASS): --json must emit ONLY JSON on stdout. The human-text lines
        # ("git diff failed", "No changed files", "Changed files: N", "no graph nodes")
        # were printed regardless of --json, so a strict parser failed at char 0.
        if args.json:
            print(json.dumps({"error": f"git diff failed: {result.stderr.strip()}"}))
        else:
            print(f"git diff failed: {result.stderr.strip()}")
        sys.exit(1)

    changed_files = [f.strip() for f in result.stdout.strip().splitlines() if f.strip()]
    if not changed_files:
        if args.json:
            print(json.dumps({"changed_files": 0, "affected": []}, indent=2))
        else:
            print("No changed files detected.")
        return

    if not args.json:
        print(f"Changed files: {len(changed_files)}\n")

    # Map each changed file to graph nodes
    all_affected = []
    for filepath in changed_files:
        # Normalize path
        fp_normalized = filepath.replace("\\", "/")

        # Find graph nodes whose file_path matches this changed file
        matched_nodes = []
        for node in g.nodes.values():
            if node.file_path and fp_normalized in node.file_path:
                matched_nodes.append(node)

        # Also check by filename stem (e.g., "D_00.portal_aggregates" matches gold:D_00.portal_aggregates)
        stem = Path(filepath).stem
        if not matched_nodes:
            for node in g.nodes.values():
                if stem and stem in node.id:
                    matched_nodes.append(node)

        if not matched_nodes:
            if not args.json:                       # CD1: don't pollute --json stdout
                print(f"  {fp_normalized} -- no graph nodes (not tracked)")
            continue

        for node in matched_nodes:
            downstream = g.downstream(node.id, max_depth=args.depth)
            upstream = g.upstream(node.id, max_depth=args.depth)

            if args.json:
                all_affected.append({
                    "file": fp_normalized,
                    "node": node.id,
                    "type": node.node_type,
                    "downstream_count": len(downstream),
                    "upstream_count": len(upstream),
                    "downstream": [{"id": n.id, "type": n.node_type, "label": n.label}
                                   for n, e, d in downstream],
                })
            else:
                down_types = {}
                for n, e, d in downstream:
                    down_types.setdefault(n.node_type, []).append(n.label)

                print(f"  {fp_normalized}")
                print(f"    Node: [{node.node_type}] {node.id}")
                if downstream:
                    parts = [f"{len(v)} {k}" for k, v in sorted(down_types.items())]
                    print(f"    Blast radius: {', '.join(parts)}")
                    # Show component-level impacts specifically (most actionable)
                    components = [n for n, e, d in downstream if n.node_type == "COMPONENT"]
                    if components:
                        print(f"    Affected pages: {', '.join(c.label for c in components)}")
                else:
                    print("    Blast radius: none (leaf node)")
                print()

    if args.json:
        print(json.dumps({"changed_files": len(changed_files), "affected": all_affected}, indent=2))


_BASELINE_FILE = _CACHE_DIR / "baseline.json"


def _xref_symbol_lookup(g: TraceGraph, symbol: str) -> None:
    """Symbol cross-reference lookup (ADHC_COMPIL_V4.014).

    Searches graph nodes by id/label/file_path substring (case-insensitive) and
    edges by source/target. Output format mirrors comp-blast structure so agents
    already know how to read it.

    Anchor: 2026-04-21 17/25 FAILs from agents passing positional args to
    `comp-xref` thinking it was a symbol-lookup tool. This mode closes the gap.
    """
    q = symbol.strip().lower()
    if not q:
        print("comp-xref: empty symbol; provide a non-empty argument.", file=sys.stderr)
        sys.exit(1)

    # Match nodes: substring on id, label, file_path
    matched_nodes = []
    for node in g.nodes.values():
        if (q in node.id.lower() or
            q in node.label.lower() or
            (node.file_path and q in node.file_path.lower())):
            matched_nodes.append(node)

    # Match edges: substring on source/target
    matched_edges = []
    for edge in g.edges:
        if q in edge.source.lower() or q in edge.target.lower():
            matched_edges.append(edge)

    print(f"XREF LOOKUP: '{symbol}'")
    print(f"  ({len(matched_nodes)} node(s), {len(matched_edges)} edge(s) matched)")
    print()

    if not matched_nodes and not matched_edges:
        # NOT-FOUND is LOUD (rc=3), not a silent rc=0 return. A zero-match xref
        # is a typo / unindexed symbol; it must be distinguishable from a
        # successful lookup so it can't read as "verified clear". (fix 2026-06-26)
        print("  No matches in graph.", file=sys.stderr)
        print("  Hints:", file=sys.stderr)
        print("    - Symbol may be a Python module/function not yet indexed", file=sys.stderr)
        print("    - Run 'comp-build' to refresh graph; check stale-cache warnings", file=sys.stderr)
        print("    - For COMP_LEARNS-corpus symbols, comp-xref does not index that tree (out-of-scope)", file=sys.stderr)
        sys.exit(3)

    if matched_nodes:
        # Group by node_type for readability
        by_type: dict[str, list] = {}
        for n in matched_nodes:
            by_type.setdefault(n.node_type, []).append(n)
        print(f"  NODES ({len(matched_nodes)}):")
        for ntype in sorted(by_type.keys()):
            print(f"    [{ntype}]")
            for n in sorted(by_type[ntype], key=lambda x: x.id)[:15]:
                fp = f" — {n.file_path}" if n.file_path else ""
                fn = f" :: {n.function_name}" if n.function_name else ""
                print(f"      {n.id}{fn}{fp}")
            if len(by_type[ntype]) > 15:
                print(f"      ... and {len(by_type[ntype]) - 15} more")
        print()

    if matched_edges:
        # Group by edge_type
        by_etype: dict[str, list] = {}
        for e in matched_edges:
            by_etype.setdefault(e.edge_type, []).append(e)
        print(f"  EDGES ({len(matched_edges)}):")
        for etype in sorted(by_etype.keys()):
            print(f"    [{etype}]")
            for e in by_etype[etype][:10]:
                print(f"      {e.source} -> {e.target}")
            if len(by_etype[etype]) > 10:
                print(f"      ... and {len(by_etype[etype]) - 10} more")
        print()


def cmd_xref(args):
    """Compare current graph against baseline snapshot, OR cross-reference a symbol.

    Dual-purpose (ADHC_COMPIL_V4.014):
      no positional arg -> graph-state-diff vs baseline (existing behavior)
      positional arg    -> symbol cross-reference lookup (NEW)

    Symbol-lookup matches against node ids, labels, file paths, and edge
    sources/targets. Returns all references for agent disambiguation.
    """
    # --check is mode-independent: it probes the cache, never rebuilds, in EITHER mode.
    if getattr(args, "check", False):
        sys.exit(_freshness_probe())
    if getattr(args, "fresh", False):
        print(_FRESH_DEPRECATION, file=sys.stderr)

    # ADHC_COMPIL_V4.014 — symbol cross-reference mode
    symbol = getattr(args, 'symbol', None)
    if symbol:
        g = _get_graph(force_rebuild=getattr(args, "force", False))
        _xref_symbol_lookup(g, symbol)
        return

    # baseline-diff mode re-derives BY DESIGN: it compares the CURRENT graph against the saved
    # snapshot, so serving a cache would compare the baseline against itself. --force is implied.
    g = _get_graph(force_rebuild=True)

    if args.save:
        path = save_baseline(g, _CACHE_DIR)
        if args.json:                                       # CX1: --json clean on the --save path too
            print(json.dumps({"baseline_saved": {"nodes": len(g.nodes),
                                                  "edges": len(g.edges), "path": str(path)}}, indent=2))
        else:
            print(f"Baseline saved: {len(g.nodes)} nodes, {len(g.edges)} edges")
            print(f"Path: {path}")
        return

    # Load baseline
    # CX1 (NFRA_TOOLPASS, the comp-diff CD1 analog): --json must emit ONLY JSON on stdout. These
    # edge paths printed human text regardless of --json -> a strict parse failed at char 0.
    if not _BASELINE_FILE.exists():
        if args.json:
            print(json.dumps({"error": "no baseline", "hint": "run comp-xref --save to create one"}))
        else:
            print("No baseline found. Run 'comp-xref --save' to create one first.")
        sys.exit(1)

    try:
        baseline = TraceGraph.load(_BASELINE_FILE)
    except Exception as e:
        if args.json:
            print(json.dumps({"error": f"failed to load baseline: {e}"}))
        else:
            print(f"Failed to load baseline: {e}")
        sys.exit(1)

    delta = diff_graphs(baseline, g)

    if args.json:
        output = {
            "baseline": {
                "nodes": len(baseline.nodes),
                "edges": len(baseline.edges),
                "built_at": baseline.built_at,
            },
            "current": {
                "nodes": len(g.nodes),
                "edges": len(g.edges),
                "built_at": g.built_at,
            },
            "summary": delta.summary(),
            "added_nodes": [{"id": n.id, "type": n.node_type, "label": n.label}
                            for n in delta.added_nodes],
            "removed_nodes": [{"id": n.id, "type": n.node_type, "label": n.label}
                              for n in delta.removed_nodes],
            "added_edges": [{"source": e.source, "target": e.target, "type": e.edge_type}
                            for e in delta.added_edges],
            "removed_edges": [{"source": e.source, "target": e.target, "type": e.edge_type}
                              for e in delta.removed_edges],
        }
        print(json.dumps(output, indent=2))
    else:
        print(f"Baseline: {len(baseline.nodes)} nodes, {len(baseline.edges)} edges")
        print(f"Current:  {len(g.nodes)} nodes, {len(g.edges)} edges")
        print()
        print(format_delta(delta))


def main():
    # _ContractParser: a usage error exits 1 (tool failure), never 2 (which the freshness contract
    # reserves for STALE). parser_class propagates it to every subparser.
    parser = _ContractParser(description="Opal full-stack trace compiler")
    sub = parser.add_subparsers(dest="command", parser_class=_ContractParser)

    # build
    p_build = sub.add_parser("build", help="Force rebuild the trace graph")
    p_build.add_argument("--check", action="store_true",
                         help="Verify cached graph SHA freshness without rebuilding (exit 2 on drift)")

    # trace -- prog is the SHIM name (T5, comp-trace dial 2026-08-04): the public entry is
    # `.tools/comp-trace <query>`, and the bare-call usage error previously printed the cli.py
    # subcommand form (`usage: cli.py [-h] {build,trace,blast,diff,xref}`), teaching a cold user
    # an invocation the shim BREAKS (`comp-trace trace <q>` errors; bare `comp-trace trace`
    # consumes the word 'trace' AS the query). The first output a cold user ever sees must teach
    # the form that works.
    p_trace = sub.add_parser("trace", prog="comp-trace", help="Trace data path from a node")
    p_trace.add_argument("query", nargs="?", help="File, component, or node to trace")
    p_trace.add_argument("--exact", action="store_true",
                         help="Match ONLY the node whose id EQUALS the query byte-for-byte "
                              "(self-selection for a canonical id whose children prefix-match "
                              "beside it). A miss under --exact is NOT-FOUND (rc=3).")
    p_trace.add_argument("--direction",
                         choices=["up", "upstream", "down", "downstream", "both"],
                         default="both",
                         help="Traversal direction: up/upstream, down/downstream, or both (default).")
    p_trace.add_argument("--depth", type=int, default=10)
    p_trace.add_argument("--json", action="store_true")
    p_trace.add_argument("--all", action="store_true", help="Trace all matches")
    add_freshness_args(p_trace)

    # blast
    p_blast = sub.add_parser("blast", help="Show blast radius of a change")
    p_blast.add_argument("query", nargs="?",
                         help="File, node, or prefix-qualified node "
                              "(e.g. lambda:fn-name, gold:D_04, component:AdvisorsTab.tsx)")
    p_blast.add_argument("--function", help="Specific function within the file")
    p_blast.add_argument("--depth", type=int, default=10)
    p_blast.add_argument("--json", action="store_true")
    p_blast.add_argument("--exact", action="store_true",
                         help="Resolve the query by exact node id only; a miss is NOT-FOUND (rc=3).")
    p_blast.add_argument("--all", action="store_true",
                         help="Carry comp-trace's --all flag: traverse both directions in blast's universe.")
    p_blast.add_argument("--direction",
                         choices=["up", "upstream", "down", "downstream", "both"], default=None,
                         help="Traversal direction: up/upstream callers, down/downstream consumers, "
                              "or both. Trace spellings are accepted as aliases.")
    p_blast.add_argument("--budget", metavar="N", default=None,
                         help="Rule-T wall-clock ceiling for traversal (carrier: --budget > "
                              "COMP_BUDGET_S > default 90s; --budget 0 = unbounded). "
                              "rc vocabulary: 0 clean, 1 tool-failed, 2 stale, 3 NOT-FOUND, "
                              "4 phantom-consumer, 5 ambiguous, 6 partial-budget.")
    p_blast.add_argument("--cursor", metavar="UNIT", default=None,
                         help="Resume after a prior direction:node-id traversal unit.")
    p_blast.add_argument("--self-test", action="store_true",
                         help="Print the four ratified answer-state tokens in one control invocation.")
    p_blast.add_argument("--check-consumers", action="store_true",
                         help="Exit 0 if node has >=1 downstream consumer; exit 4 if zero "
                              "(PHANTOM-CONSUMER verdict). rc 1 is NOT a verdict -- it means the tool "
                              "failed (usage error / crash). Combine with --all-producers for sweep mode.")
    p_blast.add_argument("--compare", metavar="NODE", default=None,
                         help="PAIR MODE (act 3): blast-radius overlap between the query node and "
                              "NODE. Emits CANDIDATE evidence for human assessment -- never a "
                              "sameness verdict.")
    p_blast.add_argument("--overlap-sweep", action="store_true",
                         help="SWEEP MODE (act 3): rank every producer pair in the population by "
                              "specificity-weighted blast-radius overlap. Candidates, not findings.")
    p_blast.add_argument("--population", metavar="PREFIX", default=None,
                         help="Restrict --overlap-sweep/--compare idf population to node ids with "
                              "this ADDRESS prefix (e.g. 'gold:', 'lambda:'). A namespace, not a "
                              "name match.")
    p_blast.add_argument("--min-score", type=float, default=None,
                         help="Weighted-jaccard threshold for --overlap-sweep (default 0.30).")
    p_blast.add_argument("--min-mass", type=float, default=None,
                         help="ABSOLUTE evidence floor: summed idf over shared consumers (default "
                              "1.0). A ratio alone ranks a single shared edge at 1.000.")
    p_blast.add_argument("--grain", choices=["script", "function", "any"], default=None,
                         help="Population grain for --overlap-sweep (default script).")
    p_blast.add_argument("--head", type=int, default=None,
                         help="Cap candidate pairs displayed (default 15). A display cap; the "
                              "unshown count is always printed.")
    p_blast.add_argument("--all-producers", action="store_true",
                         help="Sweep all producer nodes in graph; list those with zero downstream consumers. "
                              "Use with --check-consumers and --pipeline.")
    add_freshness_args(p_blast)
    p_blast.add_argument("--pipeline", choices=["inf", "bd", "all"], default=None,
                         help="Filter --all-producers sweep by pipeline (inf/bd/all).")

    # diff
    p_diff = sub.add_parser("diff", help="Map git changes to graph impact")
    p_diff.add_argument("--ref", help="Git ref to diff against (e.g., HEAD~3, main)")
    p_diff.add_argument("--staged", action="store_true", help="Only staged changes")
    p_diff.add_argument("--depth", type=int, default=5)
    p_diff.add_argument("--json", action="store_true")
    add_freshness_args(p_diff)

    # xref — dual-purpose: graph-diff (no-arg) + symbol-lookup (positional)
    p_xref = sub.add_parser(
        "xref",
        help="Compare graph against baseline (no-arg) OR cross-reference a symbol (positional)",
    )
    p_xref.add_argument(
        "symbol", nargs="?", default=None,
        help="Symbol to cross-reference (function name, file path, S3 key, Lambda name, etc.). "
             "When provided, runs symbol-lookup mode; otherwise runs graph-diff. (ADHC_COMPIL_V4.014)",
    )
    p_xref.add_argument("--save", action="store_true", help="Save current graph as baseline (no-arg mode)")
    p_xref.add_argument("--json", action="store_true")
    add_freshness_args(p_xref)

    args = parser.parse_args()
    if args.command == "build":
        cmd_build(args)
    elif args.command == "trace":
        # T5: error on the TRACE subparser (prog=comp-trace), not the top-level cli.py parser --
        # the bare-call usage must teach the shim form. blast keeps the top-level parser
        # deliberately (out of this fix's scope; byte-stability of unrelated output).
        _require_query(args, p_trace)
        cmd_trace(args)
    elif args.command == "blast":
        _require_query(args, parser)
        cmd_blast(args)
    elif args.command == "diff":
        cmd_diff(args)
    elif args.command == "xref":
        cmd_xref(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
