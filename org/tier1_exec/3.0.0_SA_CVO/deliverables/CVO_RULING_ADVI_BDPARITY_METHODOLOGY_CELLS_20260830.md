# CVO RULING -- ADVI_BDPARITY methodology cells (i) SI anchor and (ii) comparison basis

**Seat:** `3.0.0_SA_CVO` (base). **Clock:** 2026-08-30T01:2xZ (read).
**Authority:** Andrew-direct 2026-08-29T212315Z at the `0.4.0_DS_ClientPlatform~C` terminal, VERBATIM:
*"RECS APPROVED BUT THIS IS A MATTER THAT SHOULD BE HANDLED BY 3.0.0_SA_CVO, NOT CRO"* -- record
`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ANDREW_DIRECT_20260829_2123Z_BDPARITY_OPEN_CALLS_RECS_APPROVED_METHODOLOGY_TO_CVO_NOT_CRO.md`
@`7a4d8a1888` (on origin/CLOUD, is-ancestor read 00:5xZ). Referent fixed by the issuer's NARROW reading
(`2.0.0_SA_COO` 84027): the TWO methodology cells. Rider-4 probe SELECTION is NOT ruled here; the wider
reading is a RESERVED card at Andrew (D2-T69-R2).

**STANDING OF THIS DOCUMENT: FROZEN ON COMMIT.** It is written before any Black Diamond figure for the
ruled periods exists on our side. See section 4 for what that buys and what it binds.

---

## 0. The inputs, read at source (vintage on every citation)

| fact | where |
|---|---|
| BD request carries `"returnMethod": "Annualized"` in a static block preserved VERBATIM from the HAR that reconciled to the cent | `infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py:155-157, :181` @`d0f9a8f7e4` |
| SI range is `{"startDate": inception, "type": "SinceInception"}` -- WE supply the anchor | same file `:176` |
| `run()` defaults the anchor: `inception=acct.get("inception", q_start)` -- a missing anchor silently becomes the window | same file `:297` |
| roster inception is trade-start and *"never BD funding-inception"* | same file `:261` (docstring of `discover_accounts`) |
| our side emits CUMULATIVE only, carries `days_linked` AND `calendar_days`, refuses to default an SI anchor (`UNAVAILABLE-NO-ANCHOR`), refuses a window our gold does not span (`UNAVAILABLE-NO-COVERAGE`) | `data/assets/scripts/gold/runners_49f/parity_period_returns.py:33-37, :74-76, :150-157, :252, :281, :308-309` @`da93bcacfc` |
| gold floor: earliest `twr_daily` partition 2024-07-08 | same file `:390`; `0.4.0_DS_ClientPlatform~C` 83417 (535 partitions 2024-07-08..2026-08-28) |
| `c01.cumulative_investment_return` is keyed to FIRST-LINKED-DATE and is not an SI figure | same file `:13-16`; not contested by any seat |
| the ruled period set QTD / YTD / 1Y / SI | `docs/architecture/D2_ADVI_49F_E2E_PRD.md` s.9 Q2, Andrew 2026-08-19 |
| convention half already ruled: editing the builder is in-lane, EXERCISING it is a vendor call; the new ranges inherit NO reconciliation | `1.0.0_SA_CTO` 83426, 83442 |

What is NOT measured by anyone, and this ruling does not pretend it is: (a) whether BD honours the
`startDate` we pass on a `SinceInception`-typed range or substitutes its own inception; (b) what
`returnMethod: "Annualized"` does to a window shorter than one year on BD's side. Both are settled by
the first response, not by argument, and section 3 makes the response carry the answer.

---

## 1. CELL (i) -- WHICH INCEPTION ANCHORS "SINCE INCEPTION"

**RULED: the SI anchor is (b), BD's funding-inception -- the account's inception as Black Diamond holds it.**

Why, in order of weight:
1. The program is *"check our work vs BD's OWN calculated outputs"* (register, D2 PRD s.4a). BD's SI
   figure is computed from BD's inception. An "SI" on our side anchored anywhere else compares two
   different quantities under one label -- a delta between them is a definition delta, not a
   calculation delta, and the harness exists to find calculation deltas.
2. (a) roster `trade_start_date` is a report INPUT that exists only for roster accounts (5 entries
   measured, 3 active -- 83417) and is documented as *not* funding-inception. It cannot anchor a
   5,309-account census and would silently narrow the SI denominator to the roster.
3. (c) first-linked-date is our ingestion artifact. Anchoring SI there makes the comparison
   self-referential: BD would be asked to compute a window that exists only because of when we
   started reading. It is a legitimate window -- it is just not "since inception", and `c01` already
   carries it under its own name.

**ADMISSIBILITY (the half that makes the anchor gradeable).** An SI cell is COMPARABLE only where our
gold's coverage for that account opens on or before the anchor. Otherwise our side cannot produce the
quantity and the cell's outcome is `UNAVAILABLE-NO-COVERAGE` (the module already has this member) --
it is never classified, never counted as EXACT, and never approximated by a shorter window.
PREDICTION, stated so it can be wrong: with the gold floor at 2024-07-08, every account funded before
that date reads NO-COVERAGE for SI, and SI parity is testable only on inception-recent accounts. That
is not a defect of the ruling; it is what the rider-4 "inception-recent account" is for. The SI
denominator is printed as its own line: `si_computed / si_no_coverage / si_no_anchor` (the module's
summary already emits the first and third; the second is required).

**REQUEST-SIDE CONDITIONS, binding on the authorized pull:**
- Every probe account carries an EXPLICIT anchor in the payload. The `:297` default is not to be
  exercised. Where BD's funding-inception is not known to us before the pull, the SI range is OMITTED
  for that account and the cell reads `UNAVAILABLE-NO-ANCHOR` -- it is not defaulted to the window.
- The anchor's SOURCE is printed on the cell (`anchor_basis`, which the module already carries).
  The DS lane names which bronze artifact carries BD's account inception, with file/key; if none does,
  the first response's returned SI range is the source for the census and the probe says so.

---

## 2. CELL (ii) -- CUMULATIVE OR ANNUALISED FOR QTD / YTD

**RULED: the comparison basis is CUMULATIVE, for every period in the ruled set.**

Why:
1. The object under test is the CALCULATION -- geometric linking of daily TWR with the flow
   convention. Annualisation is a deterministic post-transform of (cumulative, day count). It adds no
   information about the calculation and adds one axis on which a delta can be manufactured: the
   day-count convention (365 / 365.25 / actual, `days_linked` vs `calendar_days`). A basis that can
   create deltas from a convention the harness is not testing is the wrong basis for a harness.
2. Sub-year annualisation scales a delta by roughly 365 / days-in-window: a 1 bp QTD delta reads
   about 4 bp annualised. The TIGHT class is defined in bp with CRO's word on N; that threshold means
   nothing if the figure's scale depends on the window length.
3. It costs nothing. The module emits cumulative and both day counts (`:74-76`, `:252`, `:281`), so
   the annualised form is derivable either way without a re-run and without a re-deploy.

**REQUEST-SIDE: `returnMethod: "Annualized"` STAYS AS CAPTURED.** The static block is the reconciled
shape (83426); changing it forfeits the only reconciliation basis the puller has, and we can transform
our side. Whether BD returns an annualised or a cumulative figure for a sub-year window is UNMEASURED.

**THE BASIS OF BD'S FIGURE IS ESTABLISHED FROM BD, NEVER FROM US.** For each cell, `bd_basis` is read
from the response's own labels/fields or from BD documentation. It is NEVER inferred by checking which
of our two figures matches: selecting the basis that yields EXACT is fitting the predicate to the
outcome and would certify silently. If the basis cannot be established from the response, the cell
carries `bd_basis: UNESTABLISHED`, is classified on cumulative, and "basis mismatch" is a legal NAMED
MECHANISM for a non-EXACT cell -- a basis is never SELECTED to produce EXACT. Where BD's basis is
established as annualised for a period, that period's cell compares BD's figure against OUR annualised
figure with the day count printed (`days_linked` and `calendar_days` both), and the cumulative is
carried beside it.

---

## 3. THE DISCRIMINATOR BOTH CELLS SHARE -- the response carries the window it computed

The silent failure named in P1 finding A3 (an SI cell that is arithmetically QTD) and the unmeasured
question in section 0(a) have one cure: **for every (account, period) cell the probe records the
dateRange BD RETURNED -- name, startDate, endDate -- beside the one we REQUESTED.** Requested != returned
is a distinct outcome (`UNAVAILABLE-RANGE-MISMATCH` or as the DS lane names it, with its four-postulate
record and token census per Rule 24), never a classified value. This is what makes BAR 2 (83418: SI-
COMPUTED vs SI-UNAVAILABLE as separate counted outcomes) gradeable against the BD side and not only ours.
It is cheap: the response already carries the ranges; the probe stops discarding them.

**ADJACENT, same class as cell (i), flagged so nobody discovers it later:** YTD's anchor is 1 January of
`q_end`'s year. `"type": "YearToDate"` is ATTESTED on the Dashboard endpoint and UNVERIFIED on
`performancePeriod` (83444 / A2); a `Custom` Jan-1 range is the same quantity UNLESS BD's returned
range differs -- and the returned range is exactly what section 3 captures. If the issuer reads this
sentence as outside the 21:23Z referent, it is a card, not a ruling; nothing in sections 1-2 depends on it.

---

## 4. HOW THIS SEAT GRADES WHAT IT JUST RULED -- the reconciliation of 83435

At 17:46Z (83435) this seat wrote: *"a grader pre-deciding a methodology question would be adjudicating
what it will later grade."* Andrew then placed the methodology here. Both are true; this is how they hold:

1. **STATED IN ADVANCE, THEN FROZEN.** This ruling is committed before any BD figure for the ruled
   periods exists on our side (positive control: `parity_period_returns.py` has been exercised on our
   gold only; the authorized pull is UNFIRED per 84003). A methodology that cannot see the outcome
   cannot be fitted to it -- the same mechanism as the grading bar stated in advance @`d095bc5fc9`.
2. **THIS SEAT WILL NOT AMEND SECTIONS 1-3 AFTER THE FIRST RESPONSE IS READ.** Any change to the SI
   anchor or the comparison basis after that point is a CONVENTION CHANGE under P3-3 and rides
   `1.0.0_SA_CTO`'s gate -- proposed by whoever proposes it, this seat included, and graded by CTO,
   not by this seat. A P3 cycle that concludes "the ruled anchor was the wrong convention" is graded
   by CTO; this seat recuses from grading that determination.
3. **WHAT THIS SEAT GRADES:** CONFORMANCE (the build carries anchor, basis, returned-range and outcome
   fields as ruled), COVERAGE (BAR 1: the accounts x periods denominator, both numbers printed), and
   the SILENT-FAILURE LIMB (BAR 2: SI-COMPUTED / SI-UNAVAILABLE counted separately, now on both
   sides). **WHAT IT DOES NOT GRADE:** whether sections 1-2 are the right methodology -- that is CTO's
   at the convention gate and Andrew's above it.
4. **VETO WINDOW.** `2.0.0_SA_COO` (issuer) and `1.0.0_SA_CTO` (arch gate) receive this in the same
   turn as the DS lane. An objection before the pull fires re-opens the cell; silence past the fire is
   acceptance of this as the graded methodology.

---

## 5. Effect on the sequencing clause

The approved rec's own clause was *"answer it together with CALL 2, not before it."* CALL 2 is answered
above. **The sequencing condition is DISCHARGED by this ruling.** The vendor word is Andrew's 21:23Z, not
this seat's; the scope is the recorded one and no wider: the ruled QTD/YTD/1Y/SI periods, 3-5 probe
accounts, no schedule, no cadence, no widening of any grant. The pull may fire once the request-side
conditions in sections 1-3 are met (explicit anchors; returned ranges captured). Probe-account
SELECTION is not moved by this document; it stays where the face puts it until the reserved card is
answered (84027).

Nothing is owed to this seat except the probe table, which it grades.
