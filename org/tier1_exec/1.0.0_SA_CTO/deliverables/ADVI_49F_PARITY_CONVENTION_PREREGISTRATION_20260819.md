# ADVI 49F BD-PARITY -- CONVENTION PRE-REGISTRATION (dated BEFORE any probe read)

**Author:** 1.0.0_SA_CTO -- 2026-08-19 (the probe fires THU-FRI 08-20/21; this table is registered
TODAY so every classification of a non-EXACT delta is a pre-stated hypothesis test, never a
post-hoc rationalization).
**Authority:** push plan SS7 (Andrew-direct: "We need to get to a point where our logic is EXACT");
source facts: `partner_calls/20260819_49F_MIKE_LITTLE_CALL_ANALYSIS.md` sec 2a (rev 2, docx-grounded);
D2 run R11/R12. **Consumers:** the parity harness classifier (DS-class build), CRO methodology
(GIPS contract owner), CVO census grading.

## Standing frame (from SS7, restated once)

Per account x period, our computed figures vs BD's OWN calculated outputs, classified:
`EXACT` / `EXACT-SHIFTED` (+/-1d timing) / `TIGHT` (within N bp, WITH distribution) / `LARGE` /
per-account `MIX-PROFILE`. Census prints its denominator. **Every non-EXACT class needs a NAMED
mechanism -- no smoothing.** Pre-registration licenses CLASSIFICATION of a matching signature; it
never licenses accepting a delta without the mechanism named, and convention CHANGES to our chain
remain CTO-gated (SS7 P3).

## THE FOUR PRE-REGISTERED CANDIDATES

| # | Convention (source) | Expected delta signature | How the classifier recognizes it | Verdict it licenses |
|---|---|---|---|---|
| C1 | **Return-day basis:** BD computes "365 CALENDAR day total return" (Andrew ~15:53 on the call); our chain computes daily TWR on the trading-day frontier. TWR itself is the shared standard on BOTH sides (rev-2 correction: TWR = platform standard + GIPS preference; IRR is the "simple" alternative -- NOT in play) | Small persistent rate deltas that GROW with period length; sensitivity at weekend/holiday boundaries; sub-period returns identical where no weekend spans | Re-annualize/re-compound our series on a calendar-day basis for the tested period; if the delta collapses to ~0, C1 is the mechanism. Correlation of delta size with (calendar days / trading days) ratio per period | TIGHT -> named-convention C1 (day basis). NOT a defect in either engine; drive-to-EXACT decision = whether we mirror BD's basis in the comparison layer (CTO-gated), never in our canonical chain |
| C2 | **Fee timing:** BD marks fees QUARTERLY and does NOT amortize (Andrew's impression, ~15:52); our chain carries fee events as landed | GROSS-of-fee: EXACT (or C1-only). NET-of-fee: sawtooth divergence intra-quarter that RESETS to ~0 at quarter boundaries | Compare gross-of-fee first; if gross EXACT and net diverges with quarter-end convergence, C2 is the mechanism. Check delta ~0 on quarter-close dates | TIGHT/LARGE on net-of-fee off-quarter -> named-convention C2 (fee accrual timing). Comparison harness may evaluate at quarter-ends for the net-of-fee EXACT test |
| C3 | **Pricing source:** BD prices/dividends come from IDC-class vendors (dividend rates quarterly); ours are Schwab-custodial | Deltas decompose PER-SECURITY, not per-flow: a few securities carry most of the value delta; wider on thinly-traded/fixed-income; flows/units EXACT while valuations TIGHT | Position-level decomposition: delta(account value) = sum over securities of qty x (price_BD - price_ours). If concentration in named securities with matching qty, C3 is the mechanism | TIGHT with per-security distribution -> named-source C3 (pricing vendor). Materiality bound question, not a logic change; drive-to-EXACT = source alignment decision at Andrew/CTO, never silent re-pricing |
| C4 | **Source-data deltas (BD vs Schwab):** live named case -- MITCH JOHNSON's book shows BD-vs-Schwab total-value discrepancies AT THE SOURCE (Mike, ~04:45; cause under investigation on their side) | Delta persists even when C1-C3 are all replicated exactly; our figure may match SCHWAB's own statements while differing from BD's | THREE-WAY compare on affected accounts: ours vs BD vs Schwab custodial. If ours==Schwab and BD differs, the delta is upstream of our chain | LARGE/MIX-PROFILE -> named-mechanism C4 (vendor source divergence), routed to the source-reconciliation thread (Mike is the 49F-side contact). EXCLUDED from the our-logic-EXACT bar WITH the account list printed -- never silently dropped from the denominator |

## Discipline riders

1. **Order of application:** classify C4 last (it is the residual after C1-C3 replication) --
   otherwise every unexplained delta escapes into "source divergence."
2. **EXACT-SHIFTED stays its own class** (+/-1d lag correlation) and is not folded into C1;
   day-basis and day-LAG are different mechanisms.
3. A delta matching NO pre-registered signature gets a NEW named mechanism before any
   classification ships -- this table is a floor, not a ceiling.
4. The probe (3-5 hand-checked accounts, THU-FRI) selects for signature separation: at least one
   fee-bearing account off-quarter (C2), one multi-security account with fixed income (C3), and --
   if in the 49F population -- a Mitch-Johnson-case account (C4). Selection at CRO methodology.
5. This file is referenced by D2's PRD; amendments after the first probe read are ADDENDA (dated,
   below the line), never edits to the pre-registered rows.

---

## ADDENDUM A1 -- 2026-08-19 ~19:00Z (STILL PRE-PROBE; the probe has not fired)

**C5 -- VALUATION ACCRUAL BASIS** (source: CRO~A `TRAVIS_GROUP_DECOMPOSITION_HOW_BD_BUILDS_456M_20260819.md`,
exercised same-content-date tie of qt6 group members vs our fact_rps: 276 matched accounts, 223
within 1%, and the residual tail is UNIFORMLY POSITIVE, median +$1,281/account -- "accrual-shaped").
- **Convention:** BD EMV appears to INCLUDE accrued income (interest/dividends) where our
  Schwab-custodial valuation basis may not. Status: INFERRED at registration (CRO~A's own caveat:
  one per-holding check confirms) -- registered as a pre-stated hypothesis, not a confirmed mechanism.
- **Expected signature:** small positive per-account value deltas, concentrated in income-bearing
  holdings (fixed income especially), uniform in SIGN across accounts; distinct from C3 (which
  concentrates per-security and is sign-mixed).
- **Classifier recognition:** add accrued-interest/dividend estimate to our valuation for the
  tested date; if the tail collapses toward 0, C5 is the mechanism. Per-holding accrual check on
  one bond position is the cheap confirm.
- **Verdict licensed:** TIGHT -> named-convention C5 (valuation accrual basis). Comparison-layer
  accrual add-back is CTO-gated like every convention mirror; our canonical chain unchanged.
- **Also carried from the same deliverable (parity-relevant, not conventions):** 12 of 347 Travis
  group members are non-Schwab (16.1M) -- structurally invisible to our feeds = OUT-OF-ORACLE
  class members inside BD's own group totals (bears on the denominator ruling, open-call 3);
  one $6.9M single-account REAL delta + one $5.64M absent-member outlier are OPEN CELLS at CRO~A.

## ADDENDUM A3 -- 2026-08-19 ~19:15Z (STILL PRE-PROBE; corrects + UPGRADES A1 per CRO~A's
closure addendum on TRAVIS_GROUP_DECOMPOSITION_HOW_BD_BUILDS_456M_20260819.md)

1. **A1's tail signature carried an INSTRUMENT-DOMAIN error, owned by its source and corrected
   here:** the $6.9M "REAL delta" was CASH (BD carries free cash as a position; fact_rps is
   securities-only). On the correct our-side basis (b00's own law, `dim_balance.net_mv_plus_cash`)
   the tie is **309/312 accounts within 0.1%, net +$146K on $420M**.
2. **C5 UPGRADED from inferred-tail to MEASURED MECHANISM:** `qt6 EMV - net_mv_plus_cash ==
   accrued interest TO THE PENNY` on every income-bearing account tested; firm-wide magnitude
   $88.0K across 155 positions today. qt6 EMV is proven accrual-inclusive + cash-inclusive
   (qt1 MV == Unaccrued + Accrual identity holds on 100.0% of 120,215 rows; qt6 EMV == qt1 MV
   per account); Schwab `net_mv_plus_cash` is accrual-EXCLUSIVE (measured). C5's classifier is
   therefore EXACT-form, not distributional: delta == accrued-interest, penny-level.
3. **HARNESS BASIS RULE (binds 4a) [WORDING CORRECTED BY A5 BELOW -- as originally phrased,
   "the residual IS the accrual component" made C5 circular]:** our comparison leg values on
   `net_mv_plus_cash` (cash-inclusive) -- comparing on a securities-only basis manufactures a
   false C5-shaped delta out of cash (the exact error A1's source made and corrected).
4. **C5 RIDER SPECIMEN SELECTED (discharges the A1 selection ask):** account ...2917 (largest
   accrual, $22.47K, clean separation) -- CRO~A's selection, probe rider-4 satisfied for C5.
5. **Denominator enrichment (open-call 3 at Andrew, evidence sharpened):** ~$36.3M of the Travis
   book alone is STRUCTURALLY invisible to Schwab-only feeds -- held-away class (Brighthouse
   8.69M, Lincoln 3.70M, Merrill 401k 1.09M, Fidelity 0.99M, NCF DAF 5.64M, Schwab strays
   0.07M) + 12 non-8-digit members. Out-of-oracle is not one class; the census prints these
   subclasses separately.
6. **PARKED DESIGN CELL -- DISCHARGED BY RULING ~1935Z (see A4):** our canonical sits
   accrual-EXCLUSIVE by B_02's PENDING-RULING zero. [Original park text retained: whether the
   canonical chain ever becomes accrual-inclusive was a P3 decision -- Andrew answered it
   same-evening.]

## ADDENDUM A4 -- 2026-08-19 ~19:27Z (STILL PRE-PROBE; ANDREW-RULED, closes A3 item 6)

**VALUATION BASIS RULED NET/REAL (Andrew-direct ~1935Z at the CRO~A terminal, VERBATIM: "if the
cash is not received it shouldnt be counted... the schwab approach is better here" -- record at
org/tier1_exec/4.0.0_SA_CRO~A/deliverables/ANDREW_DIRECT_20260819_VALUATION_BASIS_CASH_NET_REAL_SCHWAB_APPROACH.md).**
- **Effect on the canonical chain:** B_02's zero is no longer PENDING-RULING -- accrual-EXCLUSIVE
  is the RULED basis. The chain does not change; the pending flag retires. Flip mechanics
  (b00 ACCRUAL_STATUS stamp, convention registry entry) execute at the CTO gate + DS lane as
  record-keeping of the ruling, not as a behavior change.
- **Effect on C5:** C5 is now a PERMANENT NAMED-CONVENTION class, resolved at the COMPARISON
  LAYER ONLY (accrual add-back in the harness for classification) -- never by canonical change.
  A C5-classified delta is BD-includes-accrual-we-do-not-by-ruling: explained, expected, and
  carried with its account list.
- **BANKED, surfaced-not-adjudicated (CRO~A as ADVI_PERFORMANCE field-contract owner):** GIPS
  requires accrual accounting for interest income in PERFORMANCE calcs; book-wide impact <1bp
  today, but a bond-heavy single account's cash-basis return series saws at coupon dates
  (specimen stub 2.8% of account value). The layer-split option (SERVE on the ruled net/real
  basis; the perf engine accrues internally where GIPS-grade per-account returns are claimed)
  is the design frame IF that claim is ever served -- a future CTO design cell, activated by a
  served-claim decision, not by this ruling. CRO~A is Andrew-tasked with the parity-findings
  brief + BD performance-endpoint comparison vs our GIPS scripting; results route here.

## ADDENDUM A5 -- 2026-08-19 ~20:19Z (STILL PRE-PROBE; corrects A3 item 3's wording per CVO's
delta re-read 201752Z -- the same shared-derivation class as their C4 catch, one convention over)

**THE C5 CLASSIFIER MUST BE FALSIFIABLE, so the residual is tested AGAINST an independent
comparand, never DEFINED as the mechanism:** the harness computes `residual = qt6 EMV -
net_mv_plus_cash` and **compares it against BD's OWN PUBLISHED accrual component -- qt1's
Accrual field** (whose independence A3 item 2 itself proved: the MV == Unaccrued + Accrual
identity holds on 100.0% of 120,215 rows, and the to-the-penny measurement was made against
exactly that field). `residual == qt1.Accrual` (in-band) -> C5. **`residual != qt1.Accrual` ->
NOT C5 -- the delta stays in the census as unexplained until a mechanism is named.** The
original A3 wording ("the residual ... IS the accrual component alone") would have collapsed
the tail to zero BY CONSTRUCTION -- an instrument that cannot fail, absorbing every unexplained
valuation delta into "C5, explained" forever, which is smoothing wearing a mechanism's name.
The measurement was done right; this fixes the rule that generalizes it. (If the published
decomposition's field name differs at contract time, the comparand is named at the harness's
contract, never derived from the residual itself.)

## ADDENDUM A6 -- 2026-08-19 ~22:5xZ (STILL PRE-PROBE; source: 0.4.0_DS_ClientPlatform~B T2-DIMS
record 224230Z + ADVI_BDPARITY_T2_DIMS_PORTFOLIO_GROUP_20260819.md)

**SUPERVISION-SLEEVE GRAIN (a fourth BD-surface convention, and it is a GRAIN convention, not a
valuation one):** BD's `Account Supervised` column splits a single account into Supervised /
Unsupervised SLEEVES, each carrying its own market value; the sleeves divide the same portfolio
total (allocation identity proven to the cent, positive-controlled, key soundness 29,926/29,926).
**Rule this adds to the name-your-BD-surface rider: a compare row that does not name its
SUPERVISION TREATMENT (sleeve-summed vs single-sleeve vs whole-account) is under-specified even
when it names its surface.** Measured cost of getting it wrong: 12 of 201 group books understated
by $24,605,360.68 total when one sleeve was silently kept (DS~B's own T1 oracle, caught by
cross-implementation disagreement between two non-shared-derivation tools, corrected in place,
T1 proof re-validated rc=0; Travis Penfield unaffected). **Classifier consequence:** a delta that
decomposes as exactly one sleeve's value on affected accounts is a SLEEVE-TREATMENT mismatch in
the COMPARISON LAYER, never a C1-C5 mechanism -- check sleeve treatment BEFORE the C-ladder, or a
grain error launders itself as a convention delta.

## ADDENDUM A2 -- 2026-08-19 ~19:03Z (STILL PRE-PROBE; per CVO P0-2 @cc223ee3b6)

**C4's THIRD LEG, NAMED (the pre-registered row said "Schwab custodial" without naming the
artifact):** the third leg is **Schwab-PUBLISHED figures (client-statement-class artifacts)** --
explicitly NOT our own Schwab bronze/silver, because our canonical gold DERIVES from that feed:
on the VALUE plane "ours == Schwab-bronze" is a derivation chain agreeing with its own input
(shared-derivation, not corroboration). Computed-return compares (our TWR vs a Schwab-published
return) are genuinely independent. **C4 adjudication mode: HAND-ADJUDICATED at P1/P2 (statements
pulled manually for affected accounts); automated at P3 only if a scalable statement source
lands** (Schwab Open Gateway statement integration = the named candidate). The pre-registered
C4 row's signature and verdict are unchanged; this addendum names the instrument that runs it.

## ADDENDUM A7 -- 2026-08-30 04:4xZ (POST-PROBE; a PREMISE fact, not a convention change; text offered by 4.0.0_SA_CRO 85620 under rider 5, appended verbatim by the file's owner 1.0.0_SA_CTO)

Source: 4.0.0_SA_CRO 85559 line 3 / BP1-4 thresholds deliverable section 5 @9f894ec5d9, measured on
twr_daily vintage 2026-08-30T03:22:17Z, 37 partitions 2026-07-01..08-28.

C2's premise 'BD marks fees QUARTERLY and does not amortize' is a statement about BD. On OUR chain the
fee events (cf_gross != cf_net) in the window cluster on two firm-wide dates, 07-07 (5,497 events) and
07-21 (5,888), with 5,499 of 6,192 fee-bearing accounts billed on BOTH, then 146 on 08-10; per-event
fee/BMV p50 15.77 bp, p95 31.74 bp; per-account over the window p50 35.14 bp.

Classifier consequence: the expected net-leg sawtooth has TWO steps at the quarter open, not one; the
quarter-end convergence test and the gross-leg-first rule are unchanged; a fee event exceeding BMV (23
events > 1,000 bp, on near-empty accounts) reads LARGE on the gross-vs-net leg by construction and is
printed, never netted. The pre-registered C2 row's signature and verdict are unchanged; this addendum
records the premise the gross-leg re-read runs against.
