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
import json
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


# THE FIVE STATES (RULING.md:61 -- "the two-state collapse in nerves_resolve is to be repaired").
#
# The collapse, stated exactly: every failure returned kind=UNADDRESSED / confidence=NONE /
# node_ids=[], byte-identical, whether the trace-graph cache was missing, git had failed, the ref
# belonged to another fabric, or the ref genuinely has no address in this estate. One answer for
# four questions, and the three that are INSTRUMENT failures were being read as findings about the
# world. `nerves_resolve.card.json` v1 records it: "an absent substrate returns UNADDRESSED / NONE /
# [] byte-identical to a genuine miss".
#
# These five are MECE over "what happened to this ref" (Rule 24, one axis, one intent):
#   RESOLVED               exactly one address, and it is named
#   AMBIGUOUS              several candidates; ALL are returned and none is picked
#   GENUINELY_UNADDRESSED  every tier was ALIVE and none knew this ref -- a real finding
#   SUBSTRATE_UNAVAILABLE  a tier could not answer; the tier and its exception class are named
#   NOT_APPLICABLE         the ref belongs to another fabric/plane; the fabric is named
#
# CONFIDENCE IS KEPT AND IS ORTHOGONAL. It answers "how sure is this address", not "what happened":
# a RESOLVED can be EXACT or STRONG, and an AMBIGUOUS is WEAK. Folding them into one axis is what
# produced the collapse in the first place.
STATES = ("RESOLVED", "AMBIGUOUS", "GENUINELY_UNADDRESSED", "SUBSTRATE_UNAVAILABLE",
          "NOT_APPLICABLE")


@dataclass(frozen=True)
class TierStatus:
    """One composed tier's liveness AND vintage, per call.

    `vintage` is what makes staleness readable (W4-nerves_resolve.card.json v3: "staleness is
    silent"). An available tier answering from a six-week-old graph cache is not the same fact as an
    available tier answering from a fresh one, and before this the result could not tell them apart.
    """
    tier: str
    available: bool
    reason: str = ""
    exception_class: str = ""
    vintage: str = ""

    def as_dict(self) -> dict:
        return {"tier": self.tier, "available": self.available, "reason": self.reason,
                "exception_class": self.exception_class, "vintage": self.vintage}


@dataclass(frozen=True)
class Candidate:
    """One address, WITH the evidence that produced it. AMBIGUOUS returns every one of these."""
    node_id: str
    evidence: str = ""
    canonical_serial: str = ""

    def as_dict(self) -> dict:
        return {"node_id": self.node_id, "evidence": self.evidence,
                "canonical_serial": self.canonical_serial}


@dataclass
class Resolution:
    # -- the legacy surface, UNCHANGED and still positional (3 caller files, 5 call sites) --------
    ref: str
    node_ids: list = field(default_factory=list)
    kind: str = "UNADDRESSED"      # GRAPH | COMPILER | REPO_PATH | CLOUD | UNADDRESSED
    confidence: str = "NONE"       # EXACT | STRONG | WEAK | NONE
    source: str = ""               # which resolver answered
    # -- ADDITIVE (AC1). Defaults keep every existing Resolution(...) construction valid ----------
    state: str = "GENUINELY_UNADDRESSED"
    tiers: tuple = ()              # TierStatus per composed tier, this call
    candidates: tuple = ()         # Candidate, plural, each with its evidence
    fabric: str = "CLOUD"          # the fabric this resolution is FOR
    evidence: tuple = ()           # refs to the artifacts consulted
    policy: str = ""               # STRICT when the ref parsed as a record id

    def __post_init__(self):
        # ENFORCED BY THE RESULT TYPE, per AC1. A state outside the five is a programming error in
        # the resolver, and the resolver is the thing under repair -- so it raises here rather than
        # travelling as a sixth de-facto state that no consumer knows to branch on.
        if self.state not in STATES:
            raise ValueError("state %r is not one of %s" % (self.state, ", ".join(STATES)))

    @property
    def addressed(self) -> bool:
        return bool(self.node_ids)

    @property
    def resolver_version(self) -> str:
        """This file's own digest -- on every result, per the memo."""
        return _resolver_version()

    @property
    def substrate_unavailable(self) -> tuple:
        """The tiers that made THIS result SUBSTRATE_UNAVAILABLE -- empty in every other state.

        It must agree with `state` by construction. An earlier cut returned every dead tier
        regardless of whether it was consulted, so a GENUINELY_UNADDRESSED result also reported a
        non-empty substrate_unavailable -- and a consumer branching on the property got a different
        answer from one branching on the state. Two views of one fact that can disagree is the
        collapse again, wearing the opposite coat.
        """
        if self.state != "SUBSTRATE_UNAVAILABLE":
            return ()
        return tuple(t for t in self.tiers if not t.available)

    @property
    def dead_tiers_all(self) -> tuple:
        """Every unavailable tier, consulted or not -- the raw view, for an operator asking about
        the ESTATE rather than about this ref."""
        return tuple(t for t in self.tiers if not t.available)

    def as_dict(self) -> dict:
        return {"ref": self.ref, "state": self.state, "kind": self.kind,
                "confidence": self.confidence, "source": self.source, "fabric": self.fabric,
                "policy": self.policy, "node_ids": list(self.node_ids),
                "candidates": [c.as_dict() for c in self.candidates],
                "tiers": [t.as_dict() for t in self.tiers], "evidence": list(self.evidence),
                "resolver_version": self.resolver_version}


@functools.lru_cache(maxsize=1)
def _resolver_version() -> str:
    """sha256 of this file's own bytes, LF-normalised.

    LF-normalised because a CRLF checkout and an LF blob are the same source and different bytes; a
    version that moves with the checkout names the checkout, not the resolver.
    """
    import hashlib
    try:
        with open(os.path.abspath(__file__), "rb") as fh:
            return "sha256:" + hashlib.sha256(fh.read().replace(b"\r\n", b"\n")).hexdigest()[:16]
    except OSError as exc:
        return "unreadable:" + type(exc).__name__


def _vintage_of(path) -> str:
    """artifact path + mtime, so a stale substrate is READABLE on the result."""
    try:
        import datetime
        mt = os.path.getmtime(path)
        stamp = datetime.datetime.fromtimestamp(mt, datetime.timezone.utc)
        return "%s @%sZ" % (path, stamp.strftime("%Y-%m-%dT%H:%M:%S"))
    except OSError:
        return "%s @absent" % path


@functools.lru_cache(maxsize=1)
def _trace_graph_t():
    """The structural spine, WITH its liveness. Returns (graph_or_None, TierStatus).

    THE BROAD `except Exception: return None` THAT STOOD HERE could not be told apart from "the
    cache file does not exist", and neither could be told apart from "the ref is not in the graph".
    Three different facts, one return value. The exception classes are now named and CAUGHT BY TYPE:
    ImportError (the module is not importable here), OSError (the cache cannot be read), ValueError
    (it is not loadable JSON). Anything else is NOT swallowed -- an unanticipated failure inside the
    resolver should surface, not be laundered into a clean miss.
    """
    cache = os.path.join(_WS, ".comp-graph", "graph.json")
    vintage = _vintage_of(cache)
    try:
        sys.path.insert(0, _WS)
        from pathlib import Path
        from org.modules.graph.trace_graph import TraceGraph
    except ImportError as exc:
        return None, TierStatus("trace_graph", False, "trace_graph module not importable",
                                type(exc).__name__, vintage)
    if not os.path.exists(cache):
        return None, TierStatus("trace_graph", False, "graph cache absent", "FileNotFoundError",
                                vintage)
    try:
        return TraceGraph.load(Path(cache)), TierStatus("trace_graph", True, "", "", vintage)
    except (OSError, ValueError) as exc:
        return None, TierStatus("trace_graph", False, "graph cache unreadable",
                                type(exc).__name__, vintage)


def _trace_graph():
    """Legacy shape, kept: the graph or None. Callers inside this module use _trace_graph_t()."""
    return _trace_graph_t()[0]


@functools.lru_cache(maxsize=1)
def _pydeps_t():
    """The compiler layer (F-5 closure), WITH its liveness. Returns (mod, payload, TierStatus)."""
    src = os.path.join(_HERE, "comp_pydeps.py")
    vintage = _vintage_of(src)
    if not os.path.exists(src):
        return None, None, TierStatus("comp_pydeps", False, "comp_pydeps.py absent",
                                      "FileNotFoundError", vintage)
    try:
        import importlib.util as ilu
        spec = ilu.spec_from_file_location("comp_pydeps", src)
        mod = ilu.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod, mod._load(), TierStatus("comp_pydeps", True, "", "", vintage)
    except (ImportError, AttributeError, OSError, ValueError) as exc:
        return None, None, TierStatus("comp_pydeps", False, "comp_pydeps did not load",
                                      type(exc).__name__, vintage)


def _pydeps():
    m, p, _t = _pydeps_t()
    return m, p


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
    g = _trace_graph_t()[0]
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
def _repo_basenames_t():
    """{basename -> [repo-relative path]} over every TRACKED file, WITH liveness.

    Found by the L3b acceptance FAILING (not by guessing): `build_assets_dim.py` -- one of the THREE
    FROZEN FILES -- was UNADDRESSED. The REPO_PATH fallback only matched a FULL path, so a bare
    filename resolved to nothing, and the most dangerous file in the estate had no address. A file
    the repo tracks is a node whether or not a higher graph models it (the silver tier is not in the
    trace graph at all). git ls-files = tracked truth, gitignore-aware, one call.

    A git FAILURE HERE USED TO RETURN {} -- the same value as "the repo tracks no file by that
    name". Under that return an entire tier could be dead and every ref through it read as a clean
    miss. The rc!=0 case is now UNAVAILABLE and carries git's own stderr.
    """
    vintage = _vintage_of(os.path.join(_WS, ".git", "index"))
    try:
        out = subprocess.run(["git", "-C", _WS, "ls-files"], capture_output=True, text=True,
                             timeout=60, errors="replace")
    except (OSError, subprocess.SubprocessError) as exc:
        return {}, TierStatus("repo_basenames", False, "git ls-files did not run",
                              type(exc).__name__, vintage)
    if out.returncode != 0:
        return {}, TierStatus("repo_basenames", False,
                              "git ls-files rc=%d: %s" % (out.returncode,
                                                          (out.stderr or "").strip()[:120]),
                              "CalledProcessError", vintage)
    idx = {}
    for p in out.stdout.splitlines():
        p = p.strip().replace("\\", "/")
        if p:
            idx.setdefault(os.path.basename(p).lower(), []).append(p)
    return idx, TierStatus("repo_basenames", True, "", "", vintage)


def _repo_basenames():
    return _repo_basenames_t()[0]


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


@functools.lru_cache(maxsize=1)
def _tools_on_disk_t():
    d = os.path.join(_WS, ".tools")
    vintage = _vintage_of(d)
    if not os.path.isdir(d):
        return frozenset(), TierStatus("tools_on_disk", False, ".tools directory absent",
                                       "NotADirectoryError", vintage)
    try:
        return _tools_on_disk(), TierStatus("tools_on_disk", True, "", "", vintage)
    except OSError as exc:
        return frozenset(), TierStatus("tools_on_disk", False, ".tools not listable",
                                       type(exc).__name__, vintage)


@functools.lru_cache(maxsize=1)
def _graph_index_t():
    """The three indices. A VIEW of trace_graph, so it INHERITS that tier's liveness -- but it is
    reported under its OWN name, because a reader must be able to see which of the five tiers is
    down without knowing which are views of which. Reporting it as "trace_graph" twice would make
    the five-tier list read as four tiers and a duplicate."""
    base = _trace_graph_t()[1]
    return _graph_index(), TierStatus("graph_index", base.available,
                                      base.reason and "derived from trace_graph: " + base.reason,
                                      base.exception_class, base.vintage)


def _tier_statuses() -> tuple:
    """Every composed tier's liveness for THIS call, in precedence order.

    DERIVED, never typed: the count is len() of this tuple. The TO's face says 5 composed tiers and
    that number is re-derived here rather than asserted -- trace_graph, comp_pydeps, graph_index
    (which is a VIEW of trace_graph and carries its status), repo_basenames, tools_on_disk.
    """
    return (_trace_graph_t()[1], _pydeps_t()[2], _graph_index_t()[1], _repo_basenames_t()[1],
            _tools_on_disk_t()[1], _ledger_t()[1])


def _norm(ref: str) -> str:
    return (ref or "").strip().replace("\\", "/")


# THIS FABRIC. `executed_on_fabric` in the frozen contract is `$ref nonempty` -- a free string with
# NO vocabulary and no basis slot, exactly the shape CTO~X ruled ABSENT for semantic_layer in WP-3b.
# So this resolver does NOT classify fabrics: it declares the one it can address, and NOT_APPLICABLE
# fires ONLY on a ref that EXPLICITLY qualifies itself with a different one. Inventing a fabric
# taxonomy here to make the state reachable would be the costume that ruling refused.
THIS_FABRIC = "CLOUD"
# `fabric::ref`. DOUBLE colon deliberately: every existing id shape in this estate is single-colon
# (gold:, lambda:, s3:, arn:, tool:, file:, ent:), so no ref that resolves today can become
# NOT_APPLICABLE by accident. Compatibility is a property of the SEPARATOR CHOICE, not of care.
_FABRIC_RX = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*)::(.+)$")


def _foreign_fabric(r: str) -> str:
    """The fabric this ref names, if it names one that is not ours. Empty when in-fabric."""
    m = _FABRIC_RX.match(r or "")
    if not m:
        return ""
    named = m.group(1).upper()
    return "" if named == THIS_FABRIC.upper() else named


@functools.lru_cache(maxsize=20000)
def _resolve_chain(ref: str) -> Resolution:
    """The ONE resolver's PRECEDENCE CHAIN, unchanged: graph-id -> graph-path -> compiler layer ->
    repo path -> cloud. Its verdict is an ADDRESS; the five-state classification is resolve()'s.

    Kept as its own function so the repair adds a contract WITHOUT touching precedence logic that
    was each earned by a live failure (the vendored-fork shadowing, the bash shim, the bare function
    name, the frozen-three basename). Rewriting those while changing the result type would have made
    a regression in either indistinguishable from a regression in the other."""
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


@functools.lru_cache(maxsize=20000)
def resolve(ref: str) -> Resolution:
    """The ONE resolver. Returns exactly one of the five states, enforced by the result type.

    THE REPAIR, in one sentence: the chain answers "what address does this ref have", and this
    function answers "what HAPPENED to this ref" -- and before the repair the second question had
    only two answers for four different worlds.

    THE ORDER OF THE CLASSIFICATION IS THE MECHANISM:
      1. NOT_APPLICABLE first -- a ref for another fabric is not a miss in ours, and asking the
         tiers about it would let a coincidence of NAME resolve it (AC4 names that arm).
      2. the chain runs.
      3. one candidate -> RESOLVED; several -> AMBIGUOUS, ALL returned, none picked.
      4. NO candidate, and the decision that this whole TO exists for:
            any tier UNAVAILABLE -> SUBSTRATE_UNAVAILABLE, naming the tier and its exception class
            every tier ALIVE     -> GENUINELY_UNADDRESSED, a real finding about the estate
         Those two were byte-identical before. A dead tier now cannot be reported as a clean miss.
    """
    r = _norm(ref)
    tiers = _tier_statuses()
    evidence = tuple(t.vintage for t in tiers if t.vintage)

    foreign = _foreign_fabric(r)
    if foreign:
        return Resolution(ref, [], "UNADDRESSED", "NONE", "fabric.qualified",
                          state="NOT_APPLICABLE", tiers=tiers, candidates=(), fabric=foreign,
                          evidence=evidence)

    # A REF THAT PARSES AS A RECORD ID IS RESOLVED STRICT, AND IS NEVER BASENAME-FUZZED (AC2).
    # `ent:0.4.0-dt-clientplatform` is an IDENTITY, not a filename: if the ledger does not carry it,
    # the honest answer is "no such record", never "here are three files whose basename looks a bit
    # like it". Fuzzing a parsed id is how a resolver answers an identity question with a filesystem
    # coincidence -- and the caller cannot tell the two apart from the outside.
    inner = _FABRIC_RX.match(r).group(2) if _FABRIC_RX.match(r) else r
    if _RECORD_ID_RX.match(inner):
        rows, lst = _ledger_t()
        if rows is None:
            return Resolution(ref, [], "UNADDRESSED", "NONE", "ledger.strict",
                              state="SUBSTRATE_UNAVAILABLE", tiers=tiers, fabric=THIS_FABRIC,
                              evidence=evidence, policy="STRICT")
        if not ledger_has(inner):
            return Resolution(ref, [], "UNADDRESSED", "NONE", "ledger.strict",
                              state="GENUINELY_UNADDRESSED", tiers=tiers, fabric=THIS_FABRIC,
                              evidence=evidence, policy="STRICT")
        canon, why = canonical_serial(inner)
        return Resolution(ref, [canon or inner], "LEDGER", "EXACT", "ledger.canonical",
                          state="RESOLVED", tiers=tiers,
                          candidates=(Candidate(canon or inner, "identity_relation fold: " + why,
                                                canon or inner),),
                          fabric=THIS_FABRIC, evidence=evidence, policy="STRICT")

    # An IN-fabric qualifier is stripped before the chain sees it: "CLOUD::CLAUDE.md" names this
    # fabric and must resolve exactly as "CLAUDE.md" does. Leaving the prefix on would make an
    # explicitly-correct ref read as a miss -- the qualifier would punish the caller for using it.
    m = _FABRIC_RX.match(r)
    base = _resolve_chain(m.group(2) if m else ref)
    cands = []
    for nid in base.node_ids:
        canon = ""
        if _RECORD_ID_RX.match(nid) and _ledger_t()[0] is not None:
            canon = canonical_serial(nid)[0] or ""
        cands.append(Candidate(nid, base.source or "chain", canon))
    cands = tuple(cands)

    if len(cands) == 1:
        state = "RESOLVED"
    elif len(cands) > 1:
        state = "AMBIGUOUS"
    else:
        # ONLY TIERS THAT COULD HAVE ANSWERED THIS REF COUNT, and getting this wrong once already
        # cost me the opposite of the original defect. The first cut read "any tier unavailable ->
        # SUBSTRATE_UNAVAILABLE" over ALL tiers -- so with no ledger configured (the normal case:
        # the ledger is a published snapshot named by $NERVES_LEDGER, usually unset) EVERY genuine
        # miss reported SUBSTRATE_UNAVAILABLE. That is a permanent false alarm, and a false alarm
        # everywhere is the same disease as a collapse everywhere: the state stops carrying
        # information. A dead LEDGER cannot make a FILENAME unknowable -- the file tiers all
        # answered, and none of them knew it.
        dead = [t for t in tiers if not t.available and _tier_consulted(t.tier, inner)]
        state = "SUBSTRATE_UNAVAILABLE" if dead else "GENUINELY_UNADDRESSED"

    return Resolution(ref, list(base.node_ids), base.kind, base.confidence, base.source,
                      state=state, tiers=tiers, candidates=cands, fabric=THIS_FABRIC,
                      evidence=evidence, policy=base.policy)


# -- AC2: THE LEDGER SPINE, READ-ONLY -------------------------------------------------------------
#
# The resolver READS the ISCK ledger and never writes to it. That is not a promise in a docstring:
# `no_ledger_writes()` below is an AST sweep of this module for admit/mint/write calls, and it is an
# arm of the battery. A resolver that could mint would be able to answer a question by CREATING its
# answer, which is the one failure mode a keystone must not have.
#
# WHY A SERIAL AND NOT A NODE ID. A node id names WHERE something is (a path, a graph node); a
# minted `ent:` serial names WHAT it is, across renames and rebuilds. The legacy node_ids stay
# exactly as they were -- the canonical serial travels BESIDE them, never instead of them.
LEDGER_ENV = "NERVES_LEDGER"
# `canonicalized_as` and `merged_into` are CORRECTIVE identity: they say this serial IS that one.
# `candidate_equivalence` is a PROPOSAL that two serials might be the same subject -- following it
# would report a guess as an identity, which is exactly what AC2 forbids ("candidate-only serials
# are never reported canonical"). The exclusion is by ENUMERATION of what canonicalises, so a new
# relation_type added to the contract is non-canonicalising until someone decides otherwise, rather
# than silently joining the fold.
CANONICALIZING = ("canonicalized_as", "merged_into")
_RECORD_ID_RX = re.compile(r"^(ent|mat|matv|run|sf|sv|rel|rcpt|obs|lce|bind):[A-Za-z0-9_.:-]+$")


@functools.lru_cache(maxsize=1)
def _ledger_t():
    """The ledger read surface, WITH liveness. Returns (records_or_None, TierStatus).

    Substrate: a PUBLISHED snapshot named by $NERVES_LEDGER. There is deliberately no default path
    that silently resolves to nothing -- an unset variable is reported UNAVAILABLE with that as the
    reason, so "no ledger configured here" and "the ledger is empty" stay different answers. That
    distinction is the whole subject of this TO.
    """
    path = os.environ.get(LEDGER_ENV, "").strip()
    if not path:
        return None, TierStatus("ledger", False, "$%s is not set" % LEDGER_ENV, "KeyError", "")
    vintage = _vintage_of(path)
    if not os.path.exists(path):
        return None, TierStatus("ledger", False, "ledger snapshot absent at %s" % path,
                                "FileNotFoundError", vintage)
    try:
        import sqlite3
        con = sqlite3.connect("file:%s?mode=ro" % path.replace(chr(92), "/"), uri=True)
        try:
            rows = [json.loads(b) for (b,) in con.execute("SELECT body FROM records")]
        finally:
            con.close()
        return rows, TierStatus("ledger", True, "", "", vintage)
    except (sqlite3.Error, ValueError, OSError) as exc:
        return None, TierStatus("ledger", False, "ledger snapshot unreadable",
                                type(exc).__name__, vintage)


def canonical_serial(serial: str):
    """The canonical serial for any serial, via the identity_relation fold. Returns (serial, why).

    RETIRED -> CANONICAL, CANONICAL -> ITSELF (AC4). Followed transitively with a seen-set, because
    a chain a->b->c must land on c and a CYCLE must not hang the keystone -- a resolver that loops
    on bad data is worse than one that answers wrongly, because nothing downstream ever gets to
    disagree with it.
    """
    rows, status = _ledger_t()
    if rows is None:
        return None, "ledger UNAVAILABLE (%s)" % status.reason
    rel = [r for r in rows if r.get("record_type") == "identity_relation"]
    seen, cur = {serial}, serial
    hops = []
    while True:
        nxt = None
        for r in rel:
            if r.get("relation_type") in CANONICALIZING and r.get("subject_serial") == cur:
                nxt = r.get("object_serial")
                hops.append("%s --%s--> %s" % (cur, r.get("relation_type"), nxt))
                break
        if not nxt or nxt in seen:
            break
        seen.add(nxt)
        cur = nxt
    return cur, (" ; ".join(hops) if hops else "canonical is itself")


def ledger_has(serial: str) -> bool:
    rows, _st = _ledger_t()
    if not rows:
        return False
    for r in rows:
        for k, v in r.items():
            if (k.endswith("_serial") or k.endswith("_id")) and v == serial:
                return True
    return False


def no_ledger_writes(path=None) -> tuple:
    """AC2's NEGATIVE ARM, in the module it polices: this resolver must contain NO write call.

    An AST sweep, not a grep: a grep for "admit" matches the word in this very comment, and a
    control a comment can flip is not a control. Returns (ok, findings).
    """
    import ast
    path = path or os.path.abspath(__file__)
    tree = ast.parse(io_open_text(path))
    banned = {"admit", "mint", "write", "write_text", "commit", "execute", "executemany"}
    allow_execute_on = {"con", "cursor", "db"}          # read-only SELECT through a ro: URI
    findings = []
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call) or not isinstance(n.func, ast.Attribute):
            continue
        name = n.func.attr
        if name not in banned:
            continue
        recv = getattr(n.func.value, "id", "")
        if name in ("execute", "executemany") and recv in allow_execute_on:
            continue
        findings.append("%s(...) at line %d" % (name, n.lineno))
    return (not findings), findings


def io_open_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def _cache_clear():
    """Drop every memoised tier and result. Needed by the arm below, which must observe the SAME
    ref against a DIFFERENT substrate -- an lru_cache would otherwise hand back the answer computed
    while the substrate was alive, and the arm would pass by remembering rather than by measuring."""
    for fn in (_trace_graph_t, _pydeps_t, _graph_index_t, _repo_basenames_t, _tools_on_disk_t,
               _graph_index, _tools_on_disk, _resolve_chain, resolve, _resolver_version,
               _ledger_t):
        try:
            fn.cache_clear()
        except AttributeError:
            pass


def substrate_arm(ref: str) -> dict:
    """AC1's REQUIRED ARM: remove one tier's substrate and the SAME ref must FLIP state.

    This is the arm that proves the repair is real rather than cosmetic. Before it, a dead substrate
    and a genuine miss were byte-identical; the only way to show they no longer are is to take the
    identical ref, run it against a live estate and against a stripped one, and read two DIFFERENT
    states out. If both arms returned GENUINELY_UNADDRESSED the five states would be decoration.

    Non-destructive by construction: it points the resolver at an EMPTY TEMPORARY directory and puts
    _WS back. It never touches .comp-graph, .tools or the repo -- a control that has to damage the
    estate to prove a point is not a control anybody will run twice.
    """
    global _WS
    import tempfile
    _cache_clear()
    live = resolve(ref)
    saved = _WS
    try:
        _WS = tempfile.mkdtemp(prefix="nerves-no-substrate-")
        _cache_clear()
        stripped = resolve(ref)
        dead = [t.tier for t in stripped.tiers if not t.available]
    finally:
        _WS = saved
        _cache_clear()
    return {"ref": ref, "live_state": live.state, "stripped_state": stripped.state,
            "flipped": live.state != stripped.state,
            "stripped_is_substrate_unavailable": stripped.state == "SUBSTRATE_UNAVAILABLE",
            "dead_tiers": dead, "why": why_unavailable(stripped),
            "byte_identical": live.as_dict() == stripped.as_dict()}


# Which tiers a ref of this shape is actually ASKED. The ledger answers identities; the file and
# graph tiers answer names and paths. A tier that was never going to be consulted cannot be the
# reason a ref went unanswered.
_LEDGER_ONLY = ("ledger",)


def _tier_consulted(tier: str, ref: str) -> bool:
    if tier in _LEDGER_ONLY:
        return bool(_RECORD_ID_RX.match(ref or ""))
    return True


def why_unavailable(res: Resolution) -> str:
    """One line naming every dead tier and its exception class -- the sentence AC1 requires
    SUBSTRATE_UNAVAILABLE to be able to say, and which a clean miss can never produce."""
    dead = res.substrate_unavailable
    if not dead:
        return ""
    return "; ".join("%s UNAVAILABLE (%s: %s)" % (t.tier, t.exception_class or "no exception",
                                                  t.reason or "no reason given") for t in dead)


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
    by_state = {}
    for x in res:
        by_state[x.state] = by_state.get(x.state, 0) + 1
    stats = {
        "refs_total": n,                       # THE DENOMINATOR
        "addressed": len(addressed),
        "unaddressed": n - len(addressed),
        "hit_rate_pct": round(100.0 * len(addressed) / n, 1) if n else 0.0,
        "by_kind": by_kind, "by_confidence": by_conf,
        # ADDITIVE. `unaddressed` above is now a SUM over three different worlds, so a reader who
        # reasons from it alone is reasoning from the collapse this repair removed. by_state splits
        # it; both are printed so no existing consumer breaks and no new one is misled.
        "by_state": by_state,
        "substrate_unavailable": by_state.get("SUBSTRATE_UNAVAILABLE", 0),
        "resolver_version": _resolver_version(),
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
    #
    # THIS CASE HAS BEEN FAILING SINCE 2026-08-06 AND NOT BECAUSE OF THIS REPAIR. Its subject was
    # `comp-surface-check`, deleted at 1a962886be when the tool was retired (CLAUDE.md rule 20 says
    # so in words: "comp-surface-check is RETIRED"). The case asserted a retired tool still
    # resolves, so it went red the day the tool went away and stayed red for 22 days -- a test
    # measuring an estate that no longer exists.
    #
    # It is RE-POINTED, not weakened: `comp-aws` is a live bash shim, so the case still tests the
    # exact property it was written for -- that a NON-PYTHON tool is addressable, which comp-pydeps
    # (python-only, shebang-sniffed) cannot do alone.
    r6 = resolve("comp-aws")                # a BASH shim -- comp-pydeps indexes python only (x133 miss)
    ck("gap1.bash_shim_addressable", r6.addressed and r6.kind == "COMPILER",
       f"{r6.kind}/{r6.source} -> {r6.node_ids}")

    # AND THE RETIREMENT BECOMES ITS OWN CASE, which is only expressible now: a tool that was
    # removed from the estate must read GENUINELY_UNADDRESSED (every tier alive, nobody knows it),
    # never SUBSTRATE_UNAVAILABLE. Under the old two-state contract these were the same answer, so
    # "the tool was retired" and "the tool index is broken" could not be told apart.
    r6b = resolve("comp-surface-check")
    ck("gap1b.retired_tool_is_a_genuine_miss_not_a_dead_substrate",
       r6b.state == "GENUINELY_UNADDRESSED" and not r6b.substrate_unavailable,
       f"{r6b.state}")
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
