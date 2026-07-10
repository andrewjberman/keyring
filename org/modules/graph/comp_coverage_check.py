"""comp_coverage_check.py -- THE GATE (NFRA_COMPUNIFY S2, CTO ruling #4).

The machine-checkable non-redundancy invariant AS ENFORCEMENT. Reads the source-of-truth
ledger org/modules/graph/comp-coverage-map.yaml and FAILS when the map drifts from the
territory -- so the COMPUNIFY taxonomy stays true by gate, not by prose.

DESIGN (CTO S0/S1 ruling): the ledger's own `schema.gate_contract.rules` IS this gate's SPEC.
comp-coverage-check ENUMERATES those rule ids and dispatches each to its checker -- it does NOT
carry a parallel hand-written rule-set. A contract rule with NO checker here => UNVERIFIABLE
(a finding), never a silent PASS (the never-false-clean discipline). Rules enforced:
  one_home / seam_reference_integrity / declared_non_redundancy / coverage_single_home /
  no_trino_phantom_seam / inventory_completeness
PLUS (CTO regeneration-ownership ruling, AC5): PROJECTION-CURRENCY -- the manifest tools_index
must be a CURRENT projection of the ledger union (comp_coverage_view --verify); a stale
projection FAILS. Regeneration (emit -> writes the manifest) is an EXEC/CI step, NOT inline here
(the manifest is exec-controlled; inline regen would be an SoD break) -- this gate only ASSERTS
currency, it never writes the manifest.

Tri-state, honest (mirrors the comp-rail):
  exit 0 PASS         -- every tool one home, every overlap declared, projection current
  exit 1 FAIL         -- an unplaced tool / silent overlap / phantom seam / stale projection /
                         incomplete inventory (the offending node is NAMED)
  exit 2 UNVERIFIABLE  -- could-not-read the ledger, OR a contract rule has no checker (a finding)

Usage:
  comp-coverage-check [check]   # gate the live ledger (default)
  comp-coverage-check selfcheck # inject unplaced-tool + silent-overlap + stale-projection -> each FAILS, clean PASSes
  comp-coverage-check list      # the contract rules this gate enforces
"""

from __future__ import annotations

import copy
import json
import os
import sys
from collections import defaultdict

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comp_coverage_view  # noqa: E402 -- sibling module; the single source of the projection-currency check

_HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(_HERE, "comp-coverage-map.yaml")
SEAM_SOURCE = os.path.join(_HERE, "drift-topology.yaml")
MANIFEST = os.path.join(_HERE, "graph-call-manifest.yaml")
TOOLS_DIR = os.path.normpath(os.path.join(_HERE, "..", "..", "..", ".tools"))

PASS, FAIL, UNVERIFIABLE = 0, 1, 2


# ----------------------------------------------------------------------------- helpers
def _load(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def _homes(tool: dict) -> list[str]:
    return [k for k in ("surface", "seam") if tool.get(k)]


def _seam_ids(seam_source: dict) -> set[str]:
    return {s["seam_id"] for s in seam_source.get("seams", [])}


def _tool_name(fname: str) -> str:
    base = fname.rsplit(".", 1)[0] if "." in fname else fname
    return base if (base.startswith("comp-") or base == "pipescript") else ""


def _tools_dir_inventory() -> set[str]:
    """WORKING-TREE universe -- every comp-* file on disk, tracked or not.

    CORRECT for the OPERATOR question ("is the map consistent right now, including my uncommitted
    work"). WRONG as a commit-time signal: we share one worktree, so this also sees OTHER agents'
    untracked, mid-authoring files. That is how comp-denytest and comp-firmsep-sweep red-bannered
    every agent on 2026-07-09 for files that existed in no commit -- a fabric-wide FAIL caused by
    work nobody had committed. Use _committed_tools_inventory() for any gate. (CTO ruling 094435Z.)
    """
    inv: set[str] = set()
    if not os.path.isdir(TOOLS_DIR):
        return inv
    for f in os.listdir(TOOLS_DIR):
        t = _tool_name(f)
        if t:
            inv.add(t)
    return inv


def _committed_tools_inventory() -> set[str]:
    """COMMITTING-TREE universe -- only comp-* files git actually tracks.

    Structurally excludes another agent's untracked scratch file, so a gate built on this can never
    block agent B for agent A's work-in-progress. Falls back to the working tree if git is
    unavailable -- a fallback that can only ever be MORE inclusive, never silently narrower.
    """
    import subprocess
    try:
        out = subprocess.run(["git", "ls-files", ".tools"], capture_output=True,
                             cwd=os.path.dirname(TOOLS_DIR)).stdout
        names = out.decode("utf-8", "replace").split("\n")
    except Exception:
        return _tools_dir_inventory()
    inv: set[str] = set()
    for raw in names:
        rel = raw.strip().replace("\\", "/")
        if not rel.startswith(".tools/"):
            continue
        tail = rel[len(".tools/"):]
        if "/" in tail:
            continue  # TOP-LEVEL ONLY -- mirror os.listdir; .tools/hooks/comp-tool-hud.sh is a
            # hook, not a comp-tool, and counting it made the gate universe WIDER than the
            # operator's (it flagged comp-tool-hud as UNPLACED). Caught by the side-by-side test.
        t = _tool_name(tail)
        if t:
            inv.add(t)
    return inv or _tools_dir_inventory()


# ----------------------------------------------------------------------------- rule checkers
# Each returns a list of violation strings (empty list = clean). Keyed by the contract rule id.
def _check_one_home(led: dict, **_: object) -> list[str]:
    out = []
    for t in led.get("tools", []):
        h = _homes(t)
        if len(h) != 1:
            out.append(f"one_home: tool '{t.get('tool')}' has {len(h)} homes {h} (need exactly 1 surface|seam)")
        if not t.get("granularity"):
            out.append(f"one_home: tool '{t.get('tool')}' missing granularity")
        if not t.get("concern"):
            out.append(f"one_home: tool '{t.get('tool')}' missing concern")
    return out


def _check_seam_reference_integrity(led: dict, seam_source: dict, **_: object) -> list[str]:
    valid = _seam_ids(seam_source)
    out = []
    for t in led.get("tools", []):
        sid = t.get("seam")
        if sid and sid not in valid:
            out.append(f"seam_reference_integrity: tool '{t.get('tool')}' references seam '{sid}' absent from drift-topology.yaml")
    for a in led.get("seams", {}).get("axis", []):
        if a.get("seam_id") not in valid:
            out.append(f"seam_reference_integrity: axis seam '{a.get('seam_id')}' absent from drift-topology.yaml")
    return out


def _check_declared_non_redundancy(led: dict, **_: object) -> list[str]:
    groups: dict[str, list[dict]] = {}
    for t in led.get("tools", []):
        for r in t.get("touches_resource", []):
            groups.setdefault(r, []).append(t)
    out = []
    for res, tools in groups.items():
        if len(tools) < 2:
            continue
        concerns = [t.get("concern") for t in tools]
        if len(set(concerns)) != len(concerns):
            out.append(f"declared_non_redundancy: resource '{res}' -- CONCERN COLLISION (true redundancy) among {[t['tool'] for t in tools]}")
        for t in tools:
            declared = {x.get("tool") for x in t.get("distinct_from", []) if x.get("shared_resource") == res}
            others = {o["tool"] for o in tools if o is not t}
            missing = others - declared
            if missing:
                out.append(f"declared_non_redundancy: tool '{t['tool']}' shares '{res}' with {sorted(missing)} WITHOUT a declared distinct_from (silent overlap)")
    return out


def _check_coverage_single_home(led: dict, **_: object) -> list[str]:
    out = []
    for a in led.get("seams", {}).get("axis", []):
        if "coverage" in a:
            out.append(f"coverage_single_home: axis '{a.get('seam_id')}' stores a 'coverage' copy (must be READ from coverage_source)")
    return out


def _check_no_trino_phantom_seam(led: dict, **_: object) -> list[str]:
    tf = led.get("trino_federation", {})
    out = []
    if tf.get("fan_in_model") != "physical-catalog":
        out.append(f"no_trino_phantom_seam: fan_in_model is '{tf.get('fan_in_model')}' (must be 'physical-catalog')")
    for c in tf.get("catalogs", []):
        if c.get("name") in ("aws", "portal", "ms"):
            out.append(f"no_trino_phantom_seam: phantom per-layer catalog '{c.get('name')}' (layer is a graph_nodes COLUMN)")
    return out


# TWO CONSUMERS, TWO UNIVERSES (CTO 094435Z + COO~B 095352Z: parameterise, do not fork the tool).
# The operator asks "is the map consistent RIGHT NOW, including my uncommitted work" -> working
# tree. A GATE asks "does this COMMIT leave the map consistent" -> committing tree. Same rule,
# different universe. Set by check(universe=...); an explicit `inventory=` argument still wins.
_INVENTORY_OVERRIDE: set[str] | None = None


def _check_inventory_completeness(led: dict, inventory: set[str] | None = None, **_: object) -> list[str]:
    if inventory is not None:
        inv = inventory
    else:
        inv = _INVENTORY_OVERRIDE if _INVENTORY_OVERRIDE is not None else _tools_dir_inventory()
    if not inv:
        return ["inventory_completeness: UNVERIFIABLE -- could not enumerate .tools/ inventory"]
    homed = {t["tool"] for t in led.get("tools", [])}
    meta = {m["tool"] for m in led.get("meta_tools", [])}
    union = homed | meta
    out = []
    for t in sorted(inv - union):
        out.append(f"inventory_completeness: tool '{t}' is UNPLACED (in neither tools[] nor meta_tools[] -- silently dropped)")
    for t in sorted(homed & meta):
        out.append(f"inventory_completeness: tool '{t}' is DOUBLE-PLACED (both homed and meta)")
    return out


def _check_stable_grain(led: dict, **_: object) -> list[str]:
    """The cross-macro stable-grain contract (CTO amendments 8+9; COMPUNIFY governs, GRAPHUNI
    populates, COMPDRIFT seams on). EXTENSIBLE: the pending fractal-§10 drilldown/rollup rules
    fold in as NEW rule entries + checkers, never an engine refactor."""
    gc = led.get("grain_contract")
    if not gc:
        return ["stable_grain: grain_contract section absent (the cross-macro stable-grain contract must be declared)"]
    out = []
    ets = gc.get("edge_types", [])
    ladder_levels = set(gc.get("node_grain_ladder", {}).get("levels", []))
    names = {e.get("edge_type") for e in ets}
    by_relation: dict[str, list[str]] = {}
    for e in ets:
        et, rel = e.get("edge_type"), e.get("relation")
        if not e.get("levels"):
            out.append(f"stable_grain: edge_type '{et}' declares no `levels` attribute (grain must be a declared attribute, not encoded in the type name)")
        by_relation.setdefault(rel, []).append(et)
    # (a) each relation -> exactly ONE edge_type (a relation split across types = per-depth re-typing)
    for rel, types in by_relation.items():
        if len(types) > 1:
            out.append(f"stable_grain: relation '{rel}' is split across {sorted(types)} -- per-depth re-typing; use ONE edge_type + a `level` attribute (Amendment 2)")
    # (c) no edge_type NAME = another type's name + a grain-level token (name-encoded re-typing)
    _grain_suffixes = ladder_levels | {"l1", "l2", "deep", "shallow", "fine", "coarse"}
    for et in names:
        for other in names:
            if et != other and et.startswith(other + "_") and et[len(other) + 1:].lower() in _grain_suffixes:
                out.append(f"stable_grain: edge_type '{et}' name-encodes a grain level over '{other}' (per-depth re-typing) -- carry the depth as a `level` attribute on '{other}'")
    return out


def _check_grain_drilldown_seams(led: dict, **_: object) -> list[str]:
    """FRACTAL DRILLDOWN-SEAM stability (CTO sec-10). Each stratum-stitching edge must be a stable
    declared edge_type (carrying a `levels` attr) bridging two DECLARED strata. Empty when the
    fractal model is not yet populated -> PASS (gate-ready-ahead-of-need)."""
    gc = led.get("grain_contract", {})
    seams = gc.get("drilldown_seams", [])
    if not seams:
        return []  # fractal not populated yet -- the gate is ready, fires when ~D populates
    strata = set(gc.get("strata", []))
    et_index = {e.get("edge_type"): e for e in gc.get("edge_types", [])}
    out = []
    for s in seams:
        et = s.get("edge_type")
        if et not in et_index:
            out.append(f"grain_drilldown_seams: seam edge_type '{et}' is not a declared stable edge_type (a drilldown edge must be a stable type)")
        elif not et_index[et].get("levels"):
            out.append(f"grain_drilldown_seams: seam edge_type '{et}' carries no `levels` (grain must be a declared attribute)")
        for k in ("from_stratum", "to_stratum"):
            if s.get(k) not in strata:
                out.append(f"grain_drilldown_seams: seam '{et}' {k}='{s.get(k)}' is not a declared stratum {sorted(strata)}")
    return out


def _check_grain_rollup_consistency(led: dict, **_: object) -> list[str]:
    """GRAIN-CONSISTENCY ROLLUP contract (CTO sec-10, EXISTENTIAL-AGGREGATION 047ce51d0). Contract-
    level (type) check: existential semantics declared, BOTH defect classes present, rollup_via edges
    are declared types. The INSTANCE-level existential check runs via rollup_defects() on populated
    edges. Empty when fractal not yet populated -> PASS."""
    gc = led.get("grain_contract", {})
    rollup = gc.get("rollup")
    if not rollup and not gc.get("drilldown_seams"):
        return []
    if not rollup:
        return ["grain_rollup_consistency: drilldown_seams present but no `rollup` contract declared"]
    out = []
    if rollup.get("semantics") != "existential-aggregation":
        out.append(f"grain_rollup_consistency: rollup.semantics must be 'existential-aggregation' (CTO 047ce51d0, NOT 1:1 equality), got '{rollup.get('semantics')}'")
    declared = {d.get("id") for d in rollup.get("defect_classes", [])}
    for required in ("UNSUPPORTED", "COARSE-INCOMPLETE"):
        if required not in declared:
            out.append(f"grain_rollup_consistency: defect_class '{required}' not declared (the existential semantics requires both)")
    et_names = {e.get("edge_type") for e in gc.get("edge_types", [])}
    for rv in rollup.get("rollup_via", []):
        if rv not in et_names:
            out.append(f"grain_rollup_consistency: rollup_via edge '{rv}' is not a declared edge_type")
    return out


def _check_producer_attribution(led: dict, **_: object) -> list[str]:
    """DENOMINATOR completeness (COO~B/CTO): every edge_type must carry a producer disposition
    (scalar `producer` OR a `producer_by_pair` map). An unattributed type = a silent denominator gap."""
    out = []
    for e in led.get("grain_contract", {}).get("edge_types", []):
        if not e.get("producer") and not e.get("producer_by_pair"):
            out.append(f"producer_attribution: edge_type '{e.get('edge_type')}' has NO producer disposition (scalar `producer` or `producer_by_pair`) -- a silent gap in the denominator universe")
    return out


_DISPOSITIONS = {"eager", "bounded", "n_a"}


def _check_disposition_complete(led: dict, **_: object) -> list[str]:
    """EXPLICIT-DISPOSITION completeness (COO~B ruling). Every (edge_type x declared-level) must carry
    an explicit disposition in {eager, bounded, n_a}. An undisposed level = a SILENT cap = FAIL."""
    gc = led.get("grain_contract", {})
    disp = gc.get("level_dispositions", {})
    if not disp:
        return []  # not declared yet -> nothing to check (gate-ready ahead of need)
    out = []
    for e in gc.get("edge_types", []):
        et = e.get("edge_type")
        et_disp = disp.get(et, {})
        for lvl in e.get("levels", []):
            d = et_disp.get(lvl)
            if d is None:
                out.append(f"disposition_complete: edge_type '{et}' level '{lvl}' is UNDISPOSED (no eager/bounded/n_a) -- a silent cap; declare its policy")
            elif d not in _DISPOSITIONS:
                out.append(f"disposition_complete: edge_type '{et}' level '{lvl}' disposition '{d}' is not one of {sorted(_DISPOSITIONS)}")
    return out


def _check_referenceable_target(led: dict, **_: object) -> list[str]:
    """REFERENCEABLE-TARGET contract (GRAPHDEPTH invariant 5, EP-2-keyed). Breadth edges may only
    target referenceable nodes, never terminal members. KEYED by edge_type. Contract-level check;
    the instance-level (a populated breadth edge's target node_type) runs in the seam MECHANICAL axis."""
    ref = led.get("grain_contract", {}).get("referenceable")
    if not ref:
        return []  # not declared yet -> nothing to check (gate-ready ahead of need)
    out = []
    node_types = set(ref.get("node_types", []))
    terminal = set(ref.get("terminal_node_types", []))
    targets = ref.get("referenceable_targets", {})
    overlap = node_types & terminal
    if overlap:
        out.append(f"referenceable_target: node_types and terminal_node_types OVERLAP on {sorted(overlap)} (a type cannot be both referenceable and terminal)")
    for be in ref.get("breadth_edges", []):
        if be not in targets:
            out.append(f"referenceable_target: breadth edge_type '{be}' has NO referenceable_targets entry (keyed-by-edge_type map must cover every breadth edge)")
            continue
        for tgt in targets[be]:
            if tgt in terminal:
                out.append(f"referenceable_target: '{be}' allows TERMINAL target '{tgt}' (breadth edges must NEVER target a terminal member)")
            elif tgt not in node_types:
                out.append(f"referenceable_target: '{be}' allows '{tgt}' which is not a declared referenceable node_type")
    return out


def _edge_type_producers(et_def: dict) -> set:
    """The producer set for an edge_type: a scalar producer -> {it}; a producer_by_pair map (multi-
    producer, e.g. CONTAINS) -> the set of its values."""
    if et_def.get("producer_by_pair"):
        return set(et_def["producer_by_pair"].values())
    return {et_def["producer"]} if et_def.get("producer") else set()


def rollup_defects(coarse_edges, fine_edges, rolls_up):
    """THE CANONICAL existential-aggregation rollup check (CTO 047ce51d0) -- the ONE head GRAPHUNI's
    derive + COMPDRIFT's seam call against POPULATED edges (so the 1:1-vs-existential drift cannot
    recur). A coarse edge EXISTS iff >=1 fine edge rolls up to it (OR-rollup).
      coarse_edges : iterable of (src, dst) at the coarse stratum
      fine_edges   : iterable of (src, dst) at the fine stratum
      rolls_up     : dict mapping a fine node -> the coarse node it rolls up to (via RUNS/CONTAINS/OWNED_BY)
    Returns [(defect_class, edge)]: UNSUPPORTED (coarse, zero fine basis) + COARSE-INCOMPLETE (fine, coarse absent)."""
    coarse = set(map(tuple, coarse_edges))
    implied = set()
    for fs, fd in fine_edges:
        cs, cd = rolls_up.get(fs), rolls_up.get(fd)
        if cs is not None and cd is not None:
            implied.add((cs, cd))
    defects = [("UNSUPPORTED", ce) for ce in sorted(coarse - implied)]
    defects += [("COARSE-INCOMPLETE", ie) for ie in sorted(implied - coarse)]
    return defects


def seam_validate(led: dict, edges: list, rollup_view: dict | None, scope: dict | None = None, producer: str | None = None):
    """The 3-axis govern<->populate SEAM validation (Andrew-direct symbiotic protocol). Validates
    ~D's POPULATED edges against the grain_contract registry (~C governs) at the CATEGORICAL bar,
    SCOPE- and PRODUCER-aware (~D pre-flight findings 2+3) so phased tiers + cross-lane grains are
    not false STOPs. Returns {mechanical, in_scope_gap, phased_pending, cross_lane, semantic}.

    INTERFACE (the contract ~D emits to):
      edges       = [{edge_type, level, from_stratum, to_stratum}, ...]   (one per populated edge)
      rollup_view = {"coarse": [[src,dst],...], "fine": [[src,dst],...], "rolls_up": {node: coarse_node}}
      scope       = {"edge_types": [...], "strata": [...]}   (the grains THIS increment CLAIMS to cover;
                    out-of-scope registry grains = phased-pending, expected, not a STOP. None = full bar.)
      producer    = the lane under validation (e.g. 'graphuni-gold'); a registry type owned by ANOTHER
                    producer is CROSS-LANE (not this increment's gap). None = all producers in scope.
    """
    gc = led.get("grain_contract", {})
    et_index = {e["edge_type"]: e for e in gc.get("edge_types", [])}
    registry_types = set(et_index)
    strata = set(gc.get("strata", []))
    scope_types = set(scope.get("edge_types", [])) if scope and scope.get("edge_types") is not None else None
    scope_strata = set(scope.get("strata", [])) if scope and scope.get("strata") is not None else None
    scope_levels = scope.get("levels", {}) if scope else {}   # {edge_type: [claimed levels]} -- level-granular scope (~D finding 2)
    ref = gc.get("referenceable", {})                         # GRAPHDEPTH invariant 5: breadth-edge target check (EP-2-keyed)
    ref_targets = ref.get("referenceable_targets", {})
    ref_terminal = set(ref.get("terminal_node_types", []))
    level_dispositions = gc.get("level_dispositions", {})     # COO~B ruling: eager(must-cover)|bounded(lazy)|n_a -- bounded/n_a not gaps
    mechanical, in_scope_gap, phased_pending, cross_lane = [], [], [], []
    populated_types: set = set()
    populated_levels: dict = defaultdict(set)
    populated_strata: set = set()

    # --- AXIS 1: MECHANICAL -- every populated edge conforms to the registry ---
    for e in edges:
        et, lvl = e.get("edge_type"), e.get("level")
        populated_types.add(et)
        if et not in registry_types:
            mechanical.append(f"populated edge_type '{et}' ABSENT from registry (population-orphan -- govern must add it or ~D mis-typed)")
        elif lvl is not None and lvl not in et_index[et].get("levels", []):
            mechanical.append(f"edge '{et}' level '{lvl}' not in declared levels {et_index[et].get('levels')}")
        if et in registry_types and lvl is not None:
            populated_levels[et].add(lvl)
        for k in ("from_stratum", "to_stratum"):
            s = e.get(k)
            if s is not None:
                populated_strata.add(s)
                if s not in strata:
                    mechanical.append(f"edge '{et}' {k}='{s}' is not a declared stratum {sorted(strata)}")
        tnt = e.get("target_node_type")                       # GRAPHDEPTH inv 5: a breadth edge must target a referenceable node, never a terminal
        if et in ref_targets and tnt is not None and tnt not in ref_targets[et]:
            kind = "TERMINAL" if tnt in ref_terminal else "non-referenceable"
            mechanical.append(f"breadth edge '{et}' targets {kind} node_type '{tnt}' (allowed: {ref_targets[et]}) -- breadth edge on a non-referenceable target")

    # --- AXIS 2: DECLARATIVE -- registry<->population coverage, SCOPE + PRODUCER aware ---
    for et in sorted(registry_types):
        et_producers = _edge_type_producers(et_index[et])               # set: scalar -> {it}; producer_by_pair -> its values (multi-producer, e.g. CONTAINS)
        if producer and et_producers and producer not in et_producers:  # another lane's grain (not among this type's producers)
            tag = sorted(et_producers)[0] if len(et_producers) == 1 else sorted(et_producers)
            cross_lane.append(f"'{et}' (producer={tag}) -- not {producer}'s grain; another lane populates it")
            continue
        if scope_types is not None and et not in scope_types:            # out of this increment's claim
            if et not in populated_types:
                phased_pending.append(f"'{et}' -- declared, OUT of this increment's claimed scope (phased; a later tier)")
            continue
        if et not in populated_types:                                    # claimed (or full-bar) but unpopulated
            in_scope_gap.append(f"edge_type '{et}' in scope but ZERO populated edges")
        else:                                                            # LEVEL-granular + DISPOSITION-aware (COO~B ruling)
            declared = set(et_index[et].get("levels", []))
            et_disp = level_dispositions.get(et, {})
            claimed = set(scope_levels[et]) if et in scope_levels else declared
            for lvl in sorted(claimed - populated_levels.get(et, set())):
                d = et_disp.get(lvl)
                if d in ("bounded", "n_a"):                              # boundary b/c: declared lazy/absent -> NOT a gap
                    phased_pending.append(f"edge_type '{et}' level '{lvl}' -- disposition={d} (lazy/absent, declared), covered-when-materialized, not a gap")
                else:                                                    # eager (must cover) or UNDISPOSED (the disposition_complete gate FAILs that separately)
                    in_scope_gap.append(f"edge_type '{et}' level '{lvl}' (disposition={d or 'UNDISPOSED'}) in scope but NOT populated")
            for lvl in sorted(declared - claimed):
                phased_pending.append(f"edge_type '{et}' level '{lvl}' -- OUT of claimed scope (phased)")
    check_strata = scope_strata if scope_strata is not None else strata
    for st in sorted(set(check_strata) - populated_strata):
        in_scope_gap.append(f"stratum '{st}' in scope but ZERO populated edges")
    if scope_strata is not None:
        for st in sorted(strata - scope_strata - populated_strata):
            phased_pending.append(f"stratum '{st}' -- OUT of claimed scope (phased)")

    # --- AXIS 3: SEMANTIC -- existential rollup holds on the REAL edges (one head) ---
    if rollup_view is None:
        semantic = ["SEMANTIC axis NOT PROVIDED -- supply rollup_view {coarse, fine, rolls_up} to validate existential rollup"]
    else:
        semantic = [f"{cls}: {edge}" for cls, edge in rollup_defects(rollup_view.get("coarse", []), rollup_view.get("fine", []), rollup_view.get("rolls_up", {}))]

    return {"mechanical": mechanical, "in_scope_gap": in_scope_gap, "phased_pending": phased_pending,
            "cross_lane": cross_lane, "semantic": semantic}


def seam(edges_path: str, rollup_path: str | None, scope_path: str | None = None, producer: str | None = None) -> int:
    """CLI: scope/producer-aware 3-axis seam validation. Exit 0 GREEN (clean within claimed scope --
    proceed; phased/cross-lane reported as expected) / 1 RED (mechanical or semantic defect -- STOP) /
    2 IN-SCOPE-INCOMPLETE (claimed scope not fully covered, or semantic not supplied -- reconcile)."""
    try:
        led = _load(LEDGER)
        with open(edges_path, encoding="utf-8") as fh:
            edges = json.load(fh)
        rollup_view = json.load(open(rollup_path, encoding="utf-8")) if rollup_path else None
        scope = json.load(open(scope_path, encoding="utf-8")) if scope_path else None
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write(f"UNVERIFIABLE: could not read ledger/edges/rollup/scope: {exc}\n")
        return UNVERIFIABLE
    r = seam_validate(led, edges, rollup_view, scope=scope, producer=producer)
    labels = [("mechanical", "MECHANICAL"), ("in_scope_gap", "DECLARATIVE/in-scope-gap"),
              ("phased_pending", "DECLARATIVE/phased-pending"), ("cross_lane", "DECLARATIVE/cross-lane"),
              ("semantic", "SEMANTIC")]
    for key, label in labels:
        if r[key]:
            sys.stdout.write(f"[{label}] {len(r[key])} finding(s):\n")
            for f in r[key]:
                sys.stdout.write(f"  - {f}\n")
        else:
            sys.stdout.write(f"[{label}] clean.\n")
    red = bool(r["mechanical"]) or any(not s.startswith("SEMANTIC axis NOT PROVIDED") for s in r["semantic"])
    incomplete = bool(r["in_scope_gap"]) or any(s.startswith("SEMANTIC axis NOT PROVIDED") for s in r["semantic"])
    scope_note = f" (scope={'declared' if scope else 'FULL baseline bar'}, producer={producer or 'all'})"
    if red:
        sys.stdout.write(f"SEAM: RED{scope_note} -- STOP + reconcile (govern fixes the registry OR ~D fixes the edges); do NOT proceed.\n")
        return FAIL
    if incomplete:
        sys.stdout.write(f"SEAM: IN-SCOPE-INCOMPLETE{scope_note} -- the claimed scope is not fully covered (or semantic axis not supplied); reconcile before proceeding.\n")
        return UNVERIFIABLE
    if r["phased_pending"]:
        sys.stdout.write(f"SEAM: GREEN-IN-SCOPE{scope_note} -- mechanical+semantic clean + claimed scope fully covered; {len(r['phased_pending'])} grain(s) phased for a later tier (EXPECTED). Both sign; proceed to next tier.\n")
    else:
        sys.stdout.write(f"SEAM: GREEN{scope_note} -- mechanical+semantic clean + full coverage; baseline-complete for this scope. Both sign.\n")
    return PASS


# ----------------------------------------------------------------------------- post-population harnesses
# Staged NOW (COO~B task-3) so they fire the instant Phase-A populates the depth ladders. Both REUSE
# the canonical definitions (rollup_defects, tool_grain_map) -- one head, no re-implementation.
def assemble_rollup(stitchers: list) -> dict:
    """Build the fine->coarse rolls_up map from all producers' stratum-stitcher edges (RUNS/CONTAINS
    coarse->fine, OWNED_BY fine->coarse). Transitive: a fine node rolls up to its coarsest ancestor.
    stitchers = [{edge_type, src, dst}, ...]."""
    parent: dict = {}
    for s in stitchers:
        et, src, dst = s.get("edge_type"), s.get("src"), s.get("dst")
        if et in ("RUNS", "CONTAINS"):   # coarse src -RUNS/CONTAINS-> fine dst : dst's parent is src
            parent[dst] = src
        elif et == "OWNED_BY":           # fine src -OWNED_BY-> coarse dst : src's parent is dst
            parent[src] = dst

    def _root(n):
        seen = set()
        while n in parent and n not in seen:
            seen.add(n)
            n = parent[n]
        return n

    return {n: _root(n) for n in set(parent)}


def multiparty_rollup(coarse_edges: list, fine_edges: list, stitchers: list) -> list:
    """The Phase-A CROSS-STRATUM existential rollup (the storage-only-slice's deferred SEMANTIC axis):
    assemble rolls_up from ALL producers' stitcher edges, then run the CANONICAL rollup_defects().
    Returns [(defect_class, edge)] -- UNSUPPORTED / COARSE-INCOMPLETE. ~A+~D+~B+~C call this at Phase-A."""
    return rollup_defects(coarse_edges, fine_edges, assemble_rollup(stitchers))


def audit_grain(declared_map: dict, observed_map: dict) -> list:
    """S4 AUDIT-part (post-population): declared-grain vs REAL-traversal. declared_map = tool_grain_map
    (tool -> [grains]); observed_map = {tool: [grains it ACTUALLY traversed on the populated graph]}.
    A tool traversing a grain it didn't declare, or declaring a grain it never traverses, = a finding.
    A `cross-grain` declaration spans all -> never a mismatch."""
    out = []
    for tool, observed in observed_map.items():
        declared = set(declared_map.get(tool, []))
        if "cross-grain" in declared:
            continue
        obs = set(observed)
        if obs - declared:
            out.append((tool, "TRAVERSES-UNDECLARED", sorted(obs - declared)))
        if declared - obs:
            out.append((tool, "DECLARED-NOT-TRAVERSED", sorted(declared - obs)))
    return out


def _declared_grain_map(led: dict) -> dict:
    """The DECLARED side of the S4 audit: tool_grain_calibration.tool_grain_map (tool -> [grains]).
    ONE source of truth -- the same block the calibration lives in; never re-typed here."""
    return led.get("tool_grain_calibration", {}).get("tool_grain_map", {})


def audit(observed_path: str | None) -> int:
    """CLI: the S4 AUDIT harness -- declared tool_grain_map vs REAL post-population traversal. STAGED
    ready-to-fire so it runs the INSTANT Phase-A population lands. observed_path = a JSON object
    {tool: [grains it ACTUALLY traversed]} produced by the post-population traversal step -- the SAME
    caller-supplies-the-pull contract as `seam --edges` (the traversal SOURCE is the populated
    comp-kuzu graph / the COMPLEARN behavior plane; the harness never re-implements the pull). The
    DECLARED side loads from the ledger now. Exit 0 GREEN (declared==observed, no grain drift) /
    1 RED (a grain mismatch finding) / 2 UNVERIFIABLE (no observed map yet -- graph not populated;
    NEVER a silent PASS)."""
    try:
        led = _load(LEDGER)
    except Exception as exc:  # noqa: BLE001 -- could-not-read is UNVERIFIABLE, never a silent PASS
        sys.stderr.write(f"UNVERIFIABLE: could not read the ledger: {exc}\n")
        return UNVERIFIABLE
    declared = _declared_grain_map(led)
    if not declared:
        sys.stderr.write("UNVERIFIABLE: tool_grain_calibration.tool_grain_map absent from the ledger -- nothing to audit against.\n")
        return UNVERIFIABLE
    if not observed_path:
        sys.stderr.write(
            "UNVERIFIABLE: no --observed <observed.json> supplied. The AUDIT harness is STAGED but the "
            "OBSERVED side needs the POPULATED graph. Post-population, pull each tool's actually-traversed "
            "grains (comp-kuzu traversal / COMPLEARN behavior plane) into observed.json {tool: [grains]} "
            "and re-run `comp-coverage-check audit --observed observed.json`. Pre-population is UNVERIFIABLE, "
            "never a silent PASS.\n")
        return UNVERIFIABLE
    try:
        observed = json.load(open(observed_path, encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write(f"UNVERIFIABLE: could not read observed map {observed_path}: {exc}\n")
        return UNVERIFIABLE
    if not isinstance(observed, dict) or not observed:
        sys.stderr.write(f"UNVERIFIABLE: observed map {observed_path} is empty or not a {{tool: [grains]}} object.\n")
        return UNVERIFIABLE
    findings = audit_grain(declared, observed)
    if not findings:
        sys.stdout.write(f"AUDIT: GREEN -- every observed tool ({len(observed)}) traverses at exactly its declared grain(s). No grain drift.\n")
        return PASS
    sys.stdout.write(f"AUDIT: {len(findings)} grain-drift finding(s) (declared tool_grain_map vs REAL traversal):\n")
    for tool, kind, grains in findings:
        if kind == "TRAVERSES-UNDECLARED":
            sys.stdout.write(f"  - {tool}: TRAVERSES-UNDECLARED {grains} -- traverses a grain it did not declare (widen the declaration OR the tool overreaches its grain).\n")
        else:
            sys.stdout.write(f"  - {tool}: DECLARED-NOT-TRAVERSED {grains} -- declares a grain it never traverses (dead declaration OR that grain was never populated).\n")
    sys.stdout.write("AUDIT: RED -- reconcile the tool_grain_map with real traversal (feed new grain-gaps to COMPLEARN ~E).\n")
    return FAIL


_CHECKERS = {
    "one_home": _check_one_home,
    "seam_reference_integrity": _check_seam_reference_integrity,
    "declared_non_redundancy": _check_declared_non_redundancy,
    "coverage_single_home": _check_coverage_single_home,
    "no_trino_phantom_seam": _check_no_trino_phantom_seam,
    "inventory_completeness": _check_inventory_completeness,
    "stable_grain": _check_stable_grain,
    "grain_drilldown_seams": _check_grain_drilldown_seams,
    "grain_rollup_consistency": _check_grain_rollup_consistency,
    "producer_attribution": _check_producer_attribution,
    "referenceable_target": _check_referenceable_target,
    "disposition_complete": _check_disposition_complete,
}


# ----------------------------------------------------------------------------- projection currency (AC5)
def _manifest_inventory() -> set[str]:
    return set(_load(MANIFEST).get("tools_index", {}).keys())


def _check_projection_currency(led: dict, manifest_inv: set[str] | None = None, **_: object) -> list[str]:
    """The manifest tools_index must be a CURRENT projection: every manifest tool present in the
    ledger union. ASSERTS currency only -- never writes the manifest (regen is an EXEC/CI step).
    Delegates to comp_coverage_view.projection_lost so the gate + the projector share ONE
    definition of 'current' (the CTO regeneration-ownership ruling, AC5)."""
    inv = _manifest_inventory() if manifest_inv is None else manifest_inv
    union = comp_coverage_view.ledger_union(led)
    lost = comp_coverage_view.projection_lost(union, inv)
    if lost:
        return [f"projection_currency: manifest tools_index carries {lost} absent from the ledger union (STALE projection -- regenerate via comp_coverage_view emit)"]
    return []


# ----------------------------------------------------------------------------- the gate
def run_gate(led: dict, seam_source: dict, inventory: set[str] | None = None,
             manifest_inv: set[str] | None = None) -> tuple[int, list[str], list[str]]:
    """Enumerate the ledger's OWN gate_contract.rules + projection-currency; dispatch each to its
    checker. Returns (exit_code, violations, unverifiable_findings)."""
    rules = led.get("schema", {}).get("gate_contract", {}).get("rules", [])
    if not rules:
        return UNVERIFIABLE, [], ["gate_contract.rules absent or empty -- cannot enumerate the spec"]
    violations: list[str] = []
    unverifiable: list[str] = []
    for r in rules:
        rid = r.get("id")
        checker = _CHECKERS.get(rid)
        if checker is None:
            unverifiable.append(f"contract rule '{rid}' has NO checker in comp-coverage-check (UNVERIFIABLE -- never a silent PASS)")
            continue
        violations.extend(checker(led, seam_source=seam_source, inventory=inventory))
    # AC5 projection-currency (always run -- the CTO regeneration-ownership ruling)
    violations.extend(_check_projection_currency(led, manifest_inv=manifest_inv))
    if unverifiable:
        return UNVERIFIABLE, violations, unverifiable
    return (FAIL if violations else PASS), violations, unverifiable


def check(universe: str = "working") -> int:
    """universe='working' (default, the operator view) | 'commit' (the gate view: tracked files only).

    A gate MUST pass universe='commit'. We share one worktree, so the default working-tree read
    also sees other agents' untracked, mid-authoring comp-* files and will FAIL every agent for
    work nobody committed. That is the root of the 2026-07-09 unplaced-banner churn.
    """
    global _INVENTORY_OVERRIDE
    _INVENTORY_OVERRIDE = _committed_tools_inventory() if universe == "commit" else None
    try:
        led = _load(LEDGER)
        seam_source = _load(SEAM_SOURCE)
    except Exception as exc:  # noqa: BLE001 -- could-not-read is UNVERIFIABLE, never a silent PASS
        sys.stderr.write(f"UNVERIFIABLE: could not read the ledger/seam-source: {exc}\n")
        return UNVERIFIABLE
    code, violations, unverifiable = run_gate(led, seam_source)
    if code == PASS:
        # STANDING RULE (CTO 20260709T192409Z, promoted from the member-4 vacuous-gate self-catch):
        # "A gate that cannot state its denominator cannot be trusted to have a numerator." A green
        # that names no universe is indistinguishable from a green that swept nothing. Six
        # qualitative claims with no N behind them was exactly that shape. The commit path may be
        # quiet; this operator surface may not.
        n_tools = len(led.get("tools") or [])
        n_meta = len(led.get("meta_tools") or [])
        n_rules = len(led.get("schema", {}).get("gate_contract", {}).get("rules", []))
        n_inv = len(_INVENTORY_OVERRIDE) if _INVENTORY_OVERRIDE is not None else n_tools + n_meta
        sys.stdout.write(
            "PASS: comp-coverage-map.yaml is internally consistent -- every tool one home, every "
            "overlap declared, no phantom seam, inventory complete, projection current, grain stable.\n"
        )
        sys.stdout.write(
            f"  swept: {n_tools + n_meta} homed tool(s) ({n_tools} tools[] + {n_meta} meta_tools[]) "
            f"| {n_rules} gate_contract rule(s), 0 unverifiable | inventory universe='{universe}' "
            f"({n_inv} tool(s))\n"
        )
        return PASS
    if code == UNVERIFIABLE:
        for u in unverifiable:
            sys.stderr.write(f"UNVERIFIABLE: {u}\n")
        for v in violations:
            sys.stderr.write(f"FAIL: {v}\n")
        return UNVERIFIABLE
    for v in violations:
        sys.stderr.write(f"FAIL: {v}\n")
    sys.stderr.write(f"FAIL: {len(violations)} violation(s) -- the map drifted from the territory.\n")
    return FAIL


# STABLE case metadata (id, kind, expected) -- 1:1 with the appends below, in order. This is the
# FROZEN no-regression baseline CVO~B pins (GRAPHUNI P0-CVO fixture layer b): the {id -> expected}
# verdict map. `selfcheck --json` emits it; the re-assert requires every case still `passed`. A
# checker that drifts (e.g. existential rollup sliding toward 1:1) flips a verdict -> passed:false.
_SELFCHECK_CASES = [
    ("clean_passes", "gate-verdict", "PASS"),
    ("unplaced_tool", "gate-verdict", "FAIL"),
    ("silent_overlap", "gate-verdict", "FAIL"),
    ("stale_projection", "gate-verdict", "FAIL"),
    ("no_checker_rule", "gate-verdict", "UNVERIFIABLE"),
    ("grain_retyping", "gate-verdict", "FAIL"),
    ("bad_drilldown_stratum", "gate-verdict", "FAIL"),
    ("rollup_1to1_semantics", "gate-verdict", "FAIL"),
    ("rollup_defects_existential", "logic-assertion", "holds"),
    ("seam_3_axes_fire", "logic-assertion", "holds"),
    ("seam_scope_producer", "logic-assertion", "holds"),
    ("unattributed_edge_type", "gate-verdict", "FAIL"),
    ("breadth_terminal_allowed_target", "gate-verdict", "FAIL"),
    ("seam_breadth_terminal_instance", "logic-assertion", "holds"),
    ("undisposed_level", "gate-verdict", "FAIL"),
    ("multiparty_rollup_harness", "logic-assertion", "holds"),
    ("s4_grain_audit_harness", "logic-assertion", "holds"),
    # ISOLATED per-checker cases (CVO 2026-07-10, CTO ruling 213553Z): each trips EXACTLY ONE checker,
    # so neutering that checker flips ITS case. Before these, 6 of 12 checkers were VACUOUSLY covered --
    # a broken checker left selfcheck 17/17 GREEN. The standing neuter-audit meta-test
    # (tests/test_coverage_check_selfcheck_nonvacuous.py) enforces 12/12-flip forever.
    ("iso_one_home", "gate-verdict", "FAIL"),
    ("iso_seam_reference_integrity", "gate-verdict", "FAIL"),
    ("iso_coverage_single_home", "gate-verdict", "FAIL"),
    ("iso_no_trino_phantom_seam", "gate-verdict", "FAIL"),
    ("iso_producer_attribution", "gate-verdict", "FAIL"),
    ("iso_stable_grain", "gate-verdict", "FAIL"),
]


def selfcheck(emit_json: bool = False) -> int:
    """Inject every gate violation class + confirm the clean ledger PASSes. `emit_json` emits the
    frozen {id, kind, expected, passed} verdict-set (CVO~B P0-CVO no-regression fixture, layer b)."""
    led = _load(LEDGER)
    seam_source = _load(SEAM_SOURCE)
    inv = _tools_dir_inventory()
    manifest_inv = _manifest_inventory()
    results = []

    # 0) clean ledger PASSes
    code, _, _ = run_gate(led, seam_source, inventory=inv, manifest_inv=manifest_inv)
    results.append(("clean ledger -> PASS", code == PASS))

    # a) UNPLACED tool: add a fake tool to .tools/ inventory not in the ledger
    bad_inv = set(inv) | {"comp-ghost-unplaced"}
    code, _, _ = run_gate(led, seam_source, inventory=bad_inv, manifest_inv=manifest_inv)
    results.append(("injected unplaced tool -> FAIL", code == FAIL))

    # b) SILENT OVERLAP: a tool sharing a resource with no declared distinct_from
    led_overlap = copy.deepcopy(led)
    led_overlap["tools"].append({
        "tool": "comp-ghost-overlap", "surface": "AWS-CLOUD", "granularity": "iam-policy",
        "concern": "ghost concern", "touches_resource": ["IAM"],  # touches IAM, declares nothing
    })
    code, _, _ = run_gate(led_overlap, seam_source, inventory=inv | {"comp-ghost-overlap"}, manifest_inv=manifest_inv)
    results.append(("injected silent overlap -> FAIL", code == FAIL))

    # c) STALE PROJECTION: manifest carries a tool absent from the ledger union
    code, _, _ = run_gate(led, seam_source, inventory=inv, manifest_inv=manifest_inv | {"comp-ghost-manifest-only"})
    results.append(("injected stale projection -> FAIL", code == FAIL))

    # d) UNVERIFIABLE: a contract rule with no checker
    led_norule = copy.deepcopy(led)
    led_norule["schema"]["gate_contract"]["rules"].append({"id": "ghost_rule_no_checker"})
    code, _, _ = run_gate(led_norule, seam_source, inventory=inv, manifest_inv=manifest_inv)
    results.append(("contract rule w/o checker -> UNVERIFIABLE", code == UNVERIFIABLE))

    # e) GRAIN RE-TYPING: a relation split across two edge_types by depth (the stable-grain defect)
    led_grain = copy.deepcopy(led)
    led_grain.setdefault("grain_contract", {}).setdefault("edge_types", []).append(
        {"edge_type": "READS_S3_PREFIX", "relation": "reads_s3", "levels": ["prefix"]})  # re-types reads_s3 by depth
    code, _, _ = run_gate(led_grain, seam_source, inventory=inv, manifest_inv=manifest_inv)
    results.append(("injected grain re-typing -> FAIL", code == FAIL))

    # f) DRILLDOWN SEAM bridging an UNDECLARED stratum -> FAIL (fractal sec-10)
    led_seam = copy.deepcopy(led)
    led_seam.setdefault("grain_contract", {}).setdefault("drilldown_seams", []).append(
        {"edge_type": "RUNS", "from_stratum": "resource", "to_stratum": "GHOST_STRATUM"})
    code, _, _ = run_gate(led_seam, seam_source, inventory=inv, manifest_inv=manifest_inv)
    results.append(("injected bad drilldown stratum -> FAIL", code == FAIL))

    # g) ROLLUP mis-declared as 1:1 (not existential) -> FAIL (the drift 047ce51d0 corrected)
    led_rollup = copy.deepcopy(led)
    led_rollup.setdefault("grain_contract", {}).setdefault("rollup", {})["semantics"] = "one-to-one-equality"
    code, _, _ = run_gate(led_rollup, seam_source, inventory=inv, manifest_inv=manifest_inv)
    results.append(("injected 1:1 rollup semantics -> FAIL", code == FAIL))

    # h) rollup_defects() existential logic: UNSUPPORTED (coarse no fine basis) + COARSE-INCOMPLETE
    #    (fine, coarse absent); a supported coarse + matching fine -> no defect.
    rolls = {"fn1": "EC2", "key1": "BUCKET", "fn2": "EC2", "key2": "BUCKET2"}
    coarse = [("EC2", "BUCKET"), ("EC2", "GHOST_BUCKET")]          # 2nd has no fine basis -> UNSUPPORTED
    fine = [("fn1", "key1"), ("fn2", "key2")]                       # fn2/key2 imply (EC2,BUCKET2) absent -> COARSE-INCOMPLETE
    d = {edge: cls for cls, edge in rollup_defects(coarse, fine, rolls)}  # edge -> defect class
    rd_ok = (d.get(("EC2", "GHOST_BUCKET")) == "UNSUPPORTED"
             and d.get(("EC2", "BUCKET2")) == "COARSE-INCOMPLETE"
             and ("EC2", "BUCKET") not in d)  # supported coarse + its fine -> clean
    results.append(("rollup_defects existential logic (UNSUPPORTED + COARSE-INCOMPLETE, supported clean)", rd_ok))

    # i) SEAM validator -- each of the 3 axes fires on its own defect class
    sv_orphan = seam_validate(led, [{"edge_type": "GHOST_TYPE", "level": "x", "from_stratum": "resource", "to_stratum": "compute"}], None)
    sv_rollup = seam_validate(led, [], {"coarse": [["EC2", "GHOST"]], "fine": [], "rolls_up": {}})
    seam_ok = (bool(sv_orphan["mechanical"])        # population-orphan edge_type -> MECHANICAL fires
               and bool(sv_orphan["in_scope_gap"])  # registry types/strata unpopulated -> DECLARATIVE in-scope-gap fires
               and bool(sv_rollup["semantic"]))     # UNSUPPORTED coarse edge -> SEMANTIC fires
    results.append(("seam validator: 3 axes fire on defects (mechanical/declarative/semantic)", seam_ok))

    # j) SEAM scope+producer aware (~D pre-flight findings 2+3): a gold-tier increment CLAIMING only
    #    CALLS -> GREEN-in-scope (no in_scope_gap), other gold grains PHASED, other-lane grains CROSS-LANE.
    sv_scope = seam_validate(
        led,
        [{"edge_type": "CALLS", "level": "function", "from_stratum": "compute", "to_stratum": "compute"}],
        {"coarse": [], "fine": [], "rolls_up": {}},
        scope={"edge_types": ["CALLS"], "strata": ["compute"]}, producer="graphuni-gold")
    scope_ok = (not sv_scope["mechanical"] and not sv_scope["in_scope_gap"] and not sv_scope["semantic"]
                and bool(sv_scope["phased_pending"]) and bool(sv_scope["cross_lane"]))
    results.append(("seam scope+producer aware (claimed scope GREEN; others phased/cross-lane)", scope_ok))

    # k) PRODUCER ATTRIBUTION: an edge_type with no producer disposition -> FAIL (silent denominator gap)
    led_unattr = copy.deepcopy(led)
    led_unattr.setdefault("grain_contract", {}).setdefault("edge_types", []).append(
        {"edge_type": "GHOST_UNATTRIBUTED", "relation": "ghost", "levels": ["x"]})  # no producer / producer_by_pair
    code, _, _ = run_gate(led_unattr, seam_source, inventory=inv, manifest_inv=manifest_inv)
    results.append(("injected unattributed edge_type -> FAIL", code == FAIL))

    # l) REFERENCEABLE-TARGET gate: a breadth edge allowed to target a TERMINAL member -> FAIL (inv 5)
    led_ref = copy.deepcopy(led)
    led_ref.setdefault("grain_contract", {}).setdefault("referenceable", {}).setdefault("referenceable_targets", {})["CALLS"] = ["Statement"]
    code, _, _ = run_gate(led_ref, seam_source, inventory=inv, manifest_inv=manifest_inv)
    results.append(("injected breadth->terminal allowed-target -> FAIL", code == FAIL))

    # m) NON-REFERENCEABLE-TARGET (instance, seam MECHANICAL): a populated breadth edge on a terminal node
    sv_ref = seam_validate(led, [{"edge_type": "CALLS", "level": "function", "from_stratum": "compute", "to_stratum": "compute", "target_node_type": "Statement"}], None)
    results.append(("seam: breadth edge -> terminal target fires MECHANICAL", bool(sv_ref["mechanical"])))

    # n) DISPOSITION COMPLETENESS: a declared level with no eager/bounded/n_a disposition -> FAIL (silent cap)
    led_disp = copy.deepcopy(led)
    led_disp.setdefault("grain_contract", {}).setdefault("edge_types", []).append(
        {"edge_type": "GHOST_UNDISPOSED", "relation": "ghost_undisp", "levels": ["mystery"], "producer": "graphuni-gold"})
    code, _, _ = run_gate(led_disp, seam_source, inventory=inv, manifest_inv=manifest_inv)
    results.append(("injected undisposed level -> FAIL", code == FAIL))

    # o) MULTIPARTY cross-stratum rollup harness (Phase-A): assemble rolls_up from stitchers -> rollup_defects
    stit = [{"edge_type": "RUNS", "src": "EC2", "dst": "Script"}, {"edge_type": "CONTAINS", "src": "Script", "dst": "fn1"},
            {"edge_type": "OWNED_BY", "src": "key1", "dst": "BUCKET"}]
    mp_clean = multiparty_rollup([("EC2", "BUCKET")], [("fn1", "key1")], stit)   # fn1->EC2, key1->BUCKET -> supported
    mp_unsup = multiparty_rollup([("EC2", "GHOST")], [("fn1", "key1")], stit)    # coarse w/ no fine basis -> UNSUPPORTED
    mp_ok = (not mp_clean and any(c == "UNSUPPORTED" for c, _ in mp_unsup))
    results.append(("multiparty cross-stratum rollup harness (supported clean; unsupported->UNSUPPORTED)", mp_ok))

    # p) S4 grain-AUDIT harness (post-population): declared-vs-real traversal mismatch -> finding
    ga = audit_grain({"comp-blast": ["function", "symbol"]}, {"comp-blast": ["function", "object"]})
    ga_ok = any(t == "comp-blast" and k == "TRAVERSES-UNDECLARED" for t, k, _ in ga)
    results.append(("S4 grain-audit harness (traverses-undeclared -> finding)", ga_ok))

    # ---- ISOLATED per-checker cases: each trips EXACTLY ONE checker (verified: fires=={that rule}).
    # Purpose: neutering a checker must flip ITS case. The pre-existing cases were contaminated (e.g.
    # the grain_retyping edge_type is also producer-less + undisposed, so producer_attribution +
    # disposition_complete caught it regardless of stable_grain), leaving 6 checkers vacuously covered.
    # These fixtures are minimal-violation-only so the neuter-audit meta-test can prove 12/12 non-vacuity.

    # iso-1 one_home: a two-home tool (surface AND seam) -- inventory carries it so ONLY one_home fires.
    led_iso = copy.deepcopy(led)
    led_iso["tools"].append({"tool": "comp-iso-onehome", "surface": "AWS-CLOUD", "seam": "seam-1",
                       "granularity": "g", "concern": "c"})
    code, _, _ = run_gate(led_iso, seam_source, inventory=inv | {"comp-iso-onehome"}, manifest_inv=manifest_inv)
    results.append(("ISO one_home: two-home tool -> FAIL (only one_home)", code == FAIL))

    # iso-2 seam_reference_integrity: a tool referencing a seam_id absent from drift-topology.yaml.
    led_iso = copy.deepcopy(led)
    led_iso["tools"].append({"tool": "comp-iso-seamref", "seam": "seam-GHOST-999",
                       "granularity": "g", "concern": "c"})
    code, _, _ = run_gate(led_iso, seam_source, inventory=inv | {"comp-iso-seamref"}, manifest_inv=manifest_inv)
    results.append(("ISO seam_reference_integrity: absent seam ref -> FAIL (only seam_reference_integrity)", code == FAIL))

    # iso-3 coverage_single_home: an axis storing a 'coverage' copy (must be READ from coverage_source).
    led_iso = copy.deepcopy(led)
    led_iso.setdefault("seams", {}).setdefault("axis", []).append({"seam_id": "seam-1", "coverage": "COVERED"})
    code, _, _ = run_gate(led_iso, seam_source, inventory=inv, manifest_inv=manifest_inv)
    results.append(("ISO coverage_single_home: axis stores coverage copy -> FAIL (only coverage_single_home)", code == FAIL))

    # iso-4 no_trino_phantom_seam: a phantom per-layer catalog named 'aws' (layer is a graph_nodes COLUMN).
    led_iso = copy.deepcopy(led)
    led_iso.setdefault("trino_federation", {}).setdefault("catalogs", []).append({"name": "aws"})
    code, _, _ = run_gate(led_iso, seam_source, inventory=inv, manifest_inv=manifest_inv)
    results.append(("ISO no_trino_phantom_seam: phantom 'aws' catalog -> FAIL (only no_trino_phantom_seam)", code == FAIL))

    # iso-5 producer_attribution: an edge_type with NO producer, UNIQUE relation, and its level DISPOSED
    # (so disposition_complete + stable_grain stay clean -> ONLY producer_attribution fires).
    led_iso = copy.deepcopy(led)
    led_iso["grain_contract"].setdefault("edge_types", []).append(
        {"edge_type": "ISO_NOPROD", "relation": "iso_noprod_rel", "levels": ["isolvl"]})
    led_iso["grain_contract"].setdefault("level_dispositions", {})["ISO_NOPROD"] = {"isolvl": "n_a"}
    code, _, _ = run_gate(led_iso, seam_source, inventory=inv, manifest_inv=manifest_inv)
    results.append(("ISO producer_attribution: producer-less edge (disposed) -> FAIL (only producer_attribution)", code == FAIL))

    # iso-6 stable_grain: split an EXISTING relation across two edge_types, BOTH with producer + a disposed
    # level (so producer_attribution + disposition_complete stay clean -> ONLY stable_grain fires).
    led_iso = copy.deepcopy(led)
    _ex = next((e for e in led_iso["grain_contract"].get("edge_types", []) if e.get("relation") and e.get("producer")), None)
    if _ex:
        _dup = {"edge_type": _ex["edge_type"] + "_ISO", "relation": _ex["relation"],
                "levels": ["isolvl2"], "producer": _ex.get("producer", "iso")}
        led_iso["grain_contract"]["edge_types"].append(_dup)
        led_iso["grain_contract"].setdefault("level_dispositions", {})[_dup["edge_type"]] = {"isolvl2": "n_a"}
        code, _, _ = run_gate(led_iso, seam_source, inventory=inv, manifest_inv=manifest_inv)
        results.append(("ISO stable_grain: split relation (complete edge) -> FAIL (only stable_grain)", code == FAIL))
    else:
        results.append(("ISO stable_grain: no producer'd relation to split -- fixture UNBUILDABLE", False))

    if len(results) != len(_SELFCHECK_CASES):  # guard: metadata must stay 1:1 with the appends
        sys.stderr.write(f"selfcheck INTERNAL: {len(results)} cases vs {len(_SELFCHECK_CASES)} metadata -- update _SELFCHECK_CASES\n")
        return UNVERIFIABLE
    cases = [{"id": cid, "kind": kind, "expected": exp, "passed": bool(passed), "label": label}
             for (cid, kind, exp), (label, passed) in zip(_SELFCHECK_CASES, results)]
    ok = all(c["passed"] for c in cases)
    if emit_json:
        led = _load(LEDGER)
        sys.stdout.write(json.dumps({
            "artifact": "comp-coverage-check.selfcheck.verdict_set",
            "ledger_version": led.get("version"),
            "n_cases": len(cases),
            "gate_rules": [r.get("id") for r in led.get("schema", {}).get("gate_contract", {}).get("rules", [])],
            "all_ok": ok,
            "cases": [{k: c[k] for k in ("id", "kind", "expected", "passed")} for c in cases],
        }, indent=2, sort_keys=True) + "\n")
        return PASS if ok else FAIL
    for c in cases:
        sys.stdout.write(f"{'OK  ' if c['passed'] else 'FAIL'}: {c['label']}\n")
    sys.stdout.write(("selfcheck PASS -- the gate fails each injected violation + passes clean.\n" if ok
                      else "selfcheck FAILED -- the gate did not behave as specified.\n"))
    return PASS if ok else FAIL


def list_rules() -> int:
    led = _load(LEDGER)
    sys.stdout.write("comp-coverage-check enforces the ledger's own gate_contract.rules + projection-currency:\n")
    for r in led.get("schema", {}).get("gate_contract", {}).get("rules", []):
        has = "checker" if r.get("id") in _CHECKERS else "NO CHECKER (would be UNVERIFIABLE)"
        sys.stdout.write(f"  - {r.get('id'):28s} [{has}]\n")
    sys.stdout.write(f"  - {'projection_currency':28s} [checker] (AC5 -- manifest tools_index current vs ledger union)\n")
    return PASS


def _arg(argv: list[str], flag: str) -> str | None:
    return argv[argv.index(flag) + 1] if flag in argv and argv.index(flag) + 1 < len(argv) else None


def main(argv: list[str]) -> int:
    cmd = argv[0] if argv else "check"
    if cmd == "selfcheck":
        return selfcheck(emit_json="--json" in argv)
    if cmd == "list":
        return list_rules()
    if cmd == "seam":
        edges_path = _arg(argv, "--edges")
        if not edges_path:
            sys.stderr.write("usage: comp-coverage-check seam --edges <edges.json> [--rollup <rollup.json>] [--scope <scope.json>] [--producer <lane>]\n")
            return UNVERIFIABLE
        return seam(edges_path, _arg(argv, "--rollup"), _arg(argv, "--scope"), _arg(argv, "--producer"))
    if cmd == "audit":
        return audit(_arg(argv, "--observed"))
    # --universe commit == the GATE view (tracked files only). Default stays the operator view.
    return check(universe=(_arg(argv, "--universe") or "working"))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
