# ADVI_PRICES -- Gold Rebuild Marathon: Two-Sided Injection + Performance Optimization -- 0.6.0_AE_PartnerETL

**Date:** 2026-03-30
**Start Time:** 10:00 AM ET
**End Time:** 1:10 AM ET (2026-03-31)

## Objective

Execute full gold rebuilds to validate DS fixes: realized sell injection, synthetic buy injection, canonical prices fix, blank name filter, par-valued instrument pricing, and matured bond exclusion. Iteratively deploy and test 8+ versions of 02_build_positions_cube.py. Optimize gold pipeline runtime from 57 min to ~20 min.

---

## Deployment Sequence

| Run | Commit | Fix | Result |
|-----|--------|-----|--------|
| v1 (sell only) | 65612b84 | Realized sell injection only (buy injection not yet committed) | Gold $1,276M, gap -$319M (-20%), gross error $380M |
| v2 (sell+buy) | 9971820d | Two-sided injection: sells + buys | Gold $1,484M, gap -$111M (-7%), gross error $154M |
| v3 | 2c302e9c | CASH $1.00, money market override, POLEN/OPAL alias | CANCELLED (EC2 shutdown race) |
| v4 | 42439b66 | 56 ticker overrides, dot-ticker fix | CRASHED: `AttributeError: 'NoneType' object has no attribute 'upper'` in `_force_cash_price` |
| v5 | 77a7ccfb | Null guard fix | Gold $1,771M, gap +$185M (+11.6%), gross error $226M -- overshoot explosion |
| v6 | b695e7bc | Buy injection switched to canonical_prices | Gold $1,600M, gap +$14M (+0.9%), gross error $69M |
| v7 | 3ba357c9 | Blank name filter + par-valued pricing | Gold $1,595M, gap +$9.4M (+0.6%), gross error $64M |
| v8 | c90de842 | Matured bond exclusion | **Gold $1,591M, gap +$4.9M (+0.31%), gross error $62M** |

---

## Performance Optimization

| Phase | Before (v1) | After (v8) | Fix |
|-------|-------------|------------|-----|
| Expansion (300K pairs) | ~15 min (single-threaded) | ~2 min | ProcessPoolExecutor 60 workers (395a23b0) |
| strftime partition | ~10-15 min (300M row element-wise) | seconds | Group by datetime64, strftime on 1500 unique dates (465aac76) |
| S3 upload | ~30 min (sequential boto3 put_object) | ~30s | ThreadPoolExecutor 64 threads (f41212aa) + aws s3 sync 100 concurrency |
| Pre-2020 partitions | 14K empty parquets written | Skipped | MIN_OUTPUT_DATE=2020-01-01 (395a23b0) |
| Batch loop | 12 batches x full groupby | Single pass | Batch loop deleted, one vectorized groupby (f41212aa) |
| Vectorized injection | Row-by-row Python loops | C-level pandas | set ops, str.contains, vectorized DataFrame ops (5040f359) |
| Diff recompute | 2x full groupby+diff | Carry signed_units | compute_unit_events returns signed_units directly (597ea654) |
| Auto-scale workers | Hardcoded 32 | max(cpu_count-4, 4) = 60 on c6i.16xlarge | All gold scripts auto-scale (dbcaae70) |
| **Total 02 runtime** | **~57 min** | **~20 min** | **65% reduction** |

Sequential phases (transaction loading, sell/buy injection) still take ~12 min. DS vectorization helped but these remain the bottleneck for further optimization.

---

## Infrastructure Changes

1. **run-gold-layer.sh: Disabled pending-trigger re-run** -- was causing unwanted double-runs during QA gold rebuilds. Commented out the S3 trigger-pending.json check and incremental re-run block.

2. **run-gold-layer.sh: Removed auto-shutdown** -- `shutdown -h now` was killing EC2 mid-SSM when runs were cancelled and re-dispatched. Replaced with log message. Instance stays up for SSM commands.

3. **S3 upload strategy: aws s3 sync at 100 concurrency** -- replaced sequential boto3 put_object (30+ min for 14K partitions) with `aws configure set default.s3.max_concurrent_requests 100` + `aws s3 sync`.

---

## Operational Issues Encountered

| Issue | Root Cause | Resolution |
|-------|-----------|------------|
| v3 EC2 shutdown mid-run | Cancelled SSM triggered runner's `shutdown -h now` | Removed auto-shutdown from runner |
| v4 crash: NoneType in _force_cash_price | Unrealized report has None asset_name rows | DS added null guard (77a7ccfb) |
| v5 overshoot explosion ($205M) | Buy injection used Yahoo historical_prices, gold uses canonical_prices | DS switched to canonical_prices (b695e7bc) |
| Systemd service not starting on boot | Service in failed state from prior SIGTERM | Dispatched SSM directly instead of relying on systemd |
| 02 appeared hung at 35 min | EC2 stopped by old runner's shutdown (race condition) | Restarted EC2, re-dispatched SSM |
| GLDRST scripts accidentally pushed to S3 | Synced ALL gold scripts instead of just 02 per DS instructions | No rollback needed -- changes were safe refactors (DS confirmed) |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Synced all gold scripts to S3 on first run | Should have followed DS instructions to upload only 02. GLDRST S3_BUCKET changes went to EC2 unintentionally but ran successfully. |
| Disabled pending-trigger and auto-shutdown | Operational necessity for iterative testing. Must re-enable for production nightly runs. |
| Used aws s3 sync instead of boto3 uploads | 100x concurrency vs sequential -- 30 min to 30 seconds |
| Let v6 run finish before deploying perf fixes | Needed the canonical prices fix results before testing performance improvements |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/ec2/bd-gold-layer-runner/run-gold-layer.sh` | Disabled pending-trigger re-run + removed auto-shutdown | Yes (in working tree, tracked) |
| `.tmp_diag_injection.py` | Diagnostic: buy injection distribution analysis | No -- temp file, not for commit |

---

## Key Metrics Progression

| Metric | Start of Session | End of Session | Delta |
|--------|-----------------|----------------|-------|
| Net gap | -$319M (-20%) | **+$4.9M (+0.31%)** | -$324M |
| Gross absolute error | $380M | **$62M** | -$318M (-84%) |
| Accounts >50% off | 973 | **115** | -858 (-88%) |
| Within 10% of silver | 28.7% | **92.1%** | +63pp |
| Gold AUA | $1,276M | **$1,591M** | +$315M |
| Pipeline runtime | 57 min | **20 min** | -65% |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

Eight gold rebuild iterations deployed and tested. Net AUA gap reduced from -$319M (-20%) to +$4.9M (+0.31%). Pipeline runtime cut from 57 min to 20 min through parallelization, vectorization, and S3 upload optimization. EC2 stopped. All DS commits (sell/buy injection, canonical prices, blank names, par-valued, matured bonds, performance fixes) validated on EC2. Run-gold-layer.sh modified to disable auto-shutdown and pending-trigger re-run for iterative testing.

Yang model.pkl files investigated for potential rotation buy allocation proxy. Holdings weights (per-model target allocations) are viable but require account-to-model inference (BD doesn't populate strategy field). Flagged for next session.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Yang model weight-based buy injection** -- replace residual back-solve with model portfolio weights for rotation accounts. Requires account-to-model fingerprint matching. Design + implementation task for next session.
2. **[0.6.0_AE_PartnerETL] Re-enable auto-shutdown for production** -- current runner stays up indefinitely. Need to add shutdown back before nightly runs resume, or gate it behind an env var (e.g., `GOLD_KEEP_ALIVE=1` for QA, absent for production).
3. **[0.6.0_AE_PartnerETL] Full gold pipeline run (all scripts 00-10)** -- the iterative runs only did 02+05+05e. Need a complete pipeline run with all downstream scripts (05b, 05c, 05d, 06, 06b, 07, 08b, 08, 09, 10) to propagate the fixes to portal artifacts.
4. **[0.4.0_DS_ClientPlatform] Further 02 sequential phase optimization** -- transaction loading + injection still takes ~12 min. Parallelizing the buy injection back-solve (per-account) could cut this to ~3-4 min.
5. **[0.6.0_AE_PartnerETL] Commit and push all DS commits to origin/CLOUD** -- 7+ DS commits on CLOUD not yet pushed.

**Do NOT:**
- Re-enable `shutdown -h now` in runner without adding a `GOLD_KEEP_ALIVE` guard
- Run the nightly gold trigger with the current runner (it won't auto-shutdown, EC2 will run indefinitely)
- Assume 05f quality tiers are validated (SSM timed out on first run, re-run needed)
