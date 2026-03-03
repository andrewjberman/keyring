# ADVI Task Order Re-issue — 1.0.0_SA_CTO

**Date:** 2026-03-03
**Start Time:** session continuation
**End Time:** session end

## Objective

Audit the existing ADVI task orders and alignment threads, identify quality failures
in ADVI-001/002/003 (gpt-4o, pre-enrichment, low-quality contracts), deprecate them,
and re-issue the full task order set properly: COO re-run instructions + immediate
unblocked task orders for DS/DE/RD.

---

## Work Completed

### 1. Thread Quality Audit

Read all 3 ADVI thread receipts. Identified failures:

| Thread | Issue |
|--------|-------|
| ADVI-001 (continuous NNA + CLA) | colorMap placeholders ("#green", "#color1"); geo_drill missing from cla_timeseries; NMNC/NMEC 12-month window assumed, not verified vs header_metrics.json |
| ADVI-002 (stacked bar + rolling) | DS did not read script 10; inflows/outflows feasibility not verified; contracts generated from memory |
| ADVI-003 (Books design) | books_tab_design_brief.md was never written to disk; primary thread deliverable absent |

All 3 ran with gpt-4o before pod prompt enrichment. Turns completed in ~30-60 seconds.
Contracts are plausible but unverified. Superseded.

### 2. ADVI.json Updated

ADVI-001/002/003 marked `"status": "superseded"` with `superseded_by` and
`superseded_reason` fields. Thread counter remains at 3 — new runs will be ADVI-004/005/006.

### 3. Monolithic Task Orders Deleted (git rm)

All 4 `advisor_intelligence_completion.md` files removed:
- `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/`
- `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/`
- `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/`
- `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/`

These referenced deleted staging scripts, lacked thread serial metadata, and bundled
all streams into one file.

### 4. COO Task Order Issued

`org/tier1_exec/2.0.0_SA_COO/task_orders/advi_rerun.md`

Covers:
- Phase 0: O3 pre-flight (wait for first session logs from DS/DE/RD)
- ADVI-004 staging spec (replaces ADVI-001): full M1 context file list, M4 briefing with 3 specific gaps to resolve, opening message instructions
- ADVI-005 staging spec (replaces ADVI-002): script 10 source read requirement, inflows/outflows feasibility gate
- ADVI-006 staging spec (replaces ADVI-003): advisor-publisher + gold scripts injected, design brief file as mandatory deliverable
- Post-receipt task order requirements: 10 files split by thread serial
- Sequencing: ADVI-004 and ADVI-005 in parallel; ADVI-006 after deeper O3 signal

### 5. Immediate Unblocked Task Orders Issued

7 task orders covering streams with no thread dependency:

| File | Agent | Stream |
|------|-------|--------|
| `advi_a4_bell_curve_verify.md` | DS | A4: script 09 bell curve verification |
| `advi_a5_users_v2_mapping.md` | DS | A5: opal-users-v2 advisor identity investigation |
| `advi_i2_leaderboard_sort.md` | DE | I2: leaderboard sort stability |
| `advi_c1_geo_continuous.md` | RD | C1: GEO continuous NNA search + drill |
| `advi_c3_cla_snapshot.md` | RD | C3: CLA snapshot two-color redesign |
| `advi_h_portal_primitives.md` | RD | H: AdvisorsTab portal primitives refactor |
| `advi_i_top_performers.md` | RD | I: Top Performers visual redesign |

All issued as `2.0.0_SA_COO` (COO decomposes the PRD), committed by CTO.
No thread prefix — these streams don't trace to an alignment thread.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Supersede ADVI-001/002/003 rather than patch | Thread receipts are too low-quality to serve as binding contracts; faster to re-run with correct model and enriched prompts than to document all gaps |
| Delete monolithic task orders | Referenced deleted staging scripts; no thread serial metadata; bundling all streams in one file makes tracking impossible |
| 7 immediate task orders cover unblocked streams now | DS/DE/RD need work to start immediately; their first session logs satisfy O3 for the re-run threads |
| ADVI-006 runs after deeper O3 signal | Books is the most complex thread; DS/DE/RD need multiple sessions before they have the depth to produce a useful design brief |
| COO owns post-receipt task order issuance | CTO does not know what the new contracts will say; only COO reads receipts and writes downstream task orders |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/projects/ADVI.json` | ADVI-001/002/003 marked superseded with reasons | Yes |
| 4 x `advisor_intelligence_completion.md` | Deleted via git rm | Yes |
| `org/tier1_exec/2.0.0_SA_COO/task_orders/advi_rerun.md` | Created | Yes |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/advi_a4_bell_curve_verify.md` | Created | Yes |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/advi_a5_users_v2_mapping.md` | Created | Yes |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/advi_i2_leaderboard_sort.md` | Created | Yes |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/advi_c1_geo_continuous.md` | Created | Yes |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/advi_c3_cla_snapshot.md` | Created | Yes |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/advi_h_portal_primitives.md` | Created | Yes |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/advi_i_top_performers.md` | Created | Yes |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

ADVI task order system is now correctly structured. ADVI-001/002/003 deprecated in ADVI.json.
4 monolithic task orders deleted. COO has `advi_rerun.md` with full staging specs for
ADVI-004/005/006 and post-receipt task order requirements. 7 immediate task orders issued
to DS/DE/RD covering all unblocked streams (A4, A5, I2, C1, C3, H, I).

Execution sequence: DS/DE/RD activate on immediate task orders -> write first session logs
-> COO detects O3 satisfied -> COO runs ADVI-004 and ADVI-005 in parallel ->
COO reads receipts -> COO issues split task orders per thread -> cycle continues through
ADVI-006 (Books) and downstream deploy streams.

---

## Next Steps

1. **Push to remote** -- `git push origin CLOUD` when DT is ready
2. **Wave 6: architecture_brief.xml** -- CTO core document synthesis, now unblocked
3. **Monitor ADVI execution** -- on session start, read ADVI.json and agent session logs

**Do NOT:**
- Run ADVI-004/005/006 before O3 is satisfied (no agent session logs = low-signal thread)
- Write post-receipt task orders before reading the actual receipt — the receipt is the contract
- Commit `response.json`, `response2.json`, `.tmp_sandp_feb23.json`, or `tfplan` files
