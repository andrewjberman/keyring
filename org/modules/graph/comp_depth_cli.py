"""
NFRA_GRAPHDEPTH P3 -- comp-depth: DEPTH-scoped querying on the ONE marker-head graph.

Every investigation needs TWO coordinates: BREADTH (where on the surface -- comp-blast/trace/xref)
and DEPTH (what grain -- this tool). comp-depth exposes the depth coordinate as a usable capability,
composing on the SAME marker-head read-handle (~D's comp_marker_read.py) the re-pointed breadth tools
use -- ONE head, provenance-checked on every call (D4 one-head). It is grain-CALIBRATED by the
grain_contract 0.8.0_AE_CloudComp~C governs (node_type_grain + drilldown_seams + strata in
comp-coverage-map.yaml) -- it reads the depth model, never re-derives it.

SIZE-INVARIANT (GRAPHDEPTH CTO ruling, PRD section 9): ONE tool + ONE type-system serves EVERY grain
-- a coarser or finer scope is a `--to`/`--grain` argument (a declared `level`), never a new tool or a
type fork. drill = coarse->fine over the stratum-stitchers; rollup = fine->coarse EXISTENTIAL (the ONE
definition shared with comp_coverage_check.rollup_defects, 047ce51d0).

Subcommands (grain in: resource container surface file script object function symbol type component
field endpoint route cluster -- the node_type_grain domain):
  comp-depth grains <node-id>              the node's grain(s) SET + CONTAINS-ladder level (its depth coord)
  comp-depth scope  <grain> [--limit N]    every node at <grain> (grain-scoped node set)
  comp-depth drill  <node-id> --to <grain> coarse->fine: the <grain>-grained descendants of the node
  comp-depth rollup <node-id> --to <grain> fine->coarse EXISTENTIAL: roll the node up to <grain>
  comp-depth blast  <node-id> --grain <g>  a breadth blast (CALLS/READS_S3/...) SCOPED to grain <g>
                                           (the depth x breadth composition -- e.g. a Lambda's blast
                                           at function-grain vs resource-grain)

Read-only, deterministic, ASCII-only. Author: 0.8.0_AE_CloudComp~C (NFRA_GRAPHDEPTH.P3). 2026-07-01.
"""

from __future__ import annotations

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
for _p in (_HERE, os.path.abspath(os.path.join(_HERE, "..", "..", "..", "infra", "aws", "globgrph"))):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import comp_marker_read as MR  # noqa: E402

# The breadth (cross-surface) edge classes a "blast" traverses -- the trace-graph scope the marker-head
# handle projects (kept in sync with comp_marker_read._TRACEGRAPH_EDGE_TYPES; a small superset is safe).
_BREADTH_EDGES = frozenset(("CALLS", "READS_S3", "WRITES_S3", "FETCHES", "TRIGGERS", "REFERENCES_TYPE"))


def _usage() -> int:
    sys.stdout.write(__doc__.split("Subcommands")[1].strip() if __doc__ else "comp-depth")
    sys.stdout.write("\n")
    return 0


def _prov_line(h) -> str:
    p = h.provenance or {}
    return "[marker-head: %s | head=%s]" % (p.get("status", "?"), str(p.get("marker_head"))[:24])


def _opt(argv, name):
    if name in argv:
        i = argv.index(name)
        if i + 1 < len(argv):
            return argv[i + 1]
    return None


def _fmt(nodes, limit=20):
    out = []
    for n in nodes[:limit]:
        gr = ",".join(n.metadata.get("grains") or []) or "-"
        lv = n.metadata.get("level")
        out.append("  %-52s [grain=%s level=%s]" % (n.id[:52], gr, lv))
    if len(nodes) > limit:
        out.append("  ... (%d more)" % (len(nodes) - limit))
    return "\n".join(out)


def _load():
    return MR.load_marker_head_graph()


def _full(h):
    """The UNSCOPED full projection for depth-scoping (all node namespaces + the RUNS/CONTAINS/OWNED_BY
    strata edges + grains/level metadata). ~D's handle splits as_tracegraph()=SCOPED (the re-point
    byte-match projection, no CONTAINS) from full()=unscoped; DEPTH-scoping needs the FULL estate, so
    use full() where present. Falls back to as_tracegraph() on the pre-split handle (there it IS the full
    graph). nodes()/drill()/rollup() already resolve the right projection internally."""
    f = getattr(h, "full", None)
    return f() if callable(f) else h.as_tracegraph()


def cmd_grains(argv) -> int:
    if not argv:
        sys.stderr.write("comp-depth grains <node-id>\n")
        return 2
    h = _load()
    print(_prov_line(h))
    tg = _full(h)
    cid = MR.canon_id(argv[0], "")
    n = tg.nodes.get(cid) or tg.nodes.get(argv[0])
    if n is None:
        print("node not found at the marker head: %s (canon: %s)" % (argv[0], cid))
        return 1
    md = n.metadata
    print("%s" % n.id)
    print("  node_type: %s" % n.node_type)
    print("  grains:    %s   (the DEPTH scope discriminator, node_type_grain)" % (md.get("grains") or []))
    print("  level:     %s   (CONTAINS-ladder position; None = pure resource-stratum)" % md.get("level"))
    return 0


def cmd_scope(argv) -> int:
    if not argv:
        sys.stderr.write("comp-depth scope <grain> [--limit N]\n")
        return 2
    grain = argv[0]
    limit = int(_opt(argv, "--limit") or 20)
    h = _load()
    print(_prov_line(h))
    nodes = h.nodes(scope_grain=grain)
    print("scope grain=%s -> %d node(s):" % (grain, len(nodes)))
    print(_fmt(nodes, limit))
    return 0


def cmd_drill(argv) -> int:
    to = _opt(argv, "--to")
    if not argv or not to:
        sys.stderr.write("comp-depth drill <node-id> --to <grain>\n")
        return 2
    h = _load()
    print(_prov_line(h))
    res = h.drill(argv[0], to)
    print("drill %s -> grain=%s (coarse->fine) -> %d node(s):" % (MR.canon_id(argv[0], ""), to, len(res)))
    print(_fmt(res))
    return 0


def cmd_rollup(argv) -> int:
    to = _opt(argv, "--to")
    if not argv or not to:
        sys.stderr.write("comp-depth rollup <node-id> --to <grain>\n")
        return 2
    h = _load()
    print(_prov_line(h))
    res = h.rollup(argv[0], to)
    print("rollup %s -> grain=%s (fine->coarse, existential) -> %d node(s):"
          % (MR.canon_id(argv[0], ""), to, len(res)))
    print(_fmt(res))
    return 0


def cmd_blast(argv) -> int:
    grain = _opt(argv, "--grain")
    if not argv or not grain:
        sys.stderr.write("comp-depth blast <node-id> --grain <grain>\n")
        return 2
    h = _load()
    print(_prov_line(h))
    tg = _full(h)
    start = MR.canon_id(argv[0], "")
    # breadth BFS both directions over the cross-surface edges (impact set + callers), then SCOPE to grain.
    fwd, rev = {}, {}
    for e in tg.edges:
        if e.edge_type in _BREADTH_EDGES:
            fwd.setdefault(e.source, []).append(e.target)
            rev.setdefault(e.target, []).append(e.source)
    seen, stack = set(), [start]
    while stack:
        cur = stack.pop()
        if cur in seen:
            continue
        seen.add(cur)
        stack.extend(fwd.get(cur, []))
        stack.extend(rev.get(cur, []))
    seen.discard(start)
    scoped = [tg.nodes[i] for i in seen
              if i in tg.nodes and grain in set(tg.nodes[i].metadata.get("grains") or [])]
    print("blast %s (breadth) SCOPED to grain=%s -> %d of %d reachable node(s):"
          % (start, grain, len(scoped), len(seen)))
    print(_fmt(scoped))
    return 0


_CMDS = {"grains": cmd_grains, "scope": cmd_scope, "drill": cmd_drill,
         "rollup": cmd_rollup, "blast": cmd_blast}


def main(argv) -> int:
    for _s in (sys.stdout, sys.stderr):  # uncrashable output on a cp1252 console
        try:
            _s.reconfigure(errors="replace")
        except Exception:  # noqa: BLE001
            pass
    if not argv or argv[0] in ("-h", "--help"):
        return _usage()
    fn = _CMDS.get(argv[0])
    if fn is None:
        sys.stderr.write("comp-depth: unknown subcommand %r\n" % argv[0])
        return _usage()
    try:
        return fn(argv[1:])
    except Exception as e:  # noqa: BLE001 -- never a stack-trace dump on a read tool
        sys.stderr.write("comp-depth: %s\n" % e)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
