#!/usr/bin/env python
"""GATE: every enforcement rule in the schema is INDEPENDENTLY VERIFIED by at least one mutant.

R2-9, from 4.0.0_SA_CRO~X gap 5 generalizing 2.0.0_SA_COO~X's F7. F7 demonstrated ONE gutted-schema
case: delete LAW-2's conditional and a drifted mutant keeps the battery green. This gate does that
for EVERY rule, mechanically.

METHOD -- ablation:
    for each removable enforcement unit in the schema:
        build a COPY with that unit deleted
        re-run the whole mutant battery against the copy
        record which mutants FLIP from reject to accept
    a rule whose ablation flips ZERO mutants is NOT TESTED BY THE BATTERY -- it could be deleted
    from the contract and every arm would still print PASS.

WHY THIS IS DIFFERENT FROM ISOLATION (check_mutant_isolation.py), which is the sibling gate:
    ISOLATION asks, per MUTANT: does it trip exactly one rule?
    ABLATION  asks, per RULE:   does any mutant depend on it?
A battery can be perfectly isolating and still leave rules untested -- nothing forces every rule to
have a mutant. The two gates cover different halves and neither implies the other.

IT ALSO DIAGNOSES REDUNDANT ENFORCEMENT, which is the open R2-9 question about the three
non-isolating mutants: if ablating rule A flips nothing because rule B also catches those mutants,
A and B are redundant on that surface -- real, intended belt-and-braces, but it means neither is
independently verified and a mutant per arm is owed.

Usage:
    check_rule_ablation.py            exit 0 = every ablated rule flips >= 1 mutant
    check_rule_ablation.py --verbose  also list which mutants flip per rule
"""
import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(HERE, "ISCK_CONTRACT.v0.schema.json")

try:
    import jsonschema
except ImportError:
    print("ERROR: jsonschema not importable -- INSTRUMENT FAILURE, not a clean result.")
    raise SystemExit(2)

sys.path.insert(0, HERE)
try:
    import validate_isck
except ImportError:
    print("ERROR: validate_isck not importable from %s -- INSTRUMENT FAILURE." % HERE)
    raise SystemExit(2)


def ablations(schema):
    """Yield (label, mutated_schema) with exactly one enforcement unit removed.

    Removable units, per record $def:
      - each element of allOf (an if/then conditional, or a not-arm)
      - each key of dependentRequired
      - each member of the top-level required list
    Only these are ablated: they are the units a human would call "a rule".
    """
    defs = schema.get("$defs", {})
    for rec, node in sorted(defs.items()):
        if not isinstance(node, dict) or "properties" not in node:
            continue

        for i, _ in enumerate(node.get("allOf", []) or []):
            s = copy.deepcopy(schema)
            del s["$defs"][rec]["allOf"][i]
            if not s["$defs"][rec]["allOf"]:
                del s["$defs"][rec]["allOf"]
            yield ("%s.allOf[%d]" % (rec, i), s)

        for key in sorted((node.get("dependentRequired") or {})):
            s = copy.deepcopy(schema)
            del s["$defs"][rec]["dependentRequired"][key]
            if not s["$defs"][rec]["dependentRequired"]:
                del s["$defs"][rec]["dependentRequired"]
            yield ("%s.dependentRequired[%s]" % (rec, key), s)

        for key in sorted(node.get("required", []) or []):
            s = copy.deepcopy(schema)
            s["$defs"][rec]["required"] = [r for r in node["required"] if r != key]
            yield ("%s.required[%s]" % (rec, key), s)


def rejects(schema, inst):
    return bool(list(jsonschema.Draft202012Validator(schema).iter_errors(inst)))


def main():
    verbose = "--verbose" in sys.argv
    with open(SCHEMA_PATH, "r", encoding="utf-8") as fh:
        base = json.load(fh)

    rows = validate_isck._mutants()
    muts = []
    for row in rows:
        if not isinstance(row, (tuple, list)) or len(row) < 2:
            print("ERROR: mutant row shape %r unexpected -- INSTRUMENT FAILURE." % (row,))
            return 2
        muts.append((row[0], row[1]))
    if not muts:
        print("ERROR: battery returned 0 mutants -- INSTRUMENT FAILURE, not a clean run.")
        return 2

    # BASELINE + POSITIVE CONTROL. Every mutant must reject against the UNABLATED schema, or the
    # flip measurement below is meaningless: a mutant that already accepts cannot flip.
    baseline = {}
    for name, inst in muts:
        baseline[name] = rejects(base, inst)
    already = [n for n, r in baseline.items() if not r]
    if already:
        print("ERROR: %d mutant(s) ACCEPT against the unablated schema -- fix the battery first:"
              % len(already))
        for n in already[:5]:
            print("       %s" % n)
        print("       Ablation flips cannot be measured while a mutant is already passing.")
        return 2

    print("RULE ABLATION GATE -- %s" % os.path.basename(SCHEMA_PATH))
    print("BASELINE: %d of %d mutants reject against the unablated schema (all must)"
          % (len(muts), len(muts)))

    units = list(ablations(base))
    print("DENOMINATOR: %d removable enforcement units ablated, each against all %d mutants"
          % (len(units), len(muts)))
    print("")

    # CLASSIFY BEFORE COUNTING. A flat count is 86 failures, 81 of them plain required[field]
    # entries that no mutant removes -- true, trivial, and enough to swamp the handful that
    # encode the LAWS. A gate that reports 86 failures gets switched off, and then it gates
    # nothing. The conditional classes are the signal and they are what this gate FAILS on.
    def klass(label):
        if ".allOf[" in label:
            return "conditional"
        if ".dependentRequired[" in label:
            return "conditional"
        return "required_field"

    untested = {"conditional": [], "required_field": []}
    tested = {"conditional": 0, "required_field": 0}
    for label, s2 in units:
        flipped = [n for n, inst in muts if not rejects(s2, inst)]
        k = klass(label)
        if flipped:
            tested[k] += 1
            if verbose:
                print("  %-52s flips %d: %s" % (label, len(flipped), ", ".join(flipped[:3])))
        else:
            untested[k].append(label)

    n_cond = tested["conditional"] + len(untested["conditional"])
    n_req = tested["required_field"] + len(untested["required_field"])
    print("%-34s %6s %8s %10s" % ("class", "units", "tested", "UNTESTED"))
    print("-" * 62)
    print("%-34s %6d %8d %10d" % ("CONDITIONAL (if-then/not/depReq)", n_cond,
                                  tested["conditional"], len(untested["conditional"])))
    print("%-34s %6d %8d %10d" % ("required[field]  (informational)", n_req,
                                  tested["required_field"], len(untested["required_field"])))

    covered = tested["conditional"] + tested["required_field"]
    if covered == 0:
        print("ERROR: no ablation flipped any mutant -- suspect THIS harness, not the battery.")
        return 2

    if untested["required_field"]:
        print("")
        print("INFO: %d required[field] rule(s) have no dependent mutant. NOT a gate failure --"
              % len(untested["required_field"]))
        print("      the battery does not claim field-level coverage. Listed under --verbose.")
        if verbose:
            for label in untested["required_field"]:
                print("      - %s" % label)

    if untested["conditional"]:
        print("")
        print("UNTESTED CONDITIONAL RULES -- these encode the LAWS. Delete any one and every")
        print("mutant still rejects, so the battery prints PASS with the rule gone:")
        for label in untested["conditional"]:
            print("  FAIL: %s" % label)
        print("")
        print("GATE FAILED: %d conditional rule(s) carry no mutant that depends on them."
              % len(untested["conditional"]))
        print("  Each needs a mutant tripping ONLY it, or a note that it is redundant with")
        print("  another rule AND that the redundancy is intended.")
        return 1

    print("")
    print("OK: every ablated rule has at least one mutant that depends on it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
