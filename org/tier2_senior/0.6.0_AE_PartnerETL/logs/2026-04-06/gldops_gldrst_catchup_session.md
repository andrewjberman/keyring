# GLDOPS.001-.003 + GLDRST.009 -- Gold Catch-Up + S3 Migration Session -- 0.6.0_AE_PartnerETL

**Date:** 2026-04-06
**Projects:** ADVI_GLDOPS, ADVI_GLDRST
**Status:** IN PROGRESS -- gold incremental running (GLDRST.009 migration + GLDOPS.003 churn fix)

---

## Session Summary

Resumed from crashed session. Executed P0 data freshness diagnosis, 4-day gold outage root cause analysis, gold catch-up runs, RPS ingestion, GRO investigation, and S3 layout migration.

---

## 1. GLDOPS.001 -- Data Freshness Diagnosis (COMPLETE)

Diagnosed why daily gold trigger stopped producing runs since 04-02. Three independent root causes:

| Root Cause | Evidence |
|---|---|
| **systemd service disabled** on bd-gold-layer-runner | `systemctl is-enabled gold-layer-runner` -> `disabled`. Apr 2 21:52 UTC boot produced zero gold output. No log uploaded. |
| **AutoShutdown=disabled tag** on EC2 | ec2-auto-shutdown-enforcer logged 2,361 SKIPs across Apr 2-6: "SKIP: AutoShutdown=disabled tag" every 15 min |
| **Watchdog + pending marker deadlock** | Lambda wrote trigger-pending.json (instance running). Watchdog saw marker -> refused shutdown. No process alive to consume marker. Dead loop. |

**Fix applied:** `systemctl enable gold-layer-runner` (permanent). Instance stopped + pending marker cleared.

---

## 2. RPS Ingestion (COMPLETE)

4 new RPS files from Schwab Data Delivery (OneDrive):
- `CRS20260330.RPS`, `CRS20260331.RPS`, `CRS20260401.RPS`, `CRS20260402.RPS`
- Uploaded to `s3://opal-data-schwab/bronze/rps/` with `--sse AES256` (bucket policy requires it)
- Converter (`convert_schwab_rps_to_parquet.py`) run on EC2: 2 new silver partitions (20260401: 83,879 positions, 20260402: 83,917 positions). 20260330/20260331 already existed.
- **Total silver/RPS partitions: 558**

---

## 3. Gold Catch-Up Runs (Multiple Iterations)

### Run 1 -- Initial catch-up (13:02 UTC)
- Scripts: 00, 02, 05, 05c, 05d, 05f, 07, 08b, 08, 06b, 12, 09, 10
- **Result:** COMPLETE. Data as of 2026-04-02. AUA $1,631,539,372.
- GRO: -6.3% (AUA/velocity caps suppressing $673M in outflows)

### Run 2 -- Garbage filter (GLDOPS.003, ~14:30 UTC)
- DS commit `7ec37c80`: surgical garbage filter replaces blunt AUA/velocity caps
- nna_flows.py: 10x-account-AUA OR $50M absolute threshold (OR logic)
- **Result:** COMPLETE. GRO: +0.3%. Garbage filter excluded 282 events ($7.5B).
- Caps gone but GRO still near zero -- relationship churn contaminating market_growth

### Run 3 -- Churn fix attempt 1 (~15:34 UTC)
- DS commit `81ce9182`: churn component in AUA decomposition
- **Result:** FAILED. `ModuleNotFoundError: No module named 'lib.s3_layout'`
- Cause: churn fix pulled in GLDRST.004 s3_layout dependency

### Run 4 -- Churn fix attempt 2 (~15:54 UTC)
- Uploaded `lib/s3_layout.py` to S3
- **Result:** FAILED. `RuntimeError: No positions_cube partitions found`
- Cause: script 05 reads from new path `gold/timeseries/positions_cube/` but data only at old path `gold/positions_cube/`

### Run 5 -- S3 migration copy + combined run (IN PROGRESS, started 16:00 UTC)
- **Pre-step:** Copied ALL existing data from old S3 layout to new layout:
  - 2,284 positions_cube partitions -> `gold/timeseries/positions_cube/`
  - client_performance, synthetic_positions_index, account_performance, etc -> `gold/timeseries/`
  - accounts_dimension, advisor_assignments, client_dimension -> `gold/dimensions/`
  - firm_composition -> `gold/views/`
  - firm_mix_views, advisor_rolling_flows -> `gold/artifacts/`
  - partner_analytics -> `gold/artifacts/partner_analytics/`
  - aua_certification -> `gold/validation/aua_certification/`
  - pipeline-complete -> `gold/meta/`
- **Full S3 sync:** All 20 gold scripts + lib/ uploaded via `aws s3 sync`
- **Status at pause:** Script 02 step 2a (realized sell injection), ~8 min in. EC2 i-01003b035d2988dfb running.
- **Expected:** ~25-30 min to completion

---

## 4. GLDOPS.003 GRO Investigation Trail

| Run | GRO | NNA (endpoint) | Mkt Growth | Cap/Filter Eliminated |
|---|---|---|---|---|
| Caps (AUA 100% + velocity) | -6.3% | $391M | -$59M | $673M |
| Cap sensitivity Option A (no caps) | +0.5% | $328M | +$4M | $0 |
| Garbage filter (282 events) | +0.3% | $305M | +$3M | $7.5B |
| **Churn fix (pending)** | **~10-12% expected** | **~$300M** | **~$120M** | garbage filter |

DS root cause: new relationships entering mid-period have their initial AUA counted as market_growth (delta_aua - NNA for a relationship that didn't exist at period start). Churn decomposition separates entry/exit AUA from organic market growth.

**Cap sensitivity diagnostic** (`gldops_003_cap_sensitivity.py`) confirmed caps were the dominant distortion. **Pricing coverage diagnostic** (`gldops_003b_pricing_coverage.py`) confirmed 99.4% priced, $153M never-priced (structured notes, private funds). Pricing is not the main GRO gap.

---

## 5. GLDRST.009 S3 Migration (IN PROGRESS)

### What's deployed
- All gold scripts with GLDRST.004 (dual-write to old + new paths)
- `lib/s3_layout.py` -- centralized S3 key registry
- All data pre-copied from old layout to new layout (server-side S3 copy on EC2)
- Lambdas: bd-v2.21.2 (publisher + advisor-publisher with new paths), partners-api-v1.13.1

### New S3 Layout
```
gold/dimensions/       -- accounts_dimension, advisor_assignments, client_dimension
gold/timeseries/       -- positions_cube/, holdings_lots/, client_performance, etc.
gold/views/            -- nna_aua_by_geography, by_advisor, architect_attribution, etc.
gold/artifacts/        -- firm_mix_views, advisor_rolling_flows, partner_analytics/
gold/entities/         -- advisors/{id}/, clients/{id}
gold/validation/       -- aua_certification/, aua_validation
gold/meta/             -- pipeline-complete, pipeline-manifest, watermark
```

### Verification needed after run completes
1. All new-layout S3 keys exist
2. Old vs new key file sizes match (dual-write parity)
3. `gold/meta/pipeline-manifest.json` written (.006)
4. No import errors from lib.s3_layout
5. GRO shows ~10-12% (churn decomposition working)
6. `churn` column present in client_performance.parquet

---

## 6. Messages Sent This Session

| To | Subject | Time |
|---|---|---|
| 1.0.0_SA_CTO | P1 DIAGNOSIS: Why daily gold trigger stopped | 12:03 |
| 1.0.0_SA_CTO | BOOT FAILURE ROOT CAUSE: systemd disabled | 12:08 |
| 2.0.0_SA_COO | RPS scheduling analysis + gold catch-up running | 12:11 |
| 0.4.0_DS | Re: script 05 status -- hot-patched, merge_asof error | 12:28 |
| 0.4.0_DS | GRO data: caps eliminated $673M | 13:43 |
| 0.4.0_DS | Cap sensitivity results -- all 4 configurations | 13:50 |
| 2.0.0_SA_COO | Gold catch-up COMPLETE -- GRO needs DS investigation | 13:40 |
| 0.4.0_DS | Garbage filter gold run complete -- GRO 0.3% | 14:59 |
| 2.0.0_SA_COO | GLDOPS.003 garbage filter run complete | 14:59 |
| 0.4.0_DS | Pricing coverage diagnostic results | 15:09 |

---

## 7. Files Uploaded to S3 This Session

| File | S3 Path | Purpose |
|---|---|---|
| run-gold-layer.sh | s3://opal-data-bd/code/runner/ | Pending marker fix (af47c84e) |
| watchdog-shutdown.sh | s3://opal-data-bd/code/runner/ | 0.7.0 improvements (consolidated pgrep, timeout 10) |
| 05_build_client_performance.py | s3://opal-data-bd/code/gold/ | Multiple: merge_asof fix, silver override disabled, garbage filter, churn |
| lib/nna_flows.py | s3://opal-data-bd/code/gold/lib/ | Surgical garbage filter |
| lib/s3_layout.py | s3://opal-data-bd/code/gold/lib/ | GLDRST.004 centralized key registry |
| All 20 gold scripts | s3://opal-data-bd/code/gold/ | Full sync: GLDRST.004/.005/.006 + churn |
| convert_schwab_rps_to_parquet.py | s3://opal-data-bd/code/schwab/ | RPS converter |
| gldops_003_cap_sensitivity.py | s3://opal-data-bd/code/diagnostics/ | Cap sensitivity diagnostic |
| gldops_003b_pricing_coverage.py | s3://opal-data-bd/code/diagnostics/ | Pricing coverage diagnostic |
| 4x .RPS files | s3://opal-data-schwab/bronze/rps/ | CRS20260330-20260402 |

---

## 8. EC2 State at Session Pause

- **Instance:** i-01003b035d2988dfb (c6i.16xlarge)
- **State:** RUNNING (gold incremental in progress)
- **systemd:** gold-layer-runner ENABLED + ACTIVATING
- **Current script:** 02_build_positions_cube (step 2a, ~8 min CPU)
- **GOLD_KEEP_ALIVE:** removed (runner will self-shutdown on completion)
- **Log will be at:** s3://opal-data-bd/logs/gold-layer/gold_incremental_2026-04-06_*.log (newest one after ~16:00 UTC start)

---

## 9. What to Do on Resume

1. **Check if run completed:** `aws ec2 describe-instances --instance-ids i-01003b035d2988dfb --query 'Reservations[0].Instances[0].State.Name'`
   - If `stopped`: run completed. Check log + pull GRO numbers.
   - If `running`: check progress via SSM.

2. **GRO verification (the key metric):**
```python
# On local machine (reads from S3)
import boto3, pandas as pd
from io import BytesIO
s3 = boto3.client('s3')
resp = s3.get_object(Bucket='opal-data-bd', Key='gold/client_performance.parquet')
df = pd.read_parquet(BytesIO(resp['Body'].read()))

# Check for churn column
print('Has churn:', 'churn' in df.columns)

# Correct NNA (endpoint diff, NOT sum)
start = df[df['date'] == '2024-12-31'].groupby('relationship_id')['nna'].last()
end = df[df['date'] == '2025-12-31'].groupby('relationship_id')['nna'].last()
nna_2025 = (end - start).sum()

yr_2025 = df[(df['date'] >= '2025-01-01') & (df['date'] <= '2025-12-31')]
market_growth_2025 = yr_2025['market_growth'].sum()
churn_2025 = yr_2025['churn'].sum() if 'churn' in df.columns else 'N/A'
synth_2025 = yr_2025['synthetic_correction'].sum()
aua_2024 = df[df['date'] == '2024-12-31']['total_aua'].sum()
gro_pct = market_growth_2025 / aua_2024 * 100

# Expected: NNA ~$300M, market_growth ~$120M, GRO ~10-12%, churn column present
```

3. **GLDRST.009 verification:**
   - Check new S3 paths populated: `aws s3 ls s3://opal-data-bd/gold/timeseries/positions_cube/ | wc -l` (should be 2284+)
   - Check manifest: `aws s3 cp s3://opal-data-bd/gold/meta/pipeline-manifest.json -`
   - Check dual-write: compare file sizes old vs new for a sample key

4. **If GRO is correct (~10-12%):** Report to COO + DS. GLDOPS.003 verified.

5. **If GRO still wrong:** Check if `churn` column exists. If missing, the churn commit didn't take effect. Check which script 05 version the EC2 used.

6. **GLDRST.010 (old key cleanup):** Staged, blocked on .009 verification. After .009 confirmed, can delete legacy S3 keys.

7. **Session log:** Commit this log with `--author="0.6.0_AE_PartnerETL <0.6.0_AE_PartnerETL@opal.agent>"`

---

## 10. Pending Task Orders

| TO | Status | Blocker |
|---|---|---|
| ADVI_GLDOPS.001 | COMPLETE | -- |
| ADVI_GLDRST.009 | IN PROGRESS | Current gold run |
| ADVI_GLDRST.010 | PENDING | .009 verification |
| ADVI_GLDRST.014 | STAGED | .010 completion |
