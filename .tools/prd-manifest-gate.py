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

EXTENDED 2026-09-10 ~19:2xZ ON ANDREW-DIRECT AT THE 1.0.0_SA_CTO~Z TERMINAL, VERBATIM:
  "ok we need all of these things to be gated moving forward. proceed with designing the gate for
   key PRD surfaces, where it is refused at commit time unless it has the necessary sections."
  and, on whether the format itself had to change: "if we need to redesign PRD format to have
  structureed, clearly parseable sections to this end, so be it."

  NO REDESIGN WAS NEEDED AND THE CENSUS IS WHY. 12 of 14 step-4 PRDs already conformed on every
  limb below before a line was written; the two that did not were ADDENDA, which are a different
  domain. The format was already parseable -- IT WAS SIMPLY NOT ENFORCED AT COMMIT TIME. So this
  is a MOVE of existing L6 limbs to L4, exactly as the manifest limb was moved on 2026-09-09, and
  not a new contract anybody must migrate to.

WHAT PROVOKED IT. AMGT_RESAPP's PRD committed clean at @c0b5636ea9 carrying ZERO OUTCOME CARDS, no
header block, and a heading the L6 matcher could not see -- because its author staged a POINTER to
the L2 endpoint artifact with a note promising transcription "when this file lands in the tree", and
the landing was byte-for-byte so the promise executed nothing. FOUND AN HOUR LATER BY 2.0.0_SA_COO~ZZZ
running the L6 gate's own functions by hand, not by the machinery. The same seat had spent that same
day correcting the identical two-carrier defect on NFRA_REPORT. A rule a human has to remember on
the way past is not a rule.

THE LIMBS, AND THE BLAST RADIUS OF EACH MEASURED BEFORE SHIPPING (--census prints it live):
  A  ENDPOINT heading resolvable by the L6 matcher      0 of 10 refused
  B  exactly ONE PRD_HEADER json fence                  0 of 10 refused
  C  at least one FWD outcome card DEFINED              0 of 10 refused
  D  SURFACE MANIFEST section (the original limb)       0 of 10 refused
  E  header endpoint_outcomes == cards actually defined 0 of 10 refused, AFTER one fix
  F  an ADDENDUM defines no outcome absent from its PRD 0 of  2 refused

  ! LIMB E CAUGHT A LIVE DEFECT IN THE AUTHOR'S OWN WORK WITHIN MINUTES OF BEING WRITTEN.
  NFRA_REPORT's header declared 12 outcomes while its ENDPOINT section defined 21 -- the recut
  added FWD-13..21 and never updated the header. Fixed at prd_version v0.8 before this shipped.
  That is the limb earning its place: the drift is invisible to a reader and total to a consumer,
  because the R3 monitor emits on the HEADER and step 5 reads the SECTION.

  ! LIMB F IS THE TWO-CARRIER DEFECT MECHANIZED, and it is deliberately NOT "an addendum may not
  define outcomes". Measured: NFRA_OPSEC202609's addendum DOES define FWD-19 and that outcome IS
  in its PRD and its header -- that lane did it correctly, and a blunter limb would have refused
  correct work. The invariant is not "no outcomes in an addendum"; it is "NOTHING AN ADDENDUM
  DEFINES MAY BE ABSENT FROM THE PRD". That passes OPSEC and would have caught NFRA_REPORT.

ALL SIX SHIP FAIL-CLOSED WITH NO LEGACY CARVE-OUT AND NO AUDITED OVERRIDE, on the same reasoning
the original limb recorded: the refused set is empty, so there is nothing to grandfather, and an
escape hatch on a structural requirement is an invitation to use it.

USAGE:
  prd-manifest-gate.py <path>...    grade these paths (safe-commit passes its pathspec)
  prd-manifest-gate.py --self-test  refuse-fixtures + positive controls for every limb
  prd-manifest-gate.py --census     print the population and what each limb would refuse today
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


def _defined_fwd(text, tpg):
    """The FWD ids DEFINED as outcome cards -- read through the L6 gate's own matcher, never a copy."""
    out = set()
    for m in tpg.FWD_DEF_RE.findall(text):
        raw = m if isinstance(m, str) else (m[0] if m else "")
        hit = re.search(r"FWD-\d+", str(raw))
        if hit:
            out.add(hit.group(0))
    return out


def _header(text, tpg):
    """The parsed PRD_HEADER, or None. Uses the primary's fence matcher."""
    fences = tpg.PRD_FENCE_RE.findall(text)
    if not fences:
        return None
    try:
        return json.loads(fences[0])
    except Exception:  # noqa: BLE001
        return None


def grade(text, tpg):
    """Every limb's complaint for a step-4 PRD. Empty list == conformant.

    RETURNS A LIST since 2026-09-10. A single-violation return told an author about ONE defect per
    commit, so a PRD with three would have cost three round trips -- and AMGT_RESAPP had exactly
    three. Report them together.
    """
    v = []

    # ---- LIMB D (the original): the SURFACE MANIFEST ----
    body = tpg._top_section(text, tpg.MANIFEST_HEADING_RE)
    if body is None:
        v.append("no top-level SURFACE MANIFEST section (a heading inside a code fence does not "
                 "count). Step 5 cannot run a battery on prose.")
    elif len(body.strip()) < tpg.MANIFEST_MIN_BODY_CHARS:
        # The floor is IMPORTED, not copied -- see the module docstring. And the wording says
        # UNDER-POPULATED rather than EMPTY because the case that actually trips it is a real
        # two-row table one char short: telling a reader EMPTY sends them to the wrong repair.
        v.append("SURFACE MANIFEST heading present but the section is UNDER-POPULATED (%d chars, "
                 "floor %d). The section exists -- it needs MORE ROWS, not a new heading."
                 % (len(body.strip()), tpg.MANIFEST_MIN_BODY_CHARS))

    # ---- LIMB A: the ENDPOINT section must be resolvable BY THE L6 MATCHER ----
    # AMGT_RESAPP's heading read "## 1. ENDPOINT (...)" and a human reads that as an ENDPOINT
    # section. _top_section matches WHOLE-LINE, so the "1. " prefix made it invisible. The author
    # cannot see the difference; the consumer sees nothing else.
    endpoint = tpg._top_section(text, tpg.ENDPOINT_HEADING)
    if endpoint is None:
        v.append("no top-level ENDPOINT section the L6 matcher can resolve. It must read EXACTLY "
                 "'%s' at column 0 -- a numbered prefix ('## 1. ENDPOINT ...') is invisible to it, "
                 "and so is a heading inside a code fence." % tpg.ENDPOINT_HEADING)

    # ---- LIMB B: exactly ONE PRD_HEADER json fence ----
    nfence = len(tpg.PRD_FENCE_RE.findall(text))
    hdr = _header(text, tpg)
    if nfence == 0:
        v.append("carries no fenced json PRD_HEADER block. It must be the FIRST fenced json in the "
                 "file (org/standards/PRD_HEADER.schema.json) -- the R3 monitor and the L6 gate "
                 "both read it, and a PRD without one is invisible to the COO.")
    elif nfence > 1:
        v.append("carries %d fenced json blocks; the PRD_HEADER must be unambiguous. The FIRST "
                 "fence is read as the header -- move the others behind a non-json fence." % nfence)
    elif hdr is None:
        v.append("the first fenced json block does not parse. A header a consumer cannot read is "
                 "the same as no header, and fails silently rather than loudly.")

    # ---- LIMB C: outcomes must be DEFINED, not pointed at ----
    defined = _defined_fwd(endpoint if endpoint else text, tpg)
    if not defined:
        v.append("defines ZERO outcome cards. The ENDPOINT section must CARRY the FWD-n cards, not "
                 "point at a document that has them: a pointer promising a later transcription is "
                 "a promise nothing enforces, and that is exactly how AMGT_RESAPP shipped with no "
                 "outcomes at all.")

    # ---- LIMB E: the header and the section must agree, BOTH DIRECTIONS ----
    # The two carriers are read by DIFFERENT consumers -- the monitor reads the header, step 5
    # reads the section -- so drift between them is invisible to a reader and total to a consumer.
    if hdr is not None and defined:
        declared = set(hdr.get("endpoint_outcomes") or [])
        if declared and declared != defined:
            only_hdr = sorted(declared - defined)
            only_sec = sorted(defined - declared)
            bits = []
            if only_hdr:
                bits.append("declared in the header but NOT defined in the section: %s"
                            % ", ".join(only_hdr))
            if only_sec:
                bits.append("defined in the section but NOT declared in the header: %s"
                            % ", ".join(only_sec))
            v.append("header `endpoint_outcomes` and the ENDPOINT section DISAGREE -- %s. The R3 "
                     "monitor reads the header and step 5 reads the section, so this drift is "
                     "invisible to a reader and total to a consumer. Bump prd_version when you "
                     "fix it, or the monitor will not emit the correction." % "; and ".join(bits))
    return v


def grade_addendum(text, sibling_text, tpg):
    """LIMB F: nothing an addendum DEFINES may be absent from the PRD it amends.

    NOT 'an addendum may not define outcomes'. Measured before choosing: NFRA_OPSEC202609's
    addendum defines FWD-19 and that outcome IS in its PRD and its header -- correct work a
    blunter limb would have refused. The defect is DIVERGENCE, not presence.
    """
    v = []
    defined = _defined_fwd(text, tpg)
    if not defined:
        return v  # an addendum that defines nothing cannot diverge from anything
    if sibling_text is None:
        v.append("defines outcome card(s) %s but its PRD could not be read to confirm they are "
                 "carried there. An outcome that lives only in an addendum is invisible to every "
                 "consumer that reads the PRD." % ", ".join(sorted(defined)))
        return v
    in_prd = _defined_fwd(sibling_text, tpg)
    orphan = sorted(defined - in_prd)
    if orphan:
        v.append("defines outcome card(s) %s that are NOT defined in the PRD it amends. THE RULE "
                 "IS THAT A PRD ADDENDUM EDITS THE PRD'S OWN ENDPOINT SECTION, SAME TURN, AND "
                 "NOTHING ROUTES ONWARD UNTIL IT DOES. NFRA_REPORT round 4 was cut from an "
                 "addendum whose outcomes were never folded in, so a named constraint carrying "
                 "Andrew's own words was not in the room and the round shipped a regression to a "
                 "live daily email. Fold them in; leave this file as a pointer."
                 % ", ".join(orphan))
    return v

ADDENDUM_RE = re.compile(r"_PRD_ADDENDUM[^/\\]*\.md$", re.I)
PRIMARY_RE = re.compile(r"_PRD\.md$")


def _sibling_prd(path):
    """`<dir>/<CODE>_PRD.md` for a `<dir>/<CODE>_PRD_ADDENDUM_*.md`."""
    q = path.replace("\\", "/")
    base = re.sub(r"_PRD_ADDENDUM.*\.md$", "_PRD.md", q, flags=re.I)
    return base if base != q else None


def run(paths):
    tpg = _load_tpg()
    if tpg is None:
        print("ERROR: to-pipeline-gate.py not found -- the PRD manifest limb cannot run; "
              "REFUSED (fail-closed)", file=sys.stderr)
        return 2
    bad, graded = [], 0
    for p in paths:
        q = p.replace("\\", "/")

        # ---- ADDENDUM DOMAIN (limb F). Checked FIRST: an addendum also ends in .md and must not
        # fall through to the primary limbs, which would demand a manifest of a pointer file.
        if ADDENDUM_RE.search(q):
            text = _staged_text(p)
            if text is None:
                continue
            sib = _sibling_prd(p)
            sib_text = _staged_text(sib) if sib else None
            why = grade_addendum(text, sib_text, tpg)
            if why:
                graded += 1
                bad.extend((p, w) for w in why)
            elif _defined_fwd(text, tpg):
                graded += 1  # graded and clean
            continue

        if not PRIMARY_RE.search(q):
            continue
        text = _staged_text(p)
        if text is None or not _is_step4(text, tpg):
            continue  # not a step-4 PRD -- not this gate's domain
        graded += 1
        for w in grade(text, tpg):
            bad.append((p, w))
    if bad:
        print("BLOCKED: a step-4 PRD may not be committed without its KEY SURFACES.",
              file=sys.stderr)
        print("  Andrew-direct 2026-09-09: \"a PRD literally cannot be committed unless it has "
              "one.\"  2026-09-10: \"we need all of these things to be gated moving forward ... "
              "refused at commit time unless it has the necessary sections.\"", file=sys.stderr)
        for p, why in bad:
            print("  %s\n    %s" % (p, why), file=sys.stderr)
        print("  These are the step-4 -> step-5 handoff surfaces. The manifest is a STARTING point "
              "for the COO,", file=sys.stderr)
        print("  the ENDPOINT section is what step 10 reads back, and the header is what the "
              "monitor emits on.", file=sys.stderr)
        print("  Fix and re-commit -- and BUMP prd_version, or the correction is invisible to the "
              "COO.", file=sys.stderr)
        return 1
    if graded:
        print("  [prd-manifest] OK: %d step-4 PRD document(s) carry their key surfaces "
              "(manifest, ENDPOINT, header, outcome cards, header/section agreement)" % graded)
    return 0

def census():
    """Print the live population and what EACH limb would refuse today.

    Per-limb rather than a single total, because a gate that ships six limbs on one aggregate
    number cannot say which limb carries the risk -- and the answer differs per limb.
    """
    tpg = _load_tpg()
    files = subprocess.run(["git", "ls-files", "*_PRD.md", "*_PRD_ADDENDUM*.md"],
                           capture_output=True, text=True).stdout.split()
    nohdr = badhdr = 0
    step4, missing, addenda, add_bad = [], [], [], []
    for f in files:
        try:
            with open(f, encoding="utf-8", errors="replace") as fh:
                t = fh.read()
        except Exception:  # noqa: BLE001
            continue
        if ADDENDUM_RE.search(f.replace("\\", "/")):
            sib = _sibling_prd(f)
            st = None
            if sib:
                try:
                    with open(sib, encoding="utf-8", errors="replace") as fh:
                        st = fh.read()
                except Exception:  # noqa: BLE001
                    st = None
            addenda.append(f)
            why = grade_addendum(t, st, tpg)
            if why:
                add_bad.append((f, why))
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
    print("DENOMINATOR: %d tracked *_PRD*.md" % len(files))
    print("  no fenced json header: %d | header unparseable: %d | STEP-4 PRDs: %d | ADDENDA: %d"
          % (nohdr, badhdr, len(step4), len(addenda)))
    print("STEP-4 PRDs THIS GATE WOULD REFUSE TODAY: %d of %d" % (len(missing), len(step4)))
    for f, p, why in missing:
        print("   REFUSED  %-16s %s" % (p, f))
        for w in why:
            print("     - %s" % w[:150])
    for f, p in step4:
        if not any(f == mf for mf, _, _ in missing):
            print("   PASS     %-16s %s" % (p, f))
    print("ADDENDA THIS GATE WOULD REFUSE TODAY: %d of %d" % (len(add_bad), len(addenda)))
    for f, why in add_bad:
        print("   REFUSED  %s" % f)
        for w in why:
            print("     - %s" % w[:150])
    for f in addenda:
        if not any(f == bf for bf, _ in add_bad):
            print("   PASS     %s" % f)
    return 0

HDR = '```json\n{"step": 4}\n```\n'


def self_test():
    """Every limb gets a REFUSE fixture and a POSITIVE control, and each refusal is checked for
    WHICH limb fired.

    ⛔ THE LIMB-SCOPING IS THE POINT AND IT IS NOT DECORATION. Once grade() carried six limbs, the
    original manifest fixtures started refusing for a DIFFERENT limb than they were written to
    test -- they had no ENDPOINT section and no cards, so they refused three ways and still
    reported PASS on "refused=True". A fixture that refuses for the wrong reason is a control that
    agrees with the convenient answer. So every fixture below is an OTHERWISE-CONFORMING document
    with exactly ONE defect injected, and the assertion is on the MESSAGE, not merely on the count.
    """
    tpg = _load_tpg()
    if tpg is None:
        print("SELF-TEST ERROR: to-pipeline-gate.py not importable", file=sys.stderr)
        return 2

    HDRJ = '```json\n{"step": 4, "endpoint_outcomes": ["FWD-1"]}\n```\n\n'
    ENDPOINT = ("## ENDPOINT (step 2, /endpoint --forward)\n\n```\n"
                "  FWD-1  a real outcome card\n"
                "         DONE WHEN  APPLIED -- it is in place\n"
                "         ACCEPT     a person can tell that it happened\n```\n\n")
    MANIFEST = ("## 8. SURFACE MANIFEST (step 4 -> step 5)\n\n| id | surface | claim |\n"
                "|---|---|---|\n| S1 | the thing | absent |\n\n")
    CONFORMING = HDRJ + ENDPOINT + MANIFEST

    # (name, text, expect_refusal, substring the refusal must contain)
    cases = [
        ("POSITIVE-CONTROL  a fully conforming PRD passes every limb",
         CONFORMING, False, None),

        # ---- LIMB D: the manifest (the original limb, fixtures kept and now limb-scoped) ----
        ("LIMB D  no manifest at all",
         HDRJ + ENDPOINT + "## 1. Purpose\n\nprose only.\n", True, "SURFACE MANIFEST"),
        ("LIMB D  manifest heading present, body EMPTY",
         HDRJ + ENDPOINT + "## 8. SURFACE MANIFEST\n\n## 9. Next\n", True, "UNDER-POPULATED"),
        ("LIMB D  manifest heading only INSIDE a code fence",
         HDRJ + ENDPOINT + "```\n## 8. SURFACE MANIFEST\n| id |\n|---|\n| S1 |\n```\n",
         True, "SURFACE MANIFEST"),

        # ---- LIMB A: the ENDPOINT heading the L6 matcher must resolve ----
        ("LIMB A  ENDPOINT heading carries a numbered prefix (the AMGT_RESAPP defect)",
         HDRJ + ENDPOINT.replace("## ENDPOINT", "## 1. ENDPOINT") + MANIFEST,
         True, "ENDPOINT section"),
        ("LIMB A  no ENDPOINT heading at all",
         HDRJ + MANIFEST, True, "ENDPOINT section"),
        ("LIMB A  POSITIVE  backticks in the heading are tolerated",
         HDRJ + ENDPOINT.replace("/endpoint --forward", "`/endpoint --forward`") + MANIFEST,
         False, None),

        # ---- LIMB B: exactly one PRD_HEADER json fence ----
        ("LIMB B  a SECOND json fence makes the header ambiguous",
         CONFORMING + '```json\n{"something": "else"}\n```\n', True, "fenced json blocks"),

        # ---- LIMB C: outcomes DEFINED, not pointed at ----
        ("LIMB C  ENDPOINT section points at another document instead of carrying cards",
         HDRJ + "## ENDPOINT (step 2, /endpoint --forward)\n\nThe block lives at OTHER.md and is "
         "transcribed when this lands.\n\n" + MANIFEST, True, "ZERO outcome cards"),

        # ---- LIMB E: header and section must agree, BOTH directions ----
        ("LIMB E  header declares an outcome the section does not define",
         CONFORMING.replace('["FWD-1"]', '["FWD-1", "FWD-2"]'), True, "DISAGREE"),
        ("LIMB E  section defines an outcome the header does not declare",
         (HDRJ + ENDPOINT.replace("```\n  FWD-1", "```\n  FWD-9  another card\n         DONE WHEN"
                                  "  APPLIED -- x\n         ACCEPT     y\n\n  FWD-1")
          + MANIFEST), True, "DISAGREE"),
    ]

    ok = True
    for name, text, expect, needle in cases:
        v = grade(text, tpg)
        got = len(v) > 0
        verdict = "PASS" if got == expect else "FAIL"
        detail = ""
        if got == expect and expect and needle:
            if not any(needle in x for x in v):
                verdict, ok = "FAIL", False
                detail = " -- refused, but for the WRONG limb: %r" % (v[0][:70],)
        if got != expect:
            ok = False
            if got:
                detail = " -- %r" % (v[0][:80],)
        print("  [%s] %s (refused=%s, expected=%s)%s" % (verdict, name, got, expect, detail))

    # ---- LIMB F: the addendum limb, with the case that must NOT refuse ----
    ADD_DEF = ("# addendum\n\n```\n  FWD-9  an outcome minted in an addendum\n"
               "         DONE WHEN  APPLIED -- x\n         ACCEPT     y\n```\n")
    PRD_WITH_9 = HDRJ + ENDPOINT.replace("  FWD-1 ", "  FWD-9 ") + MANIFEST
    f_cases = [
        ("LIMB F  addendum defines FWD-9 and the PRD does NOT (the NFRA_REPORT defect)",
         ADD_DEF, CONFORMING, True),
        ("LIMB F  POSITIVE  addendum defines FWD-9 and the PRD DOES (the OPSEC case -- correct work)",
         ADD_DEF, PRD_WITH_9, False),
        ("LIMB F  POSITIVE  a pointer addendum defining nothing is never refused",
         "# addendum\n\nThis is a pointer. See the PRD.\n", CONFORMING, False),
        ("LIMB F  addendum defines an outcome and the PRD cannot be read",
         ADD_DEF, None, True),
    ]
    for name, atext, ptext, expect in f_cases:
        v = grade_addendum(atext, ptext, tpg)
        got = len(v) > 0
        verdict = "PASS" if got == expect else "FAIL"
        if got != expect:
            ok = False
        print("  [%s] %s (refused=%s, expected=%s)" % (verdict, name, got, expect))

    # ---- BOUNDARY CONTROLS on the imported floor, built BY CONSTRUCTION off the imported value ----
    floor = tpg.MANIFEST_MIN_BODY_CHARS
    for delta, expect in ((-1, True), (+1, False)):
        text = HDRJ + ENDPOINT + "## 8. SURFACE MANIFEST\n\n" + "x" * (floor + delta) + "\n"
        got = len(grade(text, tpg)) > 0
        verdict = "PASS" if got == expect else "FAIL"
        if got != expect:
            ok = False
        print("  [%s] BOUNDARY-CONTROL  manifest body of floor%+d chars (refused=%s, expected=%s)"
              % (verdict, delta, got, expect))

    # ---- DOMAIN CONTROLS: the gate must NOT grade what is not a step-4 PRD ----
    non_step4 = "## 1. Purpose\n\nan architecture doc named *_PRD.md, no step-4 header.\n"
    in_domain = _is_step4(non_step4, tpg)
    print("  [%s] DOMAIN-CONTROL  a *_PRD.md with no step-4 header is OUT of domain (in_domain=%s)"
          % ("PASS" if not in_domain else "FAIL", in_domain))
    if in_domain:
        ok = False
    for p, should_be_add in (("a/b/X_PRD_ADDENDUM_01.md", True), ("a/b/X_PRD.md", False)):
        is_add = bool(ADDENDUM_RE.search(p))
        v = "PASS" if is_add == should_be_add else "FAIL"
        if is_add != should_be_add:
            ok = False
        print("  [%s] DOMAIN-CONTROL  %r routed as addendum=%s" % (v, p, is_add))
    sib = _sibling_prd("org/missions/D0/M/X/prd/X_PRD_ADDENDUM_01.md")
    v = "PASS" if sib == "org/missions/D0/M/X/prd/X_PRD.md" else "FAIL"
    if v == "FAIL":
        ok = False
    print("  [%s] DOMAIN-CONTROL  sibling resolution -> %s" % (v, sib))

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
