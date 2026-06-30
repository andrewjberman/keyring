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


def _tools_dir_inventory() -> set[str]:
    inv: set[str] = set()
    if not os.path.isdir(TOOLS_DIR):
        return inv
    for f in os.listdir(TOOLS_DIR):
        base = f.rsplit(".", 1)[0] if "." in f else f
        if base.startswith("comp-") or base == "pipescript":
            inv.add(base)
    return inv


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


def _check_inventory_completeness(led: dict, inventory: set[str] | None = None, **_: object) -> list[str]:
    inv = _tools_dir_inventory() if inventory is None else inventory
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


def seam_validate(led: dict, edges: list, rollup_view: dict | None):
    """The 3-axis govern<->populate SEAM validation (Andrew-direct symbiotic protocol). Validates
    ~D's POPULATED edges against the grain_contract registry (~C governs) at the CATEGORICAL bar.
    Returns {mechanical, declarative, semantic, coverage} -- each axis a list of findings ([] = clean).

    INTERFACE (the contract ~D emits to):
      edges       = [{edge_type, level, from_stratum, to_stratum}, ...]   (one per populated edge)
      rollup_view = {"coarse": [[src,dst],...], "fine": [[src,dst],...], "rolls_up": {node: coarse_node}}
                    (optional; the existential-rollup view for the SEMANTIC axis)
    """
    gc = led.get("grain_contract", {})
    et_index = {e["edge_type"]: e for e in gc.get("edge_types", [])}
    registry_types = set(et_index)
    strata = set(gc.get("strata", []))
    mechanical, declarative = [], []
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

    # --- AXIS 2: DECLARATIVE -- registry <-> population CATEGORICAL coverage (map == territory) ---
    for rt in sorted(registry_types - populated_types):
        declarative.append(f"registry edge_type '{rt}' has ZERO populated edges (registry-orphan / dead type -- retire it or ~D must populate)")
    for st in sorted(strata - populated_strata):
        declarative.append(f"stratum '{st}' has ZERO populated edges (uncovered stratum -- the categorical bar is not met)")
    for et in sorted(registry_types & populated_types):
        for lvl in sorted(set(et_index[et].get("levels", [])) - populated_levels.get(et, set())):
            declarative.append(f"edge_type '{et}' level '{lvl}' declared but NOT populated (uncovered grain level)")

    # --- AXIS 3: SEMANTIC -- existential rollup holds on the REAL edges (one head) ---
    if rollup_view is None:
        semantic = ["SEMANTIC axis NOT PROVIDED -- supply rollup_view {coarse, fine, rolls_up} to validate existential rollup (categorical bar requires it)"]
    else:
        defects = rollup_defects(rollup_view.get("coarse", []), rollup_view.get("fine", []), rollup_view.get("rolls_up", {}))
        semantic = [f"{cls}: {edge}" for cls, edge in defects]

    coverage = {
        "registry_types": sorted(registry_types),
        "populated_types": sorted(populated_types),
        "covered_types": sorted(registry_types & populated_types),
        "uncovered_strata": sorted(strata - populated_strata),
    }
    return {"mechanical": mechanical, "declarative": declarative, "semantic": semantic, "coverage": coverage}


def seam(edges_path: str, rollup_path: str | None) -> int:
    """CLI: 3-axis seam validation of ~D's populated edges vs the governed registry. Exit 0 GREEN /
    1 RED (mechanical or semantic defect) / 2 INCOMPLETE (declarative coverage gap or semantic not provided)."""
    try:
        led = _load(LEDGER)
        with open(edges_path, encoding="utf-8") as fh:
            edges = json.load(fh)
        rollup_view = None
        if rollup_path:
            with open(rollup_path, encoding="utf-8") as fh:
                rollup_view = json.load(fh)
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write(f"UNVERIFIABLE: could not read ledger/edges/rollup: {exc}\n")
        return UNVERIFIABLE
    r = seam_validate(led, edges, rollup_view)
    for axis in ("mechanical", "declarative", "semantic"):
        if r[axis]:
            sys.stdout.write(f"[{axis.upper()}] {len(r[axis])} finding(s):\n")
            for f in r[axis]:
                sys.stdout.write(f"  - {f}\n")
        else:
            sys.stdout.write(f"[{axis.upper()}] clean.\n")
    red = bool(r["mechanical"]) or any(not s.startswith("SEMANTIC axis NOT PROVIDED") for s in r["semantic"])
    incomplete = bool(r["declarative"]) or any(s.startswith("SEMANTIC axis NOT PROVIDED") for s in r["semantic"])
    if red:
        sys.stdout.write("SEAM: RED -- STOP + reconcile (govern fixes the registry OR ~D fixes the edges); do NOT proceed.\n")
        return FAIL
    if incomplete:
        sys.stdout.write("SEAM: INCOMPLETE -- categorical coverage not yet met (uncovered grain/stratum, or semantic axis not supplied). Baseline NOT robust.\n")
        return UNVERIFIABLE
    sys.stdout.write("SEAM: GREEN -- mechanical + declarative + semantic all clean; categorical coverage met. Both sign.\n")
    return PASS


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


def check() -> int:
    try:
        led = _load(LEDGER)
        seam_source = _load(SEAM_SOURCE)
    except Exception as exc:  # noqa: BLE001 -- could-not-read is UNVERIFIABLE, never a silent PASS
        sys.stderr.write(f"UNVERIFIABLE: could not read the ledger/seam-source: {exc}\n")
        return UNVERIFIABLE
    code, violations, unverifiable = run_gate(led, seam_source)
    if code == PASS:
        sys.stdout.write("PASS: comp-coverage-map.yaml is internally consistent -- every tool one home, every overlap declared, no phantom seam, inventory complete, projection current, grain stable.\n")
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


def selfcheck() -> int:
    """Inject the three violation classes the CTO arch-gate names + confirm the clean ledger PASSes."""
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
    seam_ok = (bool(sv_orphan["mechanical"])       # population-orphan edge_type -> MECHANICAL fires
               and bool(sv_orphan["declarative"])  # registry types/strata unpopulated -> DECLARATIVE fires
               and bool(sv_rollup["semantic"]))    # UNSUPPORTED coarse edge -> SEMANTIC fires
    results.append(("seam validator: 3 axes fire on defects (mechanical/declarative/semantic)", seam_ok))

    ok = all(passed for _, passed in results)
    for label, passed in results:
        sys.stdout.write(f"{'OK  ' if passed else 'FAIL'}: {label}\n")
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
        return selfcheck()
    if cmd == "list":
        return list_rules()
    if cmd == "seam":
        edges_path = _arg(argv, "--edges")
        if not edges_path:
            sys.stderr.write("usage: comp-coverage-check seam --edges <populated-edges.json> [--rollup <rollup-view.json>]\n")
            return UNVERIFIABLE
        return seam(edges_path, _arg(argv, "--rollup"))
    return check()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
