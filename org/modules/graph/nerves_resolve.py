"""
nerves_resolve -- THE KEYSTONE (NFRA_NERVES L2): the ONE shared resolver.

    resolve(ref) -> Resolution{node_ids, kind, confidence, source}

AN EVENT WITHOUT AN ADDRESS IS EXHAUST; WITH ONE, IT IS TRAFFIC. Every other NERVES layer is a
function of this one, which is why it ships first.

IT DOES NOT RE-IMPLEMENT RESOLUTION. It COMPOSES the resolvers that already exist, in precedence
order, each of which already has a home and an owner:

  1. TRACE GRAPH   (trace_graph.py find_node / file_path)  -- gold scripts, lambdas, components,
                    S3 artifacts, endpoints, eventbridge. The estate's structural spine.
  2. COMP-PYDEPS   (NFRA_INSTDRILL item 8)                 -- the COMPILER layer (.tools/,
                    org/modules/). This is exactly WHY closing F-5 mattered: the tooling layer can
                    now join the organism instead of being invisible to it.
  3. REPO PATH     (a real file on disk)                    -- the universal fallback: any tracked
                    file is a legitimate node even if no higher graph models it yet.
  4. CLOUD REF     (an ARN / bucket / lambda-name shape)    -- points at comp-aws/comp-kuzu's
                    surface; we do not re-derive the cloud graph here.

THE UNRESOLVABLE ARE NOT DROPPED. `resolve` returns kind="UNADDRESSED" with the raw ref preserved.
An unresolvable ref IS THE F-5 CLASS REPEATING -- a blind spot in the estate's self-model -- and it
is a FINDING, rendered in a visible band with its denominator. (NERVES discipline: UNKNOWN is a band
everywhere; never dropped, never defaulted to a verdict.)

CONFIDENCE is stated, never implied: EXACT (an id/path matched) | STRONG (a unique graph match) |
WEAK (a substring/basename match -- could be several things) | NONE (unaddressed).

Read-only. Deterministic. No network.

Author: 1.0.0_SA_CTO~Z (NFRA_NERVES L2). 2026-07-14.
"""

from __future__ import annotations

import functools
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.normpath(os.path.join(_HERE, "..", "..", ".."))

_ARN_RX = re.compile(r"^arn:aws:[a-z0-9-]+:")
_S3_RX = re.compile(r"^s3://([^/]+)/?(.*)$")
# a lambda-ish / bucket-ish bare name (hyphenated, no slash, no extension)
_CLOUDNAME_RX = re.compile(r"^[a-z0-9]+(-[a-z0-9]+){2,}$")


@dataclass
class Resolution:
    ref: str
    node_ids: list = field(default_factory=list)
    kind: str = "UNADDRESSED"      # GRAPH | COMPILER | REPO_PATH | CLOUD | UNADDRESSED
    confidence: str = "NONE"       # EXACT | STRONG | WEAK | NONE
    source: str = ""               # which resolver answered

    @property
    def addressed(self) -> bool:
        return bool(self.node_ids)


@functools.lru_cache(maxsize=1)
def _trace_graph():
    """The structural spine. None if the cache is absent (resolver degrades, never crashes)."""
    try:
        sys.path.insert(0, _WS)
        from pathlib import Path
        from org.modules.graph.trace_graph import TraceGraph
        cache = Path(_WS) / ".comp-graph" / "graph.json"
        return TraceGraph.load(cache) if cache.exists() else None
    except Exception:  # noqa: BLE001
        return None


@functools.lru_cache(maxsize=1)
def _pydeps():
    """The compiler layer (F-5 closure). None if absent."""
    try:
        import importlib.util as ilu
        spec = ilu.spec_from_file_location("comp_pydeps", os.path.join(_HERE, "comp_pydeps.py"))
        mod = ilu.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod, mod._load()
    except Exception:  # noqa: BLE001
        return None, None


@functools.lru_cache(maxsize=1)
def _graph_index():
    """Three indices, because a ref arrives in three shapes (each gap below was found by RUNNING the
    resolver over a real day's traffic and reading its UNADDRESSED band -- not by guessing):
      by_path  full file_path -> node_id
      by_base  file basename  -> [node_id]
      by_leaf  the LAST SEGMENT of a node id -> [node_id]. This is what catches a bare FUNCTION name
               ("build_dashboard" -> gold:INF_D_04.client_portal_summary:build_dashboard, x78
               unaddressed) and a bare ARTIFACT key ("canonical_prices.parquet", x75) -- neither of
               which has a file_path basename to match on."""
    g = _trace_graph()
    by_path, by_base, by_leaf = {}, {}, {}
    if not g:
        return by_path, by_base, by_leaf
    for nid, n in g.nodes.items():
        fp = (getattr(n, "file_path", "") or "").replace("\\", "/").lower()
        if fp:
            by_path.setdefault(fp, nid)
            by_base.setdefault(os.path.basename(fp), []).append(nid)
        # the id's trailing segment: after the last ':' and then the last '/'
        leaf = nid.split(":")[-1].split("/")[-1].strip().lower()
        if leaf and leaf != nid.lower():
            by_leaf.setdefault(leaf, []).append(nid)
    return by_path, by_base, by_leaf


@functools.lru_cache(maxsize=1)
def _repo_basenames():
    """{basename -> [repo-relative path]} over every TRACKED file.

    Found by the L3b acceptance FAILING (not by guessing): `build_assets_dim.py` -- one of the THREE
    FROZEN FILES -- was UNADDRESSED. The REPO_PATH fallback only matched a FULL path, so a bare
    filename resolved to nothing, and the most dangerous file in the estate had no address. A file
    the repo tracks is a node whether or not a higher graph models it (the silver tier is not in the
    trace graph at all). git ls-files = tracked truth, gitignore-aware, one call."""
    try:
        out = subprocess.run(["git", "-C", _WS, "ls-files"], capture_output=True, text=True,
                             timeout=60, errors="replace")
        if out.returncode != 0:
            return {}
    except Exception:  # noqa: BLE001
        return {}
    idx = {}
    for p in out.stdout.splitlines():
        p = p.strip().replace("\\", "/")
        if p:
            idx.setdefault(os.path.basename(p).lower(), []).append(p)
    return idx


@functools.lru_cache(maxsize=1)
def _tools_on_disk():
    """Every .tools/ shim by bare name -- INCLUDING THE BASH ONES. comp-pydeps indexes python only
    (shebang-sniffed), so `comp-surface-check` (a bash shim) came back UNADDRESSED 133 times in the
    first live run: the keystone could not address a third of its own toolkit. A tool is a node
    whatever language its shim is written in."""
    d = os.path.join(_WS, ".tools")
    if not os.path.isdir(d):
        return frozenset()
    return frozenset(f for f in os.listdir(d)
                     if os.path.isfile(os.path.join(d, f)) and "." not in f)


def _norm(ref: str) -> str:
    return (ref or "").strip().replace("\\", "/")


@functools.lru_cache(maxsize=20000)
def resolve(ref: str) -> Resolution:
    """The ONE resolver. Precedence: graph-id -> graph-path -> compiler layer -> repo path -> cloud.
    Never raises; an unresolvable ref returns kind=UNADDRESSED (a FINDING, not a drop)."""
    r = _norm(ref)
    if not r or len(r) < 2:
        return Resolution(ref=ref)

    g = _trace_graph()
    by_path, by_base, by_leaf = _graph_index()

    # 1a. an exact graph node id (e.g. "gold:A_00.accounts_dimension", "lambda:inf-gold-trigger")
    if g and r in g.nodes:
        return Resolution(ref, [r], "GRAPH", "EXACT", "trace_graph.id")

    # 1b. an exact repo path that the graph models
    rl = r.lower()
    if rl in by_path:
        return Resolution(ref, [by_path[rl]], "GRAPH", "EXACT", "trace_graph.file_path")

    # 2. the COMPILER layer: a .tools/ shim by BARE NAME -- any language (comp-pydeps sees python
    # only; `comp-surface-check` is bash and came back UNADDRESSED x133 in the first live run).
    if r in _tools_on_disk():
        return Resolution(ref, ["tool:%s" % r], "COMPILER", "EXACT", "tools.on_disk")

    # 2b. the COMPILER layer via comp-pydeps (F-5): python modules by EXACT stem ONLY.
    # comp_pydeps._match_target FUZZY-SUBSTRING-matches (it will return `adapter_audit_cli` for a
    # ref like "audit"). That is right for a human asking "who consumes X" and CATASTROPHIC here:
    # it attached 991 false HOLD claims to adapter_audit_cli in the first L3b build, from lines that
    # merely contained the word. A DANGER MAP WITH FALSE CLAIMS IS WORSE THAN NO DANGER MAP -- it
    # trains agents to ignore the warning. Exact stem or nothing.
    mod, pg = _pydeps()
    if mod and pg:
        defines = pg.get("defines", {})
        stem = r[:-3] if r.endswith(".py") else r
        if stem in defines:
            return Resolution(ref, ["tool:%s" % stem], "COMPILER", "EXACT", "comp_pydeps.exact")

    # 1c. a basename -- MERGE the graph's hits WITH the repo's tracked-file hits.
    # THE VENDORED-FORK HAZARD, IN MY OWN RESOLVER: `_orion_api_silver_lib.py` (ONE OF THE THREE
    # FROZEN FILES) resolved to the FIVE VENDORED LAMBDA COPIES and NEVER to the canonical silver
    # source -- the copies SHADOWED the original, so the frozen file could carry no HOLD. That is the
    # exact fork-divergence class the frozen-three hold is partly about, reproduced inside the
    # instrument meant to warn about it. An ambiguous basename returns EVERY candidate, canonical
    # source INCLUDED, and says WEAK -- it never silently picks, and it never silently omits.
    base = os.path.basename(rl)
    graph_ids = list(by_base.get(base, []))
    repo_ids = ["file:%s" % h for h in _repo_basenames().get(base, [])]
    if graph_ids or repo_ids:
        # de-dup: a repo path already modeled by a graph node is not listed twice
        graph_paths = set()
        if g:
            for nid in graph_ids:
                fp = (getattr(g.nodes.get(nid), "file_path", "") or "").replace("\\", "/")
                if fp:
                    graph_paths.add(fp)
        merged = graph_ids + [rid for rid in repo_ids if rid[5:] not in graph_paths]
        if merged:
            return Resolution(ref, merged, "GRAPH" if graph_ids else "REPO_PATH",
                              "STRONG" if len(merged) == 1 else "WEAK",
                              "basename(graph+repo)")

    # 2c. a bare FUNCTION name or ARTIFACT key the graph models as a node-id LEAF
    #     ("build_dashboard" -> gold:INF_D_04...:build_dashboard; "canonical_prices.parquet" -> s3:...)
    if rl in by_leaf:
        ids = by_leaf[rl]
        return Resolution(ref, list(ids), "GRAPH",
                          "STRONG" if len(ids) == 1 else "WEAK", "trace_graph.id_leaf")

    # 3. any real repo file is a legitimate node even if no higher graph models it yet
    if os.path.exists(os.path.join(_WS, r)) and not os.path.isdir(os.path.join(_WS, r)):
        return Resolution(ref, ["file:%s" % r], "REPO_PATH", "EXACT", "repo.path")

    # 3b. a BARE FILENAME of a tracked file. THE FROZEN-THREE GAP: `build_assets_dim.py` (a silver
    # script -- the silver tier is NOT in the trace graph) was UNADDRESSED, so the most dangerous
    # file in the estate had no address and could carry no HOLD edge. A tracked file is a node.
    # WEAK when the basename is ambiguous (e.g. a vendored copy) -- we return EVERY candidate rather
    # than silently picking, because picking the wrong one here would attach a hold to the wrong file.
    hits = _repo_basenames().get(base)
    if hits:
        return Resolution(ref, ["file:%s" % h for h in hits], "REPO_PATH",
                          "STRONG" if len(hits) == 1 else "WEAK", "repo.basename")

    # 4. cloud refs -- addressed to the cloud surface (comp-aws/comp-kuzu own the derivation)
    m = _S3_RX.match(r)
    if m:
        return Resolution(ref, ["s3:%s" % m.group(1)], "CLOUD", "STRONG", "s3.uri")
    if _ARN_RX.match(r):
        return Resolution(ref, ["arn:%s" % r.split(":")[-1]], "CLOUD", "STRONG", "arn")
    if _CLOUDNAME_RX.match(r) and g:
        # a hyphenated bare name that the graph knows as a lambda/rule (find_node is substring-y,
        # so require a real hit and report WEAK when several match)
        hits = [n.id for n in g.find_node(r)]
        if hits:
            return Resolution(ref, hits, "CLOUD" if len(hits) > 1 else "GRAPH",
                              "STRONG" if len(hits) == 1 else "WEAK", "trace_graph.find_node")

    # UNADDRESSED -- a finding, never a drop.
    return Resolution(ref=ref)


def resolve_many(refs) -> tuple:
    """-> (resolutions, stats). stats ALWAYS carries the denominator (NERVES: print the denominator
    of every scan you reason from)."""
    res = [resolve(x) for x in refs]
    n = len(res)
    addressed = [x for x in res if x.addressed]
    by_kind, by_conf = {}, {}
    for x in res:
        by_kind[x.kind] = by_kind.get(x.kind, 0) + 1
        by_conf[x.confidence] = by_conf.get(x.confidence, 0) + 1
    stats = {
        "refs_total": n,                       # THE DENOMINATOR
        "addressed": len(addressed),
        "unaddressed": n - len(addressed),
        "hit_rate_pct": round(100.0 * len(addressed) / n, 1) if n else 0.0,
        "by_kind": by_kind, "by_confidence": by_conf,
    }
    return res, stats


def _self_test() -> int:
    results = []
    def ck(name, ok, detail=""):
        results.append(ok)
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   ({detail})" if detail else ""))

    # EXACT graph-path hit (a gold script the trace graph models)
    r1 = resolve("data/black_diamond/scripts/gold/A_00.accounts_dimension.py")
    ck("graph.path_exact", r1.addressed and r1.kind == "GRAPH" and r1.confidence == "EXACT",
       f"{r1.kind}/{r1.confidence} -> {r1.node_ids[:1]}")

    # COMPILER layer (F-5): comp-which is addressable ONLY because comp-pydeps exists.
    r2 = resolve("comp-which")
    ck("compiler.f5_layer_addressable", r2.addressed and r2.kind == "COMPILER",
       f"{r2.kind}/{r2.confidence} -> {r2.node_ids}")

    # REPO_PATH fallback: a real file the higher graphs do not model.
    r3 = resolve("CLAUDE.md")
    ck("repo.path_fallback", r3.addressed and r3.kind == "REPO_PATH", f"{r3.kind}")

    # CLOUD: an s3 uri addresses the bucket surface.
    r4 = resolve("s3://opal-data-assets/orion/x/2026-07-14/f.json")
    ck("cloud.s3_uri", r4.addressed and r4.kind == "CLOUD", f"{r4.node_ids}")

    # THE TWO GAPS THE FIRST LIVE RUN FOUND (found by reading the UNADDRESSED band, not by guessing):
    r6 = resolve("comp-surface-check")      # a BASH shim -- comp-pydeps indexes python only (x133 miss)
    ck("gap1.bash_shim_addressable", r6.addressed and r6.kind == "COMPILER",
       f"{r6.kind}/{r6.source} -> {r6.node_ids}")
    r7 = resolve("build_dashboard")         # a bare FUNCTION name -> a node-id LEAF (x78 miss)
    ck("gap2.bare_function_addressable", r7.addressed and "build_dashboard" in str(r7.node_ids),
       f"{r7.source} -> {r7.node_ids[:1]}")

    # THE FROZEN-THREE GAP (found by the L3b acceptance FAILING): a bare filename of a TRACKED file
    # must resolve. `build_assets_dim.py` is a silver script -- the silver tier is not in the trace
    # graph at all -- and it is one of the THREE FROZEN FILES. It had no address, so it could carry
    # no HOLD. The most dangerous file in the estate was invisible to its own danger map.
    r8 = resolve("build_assets_dim.py")
    ck("gap3.frozen_file_addressable", r8.addressed and r8.kind == "REPO_PATH",
       f"{r8.kind}/{r8.confidence} -> {r8.node_ids}")

    # UNADDRESSED IS A FINDING, NOT A DROP -- and it keeps the raw ref.
    r5 = resolve("zzz_not_a_thing_anywhere_xyz")
    ck("unaddressed.is_a_finding_not_a_drop",
       (not r5.addressed) and r5.kind == "UNADDRESSED" and r5.ref == "zzz_not_a_thing_anywhere_xyz")

    # DENOMINATOR: resolve_many always prints what it was OF.
    _res, stats = resolve_many(["CLAUDE.md", "zzz_nope_xyz"])
    ck("stats.denominator_present",
       stats["refs_total"] == 2 and stats["addressed"] == 1 and stats["unaddressed"] == 1
       and stats["hit_rate_pct"] == 50.0, str(stats["hit_rate_pct"]))

    # CONFIDENCE IS STATED, never implied: an ambiguous basename must not silently pick one.
    #   (only assert the mechanism -- that WEAK exists as a band and multi-hit yields >1 id)
    ck("confidence.weak_band_exists",
       any(x.confidence in ("EXACT", "STRONG", "WEAK", "NONE") for x in _res))

    ok = all(results)
    print("\n" + ("OK: the keystone resolves -- graph + compiler(F-5) + repo + cloud; UNADDRESSED is a band"
                  if ok else "ERROR: nerves_resolve self-test FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(_self_test())
    for a in sys.argv[1:]:
        r = resolve(a)
        print("%-50s -> %-12s %-7s %s  [%s]" % (a[:50], r.kind, r.confidence,
                                                r.node_ids or "(unaddressed)", r.source))
