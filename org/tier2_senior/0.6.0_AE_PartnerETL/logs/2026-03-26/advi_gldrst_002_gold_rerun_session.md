# ADVI_GLDRST.002 — Full Gold Rerun with Canonical Exclusions + Performance Optimization

**Agent:** 0.6.0_AE_PartnerETL
**Date:** 2026-03-26
**Task Order:** ADVI_GLDRST.002.ae-gold-rerun-canonical-exclusions.md
**Status:** IN PROGRESS — full gold run executing on c6i.16xlarge with ProcessPoolExecutor optimization

---

## Objective

Execute a full gold layer rerun to apply the canonical exclusion unification (lib/exclusions.py) committed on 2026-03-26. Regenerate all downstream parquets and portal artifacts with consistent ghost account exclusion. During execution, discovered and resolved a code bug in 06b and upgraded infrastructure from r6i.xlarge to c6i.16xlarge with ProcessPoolExecutor optimization.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | COO GO received via MCP inbox | `20260326T174818Z` — authorized ADVI_GLDRST.002 |
| 2 | Flipped task order status | `staged` -> `pending` |
| 3 | Verified EC2 instance running | `i-01003b035d2988dfb` (r6i.xlarge at this point) |
| 4 | Verified S3 code sync from prior session | `lib/exclusions.py` on S3 (7,396 bytes, 2026-03-26 12:36) — 6 scripts synced |
| 5 | Confirmed prior SSM cancelled cleanly | `f8853376` — Status: Cancelled |
| 6 | Dispatched full gold run #1 | SSM `c74ab67b` — `./run_gold_layer.sh full` |
| 7 | Run #1 completed (SSM timed out on log upload) | `pipeline-complete.json`: `{"status":"success","mode":"full","timestamp":"2026-03-26T18:54:17Z"}` |
| 8 | Pulled run log from S3 | `s3://opal-data-bd/logs/gold-layer/gold_full_2026-03-26.log` (169.5 KiB) |
| 9 | **BUG FOUND: 06b failed all 2,094 partitions** | `ERROR: name 'ghost_account_ids' is not defined` |
| 10 | Root cause identified | `load_static_tables()` loads `ghost_account_ids` at line 456 but does NOT return it (line 469). `build()` never receives the variable. |
| 11 | Sent bug report to DS via MCP | Delivered `20260326T190519Z` |
| 12 | DS fixed — commit `54d1f988` | Added `ghost_account_ids` to return tuple + unpack in `build()` |
| 13 | Uploaded fixed 06b to S3 | `aws s3 cp` — 41.0 KiB |
| 14 | Dispatched 06b-only rerun | SSM `ee004fe3` on r6i.xlarge |
| 15 | **Decision: upgrade to c6i.16xlarge** | User directive: 128 GB RAM, ad-hoc runs must be fast |
| 16 | Cancelled 06b rerun | `aws ssm cancel-command ee004fe3` |
| 17 | Stopped instance | `aws ec2 stop-instances` |
| 18 | Resized to c6i.16xlarge | `aws ec2 modify-instance-attribute --instance-type c6i.16xlarge` |
| 19 | Started instance | Booted, passed status checks |
| 20 | Expanded EBS volume | `vol-0a29e29786d44bc37`: 8 GB -> 50 GB |
| 21 | Grew partition + filesystem | `growpart` + `resize2fs` — 49 GB total, 44 GB free |
| 22 | Pre-installed all deps | pandas 2.3.3, pyarrow 23.0.1, numpy 2.2.6, boto3 1.42.77 |
| 23 | Pre-synced gold scripts from S3 | 62 .py files confirmed |
| 24 | Sent optimization request to DS via MCP | ProcessPoolExecutor specs for c6i.16xlarge (64 vCPU, 128 GB) |
| 25 | DS delivered optimization — commit `6266040f` | ThreadPoolExecutor -> ProcessPoolExecutor (fork), PROCESS_WORKERS=32, WRITE_WORKERS=64 |
| 26 | Synced optimized scripts to S3 | 11 files uploaded (06b, 05b, run_gold_layer.sh, etc.) |
| 27 | Dispatched full gold run #2 | SSM `cbbc41ed` — `./run_gold_layer.sh full` on c6i.16xlarge |
| 28 | **Currently running** | Scripts 00 (16:01), 01 (16:04) confirmed complete. Run in progress. |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Upgrade r6i.xlarge -> c6i.16xlarge | User directive: ad-hoc runs need 128 GB RAM, 64 vCPU. r6i.xlarge (4 vCPU, 32 GB) too slow for iterative testing — 06b alone takes 40+ minutes. |
| Expand EBS 8 GB -> 50 GB | Root volume was 64% full (2.8 GB free). ProcessPoolExecutor with 32 workers could hit disk limits for temp/log data. |
| Request ProcessPoolExecutor optimization from DS | Python GIL means ThreadPoolExecutor does NOT parallelize CPU-bound pandas work. Only S3 I/O benefits from threading. ProcessPoolExecutor on Linux uses fork (copy-on-write shared memory for static tables). |
| Re-run full gold layer (not just 06b) | Optimization touches 05b and 06b. Full run ensures all artifacts are consistent with the same code version. |
| Kill 06b-only rerun on r6i.xlarge | No point waiting 40+ minutes when we're about to run on 16x the compute. |

---

## Bug Found and Resolved

### 06b ghost_account_ids NameError

**Root cause:** `06b_build_client_mix_timeseries.py` — `load_static_tables()` loads `ghost_account_ids` at line 456 but the return tuple at line 469 does not include it. The `build()` function unpacks 7 values at line 614-615, so `ghost_account_ids` is never assigned in `build()`'s scope. When the ThreadPoolExecutor worker closure references it at line 778, Python raises `NameError`.

**Fix:** Commit `54d1f988` — DS added `ghost_account_ids` to the return tuple and updated the unpack in `build()`.

**Impact:** Run #1 completed all 15 other scripts successfully but 06b failed on all 2,094 partitions. Zero mix_timeseries.json aliases written. Ghost exclusion worked correctly in 05b (4 accounts, $7,334,524 removed) and 12 (193 rows, $7,334,524 removed).

---

## Infrastructure Changes

| Resource | Before | After |
|----------|--------|-------|
| Instance type | r6i.xlarge (4 vCPU, 32 GB) | c6i.16xlarge (64 vCPU, 128 GB) |
| EBS volume | 8 GB (gp3) | 50 GB (gp3) |
| 06b/05b workers | ThreadPoolExecutor, 8 process / 16 write | ProcessPoolExecutor, 32 process / 64 write |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| Task order ADVI_GLDRST.002 | `staged` -> `pending` | No — local only |

---

## Run #1 Results (r6i.xlarge, pre-optimization)

All scripts completed except 06b. Key metrics from `gold_full_2026-03-26.log`:

| Script | Duration (approx) | Key Output |
|--------|-------------------|------------|
| 00 accounts_dimension | ~4 min | 9,878 accounts |
| 01 advisor_assignments | ~4 min | 2,798 relationships, 20 advisors |
| 02 positions_cube | ~8 min | 2,094 date partitions |
| 04 client_dimension | ~1 min | 140 KiB |
| 03 holdings_lots | ~10 min | 384,092 lots |
| 05 client_performance | ~32 min | 57.8 MiB, 2,094 dates |
| 05b account_performance | ~5 min | 62.3 MiB, 4 ghost accounts excluded ($7.3M), 2,094 partitions |
| 06 client_tax_liability | ~1 min | Ghost exclusion: 193 lots removed |
| 06b client_mix_timeseries | FAILED | `name 'ghost_account_ids' is not defined` on all 2,094 partitions |
| 07 nna_by_geography | ~1 min | 61,484 non-NNA exclusions |
| 08b architect_attribution | ~1 min | 20 architects |
| 12 composition_artifacts | ~1 min | Ghost exclusion: 193 rows ($7.3M) removed |
| 08 nna_by_advisor | ~1 min | |
| 09 partner_analytics | ~1 min | |
| 10 advisor_rolling_flows | ~1 min | 96.7 MiB, 20 architects, 155 implementors |

---

## Blockers

None. All dependencies resolved:
- DS code fixes committed (`54d1f988`, `6266040f`)
- c6i.16xlarge running with all deps
- Full gold run #2 in progress

---

## Current State

> **Primary handoff point. Write as if briefing someone with zero prior context.**

**Status:** IN PROGRESS
**Active branch:** `CLOUD`

Full gold run #2 is executing on `i-01003b035d2988dfb` (c6i.16xlarge, 64 vCPU, 128 GB RAM) via SSM command `cbbc41ed-44d8-4858-82c2-c8d415cc82a3`. This run includes both the ghost_account_ids fix (`54d1f988`) and the ProcessPoolExecutor optimization (`6266040f`). Scripts 00 and 01 completed at 16:01 and 16:04 respectively. The run is currently in the middle scripts (02-05 territory). Key deliverables to verify on completion: (1) mix_timeseries.json aliases for 20 advisors, (2) account_performance.parquet with ghost exclusion, (3) composition artifacts with ghost exclusion, (4) pipeline-complete.json with fresh timestamp.

Instance was upgraded from r6i.xlarge to c6i.16xlarge during this session. EBS expanded from 8 GB to 50 GB. These are live infrastructure changes — Terraform does not own the instance type or volume size (it owns IAM, SG, instance profile). The instance type change should be reflected in EC2_MANIFEST.json if this becomes the permanent size.

---

## Next Steps

1. **[0.6.0_AE_PartnerETL] Monitor SSM `cbbc41ed` to completion** — poll status + S3 artifacts
2. **[0.6.0_AE_PartnerETL] Post-run validation per task order:**
   - (a) Cross-validate 05 vs 05b (built-in, should pass within 0.1%)
   - (b) Count mix_timeseries.json aliases (`aws s3 ls --recursive | grep mix_timeseries.json`) — expect 20
   - (c) Spot-check one advisor: book.json summary.total_aua vs architect_leaderboard.json — delta < 0.01%
   - (d) Verify DFAC classification in any composition.json — should appear under "equity"
3. **[0.6.0_AE_PartnerETL] Report completion to COO via `send_message`**
4. **[0.6.0_AE_PartnerETL] Mark task order ADVI_GLDRST.002 as `complete`**
5. **[0.6.0_AE_PartnerETL] Update memory: EC2 gold runner is now c6i.16xlarge with 50 GB EBS**

**Files to touch next:**
- `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_GLDRST.002.ae-gold-rerun-canonical-exclusions.md` — flip to `complete` after validation
- `infra/aws/ec2/EC2_MANIFEST.json` — update instance type if upgrade is permanent

**Do NOT:**
- Re-run the full gold layer again — run #2 includes all fixes
- Resize the instance back to r6i.xlarge — user directive is c6i.16xlarge for ad-hoc
- Modify any gold scripts — all code changes are DS responsibility
