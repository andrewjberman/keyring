# Session Log — D5 ORPHAN-AI domain calls (joint w/ DE, Andrew-directed)

**agent:** 0.4.2_RD_AdvisorIntelligence
**date:** 2026-06-12 (~2050Z–2100Z)
**archetype:** TRACE
**secondary_archetypes:** COORDINATE
**project:** NFRA_DEBTSCAN D5-FIX / PORTALSWEEP ORPHAN-AI cluster (DE-led, product-gated)
**status at close:** Domain calls delivered to DE (RAVC3, msg 20260612T205532Z). Deletion remains Andrew-confirm-gated; nothing committed to portal.

## 1. Mandate

DE (0.4.0_DE_ClientPlatform) ran the PORTALSWEEP AC6 orphan census: 11 AdvisorIntelligence `_shared` files with 0 live inbound at origin/DEV 73d2436a, de-wired in the multi-partner refactor 9423f71e. Andrew directed a joint determination: my product/roadmap call per item — ABANDONED vs PAUSED-WIP vs UNSURE — before DE's combined RAVC2 to COO.

## 2. Verdict: 11/11 ABANDONED, 0 PAUSED-WIP + 2 census corrections

Each call from the candidate's OWN evidence (per-file git archaeology + import trace + active-project/TO/PRD scan), not sibling-class transfer:

| Item | Call | Decisive evidence |
|---|---|---|
| AdvisorBookAccountDetail.tsx | ABANDONED | `accountDetailSlot` mechanism is LIVE but both live parents construct `<AdvisorBookAccountModal/>` into it (ClientsTab.tsx:702-744, AdvisorBookView.tsx:475). The `:57` docstring naming AccountDetail is stale pre-INFSHIP-P2 (fc6acc7a made the modal the L4). |
| ClientsTable.tsx | ABANDONED | Superseded by ClientListPanel (AdvisorBookView:51). Post-refactor touches mechanical only (SHARED.005 lint d9882117). |
| AUACompositionChart.tsx | ABANDONED | v1-era (162c44fd), superseded by PartnerAnalytics multi-view donut. |
| AssetIntelligenceTab.tsx | ABANDONED | Known-legacy since v5 tab nav (in role docs + page inventory since April pod audit); no revival in any TO/PRD. |
| FeeRoleBreakdownPanel.tsx | ABANDONED | REBORN .007 L2 fee view, superseded by NNAFEE fee-efficiency views; CanonicalBookView imports FeeEfficiencyPanel (:32). |
| DimensionSelector / MetricSelector / HeaderMetrics | ABANDONED x3 | v1-era; cohort/metric selection now inline in DistributionTab; HeaderMetrics superseded by PartnerAnalytics. Only grep hit elsewhere is the `getHeaderMetricsFresh` substring (endpoint, not component). |
| 3 barrels (ClientDetail/index, ClientDetail/panels/index, inflection/overrides/index) | ABANDONED x3 | 0 importers; live consumers import direct paths (FidelityCustodianBar via './overrides/...' in inflection/index.tsx:22 + layout.ts:10). |

**Census corrections surfaced to DE:**
1. **AUATrendChart is NOT a live sibling** — sole importer is AssetIntelligenceTab.tsx:15, itself on the orphan list (orphan→orphan; recommend it JOINS the delete list → 12). Same class as the banked gold-tree orphan→orphan pattern.
2. **Whole `_shared/ClientDetail/` subtree appears 0-inbound** (ClientDetailPage zero refs; the 5 panels zero outside-subtree importers — TimeSeriesPanel matches elsewhere are comments about a different, already-SHARED.007-deleted inline component). Old pre-AdvisorBook* client drill. Handed to DE for census-tooling verification + fold-in.

Roadmap check: active ADVI projects = COTETL/COTSNP/HISTBF/PRTORG; PRTORG's mentions (PRTORG.md:79-81) are a directory-listing description, not work intent. REBORN complete.

## 3. My follow-ups (post Andrew-confirm deletion)
- Fix stale `:57` docstring in AdvisorBookClientDetail.tsx (live file, my lane) in the deletion change window.
- Update `page_inventory.xml` — it is stale at April pre-`_shared` vintage (still describes AccountDetail as live L4, ClientsTable at L2); needs a re-audit pass regardless of this deletion.

## 4. Compiler Tools

| Tool | Result |
|------|--------|
| (none run) | DE owned the mechanical census (his AC6 tooling + tsc/vite proof); my lane was domain verification via per-file git archaeology + targeted import-trace greps against DE's already-established 0-inbound claims — no component modified, no data-rendering change, so the RD `comp-transform fields` minimum does not apply. |
