# COO Session Log — 2026-03-06
## ADVI_NNAVAR + ADVI_AUAVAR Project Launch

**Agent:** 2.0.0_SA_COO
**Date:** 2026-03-06
**Session type:** Full org audit + two new ADVI project launches + thread execution + task order issuance

---

## Context

CTO issued handoff for two new ADVI projects: ADVI_NNAVAR (NNA Variance Optimization)
and ADVI_AUAVAR (AUA Variance Analysis). Session mandate:
  1. Full org audit: validate what is complete/pending by reading team logs and commits
  2. Update COO folder-level documentation (architecture_brief.xml, task orders)
  3. Run orchestrator threads for both new projects
  4. Issue task orders from thread receipts

---

## Org Audit — Findings

### Pod 0.4 (ClientPlatform)

#### 0.4.0_DS_ClientPlatform
Read all 2026-03-05 logs. Key findings:
- ACAT Phase 3 analysis COMPLETE (top-25 audit, sign flip confirmed, $45.98M recovery).
  Production design brief written: docs/briefs/data-scientist-acat-inkind-nna-production-design.md
- Param grid v2 analysis: diag_acat_param_grid.py rewritten (gold baseline), DT brief written.
  Grid executed by DT on 2026-03-05. CRITICAL FINDING: r=0.175 flat for all 24 combos
  including BASELINE_NO_ACAT. ACAT does not move correlation. Gap -$119.8M is structural.
- diag_acat_correlation_summary.py written but NOT YET RUN (awaiting EC2 DT execution).
- Canonical NNA fix (JNL/sweep exclusion): committed to scripts 05+05b
  (commits 9bfb289b+b4f2d7a7). Awaiting CEO go/no-go before gold rebuild.
- AUA Phase 1-5 investigation complete. Root cause identified.

#### 0.4.0_DT_ClientPlatform
Read all 2026-03-05 logs. Key findings:
- Param grid v2 EC2 run: COMPLETE. r=0.175 flat, results at
  s3://opal-data-bd/diagnostics/acat_param_grid_results.csv
- ACAT Phase 2 EC2 run: COMPLETE.
- Script 09 multi-granularity deploy: COMPLETE (KeyError hotfix included).
- YANGV2 Phase 3 portal push (9b902dc): NOT DONE. DT was occupied with ACAT/script09 work.
  This is still a P0 open item.

#### 0.4.0_DE_ClientPlatform
Read 2026-03-05 logs. Key findings:
- All 4 Phase 3 YANGV2 RD task orders: APPROVED. Portal DEV at 9b902dc.
- Task order audit: V1VERS 8/8 complete, YANGV2 8/9 complete (DT portal push pending).
- Y14 gap identified (no task order issued for advisorKey Books gating). Deferred to 49FNV3.

### Pod 0.3 (TradingOperations)

#### 0.3.0_DE_TradingOperations
Read 2026-03-05 logs. SSCN proxy routes committed (CLOUD 18fd997b):
  3 GET handlers added to lambda_function.py for security-scanner endpoints.
  Portal endpoint types updated (DEV 0c41aa6). Status: COMPLETE (code side).
  Pending: DT Lambda redeploy for opal-data-refresh-api.

#### 0.3.0_DT_TradingOperations
Read 2026-03-05 logs. SSCN wave 1+2 portal DEV push: COMPLETE.
AE deployed security-scanner-v1.0.0. deployment_map.xml updated.
opal-data-refresh-api Lambda redeploy: NOT DONE. Task order pending.

### COO Incoming Task Orders (stale — updated)
- advi_rerun.md: marked COMPLETE (all ADVI-004/005/006 work done, V1VERS 8/8, YANGV2 8/9).
- partner_identity_table.md: marked COMPLETE (J1 DynamoDB + J2/J3 portal-auth commits).

### Architecture Brief
Created architecture_brief.xml from scratch (did not exist).
  org/tier1_exec/2.0.0_SA_COO/deliverables/architecture_brief.xml
  Covers: org_health, active_projects (ADVI_NNAVAR, ADVI_AUAVAR, PFMG_VISPOL, SSCN_PORTAL),
  completed_projects (ADVI_V1VERS, ADVI_YANGV2), open_items (P0-P3), deployment_state.

---

## ADVI_NNAVAR Thread (ADVI_NNAVAR-001)

**Script:** org/threads/staging/run-ADVI_NNAVAR-001-nna-gap-decomposition.sh
  Bug fixed: OPENING_FILE heredoc unquoted ($1 unbound variable on $119.8M). Fixed to
  printf for frontmatter + single-quoted heredoc for body.

**Thread:** ADVI_NNAVAR-001-nna-gap-decomposition-param-grid-analysi
**Participants:** 0.4.0_DS_ClientPlatform (turns 1,3,5), 0.4.0_DT_ClientPlatform (turns 2,4,6)
**Result:** CONVERGE at turns 5+6.

### Receipt Summary

**ACAT parameters (production recommendation):**
  ONBOARDING_DAYS = 30
  BURST_THRESHOLD = 3
  MIN_ACAT_ESTIMATE = 0
  Rationale: Phase 3 validated methodology; 7-21 day windows add $12-22M but don't move r.

**New diagnostic script:** data/black_diamond/scripts/diagnostics/diag_nnavar_gap_decomposition.py
  Design: load gold spine (client_performance.parquet) for AUA + reload silver/transactions
  with toggles. No positions_cube scan.

**6 diagnostic suites (ordered):**
| Suite | Name | Variants | What It Measures |
|-------|------|----------|-----------------|
| 0 | baseline | baseline_current_gold | Starting r~=0.175, gap~=-$119.8M confirmed |
| 1 | exclusions | excl_none, excl_action_only, excl_action_plus_desc | Canonical JNL/sweep fix impact |
| 2 | dedup | dedup_txnid_only, dedup_composite_current, dedup_composite_plus_desc | Dedup aggressiveness |
| 3 | caps | cap_event_only, cap_event_plus_aua, cap_event_plus_aua_plus_velocity | Cap layer shape distortion |
| 4 | timing | month_last_date_delta, month_sum_daily_flows | Monthly boundary effects |
| 5 | coverage | rel_fallback_on, rel_drop_unmapped | Mapping gap impact |

**S3 output:** s3://opal-data-bd/diagnostics/nnavar/{run_date}/{suite}/
  Files: summary.csv, per-variant monthly_nna.csv + metrics.json, stdout.txt, run_manifest.json

**EC2:** i-01003b035d2988dfb (bd-gold-layer-runner), suite-per-invocation, SSM send-command
**Runtimes:** exclusions ~8-12 min, dedup ~10-15 min, caps ~8-15 min, timing/coverage ~2-6 min each

---

## ADVI_AUAVAR Thread (ADVI_AUAVAR-001)

**Script:** org/threads/staging/run-ADVI_AUAVAR-001-aua-gap-segment-alignment.sh
  Bug fixed: TOPIC variable contained $55M which expanded $5 as positional param
  (set -u flag). Fixed by single-quoting the TOPIC assignment.

**Thread:** ADVI_AUAVAR-001-aua-gap-segment-decomposition-bd-allocat
**Participants:** 0.4.0_DS_ClientPlatform (turns 1,3,5), 0.4.0_DT_ClientPlatform (turns 2,4,6)
**Result:** CONVERGE at turns 5+6.

### Receipt Summary

**$1.236B vs $1.545B reconciliation (gold-vs-gold):**
  - $1.236B = gold client_performance.parquet total_aua for 2026-03-02, from an older/incomplete
    gold build (fewer positions_cube partitions at time of Phase 1 run).
  - $1.552B = gold AUA from a newer build (script 09 dry-run log, more complete coverage).
  - Discrepancy is gold-vs-gold, not BD-vs-gold. Proven by running diagnostic for same date.

**Anchor date:** D = 2026-03-02

**New diagnostic script:** data/black_diamond/scripts/diagnostics/diag_aua_gap_decomposition.py
  Two-step design:
    Step 1: Gold-vs-gold reconciliation (client_performance vs positions_cube x canonical_prices)
    Step 2: BD-vs-gold segment decomposition waterfall

**4 segments:**
| Segment | Name | Classification |
|---------|------|----------------|
| 1 | Account coverage gap (A\B, A\C) | Addressable (if material) |
| 2 | Household aggregation integrity check | Addressable (bug) if non-zero |
| 3 | Cash treatment (diagnostic-only, no headline netting) | Explainable or Addressable (COO decision) |
| 4 | Account-level residual (pricing/holdings mismatch) | Investigate |

**JSON waterfall schema locked:**
  Keys: run_metadata, totals, coverage, segments, top_account_residuals, diagnostics

**COO decision gate:**
  Cash mask definition (allocations security_name + gold asset_name) must be confirmed
  before cash is netted from headline AUA totals. Currently diagnostics-only.

**EC2:** i-01003b035d2988dfb (bd-gold-layer-runner), S3 artifact model, SSM send-command
**Output paths:**
  s3://opal-data-bd/diagnostics/aua_gap_decomposition_2026-03-02.json
  s3://opal-data-bd/diagnostics/aua_gap_decomposition_2026-03-02_stdout.txt

---

## Task Orders Issued

### ADVI_NNAVAR
| ID | Agent | File | Status |
|----|-------|------|--------|
| ADVI_NNAVAR.001-DS | 0.4.0_DS_ClientPlatform | ADVI_NNAVAR.001-DS.write-gap-decomposition-script.md | pending |
| ADVI_NNAVAR.002-DT | 0.4.0_DT_ClientPlatform | ADVI_NNAVAR.002-DT.execute-gap-decomposition-suites.md | pending (blocked on .001-DS) |

### ADVI_AUAVAR
| ID | Agent | File | Status |
|----|-------|------|--------|
| ADVI_AUAVAR.001-DS | 0.4.0_DS_ClientPlatform | ADVI_AUAVAR.001-DS.write-aua-gap-diagnostic.md | pending |
| ADVI_AUAVAR.002-DT | 0.4.0_DT_ClientPlatform | ADVI_AUAVAR.002-DT.execute-aua-gap-diagnostic.md | pending (blocked on .001-DS) |

---

## Open Items Flagged to Andrew

| Item | Priority | Owner | Action Needed |
|------|----------|-------|---------------|
| YANGV2 Phase 3 portal push | P0 | 0.4.0_DT_ClientPlatform | Run ADVI_YANGV2.portal-push.phase3.md |
| NNA canonical fix go/no-go | P1 | Andrew/CEO | Approve JNL/sweep commits 9bfb289b+b4f2d7a7 for gold rebuild |
| SSCN opal-data-refresh-api Lambda | P2 | 0.3.0_DT_TradingOperations | Deploy Lambda (SSCN_PORTAL.001-002.push-and-deploy.md) |
| AUAVAR cash mask definition | P2 | Andrew/COO | Confirm non-cash AUA definition before Segment 3 goes into waterfall |

---

## Files Modified This Session

| File | Action |
|------|--------|
| org/tier1_exec/2.0.0_SA_COO/task_orders/advi_rerun.md | Updated status to complete |
| org/tier1_exec/2.0.0_SA_COO/task_orders/partner_identity_table.md | Updated status to complete |
| org/tier1_exec/2.0.0_SA_COO/deliverables/architecture_brief.xml | Created (new) |
| org/daily_log/2026-03-06.md | Created (new) |
| org/threads/staging/run-ADVI_NNAVAR-001-nna-gap-decomposition.sh | Created (new) + bug fixed |
| org/threads/staging/run-ADVI_AUAVAR-001-aua-gap-segment-alignment.sh | Created (new) + bug fixed |
| org/threads/ADVI_NNAVAR-001-* (full thread) | Created by orchestrator |
| org/threads/ADVI_AUAVAR-001-* (full thread) | Created by orchestrator |
| org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_NNAVAR.001-DS.write-gap-decomposition-script.md | Created (new) |
| org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_NNAVAR.002-DT.execute-gap-decomposition-suites.md | Created (new) |
| org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_AUAVAR.001-DS.write-aua-gap-diagnostic.md | Created (new) |
| org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_AUAVAR.002-DT.execute-aua-gap-diagnostic.md | Created (new) |
