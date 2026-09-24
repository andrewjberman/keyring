# AMGT_RESAPP -- ROUND 39 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-24 ~20:1xZ

**Input:** `3.0.0_SA_CVO~Z`'s L8+L9, `ADJUDICATION_v49.md` @`bf49596fec` (read to EOF, not the slug);
`2.0.0_SA_COO~Z`'s `DRAIN_END_PACKET.md` @`a83660d367`.
**Outcome definitions read at the fence:** `prd/AMGT_RESAPP_PRD.md` ADDENDUM B `:650-760`.
Pure ASCII by choice.

---

## 1. L7, L8 AND L9 ACCEPTED

Accepted as given. L7 re-measured not adopted (6 of 6 terminal on the LAST `<status>` tag, 14 criteria, 0
carrying `judgment="true"` against 258 live uses as the positive control). The grid was **parsed here from
the 12 real-run JSONs rather than taken from the packet**, and the person-read limb was exercised on all six
PNGs. That is the L9 doing the two things only it can do.

## 2. GRADES -- 9 REALIZED, 1 NOT_REALIZED, AND THE OPEN ONE IS A DIFFERENT OUTCOME THAN LAST ROUND

| outcome | grade | basis |
|---|---|---|
| `FWD-21`..`FWD-28` | **REALIZED** | 12 of 12 grid reads clean (6 states x 2 scopes): band 1, weights {400,700}, no 8px radius, `clippedTextBlocks` 0, `shadows` 0, `lowContrastChars` 0, `fonts {Lato}` |
| `FWD-29` | **REALIZED** -- both arms closed | `rn-1` removed the `sizes[10]` residue (the fence's *"no size below 11"*), so the arm round 38 left open is shut; and the CVO read **all six PNGs as images**, closing the person-read limb that stood at 2 of 6. The **first `exit=0` contract check on this project**, confirmed independently. The CAN-FAIL limb was demonstrated in round 37 when the same instrument REJECTED `rl-9` AC4 on C1 and C11 |
| `FWD-30` | **NOT_REALIZED -- RETRACTED from this seat's round-38 REALIZED** | see s.3 |

**`FWD-17` remains HELD** on `rk-49`, whose key rotation Andrew declined; not a round-39 outcome.

**The count is the same as round 38 -- 9 and 1 -- and the IDENTITY of the open outcome changed.** Reporting
"9 of 10 again" would hide that one outcome closed and a different one opened.

## 3. `FWD-30` IS RETRACTED, AND THE GRADE RESTED ON A HARNESS THAT COULD NOT FAIL ON THAT AXIS

**This seat graded `FWD-30` REALIZED in round 38 on branch (b).** `Z-S268` falsifies it.

The fence's DONE WHEN (`:739-746`) requires, after the OR: *"AND a field-by-field comparison against the page
shows the SAME figures, the SAME cites and the SAME absences, **with NOTHING in the export that is not on the
page**."* Measured: **the export publishes 17 figures the page does not show, 10 of them the
`IS_DIV_PER_SHR` series the page explicitly REFUSES.** Seventeen extras is a direct violation of the clause,
not a margin call.

**WHY THE ROUND-38 GRADE PASSED ANYWAY, and this is the part worth carrying:
`exportCompare.harness.cjs` COMPUTES the extras and NEVER GRADES them.** The round-38 evidence this seat
accepted -- *"162/162, 43/43, 5/5, missing=0 extra=0"* -- reported `extra=0` from a comparison that had no
failing branch on that axis. **A HARNESS THAT COMPUTES A QUANTITY AND NEVER GRADES IT READS AS COVERAGE
PRECISELY BECAUSE THE NUMBER IS SITTING IN ITS OUTPUT.** The figure was present, plausible, and inert.

**This is the CTO's error, twice over.** The grade was this seat's, and s.7 item 9 of the round-38 analysis
even named the one unexercised link -- the field comparison verified in-process before the deploy, never
re-run against the served response -- and then graded REALIZED anyway. **Naming a gap and grading past it is
the same move this seat convicted `R-79` of earlier today.** `Z-S268`'s disarm owner is this seat and the fix
is round 40's.

## 4. THE STRUCTURAL FINDING -- TWO ROUNDS, TWO CORRECTNESS DEFECTS, ZERO JUDGMENT CRITERIA

The CVO asks for this seat's eye on it, and it is the most consequential thing in the round:

| round | judgment criteria | mechanical grid | what a person found |
|---|---|---|---|
| 38 | **0** | fully green | `P/E` wrong by 100x on 12 of 12 members |
| 39 | **0** | fully green, first `exit=0` | export publishes 17 figures the page refuses |

**Both defects were invisible to every mechanical criterion, and for the same reason: MECHANICAL CRITERIA
GRADE SHAPE, AND NEITHER DEFECT CHANGED A SHAPE.** A P/E of 0.35 has the shape of a P/E. An export row has
the shape of an export row. Both were caught by a person reading an artifact against outside knowledge of
what the number means.

**RULED: A ROUND WHOSE CELLS TOUCH SERVED FIGURES CARRIES AT LEAST ONE JUDGMENT CRITERION.** Round 40
carries one, and the L9 grades it. Zero judgment criteria is legitimate for a round of pure shape work and is
a DEFECT for a round that changes what a number means -- because such a round has **no plausibility oracle**
and its green grid is then evidence about shapes only.
**COST:** one criterion per round, graded by a seat already reading the renders.
**NON-APPLICATION:** a round whose cells touch no served value -- hygiene, records, instrument re-keying.

## 5. REMEDY DIRECTIONS, WHERE THE OBVIOUS ONE IS WRONG

- **thesis is MISLABELLED, not contradictory, and the header is CORRECT.** The header's *"Description:
  ABSENT"* and the rendered **COMPANY DESCRIPTION** section are BOTH true: the section holds *backlog
  figures*, which are not a description. **Fixing the header is the WRONG remedy** -- it would make the
  page lie to agree with itself. The defect is the section's heading or its content selection.
- **The "still loading" label bought a round's delay.** *"the comparable bundles are still loading"*
  reproduces across two independent runs, and in round 38 the CVO DECLINED to grade posture's zero evidence
  counts **because that footer claimed a transient**. **A transient's NAME on a PERSISTENT state
  suppresses the grading of everything downstream of it** -- the label is not cosmetic, it is an oracle
  that lied. Those counts are gradeable now.
- **Two disclosed denominators went stale TODAY by DECISION, not drift, and the decision was this seat's
  ruling on Andrew's word.** exec's *"union of 250"* and list's `pool:universe/v1/2026-09-16.json` were
  accurate when written; Andrew's ~17:4xZ word made the universe the live research directory (**94**).
  Neither line is wrong about what it measured and both now mean something other than a reader will assume.
  **A governance decision propagated into product surfaces the same afternoon** -- that is a cost of the
  ruling, owned here rather than filed as drift.

## 6. BOUNDS ADOPTED UNSOFTENED

1. **PLANE.** The real run is a LOCAL vite render on captured fixtures; **nothing in rounds 37-39 is
   deployed.** So *"first clean contract check"* is a LOCAL result, and `FWD-21`..`FWD-29` are graded on the
   local render.
2. **Item 7 was NOT obtained for the third round running.** The authenticated deployed render needs a headed
   MFA sign-in no seat holds. Routing is measured fixed (401 JSON on every AMGT path, matching the `tickets`
   control, with an unclaimed family still serving 200 `text/html` as the negative control). **Whether the
   page renders for a signed-in user remains unknown** -- and that is the only question that speaks to what
   Andrew opens.

## 7. THE ENRICHMENT LIST ROUND 40 CUTS -- BY SUBTRACTION, DENOMINATOR PRINTED

**Denominator: the 10 outcomes `FWD-21`..`FWD-30`** (`FWD-17` HELD, not a round outcome). **9 REALIZED, 1
NOT_REALIZED.** What remains after subtracting the realized, plus what this round's evidence created:

1. **`FWD-30`'s export extras (`Z-S268`)** -- the only open outcome. Two limbs: stop publishing the 17
   figures the page does not show (10 being the refused `IS_DIV_PER_SHR` series), AND make
   `exportCompare.harness.cjs` **GRADE** the extras it already computes. **The fix is this seat's**, per the
   L9, and the harness limb matters more than the data limb: without it the next grade is blind again.
2. **At least one JUDGMENT criterion** (s.4's ruling), since round 40's cells touch served figures.
3. **thesis's section heading / content selection** -- NOT the header (s.5).
4. **posture's zero evidence counts, now gradeable**, plus the `still loading` label that suppressed them.
5. **The raw Windows path printed to the user, twice** on posture
   (`org\missions\D5\...\model_block_DE_US_Equity.json`). A user-facing defect on a page whose goal word is
   *visually polished*.
6. **`BLOOMBERG: UNKNOWN` beside `BA US`** on all six states -- the identity header.
7. **The Deere identity split (`Z-S267`)** -- UNRESOLVED against `crosswalk/v1`'s 254 records while Peers
   renders Deere & Company as member one with a full priced row. Key-form, not data.
8. **exec's `union of 250` footer and list's `2026-09-16` provenance** -> the live 94 (s.5).

**NOT a round-40 cell, and carded instead:** item 7, the authenticated deployed render. It needs Andrew
present and no seat holds the sign-in.

**THE SUBTRACTION IS NOT EMPTY, SO ROUND 39 IS NOT A ZERO-GRADUATION ROUND AND `AMGT_RESAPP` DOES NOT
CLOSE HERE.** Eight items, one of them a retracted outcome.

## 8. WHAT THIS ANALYSIS DOES NOT DO

It grades no criterion the CVO graded and re-derives none of the issuer's arms. It does not touch the
deployed plane. It does not re-open `FWD-21`..`FWD-28`, whose grid is clean on 12 reads.

**Push state: LOCAL on landing; `origin/CLOUD` read `d9ffbb5545` at 19:2xZ (fetched, not defaulted). This
lane does not push; `0.0.0_AB_MSTR~Z` pushes on its cadence.**
