# Feasibility Brief — ADVI_FEREFI #6 fee-data: what fee history exists per firm + back-attribution feasibility

**Author:** 0.4.0_DS_ClientPlatform
**Date:** 2026-06-03T1406Z
**Context:** PRD-sequenced DS feasibility check (ADVI_FEREFI_PRD.md item 6) — "first task = confirm what fee history actually exists per firm" before the DS build. Proactive prep while awaiting the formal TO (COO 140110Z hold).
**Type:** read-only data trace + grain inspection. No build.

---

## VERDICT: FEASIBLE for both firms. Inflection requires back-attribution (Andrew's directive is exactly the simplification that makes it tractable without per-period billing history — which does not exist).

---

## What the FE actually needs (the target contract)
`AdvisorAnalytics.tsx:235-239` — `hasFeeSplitSeries` is true iff per-period timeseries entries carry ANY of:
- `total_aua_fee_paying` (and implied `total_aua_no_fee`)
- `nna_canonical_fee_paying`
- `inflows_canonical_fee_paying`

When true, the `:458` synthetic branch (`computeSyntheticFeeRatio`, `feeBucket.ts:209`) goes dead and the "approx" label drops. So the DS leg = **emit per-period `*_fee_paying`/`*_no_fee` substreams onto the Lifetime Activity timeseries** the AdvisorAnalytics panel reads.

---

## 49F — substream infra ALREADY EXISTS
- `data/black_diamond/scripts/gold/C_01b.role_aua_backfill.py` + `D_00c.portal_leaderboard.py` already emit `aua_fee_paying` / `aua_no_fee` at the role_aua grain (and `fee_breakdown.{fee_paying,no_fee}` on leaderboard entries).
- **Caveat:** `C_01b` backfill rows use `_SOURCE_TAG='p1b_backfill_equal_split_no_fee_bucket_no_flow_join'` → sets `aua_fee_paying=0, aua_no_fee=aua` for pre-data periods (a backfill approximation, not measured fees).
- **DS work for 49F #6:** likely small — confirm the Lifetime Activity *per-period timeseries* actually surfaces `total_aua_fee_paying`/`_no_fee` (the role_aua grain has it; verify the timeseries roll-up exposes it so `hasFeeSplitSeries` fires). Verify against the SERVED artifact (per `feedback_verify_against_served_artifact_not_partial_proxy`), not just the gold script.

## Inflection — NO per-period fee history exists upstream (this is the core finding)
- **Source:** `silver/api_dims/billing/` ← `build_billing_dim.py` ← `inf-billing-daily/orion_billing_dim.py` ← Orion ExcelReports "Billing Dim" saved query (DB 4698).
- **Row grain (empirically verified on `data/orion/api-recon/billing_dim_spike.csv`, 2899 rows):** **ONE ROW PER ACCOUNT** (max rows/acct = 1). It's a **current/latest billing snapshot**, NOT a per-period timeseries.
  - `Billing Cycle` = Quarterly. `Billing Period End` clusters at quarter-ends: **9/30/2025, 12/31/2025, 3/31/2026** (+ blank). Earliest = **9/30/2025 → confirms the Q3-2025 / July-2025 Inflection fee-data floor**.
- The pull supports `--window {ytd,1y,3y,5y}` (default 3y), but a single pull still returns latest-period-per-account — it does NOT return multi-period history per account. So there is **no measured per-quarter fee classification history** for Inflection.
- Per-account `is_fee_earning` IS available (current): `is_fee_earning = (fee_schedule_name != '0 Fee Schedule Names') AND (fee_amount > 0)` (`build_billing_dim.py:88`).

---

## How to satisfy Andrew's back-attribution directive (the feasible path)
Andrew: *"any account a household holds for which we DO have fee data is marked fee-paying since inception."* This sidesteps the missing per-period history:

1. Take **current per-account `is_fee_earning`** (Inflection billing dim — HAVE IT).
2. Take the **per-period AUA timeseries** per account/household (account_performance / the Lifetime Activity stream — HAVE IT).
3. **Back-attribute:** for each period, classify that period's account AUA as fee-paying if the account is currently fee-earning; roll to household; emit `total_aua_fee_paying`/`total_aua_no_fee` (+ `nna_/inflows_canonical_fee_paying`) per period.

- **Grain (PRD Q4):** per-account earliest → roll to household. Billing dim is per-account, so **per-account `is_fee_earning` rolled to household** is the right grain. Confirmed feasible.
- This is **gold-tier** business logic (classification + back-attribution = judgment) per CLAUDE.md Rule 17 — NOT silver. Correct placement.

---

## Honesty flags (decision-useful, must surface in the brief to Andrew)
1. **Inflection pre-Q3-2025 fee-paying is INFERRED, not measured.** No upstream fee record exists before ~9/30/2025. Back-attribution applies *current* status to all historical periods — defensible per the directive, but it's an inference. Label/tooltip should not imply measured history (cf. the existing `total_fee_amount` "since Jul 2025" tooltip honesty pattern).
2. **Back-attribution cannot detect fee-status CHANGES before Q3-2025** (no data). An account that was no-fee then became fee-paying will read fee-paying for all prior periods. Accepted per Andrew's directive; flag explicitly.
3. **49F backfill periods** (`C_01b` equal-split) are also approximated (aua_fee_paying=0) for pre-data periods — so "real splits, no approx" is true for the *current/recent* window for both firms, with older periods inferred/backfilled. Worth a one-line acceptance note so "no approx" isn't over-claimed.

---

## Open items for the formal TO (not blockers — scoping)
- Confirm the exact per-period timeseries artifact + entry schema the Inflection Lifetime Activity panel reads (so the substreams land where `hasFeeSplitSeries` checks). 49F path uses role_aua → leaderboard/analytics; Inflection's INF_D_0x analytics timeseries needs the same fields added.
- Decide whether the AUA-timeseries periods are quarterly (matches billing cycle) — align substream grain to the chart's interval.
- comp-validate on the new/modified gold script + CVO data verify + served-artifact check before FE consumes (PRD §verify).

Banked as grounding for the incoming ADVI_FEREFI #6 DS TO.
