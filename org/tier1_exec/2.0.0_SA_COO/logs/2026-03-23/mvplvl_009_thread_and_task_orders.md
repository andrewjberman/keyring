# MVPLVL .009 Thread Orchestration + Task Order Issuance -- 2.0.0_SA_COO

**Date:** 2026-03-23

## Objective

Run full thread orchestration for ADVI_MVPLVL .009 (Mix + Composition views broken at all drill levels). Andrew requested decisive execution with end-to-end parties: AE, DS, DE, RD. No corners cut.

---

## Work Completed

### 1. Startup Audit

Read all agent logs, project JSONs, registry. CTO had already updated delivery_status.md, REGISTRY.md, and project JSONs for GLDPRE/BKSCMP/CLSPT2 closures. DT deployed portal-v2.1.17 today with CI pipeline + MixTimeseriesPanel 4-class fix. No stale documents found -- 0 corrections needed.

### 2. Thread ADVI_MVPLVL-006: 4-Party E2E Trace

Ran Pattern 0 alignment thread with all 4 agents:
- **Participants:** DS (0.4.0), AE (0.6.0), DE (0.4.0), RD (0.4.2)
- **Model:** gpt-5.2
- **Turns:** 10 (3 max per agent x 4 agents, converged after DS + AE converged)
- **Tools:** ENABLED (M1 compliant: 9 source files + .009 task order injected)

**Thread diagnosed root cause (unanimous):**

| # | Breakpoint | Component | Owner |
|---|-----------|-----------|-------|
| 1 | Books tab uses local fetchComposition() that silently returns null on non-200, bypassing canonical API client | ClientsTab.tsx | DE |
| 2 | Missing getBooksAdvisorComposition() endpoint function | advisor-intelligence.ts | DE |
| 3 | Cash displayed as separate label instead of merged into Other | PartnerAnalytics.tsx + ClientsTab.tsx | DE + RD |
| 4 | L3/L4 per-class Other not computed in ConsolidatedOverviewPanel | ClientsTab.tsx | DE |
| 5 | L3/L4 backend only returns top-10 global (design limitation) | Lambda handle_books_composition | DESIGN DECISION |

**Bonus finding:** AE flagged advisor mix-timeseries S3 key bug (mix.json vs mix_timeseries.json). Separate from broken views.

**All agents agreed:** Backend (Lambda + gold scripts) is correct. Break is frontend wiring + display normalization. HTTP verification needed to rule out missing S3 artifacts but frontend fixes are required regardless.

### 3. Task Order Issuance

### Task Order Dispatch

| Agent | Task Order Path | Summary |
|-------|----------------|---------|
| 0.4.0_DS_ClientPlatform | org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_MVPLVL.009-ds.verify-s3-data.md | Verify gold layer S3 artifacts exist and are well-formed (from thread ADVI_MVPLVL-006) |
| 0.6.0_AE_PartnerETL | org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_MVPLVL.009-ae.verify-lambda-routes.md | Verify Lambda routes return 200; fix advisor mix-timeseries S3 key bug; gold rerun if 404 (from thread ADVI_MVPLVL-006) |
| 0.4.0_DE_ClientPlatform | org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_MVPLVL.009-de.api-wiring-normalization.md | Fix API client wiring + cash-to-other normalization + L3/L4 per-class Other (from thread ADVI_MVPLVL-006) |
| 0.4.2_RD_AdvisorIntelligence | org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_MVPLVL.009-rd.mix-rendering-normalization.md | Fix PartnerAnalytics.tsx Mix stacked bar cash-to-other rendering (from thread ADVI_MVPLVL-006) |
| 0.4.0_DT_ClientPlatform | org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_MVPLVL.009-dt.deploy-and-merge.md | QA gate + portal DEV push + PROD merge + CI deploy; optional Lambda deploy (from thread ADVI_MVPLVL-006) |

Execution dependencies:
  DS + AE (parallel, Phase 1: verify data exists)
       |
       v
  DE + RD (parallel, Phase 2: fix frontend wiring + rendering)
       |
       v
  DT (Phase 3: QA + push + deploy)

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| 4-party thread (not 2 or 3) | Andrew requested full E2E with all parties. Thread confirmed this was correct -- each agent contributed unique diagnostic signal. |
| L3/L4 per-class Other: accept frontend approximation for now | Thread consensus: backend only returns top-10 global for relationship/account. Exact per-class top-9 would require backend enhancement. Ship wiring + normalization first, revisit if CTO requires exact. |
| Cash merged into Other at display layer, not backend | Task order constraint explicit: no Cash label. Backend correctly includes cash as data. Frontend normalizes for display. |
| Separate DE/RD file ownership to avoid merge conflicts | DE owns ClientsTab.tsx + advisor-intelligence.ts. RD owns PartnerAnalytics.tsx only. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| org/threads/staging/run-ADVI_MVPLVL-006-mix-composition-e2e-trace.sh | Thread staging script | No -- local only |
| org/threads/ADVI_MVPLVL-006-mix-and-composition-e2e-trace----broken/ | Thread folder (10 messages + receipts) | No -- local only |
| org/projects/ADVI_MVPLVL.json | Updated phase + thread status | No -- local only |
| org/projects/REGISTRY.md | Updated MVPLVL row | No -- local only |
| org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_MVPLVL.009-ds.verify-s3-data.md | New task order | No -- local only |
| org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_MVPLVL.009-ae.verify-lambda-routes.md | New task order | No -- local only |
| org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_MVPLVL.009-de.api-wiring-normalization.md | New task order | No -- local only |
| org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_MVPLVL.009-rd.mix-rendering-normalization.md | New task order | No -- local only |
| org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_MVPLVL.009-dt.deploy-and-merge.md | New task order | No -- local only |

---

## Blockers

None. All task orders are issuable. No agent is blocked.

---

## Current State

> **Primary handoff point.**

**Status:** COMPLETE (thread + task orders issued)
**Active branch:** `CLOUD`

Thread ADVI_MVPLVL-006 completed with 10 turns across 4 agents (DS, AE, DE, RD). Root cause diagnosed as frontend wiring (local fetchComposition in ClientsTab.tsx) + cash-to-other display normalization. 5 task orders issued to DS/AE/DE/RD/DT covering Phase 1 verification, Phase 2 portal fixes, and Phase 3 deploy. All task orders reference the thread receipt. The CTO's original .009 task order to DE remains as the master brief; the COO task orders decompose it into per-agent deliverables with explicit dependencies.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Verify S3 artifacts** -- curl the 3 endpoints, report HTTP status + body shape
2. **[0.6.0_AE_PartnerETL] Verify Lambda routes return 200** -- if 404, run gold rerun on EC2; also fix advisor mix-timeseries S3 key
3. **[0.4.0_DE_ClientPlatform] Fix ClientsTab.tsx wiring + normalization** -- remove fetchComposition, add advisor composition endpoint, implement normalizeMixTo4Class, fix L3/L4 per-class Other
4. **[0.4.2_RD_AdvisorIntelligence] Fix PartnerAnalytics.tsx Mix rendering** -- merge cash into Other in stacked bar
5. **[0.4.0_DT_ClientPlatform] QA + deploy** -- push portal DEV, merge PROD, CI pipeline; optional Lambda deploy

**Do NOT:**
- Assume data is missing without HTTP verification (gold rerun was 2026-03-20)
- Add "Cash" as a separate label anywhere in the UI
- Have RD modify ClientsTab.tsx (DE owns that file for .009)

---

## Addendum: Phase 1 HTTP Findings + AE Task Order Revision

**Timestamp:** 2026-03-23 (same session, after AE began Phase 1 verification)

### Critical Finding

AE Phase 1 HTTP verification revealed ALL 4 endpoints return **500** (`Runtime.ImportModuleError: No module named 'etf_classifier'`). The Lambda is completely non-functional -- not just the two target views but ALL routes.

**Root cause:** The deployed Lambda zip contains a dummy stub `etf_classifier.py` (11 lines, no `classify()` method) instead of the real DynamoDB-backed `ETFClassifier`. The Lambda imports `etf_classifier` at module level (line 63), so the stub causes immediate import failure on every cold start.

**Why this happened:** `lambda-source-map.json` listed `etf_classification.py` (the 44KB Yang hardcoded dict module -- unrelated to BD classification) but NOT `etf_classifier.py` (the DynamoDB-backed classifier). The build script packages only what the source map lists.

**Classifier confusion clarified:**

| File | What it is | Relevance |
|------|-----------|-----------|
| `etf_classifier.py` (dummy stub, 11 lines) | Empty skeleton with no classify() | BROKEN -- must be replaced |
| `data/black_diamond/scripts/gold/lib/etf_classifier.py` (134 lines) | Real DynamoDB-backed ETFClassifier. Scans bd-securities on cold start, O(1) classify() after. Used by gold scripts 06b + 12. | THE ONLY CLASSIFIER THAT MATTERS |
| `etf_classification.py` (44KB) | Yang pipeline hardcoded dict system. Pre-dates DynamoDB. | IRRELEVANT to BD. Dead weight in zip. |

**S3 artifacts confirmed present and valid** -- gold rerun 2026-03-20 was successful. firm_mix_views.json, firm_composition.json, advisor composition/mix files all exist with correct shapes.

### AE Task Order Revised

**Path:** `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_MVPLVL.009-ae.verify-lambda-routes.md`

**Changes:**
- Objective rewritten to reflect 500 root cause (dummy stub) instead of speculative verification
- Requirement 1 (NEW): Copy real ETFClassifier from `data/black_diamond/scripts/gold/lib/etf_classifier.py` into Lambda source, replacing the dummy stub
- Requirement 2: Source map fix (etf_classifier.py must be in files array)
- Requirement 3: Advisor mix-timeseries S3 key fix (unchanged)
- Requirement 4: Commit + rebuild artifact (build-and-upload.sh)
- Requirement 5: Post-deploy re-verification (after DT applies Terraform)
- Added explicit constraint: do NOT use etf_classification.py (Yang hardcoded dicts) for BD classification

### Impact on Dependency Chain

This changes the picture. The Lambda is fully broken, so:
- **DE/RD portal fixes are still required** (wiring + normalization) but they cannot be visually verified until DT deploys the fixed Lambda
- **DT deploy is now BLOCKING** -- must happen before any visual confirmation of the frontend fixes
- Revised chain: AE commit + rebuild -> DT deploy Lambda -> DE/RD verify frontend rendering

### Execution Order (revised)

```
AE (fix etf_classifier + source map + mix_timeseries key + rebuild artifact)
     |
     v
DT (terraform apply partners-api -> verify 0-diff -> tag -> push)
     |
     v
DE + RD (portal fixes, now visually verifiable)
     |
     v
DT (push portal DEV -> PROD merge -> CI deploy)
```

---

## Addendum 2: DS Phase 1 Findings + Both Task Orders Revised

**Timestamp:** 2026-03-23 (same session, after DS completed S3 verification)

### DS Findings (3 issues, 1 fixed by DS)

| # | Severity | Issue | Status |
|---|----------|-------|--------|
| 1 | HIGH | Script 12 on EC2 is pre-ETFClassifier (produces `structured_notes` instead of `alternatives`). Repo version correct (5c6fd9d0) but never deployed to EC2. | AE must redeploy |
| 2 | HIGH | 06b advisor IDs used raw display names (`Josh Henson/`) while 12 uses snake_case (`josh_henson/`). Lambda serves both using same path param -> one format always 404s. | FIXED by DS: f6a4b5b8 |
| 3 | MEDIUM | firm_mix_views.json has only 1 period per granularity (incremental run had no new data). Needs full rebuild. | AE full rebuild |

S3 artifacts confirmed present with valid JSON. The gold rerun 2026-03-20 produced files, but with stale scripts.

### Task Order Revisions

**DS task order** (`org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_MVPLVL.009-ds.verify-s3-data.md`):
- Revised to acknowledge DS exceeded scope (fixed 06b, committed f6a4b5b8)
- Verification requirements marked COMPLETE
- Added Req 4: post-rebuild re-verification (after AE gold rebuild)
- Removed stale constraint "Do NOT modify any gold scripts" (DS already did, correctly)

**AE task order** (`org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_MVPLVL.009-ae.verify-lambda-routes.md`):
- Added Track B (EC2 gold script deploy + full rebuild): Requirements 6-8
- Req 6: Deploy repo versions of 06b (f6a4b5b8) + 12 (5c6fd9d0) to EC2 via safe-ec2-deploy.sh
- Req 7: Run FULL gold rebuild (not incremental) to fix taxonomy + advisor IDs + date range
- Req 8: Verify regenerated artifacts (no structured_notes, full date range, snake_case paths)
- Track A (Lambda) marked DONE (Req 1-4 complete, Req 5 pending DT deploy)
- Added DS as completed dependency

### Revised Execution Order

```
AE Track A (Lambda fix) -----> DT (terraform apply) -----> AE (verify 200s)
       DONE                                                       |
                                                                  v
AE Track B (EC2 deploy + gold rebuild) -----> DS (re-verify artifacts)
                                                        |
                                                        v
                                              DE + RD (portal fixes, now verifiable)
                                                        |
                                                        v
                                              DT (push portal DEV -> PROD -> CI)
```

Lambda deploy and gold rebuild can proceed in parallel. Both must complete before frontend can be visually verified.
