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

WS-C spot-8 (polymorphic-Role tie-breaker): when a node's edges match 2+ role derive-rules, `role_priority`
(a TOTAL order over the 14 roles, in the rule-bank) is the DETERMINISTIC winner -- highest priority wins
(guards+transforms -> Guard). This lint asserts role_priority is a total order (no omission/duplicate re-opens
the fog) and `role-resolve` exercises the tie-breaker.

Subcommands:
  comp-ontolint check [--rule-bank PATH]   -- lint the live rule-bank; exit 0 clean / 1 violation / 2 error
  comp-ontolint self-test                  -- seeded-mutant control: a base relation given a spurious Role FIRES;
                                              the clean rule-bank PASSES + the WS-C role-resolve gate-bar (a-d incl
                                              the LOAD-BEARING mutant: same node resolves DIFFERENTLY under a
                                              mutated priority -- proves the control depends on role_priority)
  comp-ontolint role-resolve <Role>...     -- WS-C spot-8: the deterministic winner among 2+ matched roles per
                                              role_priority (0 matches -> no role; 1 -> that role; 2+ arbitrated)
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

    # (3) role_priority TOTALITY (NFRA_ONTOCLARITY WS-C spot-8): the polymorphic-Role tie-breaker is a TOTAL
    # order over all declared roles -- a MISSING role re-opens the tie, a DUPLICATE rank re-opens the fog. Only
    # evaluated when role_priority is present (graceful: absent -> the WS-C fog is simply unresolved, not a lie).
    rp = doc.get("role_priority")
    if isinstance(rp, list) and valid_roles:
        rp_list = [str(r) for r in rp]
        dupes = sorted({r for r in rp_list if rp_list.count(r) > 1})
        if dupes:
            violations.append("(3) role_priority has DUPLICATE rank(s) %s -- a tie re-opens the polymorphic-Role fog" % dupes)
        missing = sorted(valid_roles - set(rp_list))
        if missing:
            violations.append("(3) role_priority OMITS role(s) %s -- a missing role re-opens the tie (not a TOTAL order over the roles)" % missing)
        extra = sorted(set(rp_list) - valid_roles)
        if extra:
            violations.append("(3) role_priority lists non-role(s) %s not declared in roles:" % extra)
    return violations


def role_priority(doc: dict) -> list:
    """The declared polymorphic-Role tie-breaker ordering (high->low); [] when absent (fog unresolved)."""
    rp = doc.get("role_priority")
    return [str(r) for r in rp] if isinstance(rp, list) else []


def resolve_role(matched_roles: list, priority: list):
    """Deterministic polymorphic-Role tie-breaker (WS-C spot-8, CTO @055731Z). Given the roles a node's edges
    matched, return the HIGHEST-priority one per `priority`. PURE, and DEPENDS ON role_priority (the property
    CTO's load-bearing mutant proves): 0 matches -> None (a base/non-role type, never an error); 1 match -> that
    role (priority not consulted); 2+ -> priority arbitrates. Raises ValueError if a matched role is absent from
    `priority` (an incomplete order cannot arbitrate -- surfaced, never guessed)."""
    matched = [r for r in matched_roles if r]
    if not matched:
        return None
    absent = [r for r in matched if r not in priority]
    if absent:
        raise ValueError("role(s) %s absent from role_priority -- cannot arbitrate (totality broken)" % absent)
    return min(matched, key=priority.index)


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
    rp = role_priority(doc)
    if rp:
        print("  role_priority tie-breaker (WS-C spot-8): %d-role total order, high->low: %s" % (len(rp), ", ".join(rp)))
    else:
        print("  role_priority tie-breaker (WS-C spot-8): ABSENT -- polymorphic-Role resolution is unresolved (the fog)")
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

    # --- WS-C spot-8: the role-resolve DETERMINISTIC tie-breaker, to CTO's enforcement gate-bar (a)-(d) @055731Z ---
    PRIO = ["Custodian", "Observer", "Gateway", "Guard", "Router", "Registry", "Trigger", "Container",
            "Transformer", "Producer", "Consumer", "Source", "Store", "Sink"]
    # (a) POSITIVE: guards+transforms -> Guard (Guard beats Transformer per the ratified order).
    a = resolve_role(["Transformer", "Guard"], PRIO) == "Guard"
    # (b) LOAD-BEARING MUTANT (CTO: the test that PROVES the control -- the SAME node must resolve DIFFERENTLY
    #     under a mutated priority; a test that passes with OR without role_priority is an instrument that cannot
    #     fail). REVERSED order -> Transformer now outranks Guard -> different answer. REMOVED -> cannot arbitrate.
    b_rev = resolve_role(["Transformer", "Guard"], list(reversed(PRIO))) == "Transformer"
    try:
        resolve_role(["Transformer", "Guard"], [])   # REMOVED priority
        b_removed = False                             # a resolver that answered anyway is NOT depending on role_priority
    except ValueError:
        b_removed = True
    b = b_rev and b_removed
    # (c) TOTALITY: the lint FIRES on an omission + on a duplicate rank; PASSES on the complete unique order.
    _roles = {r: {} for r in PRIO}
    c = (not any("(3)" in v for v in lint({"roles": _roles, "role_priority": PRIO}))
         and any("OMITS" in v for v in lint({"roles": _roles, "role_priority": PRIO[:-1]}))
         and any("DUPLICATE" in v for v in lint({"roles": _roles, "role_priority": PRIO[:-1] + ["Guard"]})))
    # (d) DEGENERATE: 0 matches -> None (not error); exactly 1 -> that role (priority arbitrates 2+ ONLY).
    d = resolve_role([], PRIO) is None and resolve_role(["Store"], PRIO) == "Store"
    wsc = a and b and c and d
    print("  WS-C role-resolve (a-positive=%s, b-LOAD-BEARING-mutant[rev->Transformer=%s, removed->raises=%s], "
          "c-totality=%s, d-degenerate=%s): %s" % (a, b_rev, b_removed, c, d, "PASS" if wsc else "FAIL"))
    ok &= wsc

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
    if cmd == "role-resolve":
        # comp-ontolint role-resolve <Role> <Role> ... -> the deterministic winner per role_priority (WS-C spot-8).
        matched = [a for a in args[1:] if not a.startswith("--")]
        try:
            doc = _load(_DEFAULT_RULE_BANK)
        except (OSError, ValueError, ImportError) as e:
            print("ERROR: %s" % e)
            return 2
        prio = role_priority(doc)
        if not prio:
            print("ERROR: role_priority absent from the rule-bank -- cannot arbitrate (the WS-C fog is unresolved)")
            return 2
        try:
            winner = resolve_role(matched, prio)
        except ValueError as e:
            print("VIOLATION: %s" % e)
            return 1
        print("role-resolve %s -> %s" % (matched, winner if winner is not None else "(no role -- base/non-role type)"))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
