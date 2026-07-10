"""NFRA_GRAPHUNI P2/D2 (b) -- D4 ONE-HEAD ASSERTION test.

The load-bearing proof that the stale-cache-phantom class (the 1347-vs-1337 catch) is DEAD:
NO structure tool serves a divergent-vintage (drifted) cache. A cache that has drifted from the
current source is a MISS -> rebuild (head-pinned), never a serve-stale. Covers BOTH head-pinned
paths:
  - gc.cached DEFAULT (comp-platinum): fingerprint-gated.
  - cli.py::_get_graph (comp-blast/trace/xref): source-SHA-drift-gated.

Author: 0.8.0_AE_CloudComp~D (NFRA_GRAPHUNI P2/D2 (b), JOINT VERDICT 20260701). Deterministic,
non-destructive (touches only the local cache; rebuilds it fresh at the end).
"""

import os
import shutil
import sys
import tempfile
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
_GRAPH = os.path.dirname(_HERE)                                 # org/modules/graph
_WS = os.path.dirname(os.path.dirname(os.path.dirname(_GRAPH)))  # workspace root
for _p in (_GRAPH, _WS):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import graph_cache as gc  # noqa: E402


def test_gc_default_head_pinned_drift_miss():
    """comp-platinum path: gc.DEFAULT honors the source fingerprint -- MATCH hits, DRIFT misses."""
    name = "_d4_headpin_test"
    gc.store(name, {"v": 1}, fingerprint=(100, 5))
    try:
        hit, _ = gc.load(name, gc.Freshness.DEFAULT, current_fingerprint=(100, 5))
        miss, _ = gc.load(name, gc.Freshness.DEFAULT, current_fingerprint=(999, 9))
        assert hit is not None, "drift-free cache must HIT (serve current vintage)"
        assert miss is None, "DRIFTED cache must MISS -> rebuild (head-pin); never serve-stale"
    finally:
        p = gc.cache_file(name)
        if os.path.exists(p):
            os.remove(p)


# Sovereign (49F/bd standing prohibition): never TARGET a bd/49F node as the poison
# victim. The freshness contract mechanically hashes every indexed file (the tool's job),
# but the victim we deliberately poison + assert on must be non-bd. Deterministic pick =
# alphabetically-first non-bd file-backed node.
_BD_MARKERS = ("black_diamond", "schwab", "opal-data-bd", "opal-data-schwab")


def _pick_nonbd_victim(graph):
    def _is_bd(n):
        hay = (n.id + " " + (n.file_path or "")).lower()
        return any(m in hay for m in _BD_MARKERS)
    cands = sorted((n for n in graph.nodes.values()
                    if n.source_sha and n.file_path and not _is_bd(n)),
                   key=lambda n: n.id)
    return cands[0] if cands else None


def test_get_graph_rebuilds_on_source_drift():
    """comp-blast/trace/xref path: a cache whose node source_sha has DRIFTED from the live source is
    NOT served -- _get_graph rebuilds, returning the CURRENT sha (never the drifted cache).

    ISOLATION (NFRA_TOOLPASS B3/B4 fix, 3.0.0_SA_CVO~B): the module cache path is redirected
    to a throwaway dir BEFORE any _get_graph call, so this test NEVER writes the production
    _CACHE_FILE. A SIGKILL at any point (the fabric reaps orphan python) leaves the production
    cache untouched -- the prior version poisoned the REAL cache and relied on a `finally`
    rebuild that a reap skips, which is exactly how DRIFTED_0000000000 leaked into the live graph.
    """
    import org.modules.graph.cli as cli
    from org.modules.graph.trace_graph import TraceGraph

    orig_cache = cli._CACHE_FILE
    tmpdir = tempfile.mkdtemp(prefix="d4_headpin_")
    cli._CACHE_FILE = Path(tmpdir) / "graph.json"          # redirect BEFORE any build/write
    try:
        cli._get_graph(force_rebuild=True, check_freshness=False)   # fresh cache in TMP only
        disk = TraceGraph.load(cli._CACHE_FILE)
        victim = _pick_nonbd_victim(disk)
        assert victim is not None, "expected at least one non-bd file-backed node with a source_sha"
        real_sha = victim.source_sha
        victim.source_sha = "DRIFTED_0000000000"                    # simulate source drift (TMP copy)
        disk.save(cli._CACHE_FILE)
        g2 = cli._get_graph(check_freshness=True)                   # must detect drift -> REBUILD
        n2 = g2.nodes.get(victim.id)
        assert n2 is not None and n2.source_sha == real_sha, (
            "head-pin must REBUILD on source drift (serve the CURRENT sha), never serve the "
            "drifted cache -- this is the D4 one-head guarantee / stale-cache-phantom kill")
    finally:
        # in-memory restore + tmp cleanup ONLY. The production cache was never a write target,
        # so this `finally` is hygiene, not correctness -- a reap that skips it still leaves
        # production untouched (the whole point of the isolation).
        cli._CACHE_FILE = orig_cache
        shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == "__main__":
    test_gc_default_head_pinned_drift_miss()
    print("PASS: gc.DEFAULT head-pinned (drift->miss)")
    test_get_graph_rebuilds_on_source_drift()
    print("PASS: _get_graph rebuilds on source drift (no divergent-vintage serve)")
    print("D4 ONE-HEAD ASSERTION: PASS")
