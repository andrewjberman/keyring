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
