# ADVI_NNAVAR Phase 3 + 3b Synthesis — Investigation Ceiling Assessment — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 20:45
**End Time:** 21:30

## Objective

Analyze DT's Phase 3 structural diagnostic results (`diag_nnavar_structural.py`, all 4 suites)
and Phase 3b timing shift results (`diag_nnavar_timing_shift.py`, both suites). Determine
which structural hypotheses are confirmed or rejected, assess the investigation ceiling, and
produce a COO-facing synthesis memo with production recommendations.

---

## Work Completed

### 1. Phase 3 Structural Results — Analysis

DT ran all 4 suites of `diag_nnavar_structural.py` (commits `defdf684` / `5e24913e`,
EC2 run completed ~19:44, DT log `nnavar_structural_diagnostics_ec2.md`).

**Schema suite — gating flags:**
- `external_flow_present`: true
- `settle_date_present`: true, 100% non-null
- Account coverage: $0.0M unmapped — perfect relationship mapping
- Partition coverage: all 13 months OK
- Cross-month settle rows: 1.2%
- Transfer In (72,591 rows) — 100% tagged `external_flow=Contribution`
- Transfer Out (30,884 rows) — 100% tagged `external_flow=Withdrawal`
- **Null/blank external_flow rate: 0.0%**

**External flow suite:**

| Variant | pearson_r | sign_agr | total_gap |
|---------|-----------|----------|-----------|
| `ef_all_transfers` (prod) | 0.157 | 11/13 | -$124.7M |
| `ef_contribution_only` | 0.157 | 11/13 | -$124.7M |
| `ef_nonempty` | 0.157 | 11/13 | -$124.7M |
| `ef_no_transfers` | **0.386** | 7/13 | -$312.5M |

**Settlement suite:**

| Variant | pearson_r | sign_agr | total_gap |
|---------|-----------|----------|-----------|
| `settle_trade_date` (prod) | 0.157 | 11/13 | -$124.7M |
| `settle_settle_date` | 0.156 | 12/13 | -$119.0M |
| `settle_settle_strict` | 0.156 | 12/13 | -$119.0M |

**BI cross-val:** `not_available.json` — no BI parquet in any candidate S3 path.

---

### 2. Phase 3b Timing Shift Results — Analysis

DT ran both suites of `diag_nnavar_timing_shift.py` (commit `3d0b6a82`, EC2 run completed
~20:42, DT log `nnavar_timing_shift_ec2.md`). DT fixed a float format bug at line 329
(`1094bb17`) before final run.

**Monthly lag suite:**

| lag | pearson_r | sign_agr | total_gap |
|-----|-----------|----------|-----------|
| -4 | 0.054 | 13/13 | -$78.1M |
| **-3** | **0.418** | **12/13** | **-$96.9M** |
| -2 | -0.138 | 12/13 | -$87.6M |
| -1 | 0.293 | 11/13 | -$114.9M |
| +0 (prod) | 0.175 | 10/13 | -$119.8M |

Peak at L=-3: our NNA leads Schwab by approximately 3 months. This is consistent with
BD posting Transfer/ACAT flows at initiation; Schwab reporting them at full settlement.

**Day shift suite — offset consistency verdict:**

```json
{
  "mean_optimal_offset_days": 2.6,
  "median_optimal_offset_days": -2.0,
  "std_optimal_offset_days": 21.8,
  "min_optimal_offset_days": -29,
  "max_optimal_offset_days": 30,
  "interpretation": "VARIABLE TIMING -- high variance, not correctable by a fixed offset rule"
}
```

Best achievable within ±30 days: pearson=0.360 (transfer_only, N=-22d).

---

### 3. Hypothesis Verdict Summary

| Hypothesis | Status | Evidence |
|------------|--------|----------|
| `external_flow` filter removes internal transfers | **REJECTED** | 100% of Transfer rows tagged Contribution/Withdrawal; ef_contribution_only ≡ ef_all_transfers. No discriminative value. |
| Settlement date (settle_date vs trade_date) shifts NNA into correct months | **REJECTED (marginal)** | +1 sign_agr, -$5.7M gap, -0.001 pearson. 1.2% cross-month rows immaterial at 13-month level. |
| BI cross-validation provides definitional ground truth | **BLOCKED** | BI parquet not in S3. Would require a separate BI data extraction. |
| Transfer rows add timing noise vs Schwab | **CONFIRMED — timing is the mechanism** | ef_no_transfers achieves r=0.386 (highest across all phases) but widens gap to -$312.5M. Transfers are real flows Schwab counts; they are timed differently. VARIABLE TIMING (std=21.8d) confirms event-driven, not rule-correctable. |

---

### 4. Investigation Ceiling Assessment

**All achievable correlations across Phases 1-3b:**

| Phase | Config | pearson_r | sign_agr | Total gap | Deployable? |
|-------|--------|-----------|----------|-----------|-------------|
| Baseline (production) | aua_t1p00 + vel_w90_t1p00 | 0.175 | 10/13 | -$119.8M | — |
| Phase 2 best | aua_t1p50 + vel_w120_t2p00 | 0.271 | 10/13 | -$174.9M | Yes |
| Phase 3 best | ef_no_transfers | 0.386 | 7/13 | -$312.5M | No (gap widens, sign_agr collapses) |
| Phase 3b monthly lag | L=-3 shift | 0.418 | 12/13 | -$96.9M | No (requires Schwab TOA dates) |

**Operational ceiling (deployable without new data): r=0.271**

The PRD target of r≥0.50 is **not reachable with current data**. The Transfer/ACAT timing
mismatch (std=21.8d per month) is the dominant structural barrier. No filtering, deduplication,
cap tuning, or date-offset rule closes this gap — it requires Schwab's actual TOA recognition
event dates for each Transfer In/Out transaction.

The best non-Transfer correlation (ef_no_transfers, r=0.386) confirms transfers are the noise
source, but excluding them widened the gap by $187.8M, which means Schwab does count
Transfer flows in their NNA. The problem is purely one of recognition timing.

---

### 5. Production Recommendation Package

**Immediately actionable (bundled single gold rebuild):**

| Change | Impact | Status |
|--------|--------|--------|
| Cap tuning: aua_t1p50 + vel_w120_t2p00 | +0.096 pearson (0.175→0.271), sign_agr maintained 10/13 | Validated in Phase 2 |
| Settlement date: use settle_date where non-null | +1 sign_agr (10→11), -$5.7M gap, near-zero rebuild cost | Validated in Phase 3 |
| JNL/sweep canonical fix (9bfb289b + b4f2d7a7) | Corrects description-based sweep exclusions | Committed — awaiting CEO go/no-go |
| ACAT integration (ONBOARDING_DAYS=30, BURST=3, MIN=0) | +$45.98M gap reduction | Validated — awaiting CEO go/no-go |

A single gold rebuild window can incorporate all four if CEO go/no-go is received. Running
two separate rebuilds (cap tuning now, ACAT later) costs ~145 min × 2 = ~5 hours. Wait for
CEO gate to bundle.

**Requires new data (cannot implement now):**

| Change | Requirement | Impact (theoretical) |
|--------|-------------|----------------------|
| TOA recognition date alignment | Schwab TOA event date feed per Transfer | r=0.418 at L=-3 (if all months aligned) |
| BI NNA cross-validation | BI parquet extraction from BD BI system | Definitional gap quantification only |

---

### 6. COO Memo Written

**File:** `docs/briefs/coo-memo-nnavar-investigation-complete.md`

Covers: investigation arc (Phase 1-3b), verdict per hypothesis, ceiling (r=0.271 operational,
r=0.418 theoretical with Schwab data), production recommendation bundle, Phase 4 options.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| ef_contribution_only is identical to production — external_flow hypothesis rejected | BD tags all Transfer rows at 100% coverage; there are no "internal transfers with blank external_flow" to filter out. The hypothesis assumed incomplete tagging; data disproves it. |
| Settlement date included in production bundle despite near-zero pearson gain | Marginal cost in a rebuild (+0 lines changed in script 05); +1 sign_agr is a real improvement worth taking. |
| Do not recommend ef_no_transfers for production | r=0.386 is the single highest correlation found, but gap widens by $187.8M and sign_agr drops to 7/13. A metric regression of this magnitude is not acceptable. |
| Operational ceiling set at r=0.271 | Every structural hypothesis tested with available data is exhausted. No further diagnostic script will improve this without Schwab TOA data. |
| PRD target (r≥0.50) flagged as unachievable with current data | This is a COO/CEO finding, not a DS decision. Documented for COO to escalate. |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| Investigation synthesis + Phase 4 options | `docs/briefs/coo-memo-nnavar-investigation-complete.md` | 2.0.0_SA_COO |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-03-06/nnavar_phase3_synthesis_and_investigation_ceiling.md` | This session log | No — pending commit |
| `docs/briefs/coo-memo-nnavar-investigation-complete.md` | COO investigation synthesis memo | No — pending commit |

---

## Blockers

None. Investigation is complete with available data. Phase 4 decisions belong to COO.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

ADVI_NNAVAR investigation is complete across Phase 1 (gap decomposition), Phase 2 (cap tuning,
31 variants), Phase 3 (structural: external_flow + settlement + bi_crossval), and Phase 3b
(timing shift: monthly_lag + day_shift). Operational ceiling is r=0.271 (deployable) and
r=0.418 (theoretical, requires Schwab TOA dates). External flow filtering is a null finding.
Settlement date is marginal. Transfer timing is VARIABLE (std=21.8d) — the dominant structural
barrier — and is not correctable by any rule available in current data. PRD target of r≥0.50
is not achievable without Schwab TOA event data. Production bundle (cap tuning + settlement +
canonical + ACAT) ready to deploy as a single gold rebuild pending COO authorization and CEO
go/no-go on JNL/ACAT changes.

---

## Next Steps

1. **[2.0.0_SA_COO] Review** `docs/briefs/coo-memo-nnavar-investigation-complete.md` — decision
   needed on (a) PRD target reassessment, (b) Schwab TOA data request, (c) gold rebuild
   authorization window

2. **[2.0.0_SA_COO / CEO] Go/no-go on JNL/sweep canonical fix + ACAT** — commits
   9bfb289b + b4f2d7a7 + ACAT params (30/3/0); needed to bundle into single rebuild

3. **[0.4.0_DT_ClientPlatform] Gold rebuild** — once COO authorizes the bundle, DT rebuilds
   gold with all confirmed changes in a single `05_build_client_performance.py` run

**Files to touch next (DS):**
- None until COO responds. Investigation is exhausted.

**Do NOT:**
- Design further diagnostic scripts without new data (Schwab TOA or BI data)
- Deploy cap parameter changes to production script 05 without COO rebuild authorization
- Implement any date offset rule on Transfer In/Out in production (VARIABLE TIMING confirmed)
- Push any commits (DT handles all pushes)
