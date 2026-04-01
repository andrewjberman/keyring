# ADHC_HISTRY P1: Schwab RPS Authority Injection Calculator -- 0.4.0_DS_ClientPlatform

**Date:** 2026-04-01
**Start Time:** 1:11 PM ET
**End Time:** 1:30 PM ET
**Project:** ADHC_HISTRY
**Task Order:** ADHC_HISTRY.002.ds-schwab-authority-injection.md

---

## Objective

Write the Phase 1 diagnostic script (`adhc_histry_005_schwab_authority_calc.py`)
implementing the Schwab RPS authority injection calculation per COO GO received
2026-04-01T13:04Z.

CTO revision: use silver/RPS/ (daily position snapshots) as the Schwab authority
instead of silver/TRN/ reconstruction. RPS gives `quantity_settled` directly per
(account, CUSIP, date) -- no sign convention analysis, no FIFO reconstruction on the
Schwab side.

---

## Work Completed

### 1. GO Message Processed

COO GO received via inbox-watch.sh, task order status already `pending`. Inbox
re-launched immediately.

### 2. Conflict Resolution Before Writing Code

Task order has a semantic conflict:
- **Objective** (CTO revised 2026-04-01): use `silver/RPS/` as Schwab authority
- **Requirement 1b** (stale, not updated): says to aggregate `silver/TRN/`
- **COO GO message**: references TRN as available, says "begin immediately"
- **Prerequisite** in objective: "wait for AE's MCP message confirming silver/RPS/ is ready"

Resolution: CTO objective amendment wins. RPS is the correct approach per Andrew's
direction. "Begin immediately" applies to writing the script (local work), not EC2
execution. "Wait for AE" applies to the S3 upload + EC2 run.

**Action taken:** Messaged AE (0.6.0_AE_PartnerETL) asking if `silver/RPS/` has been
built. AE's 2026-03-31 session log shows the TRN converter was run (337 partitions)
but does NOT show the RPS converter being run. Currently blocked on ADHC_HISTRY.003.

### 3. Script Written and Committed

**File:** `data/black_diamond/scripts/diagnostics/adhc_histry_005_schwab_authority_calc.py`
**Commit:** `c8db9f09`

#### Script Design

| Step | Action |
|------|--------|
| 1 | Check `silver/RPS/` availability -- hard exit with clear BLOCKED message if empty |
| 2 | Load account mapping (`schwab_bd_account_mapping.parquet`, 6,510 rows) |
| 3 | Build CUSIP->asset_name bridge from BD unrealized (CUSIP is authoritative join key) |
| 4 | Load all BD transactions + compute FIFO open positions (mirrors script 02 logic) |
| 5 | Load canonical prices (latest per asset) |
| 6 | Load silver allocations (reference MV for comparison) |
| 7 | **Part 1**: Load latest RPS partition, compute injection gap per (account, CUSIP) |
| 8 | **Part 2**: Iterate all RPS dates, build time series of injection gap |
| 9 | Write outputs: `schwab_authority_calc.csv`, `_overcounts.csv`, `_timeseries.csv`, `_summary.json` |

#### Key Design Decisions

| Decision | Rationale |
|---|---|
| RPS not TRN | CTO revision per Andrew's direction. RPS = position snapshot, no FIFO needed |
| CUSIP as join key | Task order constraint. TRN had ticker ambiguity (old vs new symbols). CUSIP is stable. |
| CUSIP->asset_name via BD unrealized | Both CUSIP and asset_name are present in unrealized_gain_loss.parquet |
| FIFO computed fresh from transactions | Measures true gap between what script 02 produces and Schwab RPS. Same logic as prior diagnostic. |
| Hard exit if RPS empty | Do NOT fall back to TRN silently -- that contradicts the CTO revision |
| NAME_ALIASES applied | RC1 fix must be consistent: OPAL DIVIDEND -> POLEN DIVIDEND |
| CASH excluded from injection | Confirmed correct per prior sessions |
| Over-counts flagged, not injected | Positions where FIFO > Schwab are suspect -- separate investigation needed |

---

## Current Status

**Script:** COMMITTED locally at `c8db9f09`. NOT yet uploaded to S3.

**Blocked on:** AE confirming `silver/RPS/` is populated (ADHC_HISTRY.003).
AE messaged at 1:11 PM ET asking for status.

**Do NOT:**
- Upload to S3 or run on EC2 until AE confirms silver/RPS/ is ready
- Interpret the script as complete for Phase 1 acceptance -- the EC2 run + results are still needed
- Deploy RC3/RC4 (held per Andrew's direction from 2026-03-31)

---

## Diagnostic Results

**Status: PENDING -- script not yet run on EC2.**

Results will be filed in a follow-on session log when:
1. AE confirms silver/RPS/ is populated
2. Script is uploaded to S3 (by AE per EC2_CODE_DEPLOYMENT_STANDARD.md)
3. EC2 SSM run completes
4. Output CSV downloaded and analyzed

Expected outputs:
- `s3://opal-data-bd/diagnostics/schwab_authority_calc.csv` (per-position injection gaps)
- `s3://opal-data-bd/diagnostics/schwab_authority_calc_overcounts.csv` (FIFO > RPS flags)
- `s3://opal-data-bd/diagnostics/schwab_authority_calc_timeseries.csv` (gap over time)
- `s3://opal-data-bd/diagnostics/schwab_authority_calc_summary.json` (machine-readable summary)

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `data/black_diamond/scripts/diagnostics/adhc_histry_005_schwab_authority_calc.py` | New diagnostic script | Yes -- `c8db9f09` |

---

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| This session log | This file | COO, AE |

---

## Next Steps

1. **[0.6.0_AE_PartnerETL]** Run `convert_schwab_rps_to_parquet.py` to build `silver/RPS/`
   (ADHC_HISTRY.003). Confirm partition count and date range to DS via MCP.

2. **[0.6.0_AE_PartnerETL]** Upload `adhc_histry_005_schwab_authority_calc.py` to S3
   per EC2_CODE_DEPLOYMENT_STANDARD.md after AE confirms silver/RPS/ is ready.

3. **[0.6.0_AE_PartnerETL]** Run on EC2 via SSM. Pull output from
   `s3://opal-data-bd/diagnostics/schwab_authority_calc_summary.json`.

4. **[0.4.0_DS_ClientPlatform]** Analyze results when EC2 run completes. File updated
   session log with injection gap totals, DIVZ numbers, over-count investigation.
   Report to COO to trigger Phase 2 GO.

5. **[2.0.0_SA_COO]** Review Phase 1 results when DS reports back. If injection targets
   look clean (DIVZ ~$100-110M, total gap plausibly < residual $341M), issue Phase 2 GO.
