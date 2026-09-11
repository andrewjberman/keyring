# POSN_ASTTAX -- ROUND 1 ANALYSIS (L10, 1.0.0_SA_CTO~Z)

> ⛔ **SECTIONS 2, 4 AND 6'S ROUTING ARE SUPERSEDED IN PART BY `ROUND_ANALYSIS.round1-addendum.md`.**
> An Andrew-direct PURPOSE ruling (~07:1xZ, carried as `3.0.0_SA_CVO~Z` C-S3 @`4275402ec2`) arrived AFTER
> this grade committed: ETFClassifier is a CURATED TAGGING LIST, not a single-source-of-truth architecture.
> That STRIKES two routed items ("give the seed a trigger", "account for the 169" -- neither is a defect;
> the TABLE is the one place and the 169 are provenance-attributed). The measurements below all STAND; the
> FRAME does not. Read the addendum for the corrected round-2 routing and the FWD-5 re-grade.

**archetype:** SCRIBE (ledger) · **written by** `1.0.0_SA_CTO~Z` · **2026-09-11**

| | |
|---|---|
| **Answers** | the L10 slug `surface-channel/remediations/REMEDIATION_v1.md` @`517f9547a4` from `3.0.0_SA_CVO~Z` (msg 21252); ADJUDICATION_v1 @`59b0c8470f`; stamps L8/L9 @`60852cc8cd`, L10 @`9b9ac29c4f`; sign-off re-signed v0.3 @`ca8db51d3a` |
| **Graded against** | each FWD's `DONE WHEN` bar, not the cell's completion |
| **Routes to** | `2.0.0_SA_COO~Z` (round-2 recut) · Andrew (design-spec + the classifier-carrier decision) |

---

## 1. THE VERDICT: 0 of 6 REALIZED -- a ONE-CELL INVESTIGATION ROUND that returned a NEGATIVE result, which is its value.

Round 1 cut ONE cell -- AT1-s-1, FWD-5's "which end of the chain is the one place" investigation. 1 of 1
order terminal, 1 valid proof instance, 1 channel item dispositioned, 1 judgment criterion graded (the
CVO censused the third precondition limb itself this round -- the AMGT_RESAPP lesson applied). Not a
build round; the classification cells (AT1-s-2..s-7) are UNCUT, and the surfaces are design-spec-gated.
So nothing is EXERCISED and nothing is APPLIED; **0 of 6 REALIZED, honestly.**

## 2. FWD-5's INVESTIGATION IS THE ROUND, AND IT IS A NEGATIVE RESULT (the useful kind)

**BOTH candidate answers to "one place that flows" FAIL, on non-substitutable axes:**
- **The DICT** (`etf_classification.py`) fails on COVERAGE -- it explains 116 of 285 served entries; 169
  are not reducible to its output -- AND on FLOW: the seed carrying it to the table has NO TRIGGER (101
  references / 55,582 files, every band inspected: not one scheduler, EventBridge rule, CI workflow,
  deploy script or step function; the docstring asks a HUMAN to run it, and an instruction to a person
  is not a mechanism).
- **The TABLE** (DynamoDB `etf-classifications`) fails on DURABILITY -- it IS what serving reads, but its
  116 shared entries are silently overwritable by that same untriggered seed, so a correction there
  looks like it worked until someone runs the seeder.

⭐ **THE FIGURE THAT CUTS AGAINST THE CONCLUSION, and is why this needed a SET COMPARISON not a source
read:** ZERO value-level `asset_class` mismatches across the 116 shared tickers. The chain is REAL and
was run; the mechanism is sound and the coverage is not. A reader who saw only the 116 would conclude
the architecture works. `FWD-5` is therefore NOT_REALIZED and, more usefully, **not realizable as the
system stands** -- it is THREE pieces of work (s.4).

## 3. THE GRADE, PER FWD (all NOT_REALIZED; the reason distinguishes "investigated" from "untouched")

| FWD | bar | verdict | why |
|---|---|---|---|
| FWD-1 | EXERCISED | NOT_REALIZED | classification cells uncut; surfaces gated. The retag (VXX->Structured, GLD->Commodities, the 6/VIXY split) is the right DESTINATION but the WRONG TIMING -- retagging before the carrier (FWD-5) settles is a write the next untriggered seed erases |
| FWD-2 | EXERCISED | NOT_REALIZED | same -- the Cottonwood separation is gated on the carrier resolution |
| FWD-3 | APPLIED | NOT_REALIZED | the class ORDER is rendered on no surface yet -- the S2 (order+color) surface is design-spec-gated |
| FWD-4 | APPLIED | NOT_REALIZED | the per-class COLOR is applied on no surface yet -- same S2 surface, design-spec-gated |
| FWD-5 | EXERCISED | NOT_REALIZED | the negative result above -- no "one place that flows" exists; 3 pieces of work owed |
| FWD-6 | EXERCISED | NOT_REALIZED | the two surfaces not built, so cross-surface agreement is untestable |

## 4. WHAT FWD-5 ACTUALLY REQUIRES (the round's deliverable to round 2)

Sequenced -- and the SEQUENCE is the finding: **the carrier must settle BEFORE the retag, or the retag
is erased.**
1. **Give the classification a durable single source** -- either give the seed a real trigger, or author
   directly in the table. Until then no correction to the table survives the next manual seed run.
2. **Account for the 169 unexplained table entries** -- they are `equity` 166 / `fixed_income` 3. The
   166 carry `equity`, which is ALSO the positioning lambda's unknown-DEFAULT (`lambda_function.py:359`),
   so the served `equity` bucket MIXES dict-classified, unexplained-source, and defaulted-unknown rows
   with nothing telling them apart.
3. **Make UNKNOWN distinguishable from equity FIRST** -- (2) cannot be audited otherwise: you cannot
   inventory what you cannot tell from the default. (This is `FWD-1`/`FWD-10`-adjacent -- an unchecked
   default must not read as a classification.)
4. **THEN** the retag (the 6-Commodities / VIXY+VXX-Structured split, `sub_asset_class`-driven) is safe
   and testable, and "one place that flows" (FWD-5) becomes gradeable.

## 5. CHANNEL DISPOSITION + CARRIED / OWNED

**Channel is clean:** LIMB 2 = 1 investigation item (`POSN_ASTTAX-Z-W1-S1`), 0 undispositioned, 0
defects, 0 malformed, 0 duplicate ids. The CVO's ADJUDICATION_v1 carries two rows -- `C-S1` (GRADUATES
W1-S1) and `C-S2` (the S1a-AC10 judgment grade). Neither disarms this round; the reason is in each row.

- **`is_hedge()` has NO true case** (`POSN_ASTTAX-Z-W1-S1` -> `C-S1`, disarm_owner me). The worker filed
  it OBSERVATION; **the CVO UPGRADED it to BLOCKING** -- a predicate with no true case is a class hazard,
  not a typo: `HEDGE_TICKERS` is built by filtering on `== 'other'`, no ticker carries `'other'`, so the
  set is EMPTY and `is_hedge()` returns False for all 136 incl. the 7 the dict calls `hedge`; the two
  access paths DISAGREE (`get_asset_class('GLD')`='hedge', `is_hedge('GLD')`=False, same process). Scope
  confirmed by the CVO: AUTHORING module only, and DORMANT -- no live call site, NO served figure is wrong
  today. ⛔ **IT STAYS ARMED into round 2 and I do NOT disarm it this turn** -- the slug and the C-S1 row
  both key the disarm to me but *"after S1-a settles the carrier"*, because the reconciliation is a DESIGN
  call with three non-equivalent directions ((a) document+populate `hedge`, (b) retag the 7, (c) delete
  `is_hedge` as dead after a caller census) and option (b) is exactly the write the untriggered seed
  erases if done before the carrier settles. Nothing about round 1 ending changes `HEDGE_TICKERS`.
  Carried as a class-edge note for the C-MEMBERSHIP-AT-L5 work: **trust `get_asset_class`/the DATA, never
  `is_hedge` or the module's stale 3-value comment.**
- **`C-S2` (the FWD-5 judgment grade) is INERT** -- it is a criterion graded PASS, not a live hazard, so
  there is nothing to disarm; its payload is the three-pieces-of-work routed to round 2 (s.4). The one
  other thing it does is **correct a claim this seat relayed to Andrew** -- that the dict and table are
  "one chain, not a fork." True of the MECHANISM, incomplete on COVERAGE (the chain reaches 116 of 285).
  A chain shown at one link is not a chain shown at its coverage; the set comparison settles it, and I
  repeated the COO's generalisation without running it. Logged here as mine to own.
- **THE L4-R GATE HAS A GRAIN MISMATCH, and it is MINE as the gate's owner** (`3.0.0_SA_CVO~Z` flagged,
  not asking to loosen): the CVO re-signed this PRD THREE times in two hours (v0.1/v0.2/v0.3) and the
  ENDPOINT section it certifies never changed (sha `3a69dcfa5f2e`, 6 FWD cards identical at every
  version). The sign-off is version-bound; the CVO's half certifies the ENDPOINT-vs-pins. A bump that
  touches only CONSTRAINTS (my satellite-data + hedge-disambiguation edits) re-opens the ENDPOINT
  sign-off redundantly. Candidate refinement (a gate build, not this round): key the CVO's half on the
  ENDPOINT section's sha, the CRO's on the coverage map's, so a bump re-opens only the half whose
  certified surface moved. Owned by this seat; NOT urgent; NOT loosening the gate, sharpening its grain.

## 6. COVERAGE READ + ROUTING

Every FWD has a cell (S1->FWD-1/2/5, S2->FWD-3/4, S3->FWD-6); **0 uncovered -- no PRD addendum.**
FWD-5's negative result is a FINDING, not a missing outcome. Round 2 (`2.0.0_SA_COO~Z`, ONE issuance):
the FWD-5 carrier work (s.4 items 1-3) FIRST, THEN the retag (item 4). The v0.3 constraints
(C-SATELLITE-DATA, the hedge disambiguation) bind the retag cells; the sign-offs are re-signed at v0.3.

**Push state:** LOCAL at write time. `0.0.0_AB_MSTR~Z` pushes.
