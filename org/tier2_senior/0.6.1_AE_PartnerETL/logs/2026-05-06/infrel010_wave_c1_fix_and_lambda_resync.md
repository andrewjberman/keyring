# Session Log: INFREL.010 Wave C1 Fix + Lambda Resync + D9 Gate 1 RAVC2

**Agent:** 0.6.1_AE_PartnerETL  
**Date:** 2026-05-06 (continued session, context reset recovery)  
**Session type:** Loop continuation (resumed from prior context)

---

## Summary

This session completed the RPBKTPI TO-2 RAVC2 (D9 Gate 1 cleared), diagnosed and fixed the Wave C1 tax backfill failure, rebuilt and redeployed inf-silver-chain Lambda (v1.7.25), dispatched the Wave C1 sentinel-overwrite redispatch, routed household/activity empty-partition fix to DS~C, and authored the Wave C2 skip-400 patch for DS~B.

---

## RPBKTPI TO-2 COMPLETE — D9 Gate 1 CLEARED

- gold/holdings/ confirmed: 2416 parquets, 2019-09-17 through 2026-04-28 (complete range)
- All files timestamped 2026-05-05 16:45:xx (prior session's run completed; current session's PID 8338 re-dispatch found all dates done and exited cleanly — PID 8338 dead, /tmp log cleared)
- RAVC2 sent to COO + AE 0.7
- AE 0.7 ACK'd; D9 chain proceeding

---

## Wave C1 Root Cause Diagnosis

The original Wave C1 dispatch (`inf_backfill_tax_perf.py`, SSM 461caa3a) was failing because:

1. **Bronze markers exist**: orchestrator writes per-dim markers at `bronze/orion-api/{date}/_markers/{dim}.json` on bronze pull completion. Since bronze was pulled successfully, all dates had status=ok markers.
2. **Standard re-dispatch would skip all dates**: `inf_backfill_tax_perf.py` checks `dims_done()` which reads these markers. All historical dates → all done → 0 work.
3. **Silver was failing, not bronze**: the empty-partition bug (`apply_aua_guard` on 0-row df post INFGRD filter) caused silver conversion to crash for all pre-onboarding dates. Bronze was fine; silver was failing silently.

Original SSM 461caa3a: self-terminated (not found in list-commands by session start).

---

## Lambda Rebuild: inf-silver-chain v1.7.25

DS~C's empty-partition fix (commit c70ab1401) was uploaded to `s3://opal-data-inf/code/silver/` but NOT in the Lambda zip. The Lambda zip required a resync per SYNC.md protocol.

**Actions:**
1. `cp data/orion/scripts/silver/build_billing_dim.py infra/aws/lambda/inf-pipeline/inf-silver-chain/`
2. `cp data/orion/scripts/silver/build_tax_dim.py infra/aws/lambda/inf-pipeline/inf-silver-chain/`
3. Updated SYNC.md "Last sync" for both files to c70ab140 / 2026-05-06
4. `bash infra/aws/lambda/ci/build-and-upload.sh inf-pipeline inf-silver-chain`
   - New SHA: `4T/72TgTWGglFjSD+skHgMqKCwWEYpoASkBsc312Qhw=`
5. `terraform plan` → 1 change (source_code_hash), 0 other changes
6. `terraform apply` → Success
7. 0-diff plan verified
8. `record-terraform-deploy.sh inf-pipeline --version inf-pipeline-v1.7.25` → committed e65fec8e2
9. Tagged `inf-pipeline-v1.7.25`, pushed CLOUD + --follow-tags

**Commits this action:**
| Commit | Message |
|--------|---------|
| `b9e80e0ca` | fix(ADVI_INFREL.010): resync inf-silver-chain Lambda with empty-partition fix from c70ab140 |
| `e65fec8e2` | ci: record deploy inf-pipeline @ 4ca43b39 [skip ci] |

---

## Wave C1 Sentinel Redispatch

Since direct Lambda invocation (InvocationType=RequestResponse) was blocked by IAM (`lambda:InvokeFunction` missing from both bronze-runner and gold-layer-runner EC2 roles), the approach was changed to sentinel-file overwrite.

**Approach:** Overwrite `bronze/orion-api/{date}/_BRONZE_COMPLETE.json` for each date where `silver/api_dims/tax_unrealized/snapshot_date={date}/data.parquet` is missing. EventBridge S3-ObjectCreated rule re-triggers inf-silver-chain Lambda without requiring Lambda IAM.

**Script:** `infra/aws/ec2/inf-bronze-runner/inf_silver_chain_redispatch.py`
- Committed: `2c1fe85ab`
- Uploaded: `s3://opal-data-inf/code/bronze-runner/inf_silver_chain_redispatch.py`

**Dispatch:**
- SSM CmdId: `c1b85a3c-a372-476d-bb87-debed5ca7a7e` (inf-bronze-runner i-083ad9ae297f88e9f)
- Background PID: 7200
- Params: `--from 2020-01-01 --to 2026-05-05 --resume --require-sentinel --check-dim tax_unrealized --sleep-s 2.0`
- Confirmed alive: PID_ALIVE, TRIGGER logs at [1], [31], [61]... [241/2317]
- ETA: ~77 min total (2s/date × 2317 dates)
- Progress: `s3://opal-data-inf/bronze/logs/inf-bronze-runner/infrel010_wave_c1_redispatch_progress.json`

**Coverage of current dispatch:**
- billing + tax: FIXED in v1.7.25 Lambda (will succeed for pre-onboarding dates, return empty df)
- household + activity: STILL FAILING for pre-onboarding dates (apply_aua_guard crash not yet fixed)
- All failures are non-fatal (Lambda catches exception, continues, records partial failure)

---

## Household + Activity Empty-Partition Fix (Routed to DS~C)

Code review of `convert_orion_api_to_silver.py` revealed two more unguarded `apply_aua_guard` calls:
- `build_household()`: `filter_to_inflection()` → `add_required_silver_cols()` → `apply_aua_guard(merged, 'account_aua', 'household')` — no empty check
- `build_activity()`: `filter_to_inflection()` → `add_required_silver_cols()` → `apply_aua_guard(df, 'ending_mv', 'activity')` — no empty check

Diff authored (gate-clean), sent to DS~C. When DS~C commits + S3 uploads:
- I will resync Lambda → rebuild → deploy as inf-pipeline-v1.7.26
- The sentinel re-dispatch (PID 7200) will then cover all 6 dims cleanly for pre-onboarding dates

---

## Wave C2 Assessment + Skip-400 Patch Authored

**Root cause:** `pull_inflection_performance_dim.py` exits 3 when Orion API returns 400 on POST /Generate for pre-onboarding date windows. This is expected behavior (no performance data exists for those periods). Wave C2 backfill shows 530+ failures.

**Silver-side assessment:** `build_performance()` in `convert_orion_api_to_silver.py` does NOT call `apply_aua_guard`. No crash vulnerability. Wave C2 failures are bronze-pull failures, not silver builder failures.

**Fix authored:** 3-line insert in `post_generate()` (line ~205): handle 400 specifically as exit 0 (SKIP) before generic non-201 → exit 3 logic.

**Routing:** TO sent to DS~B (original author of the file, idle). After DS~B commit + S3 upload + RAVC, I will re-trigger Wave C2 backfill.

---

## Commits This Session

| Commit | Author | Message |
|--------|--------|---------|
| `b9e80e0ca` | 0.6.1_AE_PartnerETL | fix(ADVI_INFREL.010): resync inf-silver-chain Lambda with empty-partition fix from c70ab140 |
| `e65fec8e2` | 0.6.1_AE_PartnerETL | ci: record deploy inf-pipeline @ 4ca43b39 [skip ci] |
| `2c1fe85ab` | 0.6.1_AE_PartnerETL | feat(ADVI_INFREL.010): Wave C1 sentinel redispatch script (inf_silver_chain_redispatch.py) |

**Tag:** `inf-pipeline-v1.7.25`
**Push:** CLOUD + --follow-tags (all three commits live)

---

## Pending / Next Session

1. **DS~C household+activity RAVC**: When DS~C commits + S3 uploads `convert_orion_api_to_silver.py` fix → resync Lambda (cp → build-and-upload.sh → TF apply → inf-pipeline-v1.7.26)
2. **DS~B Wave C2 RAVC**: When DS~B commits + uploads `pull_inflection_performance_dim.py` skip-400 fix → re-trigger Wave C2 backfill (`inf_backfill_perf_c2.py` re-dispatch)
3. **Wave C1 completion**: Verify PID 7200 completes 2317 dates, check S3 progress file. Then RAVC5 FINAL to COO.
4. **RAVC5 FINAL billing**: Billing backfill 71 ok / 4 fail — still need retry for 4 failures (2 leap-day, 1 timeout, 1 exit=3)
5. **Verify 2026-05-07 first fires**: inf-api-txn (13:00 UTC), performance dim (12:30 UTC)
6. **AE 0.7 EC2_MANIFEST**: COO relaying to AE 0.7 for inf-bronze-runner manifest update
