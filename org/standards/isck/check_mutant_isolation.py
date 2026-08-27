#!/usr/bin/env python
"""GATE: every mutant in the battery trips EXACTLY ONE schema rule (pass finding F7's companion).

WHY THIS EXISTS. The battery's own output cannot answer this. Every mutant fails the ROOT `oneOf`
and reports the identical, information-free verdict "not valid under any of the given schemas", so
"19 of 19 REJECT" says a mutant died -- never WHICH RULE KILLED IT. This gate bypasses the root
oneOf, validates each mutant against its OWN record $def, and counts distinct (keyword, schema
path) causes.

WHAT A NON-ISOLATING MUTANT COSTS: if a mutant trips two rules, deleting the one it NAMES leaves it
still rejecting -- so the battery stays green while the rule it was written to defend is gone.
Demonstrated against v0: with a drifted fixture, LAW 2's conditional could be removed from the
schema and the battery still printed 19 of 19 REJECT.

RELATIONSHIP TO ATTRIBUTION, because they are different questions that happened to agree at v0:
    ISOLATION   (this gate)  does the mutant trip exactly ONE rule?
    ATTRIBUTION (DT~X's)     is it the RIGHT rule?
A mutant can isolate perfectly and still test the wrong thing. Run both; neither substitutes.

Origin: 19 of 19 isolating at the frozen v0 target @8ba18439dd -- the negative arm VERIFIED, not
merely unbroken (2.0.0_SA_COO~X, ISCK adversarial pass round 1). Re-run after every change to the
conditionals or that verification is stale.

Usage:
    check_mutant_isolation.py    exit 0 = every mutant isolates and none validates
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(HERE, "ISCK_CONTRACT.v0.schema.json")

try:
    import jsonschema
except ImportError:
    print("ERROR: jsonschema not importable -- cannot run. This is an INSTRUMENT failure,")
    print("       not a clean result. Do not read this as 'no isolation defects'.")
    raise SystemExit(2)

sys.path.insert(0, HERE)
try:
    import validate_isck
except ImportError:
    print("ERROR: validate_isck not importable from %s -- instrument failure, not a result." % HERE)
    raise SystemExit(2)


def main():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as fh:
        schema = json.load(fh)
    defs = schema["$defs"]

    muts = validate_isck._mutants()
    if not muts:
        print("ERROR: battery returned 0 mutants -- instrument failure, NOT a clean run")
        return 2

    print("MUTANT ISOLATION GATE -- %s" % os.path.basename(SCHEMA_PATH))
    print("DENOMINATOR: %d mutants" % len(muts))
    print("")

    bad_multi, bad_valid, bad_norec = [], [], []
    # The battery widened from (name, inst) to (name, inst, expected_reason) when v0.1's
    # expected-reason assertions landed. Unpack DEFENSIVELY: a shape change must degrade to a
    # NAMED instrument failure, never a traceback -- a crash is easy to read as "gate is broken,
    # skip it", which is how a gate quietly stops gating.
    norm = []
    for row in muts:
        if not isinstance(row, (tuple, list)) or len(row) < 2:
            print("ERROR: mutant row shape %r unexpected -- INSTRUMENT FAILURE, not a result" % (row,))
            return 2
        norm.append((row[0], row[1]))

    for name, inst in norm:
        rt = inst.get("record_type")
        if rt not in defs:
            bad_norec.append((name, rt))
            print("%-54s ERROR: record_type %r has no $def" % (name[:54], rt))
            continue
        sub = {"$ref": "#/$defs/%s" % rt, "$defs": defs}
        errs = list(jsonschema.Draft202012Validator(sub).iter_errors(inst))
        if not errs:
            bad_valid.append(name)
            print("%-54s VALIDATES -- hole in the contract" % name[:54])
            continue
        causes = {(e.validator, str(e.absolute_schema_path)) for e in errs}
        flag = "" if len(causes) == 1 else "  NON-ISOLATING"
        if len(causes) > 1:
            bad_multi.append((name, sorted(kw for kw, _ in causes)))
        print("%-54s causes=%d%s" % (name[:54], len(causes), flag))

    print("")
    isolating = len(norm) - len(bad_multi) - len(bad_valid) - len(bad_norec)
    print("ISOLATING: %d of %d" % (isolating, len(norm)))

    # POSITIVE CONTROL on the gate itself: if NOTHING isolates, suspect the harness, not the
    # battery. A uniform result across a whole set is an instrument signature.
    if isolating == 0:
        print("ERROR: zero mutants isolated -- suspect this harness, not the battery.")
        return 2

    rc = 0
    for name, rt in bad_norec:
        print("FAIL: %-46s unknown record_type %r" % (name, rt))
        rc = 1
    for name in bad_valid:
        print("FAIL: %-46s VALIDATES against its own $def" % name)
        rc = 1
    for name, kws in bad_multi:
        print("FAIL: %-46s trips %d rules %s -- delete the rule it names and it still rejects"
              % (name, len(kws), kws))
        rc = 1

    if rc == 0:
        print("OK: every mutant trips exactly one rule. The negative arm can fail at the field")
        print("    under test. NOTE: isolation is not attribution -- run the attribution probe too.")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
