"""
NFRA_COMPROUTE L2 -- the capability-map PROVIDER (PRD section 3 interface).

WHAT THIS IS
------------
The pluggable, provider-AGNOSTIC capability source the COMPROUTE posterior engine
(L3, ~E) consumes. It exposes the LIVE, CI-guarded COMPUNIFY map
(org/modules/graph/comp-coverage-map.yaml) as a set of `Capability` records, each
carrying the PRD section-3 shape:

    {id, keywords, surface, grain, concern, affinity_key}

behind the `CapabilityMapProvider` interface. The engine routes
`intent -> {candidate capabilities}` with ZERO knowledge that these are
"comp-tools" -- so a Stage-2 provider (skills / MCP tools / docs / agent-lane
dispatch) slots in UNCHANGED (PRD section 3 + CTO ruling 2; the section-9c
generalization proof). The comp-tool map (COMPUNIFY) is merely the FIRST provider.

PLUS the `role->surface_affinity` table hook -- the context prior the scorer reads:
`surface_prior(cap.surface, ctx) = role_surface_affinity.by_role[ctx.role][key]`.
PRIOR-not-FILTER (PRD section 2): an ADDITIVE bias (0.0 neutral, never a hard
filter); empty/unknown affinity degrades gracefully to 0.0 (cold-start-safe).

LANE-PORTABILITY (PRD section 5)
--------------------------------
Read-side cognition: a pure YAML read of the CI-guarded COMPUNIFY map -- no AWS /
infra / exec-manifest ownership needed (any DE/AE lane can author it). The map
REGISTRATION (the `role_surface_affinity` block added to comp-coverage-map.yaml)
is the COMPUNIFY governor's act; COMPROUTE READS the map, never edits it from the
router side (PRD section 8). The capability records source from the YAML ledger
(surfaces[] + tools[].surface + tool_grain_calibration + role_surface_affinity) --
the CI-guarded capability map the TO names -- NOT from the estate Kuzu graph (which
carries AWS/portal/pipeline resource nodes, not comp-tool capabilities). Lanes that
need estate-GRAPH data shell to `comp-kuzu --json`; the tool-capability map is the
YAML, read here directly (equally lane-portable).

Authored: 0.8.0_AE_CloudComp~C 2026-07-01 (NFRA_COMPROUTE.L2). Provider interface
= PRD section 3; the binding L2<->L3 contract is the six fields + the three methods.
"""

from __future__ import annotations

import dataclasses
import os
import re
from typing import Any, Iterable, List, Mapping, Optional, Tuple

try:
    import yaml
except ImportError as exc:  # pragma: no cover - yaml is a repo baseline dep
    raise ImportError("comp_capability_provider requires PyYAML (repo baseline)") from exc


_HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MAP_PATH = os.path.join(_HERE, "comp-coverage-map.yaml")
_MANIFEST_PATH = os.path.join(_HERE, "graph-call-manifest.yaml")


def _load_write_path_tools(manifest_path=None):
    """Per-tool cap.write_path, sourced from ~B's DR3 manifest tags (E1). A tool is a genuine WRITE-PATH
    tool (DR1 route() excludes it from a read/navigate intent) IFF it has >=1 write_path entry AND NO
    read-answering entry -- i.e. a WHOLE-write tool (comp-build). A MIXED tool stays write_path=False:
    comp-aws's `derive` is write but classes/metrics/diff ANSWER reads; comp-lambdamap's `derive --write`
    is a subcommand but deploy-SHA parity is a read. Tool-level exclusion of a mixed tool would wrongly
    drop its reads (and regress its read self-route). ~C DR2 finding: E1 tool-level exclusion is
    whole-write-tools ONLY; a write SUBCOMMAND is a COMPUTE-intent action (free, never read-routed)."""
    try:
        import yaml
        with open(manifest_path or _MANIFEST_PATH, "r", encoding="utf-8") as fh:
            m = yaml.safe_load(fh) or {}
    except Exception:  # noqa: BLE001 -- manifest unreadable => no write-path exclusion (fail-open, surfaced)
        return frozenset()
    per_tool = {}
    for e in (m.get("entries") or []):
        tool = str(e.get("tool", "")).split()[0]
        if tool:
            per_tool.setdefault(tool, []).append(bool(e.get("write_path", False)))
    return frozenset(t for t, flags in per_tool.items() if flags and all(flags))


# The affinity-key domain (== the normalized cap.surface). Surface-homed tools key
# on their surface; seam-homed tools bucket to SEAM; the tooling layer buckets to META.
SEAM_KEY = "SEAM"
META_KEY = "META"
SURFACE_KEYS = ("LOCAL", "GIT", "AWS-CLOUD", "MS-CLOUD", "TRINO", SEAM_KEY, META_KEY)

# FALLBACK ONLY (NFRA_COMPCLOSE Phase A, 2026-07-14): routability is now DECLARED per meta_tool in
# comp-coverage-map.yaml (`routable: true|false` on every entry) -- because this role allowlist was a
# SILENT-DROP mechanism: any meta-tool whose role was not listed here got routable=False and vanished
# from the posterior candidate set with no error (bit comp-system per the note below; bit comp-whoread /
# comp-deadgrant / comp-denytest / comp-tagauthz / comp-firmsep-sweep / comp-tool-health / comp-toolgraph
# for weeks -- agents logged "no comp-tool answers which principals touch X" while comp-whoread sat on
# disk). A NEW ROLE STRING => routable must be declared at registration, never inferred here. This set
# remains only as the fallback for a map entry that omits the key (no-regression path).
# NON-routable by design: router (comp-which), search-primitives (comp-grep/glob -- the never-dead-end
# FALLBACK, surfaced via route()'s kind="fallback", not a scored candidate), session-primitive (comp-to),
# enforcement gates, test harnesses, meta-measurement (comp-perf). routable=False still keeps inventory whole.
_ROUTABLE_META_ROLES = frozenset({
    "estate-router", "cache-management", "meta-report", "governance",
    "compdrift-loop", "complearn-loop", "fedobs-reflective-reader",
    # system-compiler (comp-system, NFRA_SYSTEM P3): a cross-surface AGGREGATOR, so it is homed in
    # meta_tools[] rather than on one surface -- but it IS a routing target (manifest tools_index
    # declares its comp-which routing string). Omitting the role left comp_route.py:329's routable
    # filter dropping it from the candidate set entirely, so no curated rule could ever surface it.
    "system-compiler",
})

# Minimal stopword set for keyword extraction (query_match wants a rich bag-of-words,
# so filter only true noise words + the ubiquitous "comp" token).
_STOPWORDS = frozenset(
    """
    a an the of to is it its at in on or and vs for per not no any this that which
    what how are be by with from into over as if so do does did has have had was
    were will can may via than then when where who whom whose but out up off both
    each only same other more most such all one two comp
    """.split()
)


@dataclasses.dataclass(frozen=True)
class Capability:
    """The PRD section-3 capability record -- the binding L2<->L3 contract shape."""

    id: str
    keywords: Tuple[str, ...]
    surface: str          # LOCAL/GIT/AWS-CLOUD/MS-CLOUD/TRINO | a seam-id | "META"
    grain: str            # the home granularity (single); declared_grains carries all
    concern: str          # the one-question concern (from the map)
    affinity_key: str     # NORMALIZED surface = the PRIOR key (role_surface_affinity / surface_prior).
    #                       NOT the learned key: the LEARNED history_affinity term keys by `id` (per-cap-id,
    #                       CTO-ratified 2026-07-01, engine f64083634) so it can disambiguate same-surface tools.
    # ---- enrichments (non-binding; do not alter the 6 above) ----
    declared_grains: Tuple[str, ...] = ()   # tool_grain_calibration operating grains
    kind: str = "surface"                   # "surface" | "seam" | "meta"
    routable: bool = True                   # a routing target vs present-for-completeness
    write_path: bool = False                # E1 (DR3, ~B-tagged): a genuine WRITE-PATH tool (rebuild/derive/
    #                                         write, e.g. comp-aws-derive/comp-build) -> EXCLUDED from a
    #                                         read/navigate intent by DR1 route()'s Stage-A. read-recompute
    #                                         (default) stays write_path=False. The engine reads cap.write_path.


class CapabilityMapProvider:
    """
    The provider INTERFACE (PRD section 3). A concrete provider exposes:

      capabilities() -> list[Capability]           the full capability set
      surface_prior(surface_or_key, ctx) -> float  the role->surface additive prior
      affinity_key(cap) -> str                     the PRIOR (surface) key; the LEARNED term keys by cap.id (per-cap-id)

    L3's engine codes to THIS (never to a concrete map) so any Stage-2 provider
    slots in unchanged. Subclasses / duck-typed implementations both satisfy it.
    """

    def capabilities(self) -> List[Capability]:
        raise NotImplementedError

    def surface_prior(self, surface_or_key: str, ctx: Optional[Mapping[str, Any]]) -> float:
        raise NotImplementedError

    def affinity_key(self, cap: Capability) -> str:
        return cap.affinity_key


def _normalize_affinity_key(surface: Optional[str]) -> str:
    """Map a raw home (surface-id | seam-id | 'META') to the affinity-table key."""
    if not surface:
        return META_KEY
    s = str(surface)
    if s.lower().startswith("seam"):
        return SEAM_KEY
    if s in SURFACE_KEYS:
        return s
    if s == META_KEY:
        return META_KEY
    # An unrecognized surface: neutral bucket (never crash the scorer; cold-start-safe).
    return s


def _tokenize(text: str) -> List[str]:
    return [t for t in re.split(r"[^a-z0-9]+", (text or "").lower()) if t]


def _keywords(
    tool_id: str,
    concern: str,
    touches_resource: Iterable[str],
    grain: str,
    surface: str,
    extra: Iterable[str] = (),
) -> Tuple[str, ...]:
    """Derive the query_match bag-of-words from map-carried fields (section-3 'description=keywords')."""
    toks: List[str] = []
    # tool id + its distinctive suffix (drop the "comp" prefix noise)
    toks.append((tool_id or "").lower())
    toks.extend(_tokenize(tool_id))
    # the concern is the natural-language description of what the tool answers
    toks.extend(_tokenize(concern))
    # named resources + grain + surface are strong routing signals
    for r in touches_resource or ():
        toks.extend(_tokenize(str(r)))
    toks.extend(_tokenize(grain))
    toks.extend(_tokenize(surface))
    for e in extra or ():
        toks.extend(_tokenize(str(e)))
    seen: List[str] = []
    for t in toks:
        if len(t) >= 2 and t not in _STOPWORDS and t not in seen:
            seen.append(t)
    return tuple(seen)


def _grains_for(tool_id: str, grain_map: Mapping[str, Any], fallback: str) -> Tuple[str, ...]:
    declared = grain_map.get(tool_id)
    if declared:
        return tuple(str(g) for g in declared)
    return (fallback,) if fallback else ()


def _build_capabilities(m: Mapping[str, Any]) -> List[Capability]:
    """Project the COMPUNIFY map (tools[] + meta_tools[]) into Capability records."""
    grain_map = ((m.get("tool_grain_calibration") or {}).get("tool_grain_map")) or {}
    write_path_tools = _load_write_path_tools()   # E1: whole-write tools (~B DR3 manifest tags), read-excluded
    caps: List[Capability] = []

    # ---- surface / seam-homed inspection tools (the routing targets) ----
    for t in m.get("tools") or ():
        tool_id = t.get("tool")
        if not tool_id:
            continue
        seam = t.get("seam")
        surface_field = t.get("surface")
        if seam:
            surface = str(seam)
            kind = "seam"
        else:
            surface = str(surface_field) if surface_field else META_KEY
            kind = "surface"
        grain = str(t.get("granularity") or "")
        concern = str(t.get("concern") or "")
        touches = t.get("touches_resource") or []
        affinity_key = _normalize_affinity_key(surface)
        caps.append(
            Capability(
                id=tool_id,
                keywords=_keywords(tool_id, concern, touches, grain, surface),
                surface=surface,
                grain=grain,
                concern=concern,
                affinity_key=affinity_key,
                declared_grains=_grains_for(tool_id, grain_map, grain),
                kind=kind,
                routable=True,
                write_path=(tool_id in write_path_tools),
            )
        )

    # ---- the tooling layer (accounted for COMPLETENESS; never silently dropped) ----
    for mt in m.get("meta_tools") or ():
        tool_id = mt.get("tool")
        if not tool_id:
            continue
        role = str(mt.get("role") or "")
        concern = str(mt.get("concern") or mt.get("not_homed_reason") or role or "")
        declared = mt.get("declared_grain") or []
        grain = str(declared[0]) if declared else "meta"
        caps.append(
            Capability(
                id=tool_id,
                keywords=_keywords(tool_id, concern, [], grain, META_KEY, extra=[role]),
                surface=META_KEY,
                grain=grain,
                concern=concern,
                affinity_key=META_KEY,
                declared_grains=tuple(str(g) for g in declared) if declared else (),
                kind="meta",
                # DECLARED routability wins (comp-coverage-map.yaml `routable:` per entry, NFRA_COMPCLOSE);
                # the role allowlist is the fallback for entries that omit the key -- never the primary,
                # because an unlisted role silently dropped real query tools from the candidate set.
                routable=(bool(mt["routable"]) if "routable" in mt
                          else role in _ROUTABLE_META_ROLES),
                write_path=(tool_id in write_path_tools),
            )
        )

    return caps


class ComptoolCapabilityMapProvider(CapabilityMapProvider):
    """The FIRST provider (PRD section 3): the comp-tool capability map from COMPUNIFY."""

    def __init__(self, map_path: Optional[str] = None):
        self.map_path = map_path or DEFAULT_MAP_PATH
        with open(self.map_path, "r", encoding="utf-8") as fh:
            self._map = yaml.safe_load(fh) or {}
        self._caps = _build_capabilities(self._map)
        self._by_id = {c.id: c for c in self._caps}
        self._affinity = self._map.get("role_surface_affinity") or {}

    # ---- the section-3 interface ----
    def capabilities(self) -> List[Capability]:
        return list(self._caps)

    def surface_prior(self, surface_or_key: str, ctx: Optional[Mapping[str, Any]]) -> float:
        """role_surface_affinity lookup. ADDITIVE prior (never a filter); cold-start -> default."""
        key = _normalize_affinity_key(surface_or_key)
        table = self._affinity or {}
        default = float(table.get("default_prior", 0.0))
        role = (ctx or {}).get("role")
        by_role = table.get("by_role") or {}
        if role and role in by_role:
            return float((by_role[role] or {}).get(key, default))
        return default

    def affinity_key(self, cap: Capability) -> str:
        return cap.affinity_key

    # ---- convenience (not part of the binding interface) ----
    def capability(self, tool_id: str) -> Optional[Capability]:
        return self._by_id.get(tool_id)

    def routable_capabilities(self) -> List[Capability]:
        return [c for c in self._caps if c.routable]

    @property
    def role_surface_affinity(self) -> Mapping[str, Any]:
        return self._affinity


class SmokeCapabilityMapProvider(CapabilityMapProvider):
    """
    A second, DIFFERENT-domain provider implementing the SAME interface -- the
    PRD section-9c generalization proof (a Stage-2 provider slots in unchanged).
    Two hardcoded capabilities from a non-comp-tool domain (skills), zero COMPUNIFY.
    """

    _CAPS = (
        Capability(
            id="skill:deck-gen",
            keywords=("deck", "slides", "pptx", "presentation", "powerpoint"),
            surface="SKILLS",
            grain="artifact",
            concern="generate a brand-compliant Opal PowerPoint from a deck prompt",
            affinity_key="SKILLS",
            declared_grains=("artifact",),
            kind="surface",
            routable=True,
        ),
        Capability(
            id="skill:find",
            keywords=("find", "leads", "prospects", "agencies", "dualbiz"),
            surface="SKILLS",
            grain="record",
            concern="surface dual-business insurance producing-agency leads by case and geography",
            affinity_key="SKILLS",
            declared_grains=("record",),
            kind="surface",
            routable=True,
        ),
    )

    def __init__(self, affinity: Optional[Mapping[str, Any]] = None):
        self._affinity = affinity or {"default_prior": 0.0, "by_role": {}}

    def capabilities(self) -> List[Capability]:
        return list(self._CAPS)

    def surface_prior(self, surface_or_key: str, ctx: Optional[Mapping[str, Any]]) -> float:
        table = self._affinity or {}
        default = float(table.get("default_prior", 0.0))
        role = (ctx or {}).get("role")
        by_role = table.get("by_role") or {}
        if role and role in by_role:
            return float((by_role[role] or {}).get(surface_or_key, default))
        return default


def get_provider(map_path: Optional[str] = None) -> ComptoolCapabilityMapProvider:
    """Factory for the default (comp-tool) provider."""
    return ComptoolCapabilityMapProvider(map_path=map_path)


# ---------------------------------------------------------------------------
# Phase-3 conformance smoke-consumer (mandate phase-3 / acceptance criterion 3).
# Runs `python comp_capability_provider.py` -> asserts every record carries all six
# section-3 fields populated, the role->surface_affinity table is present +
# queryable, and a SECOND provider satisfies the SAME interface (generalization).
# ---------------------------------------------------------------------------
def _conformance(provider: CapabilityMapProvider, ctx: Optional[Mapping[str, Any]]) -> List[str]:
    """A provider-agnostic smoke-consumer. Returns a list of failure strings (empty = PASS)."""
    fails: List[str] = []
    caps = provider.capabilities()
    if not caps:
        fails.append("provider returned ZERO capabilities")
    six = ("id", "keywords", "surface", "grain", "concern", "affinity_key")
    for c in caps:
        for field in six:
            val = getattr(c, field, None)
            if val is None or (isinstance(val, str) and not val.strip()) or (field == "keywords" and not val):
                fails.append("capability %r missing/empty section-3 field %r" % (getattr(c, "id", "?"), field))
        # surface_prior must return a float and NEVER raise (PRIOR-not-FILTER, cold-start-safe)
        try:
            prior = provider.surface_prior(c.affinity_key, ctx)
            float(prior)
        except Exception as e:  # noqa: BLE001 - conformance surfaces any prior failure
            fails.append("surface_prior(%r) raised: %s" % (c.affinity_key, e))
    return fails


def _main() -> int:
    import json

    print("== NFRA_COMPROUTE L2 -- capability-map provider conformance ==")
    prov = get_provider()
    caps = prov.capabilities()
    routable = prov.routable_capabilities()
    print("capabilities: %d total, %d routable" % (len(caps), len(routable)))

    # 1) section-3 six-field conformance (with a role ctx to exercise the prior)
    ctx = {"role": "DE", "working_set": [], "trajectory": []}
    fails = _conformance(prov, ctx)

    # 2) role_surface_affinity present + queryable
    aff = prov.role_surface_affinity
    if not aff or not aff.get("by_role"):
        fails.append("role_surface_affinity table absent or empty (governor ADD missing)")
    else:
        # exercise a known seed prior; DE should carry an AWS-CLOUD affinity > 0
        p = prov.surface_prior("AWS-CLOUD", {"role": "DE"})
        print("surface_prior(AWS-CLOUD, role=DE) = %s" % p)
        if p <= 0.0:
            fails.append("seed prior surface_prior(AWS-CLOUD, DE) should be > 0 (LD-0231 cold-start seed)")
        # cold-start / unknown role -> neutral default, never a crash
        p0 = prov.surface_prior("AWS-CLOUD", {"role": "NOSUCHROLE"})
        print("surface_prior(AWS-CLOUD, role=UNKNOWN) = %s (cold-start neutral)" % p0)

    # 3) generalization: a SECOND provider satisfies the SAME interface unchanged
    smoke = SmokeCapabilityMapProvider()
    smoke_fails = _conformance(smoke, {"role": "DE"})
    if smoke_fails:
        fails.extend("smoke-provider: " + f for f in smoke_fails)
    else:
        print("generalization: SmokeCapabilityMapProvider (%d caps) conforms to the SAME interface -- OK"
              % len(smoke.capabilities()))

    # a small sample for the record
    sample = [
        {"id": c.id, "surface": c.surface, "grain": c.grain, "affinity_key": c.affinity_key,
         "n_keywords": len(c.keywords)}
        for c in caps[:3]
    ]
    print("sample: " + json.dumps(sample))

    if fails:
        print("CONFORMANCE FAIL (%d):" % len(fails))
        for f in fails:
            print("  - " + f)
        return 1
    print("CONFORMANCE PASS: all %d capabilities carry the six section-3 fields; "
          "role_surface_affinity present + queryable; generalization interface proven." % len(caps))
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(_main())
