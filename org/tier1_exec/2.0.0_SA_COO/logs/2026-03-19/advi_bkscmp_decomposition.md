# ADVI_BKSCMP Decomposition — 2.0.0_SA_COO

**Date:** 2026-03-19

## Objective

Decompose CTO's ADVI_BKSCMP PRD into 4 task orders for DS, RD, DT, and AE.
Pre-flight verification completed on all key source files before writing task orders.

---

## Pre-Flight Verification Results

| Check | Finding |
|-------|---------|
| ClientsTab.tsx:383 handleSelectAdvisor | CONFIRMED: `name.toLowerCase().trim().replace(/[^a-z0-9_]+/g, '_').replace(/^_+|_+$/g, '') \|\| 'unknown'` |
| ClientsTab.tsx:875-884 composition block | CONFIRMED: exact lines match PRD §WS3b target |
| showFilteredOther render | CONFIRMED: lines 1039-1050 (to be removed) |
| showOther render | CONFIRMED: lines 1055-1068, uses `composition.concentration.other.pct` |
| Empty state at 1073 | CONFIRMED: `allItems.length === 0 ? 'No holdings data at this level'` |
| Lambda routing line 1222 | CONFIRMED: `elif action == 'composition': return handle_books_composition(...)` routes ALL entity types |
| Lambda handle_books_composition | CONFIRMED: exists at line 829, handles firm via in-Lambda computation, L3/L4 works today |
| Lambda version | CONFIRMED: 2.7 (current); target 2.8 |
| run_gold_layer.sh incremental 08b position | CONFIRMED: line 114, immediately followed by 06b at line 115 |
| run_gold_layer.sh full 08b position | CONFIRMED: line 158, immediately followed by 06b at line 159 |
| pipeline-complete.json write | CONFIRMED: at line 175, after all scripts -- does not affect script 12 |

**Key deviation from PRD description:**
PRD §WS2-E describes routing as "add composition dispatch for firm and advisor."
Actual Lambda already dispatches composition for all entity types to `handle_books_composition`.
DS must SPLIT the routing: firm/advisor → new S3-proxy handlers; relationship/account → keep existing.
This is documented explicitly in task order BKSCMP.001 req 5.

---

## Task Order Dispatch

| Agent | Task Order Path | Summary |
|-------|----------------|---------|
| 0.4.0_DS | org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_BKSCMP.001.ds-script12-lambda-routes.md | Write script 12 + run_gold_layer.sh update (WS1) + Lambda v2.8 handlers + routing split (WS2). Two commits. |
| 0.4.2_RD | org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_BKSCMP.002.rd-types-holdings-adapter.md | Extend types.ts + schema-adaptive holdings block in ConsolidatedOverviewPanel (WS3). Parallel, no gate. |
| 0.4.0_DT | org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_BKSCMP.003.dt-lambda-deploy.md | Deploy opal-partners-data v2.8 → partners-api-v1.5.0 (WS4 Lambda). Gates on DS WS2 commit. |
| 0.6.0_AE | org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_BKSCMP.004.ae-ec2-gold-run.md | Upload script 12 + run_gold_layer.sh to S3; run incremental gold layer; verify artifacts (WS4 EC2). Gates on DS WS1 commit. |

Execution dependencies:
  DS WS1 commit → AE (upload + gold run)
  DS WS2 commit → DT (Lambda deploy)
  RD (parallel, no gate)
  AE gold run + DT deploy → artifacts live and serveable → RD portal changes visible

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| AE runs incremental, not full | holdings_lots is available in incremental mode; script 12 reads latest partition regardless of run mode. Full mode not needed and is slower (60-90 min vs 15-30). |
| DS commits WS1 (script 12) and WS2 (Lambda) separately | AE and DT have different gates; batching would force one to wait on the other unnecessarily. |
| RD parallel track | Frontend adapter is backward-compatible: when Lambda returns 404, falls through to synthesizeFrom* exactly as today. |
| Lambda routing split (not new handler replacing old) | `handle_books_composition` for relationship/account is working and must not be touched. Only the firm/advisor composition routing is redirected to new S3-proxy handlers. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| org/projects/ADVI_BKSCMP.json | Phase updated: decomposition complete, 4 TOs issued | No |
| org/projects/REGISTRY.md | ADVI_BKSCMP row updated | No |
| org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_BKSCMP.001.ds-script12-lambda-routes.md | New task order | No |
| org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_BKSCMP.002.rd-types-holdings-adapter.md | New task order | No |
| org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_BKSCMP.003.dt-lambda-deploy.md | New task order | No |
| org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_BKSCMP.004.ae-ec2-gold-run.md | New task order | No |

---

## Current State

**Status:** COMPLETE

Task orders issued. Pending commit of all COO session work.

## Next Steps

1. **[2.0.0_SA_COO] Commit** all COO session work: startup corrections + session logs + BKSCMP task orders + project JSON + registry updates.
2. **[0.4.0_DS] Execute BKSCMP.001** — script 12 + Lambda v2.8 (no gate; start immediately).
3. **[0.4.2_RD] Execute BKSCMP.002** — types + holdings adapter (no gate; start immediately).
4. **[0.4.0_DE] Execute MVP318.004** — WS3e advisor types + WS5 chart windows (gate cleared: partners-api-v1.4.0 live).
5. **[0.6.0_AE] Execute MVP318.003** — FULL gold run (gate cleared: bd-v2.19.0 live). Also note BKSCMP.004 incremental run is a separate follow-on.
6. **[2.0.0_SA_COO] Confirm WS6 gate** once DE MVP318.004 req 3 (chart windows) committed to portal DEV — then green-light DT for DEV->PROD merge.
