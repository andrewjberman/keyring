#!/usr/bin/env python3
"""comp-ontolint -- lint the NFRA_ONTOLOGY Relation-vs-Role composite exception (NFRA_ONTOCLARITY WS-B fog-7).

The fog (brief S3c): three edges are DUAL-AXIS -- they yield a base Relation PLUS a Role
(routes-to->Router, resolves-through->Registry, projects->Gateway); ALL OTHER relations are single-axis
(a Relation, no Role). Today that exception is a prose "load-bearing subtlety" that nothing enforces, so a
classifier must just KNOW the 3-item list -> it re-drifts on the next reader (Rule-20: cannot-block = not-a-gate,
at the definitional layer). This lint makes the exception a MACHINE-CHECKED invariant read from the canonical
rule-bank (meta.canonical_source), so it can no longer silently drift.

INVARIANT (structure-derived from org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml):
  (1) SINGLE-AXIS: no base `relations:` entry carries a `role:` key (a base relation is a Relation, not a Role).
  (2) VALID-ROLE:  every `relation_composites:` `role:` value is a declared Role (a key of `roles:`).
  (3) DUAL-AXIS SET is EXPLICIT + enumerated: the exception list = composites carrying a `role:` -- printed as the
      machine-readable list that REPLACES the prose (a reader/classifier reads the list, not a paragraph).
A VIOLATION of (1) or (2) FIRES (non-zero exit). Advisory/no-guess: an unreadable rule-bank is a hard error,
never a silent pass (a control that cannot fail is not a control).

Subcommands:
  comp-ontolint check [--rule-bank PATH]   -- lint the live rule-bank; exit 0 clean / 1 violation / 2 error
  comp-ontolint self-test                  -- seeded-mutant control: a base relation given a spurious Role FIRES;
                                              the clean rule-bank PASSES (the exercise CTO's arch-gate requires)
"""
from __future__ import annotations

import sys
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_DEFAULT_RULE_BANK = os.path.join(_HERE, "NFRA_ONTOLOGY_RULE_BANK.yaml")


def _load(path: str) -> dict:
    import yaml
    with open(path, encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    if not isinstance(doc, dict):
        raise ValueError("rule-bank did not parse to a mapping: %s" % path)
    return doc


def lint(doc: dict) -> list:
    """PURE. Returns a list of violation strings ([] == clean). The Relation-vs-Role invariant over a rule-bank dict."""
    violations: list = []
    relations = doc.get("relations") if isinstance(doc.get("relations"), dict) else {}
    composites = doc.get("relation_composites") if isinstance(doc.get("relation_composites"), dict) else {}
    valid_roles = set(doc.get("roles") or {}) if isinstance(doc.get("roles"), dict) else set()

    # (1) SINGLE-AXIS: a base relation must NOT carry a role.
    for name, spec in relations.items():
        if isinstance(spec, dict) and "role" in spec:
            violations.append(
                "(1) base relation '%s' carries role '%s' -- base relations are SINGLE-AXIS (a Relation, not a Role); "
                "only relation_composites may be dual-axis" % (name, spec.get("role")))

    # (2) VALID-ROLE: every composite role is a declared Role.
    for name, spec in composites.items():
        if isinstance(spec, dict) and "role" in spec:
            role = spec.get("role")
            if valid_roles and role not in valid_roles:
                violations.append(
                    "(2) composite '%s' binds role '%s' which is NOT a declared Role (roles: keys) -- "
                    "a dual-axis Role must be one of the 14" % (name, role))
    return violations


def dual_axis_set(doc: dict) -> dict:
    """The machine-readable exception list: {composite -> Role} for composites carrying a role (replaces the prose)."""
    composites = doc.get("relation_composites") if isinstance(doc.get("relation_composites"), dict) else {}
    return {n: s.get("role") for n, s in composites.items() if isinstance(s, dict) and "role" in s}


def _check(path: str) -> int:
    try:
        doc = _load(path)
    except (OSError, ValueError, ImportError) as e:
        print("ERROR: comp-ontolint could not read the rule-bank (%s): %s" % (path, e))
        return 2
    dual = dual_axis_set(doc)
    viols = lint(doc)
    n_rel = len(doc.get("relations") or {})
    print("comp-ontolint check: rule-bank=%s" % path)
    print("  DENOMINATOR: %d base relations (single-axis) + %d dual-axis composite exception(s)" % (n_rel, len(dual)))
    print("  DUAL-AXIS exception list (machine-read, replaces the prose):")
    for name, role in sorted(dual.items()):
        print("    %-18s -> %s" % (name, role))
    if viols:
        print("  RESULT: FAIL -- %d violation(s):" % len(viols))
        for v in viols:
            print("    !! " + v)
        return 1
    print("  RESULT: PASS -- Relation-vs-Role invariant holds (base relations single-axis; composite roles valid).")
    return 0


def _self_test() -> int:
    """Seeded-mutant control (CTO arch-gate condition: the lint must FIRE on a mutant, not merely assert)."""
    ok = True
    # CLEAN fixture: the real shape -- base relations single-axis, the 3 composites dual-axis with valid roles.
    clean = {
        "roles": {"Router": {}, "Registry": {}, "Gateway": {}, "Store": {}, "Producer": {}},
        "relations": {"produces": {"binds_up": []}, "consumes": {"binds_up": []}},
        "relation_composites": {
            "projects": {"role": "Gateway"}, "routes-to": {"role": "Router"}, "resolves-through": {"role": "Registry"}},
    }
    c_clean = (lint(clean) == [])
    print("  clean fixture PASSES (no violation): %s" % c_clean)
    ok &= c_clean

    # MUTANT 1: a base relation given a spurious Role (violates (1) SINGLE-AXIS) -> MUST fire.
    m1 = {k: (dict(v) if isinstance(v, dict) else v) for k, v in clean.items()}
    m1["relations"] = dict(clean["relations"])
    m1["relations"]["produces"] = {"binds_up": [], "role": "Producer"}
    m1_fires = any("(1)" in v for v in lint(m1))
    print("  MUTANT 1 (base relation 'produces' given role 'Producer') FIRES: %s" % m1_fires)
    ok &= m1_fires

    # MUTANT 2: a composite bound to an UNDECLARED role (violates (2) VALID-ROLE) -> MUST fire.
    m2 = {k: (dict(v) if isinstance(v, dict) else v) for k, v in clean.items()}
    m2["relation_composites"] = dict(clean["relation_composites"])
    m2["relation_composites"]["projects"] = {"role": "Nonesuch"}
    m2_fires = any("(2)" in v for v in lint(m2))
    print("  MUTANT 2 (composite 'projects' bound to undeclared role 'Nonesuch') FIRES: %s" % m2_fires)
    ok &= m2_fires

    # RANDOM-INPUT control: an empty rule-bank has no relations -> no violations (the lint does not fire on nothing).
    empty_ok = (lint({}) == [])
    print("  empty rule-bank -> no false-positive: %s" % empty_ok)
    ok &= empty_ok

    print("=== comp-ontolint self-test: %s ===" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv: list) -> int:
    args = argv[1:]
    cmd = args[0] if args else "check"
    if cmd == "self-test":
        return _self_test()
    if cmd == "check":
        path = _DEFAULT_RULE_BANK
        if "--rule-bank" in args:
            path = args[args.index("--rule-bank") + 1]
        return _check(path)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
