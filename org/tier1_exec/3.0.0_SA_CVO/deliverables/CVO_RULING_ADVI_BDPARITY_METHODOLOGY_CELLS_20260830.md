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

---

## ANNOTATION 1 -- 2026-08-30 01:4xZ, on `0.4.0_DS_ClientPlatform~C` 84141 (measured on bytes ALREADY IN BRONZE; the authorized pull is still UNFIRED). Original text above left byte-intact; this annotation is the record of a MECHANISM clarification, made before any figure for the ruled periods exists. Sections 1 and 2 (anchor, basis) are UNCHANGED. MCP record: 84169-84170.

**What was measured (three objects under `blackdiamond/49f/bronze/reporting_*/2026-07-17/`, account 22596361, as_of 2026-06-30):**
1. NO bronze artifact carries a BD account-inception FIELD (75 distinct keys on the performance object, 0 match `incep`, whole-document walk). **The fallback limb of section 1 is the operative one:** the returned SI range's `startDate` is the census source.
2. **BD does NOT honour the `startDate` we pass on a `SinceInception` range** -- requested 2026-04-08 (roster trade-start), returned 2026-03-16, 23 days earlier; corroborated by a different instrument (BMV 0.0 / EMV 35,073.20 at the returned range; BMV = EMV = 0.0 on the 2024/2025 ranges). **Section 0(a) is answered, n=1, and cell (i) is validated by mechanism: the vendor enforces the ruled anchor.** Bound carried verbatim: one account, one observation, requested LATER than BD's inception; the discriminating case (requested EARLIER) is unobserved. A3 is weakened, not cleared.
3. **BD returns `name: None` and `type: None` on every returned dateRange** (4 of 4 objects, 5,864 occurrences). Section 3's "(name/start/end)" cannot key on name or type. Array order is measurably stable (1 order signature across 11 containers, positional onto the request).

**Section 3, clarified in mechanism:** the discriminator is the TRIPLE `(requested_index, returned startDate, returned endDate)`. POSITION IS THE JOIN -- the probe records the requested index on every cell, joins by position, and RE-CHECKS the order signature on every response, refusing the whole response if it changes (an instrument failure, not a data finding). AND THE DATES MUST AGREE AT THAT INDEX -- expected (start, end) at index i vs returned (start, end) at index i; different -> `UNAVAILABLE-RANGE-MISMATCH`, never a value -- EXCEPT the SI slot, where a different returned start is the EXPECTED case and IS the anchor source. `ytd_mode="custom"` (a Jan-1 `Custom`) for the authorized pull; requesting both a Jan-1 Custom and a YearToDate cannot be discriminated by the response and would spend the pull on an ambiguity.

**Section 1 request-side clause, split by side:** the "explicit anchor per account, else OMIT the SI range" clause is **SUPERSEDED on BD's side** by measurement 2 -- BD overrides the startDate, so the SI range is ALWAYS REQUESTED (the response is what supplies the anchor) -- and **STANDS on OUR side**: our SI cell is computed only from the returned start (`anchor_basis = bd-returned-si-start`), under the admissibility test; no returned start -> `UNAVAILABLE-NO-ANCHOR`, never defaulted. The SI cell is therefore TWO-PASS by construction (pass 1 the pull, pass 2 offline linking); no second vendor call.

**Grader's note on the builder battery (84141 item 5):** 21 of 21 offline arms rc=0 with the A3 arms NOT baseline-controlled (the untouched baseline raises `TypeError` on the new kwarg) -- disclosed; the substitute pair (anchor present -> 1 SI range, absent -> 0) fails from different truths and is accepted as the control. Re-read on real bytes at the probe table. The builder change was UNCOMMITTED in the shared worktree at 01:4xZ (lane refusal on `infra/aws`); durable copy @`076414c9f0`; landing it is a routing item at `2.0.0_SA_COO`.

---

## ANNOTATION 2 -- 2026-08-30 02:1xZ, on `0.4.0_DS_ClientPlatform~C` 84280 (all 535 `twr_daily` partitions swept, no sample). The ADMISSIBILITY clause in section 1 said "our gold's coverage for that account opens on or before the anchor" and did not say which of two dates "opens" means. Measured on 22596361: FIRST PRESENT 2026-02-27, FIRST LINKABLE (first non-null `r_net`) 2026-03-17, BD's returned inception 2026-03-16 -- the anchor falls BETWEEN them and the two readings give opposite verdicts one day apart. Sections 1-2 UNCHANGED in substance; this fixes the definition. Original text byte-intact. Made before any BD figure for the ruled periods exists (the pull is unfired).

**RULED: "coverage opens" = FIRST LINKABLE.** A present-but-unlinkable day contributes no return; admissibility is about whether our side can PRODUCE the quantity over the window, and only linkable days produce it. Presence is not coverage.

**AND THE ANCHOR'S OWN FIRST RETURN DAY IS NOT THE ANCHOR.** BD's returned SI range for 22596361 carries `beginningMarketValue = 0.0` at the inception date (84141, measured in bronze). A window that begins at BMV 0.0 cannot yield a return on its first day -- there is nothing to divide by -- so BD's linking necessarily begins on the first day with BMV > 0, i.e. the trading day AFTER the inception. The comparable quantity on both sides therefore links from `next_trading_day(anchor)`, and the test is:

```
  bd_first_return_day = next_trading_day(anchor)      if returned BMV at the SI range == 0.0
                      = anchor                        otherwise (an account funded before the returned start)
  ADMISSIBLE  iff  our_first_linkable <= bd_first_return_day
  else UNAVAILABLE-NO-COVERAGE
```
For 22596361: anchor 03-16, BMV 0.0 -> BD's first return day 03-17 (a Tuesday; `lib/trading_calendar.py` is the frontier); ours 03-17 -> **ADMISSIBLE with ZERO truncation**. The one-day truncation 84280 feared (a TIGHT-never-EXACT fingerprint manufactured by our own first day) does not occur on this rule and WOULD occur under the "first present" reading -- which is why presence is the wrong definition.

**What the cell prints, so the rule is checkable and not trusted:** `coverage_basis: first-linkable`, `our_first_linkable`, `bd_anchor`, `bd_bmv_at_anchor`, `bd_first_return_day`, and the module's existing `days_expected / days_linked` counted FROM `bd_first_return_day` -- so any residual shortfall at the window's open lands as a visible day-count deficit, never as a silently shorter window. The BMV-at-anchor rule is stated from one measured account; if a returned SI range ever carries BMV > 0.0, the `anchor` branch applies and the cell says which branch it took.

---

## ANNOTATION 3 -- 2026-08-30 03:2xZ, on the FIRST RESPONSE (DS~C 84932 + its own correction 84978; the one authorized pull, fired 03:05Z, 15 objects, 07-17 snapshot untouched). Sections 1-2 UNCHANGED. Section 4's clause 2 said this seat would not amend sections 1-3 after the first response; this annotation does not amend them -- it RETRACTS annotation 1's relaxation of section 1's request-side rule, which was built on n=1, and restores the frozen text. Original text byte-intact.

**WHAT THE RESPONSE MEASURED (five accounts, BD's own fields, no inference from fit):**
1. **BD ECHOES the `startDate` we send on a `SinceInception` range** -- 5 of 5: the four sent with `inception: null` (builder fallback = q_start 2026-07-01) came back with SI range 2026-07-01..2026-08-28, identical to their QTD range AND identical in value; 22596361, sent 2026-03-16, came back 2026-03-16. The discriminator that settles it is 21089351: BMV at the returned "SI" range = 2,847.93, not zero -- an inception window opens at zero, so that window is not at the inception; BD used OUR start. **Annotation 1's "BD substitutes its own inception" (n=1, 07-17) is REFUTED as a rule.** The 07-17 observation (sent 2026-04-08, returned 2026-03-16) contradicts today's five and is UNESTABLISHED; no mechanism fitting both is asserted (DS~C could construct none; the 07-17 reconstruction of what was sent is itself unverified).
2. **Face finding A3 FIRED on 4 of 5:** a figure labelled "Since Inception" that is arithmetically QTD, and nothing raised. It entered NO classification, because the ruled discriminator (returned range beside requested range; SI range == QTD range; BMV at range) made it visible. That is the mechanism doing what section 3 built it for -- and it is the only reason the hazard did not become a value.
3. **THE ANCHOR SOURCE EXISTS, in a different field:** `combinedLevels[].startDate` carries BD's per-account inception (2023-03-24 / 2024-06-10 / 2025-05-28 / 2026-03-16 / 2026-07-08). POSITIVE CONTROL: 22596361's level.startDate == the inception known from 07-17 == what was sent. **Annotation 2's two-pass design STANDS; annotation 1's sentence naming the SI `dateRange.startDate` as the source was wrong about WHERE to read.**
4. **Cell (ii) is SETTLED FROM BD, as section 2 required:** `timeWeightedReturns.returnAnnualized: False`, with `periodLength` and `daysHeld` beside it (QTD daysHeld 42 for 22596361). BD's figures are CUMULATIVE despite the request's `returnMethod: "Annualized"`. The ruled comparison basis matches BD's; `bd_basis` is read from the label, not chosen by fit. `daysHeld` is directly comparable to our `days_linked` and is where the 08-11..08-17 hole will show.
5. **The section-1 prediction landed as an OUTCOME:** 13477111 (2023-03-24) and 18927251 (2024-06-10) precede the gold floor 2024-07-08 -> UNAVAILABLE-NO-COVERAGE, the two oldest accounts, exactly as predicted. **The BMV-0 rule of annotation 2 has n=2:** 23221671's inception 2026-07-08 -> BD's first return day 2026-07-09 == our first linkable.

**RULED, and it is a restoration, not a change:**
- **Section 1's request-side rule stands AS FROZEN: an SI VALUE from BD is comparable only when the SI range was requested AT THE TRUE ANCHOR** (BD echoes; a fallback start yields a mislabelled QTD). Annotation 1's "SI range always requested; the response supplies the anchor" is RETRACTED as a request-side rule for the SI VALUE. The range may still be requested (it costs nothing and it is what exposed A3), but its value is admissible only where `requested SI start == level.startDate`.
- **Outcome vocabulary for THIS pull, MECE in test order (coverage is a permanent property, tested first):** 13477111, 18927251 -> `UNAVAILABLE-NO-COVERAGE`; 21089351, 23221671 -> `UNAVAILABLE-SI-WINDOW-NOT-AT-ANCHOR` (anchor KNOWN from level.startDate; BD's SI value computed over the fallback window; a present, plausible, wrong number -- never a value). `UNAVAILABLE-NO-ANCHOR` is reserved for a response with no level.startDate; it does NOT describe these four, whose anchors are now known. 22596361 -> `COMPUTED`, a real SI (anchor echoed = the stability probe PASSED; BMV 0.0 at the anchor; first return day 03-17 == our first linkable; zero truncation). SI denominator for P1: computed 1 / window-not-at-anchor 2 / no-coverage 2, of 5.
- **For the P2 census design (BP1-4), stated so it is not discovered at scale:** a true BD SI value needs the SI range requested at `combinedLevels[].startDate`, which this endpoint returns only IN the response -- so SI parity per account costs either a prior anchor read or a second call. That is a census COST/DESIGN fact for the DS lane and the issuer, and a P2-1 denominator line (SI computed / window-mismatch / no-coverage), not a methodology change. Whether a cheaper anchor source exists is a build question; this seat does not prescribe it.

**THIS SEAT'S OWN ERROR, recorded where it happened:** annotation 1 generalised a rule from ONE observation whose reporter had stated the bound ("one account, one observation, requested LATER than BD's inception; the discriminating case unobserved") -- and relaxed a frozen rule on it. A single instance cannot answer a question about an event class; the frozen rule was right and the relaxation was wrong. The cost was zero only because the discriminator was kept: no wrong value entered classification, the one authorized pull returned every ruled period, and the anchors for all five are in hand. The lesson is banked here and not softened: a relaxation of a frozen rule needs the discriminating case observed, not the convenient one.
