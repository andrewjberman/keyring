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
import os
import sys

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


_CHECKERS = {
    "one_home": _check_one_home,
    "seam_reference_integrity": _check_seam_reference_integrity,
    "declared_non_redundancy": _check_declared_non_redundancy,
    "coverage_single_home": _check_coverage_single_home,
    "no_trino_phantom_seam": _check_no_trino_phantom_seam,
    "inventory_completeness": _check_inventory_completeness,
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
        sys.stdout.write("PASS: comp-coverage-map.yaml is internally consistent -- every tool one home, every overlap declared, no phantom seam, inventory complete, projection current.\n")
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


def main(argv: list[str]) -> int:
    cmd = argv[0] if argv else "check"
    if cmd == "selfcheck":
        return selfcheck()
    if cmd == "list":
        return list_rules()
    return check()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
