# GLDOPS/GLDRST Resume Session -- 0.6.0_AE_PartnerETL

**Date:** 2026-04-06
**Projects:** ADVI_GLDOPS, ADVI_GLDRST
**Status:** IN PROGRESS -- second gold incremental running, first run analyzed

---

## Session Summary

Resumed from prior session. Confirmed previous gold run output on S3, extracted GRO/NNA/market growth numbers for DS analysis (GLDOPS.003), verified second gold run in progress, notified DS with full artifact inventory.

---

## 1. Previous Gold Run -- Output Confirmed (COMPLETE)

CloudTrail analysis of bd-gold-layer-runner (i-01003b035d2988dfb):
- Instance auto-stopped at **8:30 AM ET** (watchdog shutdown after run completion)
- Multiple restart attempts between 8:32 AM - 11:57 AM ET
- S3 writes landed between **8:08 AM - 12:17 PM ET** across all gold artifacts
- **12,578 files** written to `s3://opal-data-bd/gold/`

### Artifacts produced (all timestamped 2026-04-06):

| Time (ET) | Artifact | Details |
|---|---|---|
| 08:08 | accounts_dimension_latest.parquet | 718 KB |
| 09:00 | advisors/*/mix*.json | All advisors, daily + timeseries |
| 09:50 | clients/*.json | Client dimension JSONs |
| 10:21 | views/nna_aua_by_geography.parquet | 3.1 MB, 72,845 rows |
| 10:21 | views/architect_attribution.parquet | 93 KB |
| 10:21 | advisors/*/composition.json | All advisors |
| 11:59 | timeseries/client_performance.parquet | 114 MB |
| 11:59 | timeseries/account_performance.parquet | 75 MB |
| 11:59 | timeseries/account_quality_tiers.parquet | 358 KB |
| 12:00 | artifacts/partner_analytics/* | Quarterly snapshots + header metrics |
| 12:00 | validation/aua_certification/*.json | 15 dates (2026-03-11 to 2026-04-02) |
| 12:15 | timeseries/synthetic_positions_index.parquet | 525 KB |
| 12:17 | timeseries/positions_cube/2026-03-29 to 2026-04-02 | 5 daily partitions, ~545 KB each |

---

## 2. GRO / NNA / Market Growth Analysis (COMPLETE)

Extracted from `nna_aua_by_geography.parquet` (data through 2026-04-02):

### YTD 2026
| Metric | Value |
|---|---|
| AUA start (2026-01-01) | $1,349,870,289 |
| AUA end (2026-04-02) | $1,642,927,606 |
| AUA change | +$293,057,317 |
| NNA (cumulative change YTD) | +$106,608,674 |
| Market growth (implied) | +$186,448,643 |
| GRO (AUA growth %) | 21.7% |

### Trailing 12 Month
| Metric | Value |
|---|---|
| AUA start (2025-04-02) | $998,753,482 |
| AUA end (2026-04-02) | $1,642,927,606 |
| NNA (cumulative change) | +$334,681,203 |
| Market growth | +$309,492,921 |
| GRO (AUA growth %) | 64.5% |

### Flow Detail (latest date 2026-04-02)
| Metric | Value |
|---|---|
| Cumulative inflows | $1,839,709,406 |
| Cumulative outflows | $961,560,336 |
| Net NNA | $878,149,070 |
| Relationships | 3,052 |
| Churn column (cum_outflows) | Present -- GLDOPS.003 requirement confirmed |

### Recent Daily GRO Decomposition
| Date | AUA Change | NNA Change | Market Growth |
|---|---|---|---|
| 2026-03-29 | +$21.8M | +$5K | +$21.8M |
| 2026-03-30 | +$6.0M | +$2.5M | +$3.5M |
| 2026-03-31 | +$32.6M | +$2.1M | +$30.5M |
| 2026-04-01 | +$8.5M | -$1.6M | +$10.2M |
| 2026-04-02 | -$1.7M | -$0.9M | -$0.8M |

---

## 3. DS Notification (COMPLETE)

Sent message to `0.4.0_DS_ClientPlatform` at 12:24 PM ET with:
- Full GRO/NNA/market growth numbers (YTD + trailing 12M)
- All S3 artifact paths for their GLDOPS.003 analysis
- Note that a second run is in progress with GLDRST.009 migration

---

## 4. Second Gold Run -- In Progress (MONITORING)

A second gold incremental run started at **12:00 PM ET** (16:00 UTC):
- **Mode:** incremental, start-date 2026-03-29, 60 workers
- **Instance:** bd-gold-layer-runner (i-01003b035d2988dfb), c6i.16xlarge
- **Log:** `/tmp/gold_runner.log`

### Completed steps in current run:
| Step | Status | Details |
|---|---|---|
| Canonical prices v2 | DONE (79s) | 10,565,013 rows, 10,047 assets |
| Scoped overrides | DONE | 12,099 rows for 7 assets |
| 00_accounts_dimension | DONE (skipped) | No new files since 2026-04-02 |
| 02_build_positions_cube | IN PROGRESS | 2,838,209 rows loaded, RPS injection phase (73,027 synthetic events from 5,255 Schwab-BD accounts) |

### Steps remaining:
03_holdings_lots -> 04_client_dimension -> 05_client_performance -> 05b_account_performance -> 05c/d_aua_validation -> 05f_account_quality_tiers -> 06_tax_liability -> 06b_client_mix_timeseries -> 07_nna_aua_by_geography -> 08_nna_aua_by_advisor -> 08b_architect_attribution -> 09_partner_analytics -> 10_advisor_rolling_flows -> 12_composition_artifacts

This run includes:
- **GLDRST.009**: S3 key migration (new layout paths at gold/timeseries/)
- **GLDOPS.003**: churn fix

---

## Resume Instructions

1. **Check if instance stopped** (= run complete):
   ```
   aws ec2 describe-instances --instance-ids i-01003b035d2988dfb --query "Reservations[].Instances[].State.Name" --output text
   ```

2. **If still running**, pull progress:
   ```
   aws ssm send-command --instance-ids i-01003b035d2988dfb --document-name "AWS-RunShellScript" --parameters 'commands=["tail -80 /tmp/gold_runner.log"]'
   ```

3. **On completion, verify:**
   - a. GRO numbers: NNA ~$300M, market growth ~$120M, GRO ~10-12% (expected from GLDOPS.003 task order)
   - b. GLDRST.009 migration: new layout paths populated at `s3://opal-data-bd/gold/timeseries/` (2,284+ positions_cube partitions expected)
   - c. Pipeline manifest at `s3://opal-data-bd/gold/meta/`
   - d. Churn column present in output

4. **Notify DS** with updated numbers from second run if they differ materially from first run.

---

## Inbox Watcher
- `inbox-watch.sh` running as PID 94716
- Output file: `/tmp/inbox-watch-ae.out`
