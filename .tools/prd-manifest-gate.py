#!/usr/bin/env python
"""prd-manifest-gate -- a step-4 PRD may not be COMMITTED without a SURFACE MANIFEST.

ANDREW-DIRECT 2026-09-09 ~19:2xZ at the 1.0.0_SA_CTO~Z terminal, VERBATIM:
  "the surface_manifest first of all is mandatory; a PRD literally cannot be committed unless
   it has one."

WHAT THIS CHANGES, and it is a MOVE rather than a NEW RULE. The estate ALREADY required a
surface manifest -- org/standards/PRD_HEADER.schema.json says the step-6 TO gate "refuses a TO
whose PRD lacks this block, the ENDPOINT section, or the surface manifest", and then states the
consequence plainly: "A PRD with no header is not refused by itself -- a TO cut against it is."
So the refusal sat at L6 and pointed at the COO's task order, never at the CTO's PRD.

THAT IS EXACTLY HOW NFRA_REPORT v0.1 COMMITTED CLEAN WITH NO MANIFEST (@ff9900b0ea). The author
was not refused; the consumer would have been, one step later, for the author's omission. The
gap was found by Andrew and independently by 2.0.0_SA_COO~ZZ (msg 20590) -- by two readers, not
by the machinery. This gate moves the refusal to the act that creates the defect.

DISCRIMINATOR -- WHY THIS DOES NOT DEMAND A MANIFEST FROM 197 OTHER FILES. `*_PRD.md` is NOT the
same set as "step-4 project PRD": 205 tracked *_PRD.md, and only 8 carry a PRD_HEADER with
`step: 4`. The schema declares that field's purpose in its own words -- "Always 4. Present so a
consumer can reject a document that merely LOOKS like a PRD." So THAT is the discriminator, and
an architecture doc named *_PRD.md is simply not in the domain.

BLAST RADIUS, MEASURED BEFORE SHIPPING (2026-09-09 @f060f2354e, printed by --census):
  205 tracked *_PRD.md | 187 no fenced json header | 4 header unparseable | 8 step-4 PRDs
  STEP-4 PRDs THIS GATE WOULD REFUSE TODAY: 0 of 8.
A gate that wedges the estate is worse than the gap it closes, so the population was censused
BEFORE the gate was written rather than after it refused someone. Because the refused set is
empty, this ships fail-closed with NO legacy carve-out and NO prospective-only machinery -- the
surprise-row-gate needs those because ~190 legacy rows predate it; this one does not.

NO AUDITED OVERRIDE, DELIBERATELY. Every sibling gate carries one. Andrew's word is "literally
cannot", the measured wedge risk is zero, and an escape hatch on a one-line requirement is an
invitation to use it. REVERSIBLE IN ONE WORD if that proves wrong -- this paragraph is the flag.

ONE DETECTOR, ONE PRIMARY. The manifest test is NOT re-implemented here. It is IMPORTED from
.tools/to-pipeline-gate.py (_top_section + MANIFEST_HEADING_RE + PRD_FENCE_RE +
MANIFEST_MIN_BODY_CHARS), which is the same code the L6 limb runs and which CVO~A already
hardened @d019922d68 against two false passes: a heading INSIDE a code fence, and a heading with
an empty body. Two carriers of one rule drift from minute one; this file is a CALLER, not a copy.

  CORRECTED 2026-09-09 on 3.0.0_SA_CVO~Z's verification (msg 20602), and the correction is
  against THIS FILE'S OWN CLAIM. The first cut said the two gates "cannot drift apart". That was
  TRUE of the two symbols it imported and FALSE of the THIRD thing the gates share: the
  emptiness floor, which was a duplicated literal `40` in both files. Both read 40, so nothing
  had diverged -- but the property CLAIMED was structural and this limb did not have it, and
  tuning the floor in one file would have made the L4 and L6 refusals disagree SILENTLY, which
  is the exact outcome importing was chosen to prevent. The floor is now a NAMED CONSTANT in the
  primary and imported here. The shape is worth naming because it is general: a property
  verified on the limbs it names, with an untested limb sitting inside the same claim.

THE FLOOR IS UNMEASURED AND SAYS SO. 40 is inherited; no derivation appears in either file's
history and none is invented here. What is new is that it is CONTROLLED AT ITS BOUNDARY by
--self-test below (39 chars must refuse, 41 must pass), so a change to it fails a test rather
than silently splitting the two gates.

GRADES THE STAGED BLOB, not the worktree -- the staged bytes are what the commit will contain.

USAGE:
  prd-manifest-gate.py <path>...    grade these paths (safe-commit passes its pathspec)
  prd-manifest-gate.py --self-test  refuse-fixture + positive control, both must hold
  prd-manifest-gate.py --census     print the population and what would be refused today
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _load_tpg():
    """Import the L6 gate as a module so the manifest test has exactly ONE implementation."""
    path = os.path.join(HERE, "to-pipeline-gate.py")
    if not os.path.exists(path):
        return None
    spec = importlib.util.spec_from_file_location("_tpg_for_prd_gate", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _staged_text(path):
    """The bytes THIS COMMIT will contain: the index blob, falling back to the worktree.

    A gate that reads the worktree grades something the commit may not carry.
    """
    try:
        out = subprocess.run(["git", "show", ":" + path.replace("\\", "/")],
                             capture_output=True)
        if out.returncode == 0:
            return out.stdout.decode("utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except Exception:  # noqa: BLE001
        return None


def _is_step4(text, tpg):
    """True only for a document that DECLARES itself a step-4 PRD in its own header."""
    m = tpg.PRD_FENCE_RE.search(text)
    if not m:
        return False
    try:
        return json.loads(m.group(1)).get("step") == 4
    except Exception:  # noqa: BLE001
        return False


def grade(text, tpg):
    """Return a violation string, or None when conformant. Mirrors the L6 limb's two checks."""
    body = tpg._top_section(text, tpg.MANIFEST_HEADING_RE)
    if body is None:
        return ("no top-level SURFACE MANIFEST section (a heading inside a code fence does not "
                "count). Step 5 cannot run a battery on prose.")
    if len(body.strip()) < tpg.MANIFEST_MIN_BODY_CHARS:
        # The floor is IMPORTED, not copied -- see the module docstring. And the wording says
        # UNDER-POPULATED rather than EMPTY because the case that actually trips it is a real
        # two-row table one char short: telling a reader EMPTY sends them to the wrong repair.
        return ("SURFACE MANIFEST heading present but the section is UNDER-POPULATED (%d chars, "
                "floor %d). The section exists -- it needs MORE ROWS, not a new heading."
                % (len(body.strip()), tpg.MANIFEST_MIN_BODY_CHARS))
    return None


def run(paths):
    tpg = _load_tpg()
    if tpg is None:
        print("ERROR: to-pipeline-gate.py not found -- the PRD manifest limb cannot run; "
              "REFUSED (fail-closed)", file=sys.stderr)
        return 2
    bad, graded = [], 0
    for p in paths:
        if not re.search(r"_PRD\.md$", p.replace("\\", "/")):
            continue
        text = _staged_text(p)
        if text is None or not _is_step4(text, tpg):
            continue  # not a step-4 PRD -- not this gate's domain
        graded += 1
        why = grade(text, tpg)
        if why:
            bad.append((p, why))
    if bad:
        print("BLOCKED: a step-4 PRD may not be committed without a SURFACE MANIFEST.",
              file=sys.stderr)
        print("  Andrew-direct 2026-09-09: \"a PRD literally cannot be committed unless it has "
              "one.\"", file=sys.stderr)
        for p, why in bad:
            print("  %s\n    %s" % (p, why), file=sys.stderr)
        print("  The manifest is the step-4 -> step-5 handoff: one row per ENGINE, and it is a "
              "STARTING", file=sys.stderr)
        print("  point for the COO, not an ending point. Add the section, then re-commit.",
              file=sys.stderr)
        return 1
    if graded:
        print("  [prd-manifest] OK: %d step-4 PRD(s) carry a SURFACE MANIFEST" % graded)
    return 0


def census():
    tpg = _load_tpg()
    files = subprocess.run(["git", "ls-files", "*_PRD.md"],
                           capture_output=True, text=True).stdout.split()
    nohdr = badhdr = 0
    step4, missing = [], []
    for f in files:
        try:
            with open(f, encoding="utf-8", errors="replace") as fh:
                t = fh.read()
        except Exception:  # noqa: BLE001
            continue
        m = tpg.PRD_FENCE_RE.search(t)
        if not m:
            nohdr += 1
            continue
        try:
            h = json.loads(m.group(1))
        except Exception:  # noqa: BLE001
            badhdr += 1
            continue
        if h.get("step") == 4:
            step4.append((f, h.get("project")))
            why = grade(t, tpg)
            if why:
                missing.append((f, h.get("project"), why))
    print("DENOMINATOR: %d tracked *_PRD.md" % len(files))
    print("  no fenced json header: %d | header unparseable: %d | STEP-4 PRDs: %d"
          % (nohdr, badhdr, len(step4)))
    print("STEP-4 PRDs THIS GATE WOULD REFUSE TODAY: %d of %d" % (len(missing), len(step4)))
    for f, p, why in missing:
        print("   REFUSED  %-16s %s\n     %s" % (p, f, why))
    for f, p in step4:
        if not any(f == mf for mf, _, _ in missing):
            print("   PASS     %-16s %s" % (p, f))
    return 0


HDR = '```json\n{"step": 4}\n```\n'


def self_test():
    """TWO ways a guard fails: it cannot refuse, and it refuses everything.

    Both fixtures below must hold, and each is able to fail on its own.
    """
    tpg = _load_tpg()
    if tpg is None:
        print("SELF-TEST ERROR: to-pipeline-gate.py not importable", file=sys.stderr)
        return 2
    cases = [
        # (name, text, expect_refusal)
        ("REFUSE-FIXTURE  no manifest at all",
         HDR + "## 1. Purpose\n\nprose only, no manifest anywhere.\n", True),
        ("REFUSE-FIXTURE  heading present, body EMPTY",
         HDR + "## 8. SURFACE MANIFEST\n\n## 9. Next\n", True),
        ("REFUSE-FIXTURE  heading only INSIDE a code fence",
         HDR + "## 1. Purpose\n\n```\n## 8. SURFACE MANIFEST\n| id | surface |\n|---|---|\n"
               "| S1 | a real looking row that is fenced |\n```\n", True),
        ("POSITIVE-CONTROL  real manifest passes",
         HDR + "## 8. SURFACE MANIFEST (step 4 -> step 5)\n\n| id | surface | claim |\n"
               "|---|---|---|\n| S1 | the thing | absent |\n", False),
    ]
    # BOUNDARY CONTROLS on the imported floor (3.0.0_SA_CVO~Z msg 20602: "40 IS AN UNMEASURED EXACT
    # CONSTANT and the 5 controls do not cover its boundary"). Built by CONSTRUCTION off the imported
    # value rather than hardcoding 39/41, so these follow the floor if it is ever retuned -- a control
    # pinned to a constant the fix will move is a control that stops testing.
    floor = tpg.MANIFEST_MIN_BODY_CHARS
    pad = "## 8. SURFACE MANIFEST\n\n"
    cases.append(("BOUNDARY-CONTROL  body of floor-1 chars REFUSES",
                  HDR + pad + "x" * (floor - 1) + "\n", True))
    cases.append(("BOUNDARY-CONTROL  body of floor+1 chars PASSES",
                  HDR + pad + "x" * (floor + 1) + "\n", False))
    ok = True
    for name, text, expect in cases:
        got = grade(text, tpg) is not None
        verdict = "PASS" if got == expect else "FAIL"
        if got != expect:
            ok = False
        print("  [%s] %s (refused=%s, expected=%s)" % (verdict, name, got, expect))
    # The domain discriminator is itself a claim -- test that a non-step-4 doc is NOT graded.
    non_step4 = "## 1. Purpose\n\nan architecture doc named *_PRD.md, no step-4 header.\n"
    in_domain = _is_step4(non_step4, tpg)
    print("  [%s] DOMAIN-CONTROL  a *_PRD.md with no step-4 header is OUT of domain (in_domain=%s)"
          % ("PASS" if not in_domain else "FAIL", in_domain))
    if in_domain:
        ok = False
    print("SELF-TEST: %s" % ("ALL HOLD" if ok else "BROKEN"))
    return 0 if ok else 1


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)
    if args[0] == "--self-test":
        sys.exit(self_test())
    if args[0] == "--census":
        sys.exit(census())
    sys.exit(run(args))
