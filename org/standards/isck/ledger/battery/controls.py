#!/usr/bin/env python
"""NON-MANIFEST controls: rules the ledger enforces that the PINNED battery has no arm for.

WHY THIS FILE EXISTS, and it is a correction rather than a design. The wave-2 resolver commit
d6ed40dc6e implemented sec 2d's class half -- STRICT means "resolve ... to a record OF THE NAMED
CLASS" -- and its commit body said the rule was "exercised by a control in this commit". It was
not. The control was run in a shell and the OBJECT BYTES carried no trace of it. 3.0.0_SA_CVO~X
read the commit scope, found no such fixture, and blocked AC2's evidence: correctly, because a
control that exists only as a sentence in a commit message is a description of a protection, not a
protection. The message scrolls; the artifact persists. This file is the artifact.

WHAT IS AND IS NOT IN HERE. The pinned battery's denominator is generated from the design at
d0398b977d, and the spec is frozen mid-round -- so a rule the design does not name an arm for
cannot be added to MANIFEST.json without moving a vintage every wave-2 evidence line cites
(issuer 111357Z). These controls therefore carry NO manifest arm ids, are never counted in
`ran N of N`, and are run by their own command. They are evidence for a cell, beside the arms,
with the coverage gap RECORDED rather than hidden.

RUN: `python controls.py` -- every control prints its own line; exit 1 if any did not behave.
Each control has BOTH directions, because a refusal with no admitted sibling proves only that the
ledger says no.
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from ledger import engine                                              # noqa: E402
from ledger.battery.arms import row_02_resolver as R                   # noqa: E402

RESULTS = []


def control(name):
    def deco(fn):
        RESULTS.append((name, fn))
        return fn
    return deco


def _store(tag):
    path = os.path.join(tempfile.mkdtemp(), "%s.sqlite" % tag)
    store = engine.Store(path)
    R.build_universe(store)
    return store


@control("C1 wrong-class scalar reference is REFUSED, with the right attribution")
def c1():
    """entity_binding.entity_serial pointing at a MATERIALIZER: resolves, wrong class."""
    store = _store("c1")
    rec = R._base(store, "entity_binding", "bind:control")
    rec["entity_serial"] = R.SEED["materializer"]
    try:
        store.admit([rec])
    except engine.Rejected as exc:
        expected = "L-02-unresolved-entity_binding.entity_serial"
        if exc.rule != expected:
            return False, "refused, but as %s not %s" % (exc.rule, expected)
        if "record_type" not in str(exc) and "materializer" not in str(exc):
            return False, "refused without naming the class it found"
        return True, "refused as %s" % exc.rule
    return False, "ADMITTED -- a binding whose entity_serial is a materializer"


@control("C2 right-class sibling is ADMITTED (the arm that makes C1 mean something)")
def c2():
    store = _store("c2")
    rec = R._base(store, "entity_binding", "bind:control")
    rec["entity_serial"] = R.SEED["entity"]
    try:
        store.admit([rec])
        return True, "admitted"
    except engine.Rejected as exc:
        return False, "REFUSED as %s -- then C1 proves nothing but 'the ledger says no'" % exc.rule


@control("C3 wrong-class inside an ARRAY field is REFUSED (the shape a resolver skips)")
def c3():
    """A scalar-only resolver ignores list items entirely; this is the value nobody checks."""
    store = _store("c3")
    rec = R._base(store, "materialization_run", "run:control")
    rec["output_surface_version_ids"] = [R.SEED["materializer"]]        # not a surface_version
    try:
        store.admit([rec])
    except engine.Rejected as exc:
        expected = "L-02-unresolved-materialization_run.output_surface_version_ids[]"
        return (exc.rule == expected), "refused as %s" % exc.rule
    return False, "ADMITTED -- a wrong-class id inside a list was never inspected"


@control("C4 right-class ARRAY sibling is ADMITTED")
def c4():
    store = _store("c4")
    rec = R._base(store, "materialization_run", "run:control")
    rec["output_surface_version_ids"] = [R.SEED["surface_version"]]
    try:
        store.admit([rec])
        return True, "admitted"
    except engine.Rejected as exc:
        return False, "REFUSED as %s" % exc.rule


def main():
    print("NON-MANIFEST CONTROLS -- sec 2d's class half. These are NOT battery arms and are not "
          "counted in `ran N of N`; the pinned battery names no arm for this rule.")
    ok = True
    for name, fn in RESULTS:
        try:
            passed, detail = fn()
        except Exception as exc:                                       # noqa: BLE001
            passed, detail = False, "%s: %s" % (type(exc).__name__, exc)
        ok = ok and passed
        print("  %-64s %s  %s" % (name, "PASS" if passed else "FAIL", detail))
    print("RESULT: %s -- COUNTED %d controls"
          % ("all controls behaved as declared" if ok else "A CONTROL DID NOT BEHAVE", len(RESULTS)))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
