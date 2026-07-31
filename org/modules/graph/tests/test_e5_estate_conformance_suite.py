#!/usr/bin/env python3
"""WS-E5 estate-side conformance suite -- ten specimens, EACH CARRYING ITS OWN MUTANT.

Author: 0.7.0_AE_CloudOps~D. TO: NFRA_VELOCITY_ESTATE.WS-E5 @8396b9b785.
COO 150455Z + 152143Z: build the nine-specimen suite, add the scoped-vs-unscoped membership
test as specimen 10, and *"every specimen carries its OWN mutant, not a presence check."*

WHY NOT A PRESENCE CHECK -- the argument is now the TO's, and it was earned by measurement:
A PRESENCE SURVEY WOULD HAVE BEEN WRONG IN BOTH DIRECTIONS. It would have missed that
comp-legacywriter ALREADY emits a full boundary report (in prose), AND missed that
comp-trigger's boundary is scope-correct while comp-legacywriter's is not.
PRESENCE IS NOT THE AXIS. CORRECTNESS UNDER SCOPE CHANGE IS, and only a mutant reveals it.

WHAT A MUTANT IS HERE: a deliberate perturbation of the thing a declaration claims to bound,
plus the assertion that the declaration MOVES. A declaration that does not move under its own
subject's mutation is a CONFORMANT DISCLAIMER -- C7's discipline, verbatim: *"a fully-conformant
boundary declaration is compatible with every value being wrong."*

DENOMINATOR OF THIS SUITE, STATED UP FRONT: ten specimens, drawn from the nine same-day
false-negative mechanisms named in the ESTATE PRD plus the scope-membership test. This is NOT a
census of estate false-negative modes -- it is the enumerated set the PRD named, and a mode nobody
wrote down is not in it. The suite cannot see what the PRD did not enumerate.

STATUS HONESTY: specimens marked EXERCISED were run against a live instrument. Specimens marked
DECLARED-NOT-EXERCISED carry their mutant DESIGN but have not been run -- they are not claims that
the estate passes. A suite that silently mixes the two is the exact thing this workstream exists
to stop.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

# parents[4] is the repo root: tests <- graph <- modules <- org <- ajb_workspace.
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / ".tools"))
from msys_argv_guard import msys_safe_run  # noqa: E402

# The mutant pair: the SAME instrument asked a WIDE question and a NARROW one.
# If the answer moves and the declared boundary does not, the declaration is a disclaimer.
_TIMEOUT = 600


def _run(argv: list[str]) -> tuple[int, str]:
    """Invoke a comp-tool for real. No fixtures, no recorded output -- the point is to EXERCISE.

    MUST route through `msys_safe_run` (CLAUDE.md, the 5-member native-parent/MSYS-child class).
    The comp-tools are EXTENSIONLESS BASH SHIMS: native-Python `subprocess.run` raises
    `FileNotFoundError [WinError 2]` on every one of them, and `shutil.which` reports them
    PRESENT because it walks PATH without asking whether CreateProcess can execute the result.

    THAT MISMATCH IS SPECIMEN 1'S SHAPE, HIT LIVE INSIDE THIS SUITE: a presence probe that
    cannot distinguish "absent" from "present but not invocable by me." My first draft used
    `which` as the availability guard, which would have SKIPPED (= silently reported
    UNVERIFIABLE) on a fully-installed estate. Kept as a comment because the suite's own
    near-miss is the cheapest evidence the mechanism is ergonomic rather than exotic.
    """
    p = msys_safe_run(argv, capture_output=True, text=True, timeout=_TIMEOUT)
    return p.returncode, (p.stdout or "") + (p.stderr or "")

def _have(tool: str) -> bool:
    """Availability asked THROUGH THE SAME PATH THE CALL WILL TAKE.

    `shutil.which` is the wrong oracle here and this suite proved it on itself: it answers about
    native CreateProcess resolution, while every real invocation goes through bash. An
    availability probe on a different path than the call is not a probe of the call.
    """
    rc, _ = _run(["command", "-v", tool])
    return rc == 0


def _boundary_lines(text: str, needles: tuple[str, ...]) -> str:
    """The scan-population claim the tool prints. Crude on purpose: we test whether it MOVES."""
    keep = [ln.strip() for ln in text.splitlines() if any(n in ln for n in needles)]
    return " | ".join(keep)


# ---------------------------------------------------------------------------------------------
# SPECIMEN 10 -- SCOPE MEMBERSHIP. LIVE MUTANT. This is the one that produced a real defect.
#
# THIS SUITE ALMOST SHIPPED THIS SPECIMEN AS `assert True` PLUS A DOCSTRING CITING YESTERDAY'S
# NUMBERS. That is a criterion its own author wrote, that cannot fail, over an artifact it does
# not touch -- SPECIMENS 8 AND 9, committed inside the suite that names them. Caught on read-back,
# recorded here rather than quietly fixed, because the near-miss is the evidence that the failure
# mode is ergonomic and not stupid: a recorded measurement reads exactly like a live one.
# ---------------------------------------------------------------------------------------------

@pytest.mark.xfail(
    strict=True,
    reason="LIVE DEFECT in comp-legacywriter: a scoped answer carries an UNSCOPED boundary. "
           "strict=True on purpose -- if the instrument is fixed this XPASSes and pytest reports "
           "it as a FAILURE, which is the notification. Owner COO (150455Z), routed to CTO.",
)
def test_specimen_10_live_mutant_boundary_must_move_with_scope():
    """LIVE. comp-legacywriter wide vs narrow; asserts the DECLARED boundary moves. It does not.

    >> THE MUTANT-APPLIED PRECONDITION CAUGHT A CONFOUND IN THIS VERY TEST, AND THAT IS THE
    STRONGEST EVIDENCE IN THE SUITE FOR WHY COO/~E's RULE BELONGS ON EVERY SPECIMEN. <<

    My first draft mutated `--census` -> `--census mdpf`. Those are 202 lines and 202 lines:
    `--census` is a DIFFERENT MODE that does not scope by target, so the "mutant" changed the
    argv and not the question. The precondition fired (`202 -> 202`) and refused to score a
    verdict. Without it I would have read the unchanged boundary as CONFIRMATION of the defect
    -- THE RIGHT ANSWER FOR THE WRONG REASON, which is unfalsifiable and would have hardened a
    claim already routed to CTO.

    RE-DERIVED CORRECTLY 2026-07-31T15:57Z (same mode both sides, scope is the POSITIONAL
    `target`; `--bucket` does not exist and exits rc=2):
        wide  `comp-legacywriter`        -> 2426 lines
        narrow `comp-legacywriter mdpf`  ->  297 lines   (answer narrows 88%)
        boundary BOTH: `examined 8916 file(s)` + `642 distinct (BUCKET,KEY) location(s)`
    THE FINDING STANDS. Only my instrument for it was broken.

    NUMBER-DRIFT NOTE, so nobody re-derives from memory: the 07-30 record said the scoped run was
    181 lines; today it is 297 (repo moved, 8915 -> 8916 files). `181` ALSO appears in this
    tool's own output as `181 probe-site(s)` -- a coincidence, but exactly the kind that turns a
    remembered number into a false corroboration. Quote the run, never the recollection.
    """
    if not _have("comp-legacywriter"):
        pytest.skip("comp-legacywriter not on PATH -- UNVERIFIABLE, not PASS")

    rc_wide, wide = _run(["comp-legacywriter"])
    rc_narrow, narrow = _run(["comp-legacywriter", "mdpf"])
    assert rc_wide == 0 and rc_narrow == 0, f"tool errored: {rc_wide}/{rc_narrow}"

    n_wide, n_narrow = len(wide.splitlines()), len(narrow.splitlines())
    # PRECONDITION, not the finding: prove the mutation took effect at all.
    assert n_narrow < n_wide, (
        f"NON-MUTATING MUTANT: answer did not narrow ({n_wide} -> {n_narrow}). "
        "This test proves nothing in this state -- fix the mutant before reading the result."
    )

    needles = ("examined", "distinct (BUCKET")
    b_wide = _boundary_lines(wide, needles)
    b_narrow = _boundary_lines(narrow, needles)
    assert b_wide, "boundary line not found in wide run -- instrument shape changed, re-derive"

    # The scoped run must ALSO name the address space it ranges over. comp-trigger prints
    # `forensics for: "mdpf"`; comp-legacywriter's header names the run, the spec and the source
    # HEAD -- and never the target. An unlabeled count beside a scoped answer IS the defect.
    header = "\n".join(narrow.splitlines()[:3]).lower()
    names_scope = "mdpf" in header

    assert b_wide != b_narrow or names_scope, (
        f"UNSCOPED BOUNDARY ON A SCOPED ANSWER: answer narrowed {n_wide} -> {n_narrow} lines "
        f"while the declared boundary did not move AND the header never names the scope.\n"
        f"  wide  : {b_wide}\n  narrow: {b_narrow}\n"
        "The answer and the boundary describe different populations and nothing in the output "
        "distinguishes them. Live defect in comp-legacywriter; owner COO, routed to CTO."
    )


def test_specimen_10b_live_mutant_counterexample_comp_trigger():
    """LIVE. The DIFFERENT-FAMILY counter-example -- and a NARROWING of my own earlier claim.

    I reported to COO that comp-trigger's boundary is "scope-correct." RUNNING IT PROPERLY SAYS
    OTHERWISE, AND AGAINST MY INTEREST: its denominator does NOT move with scope either. Wide
    (`--list`) and narrow (`mdpf`) BOTH print `142 events-rules + 12 schedules`.

    THE REAL DISCRIMINATOR IS LEGIBILITY, NOT SCOPE-TRACKING:
      comp-trigger narrow : `forensics for: "mdpf"` + `denominator: 142 ... SCANNED`
                            -> names the query, and labels the number as the SCAN population
      comp-legacywriter   : names neither -- an unlabeled count adjacent to a scoped answer
    So a comp-trigger reader can separate scan-population from answer-population; a
    comp-legacywriter reader cannot. BOTH tools carry a scope-invariant denominator.

    THIS MAKES THE TWO INSTRUMENTS MORE ALIKE THAN MY "one passes, one fails" FRAMING IMPLIED.
    The refutation of the CLASS claim survives -- they still differ, and the difference is real
    and readable. But the axis is narrower than I reported, and a reader who took "scope-correct"
    to mean "its denominator tracks scope" would have been misled by me. Corrected here, in the
    executable artifact, not only in prose.
    """
    if not _have("comp-trigger"):
        pytest.skip("comp-trigger not on PATH -- UNVERIFIABLE, not PASS")

    # `query` is a POSITIONAL ON THE TOP-LEVEL PARSER, not a subcommand argument. An earlier
    # draft passed a literal "forensics" -- argparse silently took it AS THE QUERY (it is the
    # tool's own description word). THE rc=2 THAT EXPOSED IT CAME FROM THE SECOND TOKEN, NOT THE
    # WRONG ONE: `comp-trigger forensics` alone would have exited 0 on a scope matching nothing,
    # and I would have scored a PASS against an empty query. A LOUD FAILURE CAUGHT A SILENT ONE.
    rc_wide, wide = _run(["comp-trigger", "--list"])
    rc_narrow, narrow = _run(["comp-trigger", "mdpf"])
    assert rc_wide == 0 and rc_narrow == 0, f"tool errored: {rc_wide}/{rc_narrow}"

    # MUTANT-APPLIED PRECONDITION (COO 153845Z: ~E reached this independently -- an unapplied
    # mutation reads exactly like a guard that cannot be broken). Scope must have BITTEN.
    assert len(narrow.splitlines()) < len(wide.splitlines()), (
        "NON-MUTATING MUTANT: scoped output is not smaller -- the query did not bite, so any "
        "verdict below is about nothing."
    )
    # The ACTUAL predicate: a scoped answer must NAME its scope and LABEL its denominator as
    # the scanned population. Not "the denominator changed" -- it does not, and that is fine.
    assert "mdpf" in narrow.lower(), "scoped run must name its own address space"
    assert "scanned" in narrow.lower(), (
        "scoped run must LABEL its denominator as the SCAN population; an unlabeled count "
        "beside a scoped answer is the comp-legacywriter defect"
    )


# ---------------------------------------------------------------------------------------------
# SPECIMEN 2 -- PAGINATED list-* RETURNS A PAGE COUNT WEARING A TOTAL'S CLOTHING. EXERCISED LIVE.
# ---------------------------------------------------------------------------------------------

def test_specimen_2_live_mutant_paginated_count_is_not_a_total():
    """LIVE. The mutant is the COUNTING METHOD, held over one unchanged population.

    `aws events list-rules --query 'length(Rules)'` applies --query PER PAGE, so it reports the
    LAST page's size with no error and no warning. `--no-paginate` off, `length()` on: the number
    is a page size wearing a total's clothing.

    Measured 2026-07-31 during the WS-E2 census: naive **100** vs paginated truth **142**. The
    census's own denominator would have been 42 short. Landed as law in CLAUDE.md the same day.

    This asserts the DISAGREEMENT is real right now, live, against AWS -- not that the two
    historical literals differ, which is a tautology and would pass in an empty account.
    """
    if not _have("aws"):
        pytest.skip("aws not on PATH -- UNVERIFIABLE, not PASS")

    rc_naive, naive = _run(
        ["aws", "events", "list-rules", "--query", "length(Rules)", "--output", "text"]
    )
    rc_true, true_ct = _run(
        ["aws", "events", "list-rules", "--query", "length(Rules)", "--output", "text",
         "--no-paginate"]
    )
    if rc_naive != 0 or rc_true != 0:
        pytest.skip("no AWS creds in this context -- UNVERIFIABLE, not PASS")

    # The naive form emits ONE NUMBER PER PAGE. That shape is itself the tell.
    pages = [int(x) for x in naive.split() if x.strip().isdigit()]
    assert pages, f"unparseable: {naive!r}"
    if len(pages) == 1:
        pytest.skip(
            f"population fits in one page ({pages[0]}) -- the hazard is REAL but DORMANT here; "
            "a green in this state is not evidence the estate is safe"
        )
    assert sum(pages) != pages[-1], (
        f"PAGE COUNT READ AS TOTAL: --query emitted {len(pages)} per-page counts {pages}; "
        f"a caller taking the last value reads {pages[-1]} against a true {sum(pages)}."
    )


# ---------------------------------------------------------------------------------------------
# SPECIMENS 1, 3-9 -- MUTANT DESIGNS, DECLARED NOT EXERCISED.
# Each states the perturbation and what must move. NONE asserts the estate passes.
# ---------------------------------------------------------------------------------------------

SPECIMEN_MUTANTS = {
    1: dict(
        name="AccessDenied indistinguishable from absent",
        mutant="revoke read on a key that EXISTS; the detector must report UNVERIFIABLE, not ABSENT",
        moves="the failure_direction field: traversal_exact -> unknown",
    ),
    3: dict(
        name="name-substring predicates",
        mutant="add a resource whose name CONTAINS the probe substring but is a different resource",
        moves="the address_space membership count; a substring predicate silently widens it",
    ),
    4: dict(
        name="UTC-4 LastModified misread",
        mutant="an object written 23:30 local vs 03:30 UTC next day; same instant, different date bucket",
        moves="any date-bucketed denominator; a typed Z hides it, a computed offset does not",
    ),
    5: dict(
        name="terraform 'No changes' read as success",
        mutant="run against a DIFFERENT state key; 'No changes' is emitted for a plan that proves nothing",
        moves="nothing -- and THAT is the finding: the message is invariant to the question asked",
    ),
    6: dict(
        name="rc=0 conflating PASS with STALE",
        mutant="freeze the input; a PASS-on-stale and a PASS-on-fresh must not be the same token",
        moves="the vintage field; rc alone cannot carry it (LD-13: score on OUTPUT, never rc)",
    ),
    7: dict(
        name="not-due default literals",
        mutant="advance the clock past the due boundary; a default-literal check answers identically",
        moves="the due computation; a literal default is invariant to time and so cannot detect lateness",
    ),
    8: dict(
        name="self-authored unfailable acceptance criterion (A)",
        mutant="negate the artifact under test; a criterion its own author wrote may still pass",
        moves="the verdict -- if it does not, the criterion is a restatement of the work",
    ),
    9: dict(
        name="self-authored unfailable acceptance criterion (B)",
        mutant="hand the criterion to an oracle EXTERNAL to the author",
        moves="the verdict, exactly as my own conformance allowlist passed 7/7 while the external "
              "lint found 4 -- a check written by the checked party cannot fail on what that "
              "party already decided is fine",
    ),
}


@pytest.mark.parametrize("num", sorted(SPECIMEN_MUTANTS))
def test_specimen_mutant_design_is_declared(num):
    """Every specimen carries a stated mutant and a stated must-move. NOT an estate claim.

    These are DECLARED-NOT-EXERCISED. This test asserts only that the DESIGN is present and
    non-empty -- it does not assert the estate passes any of them, and a reader must not
    convert a green here into a coverage claim. That conversion is specimen 8/9's own failure
    mode, and this suite would be committing it.
    """
    spec = SPECIMEN_MUTANTS[num]
    assert spec["mutant"], f"specimen {num} has no mutant"
    assert spec["moves"], f"specimen {num} does not say what must MOVE"


def test_suite_states_its_own_exercised_denominator():
    """E5's standard turned on E5: this suite declares what it has and has not run."""
    exercised = {2, 10}
    declared_only = set(SPECIMEN_MUTANTS)
    assert not (exercised & declared_only), "a specimen must not be counted in both columns"
    assert len(exercised) + len(declared_only) == 10
    # EXERCISED 2 of 10. The other 8 are designs, not verdicts. Stated, not implied.
