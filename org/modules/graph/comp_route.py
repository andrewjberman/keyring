"""
comp-route -- the NFRA_COMPROUTE core posterior decision engine (Stage-1 L3, the DECIDES verb).

Given an INTENT (a natural-language question / HUD-intercepted call) and a CONTEXT (agent role,
working-set, session trajectory), decide WHICH capability best serves it -- the fabric's
intent->capability router. This is the ENGINE (the systems alpha), NOT a surface: comp-which is the
first surface that will invoke it (L4).

    score(cap) = w_q*query_match(intent, cap.keywords)
               + w_s*surface_prior(cap.affinity_key, ctx)      # PRIOR  (COMPUNIFY, additive boost)
               + w_h*history_affinity(cap.affinity_key, role)  # LEARNED (COMPLEARN tool_activity, OUTCOME-weighted)

    + a MARGIN-DISAMBIGUATION gate (never silent-argmax within eps -- surface BOTH with their concern)
    + the PRIOR-not-FILTER invariant (prior biases, never excludes)
    + graceful COLD-START (empty affinity -> score = query + prior + margin).

THE GENERALIZATION INTERFACE (PRD section 3 -- the load-bearing systems alpha): the engine is
capability-map-AGNOSTIC. It never assumes it is routing "comp-tools". It routes over a pluggable
`CapabilityMapProvider` (yields {id, keywords, surface, grain, concern, affinity_key} capabilities +
owns the surface_prior lookup) plus an optional `AffinityProvider` (the OUTCOME-weighted learned
term). The comp-tool map (COMPUNIFY, ~C's L2) is merely the FIRST provider; skills / MCP tools / docs
/ agent-lane-dispatch are later providers -- NEW DATA, not a re-architecture. Any code here that
assumes "comp-tool" is a finding (CTO ruling 2).

THE L2->L3 INTERFACE CONTRACT (locked with ~C, 2026-07-01, NFRA_COMPROUTE section 3):
  Capability = 6 binding fields (id, keywords, surface, grain, concern, affinity_key)
             + 3 enrichments (declared_grains, kind, routable).
  CapabilityMapProvider = capabilities() -> list[Capability]   (engine filters `routable` for targets)
                          surface_prior(affinity_key, ctx) -> float   (role_surface_affinity; cold-start -> 0.0)
                          affinity_key(cap) -> str
  ctx at the provider boundary = a plain dict {"role","working_set","trajectory"}.
At L4 the engine imports ~C's `Capability` + `CapabilityMapProvider` from capability_map_provider.py;
until then a FIELD-IDENTICAL local copy lets L3 build+self-test now. The engine duck-types every
capability field (+ getattr(cap,"routable",True)), so it consumes ~C's real objects with zero edit.

CTO rulings honored (PRD section 6): (2) capability-map-agnostic from Stage 1; (3) PRIOR-not-FILTER +
never-silent-argmax are inviolable; (4) history_affinity is OUTCOME-weighted, never invocation count
(the Goodhart tie -- count enters only as a confidence denominator via m-estimate shrinkage).

Read-only, deterministic, no LLM, lane-portable (org/modules/graph/). The live tool_activity affinity
read is best-effort + degrades to cold-start offline (L4 wires the live Trino path into comp-which).

Usage:
    comp-route "<intent>" [--role R] [--working-set a.py,b.py] [--provider fixture|smoke]
               [--surface-affinity graph:0.6,portal:0.7] [--live-affinity] [--json]
    comp-route --self-test [--json]     # reproduces the PRD section 9c smoke-provider + the 2 grounded cases

Author: 0.8.0_AE_CloudComp~E (NFRA_COMPROUTE Stage-1 L3). 2026-07-01.
Spec: docs/architecture/NFRA_COMPROUTE_PRD.md sections 2/3/9 + org/projects/NFRA_COMPROUTE/DECOMP-MAP.md.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from typing import Iterable, Mapping, Optional, Protocol, runtime_checkable

_WS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))

# Stopwords dropped from intent/keyword tokenization (query_match is coverage, not TF).
_STOP = frozenset(
    "a an the of for to in on is are do does how what which with by via that this my your".split()
)
_TOKEN = re.compile(r"[a-z0-9]+")


# ============================================================================================
# The capability + context + result data model (provider-agnostic -- no "comp-tool" anywhere).
# Field-identical to ~C's L2 `Capability` (capability_map_provider.py); the engine duck-types it.
# ============================================================================================
@dataclass(frozen=True)
class Capability:
    """One routable capability, as a provider yields it. The section-3 interface shape -- provider-agnostic:
    a comp-tool, a skill, an MCP tool, a doc, or an agent-lane all fit this SAME shape."""

    id: str
    keywords: tuple[str, ...]
    surface: str                 # where it lives (a surface / seam-id / "META")
    grain: str                   # its home granularity (single)
    concern: str                 # what it is FOR (the disambiguation label an agent reads)
    affinity_key: str            # NORMALIZED surface = the role_surface_affinity + tool_activity join key
    # --- enrichments (non-binding; defaulted so built-in providers need not specify) ---
    declared_grains: tuple[str, ...] = ()
    kind: str = "surface"        # "surface" | "seam" | "meta"
    routable: bool = True        # False = pure tooling-layer node (gate/test/router), not a routing target


@dataclass
class RouteContext:
    """The routing context = {role, working-set, trajectory}. Normalized to a plain dict at the
    provider boundary (ctx["role"]) per the locked L2->L3 contract."""

    role: str = ""
    working_set: tuple[str, ...] = ()      # open files / recent tools (context signal)
    trajectory: tuple[str, ...] = ()       # recent intents (session-trajectory signal)

    def as_dict(self) -> dict:
        return {"role": self.role, "working_set": list(self.working_set), "trajectory": list(self.trajectory)}


def _ctx_dict(ctx) -> dict:
    """Accept either a RouteContext or a plain mapping; normalize to the provider-boundary dict."""
    if isinstance(ctx, RouteContext):
        return ctx.as_dict()
    if isinstance(ctx, Mapping):
        return {"role": ctx.get("role", ""), "working_set": list(ctx.get("working_set", [])),
                "trajectory": list(ctx.get("trajectory", []))}
    return {"role": "", "working_set": [], "trajectory": []}


@dataclass
class Weights:
    """Scorer weights + the disambiguation margin. Tunable; the Goodhart gate (CVO) tunes these on a
    VALUE metric, never usage. Defaults: likelihood-primary (query), prior a boost, affinity meaningful."""

    w_q: float = 0.55
    w_s: float = 0.20
    w_h: float = 0.25
    eps: float = 0.05      # within-margin => disambiguate, never argmax


@dataclass
class Scored:
    cap: Capability
    score: float
    query: float
    prior: float
    affinity: Optional[float]   # None => cold-start for this capability (no history)
    matched_terms: tuple[str, ...]


@dataclass
class RouteResult:
    kind: str                       # "decision" | "disambiguation" | "empty"
    intent: str
    ranked: list                    # list[Scored], full ranking (nothing is ever filtered out by score)
    within_margin: list             # list[Scored] tied within eps (== [decision] when confident)
    cold_start: bool
    training_row: dict              # the flywheel row L4 persists to tool_activity
    regression_case: dict           # the routing regression-test case L4 persists

    @property
    def decision(self) -> Optional[Scored]:
        return self.within_margin[0] if self.kind == "decision" and self.within_margin else None


# ============================================================================================
# The provider interfaces (PRD section 3, locked with ~C). The engine depends ONLY on these.
# ============================================================================================
@runtime_checkable
class CapabilityMapProvider(Protocol):
    """The PRIOR provider (COMPUNIFY, ~C's L2). Yields the full capability set + owns the
    role_surface_affinity lookup. The comp-tool map is the FIRST impl; any capability-map (skills /
    MCP / docs / lanes) implements the same protocol."""

    def capabilities(self) -> list:                                   # -> list[Capability]
        ...

    def surface_prior(self, affinity_key: str, ctx: Mapping) -> float:
        ...

    def affinity_key(self, cap) -> str:
        ...


@runtime_checkable
class AffinityProvider(Protocol):
    """The LEARNED term (COMPLEARN, ~E's tool_activity). Returns an OUTCOME-weighted affinity in [0,1]
    for (cap_id, role) -- keyed PER-CAP-ID (CTO ruling 2026-07-01), so it can disambiguate same-surface
    tools. `prior` is the m-estimate backoff (the engine passes the cap's surface_prior): a cold cap
    (n=0) backs off to it, a hot cap converges to its own per-cap outcome mean. Returns None only when
    there is no data AND no prior. MUST be outcome-weighted, never a raw invocation count (CTO ruling 4)."""

    def affinity(self, cap_id: str, role: str, ctx: Mapping, prior: Optional[float] = None) -> Optional[float]:
        ...


# ============================================================================================
# The scorer (deterministic + explainable). Each term is in [0,1]; weights sum to 1 => score in [0,1].
# ============================================================================================
def _tokenize(text: str) -> list[str]:
    return [t for t in _TOKEN.findall(text.lower()) if t not in _STOP]


def query_match(intent: str, keywords: Iterable[str]) -> tuple[float, tuple[str, ...]]:
    """Coverage of the intent by the capability's keywords, in [0,1], + which intent terms matched.

    For each intent token, it matches if any keyword token equals it or contains it (light stem
    tolerance). score = matched_intent_tokens / total_intent_tokens (LIKELIHOOD). Deterministic; no
    ranking magic, so a disambiguation is explainable by the matched terms."""
    itoks = _tokenize(intent)
    if not itoks:
        return 0.0, ()
    ktoks = set()
    for kw in keywords:
        ktoks.update(_tokenize(kw))
    matched = []
    for it in itoks:
        if any(it == kt or it in kt or kt in it for kt in ktoks):
            matched.append(it)
    return len(matched) / len(itoks), tuple(dict.fromkeys(matched))


def _score_one(cap, intent: str, ctx_d: dict, weights: Weights,
               provider: CapabilityMapProvider,
               affinity_provider: Optional[AffinityProvider]) -> Scored:
    q, matched = query_match(intent, cap.keywords)
    key = provider.affinity_key(cap) if hasattr(provider, "affinity_key") else getattr(cap, "affinity_key", cap.surface)
    # PRIOR (w_s): provider-owned role_surface_affinity lookup, keyed by the SURFACE (affinity_key).
    # ADDITIVE, never a filter; cold-start -> 0.0.
    p = float(provider.surface_prior(key, ctx_d)) if hasattr(provider, "surface_prior") else 0.0
    a: Optional[float] = None
    if affinity_provider is not None:
        # LEARNED (w_h) keyed PER-CAP-ID (CTO ruling 2026-07-01) -- "has THIS role had good outcomes
        # with THIS capability" is inherently per-cap; a surface-grain learned term is redundant with
        # w_s and cannot disambiguate same-surface tools. The m-estimate prior is the surface-grain
        # surface_prior, so a cold cap (n=0) backs off to the static prior (subsumes the (c) hybrid).
        # NOTE: SHADOW until real routing-outcome telemetry justifies live weighting (CTO seq step 4);
        # comp-which passes affinity_provider=None today, so live routing stays cold-start.
        a = affinity_provider.affinity(getattr(cap, "id", ""), ctx_d.get("role", ""), ctx_d, prior=p)
    a_term = a if a is not None else 0.0           # no learned data + no backoff => 0 contribution
    score = weights.w_q * q + weights.w_s * p + weights.w_h * a_term
    return Scored(cap=cap, score=score, query=q, prior=p, affinity=a, matched_terms=matched)


# ============================================================================================
# THE ENGINE -- route(intent, ctx, provider [, affinity_provider]). Provider-agnostic.
# ============================================================================================
def route(intent: str, ctx, provider: CapabilityMapProvider,
          affinity_provider: Optional[AffinityProvider] = None,
          weights: Optional[Weights] = None) -> RouteResult:
    """Decide which capability serves `intent` in `ctx`.

    PRIOR-not-FILTER: EVERY routable candidate is scored + ranked; none is ever excluded by surface (a
    strong query_match on a non-ctx surface can win or land within-margin). MARGIN gate: within eps of
    the top => surface ALL tied candidates with their concern (never silent-argmax). COLD-START: no
    affinity_provider (or it returns None for every cap) => score = query + prior + margin, still routes."""
    weights = weights or Weights()
    ctx_d = _ctx_dict(ctx)
    caps = [c for c in provider.capabilities() if getattr(c, "routable", True)]
    scored = [_score_one(c, intent, ctx_d, weights, provider, affinity_provider) for c in caps]
    scored.sort(key=lambda s: (-s.score, s.cap.id))     # deterministic tie-break by id

    if not scored:
        return RouteResult("empty", intent, [], [], True, {}, {})

    top = scored[0].score
    within = [s for s in scored if (top - s.score) < weights.eps]   # includes the top; PRIOR never filters
    cold_start = all(s.affinity is None for s in scored)
    kind = "decision" if len(within) == 1 else "disambiguation"

    # The flywheel: every route is a training row; every disambiguation is a regression-test case.
    # L4 persists these (training_row -> tool_activity; regression_case -> the routing regression test).
    training_row = {
        "intent": intent, "role": ctx_d.get("role", ""),
        "working_set": ctx_d.get("working_set", []),
        "ranked": [{"id": s.cap.id, "score": round(s.score, 4),
                    "query": round(s.query, 4), "prior": round(s.prior, 4),
                    "affinity": (round(s.affinity, 4) if s.affinity is not None else None)}
                   for s in scored[:5]],
        "kind": kind, "cold_start": cold_start,
        # outcome is filled at USE time by the surface (which option the agent picked / whether it
        # resolved the intent) -- that closes the loop into the OUTCOME-weighted signal, not a count.
        "outcome": None,
    }
    regression_case = {
        "intent": intent, "role": ctx_d.get("role", ""),
        "expect_kind": kind,
        "expect_ids": [s.cap.id for s in within],
    } if kind == "disambiguation" else {}

    return RouteResult(kind, intent, scored, within, cold_start, training_row, regression_case)


# ============================================================================================
# Concrete providers.  (a) a dict provider for tests/smoke; (b) the live tool_activity affinity.
# ============================================================================================
class DictCapabilityProvider:
    """A capability map from an in-memory list + a role_surface_affinity table. Backs the smoke
    provider + the validation fixtures, and mirrors ~C's L2 shape (capabilities/surface_prior/
    affinity_key). Deliberately trivial: proves the engine needs NOTHING but the section-3 interface.

    role_surface_affinity: {role: {affinity_key: prior_in_0_1}}. Unknown role/key -> 0.0 (cold-start)."""

    def __init__(self, caps: Iterable[Capability], role_surface_affinity: Optional[dict] = None):
        self._caps = list(caps)
        self._rsa = role_surface_affinity or {}

    def capabilities(self) -> list:
        return list(self._caps)

    def surface_prior(self, affinity_key: str, ctx: Mapping) -> float:
        role = ctx.get("role", "") if isinstance(ctx, Mapping) else getattr(ctx, "role", "")
        return float(self._rsa.get(role, {}).get(affinity_key, 0.0))   # ADDITIVE; unknown -> 0.0

    def affinity_key(self, cap) -> str:
        return getattr(cap, "affinity_key", cap.surface)


class DictAffinityProvider:
    """A pre-computed {(cap_id, role): value} affinity map (already outcome-weighted), keyed PER-CAP-ID.
    For tests / a cache. An absent cap backs off to `prior` (the surface-grain m-estimate prior the
    engine passes); None if no prior given either."""

    def __init__(self, table: dict):
        self._t = table

    def affinity(self, cap_id: str, role: str, ctx: Mapping, prior: Optional[float] = None) -> Optional[float]:
        if (cap_id, role) in self._t:
            return float(self._t[(cap_id, role)])
        if cap_id in self._t:
            return float(self._t[cap_id])
        return prior


# ---- the OUTCOME-weighted learned term off the live tool_activity catalog (CTO ruling 4) ----------
def result_class(result: Optional[str]) -> float:
    """Map a tool_activity `result` cell to an outcome value in [0,1]. PASS-class -> 1.0, FAIL/DENY ->
    0.0, unknown/neutral -> 0.5. This is the VALUE anchor: a tool that runs a lot but FAILS scores
    low, a tool that succeeds scores high -- the opposite of a usage count."""
    if result is None:
        return 0.5
    r = str(result).strip().lower()
    if not r:
        return 0.5
    if any(t in r for t in ("pass", "ok", "success", "rc0", "rc=0", "green", "match", "run-grep", "run-glob")):
        return 1.0
    if any(t in r for t in ("fail", "error", "deny", "denied", "rc1", "rc=1", "traceback", "missing", "stale", "red")):
        return 0.0
    return 0.5


def outcome_value(row: dict) -> float:
    """Per-row outcome value in [0,1]: the result class, plus a small bonus when the row carries a
    GAP-FOUND annotation (gap_text -- the highest-value discovery per the tool_activity schema).
    NOTE: `matches` (a rail count) is deliberately NOT used as reward -- it is the Goodhart trap."""
    v = result_class(row.get("result"))
    if row.get("gap_text"):
        v = min(1.0, v + 0.2)
    return v


def outcome_weighted_affinity(rows: list, key: str, role: str, k: float = 5.0,
                              prior: Optional[float] = None) -> Optional[float]:
    """OUTCOME-weighted affinity for (key=cap_id, role) over tool_activity rows, in [0,1].

    Anti-Goodhart core: the SCORE is the (shrunk) MEAN outcome value, never the SUM/COUNT. Count enters
    ONLY as the confidence denominator of an m-estimate: affinity = (sum(v) + k*p) / (n + k). So 100
    low-value invocations do NOT beat 5 high-value ones; more usage only sharpens confidence in the
    outcome estimate, it is never itself the reward (CTO ruling 4).

    `prior` is the surface-grain m-estimate backoff (the engine passes the cap's surface_prior, CTO
    ruling 2026-07-01): a cold cap (n=0) backs off to it -- subsuming the (c) hybrid -- and a hot cap
    converges to its own per-cap mean. n=0 with no prior returns None (true cold-start)."""
    vals = [outcome_value(r) for r in rows
            if r.get("tool") == key and (not role or r.get("role") in (role, None))]
    n = len(vals)
    if n == 0:
        return prior   # backoff to the surface-grain prior; None if none given (true cold-start)
    p = prior if prior is not None else 0.5
    return (sum(vals) + k * p) / (n + k)


class ToolActivityAffinityProvider:
    """The Stage-1 LEARNED provider: OUTCOME-weighted history_affinity off ~E's live tool_activity
    catalog (COMPLEARN). Lane-portable + best-effort: `row_source` defaults to a graceful reader that
    returns [] offline, so the engine degrades to cold-start rather than failing. L4 wires the live
    Trino/parquet path (the catalog lives at s3://opal-313476888478-globgrph/warehouse/tool_activity/).

    The engine never imports this -- it is injected -- so the comp-tool coupling stays OUT of the
    agnostic core (CTO ruling 2)."""

    def __init__(self, row_source=None, k: float = 5.0):
        self._rows = None
        self._row_source = row_source if row_source is not None else _default_tool_activity_rows
        self._k = k

    def _load(self) -> list:
        if self._rows is None:
            try:
                self._rows = list(self._row_source())
            except Exception:  # noqa: BLE001 -- offline / no reader => cold-start, never a hard fail
                self._rows = []
        return self._rows

    def affinity(self, cap_id: str, role: str, ctx: Mapping, prior: Optional[float] = None) -> Optional[float]:
        return outcome_weighted_affinity(self._load(), cap_id, role, k=self._k, prior=prior)


def _default_tool_activity_rows() -> list:
    """Best-effort local read of the tool_activity parquet cache. Returns [] when unavailable (no
    pyarrow / no cache) so the provider degrades to cold-start. L4 replaces this with the live Trino
    read wired into comp-which."""
    cache = os.path.join(_WS, ".comp-graph", "tool_activity_cache.parquet")
    if not os.path.exists(cache):
        return []
    try:
        import pyarrow.parquet as pq  # lazy: never a hard import dependency of the engine
    except Exception:  # noqa: BLE001
        return []
    try:
        return pq.read_table(cache).to_pylist()
    except Exception:  # noqa: BLE001
        return []


# ============================================================================================
# Built-in providers for the CLI / self-test.
# ============================================================================================
def build_fixture_caps() -> list:
    """The comp-tool validation caps the 2 grounded PRD-section-2 failure modes use. affinity_key ==
    surface for these surface-homed tools (per ~C's normalization)."""
    return [
        Capability("comp-cluster", ("cluster", "group", "similar", "near-duplicate", "components"),
                   surface="graph", grain="cross-tool", concern="grouping similar things",
                   affinity_key="graph"),
        Capability("comp-transform", ("transform", "component", "schema", "field", "props", "similar"),
                   surface="portal", grain="component", concern="component schema / prop shape",
                   affinity_key="portal"),
        Capability("comp-drift", ("drift", "change", "parity", "stale", "vintage", "estate"),
                   surface="estate", grain="seam", concern="change/parity drift detection",
                   affinity_key="estate"),
        Capability("comp-aws", ("aws", "resource", "estate", "s3", "lambda", "drift"),
                   surface="estate", grain="resource", concern="live AWS resource inspection",
                   affinity_key="estate"),
    ]


def build_fixture_provider(role_surface_affinity: Optional[dict] = None) -> DictCapabilityProvider:
    return DictCapabilityProvider(build_fixture_caps(), role_surface_affinity=role_surface_affinity)


def build_smoke_provider(role_surface_affinity: Optional[dict] = None) -> DictCapabilityProvider:
    """The PRD section 9c SMOKE PROVIDER -- a 2nd capability-map in a NON-tool domain (a library's
    sections). It slots into route() with ZERO engine change: if the same engine routes this, the
    generalization interface is REAL (the engine truly does not assume comp-tools)."""
    caps = [
        Capability("fiction-shelf", ("novel", "fiction", "story", "literature"),
                   surface="reading-room", grain="shelf", concern="borrow a novel",
                   affinity_key="reading-room"),
        Capability("reference-desk", ("dictionary", "encyclopedia", "reference", "atlas", "lookup"),
                   surface="reference-hall", grain="desk", concern="look a fact up",
                   affinity_key="reference-hall"),
        Capability("periodicals", ("magazine", "journal", "newspaper", "periodical"),
                   surface="reading-room", grain="rack", concern="read a periodical",
                   affinity_key="reading-room"),
    ]
    return DictCapabilityProvider(caps, role_surface_affinity=role_surface_affinity)


# ============================================================================================
# Rendering + CLI
# ============================================================================================
def _fmt_scored(s: "Scored") -> str:
    a = "cold" if s.affinity is None else f"{s.affinity:.2f}"
    return (f"    {s.cap.id:16s} score={s.score:.3f}  [q={s.query:.2f} p={s.prior:.2f} h={a}]  "
            f"{s.cap.surface}/{s.cap.grain} -- {s.cap.concern}")


def render(r: RouteResult) -> str:
    if r.kind == "empty":
        return f'comp-route: no candidate capabilities for "{r.intent}"'
    L = [f'=== comp-route: "{r.intent}" ===' + ("   [COLD-START: no learned affinity]" if r.cold_start else "")]
    if r.kind == "decision":
        d = r.decision
        L.append(f"\nDECISION (confident, margin >= eps): {d.cap.id}")
        L.append(_fmt_scored(d))
    else:
        L.append(f"\nDISAMBIGUATION ({len(r.within_margin)} within-margin -- pick by concern, NOT auto-chosen):")
        for s in r.within_margin:
            L.append(_fmt_scored(s))
    L.append("\nfull ranking:")
    L += [_fmt_scored(s) for s in r.ranked]
    return "\n".join(L)


def _result_json(r: RouteResult) -> dict:
    def sd(s):
        return {"id": s.cap.id, "score": round(s.score, 4), "query": round(s.query, 4),
                "prior": round(s.prior, 4), "affinity": (round(s.affinity, 4) if s.affinity is not None else None),
                "surface": s.cap.surface, "grain": s.cap.grain, "concern": s.cap.concern,
                "matched_terms": list(s.matched_terms)}
    return {"kind": r.kind, "intent": r.intent, "cold_start": r.cold_start,
            "decision": (sd(r.decision) if r.decision else None),
            "within_margin": [sd(s) for s in r.within_margin],
            "ranked": [sd(s) for s in r.ranked],
            "training_row": r.training_row, "regression_case": r.regression_case}


# ---- the self-test: reproduces PRD section 9c (smoke) + the 2 grounded section-2 cases -----------
def _self_test() -> tuple[bool, list]:
    checks = []

    def ck(name, ok, detail=""):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})
        return ok

    # Case A: comp-cluster -> comp-transform (within-margin CROSS-tool): PRIOR narrows + MARGIN
    # disambiguates. Different surfaces (graph vs portal) => the prior contributes (differs), yet they
    # remain within-margin => BOTH surfaced with concern (never silent-argmax).
    provA = build_fixture_provider(role_surface_affinity={"DE": {"graph": 0.6, "portal": 0.7}})
    ctxA = RouteContext(role="DE")
    # "similar components" hits comp-cluster + comp-transform equally on query_match => the DIFFERING
    # surface_prior (graph 0.6 vs portal 0.7) is what narrows, yet the pair stays within eps => a
    # within-margin CROSS-tool disambiguation (the PRD-section-2 case-A behavior, not a silent argmax).
    rA = route("similar components", ctxA, provA)
    idsA = {s.cap.id for s in rA.within_margin}
    priorsA = {s.cap.id: s.prior for s in rA.ranked}
    ck("A.disambiguation", rA.kind == "disambiguation", f"kind={rA.kind}")
    ck("A.both_surfaced", {"comp-cluster", "comp-transform"} <= idsA, f"within={sorted(idsA)}")
    ck("A.prior_contributes", priorsA.get("comp-cluster") != priorsA.get("comp-transform"),
       f"priors cluster={priorsA.get('comp-cluster')} transform={priorsA.get('comp-transform')}")
    ck("A.each_has_concern", all(s.cap.concern for s in rA.within_margin), "")

    # Case B: comp-drift -> comp-aws (SAME surface 'estate'): surface-prior EQUAL => prior cannot
    # disambiguate => proves prior necessary-not-sufficient => LIKELIHOOD + MARGIN(by concern) resolve.
    provB = build_fixture_provider(role_surface_affinity={"AE": {"estate": 0.8}})
    ctxB = RouteContext(role="AE")
    rB = route("estate drift", ctxB, provB)
    pri = {s.cap.id: s.prior for s in rB.ranked}
    ck("B.prior_equal_same_surface", abs(pri.get("comp-drift", 0) - pri.get("comp-aws", 1)) < 1e-9,
       f"drift={pri.get('comp-drift')} aws={pri.get('comp-aws')}")
    # With the prior EQUAL for the two, removing the prior entirely must not change WHICH two are the
    # top contenders -> the prior alone is not what decides B (necessary-not-sufficient, demonstrated).
    wnop = Weights(w_q=0.75, w_s=0.0, w_h=0.25)
    rB_np = route("estate drift", ctxB, provB, weights=wnop)
    top2_B = {s.cap.id for s in rB.ranked[:2]}
    top2_B_np = {s.cap.id for s in rB_np.ranked[:2]}
    ck("B.prior_not_sufficient", top2_B == top2_B_np and {"comp-drift", "comp-aws"} <= top2_B,
       f"withprior_top2={sorted(top2_B)} noprior_top2={sorted(top2_B_np)}")

    # PRIOR-not-FILTER: a capability on a NON-ctx surface (prior 0) with the STRONGEST query_match is
    # never excluded -- it wins or lands within-margin. 'portal' is absent from role_surface_affinity.
    provC = build_fixture_provider(role_surface_affinity={"DE": {"graph": 0.9}})   # portal absent => prior 0
    rC = route("component schema field props", RouteContext(role="DE"), provC)
    ids_top = {s.cap.id for s in rC.within_margin}
    transform = next(s for s in rC.ranked if s.cap.id == "comp-transform")
    ck("C.prior_not_filter", "comp-transform" in ids_top and transform.prior == 0.0,
       f"transform prior={transform.prior} within={sorted(ids_top)}")

    # Cold-start: no affinity_provider => cold_start True, still returns a valid routing result.
    ck("coldstart.flag", rA.cold_start is True, "")
    ck("coldstart.routes", rA.kind in ("decision", "disambiguation"), "")

    # Generalization interface (PRD section 9c): the SMOKE provider (non-tool domain) routes through
    # the SAME route() with ZERO engine change.
    smoke = build_smoke_provider(role_surface_affinity={"patron": {"reading-room": 0.6}})
    rS = route("borrow a fiction novel", RouteContext(role="patron"), smoke)
    ck("smoke.routes_unchanged", rS.kind in ("decision", "disambiguation") and rS.ranked, f"kind={rS.kind}")
    ck("smoke.picks_fiction", rS.ranked[0].cap.id == "fiction-shelf", f"top={rS.ranked[0].cap.id}")

    # OUTCOME-weighted, never count (CTO ruling 4): a cap with FEW high-outcome rows beats a cap with
    # MANY low-outcome (FAIL/DENY) rows. Count must not win.
    rows = (
        [{"tool": "good", "role": "DE", "result": "PASS", "gap_text": "found gap"}] * 4
        + [{"tool": "spammy", "role": "DE", "result": "DENY"}] * 40
        + [{"tool": "spammy", "role": "DE", "result": "FAIL"}] * 40
    )
    a_good = outcome_weighted_affinity(rows, "good", "DE")
    a_spam = outcome_weighted_affinity(rows, "spammy", "DE")
    ck("goodhart.outcome_beats_count", a_good is not None and a_spam is not None and a_good > a_spam,
       f"good(n=4)={a_good:.3f} > spammy(n=80)={a_spam:.3f}")

    # PER-CAP-ID disambiguation (CTO ruling 2026-07-01, the whole point): the query "estate" matches
    # comp-drift AND comp-aws equally (both on the 'estate' surface, equal query, equal prior) -> without
    # affinity it is a TIE (disambiguation). A PER-CAP learned term (drift 0.95 vs aws 0.2) breaks the
    # tie to a confident DECISION -- the ONE job a surface-grain w_h could NOT do (it gave both caps the
    # same value). comp-aws with no per-cap data would back off to its surface_prior.
    tie = route("estate", RouteContext(role="AE"), provB)
    aff = DictAffinityProvider({("comp-drift", "AE"): 0.95, ("comp-aws", "AE"): 0.2})
    dis = route("estate", RouteContext(role="AE"), provB, affinity_provider=aff)
    ds = next(s for s in dis.ranked if s.cap.id == "comp-drift")
    aw = next(s for s in dis.ranked if s.cap.id == "comp-aws")
    ck("affinity.per_cap_disambiguates_same_surface",
       {"comp-drift", "comp-aws"} <= {s.cap.id for s in tie.within_margin} and ds.affinity == 0.95
       and aw.affinity == 0.2 and dis.decision is not None and dis.decision.cap.id == "comp-drift",
       f"no-aff={tie.kind}; with-aff decision={dis.decision.cap.id if dis.decision else None}")
    # cold cap backs off to the surface-grain prior (the (c) hybrid, subsumed by the m-estimate).
    aff2 = DictAffinityProvider({("comp-drift", "AE"): 0.95})
    dis2 = route("estate", RouteContext(role="AE"), provB, affinity_provider=aff2)
    aw2 = next(s for s in dis2.ranked if s.cap.id == "comp-aws")
    ck("affinity.cold_cap_backs_off_to_surface_prior", aw2.affinity == aw2.prior == 0.8,
       f"comp-aws affinity={aw2.affinity} == surface_prior={aw2.prior}")

    ok = all(c["pass"] for c in checks)
    return ok, checks


def main() -> int:
    ap = argparse.ArgumentParser(description="comp-route -- the NFRA_COMPROUTE posterior decision engine")
    ap.add_argument("intent", nargs="?", help="the intent (natural-language question) to route")
    ap.add_argument("--role", default="", help="agent role context (DE/AE/DS/...)")
    ap.add_argument("--working-set", default="", help="comma-separated open files / recent tools")
    ap.add_argument("--provider", choices=("fixture", "smoke"), default="fixture",
                    help="which built-in capability map to route against (default: fixture=comp-tools)")
    ap.add_argument("--surface-affinity", default="",
                    help="comma-separated affinity_key:prior pairs for --role (e.g. graph:0.6,portal:0.7)")
    ap.add_argument("--live-affinity", action="store_true",
                    help="wire the live tool_activity OUTCOME-weighted affinity (degrades to cold-start offline)")
    ap.add_argument("--self-test", action="store_true", help="run the PRD 9c smoke + 2 grounded cases")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    if args.self_test:
        ok, checks = _self_test()
        if args.json:
            print(json.dumps({"pass": ok, "checks": checks}, indent=2))
        else:
            print("=== comp-route --self-test (PRD sections 2 + 9c) ===")
            for c in checks:
                print(f"  [{'PASS' if c['pass'] else 'FAIL'}] {c['check']}" + (f"   ({c['detail']})" if c["detail"] else ""))
            print(f"\n{'OK: all checks pass' if ok else 'ERROR: one or more checks FAILED'}")
        return 0 if ok else 1

    if not args.intent:
        ap.print_help()
        return 2

    sa = {}
    for pair in args.surface_affinity.split(","):
        if ":" in pair:
            s, _, v = pair.partition(":")
            try:
                sa[s.strip()] = float(v)
            except ValueError:
                pass
    rsa = {args.role: sa} if sa else None
    ctx = RouteContext(role=args.role,
                       working_set=tuple(w.strip() for w in args.working_set.split(",") if w.strip()))
    provider = build_smoke_provider(rsa) if args.provider == "smoke" else build_fixture_provider(rsa)
    aff = ToolActivityAffinityProvider() if args.live_affinity else None
    r = route(args.intent, ctx, provider, affinity_provider=aff)
    if args.json:
        print(json.dumps(_result_json(r), indent=2))
    else:
        print(render(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
