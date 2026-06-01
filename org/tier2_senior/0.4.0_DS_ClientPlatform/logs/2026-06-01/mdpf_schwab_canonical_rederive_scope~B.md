# MDPF 49F non_model — Black-Diamond→Schwab canonical re-derive: SCOPE (DS~B, 2026-06-01)
SCOPE-FIRST per COO (162938Z) + CTO oversight. Andrew-direct canonical: 1b plug = Schwab_total − SmartX_model(1a) − SmartX_SMA(1c); total=1a+1b+1c, all DISJOINT. NO backfill until Andrew sees scope. Reconcile target: DE brief 081be4a0e. CVO sole verify-writer.

## The 5/18 seam = ONE event (disentangled per COO ask)
The −$172-180M 49F non_model step at 5/18 is the **v0.8→v0.9 basis change, which IS the "Black Diamond→Schwab" change** — not two separate things. Per WS-E header: v0.9 (Andrew Mandate Change 3, 5/20) "SUPERSEDES v0.7 (full-BD-book certified_aua) AND v0.8 (SMA-inclusive 1b); it restores the Schwab basis." Mechanically: pre-5/18 counted the FULL BD certified_aua book (all custodians); v0.9 restricts to Schwab-custodied accounts. The ~$140-180M = the non-Schwab-custodied accounts. (The SMA +$25M reclass is a separate small overlay at the same date.)

## EXACT-vs-ESTIMATE determination (CTO's hard dependency) — EMPIRICALLY VALIDATED
The Schwab restriction = certified_aua (liability-excluded) ∩ Schwab-custodied, where custodian comes from an account_id→billing_account_custodian crosswalk built from the FULL silver/fees history (stable per account, .001 audit: 0 conflicts).
- **Source availability:** BD `silver/allocations` (per-account: account_id, account_market_value, account_type) = 91 partitions, **earliest 2026-01-16**. BD `silver/fees` (crosswalk) = back to **2020** (1,869 partitions, 10,526 accounts: 7793 Schwab / 1613 Fidelity IWS / 675 ByAll / 445 DST).
- **EMPIRICAL PROOF (2026-04-15, full crosswalk):** full-book(liab-excl)=$1,699,280,891; **Schwab-restricted=$1,556,208,375**; non-Schwab-known=$137.2M; unmatched=17 accts (~$5.9M, matches WS-E's known ~$7.3M bucket). => the Schwab-restricted partner_custody_total is computable EXACTLY for a historical date, identical to the v0.9 method.

**Determination:**
- **2026-01-16 → 5/17: EXACT-re-derivable.** partner_custody_total (the dominant ~$140-180M correction) is EXACT (per-account silver/allocations + stable crosswalk). 1b = custody(EXACT) − 1a − 1c; the only estimate element is the small **1c (~$25M) bandaid term** (weekly-interp; no production historical SMA). So re-derived 1b is exact-in-custody with a ~$25M estimate sub-component — and that 1c term should be LABELED estimate per CTO (Andrew reads this trend).
- **pre-2026-01-16 (2024-11 → 1/15): NOT exact-re-derivable** — no silver/allocations that far back. ESTIMATE/FLAG only (annotate as Black-Diamond-era, non-canonical).

## Firm-scope
**49F-specific.** The Schwab restriction is Cohort 1 = 49financial. Inflection (2a/2b, eclipse/orion source) is UNAFFECTED. Global = aggregate → global non_model shifts as a CONSEQUENCE of the 49F re-derive (re-run aggregator + rollup after re-emit).

## Mechanism (for the re-derive, if GO)
Per historical date 1/16-5/17: compute_partner_custody_total(date, full_crosswalk) [WS-E logic] → 1b = custody − existing_1a − 1c. NOTE: WS-E normally reads WS-B model_aua_positions (feeder exists only 5/18+), so the historical re-derive uses 1a from the existing historical series (backfill), not a live WS-B run — a backfill-style recompute. Then re-emit 49F non_model partitions → re-run mdpf_aggregate_aua + build_aggregate_aua_timeseries rollup. Full Rule 13 cycle + ds-commit-gate. DE serving-verifies post-emit.

## RECOMMENDATION
**Re-derive 1/16-5/17 onto the Schwab canonical (option b smooth — CTO-endorsed, methodologically right): EXACT for custody; LABEL the ~$25M 1c term as estimate.** Annotate the pre-1/16 region as Black-Diamond-era non-canonical (not re-derivable; no silver/allocations). This makes Andrew's trend continuous + canonical from 1/16, with the residual pre-1/16 seam self-described. Surface the exact(custody)/estimate(1c-term, pre-1/16) split to CTO+Andrew BEFORE emit per CTO. Awaiting GO; no backfill executed.
