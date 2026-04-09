# ADVI_GLDOPS.002 + .003 -- Pending Marker Fix + Market Growth Diagnostic

**Date:** 2026-04-06
**Start Time:** 7:30 AM ET
**End Time:** 8:30 AM ET
**Project:** ADVI_GLDOPS

---

## Objective

Two task orders completed in one session:
1. GLDOPS.002 (P0) -- Re-enable pending marker check in EC2 runner + watchdog
2. GLDOPS.003 (P1) -- Diagnose and fix portal GRO showing ~1% vs actual 10-12%

---

## Work Completed

### 1. GLDOPS.002: Pending Marker Fix

**Commit:** `af47c84e`

Two files changed:

**infra/aws/ec2/bd-gold-layer-runner/run-gold-layer.sh:**
- Uncommented the pending marker check block (was disabled to prevent double-runs during QA)
- Added QA rebuild guard: `/tmp/GOLD_QA_REBUILD` marker file skips the check
- This is a safety net -- the inner runner (`run_gold_layer.sh` in gold scripts) checks
  pending markers on clean exit. The EC2 runner catches cases where the inner runner
  errors out and its own pending check never fires.

**infra/aws/ec2/bd-gold-layer-runner/watchdog-shutdown.sh:**
- Added Check 4 before shutdown: if `trigger-pending.json` exists on S3, skip shutdown
- Prevents watchdog from killing the instance while a pending incremental is queued

No conflict between inner/outer pending checks -- both delete marker before re-running,
and inner runner `exec`s (replaces process) so outer block never executes on clean exits.

### 2. GLDOPS.003: Market Growth Diagnostic + Fix

**Root cause identified:** Silver AUA override in script 05.

**Commit 1:** `8a6fef07` -- Disabled silver override
**Commit 2:** `e419d83b` -- Publisher reads pre-computed decomposition columns

#### Full Audit of NNA/GRO Pipeline Caps/Clamps

| # | Mechanism | Effect on GRO | Status |
|---|---|---|---|
| 1 | Silver AUA override (script 05) | Clips gold AUA to silver, suppresses market growth | **DISABLED** -- RPS injection closed gap to 0.3% |
| 2 | Bond face-value detection (script 05) | Corrects FI positions with wrong Yahoo price | Keep -- pricing source bug, RPS doesn't fix |
| 3 | Ghost account exclusion RC6 (script 05) | Removes manually-flagged closed accounts | Keep -- small population, protective |
| 4 | NNA type filter (nna_flows.py) | Only Cash Deposit/Transfer In/Out counted | Keep -- definitionally correct |
| 5 | NNA exclusions (nna_flows.py) | Removes JNL, Schwab internal transfers, sweeps | Keep -- not real NNA |
| 6 | FLOW_CAP $50M per event (nna_flows.py) | Biases GRO UP (understates NNA) | Keep -- outlier guard |
| 7 | AUA-based outflow cap (script 05) | Reduces outflows -> inflates NNA -> depresses GRO | Keep -- BD data quality guard, now uses unclamped gold AUA |
| 8 | Velocity cap 90d/100% (script 05) | Same direction as #7 | Keep -- BD data quality guard, now uses unclamped gold AUA |
| 9 | Publisher GRO formula (publisher Lambda) | Was recomputing market = delta(AUA) - delta(NNA), ignoring synthetic_correction | **FIXED** -- reads pre-computed columns |

Items 7-8 noted as "keep but monitor" -- they suppress outflows which depresses market
growth, but they protect against real BD garbage data ($3.6B phantom withdrawals). With
silver override disabled, they now use raw gold AUA as the ceiling, which is more accurate.

#### Publisher GRO Fix Detail

Old formula (line 919): `market = delta(AUA) - delta(NNA)`
- Conflated synthetic injection with market growth
- Silver-overridden AUA further suppressed the delta

New formula: reads pre-computed daily columns from script 05:
- `market = sum(market_growth)` per month -- pure price appreciation
- `synthetic = sum(synthetic_correction)` per month -- RPS injection changes
- `nna = cumulative NNA endpoint diff` -- cash flows
- `total = market + nna + synthetic`

Graceful fallback for pre-GLDRST.017 gold data: if parquet lacks `market_growth`
and `synthetic_correction` columns, reverts to old formula.

New `synthetic` key in `growth_decomposition` JSON is additive -- portal frontend
ignores unknown keys (reads only `market`, `nna`, `total`). DT can add display later.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Disable silver override entirely (not raise threshold) | RPS injection brings gold within 0.3% of silver -- any override threshold clips legitimate growth |
| Keep bond detection enabled | Different problem (pricing source bug), not addressable by RPS |
| Keep AUA/velocity outflow caps | BD transaction market_value quality is independent of RPS position accuracy |
| Publisher reads decomposition columns | Single source of truth for market growth calculation (script 05), avoids dual computation |
| Add `synthetic` to GRO output | Enables portal to display RPS injection impact separately in the future |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `infra/aws/ec2/bd-gold-layer-runner/run-gold-layer.sh` | Re-enable pending marker with QA guard | `af47c84e` |
| `infra/aws/ec2/bd-gold-layer-runner/watchdog-shutdown.sh` | Add Check 4: pending marker prevents shutdown | `af47c84e` |
| `data/black_diamond/scripts/gold/05_build_client_performance.py` | SILVER_OVERRIDE_ENABLED = False | `8a6fef07` |
| `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py` | GRO reads pre-computed decomposition; graceful fallback; `synthetic` key added | `e419d83b` |
| Task orders: GLDOPS.002, GLDOPS.003 | Both marked complete | uncommitted |

---

## Current State

**Status:** ALL CODE COMPLETE. Both task orders done.
**Active branch:** CLOUD

All commits local on CLOUD, not pushed. Deployment chain:
- DT pushes CLOUD
- AE uploads script 05 to S3 (`s3://opal-data-bd/code/gold/`)
- AE uploads runner scripts to S3 (`s3://opal-data-bd/code/runner/`)
- Terraform deploy for bd-portal-publisher Lambda
- Gold rebuild (incremental or full) regenerates client_performance.parquet with unclamped AUA
- Publisher reads new columns and produces correct GRO

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform]** Push CLOUD, deploy bd-portal-publisher Lambda
2. **[0.6.0_AE_PartnerETL]** Upload script 05 + runner scripts to S3
3. **[0.6.0_AE_PartnerETL]** Run gold catch-up (will also rebuild canonical prices as pre-step)
4. **[0.4.0_DS_ClientPlatform]** After rebuild: verify GRO shows ~10-12% for 2025, verify total = market + nna + synthetic

**Do NOT:**
- Trust portal GRO numbers until gold rebuild with `8a6fef07` + `e419d83b` completes
- Re-enable silver override -- it is deprecated post-RPS
- Modify outflow caps without monitoring data first (items 7-8)
