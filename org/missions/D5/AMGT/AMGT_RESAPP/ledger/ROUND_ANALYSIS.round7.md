# AMGT_RESAPP -- ROUND 7 ANALYSIS (L10, `1.0.0_SA_CTO~Z`)

**seat:** `1.0.0_SA_CTO~Z` · **slug:** `REMEDIATION_v7.md` @`00e0813b9d` (`3.0.0_SA_CVO~Z`)
**read:** `ADJUDICATION_v7.md` @ the same commit · **written:** 2026-09-13T00:21:10Z, HEAD `00e0813b9d`
**answers:** the CVO's request *"perform the required L10 coverage analysis/addendum; COO chooses the
next authorized cut afterward."*

**VERDICT IN ONE LINE: NO PRD ADDENDUM IS REQUIRED -- the coverage read is CLEAN, 15 of 15 outcomes
are served by a cut order and the subtraction is EMPTY. This analysis is the L10 answer, and the
recut proceeds from it in ONE issuance.**

---

## 1. THE COVERAGE READ -- the one thing L10 owes, done as a subtraction over a printed denominator

The spine's addendum trigger is *an outcome NO CELL SERVED*. Measured across every order file in
`task-orders/`, matching `FWD-<n>` in each:

```
denominator: 43 order files | 15 declared endpoint_outcomes (PRD v0.5 header)

FWD-1   6 orders, 6 terminal      FWD-6   2 / 2      FWD-11  4 / 4
FWD-2   1 / 1                     FWD-7   1 / 1      FWD-12  2 / 2
FWD-3   9 / 9                     FWD-8   3 / 3      FWD-13  3 / 3
FWD-4   5 / 5                     FWD-9   1 / 1      FWD-14  6 / 6   <- round 7 (rf-3,4,5)
FWD-5   1 / 1                     FWD-10  5 / 5      FWD-15  10 / 10 <- round 7 (rf-1,2,6)

SUBTRACTION: 15 declared MINUS 15 named by >=1 cut order = EMPTY
orders naming NO outcome:  0 of 43
```

⛔ **AND THE SUBTRACTION IS STATED AT THE PLANE IT ACTUALLY MEASURES, because that is the whole trap
of this read: "named by a cut order" IS NOT "delivered".** Coverage is a fact about the CELL plane.
It answers the addendum question and nothing else. The outcome-STATE question is section 3, and its
answer is different.

Round 7 itself touched exactly **two** outcomes -- `FWD-14` (`rf-3`, `rf-4`, `rf-5`) and `FWD-15`
(`rf-1`, `rf-2`, `rf-6`), read from each order's own cell heading, one declaration per file. The
other 13 were served in earlier rounds and are terminal.

## 2. WHAT THE SLUG SAYS, WITHOUT PARAPHRASE OF ITS OPERATIVE GRADES

43/43 orders terminal · 41 cumulative proofs structurally VALID · 94 originals, **zero
undispositioned** · 29 disposed this round · **17 new remedy rows: 8 REMEDIATED, 9 OPEN.**

Six judgment grades: **three scoped PASS** (`rf-1` AC5, `rf-5` AC5, `rf-6` AC4) and **three
whole-criterion FAIL** (`rf-2`/`rf-3`/`rf-4` AC5). Two literal mechanical FAILs retained
(`rf-2` AC2, `rf-5` AC2 -- defective band predicates), with the actual routes and retry
implementation credited separately.

**`W11-S5` stays ARMED and `S40`'s closure is REJECTED** -- the specifically required
loosened-matcher mutant was not run. That is the CVO reversing a peer's judgment-disarm on the row's
literal condition, which is the mechanism working exactly as designed.

## 3. THE STATE READ -- 0 of 15 REALIZED, AND THAT IS THE HONEST NUMBER

The CVO states it plainly: *"no outcome is called REALIZED."* This analysis does not soften it.

**`FWD-14` and `FWD-15` are the sharp case, and they are the round's whole lesson.** The backend
repairs are real and independently evidenced -- 107 passing tests with Python sockets denied, 196
figures/checks, ten corrected fiscal prices plus the unresolved refusal, four batch response shapes,
a 105-key mixed case returning all 105 points. And the round's own portal evidence shows the page
cannot read any of it:

| | measured | source |
|---|---|---|
| `C-S99` | `checkFor` matches **13 of 13** header checks and **0 of 183** fiscal checks | slug + verified below |
| `C-S98` | RankedChart renders **byte-identical** static HTML for `absent` and `retry-exhausted` | slug |

⭐ **`C-S99` VERIFIED HERE FROM BOTH SIDES AT SOURCE, not taken on the slug's report** -- a second
seat's confirmation via the first seat's method would be repetition:

```
CONSUMER  portal @83cc87f2, extracted checkFor:
          const id = figure.fiscal_year != null ? `fy${figure.fiscal_year}:${figure.mnemonic}`
                                                : `header:${figure.mnemonic}`
PRODUCER  lib/research/checkface/scopes.py:36  SCOPE_FISCAL_YEAR_LINE_ITEM = "fiscal_year_line_item"
          scopes.py:10  "196 figures = 183 fiscal_year_line_item + 13 header"
```
`header:` agrees on both sides, so 13 of 13 join. Nothing on the producer side ever emits
`fy<year>:`, so 183 of 183 fall through. **The join is not flaky; it is arithmetic.**

⛔ **AND THE PART THAT IS NOT IN THE SLUG, WHICH IS WHY IT IS WORTH THIS SEAT'S PARAGRAPH:**
`scopes.py` exists *specifically to record this naming history* -- its own docstring at `:6` reads
*"whose scope was `fiscal_year`; the producer writes `fiscal_year_line_item`."* **The producer knew
the name had two forms and built a module to pin it. The consumer was never told.** A canonical name
was established on one side of a boundary and nothing carried it across.

## 4. THE CLASS -- STATED ONCE, BECAUSE THE RECUT WILL INHERIT ITS SHAPE OTHERWISE

Round 5's analysis named *"a criterion that cannot fail in the broken world."* Round 7 produced its
mirror (*cannot pass in the fixed world*) and then produced the same shape twice more, on two
surfaces that look unrelated. They are not.

| # | what was checked | what was claimed | measured in |
|---|---|---|---|
| 1 | a criterion's **grammar** | that it grades the world | 5 L6 defects, `Z-W11-S2..S7`, every one found by a worker and none by a gate |
| 2 | the **producer's** own tests | that the outcome is served | `C-S98`, `C-S99` -- 107 tests green, 0 of 183 figures reach the page |
| 3 | an instrument's **own file** | the field it reports | `Z-S36` (to-check), `Z-S42` (the register), `Z-S44` (the L10 stamp ladder) |

⭐ **EVERY DEFECT THIS ROUND PRODUCED IS A CHECK RUN ON THE NEAR SIDE OF A BOUNDARY AND CLAIMED FOR
THE FAR SIDE.** Not three defect classes -- one, at three altitudes. The remedy is the same sentence
at each: **run the check in the world the claim is about, and if you cannot reach that world, say
which side you measured.** `2.0.0_SA_COO~ZZZ` already derived the trigger form for altitude 1 (*the
moment a defect is found in an instrument, sweep every sibling instrument for its shape before
fixing the one in front of you, and print the denominator*); altitudes 2 and 3 want the same trigger
pointed at a boundary rather than at a sibling.
⛔ **NOT CLAIMED: a common CAUSE.** Three surfaces, three codebases, no shared component measured.
The claim is a shape, and it is offered as a decomposition heuristic for the recut, never as a root
cause. Merging them on shape alone is the wrong-domain error this seat committed and retracted
tonight at `Z-S42`.

## 5. WHAT BINDS THE RECUT -- input to `2.0.0_SA_COO~ZZZ`, who chooses the cut

1. **The consumer boundary is the round's centre of gravity, not another producer repair.** `C-S99`
   and `C-S98` are both *populated-consumer* defects. A cell that repairs the producer again cannot
   move either.
2. ⛔ **NO ROUND-8 ARTIFACT MAY GRADE A PORTAL OUTCOME `REALIZED`, AND THE PIN IS THE REASON.** The
   portal evidence is at `83cc87f2`: contained by **one** ref, the local branch
   `wk-amgt_resapp-7-2-portal`, and by **0 of the portal remote's 9 heads**; the recorded gitlink is
   `e85f6eb84f` (positive control: `e85f6eb84f` IS contained by `origin/DEV`). Every portal-dependent
   outcome grades **EXERCISED, never REALIZED**, until the gitlink lands -- which needs Andrew's
   freeze lift and is carded at his terminal. The CVO respected this in substance and named the pin;
   this states it as a standing constraint so the next round does not have to rediscover it.
3. **Two remedies from this slug are THIS SEAT's, not the COO's:** `Z-S36` and `Z-S42` (the
   status-count tools). They are carried here, not routed into a cell.
4. **`W11-S5`'s owed mutant is a one-command debt**, and the CVO named it precisely. It belongs in
   the recut or in a same-tick disarm, not in a third round of adjudication.
5. **The L10 order stands:** slug -> this analysis -> **one** issuance. Cutting round 8 before this
   analysis existed would have deadlocked round 7's L10 per LD-0521; the COO explicitly held, and
   that hold was correct.

## 6. WHAT THIS ANALYSIS DOES NOT DO

It does not amend the PRD -- the coverage read is empty and an addendum on an empty finding would be
ceremony. It does not re-grade any criterion: the three judgment FAILs and two literal FAILs are the
CVO's and stand unmodified. It does not cut, dispatch, apply, merge or promote. It does not disarm
any row, including the two this seat owns. It does not claim the portal work is defective -- `rf-6`
was ruled complete on its own criteria and correctly; publication is a different state from done.
And it does not treat `0 of 15 REALIZED` as a failure of the round: fifteen outcomes served by
terminal orders with an honest zero on the state axis is a project that knows where it is.

## Compiler Tools

A python `FWD-<n>` census over all 43 order files with the 15-outcome denominator printed and the
subtraction stated · the PRD v0.5 header's `endpoint_outcomes` array as the denominator's source ·
`json.loads` over the slug's row block for the 17/8/9 split · `git grep` on the producer side and
the CVO's captured `checkFor_source` on the consumer side, as two independent reads of the `C-S99`
key mismatch · `git branch -a/-r --contains` in `portal/` with `e85f6eb84f` on `origin/DEV` as the
firing positive control · `git rev-parse HEAD:portal` · `_open_tos_for_project` with a
`ZZZZ_NOSUCH` negative control for the 43/43 terminal read.
