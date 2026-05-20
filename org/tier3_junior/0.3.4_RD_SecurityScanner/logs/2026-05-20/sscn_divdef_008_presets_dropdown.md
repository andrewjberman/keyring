# SSCN_DIVDEF.008 -- Presets dropdown implementation

**Agent:** 0.3.4_RD_SecurityScanner
**Date:** 2026-05-20
**Task order:** SSCN_DIVDEF.008-RD (PM: 0.3.0_DE_TradingOperations)
**PRD:** docs/architecture/SSCN_DIVDEF.md v0.5 (commit adbc3c34e) -- §A/§B/§6.8

## Scope

Refactor the hardcoded DIVZ-on-load seeding (`initializeDefaultsWithWeights`)
into a PRESETS-registry model and add ONE new control: a labeled "Presets:"
`<select>` placed left of the universe dropdown in ScannerHeaderPanel.

## Files changed (4, all in portal/src/pages/SecurityScanner/)

| File | Change |
|------|--------|
| `constants.ts` | Added `Preset` interface, `PRESETS` registry (single `divz` entry referencing `DEFAULT_PRESET` unchanged), `DEFAULT_PRESET_ID = 'divz'`. `DEFAULT_PRESET` content byte-identical -- registry references it. |
| `hooks/useScannerState.ts` | Added `applyPreset(presetId, allFactors)` action (atomic universe + factors + weights set). Added derived `activePresetId: string \| null` via `useMemo` (matches preset on universe + code-set + per-code weights; `null` = Custom). Removed `initializeDefaultsWithWeights` (interface member + function + return entry). Both new members added to `ScannerStateActions` + return object. |
| `components/ScannerHeaderPanel.tsx` | Added `activePresetId` + `onPresetChange` props. Added the "Presets:" `<select>` as the FIRST child of the existing `actions` flex row (left of universe select), matching the universe select className exactly. "Custom" option renders only when `activePresetId === null` and is `disabled` (display-only state). No other change. |
| `SecurityScanner.tsx` | On-load `useEffect` now calls `scannerState.applyPreset(DEFAULT_PRESET_ID, factorData.factors)` (replaced manual DEFAULT_PRESET pick loop). Import `DEFAULT_PRESET` -> `DEFAULT_PRESET_ID`; dropped now-unused `FactorDefinition` type import. Passed `activePresetId` + `onPresetChange` props to `<ScannerHeaderPanel>`. Copy fix: "6 universes" -> "5 universes" at JSDoc (line ~6) and `description=` prop (line ~74). |

`defaultsSeeded` ref guard + `if (!factorData) return` guard retained.
No element SSCN_DIVDEF.007 reverted was reopened. ONE new control only.

## Acceptance criteria

| AC | Status |
|----|--------|
| AC1 -- fresh load applies DIVZ (r1000, 13 factors at §3.1 weights), dropdown shows "DIVZ -- Dividend" | Implemented; visual confirm by DE /frontend-dev |
| AC2 -- selecting DIVZ after manual edits re-applies universe+factors+weights atomically | Implemented (`applyPreset` 3 batched setState in one handler) |
| AC3 -- manual edit flips dropdown to "Custom" | Implemented (`activePresetId` pure derive returns `null` on divergence) |
| AC4 -- no layout change vs post-.007 baseline other than the new dropdown | Implemented; visual confirm by DE /frontend-dev |
| AC5 -- /frontend-dev smoke green | DE runs |
| AC6 -- typecheck + lint clean | PASS (transcript below) |

## Compiler Tools

| Tool | Phase | Result |
|------|-------|--------|
| `comp-transform schema-check ScannerHeaderPanel` | Phase 1 (before) | "All rendered fields match their response types." -- baseline. |
| `comp-transform schema-check ScannerHeaderPanel` | Phase 3 (after) | "All rendered fields match their response types." -- no MISSING introduced by the 2 new props. |

Phase 2 (`comp-cache collisions`) + /frontend-dev smoke are run by DE 0.3.0 per
the TO handback (DE owns the full 3-phase compiler mandate + commit + RAVC2).

## typecheck + lint transcript

```
$ bun run typecheck
$ tsc -b --noEmit
typecheck exit: 0

$ bun run lint
... 11 problems (0 errors, 11 warnings)
lint exit: 0
```

All 11 lint warnings are pre-existing in files outside this TO's scope
(`src/components/market-performance/RSIBars.tsx`,
`src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx`).
Zero warnings and zero errors in any SecurityScanner file. Both commands exit 0.

## Handback + acceptance

MCP sent to 0.3.0_DE_TradingOperations with the 4-file list + gate results.

DE verification (reply, same session): all 4 files reviewed vs spec and ACCEPTED.
- comp-cache collisions: no scanner-key collision.
- comp-transform schema-check ScannerHeaderPanel: clean (no MISSING from the 2 new props).
- /frontend-dev smoke: 21/21 PASS -- includes new scenario 5 covering AC1 (DIVZ on
  load), AC2 (atomic re-apply), AC3 (Custom-on-manual-edit) all green.
- typecheck exit 0; lint 0 errors.

DE committed the portal implementation: portal DEV `b05388dc` (6 files -- the RD 4
plus the smoke constitution/runner DE extended with scenario 5). DE is taking the
RAVC2 to COO and closing SSCN_DIVDEF.008.

RD org-side deliverables (this log + page_inventory.xml) committed separately under
the RD author per XXX.md "don't edit another agent's core document" -- DE did not
commit the RD core doc under the DE author.
