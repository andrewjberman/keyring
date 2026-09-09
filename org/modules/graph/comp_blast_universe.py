"""comp-blast's UNIVERSE: the canonical Kuzu resource graph + a subject-scoped worktree overlay.

ANDREW-DIRECT RULING 2026-08-03 (ANDREW_RULING_projections_default_kuzu_full_graph_20260803.md,
verbatim): "all projections should by default be kuzudb full resource graph, or at the very least
territory-specific full graph ... Comp-blast absolutely should cover all of AWS."

WHAT THIS REPLACES AND WHY
--------------------------
comp-blast used to build a PRIVATE trace graph at invocation (trace_graph.build_graph, 8 accreted
extraction passes): 2,255 nodes / 2,950 edges / ~35s cold, carrying exactly FOUR S3_BUCKET nodes.
`comp-blast opal-data-mdpf` -- a real production bucket with live consumers -- returned NOT-FOUND,
while the canonical graph resolved it. The full graph existed, was fresh, and knew the answer; the
projection did not ask it. A private universe is not a smaller answer, it is a CONFIDENT WRONG ONE:
NOT-FOUND on a Rule-20 change-safety gate reads as "nothing breaks."

THE ONE PROPERTY WORTH PRESERVING is invocation-time HEAD-PINNING. Kuzu models the committed/live
estate and trails it by hours; "what breaks if I change X" is a MID-EDIT question about a working
tree that may not even be committed. So the trace graph's head-pin survives as a SUBJECT-SCOPED
OVERLAY (seconds, one file) rather than as a whole private universe (35s, everything).

  UNIVERSE  = kuzu           -- existence, denominator, typology, estate-wide traversal
  OVERLAY   = worktree       -- the blasted SUBJECT's own edges, re-derived NOW
  PRECEDENCE= overlay wins on the subject's own out-edges; kuzu wins on everything else

FAIL LOUD, NEVER FALL BACK. If kuzu is unreachable this module raises. It must NOT silently drop to
a private scan -- a silent fallback re-creates the exact defect the ruling removes, and it would do
so INVISIBLY, which is worse than the original because the original at least said NOT-FOUND.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

_WORKSPACE = Path(__file__).resolve().parent.parent.parent.parent
_GLOBGRPH = _WORKSPACE / "infra" / "aws" / "globgrph"

if str(_WORKSPACE) not in sys.path:
    sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph.trace_graph import Edge, Node, TraceGraph  # noqa: E402


# --------------------------------------------------------------------------- ASCII emission (defect a)
#: Transliterations for the characters the risk/co-change corpora actually carry. The corpora are
#: harvested from COMMIT MESSAGES and ledger prose, so non-ASCII is a permanent inflow, not a
#: one-time dirty-data event -- which is exactly why the fix belongs at the EMISSION BOUNDARY and
#: not in the data. Editing the corpus would fix today's 28 nodes and silently re-break on the next
#: harvest.
_TRANSLIT = {
    "→": "->", "←": "<-", "↔": "<->", "⇒": "=>",
    "—": "--", "–": "-", "‑": "-", "−": "-",
    "‘": "'", "’": "'", "“": '"', "”": '"', "‚": ",",
    "…": "...", " ": " ", "•": "*", "·": "*", "▪": "*",
    "✓": "OK", "✔": "OK", "✗": "X", "✘": "X", "✕": "X",
    "§": "S", "±": "+/-", "×": "x", "≈": "~", "≥": ">=",
    "≤": "<=", "≠": "!=", "€": "EUR", "£": "GBP", "″": '"',
}


def ascii_safe(text: str) -> str:
    """Render any string emittable on a cp1252 (Windows) stdout, losslessly where we can.

    DEFECT (a) ROOT, source-confirmed 2026-08-03: `nerves-risk-edges.json` stores non-ASCII
    JSON-ESCAPED (`\\u2192`), so the FILE is pure ASCII and a raw-text scan of it reports ZERO
    non-ASCII -- but `json.load` decodes the escape into a real arrow, and `_render_risk` prints
    that claim prose straight to stdout. Measured by sweeping the full denominator through a real
    cp1252 stream: 28 of 2,255 nodes raise UnicodeEncodeError (the 07-31 dial measured 20 of 2,252
    -- same class, count tracks the cache).

    THE FAILING NODES ARE THE RISK-BEARING ONES. A HOLD claim is precisely the output that must
    never be lost, so this crash silenced the warnings on the files most dangerous to change.

    CLAUDE.md Code Quality is the binding rule (no non-ASCII in anything that runs on AWS/CI).
    This is the ROOT fix the spec asks for -- an emission boundary every comp-blast print passes
    through -- not a try/except wrapper that converts a crash into a quieter crash.
    """
    if text is None:
        return ""
    s = str(text)
    if s.isascii():
        return s
    for bad, good in _TRANSLIT.items():
        s = s.replace(bad, good)
    if s.isascii():
        return s
    # Anything still unmapped: never raise, never drop the line, mark it visibly so a reader can
    # tell a transliteration happened rather than silently reading mangled evidence.
    return s.encode("ascii", "backslashreplace").decode("ascii")


def aprint(*args, **kwargs) -> None:
    """ASCII-safe print. The single emission boundary for comp-blast."""
    print(*[ascii_safe(a) for a in args], **kwargs)


def install_ascii_stdout() -> None:
    """Belt to aprint's braces: make the process's own streams ASCII-tolerant.

    Catches emission from code paths this build does not own (_render_risk, _print_cochange,
    argparse, tracebacks). Uses `backslashreplace` so nothing is silently deleted.
    """
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:
            continue
        try:
            enc = (getattr(stream, "encoding", "") or "").lower()
            if enc.replace("-", "") not in ("utf8", "utf_8"):
                reconfigure(errors="backslashreplace")
        except Exception:  # noqa: BLE001 -- emission hardening must never break the tool
            pass


# --------------------------------------------------------------------------- kuzu universe
class KuzuUnavailable(RuntimeError):
    """Kuzu could not be reached or read. comp-blast FAILS on this -- it never falls back."""


def _projection_client():
    """Import the ONE served-graph client (TO-CG-D-3 / CG-s-6). No local database exists."""
    if str(_GLOBGRPH) not in sys.path:
        sys.path.insert(0, str(_GLOBGRPH))
    try:
        import projection_client  # noqa: PLC0415
    except Exception as ex:  # noqa: BLE001
        raise KuzuUnavailable(
            f"cannot import the served graph client ({type(ex).__name__}: {ex}). "
            f"comp-blast's universe IS the served cloud graph -- it does not fall back to a "
            f"private scan and there is no local database left to read."
        ) from ex
    return projection_client


def _import_globgrph():
    """RETIRED SHIM (TO-CG-D-7, R7). The local `_canonical`/`_provenance`/`kuzu` triple this
    returned no longer exists on any consumer path; the universe comes from the served graph.
    Kept as a NAMED refusal rather than deleted so a stale caller gets a sentence, not an
    AttributeError."""
    raise KuzuUnavailable(
        "the local canonical kuzu layer is RETIRED (NFRA_CLDGRPH R7 / CG-s-8). The universe is "
        "the SERVED graph; use projection_client.connect() / load_kuzu_universe()."
    )


def kuzu_provenance(db_path: str | None = None) -> str:
    """The served graph's provenance block, from the service's OWN fields (never a client clock)."""
    try:
        pc = _projection_client()
        return ascii_safe(_served_provenance_block(pc.health()))
    except Exception as ex:  # noqa: BLE001
        return f"=== served graph provenance UNAVAILABLE ({type(ex).__name__}: {ex}) ==="


def _served_provenance_block(served: dict, nodes=None, edges=None) -> str:
    """The comp-kuzu-shaped provenance header, rebuilt from the SERVICE's response fields.

    The age is the service's `age_line` (source: the manifest's `committed_at`); there is no
    second clock here and no `STALE-SERVED` arm -- the served pointer IS the vintage, so a served
    graph cannot be labeled-stale (TO-CG-D-7 removed the seam that could label one)."""
    lines = ["=== served cloud graph (opal-globgrph projection) ==="]
    age_line = served.get("age_line") or (
        "Built from the estate as of %s." % str(served.get("vintage") or "unknown"))
    lines.append("  %s" % age_line)
    lines.append("  vintage: %s" % (served.get("vintage") or "unknown"))
    if served.get("manifest_sha256"):
        lines.append("  manifest: %s" % served["manifest_sha256"])
    if served.get("artifact_prefix"):
        lines.append("  artifact: %s" % served["artifact_prefix"])
    if nodes is not None or edges is not None:
        lines.append("  universe: %s nodes / %s edges (served, whole estate)" % (nodes, edges))
    lines.append("  transport: HTTPS /graph/cypher -- no local database, no cache, no fallback")
    return "\n".join(lines)


def load_kuzu_universe(db_path: str | None = None, refresh: bool = True, *,
                       budgeted: bool = False,
                       unbudgeted_label: str | None = None) -> tuple[TraceGraph, str, dict]:
    """Project the SERVED cloud graph into a TraceGraph.

    Returns (graph, provenance_block, served) -- `served` is the SERVICE's own provenance dict
    (`vintage`, `age_line`, `manifest_sha256`, `artifact_prefix`, plus the two counts this call
    measured). The third element used to be a local db path; there is no local path any more.

    TO-CG-D-7 (R7): the universe arrives over ONE transport, `projection_client.query`. Nothing
    here opens a database, imports `kuzu`, names a local directory, refreshes, or decides between
    full and incremental -- those decisions moved to the cloud engine and the pointer swap.
    `refresh` and `budgeted` are accepted for signature compatibility and are INERT: there is no
    refresh mutex a client can enter, so a bounded caller costs exactly what an unbounded one does.

    A TraceGraph is still the carrier ON PURPOSE: BFS traversal, `format_blast` and the
    PHANTOM-CONSUMER / CONSUMER-OK strings callers key on are reused unchanged.
    """
    if db_path:
        raise KuzuUnavailable(
            f"local database paths are RETIRED (NFRA_CLDGRPH R7 / CG-s-8): {db_path!r} will not be "
            f"opened. comp-blast's universe is the SERVED graph and there is no local copy to read."
        )
    pc = _projection_client()
    conn = pc.connect(timeout_s=240.0)

    try:
        res = conn.execute(
            "MATCH (n:CloudNode) RETURN n.node_id, n.node_type, n.name, n.layer, n.arn, "
            "n.source, n.drift_class"
        )
        g = TraceGraph(built_at=0.0)
        while res.has_next():
            nid, ntype, name, layer, arn, source, drift = res.get_next()
            nid = str(nid)
            g.nodes[nid] = Node(
                id=nid,
                node_type=str(ntype or "UNKNOWN"),
                label=str(name or nid),
                file_path="",
                metadata={
                    "layer": str(layer or ""), "arn": str(arn or ""),
                    "source": str(source or ""), "drift_class": str(drift or ""),
                },
            )

        res2 = conn.execute(
            "MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) "
            "RETURN a.node_id, b.node_id, e.edge_type"
        )
        while res2.has_next():
            src, tgt, etype = res2.get_next()
            src, tgt = str(src), str(tgt)
            if src in g.nodes and tgt in g.nodes:
                g.edges.append(Edge(source=src, target=tgt, edge_type=str(etype or "UNKNOWN")))
    except KuzuUnavailable:
        raise
    except Exception as ex:  # noqa: BLE001
        raise KuzuUnavailable(
            f"served graph query failed ({type(ex).__name__}: {ex}). comp-blast does not fall back."
        ) from ex

    if not g.nodes:
        raise KuzuUnavailable(
            "the served cloud graph returned ZERO nodes. An empty universe makes every query a "
            "NOT-FOUND, which on this gate reads as 'nothing breaks' -- refusing to serve it."
        )

    served = {
        "vintage": conn.vintage,
        "age_line": conn.age_line,
        "manifest_sha256": conn.manifest_sha256,
        "artifact_prefix": conn.artifact_prefix,
        "nodes": len(g.nodes),
        "edges": len(g.edges),
    }
    prov = ascii_safe(_served_provenance_block(served, len(g.nodes), len(g.edges)))
    if unbudgeted_label:
        prov += ("\n  UNBUDGETED CALL (%s): the served graph costs the same either way; "
                 "no refresh path exists to skip." % unbudgeted_label)
    return g, prov, served


# --------------------------------------------------------------------------- resolution (defect c)
#: Disjoint from the existing contract (0 clean / 1 tool-failed / 2 stale / 3 not-found /
#: 4 phantom-consumer). CVO pinned this value 2026-08-03: an ambiguous subject is NOT a not-found
#: (the nodes exist) and NOT a clean answer (we refused to pick), so it may not overload 3 or 0.
EXIT_AMBIGUOUS_SUBJECT = 5

RESOLVE_EXACT = "EXACT"
RESOLVE_AMBIGUOUS = "AMBIGUOUS"
RESOLVE_NONE = "NONE"


def resolve_subject(g: TraceGraph, query: str) -> tuple[str, list[Node]]:
    """Resolve a query to ONE node, or refuse.

    DEFECT (c) ROOT: `find_node` is a pure SUBSTRING match and `cmd_blast` took `matches[0]`.
    Exercised at HEAD a1cab01483: `comp-blast load_accounts_dim` returned, at rc=0, a full blast
    answer about `gold:B_01.holdings_lots:load_accounts_dimension` -- a DIFFERENT function in a
    DIFFERENT script -- while the exact node `gold:D_00f.advisor_nna_canonical:load_accounts_dim`
    existed and was one of 17 matches. Nothing in the output said a choice had been made.

    THAT IS THE SILENT WRONG-SUBJECT CLASS, and on a change-safety gate it is worse than a crash:
    the operator asked "what breaks if I change A" and got a true answer about B, stamped rc=0.

    Precedence -- specificity first, and every tier that can still be ambiguous SAYS SO:
      1. exact node_id                      (case-sensitive, then case-insensitive)
      2. exact COLON-SUFFIX                 (`gold:A_00.x` -> `pipeline:bd:gold:A_00.x`)
      3. exact last-segment / basename      (`load_accounts_dim` -> `...:load_accounts_dim`)
      4. substring                          (the old behavior) -- ONE hit answers; MANY refuse

    TIER 2 IS AN ID-SHAPE MIGRATION, not a convenience. The private universe addressed a gold script
    as `gold:A_00.accounts_dimension`; kuzu addresses the same script as
    `pipeline:bd:gold:A_00.accounts_dimension`, and kuzu carries ZERO `gold:`-prefixed ids (measured).
    Without this tier every existing call site and every operator's muscle memory silently degrades:
    the old id is still a SUBSTRING of the new one, so it would fall to tier 4 and match the script
    PLUS all ~40 of its function nodes -> AMBIGUOUS. Anchoring on a colon boundary matches the script
    and nothing else, because a function node ends `:<function>`, not `:<script>`.
    """
    if not query:
        return RESOLVE_NONE, []

    q = query.strip()
    ql = q.lower()

    exact = [n for n in g.nodes.values() if n.id == q]
    if len(exact) == 1:
        return RESOLVE_EXACT, exact
    if not exact:
        exact = [n for n in g.nodes.values() if n.id.lower() == ql]
        if len(exact) == 1:
            return RESOLVE_EXACT, exact
    if len(exact) > 1:
        return RESOLVE_AMBIGUOUS, sorted(exact, key=lambda n: n.id)

    suffix = [n for n in g.nodes.values() if n.id.lower().endswith(":" + ql)]
    if len(suffix) == 1:
        return RESOLVE_EXACT, suffix
    if len(suffix) > 1:
        return RESOLVE_AMBIGUOUS, sorted(suffix, key=lambda n: n.id)

    def _segments(node: Node) -> set[str]:
        raw = node.id.replace("\\", "/")
        segs = {raw.rsplit(":", 1)[-1], raw.rsplit("/", 1)[-1]}
        if node.label:
            segs.add(str(node.label))
        return {s.lower() for s in segs if s}

    seg_hits = [n for n in g.nodes.values() if ql in _segments(n)]
    if len(seg_hits) == 1:
        return RESOLVE_EXACT, seg_hits
    if len(seg_hits) > 1:
        return RESOLVE_AMBIGUOUS, sorted(seg_hits, key=lambda n: n.id)

    subs = [n for n in g.nodes.values() if ql in n.id.lower() or ql in str(n.label).lower()]
    if len(subs) == 1:
        return RESOLVE_EXACT, subs
    if len(subs) > 1:
        return RESOLVE_AMBIGUOUS, sorted(subs, key=lambda n: n.id)
    return RESOLVE_NONE, []


# --------------------------------------------------------------------------- worktree overlay
def _git(args: list[str]) -> str:
    try:
        r = subprocess.run(["git", *args], capture_output=True, text=True,
                           cwd=str(_WORKSPACE), timeout=20)
        return r.stdout.strip() if r.returncode == 0 else ""
    except Exception:  # noqa: BLE001
        return ""


def _sha256_of(paths: list[Path]) -> str:
    import hashlib
    h = hashlib.sha256()
    for p in sorted(paths, key=lambda x: str(x)):
        try:
            h.update(p.read_bytes())
        except Exception:  # noqa: BLE001
            h.update(b"<unreadable>")
    return h.hexdigest()[:12]


def subject_files(node: Node, query: str) -> list[Path]:
    """Locate the blasted subject's source file(s) in the CURRENT working tree.

    Kuzu nodes are ARNs and logical ids, not paths, so the overlay has to map back to the tree. A
    subject with no worktree file (an S3 bucket, an IAM role) legitimately has NO overlay -- that is
    reported as scope=none, never as a silent empty overlay.
    """
    cands: list[Path] = []
    stem = node.id.replace("\\", "/").rsplit(":", 1)[-1].rsplit("/", 1)[-1]
    stem = stem.split(".py")[0]
    for raw in {stem, str(node.label or ""), query}:
        raw = str(raw).strip()
        if not raw or "/" in raw or raw.endswith(("/",)):
            continue
        base = raw.split(":")[-1].replace(".py", "")
        if not base:
            continue
        for root in ("data", "infra/aws/lambda", "org/modules/graph", "lib"):
            rp = _WORKSPACE / root
            if not rp.exists():
                continue
            try:
                for hit in rp.rglob(f"{base}.py"):
                    if hit.is_file() and hit not in cands:
                        cands.append(hit)
            except Exception:  # noqa: BLE001
                continue
    # A node whose id IS a path
    for raw in (node.id, query):
        p = _WORKSPACE / str(raw).replace("\\", "/")
        if p.is_file() and p not in cands:
            cands.append(p)
    return cands[:8]


def derive_overlay(node: Node, query: str) -> tuple[list[Edge], dict]:
    """Re-derive the SUBJECT's own edges from the working tree, right now.

    This is the preserved head-pin. It reuses the EXISTING extraction helpers (extract_s3's
    per-file readers) scoped to the subject's file(s) -- seconds, not the 35s whole-tree scan the
    private universe cost.

    Returns (edges, provenance) where provenance carries HEAD, dirty, file count and a content
    digest. The digest is over CONTENT, not mtime: a mutation must change it in the same
    invocation, and a revert must change it back.
    """
    files = subject_files(node, query)
    head = _git(["rev-parse", "--short", "HEAD"]) or "unknown"
    prov = {
        "head": head,
        "dirty": False,
        "files": len(files),
        "digest": "-",
        "scope": "none",
    }
    if not files:
        return [], prov

    rel = [str(p.relative_to(_WORKSPACE)).replace("\\", "/") for p in files]
    porcelain = _git(["status", "--porcelain", "--", *rel])
    prov["dirty"] = bool(porcelain)
    prov["digest"] = _sha256_of(files)
    prov["scope"] = "subject"

    edges: list[Edge] = []
    try:
        from org.modules.graph.extract_s3 import (  # noqa: PLC0415
            _clean_s3_key, _extract_functions_with_s3, _extract_s3_reads, _is_valid_s3_key,
        )
    except Exception:  # noqa: BLE001 -- overlay is additive; never break the kuzu answer
        return edges, prov

    for p in files:
        try:
            content = p.read_text(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            continue
        try:
            writes = _extract_functions_with_s3(content)
            for _fn, keys in (writes or {}).items():
                for key in keys:
                    k = _clean_s3_key(key)
                    if k and _is_valid_s3_key(k):
                        edges.append(Edge(source=node.id, target=f"s3:{k}",
                                          edge_type="WRITES_S3",
                                          metadata={"overlay": "worktree"}))
            for key in (_extract_s3_reads(content) or set()):
                k = _clean_s3_key(key)
                if k and _is_valid_s3_key(k):
                    edges.append(Edge(source=f"s3:{k}", target=node.id,
                                      edge_type="READS_S3",
                                      metadata={"overlay": "worktree"}))
        except Exception:  # noqa: BLE001
            continue

    prov["edges"] = len(edges)
    return edges, prov


def apply_overlay(g: TraceGraph, node: Node, edges: list[Edge]) -> None:
    """Overlay wins on the SUBJECT's own out-edges; kuzu wins on everything else (spec 3.2).

    Only the subject's own edges are replaced -- the overlay re-derived exactly those, so replacing
    anything wider would be asserting worktree authority over estate facts it never looked at.
    """
    if not edges:
        return
    subject_overlay_types = {e.edge_type for e in edges if e.source == node.id}
    if subject_overlay_types:
        g.edges = [e for e in g.edges
                   if not (e.source == node.id and e.edge_type in subject_overlay_types)]
    for e in edges:
        if e.target not in g.nodes:
            g.nodes[e.target] = Node(id=e.target, node_type="S3Key", label=e.target,
                                     metadata={"overlay": "worktree"})
        if e.source not in g.nodes:
            g.nodes[e.source] = Node(id=e.source, node_type="S3Key", label=e.source,
                                     metadata={"overlay": "worktree"})
        g.edges.append(e)
    g._indexed = False


# --------------------------------------------------------------------------- declared territory
#: Edge types that mean "this node PRODUCES the target", as opposed to merely reading or calling it.
#: This is the ROLE half of the producer predicate and it is written down here, once, rather than
#: inferred -- an inferred producer set is the same accident the type allowlist was.
PRODUCER_EDGE_TYPES = (
    "WRITES", "WRITES_S3", "PROJECTS_TO", "TRIGGERS",
    "SFN_INVOKES", "S3_INVOKES", "EVENT_INVOKES", "SNS_INVOKES",
)

#: Node types that are FUNCTION grain in the canonical graph. The retired universe carried a
#: `function_name` field and grain was read off it; kuzu nodes have no such field, so grain is a
#: node_type property here. Declared explicitly because a silently-wrong grain filter would put
#: intra-file structure back at the top of the ranking -- the exact noise the first sweep produced.
FUNCTION_GRAIN_TYPES = ("PipelineFunction", "Hook", "DataFetch")


def declared_producer_territory(g: TraceGraph, selector: str | None = None,
                                grain: str = "script") -> tuple[list, dict]:
    """THE PRODUCER POPULATION, as an explicit filter over the canonical graph.

    CTO arch call 2026-08-04: the old population was `node_type in {LAMBDA, GOLD_SCRIPT,
    GOLD_FUNCTION, SILVER_SCRIPT, S3_ARTIFACT}` evaluated over a private cache -- i.e. THE
    POPULATION WAS DEFINED BY WHATEVER THAT CACHE HAPPENED TO CONTAIN, WHICH IS NOT A DEFINITION AT
    ALL. And a naive re-base to all 20,480 kuzu nodes is equally wrong: that is not the producer
    population either, so it would trade an undefined population for a wrong one. The conforming
    form is Andrew's own second clause -- a TERRITORY-SPECIFIC full graph: an explicit, written,
    inspectable filter over the canonical graph.

    ROLE-BASED, NOT TYPE-BASED (the choice is load-bearing, so it is stated):
    a producer is a node with at least one outbound PRODUCER_EDGE_TYPES edge. Type-based would have
    re-encoded the same accident in new names -- still a list someone chose. Role-based makes
    membership a PROPERTY OF THE GRAPH, self-maintaining as the estate changes, and it matches what
    the metric actually measures (overlap of what two things WRITE).

    THE TRADEOFF, declared rather than hidden: membership now moves when extraction coverage moves.
    That is why the returned definition carries N -- a change in N between runs is a FINDING about
    coverage, not noise to absorb.

    Returns (ids, definition). The definition is emitted in the output per CTO term T1: a score is
    uninterpretable without the population it was computed against.
    """
    if not g.edges:
        return [], {"predicate": "n/a", "n": 0, "error": "universe carries no edges"}

    producers = set()
    for e in g.edges:
        if e.edge_type in PRODUCER_EDGE_TYPES:
            producers.add(e.source)

    ids = []
    for nid in sorted(producers):
        node = g.nodes.get(nid)
        if node is None:
            continue
        if selector and not nid.startswith(selector):
            continue
        is_fn = node.node_type in FUNCTION_GRAIN_TYPES
        if grain == "script" and is_fn:
            continue
        if grain == "function" and not is_fn:
            continue
        ids.append(nid)

    definition = {
        "territory": "PRODUCER (role-derived) over the canonical kuzu graph",
        "predicate": ("node has >=1 outbound edge of type " + "|".join(PRODUCER_EDGE_TYPES)),
        "grain": grain,
        "grain_rule": ("function-grain node_types = " + "|".join(FUNCTION_GRAIN_TYPES)),
        "selector": selector or "(none -- whole territory)",
        "universe_nodes": len(g.nodes),
        "producers_before_filters": len(producers),
        "n": len(ids),
    }
    return ids, definition


def format_population_definition(definition: dict, role: str = "population") -> str:
    """CTO acceptance term T1: emit the DEFINITION, not a name for it.

    A score without its population is not a weak number, it is an uninterpretable one -- the same
    shape as the dual-provenance rule: the reader must be able to see what the answer is an answer
    OVER. So this prints the predicate itself and the resulting N, never a label like "producers".
    """
    lines = [f"=== DECLARED TERRITORY ({role}) ==="]
    lines.append(f"  territory:  {definition.get('territory', '?')}")
    lines.append(f"  predicate:  {definition.get('predicate', '?')}")
    lines.append(f"  grain:      {definition.get('grain', '?')}  ({definition.get('grain_rule', '')})")
    lines.append(f"  selector:   {definition.get('selector', '?')}")
    lines.append(f"  N:          {definition.get('n', 0)} node(s) "
                 f"(from {definition.get('producers_before_filters', 0)} role-matched "
                 f"of {definition.get('universe_nodes', 0)} in the universe)")
    lines.append("  NOT COMPARABLE ACROSS DEFINITIONS: a score computed over a different population "
                 "is a different")
    lines.append("  statistic wearing the same name. Do not trend these against scores from another "
                 "predicate or N.")
    lines.append("=" * 34)
    return ascii_safe("\n".join(lines))


def format_dual_provenance(kuzu_block: str, overlay: dict) -> str:
    """BOTH vintages, ALWAYS (spec 3.3). A single-vintage answer is a P3 conformance failure.

    The kuzu block passes through as-is (it is comp-kuzu's own, already reviewed); the overlay adds
    exactly one line. Two universes answered this question and the reader is entitled to know the
    vintage of each.
    """
    lines = [kuzu_block.rstrip()]
    lines.append(
        "=== comp-blast worktree overlay ===\n"
        f"  HEAD: {overlay.get('head', 'unknown')}  "
        f"dirty: {'yes' if overlay.get('dirty') else 'no'}  "
        f"subject-files: {overlay.get('files', 0)}  "
        f"content-digest: {overlay.get('digest', '-')}  "
        f"scope: {overlay.get('scope', 'none')}"
        + (f"  overlay-edges: {overlay['edges']}" if overlay.get("edges") else "")
    )
    if overlay.get("scope") == "none":
        lines.append(
            "  (no worktree file maps to this subject -- estate-only answer, kuzu vintage governs)"
        )
    lines.append("=" * 28)
    return ascii_safe("\n".join(lines))
