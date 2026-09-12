# INTERIM OUTCOME COVERAGE -- IRPT, 2026-09-12 ~06:30Z

**Why this exists.** Andrew asked where the IRPT outcomes stand and the only answer available was
ROUND 1's grades, because outcomes are graded ONLY at round close. Both rounds are mid-flight, so for
the whole span of an ~18-hour round the estate cannot answer a mid-round outcome question except with
the previous round's numbers. **That is a gap in the cadence this seat designed**, not a shortfall in
any lane's execution. This file is the read the cadence does not produce.

⛔ **THIS IS NOT A GRADE AND DOES NOT SUBSTITUTE FOR ONE.** L9 grading is `3.0.0_SA_CVO`'s and happens
at round close on the round's evidence. **COVERAGE ANSWERS "IS EVERY CELL THIS OUTCOME DEPENDS ON
COMPLETE?" -- NOTHING MORE.** A fully-covered outcome can still grade NOT_REALIZED; round 1 proved
exactly that, closing 0 REALIZED on both projects with every cell swept.

## Method (re-derivable by anyone, no new instrument)

The decomposition's own **outcome coverage line** (cell -> `FWD-n`) read against the **`<status>` of
each issued face**. Two existing artifacts, no tool written, no seat asked for anything.
Denominators printed. Vintage: faces read 2026-09-12 06:15Z.

---

## IRPT_BCKEND -- round 2, 10 of 12 cells complete

| outcome | its cells | coverage |
|---|---|---|
| **FWD-3** | rt-1, rt-8, rt-10 | **FULLY SERVED** |
| **FWD-4** | rt-8, rt-9, rt-10, rt-11 | **FULLY SERVED** |
| **FWD-9** | rt-11 | **FULLY SERVED** |
| **FWD-10** | rt-4 | **FULLY SERVED** |
| FWD-2 | rt-1, rt-2, rt-3, rt-4, rt-7, **rtb-1** | waiting on rtb-1 ALONE |
| FWD-5 | rt-3, rt-5, rt-7, **rtb-1** | waiting on rtb-1 ALONE |
| FWD-8 | rt-8, **rtb-1** | waiting on rtb-1 ALONE |
| FWD-11 | rt-1, rt-2, **rtb-1** | waiting on rtb-1 ALONE |
| FWD-1 | rt-3, rt-5, **rt-6**, **rtb-1** | waiting on BOTH |
| FWD-7 | rt-5, **rt-6** | waiting on rt-6 ALONE |

⭐ **FOUR OF TEN OUTCOMES ARE FULLY SERVED RIGHT NOW and are ungradeable solely because the round has
not closed.** ⭐ **TWO ORDERS GATE THE OTHER SIX, AND `IB-rtb-1` ALONE GATES FIVE.** "10 of 12 cells"
conceals both facts; the coverage read is the stronger instrument and `2.0.0_SA_COO~B` has adopted it
for its own reporting and for the L10 slug.

### The `rtb-1` gate is REAL and was checked, not assumed

This seat asked whether `rtb-1`'s wait on `rt-6` was a genuine dependency or a queue artifact.
`2.0.0_SA_COO~B` answered structurally (96076):

- The decomp separates an **EDGE SET** ("computed from the edge set, NOT CHOSEN", keyed to observed
  completion) from a **slot table derived from it**. `IB-rt-6 -> IB-rtb-1` is in the EDGE SET and is
  **CROSS-SLOT** (rtb-1 in ~1, rt-6 in ~2), so it cannot be one slot's queue artifact.
- `rtb-1` is a **pure VERIFY cell with NO write surface** -- it is defined entirely by what it READS.
  `rt-6` **deploys** three production builds on the **directory** surface, and the directory routes
  are among the v1 routes `rtb-1` replays.
- ⛔ **Seating it in parallel would certify bytes `rt-6` is about to replace, and would put a STALE
  GREEN CERTIFICATION on the record in the interval** -- an authenticated replay asserting a served
  state that no longer exists by the time anyone reads it. Same class as this round's perishable
  post-apply plan and the version count that moved under an authorization, and worse here because the
  artifact is a certification.
- ⭐ **All six of `rtb-1`'s incoming edges are build-or-deploy cells; five are terminal; `rt-6` is the
  LAST cell in the round that still moves served bytes.** So the gate is not a position in a queue --
  it is *do not certify until nothing else will change what you are certifying*, which a verify cell
  with no write surface has **by construction**.

**The three idle slots are idle because nothing is releasable, not because work is held back.**

---

## IRPT_FNTEND -- round 2 did NOT close; round 3 issued

Round 2's 8 outcomes were never regraded, because the round did not close: `FE-s-18` was kept
NON-TERMINAL on a real defect (the tab bodies cannot mount from any network response). Coverage for
round 3 is not yet meaningful -- its six orders were issued at 06:16Z and none is seated.

**Last graded state stands: 0 REALIZED, 5 NOT_REALIZED, 3 NOT_EVALUATED.**

---

## The CTO-side item this read makes concrete

A cadence that grades only at a round boundary makes **every mid-window question unanswerable rather
than merely stale** (`2.0.0_SA_COO~B`'s phrasing, and it is the right one). It is the same shape as
the two timing findings this round already produced: **a measurement's validity has a window.**

**NOT FIXED HERE, deliberately.** Making this read repeatable is a mechanism change, and this seat
held both other lanes to bringing mechanism changes to L10 with the round's evidence rather than
landing them mid-round. The same standard binds this seat. Carried to L10 as a CTO item; **no gate is
proposed, no seat is asked for anything, and nothing about the running rounds changes.**
