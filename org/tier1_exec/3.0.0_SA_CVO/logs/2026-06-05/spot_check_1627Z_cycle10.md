# /spot-check cycle 10 — yield-curve clobber-fix VERIFIED + GLDINC build-PRD (draft) noted

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO · 2026-06-05 ~1627Z · checkpoint c3242ac27 -> 173f87bd8

## Delta (8 non-CVO commits) — yield-curve fix + GLDINC build-PRD
- AE yield-curve clobber-fix (38c45d108 guard / 1c8f43c15 IAM / 4d62826e0 deploy / 173f87bd8 1Y-restored).
- CTO ADHC_GLDINC build-PRD v0.1->v0.1.1 (8c9acb101/2663ca6bb) + AE build-lead review (10fb964fa). COO drive cycle-10.

## VERIFY (data-delivery, read-the-artifact) — yield_curve_fred.json: PASS
Served `s3://opal-data-portal-v2/json/macro/yield_curve_fred.json`:
- EXISTS 674KB. FRESH LastModified 2026-06-05T15:50:03Z (~37min, matches the deploy+run window). NOT-FROZEN (freshly merge-written, 1Y restored).
- COMPLETE: all 10 CONFIGURED tenors present (1M/3M/1Y/2Y/3Y/5Y/7Y/10Y/20Y/30Y) incl the restored **1Y**. `preserved_tenors` key = the merge-preserve fix mechanism live.
- SHARP-TEST: 6M appeared missing vs a standard curve — but verified against producer config (ingest_yield_curve_fred.py:40-52): DGS6MO is NOT an ingested series. 6M absent = BY DESIGN, not a clobber victim. No gap. (Avoided false-positive by checking producer config before flagging — same discipline as NFRA_COSTRED / current_phase.)
- **Verdict: PASS — "1Y restored" independently confirmed; full configured curve served fresh; merge-preserve guard live.**

## GLDINC build-PRD (8c9acb101 v0.1, 2663ca6bb v0.1.1) — DRAFT, no gate due
DRAFT FOR ANDREW REVIEW (plan not build-auth); production untouched, each cutover separately gated. 5 hard safety gates (dual-run parity oracle N>=5 + phased one-at-a-time + reconcile-correctness DS-owned + checkpoint-primitive-first + cost-model sizing). §4a reconcile-parity carve-out (scoped single-date re-run vs no-ad-hoc gate) = the ONE open Andrew decision. **NOT a ratified PRD -> verify-channel NOVEL-PRD pre-propagate-gate fires when Andrew approves + before build /drive.** Watch for next verify-channel.

## Observation (non-actionable, P3-fyi to AE)
6M (DGS6MO) is omitted from the yield-curve series config — a curve conventionally includes 6M. Pre-existing design (NOT this fix); flagged to AE for judgment, not routed as a finding.

## Verdict
yield-curve VERIFY PASS (independent confirm of AE's deployed fix); GLDINC PRD draft noted (gate pending Andrew). Checkpoint advances.
