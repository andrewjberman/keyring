# Session Log — ADVI_HISTBF.001 Phase 0 Probe

**Agent:** 0.4.0_DS_ClientPlatform_B  
**Date:** 2026-04-30  
**TO:** ADVI_HISTBF.001 Phase 0 — shape validation & asOf probe  
**Session type:** continuation from prior context (summary handoff)  

---

## What Happened

### Startup (resumed from summary)
Prior session had written all 8 probe scripts but not committed or run them. This session:
1. Ran pre-commit gate on all 8 scripts — all passed
2. Committed: `faff44c97` — 8 probe scripts
3. Pushed to origin/CLOUD

### Probe Execution — REST dims

**positions_mv** (`probe_inflec_positions_mv.py`)
- Ran immediately, 45/45 calls succeeded
- MV varies from $0 (2020-05-26) to $3.86M (today) across 5 sample clients
- Result: **SUPPORTED**

**assets_v2** (`probe_inflec_assets_v2.py`)
- 45/45 calls succeeded, zero missing fields at all dates
- Full 58-field schema present from 2020-05-26 through today
- Result: **SUPPORTED**

**accounts_v2** (`probe_inflec_accounts_v2.py`)
- 7 variants run; undocumented date params (asOfDate, snapshotDate, endDate) all silently ignored
- Row count = 2918 for all variants with undoc params. 3 accounts when `createdDateStart=today`
- Script classified as PARTIAL-INVESTIGATE due to today-filter variance, but manually evaluated as **CURRENT-ONLY**
- Result: **CURRENT-ONLY**

**household_rep_mapping** (`probe_inflec_household_rep_mapping.py`)
- All date variants return identical row counts per endpoint
- Script has a cross-comparison bug (rep vs client baseline comparison) triggering false PARTIAL-INVESTIGATE
- Manually evaluated: no actual row count difference across any date variant
- Result: **CURRENT-ONLY**

### Probe Execution — Envision dims (fixes required)

Encountered 3 bugs in Envision probes before successful runs:

**Bug 1 — CREATE missing requiredOptions/additionalOptions** (`3c553e6c1`)
- Envision `/ExcelReports/Verbose` POST requires `requiredOptions` and `additionalOptions` in create body
- Fix: load these from `billing_dim_spike.verbose.json` template

**Bug 2 — CREATE missing access rule blobs** (`dc3628f40`)
- Envision CREATE also requires `loginAccessRules`, `databaseGroupAccessRules`, etc.
- Fix: switch from scratch-built dict to full `billing_dim_spike.verbose.json` deep clone (same pattern as `pull_unified_account_dim.py`)

**Bug 3 — strftime `%-m/%-d/%Y` Windows incompatible** (`1a2ebac84`)
- Linux format string not supported on Windows Python
- Fix: replaced with `f"{d.month}/{d.day}/{d.year}"` cross-platform f-string

After fixes, all 4 Envision probes ran successfully:

**household** (`probe_inflec_household.py`)
- 4/5 ranges completed (7d timed out at 60s generate)
- Row count locked at 2904; rep_dist identical across all date ranges
- Result: **CURRENT-ONLY**

**billing** (`probe_inflec_billing.py`)
- 5/5 ranges completed, no timeouts
- Fees vary: 7d=-$87 → origin=-$20.35M. Row count 2904 constant; rep_dist identical
- Result: **PARTIAL**

**activity** (`probe_inflec_activity.py`)
- 4/5 ranges completed (365d timed out)
- Contrib/distrib vary by period. Rep_dist identical
- Result: **PARTIAL**

**performance** (`probe_inflec_performance.py`)
- 3/5 ranges completed (1825d + origin timed out — compute-heavy)
- TWR varies: 7d=-0.38% → 365d=+44.65%. Rep_dist identical
- Result: **PARTIAL**

### Deliverables Written
- `docs/data/inflec_histbf_eligibility_matrix.md` — 8-row matrix with evidence and Phase 1 implications
- `docs/data/inflec_histbf_rate_limiter_constants.md` — SAFE_FLOOR, STEP_UP/DOWN, BATCH_SIZE, per endpoint class

---

## Commits This Session
| Commit | Description |
|--------|-------------|
| `faff44c97` | feat(ADVI_HISTBF.001): Phase 0 probe scripts for all 8 dims |
| `3c553e6c1` | fix: Envision probes — add requiredOptions/additionalOptions to CREATE body |
| `dc3628f40` | fix: Envision probes — use full template clone (access rules) |
| `1a2ebac84` | fix: Envision probes — strftime %-m/%-d -> f-string (Windows) |

---

## Key Architectural Finding

**Rep assignment history is NOT accessible via any Orion API endpoint.**

All 3 endpoints that carry rep attribution (accounts_v2, household_rep_mapping, household Envision) return current-state assignments regardless of date params. For HISTBF Phase 1:
- MV backfill: PROCEED (REST endpoint fully supports historical dates)
- Billing/activity backfill: PROCEED with current-state rep attribution
- Historical rep-to-household state: NOT feasible via API; accept current-state mapping or obtain advisor transition dates from Inflection manually

**Envision performance timeout issue:** 5-year + cumulative TWR queries time out at 60s. Performance backfill should be limited to rolling 365d windows, consistent with standard industry reporting windows.

---

## RAVC4 Pending
Sending RAVC4 to COO + cc AE 0.6.1 upon commit of this log + deliverables.

Next phase (Phase 1) gates on:
1. JWTRES.001 ship (per ADVI_HISTBF.001 spec — JWT refresh resilience before full backfill)
2. CTO review of eligibility matrix
3. Phase 1 sizing/scope decision from AE 0.6.1 re: REST MV backfill approach
