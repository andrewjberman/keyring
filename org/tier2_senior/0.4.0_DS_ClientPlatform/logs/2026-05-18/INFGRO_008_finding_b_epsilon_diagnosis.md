# Session Log -- ADVI_INFGRO.008 Finding B epsilon-coverage diagnosis

**Agent:** 0.4.0_DS_ClientPlatform (DS~C lane)
**Date:** 2026-05-18
**TO:** ADVI_INFGRO.008 (dsc-infc02-epsilon-coverage-diagnosis), issued by 2.0.0_SA_COO
**Project:** ADVI_INFGRO

---

## Current State

Phase 0 diagnosis COMPLETE. Finding B (firm_epsilon_$ = 71.6% of the AUA-growth
decomposition) root-caused. Candidates (i) coverage and (ii) staleness ruled OUT
with evidence; candidate (iii) ruled IN and precisely characterized:
`silver/performance_dim.twr_factor_period` is an inception-to-date ANNUALIZED TWR
rate, which `INF_C_02._build_daily_factor_table` misinterprets as a
cumulative-growth factor. Diagnosis brief committed; reconciliation-method choice
escalated to CTO. This TO is diagnosis-only -- no script modified.

---

## Diagnosis Summary

| Candidate | Verdict | Evidence |
|-----------|---------|----------|
| (i) incomplete perf coverage | RULED OUT | 100% of firm epsilon_$ ($16.50M) is in return-COVERED households; 0% in uncovered rows. Non-managed accounts = 0.1% of AUA. |
| (ii) bronze/performance staleness | RULED OUT (as cause) | performance_dim 05-13-only -> 4 stale days carry NaN return/epsilon -> fillna(0) -> contribute 0 to epsilon. Real freshness gap, surfaced as a linkage to RUNDATE-DISPATCH-IMPL, not the cause of dominance. |
| (iii) INF_C_02 per-row scaling/grain error | RULED IN -- sole cause | `twr_factor_period` is `1 + inception-to-date annualized return`; `_build_daily_factor_table` treats it as a cumulative-growth factor (`f_curr/f_prior`). Per-period returns come out ~6-10x too small; epsilon absorbs the rest. |

**Key proof:** reconstructing cumulative growth as `twr_factor_period ** years_since_inception`
recovers YTD returns matching the AUA-implied return within 0.2-0.6pp for
established households (167: +3.23% recon vs +3.46% AUA vs +0.36% current INF_C_02;
68: +5.14%/+5.41%/+0.61%; 388: +4.97%/+5.56%/+0.61%).

**Shared root with Finding A:** the same defect understates INFGRO.007's window
`*_return_pct_twr` in absolute scale (~6x) -- confirming the PRD section 8.4
predicted shared-upstream-root case. INFGRO.007's aggregation fix is correct; its
inputs are ~6x understated. INFGRO.005 criterion (a) is relatively-plausible-only
until the INF_C_02 fix lands.

---

## Compiler Tools

| Tool | Command | Observed | vs Expect |
|------|---------|----------|-----------|
| comp-pipescript io | `comp-pipescript io INF_C_02.client_performance` | READS: `gold/dimensions/accounts_dimension_latest.parquet`, `gold/timeseries/client_performance.parquet` (append-mode self-read). WRITES: `gold/timeseries/client_performance.parquet` -> INF_C_04, INF_C_06, INF_D_00, INF_D_00b, INF_D_00d, INF_D_04, INF_D_05a. No COLUMN GAPS. | PASS. WRITES + consumer fan-out match the TO expect. The dynamic paginated reads (`canonical_performance_*`, `silver/performance_dim/*`) are not statically traced by the tool -- documented from source instead. NOT a STOP condition: the PRD section 8.4 I/O model holds; the tool simply cannot trace `get_paginator` loops. |
| comp-pipescript feeds | `comp-pipescript feeds INF_C_02.client_performance` | "INF_C_02: no upstream pipeline dependencies (reads from silver or external)" | PASS. Matches the TO expect -- Set P / Set A sources are silver-tier / external, the basis for the coverage comparison. |

---

## Files Modified

| File | Change |
|------|--------|
| (none -- diagnosis-only TO) | No script modified. Read-only diagnosis. |

Deliverable produced: `docs/briefs/infgro-finding-b-epsilon-coverage-diagnosis-20260518.md`.

---

## Acceptance Criteria

| AC | Status | Notes |
|----|--------|-------|
| AC1 | PASS | Set P (37,656 rows / 295 hh) vs Set A (38,840 rows / 296 hh); A-P = 1,184 rows (the 4-day stale tail); count + AUA-weighted $ + per-advisor in the brief. |
| AC2 | PASS | 100% of firm epsilon_$ attributed to COVERED rows; candidate (i) explains 0%. |
| AC3 | PASS | (ii) ruled OUT (staleness contributes 0 to epsilon); (iii) ruled IN with the annualized-rate characterization + reconstruction proof. |
| AC4 | PASS | Brief committed under docs/briefs/ with A/B/C framing -- noting the TO's coverage-framed A/B/C do not fit, restated as Method X/Y/Z. |
| AC5 | PASS | Escalation MCP to 1.0.0_SA_CTO, CC 2.0.0_SA_COO. |
| AC6 | PASS | This Compiler Tools section reproduces both Phase 0 runs. |

---

## Next Steps

| Recipient | Item |
|-----------|------|
| **CTO 1.0.0** | Reconciliation-method ruling: Method X (reconstruct cumulative from the annualized rate in INF_C_02) vs Method Y (obtain a true cumulative/periodic TWR from Orion). Touches PRD section 2.4. The fix TO is authored after the ruling. |
| **COO 2.0.0** | CC on the escalation. Finding B is the shared root of INFGRO.007's absolute-scale understatement -- INFGRO.005 criterion (a) is relatively-plausible-only until the INF_C_02 fix lands; criterion (b) epsilon stays open on the fix. |
| **COO 2.0.0** | Linkage (not absorbed): performance_dim 05-13-staleness ties to the bronze/performance --run-date catalog item / RUNDATE-DISPATCH-IMPL (AE 0.7.0 lane). |
