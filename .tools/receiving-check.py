#!/usr/bin/env python
"""receiving-check -- run the RECEIVING gate on an artifact BEFORE you accept it.

ANDREW-DIRECT 2026-09-10 ~20:0xZ at the 1.0.0_SA_CTO~Z terminal, choosing this from three proposed
refinements: "The best one is the receiving check. I dont think we can do anything about the rest."

WHAT IT IS FOR. Under the canonical workflow an artifact crosses a seat boundary at nearly every
limb: the CTO hands a PRD to the COO, the COO hands a task order to a worker, the worker hands an
instance to the CVO, the CVO hands a slug to the CTO. AT EVERY ONE OF THOSE HANDOFFS THE RECEIVER
CAN GRADE WHAT IT WAS GIVEN BEFORE BUILDING ON IT -- and mostly does not, because doing so means
knowing which of six tools owns that artifact type and how to invoke it.

WHY IT EXISTS, AND THE DAY IS THE ARGUMENT. On 2026-09-10 every defect that mattered was caught by
a PERSON READING CAREFULLY and none by machinery:
  - 2.0.0_SA_COO~ZZZ ran the L6 gate's own functions against a landed PRD before cutting against it,
    found THREE refusals, and handed it back. That PRD had ZERO OUTCOME CARDS.
  - 0.0.0_AB_MSTR~Z measured who had actually authored tree registrations before accepting a claim
    that it was blocking one.
  - 4.0.0_SA_CRO~Z measured a source a PRD constraint NAMED, and found the page could not work.
  - 3.0.0_SA_CVO~Z re-read eight grades against the bar directly above the one that had been graded.
THE FIRST OF THOSE IS THE MODEL AND IT HAPPENED BECAUSE THAT LANE WAS DILIGENT, NOT BECAUSE ANYTHING
REQUIRED IT. Readers do not scale and they get tired. This makes the check one command.

⛔ THE DESIGN RULE THAT MATTERS MOST: AN UNKNOWN ARTIFACT TYPE MUST NOT RETURN CLEAN. A dispatcher
that prints nothing for an artifact it does not recognise tells the receiver "accepted" while nothing
ran. That is the exact failure this tool exists to prevent, and it is a failure this estate committed
twice on the day the tool was written -- a gate invoked on a PRD it did not classify printed NOTHING
and was read as a pass, and a census glob with a typo returned "0" over a denominator of 0. So the
verdict vocabulary has FOUR values and silence is not one of them:

    ACCEPT     a checker ran and the artifact passed it
    HAND BACK  a checker ran and the artifact failed it -- the output names what and to whom
    NOT-BOUND  a proof-of-spec instance was handed over WITHOUT the order it closes. Nothing ran:
               the checker would otherwise read its governing order from the instance's OWN
               decomp_ref.to_ref, a field the graded party writes, so any verdict would be one the
               instance steered. Re-run with --governing-order <the order you were handed with it>.
    UNCHECKED  NO checker exists for this artifact type. Accepting is a JUDGMENT CALL, not a
               verified act, and the verdict says so in those words.

THE L7 -> L8 ROUTE BINDS THE ORDER (2026-09-14, IRPT_FNTEND FE-s-43; 1.0.0_SA_CTO RULING AA, round-6
analysis @4713211d87 s.3; row IRPT_FNTEND-W4-S14 as graduated by 3.0.0_SA_CVO in C-S90). The proof
route used to pass the instance and nothing else, so its verdict came from whatever order the
instance's own to_ref named: 3.0.0_SA_CVO's arm C showed an unbound call still steered by a doctored
to_ref. RULING S (FE-s-37) had already bound the complete-flip path; this binds the receiving one.
The receiver passes the order it was handed, the route hands it to proof-of-spec-check.py as
--governing-order, and the checker refuses an instance whose to_ref or to_id names another order.
Every other route is unchanged: --governing-order binds the proof route and nothing else.

⛔ IT RE-IMPLEMENTS NOTHING. Every check is the OWNING TOOL, invoked as a subprocess, with that
tool's own output shown verbatim. Two carriers of one rule drift from the minute the second is
written -- this file is a DISPATCHER and a REPORTER, never a second opinion.

⛔ IT IS READ-ONLY AND REFUSES NOTHING AT COMMIT TIME. It grades an artifact you were HANDED. The
commit-time gates are separate and unchanged; this does not wrap, replace or weaken them, and a lane
that skips it is not blocked -- it is simply accepting on its own judgment rather than on a check.

USAGE:
  receiving-check.py <path>...                              grade the artifact(s) you are about to accept
  receiving-check.py <instance> --governing-order <order>   grade a proof-of-spec instance against the
                                                            order it closes (required for that route)
  receiving-check.py --boundaries  print which canonical-flow handoffs HAVE a receiving check
  receiving-check.py --self-test   classification + dispatch controls, both directions
"""
import os
import re
import subprocess
import sys
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# THE DISPATCH TABLE IS DATA SO IT CAN BE READ AND ARGUED WITH.
# (pattern, artifact label, tool, argv-builder, the handoff it sits on)
# ---------------------------------------------------------------------------
ROUTES = [
    (re.compile(r"/prd/[^/]*_PRD_ADDENDUM[^/]*\.md$", re.I),
     "PRD addendum", "prd-manifest-gate.py", lambda p: [p],
     "L4 -> L5  (CTO hands an amended spec to the COO)"),
    (re.compile(r"/prd/[^/]*_PRD\.md$", re.I),
     "step-4 PRD", "prd-manifest-gate.py", lambda p: [p],
     "L4 -> L5  (CTO hands the spec to the COO)"),
    (re.compile(r"/task-orders/[^/]+\.md$", re.I),
     "task order", "to-pipeline-gate.py", lambda p: [p],
     "L6 -> L7  (COO hands an order to a worker)"),
    (re.compile(r"proof_of_spec[^/]*\.json$", re.I),
     "proof-of-spec instance", "proof-of-spec-check.py",
     lambda p, order=None: [p] + (["--governing-order", order] if order else []),
     "L7 -> L8  (worker hands an instance to the CVO)"),
    (re.compile(r"/surprise-channel/", re.I),
     "surprise-channel row set", "surprise-row-gate.py", lambda p: [p],
     "ANY      (a row crossing into a drain or a slug)"),
    (re.compile(r"(^|/)project\.json$|^org/projects/[^/]+\.json$", re.I),
     "register row", "missions-tree-index.py", lambda p: ["check"],
     "L3       (the register the row must appear in)"),
]

# THE ROUTES THAT TAKE THE GOVERNING ORDER (FE-s-43). Only the proof-of-spec checker grades an artifact against the
# order it closes; every other route's argv-builder is never handed the order, so its argv is what it was.
BOUND_TOOLS = {"proof-of-spec-check.py"}

NOT_BOUND_BODY = (
    "nothing ran. A proof-of-spec instance is graded against the ORDER IT CLOSES, and no order was handed over. "
    "Unbound, proof-of-spec-check.py reads its governing order from the instance's own decomp_ref.to_ref (else its "
    "to_id) -- fields the graded party writes -- so a verdict here would be one the instance steered (1.0.0_SA_CTO "
    "RULING AA; row IRPT_FNTEND-W4-S14). Re-run with the order you were handed: "
    "receiving-check.py <instance> --governing-order <task-order.md>")

# HANDOFFS WITH NO RECEIVING CHECK -- NAMED, NOT HIDDEN. Printed by --boundaries so the gap is
# legible rather than discovered by a lane that assumed silence meant clean.
UNCOVERED = [
    ("decomposition", "org/missions/**/decompositions/*.md",
     "L5 -> L6  (the COO's own cut, read back before issuance)"),
    ("round analysis", "org/missions/**/ledger/ROUND_ANALYSIS.round*.md",
     "L10 -> recut  (CTO hands the analysis to the COO)"),
    ("completion report", "org/missions/**/ledger/COMPLETION_REPORT.round*.json",
     "L7 -> L8  (schema-validated by the COO at write; no RECEIVING check)"),
    ("L1 brief", "docs/briefs/*.md",
     "L1 -> L2  (CRO hands the brief to the CTO)"),
]


def _order_arg(governing_order):
    """The order as an ABSOLUTE path, or None. The checker resolves a relative --governing-order against ITS OWN
    tree, not the caller's cwd, so a receiver running from a subdirectory would otherwise bind the wrong file."""
    if not governing_order:
        return None
    return os.path.abspath(governing_order)


def classify(path, governing_order=None):
    """(label, tool, argv, handoff) or None. FIRST match wins and the order is deliberate:
    the addendum pattern precedes the PRD pattern because an addendum also ends in .md and would
    otherwise be graded as a PRD -- which would demand a surface manifest of a pointer file.
    `governing_order` reaches only a BOUND_TOOLS route's argv; every other route ignores it."""
    q = path.replace("\\", "/")
    for rx, label, tool, argvf, handoff in ROUTES:
        if rx.search(q):
            if tool in BOUND_TOOLS:
                return label, tool, argvf(path, _order_arg(governing_order)), handoff
            return label, tool, argvf(path), handoff
    return None


def run_one(path, governing_order=None):
    """Grade one artifact. Returns (verdict, label, output). A BOUND_TOOLS route with no governing order returns
    NOT-BOUND without running anything: an unbound proof verdict is the instance's own, never the receiver's."""
    hit = classify(path, governing_order)
    if hit is None:
        return ("UNCHECKED", "unrecognised", "")
    label, tool, argv, _handoff = hit
    if tool in BOUND_TOOLS and not governing_order:
        return ("NOT-BOUND", label, NOT_BOUND_BODY)
    tp = os.path.join(HERE, tool)
    if not os.path.exists(tp):
        return ("UNCHECKED", label,
                "the owning tool %s is NOT PRESENT on this device -- nothing ran" % tool)
    try:
        out = subprocess.run([sys.executable, tp] + argv,
                             capture_output=True, text=True, timeout=180)
    except Exception as exc:  # noqa: BLE001
        return ("UNCHECKED", label, "the owning tool did not run (%s)" % exc)
    body = ((out.stdout or "") + (out.stderr or "")).strip()
    return ("ACCEPT" if out.returncode == 0 else "HAND BACK", label, body)


def _print_body(body):
    """The owning tool's output, WRAPPED and never truncated: a violation naming two paths is longer than a line,
    and cutting it at a fixed width dropped the second path from the very hand-back that has to name it. A wrapped
    continuation carries its OWN gutter (`:`), because the owning tools indent their own lines and a `|` gutter
    would make a continuation indistinguishable from an indented line."""
    for line in body.split("\n"):
        parts = textwrap.wrap(line, 150, break_long_words=False, break_on_hyphens=False) or [""]
        print("      | %s" % parts[0])
        for cont in parts[1:]:
            print("      :   %s" % cont)


def run(paths, governing_order=None):
    rows = [(p,) + run_one(p, governing_order) for p in paths]
    print("RECEIVING CHECK -- %d artifact(s)" % len(rows))
    if governing_order:
        print("  governing order handed over: %s (binds the proof-of-spec route only)" % governing_order)
    print("=" * 78)
    for p, verdict, label, body in rows:
        print("  %-10s %-26s %s" % (verdict, label, p))
        if body:
            _print_body(body)
    print("=" * 78)
    n_hb = sum(1 for r in rows if r[1] == "HAND BACK")
    n_un = sum(1 for r in rows if r[1] == "UNCHECKED")
    n_ok = sum(1 for r in rows if r[1] == "ACCEPT")
    n_nb = sum(1 for r in rows if r[1] == "NOT-BOUND")
    n_bound_route = sum(1 for p in paths if (classify(p) or ("", ""))[1] in BOUND_TOOLS)
    if n_nb:
        print("VERDICT: %d ACCEPT | %d HAND BACK | %d NOT-BOUND | %d UNCHECKED" % (n_ok, n_hb, n_nb, n_un))
    else:
        print("VERDICT: %d ACCEPT | %d HAND BACK | %d UNCHECKED" % (n_ok, n_hb, n_un))
    if n_hb:
        print("  >> DO NOT BUILD ON IT. Hand it back to the artifact's author with the output above.")
        print("     A defect found at the handoff costs one message; the same defect found after a")
        print("     cut costs a round.")
    if n_nb:
        print("  >> NOT-BOUND IS NOT ACCEPT. A proof-of-spec instance is graded against the order it")
        print("     closes and none was handed over, so nothing ran and there is no verdict to quote.")
        print("     Re-run: receiving-check.py <instance> --governing-order <the task order>.")
    if n_un:
        print("  >> UNCHECKED IS NOT ACCEPT. No checker exists for that artifact type on this")
        print("     device, so accepting it is YOUR JUDGMENT and not a verified act. Say which in")
        print("     your acceptance message -- 'receiving-check: UNCHECKED' is an honest line.")
    if governing_order and not n_bound_route:
        print("  NOTE: --governing-order was given but no proof-of-spec instance was among the artifacts;")
        print("        it bound nothing.")
    if n_ok and not n_hb and not n_un and not n_nb:
        print("  >> Safe to build on, and say so: cite the tool that passed it, not this wrapper.")
    return 1 if (n_hb or n_nb) else 0


def boundaries():
    print("CANONICAL-FLOW HANDOFFS AND THEIR RECEIVING CHECKS")
    print("=" * 78)
    print("COVERED -- the receiver can grade what it was handed:")
    for _rx, label, tool, _a, handoff in ROUTES:
        present = "" if os.path.exists(os.path.join(HERE, tool)) else "   [TOOL ABSENT]"
        bound = "   [binds --governing-order]" if tool in BOUND_TOOLS else ""
        print("  %-28s %-24s %s%s%s" % (handoff, label, tool, present, bound))
    print()
    print("NOT COVERED -- accepting these is a judgment call and the tool says so:")
    for label, glob, handoff in UNCOVERED:
        print("  %-28s %-24s %s" % (handoff, label, glob))
    print()
    print("  This list is the point. A gap you can SEE is a decision; a gap you cannot is a")
    print("  silent pass. Nothing here is a proposal to build four more gates -- most of these")
    print("  handoffs may not warrant one, and that is a judgment for their owners.")
    return 0


def self_test():
    """Classification in BOTH directions, and the dispatcher's own failure mode."""
    cases = [
        ("org/missions/D5/AMGT/X/prd/X_PRD.md", "step-4 PRD"),
        ("org/missions/D5/AMGT/X/prd/X_PRD_ADDENDUM_01.md", "PRD addendum"),
        ("org/missions/D12/NFRA/X/task-orders/X.TO-a-1.thing.md", "task order"),
        ("org/missions/D12/NFRA/X/deliverables/W~1/X.TO-a-1.proof_of_spec.json",
         "proof-of-spec instance"),
        ("org/missions/D12/NFRA/X/surprise-channel/investigations/INVESTIGATION_v1.md",
         "surprise-channel row set"),
        ("org/missions/D5/AMGT/X/project.json", "register row"),
        ("org/projects/AMGT_RESAPP.json", "register row"),
        # MUST NOT CLASSIFY -- silence here is the whole hazard, so it is asserted explicitly
        ("org/missions/D5/AMGT/X/decompositions/X_DECOMP.md", None),
        ("docs/briefs/some-brief.md", None),
        ("docs/architecture/SOMETHING_PRD.md", None),   # not under a tree prd/ folder
        ("README.md", None),
    ]
    ok = True
    for path, expect in cases:
        hit = classify(path)
        got = hit[0] if hit else None
        good = got == expect
        if not good:
            ok = False
        print("  [%s] %-62s -> %s" % ("PASS" if good else "FAIL", path[-62:], got))

    # ORDER CONTROL: the addendum rule must win over the PRD rule, or an addendum is graded as a
    # PRD and refused for lacking a surface manifest it was never meant to carry.
    add = classify("a/prd/X_PRD_ADDENDUM_01.md")
    order_ok = add is not None and add[0] == "PRD addendum"
    if not order_ok:
        ok = False
    print("  [%s] ORDER-CONTROL  addendum pattern precedes the PRD pattern" %
          ("PASS" if order_ok else "FAIL"))

    # VERDICT CONTROL: an unclassified path must return UNCHECKED and never ACCEPT.
    v, _lbl, _b = run_one("README.md")
    v_ok = v == "UNCHECKED"
    if not v_ok:
        ok = False
    print("  [%s] VERDICT-CONTROL  an unrecognised artifact returns %r, not ACCEPT" %
          ("PASS" if v_ok else "FAIL", v))

    # BINDING CONTROLS (FE-s-43). An instance received WITHOUT its order reads NOT-BOUND and runs nothing (the
    # path need not exist: a run would have failed on it, so a NOT-BOUND here proves nothing was invoked); WITH its
    # order the argv carries --governing-order and the ABSOLUTE order path; every other route ignores the order.
    inst = "org/missions/D12/NFRA/X/deliverables/W~1/X.TO-a-1.proof_of_spec.json"
    order = "org/missions/D12/NFRA/X/task-orders/X.TO-a-1.thing.md"
    nb, _lbl, nb_body = run_one(inst)
    nb_ok = nb == "NOT-BOUND" and nb_body.startswith("nothing ran")
    if not nb_ok:
        ok = False
    print("  [%s] BINDING-CONTROL  an instance received with no order returns %r and runs nothing" %
          ("PASS" if nb_ok else "FAIL", nb))
    argv = (classify(inst, order) or ("", "", []))[2]
    argv_ok = argv == [inst, "--governing-order", os.path.abspath(order)]
    if not argv_ok:
        ok = False
    print("  [%s] BINDING-ARGV  the proof route hands the order over as --governing-order <absolute path>" %
          ("PASS" if argv_ok else "FAIL"))
    others = [p for p, e in cases if e and e != "proof-of-spec instance"]
    same = [p for p in others if classify(p, order) == classify(p)]
    same_ok = len(same) == len(others)
    if not same_ok:
        ok = False
    print("  [%s] BINDING-SCOPE  --governing-order changes no other route's classification or argv: %d of %d" %
          ("PASS" if same_ok else "FAIL", len(same), len(others)))

    # TOOL-PRESENCE CONTROL: every route names a tool that exists, or --boundaries lies.
    for _rx, label, tool, _a, _h in ROUTES:
        p = os.path.exists(os.path.join(HERE, tool))
        if not p:
            ok = False
        print("  [%s] TOOL-PRESENCE  %-26s %s" % ("PASS" if p else "FAIL", label, tool))

    print("SELF-TEST: %s" % ("ALL HOLD" if ok else "BROKEN"))
    return 0 if ok else 1


def _lift_order(argv):
    """(paths, governing_order, error). --governing-order is lifted out of argv FIRST (the checker's own shape), so
    the positional contract -- one or more artifact paths -- is exactly what it was."""
    rest, order, i = [], None, 0
    while i < len(argv):
        a = argv[i]
        if a == "--governing-order" or a.startswith("--governing-order="):
            val = a.split("=", 1)[1] if "=" in a else (argv[i + 1] if i + 1 < len(argv) else "")
            i += 1 if "=" in a else 2
            if not val.strip():
                return None, None, "--governing-order needs the path of the order the instance closes"
            if order is not None:
                return None, None, "--governing-order was given twice; one call binds one order"
            order = val
            continue
        rest.append(a)
        i += 1
    if not rest:
        return None, None, "no artifact path was given"
    return rest, order, None


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)
    if args[0] == "--self-test":
        sys.exit(self_test())
    if args[0] == "--boundaries":
        sys.exit(boundaries())
    paths, gov, err = _lift_order(args)
    if err:
        print("USAGE-ERROR (rc=2): %s" % err)
        sys.exit(2)
    sys.exit(run(paths, gov))
