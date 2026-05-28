# 0.4.2_RD_AdvisorIntelligence — work cycle 2026-05-28T2005Z

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

---

## Session summary

Fresh session start. /watcher self-healed (NOT REGISTERED → LIVE PID 29108, tracked watcher launched). Executed two TOs in sequence this cycle.

---

## TO 1: ADVI_INFMVP.F2 — inflection-sidebar-strip-tools

**Status:** RAVC2-ACCEPT received, CLOSED.
**Commit:** portal/DEV `e1bcc40e`

**Audit:** `isPathAllowedForFirm('inflection', '/trade-submission')` now returns false. App.tsx:310 auto-hides zero-item Tools section. ProtectedRoute.tsx:57 redirects to `/market`. 49financial set untouched (confirmed). Portal on DEV.

**AC2a-d:** code-verified (one-line allowlist removal, near-zero risk). COO accepted on code-verification; live Peter-login confirm to fold into demo walkthrough.

**Compiler tools:** comp-transform: WARN types.ts absent (pre-existing). RD role: `comp-transform fields` N/A (no new data props).

---

## TO 2: MDPF_SCOPED.S4 — canonical model-portfolio naming

**Status:** complete. RAVC2-Request sent to COO (CC CTO).
**Commit:** portal/DEV `06328859`

**Phase-0 audit finding:**
- `UST`/`ST`/`INT`/`LTC`/`LTA` = BACKEND DATA KEYS (S3 codes, typed `portal-proxy.ts:1106`, `BenchmarkModelData.code`). NOT renamed.
- SmartX DynamoDB model_name strings in `aum.ts:265-269` = BACKEND JOIN KEYS. NOT touched.
- Display-mapping layer = safe. Updated.

**Approach:** display-mapping layer only (no data-key rename).

**11 files changed (display-only):**
- `lib/modelPortfolioColors.ts` — canonical keys + backward-compat aliases (API-returned names still work via partial/exact match)
- `api/endpoints/benchmarks.ts MODEL_NAMES`
- `components/MaxDrawdownChart|RollingCaptureChart|RollingSharpeChart` — MODEL_NAMES + MODEL_COLOR_KEYS
- `Attribution/constants/holdings-shared.tsx` name fields
- `Attribution/panels/AllocationHeatmap.tsx` PORTFOLIO_NAMES (display headers; data join at :131 uses codes)
- `FactorTilts/constants.ts` AVAILABLE_PORTFOLIOS name fields (NOT modelToAumName:200-204)
- `Positioning/panels/PositioningSummary.tsx` + `shared/gridConfig.ts`
- `ModelPortfolios/tabs/PeersTab.tsx` MODEL_CODE_TO_NAME

**NOT renamed (DS~B coordination needed):**
- `FactorTilts/constants.ts:200-204` modelToAumName — AUM S3 join keys
- `Attribution/tabs/HoldingsTab.tsx:130-134` + `SelectionTab.tsx:95-97` codeMap — DynamoDB AUM join
- Inconsistency flagged: HoldingsTab uses "Ultra Short Term" (no hyphen) vs FactorTilts "Ultra Short-Term" (hyphen) for AUM weight lookups — possible different data sources; DS~B to verify

**Q3 flag (AC4-Q3):** LT/ULT compact-UI abbreviations not wired — awaiting COO/Andrew call.

**Compiler tools:**
- `comp-transform schema-check Attribution`: WARN types.ts absent (pre-existing, not caused by this change)
- `comp-transform schema-check Positioning`: PASS — all rendered fields match response types
- `comp-transform schema-check FactorTilts`: PASS — getAUMFlowsWithMetrics type warn is pre-existing
- `bun tsc --noEmit`: CLEAN (zero errors)

---

## Compiler tools log

| Tool | Target | Result |
|---|---|---|
| comp-transform schema-check | ModelPortfolios | WARN: no types.ts (pre-existing) |
| comp-transform schema-check | Attribution | WARN: no types.ts (pre-existing) |
| comp-transform schema-check | Positioning | PASS |
| comp-transform schema-check | FactorTilts | PASS (AUMFlowsWithMetrics warn pre-existing) |
| bun tsc --noEmit | portal/ | CLEAN |
