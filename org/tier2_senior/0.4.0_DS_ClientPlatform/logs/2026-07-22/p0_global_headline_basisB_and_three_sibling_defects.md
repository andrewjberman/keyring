# MDPF_REVAMP P0 -- global headline internally inconsistent: Andrew-caught, basis-B implemented, THREE sibling defects found after the fix (DS)

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, VALIDATE, COORDINATE
**Serial:** 0.4.0_DS_ClientPlatform | **Date:** 2026-07-22 | **Window:** ~23:37Z (prior log d0575b280) -> ~05:45Z

## Summary
Andrew caught a real bug on the LIVE Global view after the flip. Root-caused it at source in one pass,
took the business call to Andrew (he ruled EXCLUDE/B), implemented it -- and then the fix's own
verification surfaced THREE MORE defects, one of which I introduced and one of which my own new gate was
structurally blind to. All four closed, each with a mutant-proven assertion so the class cannot recur.
Net: 4 producer commits + 3 ledger commits, coherent-9 re-staged and FROZEN, re-publish HELD, live serve
on legacy throughout (router rollback fired before I started).

## The four defects (the arc, in the order they surfaced)
1. **THE P0 (Andrew's catch, pre-existing).** `opal_aggregate_aua` was composed on the EXCLUDING basis
   (`:931-932`, 49F(model+non_model)+INF(model)) while `non_model_aua` was a FULL firm-sum (`:929`).
   TWO BASES IN ONE ARTIFACT -> the FE, which derives the non-model band as (total-model), inherited a
   hole == inflection's non_model on **421/421 dates** ($64.5M frontier .. $203.2M max, median $163.1M).
   **NOT a revamp regression** -- DT proved legacy fails 429/429 identically; the revamp faithfully
   reproduced a long-standing defect.
2. **PARTIAL ROWS -- I INTRODUCED THIS.** Rebasing non_model to 49F-only left it POPULATED on the 6 gap
   dates beside a None total. Pre-fix those rows were cleanly all-None; my rebase un-nulled one column.
3. **MY OWN GATE WAS BLIND TO (2).** The identity assertion only runs where every term is present, so it
   structurally SKIPPED the partial rows -- it would have reported PASS on a defect it could not see. DT
   caught what my instrument could not. Fixed with an all-or-nothing rule + a partial-row RED clause.
4. **FALSE DIP -- caught while FREEZING, before signalling stable.** `by_model` summed firms as
   `(v49 or 0) + (vinf or 0)`, emitting None only when BOTH legs were missing -> an ABSENT firm leg was
   COALESCED TO ZERO, so the global per-model series silently became 49F-ONLY while `model_aua` (via
   `_sum2`) correctly went None. A2 aum-timeseries therefore PUBLISHED a fabricated collapse:
   07-10 $1,502,933,710.69 -> **07-13 $1,395,691,979.72 (-$107.2M / -7.1%)** -> 07-16 $1,502,669,170.46;
   also 05-21 -$57.6M. Absence was being RENDERED AS A COLLAPSE -- the mirror of the imputation we had
   just refused to restore (there the code would invent a VALUE; here it invented a ZERO).

## Andrew-direct ruling (recorded verbatim, broadcast same-turn)
Presented the A/B basis choice with measured consequences; Andrew selected **"EXCLUDE consistently"** --
keep the total at $1.813B, redefine non-model to 49F-only so the two agree, Inflection non-model becomes a
separate audit field. Broadcast to CTO/CVO/DT/DE. **The broadcast was load-bearing: CVO was mid-build on a
Layer-3 clause encoding the OPPOSITE (A) basis and HALTED it before ship** -- that clause would have
RED-flagged a correct artifact.

## The gate (4 clauses, all MUTANT-PROVEN -- fail-closed, refuses to emit)
(i) headline identity `opal_aggregate == model + non_model`; (ii) leg pins (non_model == 49F's,
inflection_non_model_aua == INF's -- pins BOTH recurrence directions); (iii) row coherence (no partial
rows -- closes the skip-hole in (i)); (iv) band/total agreement, `sum(by_model cohort=='model') ==
model_aua` AND **absence must agree** (the false-dip detector; absence limb EXACT, value limb 5c
rounding-order tolerance set from measured cause after it fired on genuine 1-cent rounding and correctly
refused to emit).
Mutants: shipped-defect -> RED 421; 2b-leg dropped -> RED 427; +$0.02 on ONE date -> RED; one partial row
restored -> RED on two independent clauses. Control PASS. Gate is DISCRIMINATING, not decorative.

## Dispositions I owned (both overturned another agent's read, on mechanism)
- **SMA is NOT omitted (DE's claim refuted, DE re-derived and retracted).** 49F model_aua == sum(5 core)
  EXACTLY; custody - model_aua == non_model EXACTLY; SMA ($23,354,316.22) is in custody but not model_aua
  => a residual component INSIDE non_model, counted exactly ONCE in the Non-Model band. DE's step assumed
  SMA would sit ON TOP of 274.67M.
- **3 INF dates are HONEST (CVO's "restore 05-21" overturned, CVO re-verified and retracted).** eclipse
  model partition ABSENT on 05-21/06-01/07-01 while orion custody PRESENT; bracketing days present. The
  legacy's value is an IMPUTATION, not a measurement -- restoring would FABRICATE. Rule 22: mechanism
  beats "legacy has a value".
- **REFUSED to null orion's REAL custody to force a gate green** -- nulling a measurement to satisfy an
  instrument is fabricating ABSENCE. Deliberate asymmetry: null the underivable (global cross-section),
  KEEP the measured (inflection custody), exempt via a lineage-verified marker.

## New finding (upstream, not a producer defect)
**07-13/14/15 = a bounded 3-day INFLECTION FEED OUTAGE across BOTH feeds** (orion missing exactly those 3
weekdays out of 75 swept; eclipse too). Mon/Tue/Wed. **NEVER#1 resolved BEFORE saying it**: canonical
`lib/trading_calendar.py` returns is_trading_day=True for all three (2026 NYSE holidays contain no July
date but 07-03, the observed July-4, which the calendar correctly excludes); Schwab reported on all three
while nobody reported on 07-03 -- the opposite signature. Orion's latest partition is 2026-07-21 so the
feed is CURRENT: a historical hole, NOT a live outage. Shim-vs-canonical swept 628 days: **0 divergences**
(retires a risk my own 9d21de589 had flagged). Triage routed to CTO post-gate.

## Ledger work (all LEDGER-ONLY -- zero S3 writes, freeze held)
`_shape_extras` declares `inflection_non_model_aua` published-only (DECLARED, not harness-exempted: it is
numeric DATA and exempting data is how a real extra hides). Then all 8 global `non_model_history_windows`
+ `non_model_latest` RE-BASED. **DT's challenge -- "a band fitted to the observed data can only ever
pass" -- is the sharpest point of the night and I did not paste their ranges.** Each band is DERIVED as
(that window's prior D-2 band) + (measured inflection-share range A = the ruling's arithmetic), then the
OBSERVED range is TESTED against the envelope. A+B==observed EXACT at every in-window date (41/41 ... 6/6)
and observed fell INSIDE all nine -- **a check that could have failed**. Flagged the 2026-07-01 window as
the THINNEST (n=6) rather than presenting all eight as equally solid; CTO ruled CVO's source re-derive
carries its correctness. Also DEMOTED my own earlier standalone broad-band entry to a note -- a single
[-56,-10] band would have matched everything in range and MASKED DT's per-window precision (the
tuned-to-pass failure one level up).

## Legacy raw-consumer trace (CTO's open item) -- CLOSED
There IS a raw consumer (`ModelPortfolios.tsx:872` `lastNonNull(perFirmMdpfData.non_model_aua)`, `:935`
per-date map) -- so "the FE only derives the band" was INCOMPLETE. BUT every raw read is gated by
`:863 isPerFirm = effectiveFirmId !== 'global'`, so it NEVER reads the global artifact. => CTO's ruling
holds (re-land supersedes, no parallel legacy data-fix), AND it independently confirms zero-FE-change for
the B rebase on a path DE had not checked. **Guardrail banked:** per-firm non_model IS display-load-
bearing, so extending basis-B to the per-firm artifacts would be an FE-visible change, not a repoint.

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-grep | legacy raw-consumer trace (portal/src) | PASS | 17 matches/2 files, 403 scanned; systems-context surfaced the ModelPortfolios owner tools |
| DT mdpf_parity_check --consistency @f64797340 | 4 runs across vintages | PASS (final) | 49f 427/427, global PASS, CROSSFIRM regime-B; drove the marker + _shape_extras + band re-base |
| safe-commit (surface-check + risk-reflex) | 7 commits | PASS | reflex CLEAN each |
| commit-gate (py_compile + ruff) | every .py edit | PASS | caught the stale meta-key KeyError early |
| comp-system-gate | 3 ledger commits | OVERRIDE (audited) | doc-only, data-neutral, frozen ETags untouched |
| lib/trading_calendar (canonical) + shim sweep | NEVER#1 resolution | PASS | 628 days, 0 divergences; 07-03 positive control |
**What worked:** the mutant tests -- every clause was proven able to FAIL before any PASS was recorded.
**What failed:** nothing silently. **Gap found:** the comp-system-gate reads its override ONLY from `-m`
argv, never the `-F` file, while the CLAUDE.md Git gate DENIES `-m` carrying `$(` -- and the override must
be its OWN-LINE `-m` paragraph (sed `^` anchor). Resolved by splitting the commit; banked for the fabric.

## Files Modified
see commit messages: **4ec837e72** (basis-B + gate), **943d0a2bb** (row-coherence + honest-None marker),
**78f25db36** (by_model absent-as-zero + clause iv), plus ledger **b8224324e** / **842d0f816** /
**82e1f9d04**. All authored 0.4.0_DS_ClientPlatform, pushed origin/CLOUD.

## Blockers
None. Re-publish HELD by design (CTO's gate). Remaining legs are OTHERS' by design -- CVO's independent
re-derive is the correctness signal and I structurally cannot run it for them.

## Current State (zero-context handoff)
- **FROZEN COHERENT-9 (signalled; do NOT move without announcing):** 49f `aa5c5b85066109c9bdb557e51b0d8ffd`
  / inflection `cec5a0d6fe749aae77735f9297edbb71` / global `c27e1f370f9c08de6489cb11bf885e13` /
  A4 `8a195549c6f80257f188d91a6423d547` / A1 `529b7c211b268f6cb72fa4a92941727d` /
  A2 `f2c034760b44c4bd7338be0fd6c75c58` / account_distribution x3 unchanged
  (`865919f2be40...` / `afb964c4d67f...` / `b946d8364ca3...`).
- **LIVE-READ green pinned to those ETags:** identity 421/421 PASS, partial rows 0, band/absence 0,
  A1 self-identity TRUE, A4 pin TRUE (DE's 2026-01-16 boundary-step risk closed), A2 gap dates
  [None,None,None].
- **Basis B:** global non_model_aua = 49F-only (274,667,920.44 @07-20); inflection non-model
  (64,478,099.34) in `inflection_non_model_aua`, NEVER summed into the headline.
- **Producer:** `dim_mdpf_aggregate_aua_timeseries.py` -- 4-clause fail-closed `_assert_global_composition`
  + `_honest_none_marker` (meta.honest_none with by_date REASON map + feed prefixes; two classes:
  model_partition_absent vs all_feeds_absent).
- **Verification state:** DT consistency GREEN rc=0 + marker wired @41cbd7220 (11 mutants) + A2 dip
  confirmed gone; CVO marker lineage-verify ALL OK (both classes + positive control run separately);
  CVO Layer-3 re-running on the frozen vintage. CTO gates on CVO green + DT parity + his own
  HeadObject-confirm-all-legs-cite-the-same-set.
- **Live serve is LEGACY** (router rolled back before this work began). I have published NOTHING.

## Next Steps
- **[3.0.0_SA_CVO]** Layer-3 re-derive + E5 absence-agreement limb on `c27e1f37...` (the correctness leg).
- **[0.2.0_DT_PortfolioAnalytics]** re-run parity on @82e1f9d04 (band re-base) -> NAMED_DELTA_PASS.
- **[1.0.0_SA_CTO]** gate on all-legs-same-ETag-set; then FE-first re-land + fresh co-sign.
- **[0.4.0_DE_ClientPlatform]** 6-cell render-check + duplicate-key gate on the frozen set; the 2x
  (year-less monthly x-axis key collision over Global's 21-month window) is FE-only, held for CTO GO.
- **[me]** HOLD the freeze; turn any finding same-turn. Open: 3-day inflection outage backfill triage
  (CTO routes post-gate). Reachable, event-driven (Monitor bm9586ict). No crons.
