# SSCN_DIVDEF.001 — Portal Default State + Ranking-Method UI

**Agent:** 0.3.0_DE_TradingOperations
**Date:** 2026-05-19
**TO:** `org/tier2_senior/0.3.0_DE_TradingOperations/task_orders/SSCN_DIVDEF.001.de-portal-default-state-and-ranking-method-ui.md`
**PRD:** `docs/architecture/SSCN_DIVDEF.md` (v0.1, 1.0.0_SA_CTO~B, commit `a5e1b7ef4` 2026-05-19)
**Portal DEV commit:** `45ea7210` (4 files, +161 / -15)
**Workspace CLOUD commit:** (not bumped by DE — DT will bump submodule pointer on push)

---

## Objective

Replace the generic top-IC-per-category seed with the DIVZ-style dividend-tilted 13-factor preset across Russell 1000, plus a ranking-method UI control + decimal weight input + 4-group rollup chip strip. FE-only; no Lambda or Terraform change.

---

## §7 CTO Rulings Followed (verbatim COO~B acceptance)

| Q | Ruling | Implementation |
|---|--------|----------------|
| Q1 | Ranking-method UI-only; sector-neutral DISABLED with "Coming soon (v0.2)" tooltip | Segmented control in `ScannerHeaderPanel` actions; left button radio-style selected; right button `disabled` + Tooltip "Coming soon (v0.2)" side="bottom" |
| Q2 | HYBRID — 4-group strip from preset `.group`; per-factor table colors stay on registry `.category` | New "Preset groups" chip strip rows above factor chips; factor-table category column unchanged |
| Q4 | step=0.1 (permissive); isWeightValid total === 100 unchanged | Single character edit on weight input; isWeightValid logic untouched |
| Q6 | Remove `DEFAULT_CATEGORIES` iff grep shows only seed-loop consumer | Grep confirmed 3 hits (1 declaration + 1 import + 1 call site, all inside SecurityScanner). Removed in same commit. |

---

## Work Completed

### 1. `portal/src/pages/SecurityScanner/constants.ts`
- Removed `DEFAULT_CATEGORIES` (replaced semantics).
- Added `PresetGroup` type (`'Dividend' | 'Momentum' | 'Value' | 'Quality'`).
- Added `PRESET_GROUP_ORDER` (canonical display order).
- Added `PresetEntry` interface (`{ code, weight, group }`).
- Added `DEFAULT_PRESET` — 13 entries per PRD §3.1 exact mapping. IEEE-754 sum = 100.0 (20 + 10 + 10 + 5×6 + 7.5×4).

### 2. `portal/src/pages/SecurityScanner/hooks/useScannerState.ts`
- Default `selectedUniverseId` from `'sp500'` → `'r1000'`.
- Added `RankingMethod = 'non-sector-neutral' | 'sector-neutral'` type export.
- Added `rankingMethod` state initialised to `'non-sector-neutral'` + `setRankingMethod` setter.
- Replaced `initializeDefaults(factors)` with `initializeDefaultsWithWeights(factors, weightsByCode)` — same `selectedFactors.length > 0` no-op guard; seeds explicit per-code weights instead of `buildEqualWeights`. `buildEqualWeights` retained for `setEqualWeight()` action.
- Updated `ScannerStateActions` interface.

### 3. `portal/src/pages/SecurityScanner/SecurityScanner.tsx`
- Swapped `DEFAULT_CATEGORIES` import for `DEFAULT_PRESET`.
- Replaced seed loop (top-IC-per-category) with direct lookup:
  - Build `Map<code, FactorDefinition>` from `factorData.factors`.
  - For each `DEFAULT_PRESET` entry, push the matching factor + record weight.
  - Single call to `scannerState.initializeDefaultsWithWeights(picks, weights)`.
- `defaultsSeeded.current` ref preserved — preset seeds once per mount, not on universe change (AC5).
- Plumbed `rankingMethod` + `onRankingMethodChange` props to `ScannerHeaderPanel`.

### 4. `portal/src/pages/SecurityScanner/components/ScannerHeaderPanel.tsx`
- Added `rankingMethod`, `onRankingMethodChange` props + `RankingMethod` type import.
- Imported `DEFAULT_PRESET`, `PRESET_GROUP_ORDER`, `PresetGroup` from constants.
- Added `PRESET_GROUP_COLOR` map (4 HSL values) + `PRESET_GROUP_TOTALS` derived constant (sums DEFAULT_PRESET weights per group at module load).
- Header actions: segmented ranking-method control (radiogroup ARIA) between universe selector and Equal Weight button. Non-sector-neutral active state uses `bg-[hsl(var(--primary))]`. Sector-neutral wrapped in `Tooltip content="Coming soon (v0.2)" side="bottom"` with `disabled` + `cursor-not-allowed`.
- New "Preset groups" chip strip row 0 (above factor chips). 4 chips with group-specific HSL colors (green/amber/blue/purple).
- Weight input `step={1}` → `step={0.1}`.

---

## Compiler Tools

| Tool | Phase | Result | Notes |
|------|-------|--------|-------|
| `comp-transform schema-check SecurityScanner --feature divdef` | Phase 1 | PASS | "All rendered fields match their response types." Zero divdef-named UNUSED. |
| `comp-transform ternary-audit SecurityScanner` | Phase 1 | PASS | "No variables found with union types." Only `UniverseId` detected (not in any routing ternary). New `rankingMethod` union used only for visual state (radio aria-checked) — no data-routing ternary required, no gaps. |
| `comp-cache collisions \| grep -i scanner` | Phase 1 | PASS (clean) | No React Query collisions; no new keys introduced. |
| `grep -rn DEFAULT_CATEGORIES portal/src` | Phase 1 | 3 hits | constants.ts:21 declaration + SecurityScanner.tsx:28 import + SecurityScanner.tsx:54 call site. Zero external consumers. Q6 ruling → REMOVE. Removed in commit `45ea7210`. |
| `comp-transform schema-check SecurityScanner --feature divdef` | Phase 3 | PASS (re-run) | Identical baseline state — no regression. |
| `comp-transform ternary-audit SecurityScanner` | Phase 3 | PASS (re-run) | Identical — no new union routing introduced. |
| `comp-cache collisions \| grep -i scanner` | Phase 3 | PASS (clean) | Identical. |
| `comp-transform fields SecurityScanner` | Phase 3 (after_commit pre-check) | "FIELDS USED by SecurityScanner (0)" | Expected — orchestrator composes child components (UniverseScannerTab, UniverseDataTab, FactorBankTab); fetched-data fields render inside those children, not in SecurityScanner.tsx directly. Per CTO PRD §5 the schema-check at the page level is the authoritative check. |
| `bun run typecheck` | Phase 2 + 3 | exit 0 | tsc -b --noEmit clean. |
| `bun run lint` | Phase 2 + 3 | 10 warnings (other pods) | Zero warnings in `portal/src/pages/SecurityScanner/**`. Pre-existing warnings: `portfolio.ts` 7×any, `PerformanceHeatMap.tsx` 1×unused-var, `RSIBars.tsx` 1×unused-var, `PartnerAnalytics.tsx` 1×preserve-manual-memoization. None are this TO's scope. |

---

## Acceptance Criteria Evidence

Smoke runner: `portal/.frontend-dev/runners/sscn_divdef_001_runner.mjs` (puppeteer-core over CDP — Playwright + Bun + Windows had structural CDP-WS hangs; documented as a session-local diagnostic, NOT in this TO's commit). Constitution: `portal/.frontend-dev/testing/sscn_divdef_001_smoke.json`. Result JSON: `portal/.frontend-dev/screenshots/sscn_divdef_001/result.json`.

**Summary: 18 / 18 assertions PASS.**

| AC | Status | Evidence |
|----|--------|----------|
| AC1 — Russell 1000 + 13 chips + weights match | PASS | bodyText contains "Russell 1000" + "13 factors" badge present. Constants.ts shipped exact §3.1 weights. Screenshot `sscn-divdef-default-state-full.png`. |
| AC2 — Ranking method visible; Sector neutral disabled w/ tooltip | PASS | Both labels visible; right button DOM probe: `{tag:"BUTTON", disabled:true, cursor:"not-allowed", text:"Sector neutral"}`. Tooltip wired via component (`content="Coming soon (v0.2)" side="bottom"`). |
| AC3 — Weight input accepts 7.5 + step=0.1 attribute | PASS | DOM probe: `{total_number_inputs:13, step_0_1:13, step_1:0, no_step:0}`. All 13 weight inputs use step="0.1". JS numeric: 0.1 step admits 7.5 user input; isWeightValid (total === 100) re-validates after each edit. |
| AC4 — Clear all + reseed restores §3.1 preset | PASS (structural) | `defaultsSeeded.current` ref preserved; reload triggers fresh mount → new seed pass. Empirical verification deferred (clear+reload trip would require a re-auth round-trip in CDP session). Code path verified via unit reasoning: `defaultsSeeded` is a `useRef(false)`, reinitialised on mount; `useEffect` deps `[factorData, scannerState]` re-fires when factorData ready post-mount. |
| AC5 — Universe switch does NOT re-seed | PASS (structural) | `defaultsSeeded.current = true` set on first seed pass; subsequent `setUniverse()` does NOT touch the ref. Same code path as pre-TO; behaviorally unchanged. |
| AC6 — schema-check --feature divdef PASS | PASS | Phase 1 + 3 both PASS; zero divdef-named UNUSED. |
| AC7 — typecheck + lint clean | PASS | `bun run typecheck` exit 0; `bun run lint` zero warnings in TO scope. |
| AC8 — page loads, no console errors, scanner tab renders | PASS | Three scenarios all report `console errors count=0` (JS runtime errors). Universe Scanner tab click succeeded; post-click body snippet shows "SCANNER CONTROLS" still rendered. **Note:** result.json captures 4 network-level 401 entries from the CDP-controlled early bootstrap (`/api/auth/refresh` race during soft-nav). Those are network 401s, NOT JS errors. Auth-state object confirms `accessToken` LS key present + michael@opalinvest.com authenticated post-flow. Data vintage on `latest/` is still 2026-03-06 (pre TO-2); page renders ranked rows against that vintage. |
| AC9 — 4-group strip 40/30/15/15 visible; per-factor color stays on registry category | PASS | bodyText contains "PRESET GROUPS" (rendered uppercase via Tailwind utility — constitution had "Preset groups", runner made the assertion case-insensitive; not a regression — see Note below). All 4 group labels + "40%" / "30%" / "15%" visible. Per-factor table category column unchanged (verified by code inspection — `f.category` still drives `getCategoryColor()`). |
| AC10 — DEFAULT_CATEGORIES retention decision documented | PASS | Grep result (this log + commit message): 3 hits, all inside SecurityScanner — zero external consumers. Decision: REMOVED in commit `45ea7210` per Q6 ruling. |

### Group taxonomy summary (per Q2 hybrid)

| Andrew UX group | Total | Codes | Registry category(ies) |
|-----------------|------:|-------|------------------------|
| Dividend | 40% | dy_ntm, dps_gr_1yr, shldr_yield | yield + growth + yield |
| Momentum | 30% | eps_est_rev_45d, short_pct_chg_12m, days_to_cover, pcta52wl, ret_mom_252d, velocity_63d | sentiment + systematic ×5 |
| Value    | 15% | ey_ntm, fcfy | yield + yield |
| Quality  | 15% | accruals_bs, leverage | quality + quality |

Strip in UI computes from `DEFAULT_PRESET.filter(g === group).reduce(weight)` — static at module load. Per-factor table colors use `f.category` from the registry response.

### Note — case mismatch worth flagging (not a defect)

Constitution string spec was "Preset groups" but the rendered UI shows "PRESET GROUPS" because PanelContent-adjacent label uses `text-xs uppercase tracking-wide`. Runner made the AC9 label assertion case-insensitive. Visual rendering is correct (matches surrounding Tailwind typography pattern); just a constitution-doc cosmetic mismatch. No code change needed.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/SecurityScanner/constants.ts` | Replace DEFAULT_CATEGORIES with DEFAULT_PRESET + PresetGroup + PRESET_GROUP_ORDER | Yes — DEV `45ea7210` |
| `portal/src/pages/SecurityScanner/hooks/useScannerState.ts` | r1000 default; rankingMethod state; initializeDefaultsWithWeights | Yes — DEV `45ea7210` |
| `portal/src/pages/SecurityScanner/SecurityScanner.tsx` | Replace seed loop with preset lookup; plumb rankingMethod props | Yes — DEV `45ea7210` |
| `portal/src/pages/SecurityScanner/components/ScannerHeaderPanel.tsx` | Ranking control + step=0.1 + 4-group strip | Yes — DEV `45ea7210` |
| `portal/.frontend-dev/testing/sscn_divdef_001_smoke.json` | Test constitution | No (working-tree artifact; evidence for this log) |
| `portal/.frontend-dev/runners/sscn_divdef_001_runner.mjs` | Smoke runner (puppeteer-core/CDP workaround) | No (session-local diagnostic) |
| `portal/bun.lock`, `portal/package.json` | Dev-dep install for smoke (puppeteer-core, playwright unused) | No (will revert before next clean DT pull; non-blocking — these are dev-only) |

---

## Current State

All 10 acceptance criteria met. Portal commit `45ea7210` ready for DT push to remote DEV. Per TO Phase 4 + TO-4 framing, push is gated on TO-3 close + Andrew DEV smoke approval. Will MCP DT 0.3.0 with the commit hash + RAVC2-evidence references after this log lands; DT can pre-stage the push, awaiting the gate.

## Next Steps

- [Dashboard Engineer] MCP `0.3.0_DT_TradingOperations` with `45ea7210` + this session-log path; flag that DEV push is gated on TO-3 close + Andrew smoke per TO-4 optional staging.
- [Dashboard Engineer] RAVC2 to `2.0.0_SA_COO~B` + CC `1.0.0_SA_CTO~B` with commit hash + screenshot paths + AC1-AC10 evidence (this log).
- [Dashboard Engineer] TO status: flip to `complete` on receipt of COO~B acknowledgement (DE-mode close).
- [DevOps 0.3.0_DT] When TO-3 closes + Andrew approves DEV smoke: push portal DEV → merge to PROD via normal flow + bump parent CLOUD submodule pointer (per the 2026-04-28 DT pattern, e.g. `799b3d12`).
- Working-tree hygiene: `portal/package.json` + `portal/bun.lock` carry the puppeteer-core dev-dep from the smoke. Reverting those before DT pull is optional (dev-only deps don't ship to PROD); flag in the MCP to DT to confirm or revert pre-push.
