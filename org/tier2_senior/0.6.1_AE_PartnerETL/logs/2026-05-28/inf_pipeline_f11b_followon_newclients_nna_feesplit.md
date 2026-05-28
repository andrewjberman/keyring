# ADVI_INFDEMO F11-B follow-on — new_clients fee-split + NNA Lifetime-Activity/Flows reconciliation

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, DEPLOY
**Agent:** 0.6.1_AE_PartnerETL
**Date:** 2026-05-28
**Assignment:** Andrew-direct (conversational + via 1.0.0_SA_CTO / 0.4.0_DS / 2.0.0_SA_COO / 0.4.2_RD)
**Status at log-write:** HOLDING per Andrew-direct "hold til further advice". Leg-1 LIVE; leg-2 DEFERRED post-demo.

---

## Summary

After the original F11 fee_breakdown PROD ship (this morning), Andrew flagged two issues on the IWM demo surface:
- **A — new_clients flattened:** leaderboard `fee_breakdown.{fee_paying,no_fee}` carried no `new_clients` (entry-level only); 49F reference splits it.
- **B — NNA mismatch:** "Lifetime Activity" NNA != "Flows" NNA under fee-split cohort selection (aggregate reconciled).

Both root-caused, fixed in code (DS-authored), and partially deployed. Leg-1 (leaderboard new_clients fee-split) is LIVE for the demo via CF invalidation; leg-2 (advisor timeseries real fee sub-streams, a Lambda deploy) is deferred post-demo per Andrew. Currently holding all further action per Andrew.

## Issue A — new_clients fee-split (DONE + LIVE)

- Root: `INF_D_00c` `_fee_bucket()` (lines 1206-1219) emitted aua/account_count/client_count/nna/inflows/outflows but NOT `new_clients`; entry-level only (1240). 49F splits it.
- Fix: DS commit **9950a3f2c** (on CLOUD) — new-client household classified `fee_paying` if ANY account fee-earning (billing `is_fee_earning`), else `no_fee`. Additive-only; validated (Peter MAX 198 = 184 + 14; sum-invariant PASS QTD/YTD/MAX).
- Deploy (leg-1): DS regenerated leaderboard.json gold-side (Rule 13); I fired the CF invalidation. **LIVE.**
  - Live artifact: `s3://opal-data-inf/platinum/firm/leaderboard.json` LastModified 2026-05-28T17:39:02Z, 26604B. Peter MAX new_clients 198=184+14 verified.
  - CF invalidation: **I2UXSDO7FFZKPXRW9VXIZS1VQJ** (InProgress at fire) `/api/scoped/advisor-intelligence/*` on EVTSA9VEHNZVH.
  - Rollback: backup `s3://opal-data-inf/platinum/firm/_rollback/leaderboard.json.pre-F11newclients-20260528T173355Z`; git pre-point `ac95741d6`.

## Issue B — NNA Lifetime-Activity vs Flows fee-split (CODE DONE, DEPLOY DEFERRED)

- Root (scope-corrected twice): the advisor "Lifetime Activity" `platinum/advisors/{id}/timeseries.json` is written by the **`inf-portal-advisor-publisher` Lambda** (`lambda_function.py:1174`), NOT gold `INF_D_06/09` (those write per-client/per-account surfaces). The timeseries carried no fee sub-streams, so the FE adapter synthesized the fee-split via a ratio — diverging from the leaderboard's real per-account split. Aggregate reconciled; fee-split did not.
- Fix: DS commit **982394f01** (on CLOUD) — `_build_timeseries` partitions per-account `canonical_nna` by billing `is_fee_earning` (SAME predicate as leaderboard -> reconciles by construction), emits 6 daily keys: `{nna,inflows,outflows}_canonical_{fee_paying,no_fee}`. Additive-only; validated Peter 2194 pts, fee_paying+no_fee==aggregate exact.
- **Field-name verification (AE↔RD, self-verified by reading both sides):**
  - NNA/inflows/outflows: Lambda emits == adapter `AdvisorAnalytics.tsx` reads (`pickNnaCanon/pickInflowsCanon/pickOutflowsCanon`). MATCH -> real split on deploy, zero FE change.
  - **AUA gap:** adapter `pickAua` (line 245) reads `total_aua_fee_paying/_no_fee`, which leg-2 does NOT emit; `hasFeeSplitSeries` auto-true disables the synthetic AUA path -> AUA toggle would go INERT (aggregate).
- **AUA decision (PARKED post-demo):** (a) emit real `total_aua_fee_paying/_no_fee` — FEASIBLE in my Lambda (`perf_ts` carries per-account daily `total_aua` + `account_id` at L863-869; partition by the same fee map as flows); (b) RD per-metric `hasFeeSplitSeries` so AUA stays synthetic-responsive; (c) REJECTED (inert toggle = regression). Lean (a) true-reconciliation if cheap, else (b).
- Deploy (leg-2): a Terraform Lambda deploy (build zip -> S3 -> source-map -> plan -> safe-apply HALTGT -> 0-diff -> tag inf-v -> push --follow-tags -> re-fire Lambda). **DEFERRED post-demo per Andrew** (no time for TF deploy mid-PROD-demo). Deployed Lambda code stale (LastModified 2026-05-13).
  - Rollback: git `982394f01^`; TF-prior / S3-artifact restore of timeseries.json.

## Ownership / lane resolution

- `inf-portal-advisor-publisher` is an inf-pipeline Lambda = my (0.6.1) charter. Legs 1+2 are mine (gold rerun + Lambda TF deploy). DS owns the code; AE owns deploy.
- DS `INF_D_06/09` follow-on TO stood down (COO) — redundant for the advisor surface (my Lambda is self-contained); per-client/account surfaces not fee-split in the demo path (post-demo if ever).

## "Full Group-D run" consideration (OPEN, post-demo)

Andrew raised running a FULL Group-D chain (`CHAIN_GOLD_D`, 21 scripts, dependency-ordered) vs à la carte `INF_D_00c`, to avoid leaving other D-group artifacts (advisor book.json, client summaries, etc.) stale/inconsistent with the new fee-split. The Lambda (timeseries) is NOT in the gold chain — separate TF deploy + re-fires on pipeline-complete. Open question to Andrew: full-chain off current silver vs `--chain full` (pull fresh upstream A/B/C). Parked.

## Adjacent task (separate, DONE)

ETF-retag `firm_concentrations.json` CF invalidation — Andrew reassigned to me; AE~A had already fired `I4HAK7U6Z0JIP3HO1XAGAN08AH` (Completed 17:25Z) before the reroute; my fire `I5FNUWO9RBRKVXY6EGL9HRK2BU` (17:28Z) crossed the stand-down = harmless redundant (same path, post-artifact). No re-fire.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `aws s3api head-object` / `aws s3 cp` + python | Verify regenerated artifacts + new_clients split + sum-invariant + additive-diff | leg-1 leaderboard 17:39Z Peter 198=184+14 verified |
| `git show 982394f01` / `git diff` | Extract exact emitted field names (Lambda) | 6 keys `{nna,inflows,outflows}_canonical_{fee_paying,no_fee}` |
| Grep portal `AdvisorAnalytics.tsx` | Extract adapter-read field names (field-name gate) | NNA/flows MATCH; AUA reads `total_aua_*` (not emitted) -> inert-toggle gap |
| `aws cloudfront create-invalidation` | Fire leg-1 + firm_concentrations invalidations | I2UXSDO7... (leg-1) + I5FNUW... (firm_conc redundant) |
| `aws lambda get-function-configuration` | Confirm deployed Lambda stale | LastModified 2026-05-13 (needs leg-2 deploy) |
| Read Lambda `_build_timeseries` (L857-916) | Assess option-(a) AUA feasibility | `perf_ts` has per-account daily total_aua -> option (a) feasible |

Note: `comp-pipescript deployed` defaults to BD bucket (doesn't scan opal-data-inf); used md5/head-object against the INF bucket directly (same INF-bucket coverage gap as prior sessions).

## Current hold state (per Andrew "hold til further advice")

- Leg-1 LIVE (CF clearing). Leg-2 code committed but NOT deployed (deferred). AUA decision parked. Full-Group-D-run scope question open. No further action until Andrew advises. All rollback anchors retained.
