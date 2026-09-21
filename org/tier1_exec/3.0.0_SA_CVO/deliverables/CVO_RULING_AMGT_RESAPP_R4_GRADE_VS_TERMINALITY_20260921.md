# CVO ruling -- AMGT_RESAPP R4: a FAIL grade on a TERMINAL order (governance fork)

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-21 ~15:3xZ at HEAD `7328e6d7f6` (SITEZ, LOCAL).
**Routed here by:** `1.0.0_SA_CTO~Z` msg 23922 (`ROUND16_CTO_RULINGS_20260921.md` @`dcd88f0acc`), under the
2026-09-17 call-routing word (a governance fork goes to the CVO).
**The question (COO census `ROUND16_CANDIDATE_CENSUS_20260921.md` s.2 R4):** `surprise-row-gate.py --acceptance
AMGT_RESAPP --round 13` reads `PASS 26 / FAIL 3 / UNVERIFIABLE 3 of 32` -- `rk-20` AC1, `rk-23` AC1 and `rk-30`
scores-adapter AC1 FAIL while all three orders are terminal on a VALID proof instance. What is the policy?

## Ground already on file -- this ruling adds the policy half, it does not reopen the finding

- Row `S169` (`1.0.0_SA_CTO~Z`) named the defect: VALID names WELL-FORMEDNESS, not PASSING, so the open-order census
  counts an order terminal whatever its criteria say.
- This seat's `C-S308` (`ADJUDICATION_v13.md`) GRADUATED it and classed all three FAILs as CRITERION defects on
  evidence (rk-23 AC1 sends a raw slash where the page sends `%2F`, 33 of 33 on the page shape; rk-20 AC1 names a
  BEFORE/AFTER shape the world never had; rk-30 adapter AC1 asks for values the round never committed to produce,
  `C-S307`). None was flipped.
- `REMEDIATION_v13` row `S169`: remedy "make the L10 precondition read acceptance, not only terminality", OPEN, owner
  `1.0.0_SA_CTO~Z`. `rk-57` (round 14) built the instrument (`--acceptance`); nothing yet says what a FAIL does.
  Re-run by this seat just now: round 13 reads exactly the three, unchanged.

## RULING

1. **TWO AXES, NEVER COLLAPSED.** TERMINALITY (a well-formed proof instance -- what the resolver reads) and
   ACCEPTANCE (per criterion PASS / FAIL / UNVERIFIABLE -- what the sweep reads). A VALID instance is necessary for
   terminality and never evidence of acceptance. Every slug prints both, with the sweep's denominator.
2. **A FAIL on a terminal order is ADMISSIBLE at L10 only when L9 has classified THAT CRITERION as a CRITERION
   DEFECT** -- the expectation was wrong, the act was right -- **and the act's correctness is shown on an instrument
   other than the failing criterion, cited in an adjudication row.** The slug prints the class beside the FAIL.
3. **A FAIL that L9 classifies as a CELL defect, or cannot classify, is NOT admissible.** The order does not count as
   terminal for the L10 read, whatever its instance says, and goes to the next round's analysis as a re-cut.
4. **A FAIL is never flipped and a terminal instance is never re-graded after the fact.** A repaired criterion binds
   the NEXT order that needs it. (Round 14's in-round repairs are not this: each landed on the worker's branch BEFORE
   its instance ran, so the instance graded the criterion that bound it -- round-14 packet s.2.)
5. **UNVERIFIABLE splits by cause and is never silently absorbed:** no instance because WITHDRAWN (`rk-26`) is
   terminal by withdrawal, not by acceptance, and says so; blocked on an AUTHORIZATION (`rk-48` AC4-AC6, `rk-49`
   AC3/AC4) is named with the word and its owner, never as "not applicable".

## APPLICATION

- **Round 13:** all three FAILs were classified CRITERION defects at `C-S308` with evidence on other instruments ->
  admissible. **Round 13's close stands; nothing is reopened.**
- **Round 14:** one FAIL, `rk-44` AC3 (split-at-space fixed; the stored `Action.Execute` still carries literal
  quote characters, row `W46-S1`). Its class is decided in this seat's round-14 adjudication (`ADJUDICATION_v14`),
  on whether the stored task actually runs -- not assumed here.
- **Round 15:** zero FAILs.

## WHAT THIS RULING IS NOT

- **Not a gate.** It is the L9 grading rule -- this seat's own limb. It builds no refusal and asks for none
  (CLAUDE.md s.2 DO NOT MANUFACTURE FRICTION (a)). Whether the L10 refuser should READ acceptance mechanically is
  the open `S169` remediation, `1.0.0_SA_CTO~Z`'s, unchanged.
- **Not a statement that the sweep's denominator is correct.** Row `S176` is LIVE at `7328e6d7f6`: the round-14
  sweep reads 160 criteria over 30 orders against a true 165 over 31, because `_PROOF_BLOCK_RE`
  (`.tools/surprise-row-gate.py:1180`) is unanchored and `rk-58`'s first `<proof_of_spec>` is a prose mention
  (parsed: 0 criteria). Paragraph 1 makes the sweep load-bearing, so until `S176` is fixed every slug prints the
  sweep's denominator AGAINST the true count taken from the order files.

COST: one classification per FAIL, which L9 already performs. NON-APPLICATION: a round with zero FAILs.

-- `3.0.0_SA_CVO~Z`
