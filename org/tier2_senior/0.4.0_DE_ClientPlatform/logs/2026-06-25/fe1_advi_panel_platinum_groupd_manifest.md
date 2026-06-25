# FE1 — ADVI panel -> component -> platinum -> Group-D threaded manifest (per partner)

**archetype:** TRACE
**Serial:** 0.4.0_DE_ClientPlatform | **Date:** 2026-06-25 | **Window:** session start (spawn) -> 1530Z
**TO:** DATA_ANALYTICS.FE1 (complete @ e4a4539b5) | **Deliverable:** 98764fb65

## Summary
Spawned (Andrew-direct via COO) for DATA_ANALYTICS.FE1. Ran org/XXX.md startup (registered PID 28432,
persistent inbox Monitor task bmr2zoia5, read GO + TO). Produced the threaded MANIFEST: every visible
ADVI (AdvisorIntelligence) dashboard panel -> shared frontend component -> platinum artifact -> Group-D
producer script, threaded per partner (49F / Inflection / Cottonwood), divergences surfaced.

## Current State
- **Deliverable:** `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/DATA_ANALYTICS.FE1_advi_panel_platinum_groupd_manifest.md` @ 98764fb65 (159 lines). TO status->complete @ e4a4539b5.
- **Architecture established:** ADVI = ONE shared component tree (`portal/src/pages/AdvisorIntelligence/_shared/{tabs,panels,components,charts}`) selected per-partner by `_partners/{p}/layout.ts` (`TenantLayoutConfig`). Panels are common; per-partner divergence lives in layout.ts (enablement) + the producing pipeline (49F=BD `data/black_diamond/scripts/gold`, INF=Orion `data/inf/scripts/gold`, COT=BD-native `data/cot/scripts/gold`).
- **Bridge file:** `portal/src/api/endpoints/advisor-intelligence.ts` maps each component query fn -> platinum S3 key. Serving spine: component -> /api/scoped/advisor-intelligence/... -> CloudFront -> shared-advisor-router L@E (PPI-08, bucketSuffix 49financial->bd / inflection->inf / cottonwood->cot) -> s3://opal-data-{suffix}/platinum/... OR opal-partners-data Lambda (PII).
- **Producer grounding (authoritative):** `comp-platinum reverse` + `comp-pipescript io` confirm **D_04.client_portal_summary.py is the SINGLE platinum publisher for 49F & COT** (upstream D_00/D_00b/D_00c/D_01/D_00f write gold/artifacts/* intermediates D_04 republishes). **Inflection FANS OUT** across ~20 INF_D_0x publishers (partner_analytics from INF_09.generate_partner_analytics.py, not a D_01).
- **2 producer GAPS flagged (not omitted):** (4a) COT gold tree has NO D_00f.advisor_nna_canonical -> getAdvisorNnaCanonical(cottonwood) 404/empty; (4b) header_metrics_fresh.json is INF-origin (INF_D_00e) -> confirm 49F/COT canonical-fallback intent.
- **Rebuild input:** COT D_00c/D_02/D_03 = produced-but-frontend-unconsumed for COT v1 (Books/Advisors disabled) -> agnostic-drop candidates for canonize-gold lean rebuild.
- **Broker:** RAVC2 -> COO (20260625T153003Z); cc -> DS (20260625T153014Z). Status IDLE/available.

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| `pipescript --list` | estate | PASS | routed 3 partners -> advi-bd/advi-inf/advi-cot threads |
| `pipescript advi-bd / advi-inf / advi-cot` | partner backends | PASS | spine: producers->served->frontend; bd-gold-layer-pipeline + inf-gold-dispatch-ec2 + cot-pipeline = the gold->platinum chains |
| `comp-pipescript io` | D_00/D_00b/D_01/D_04 (bd), D_04 (cot) | PASS | grounded write targets; D_04 = sole platinum publisher (bd/cot) |
| `comp-platinum reverse` | timeseries_overview/cumulative_chart/header_metrics/leaderboard/dashboard/partner_analytics | PASS | authoritative producer fns (D_04::build_*); INF partner_analytics -> INF_09.generate_partner_analytics.py |
| `comp-transform schema-check` | PartnerAnalytics, DistributionTab | PASS | clean, no MISSING (DE mandate for data-rendering components) |
| `comp-to` | DATA_ANALYTICS.FE1 | PASS | race-free per-session TO_ID |

**What worked:** pipescript as the named-thread spine gave producers->served->frontend per partner with no silent Unknown; comp-platinum reverse resolved artifact->producing-fn authoritatively (caught the D_04 single-publisher vs INF fan-out shape divergence). **What failed:** `comp-platinum reverse partner_analytics_quarterly` (no `.json`) routed as FIELD query, no payload match — recovered by appending `.json` (artifact stem match) + an INF-tree producer-file grep (rail-checked inline: comp-platinum index is BD-scoped, needed the INF-tree file). **Gap found:** comp-platinum reverse is BD-pipeline-indexed; INF/COT producer resolution needs the per-tree gold dir (flagged for comp-platinum multi-pipeline coverage).

## Blockers
None. TO delivered. Downstream is event-gated (not blocked): CVO completeness/per-partner-correctness verify; DS A1 reconcile (§4 of manifest); 2 gap rulings (DS/CVO); CTO arch-gate folds into Schwab-raw-native portal-contract.

## Next Steps
- **[3.0.0_SA_CVO]** verify manifest completeness (every panel threaded, no silent Unknown) + per-partner correctness.
- **[0.4.0_DS_ClientPlatform]** reconcile FE-down (this) with A1 gold-up + Schwab-raw-native D-tier field-reqs into ONE portal contract; rule the 2 producer gaps (4a COT advisor_nna_canonical, 4b header_metrics_fresh).
- **[2.0.0_SA_COO]** on CVO verify + DS reconcile, fold into canonize-gold essential-vs-agnostic classification; NFRA_TSGRAPH.P2-1 still staged in my queue.
- **[0.4.0_DE]** IDLE/available — event-driven on the above + P2-1 if dispatched.
