# NNAVAR Structural Diagnostics EC2 Execution — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 19:29
**End Time:** 19:44

---

## Objective

Execute all 4 suites of `diag_nnavar_structural.py` (Phase 3) on EC2
`i-01003b035d2988dfb` per `docs/briefs/devops-brief-nnavar-structural-ec2-run.md`.
Tests three structural hypotheses: Transfer contamination, settle vs trade date,
and BI pre-computed NNA cross-validation.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | git pull CLOUD | Already up-to-date at `5e24913e` |
| 2 | Upload script to S3 | `s3://opal-data-bd/scripts/diagnostics/diag_nnavar_structural.py` (42.2 KB) |
| 3 | Start EC2 instance | Was stopped — started, SSM online |
| 4 | Suite: schema | CMD `92fd62f4` — SUCCESS, 54s |
| 5 | Gating check passed | external_flow_present=true, settle_date_present=true (100% non-null) |
| 6 | Suite: external_flow | CMD `c261b223` — SUCCESS, 45s |
| 7 | Suite: settlement | CMD `2be1b602` — SUCCESS, 30s |
| 8 | Suite: bi_crossval | CMD `e23a0ae4` — SUCCESS, 3s (not_available.json) |

---

## Schema Suite — Gating Flags

| Flag | Value | Implication |
|------|-------|-------------|
| `external_flow_present` | **true** | external_flow suite enabled |
| `settle_date_present` | **true** (100% non-null) | settlement suite enabled |
| Account coverage | **$0.0M unmapped** | Perfect relationship mapping in Schwab window |
| Partition coverage | All 13 months: **OK** | No data gaps |
| Cross-month settle rows | **1.2%** of flow rows | Small; mostly T+0/T+1 |

**Transfer type breakdown (key finding):**
- Transfer In: 72,591 rows → 72,591 tagged `external_flow=Contribution` ($1.510B)
- Transfer Out: 30,884 rows → 30,884 tagged `external_flow=Withdrawal` (-$622M)
- Null/blank external_flow rate: **0.0%** — ALL rows tagged

S3: `s3://opal-data-bd/diagnostics/nnavar_structural/20260306/schema/`

---

## External_Flow Suite Results

| Variant | Flow rows | Inflow | Outflow | pearson_r | sign_agr | total_gap |
|---------|-----------|--------|---------|-----------|----------|-----------|
| `ef_all_transfers` *(prod)* | 233,874 | $2,693.2M | $1,803.6M | 0.157 | 11/13 | -$124.7M |
| `ef_contribution_only` | 233,789 | $2,693.2M | $1,803.6M | 0.157 | 11/13 | -$124.7M |
| `ef_nonempty` | 233,845 | $2,693.2M | $1,803.6M | 0.157 | 11/13 | -$124.7M |
| `ef_no_transfers` | 145,032 | $1,397.4M | $1,328.9M | **0.386** | 7/13 | -$312.5M |

S3: `s3://opal-data-bd/diagnostics/nnavar_structural/20260306/external_flow/`

---

## Settlement Suite Results

| Variant | pearson_r | sign_agr | total_gap |
|---------|-----------|----------|-----------|
| `settle_trade_date` *(prod)* | 0.157 | 11/13 | -$124.7M |
| `settle_settle_date` | 0.156 | 12/13 | -$119.0M |
| `settle_settle_strict` | 0.156 | 12/13 | -$119.0M |

S3: `s3://opal-data-bd/diagnostics/nnavar_structural/20260306/settlement/`

---

## BI Cross-Validation Suite

**Result:** `not_available.json` — BI data not found in any candidate S3 path.
This is expected behavior per the brief. No retry needed.

S3: `s3://opal-data-bd/diagnostics/nnavar_structural/20260306/bi_crossval/`

---

## Key Findings (DT observations)

1. **`ef_contribution_only` and `ef_nonempty` are IDENTICAL to production baseline.**
   All Transfer In/Out rows are already tagged with external_flow=Contribution/Withdrawal.
   Filtering by external_flow label makes zero difference. The schema audit confirmed:
   external_flow null/blank rate = 0.0% for flow rows.

2. **Removing Transfers entirely (`ef_no_transfers`) achieves pearson=0.386** — the
   highest correlation found across all phases. Transfer rows (72,591 In + 30,884 Out)
   add significant noise that degrades correlation. However:
   - Sign agreement collapses: 11/13 → 7/13
   - Gap widens significantly: -$124.7M → -$312.5M
   Transfer rows partially fill the Schwab gap even while lowering correlation quality.

3. **Settlement date is not a meaningful driver.** settle_date moves sign agreement
   11→12 and narrows gap by $5.7M — within noise. The 1.2% cross-month rows are
   immaterial at the 13-month aggregation level.

4. **BI pre-computed NNA not available in S3.** Cannot cross-validate against BD's
   own NNA figures. DS/COO to decide if BI data retrieval is worth pursuing.

5. **Phase 3 ceiling (with Transfers excluded): pearson=0.386.** Still below PRD
   target of 0.50. The Transfer rows are the dominant noise source, but they also
   contribute real flow volume that partially matches Schwab. The net question for
   DS: does Schwab count Transfer In/Out separately from their NNA calculation?

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Run bi_crossval immediately after settlement | Non-blocking; 3s to confirm not_available |
| Report all 4 suites together | All completed in <3 min total active runtime |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| None — script committed by DS at `defdf684` | Upload to S3 only | N/A |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

All 4 Phase 3 structural suites complete. Key finding: Transfer rows are the dominant
structural noise source. `ef_no_transfers` achieves pearson=0.386 (new high) but at
cost of sign agreement and gap. Settlement date and external_flow labeling are both
non-drivers. BI cross-validation data not in S3. DS determines Phase 4 scope.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Interpret ef_no_transfers result** — Does Schwab
   count Transfer In/Out in their NNA? If Schwab excludes internal transfers, our
   inclusion of them is the structural mismatch. If Schwab includes them, the noise
   is methodological.

2. **[COO/DS] Determine whether to pursue BI data retrieval** — `not_available.json`
   confirmed no BI data in S3. If BI pre-computed NNA is needed, it requires a
   separate data pull from the BI system.

3. **[COO] Go/no-go on Phase 4** — Phase 3 ceiling is pearson=0.386. If the target
   (0.50) is still required, Phase 4 needs to address the Transfer row question
   definitively.

**Do NOT:**
- Deploy any parameter or filter changes to production without DS/COO task order
- Pursue BI data retrieval without explicit instruction
