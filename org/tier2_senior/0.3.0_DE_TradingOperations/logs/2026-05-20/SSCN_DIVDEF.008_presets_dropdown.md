# SSCN_DIVDEF.008 — Presets Dropdown (PRD v0.5 §6.8)

**Agent:** 0.3.0_DE_TradingOperations (PM/owner)
**Implementation:** 0.3.4_RD_SecurityScanner (under DE coordination)
**Date:** 2026-05-20
**TO:** `org/tier2_senior/0.3.0_DE_TradingOperations/task_orders/SSCN_DIVDEF.008.de-rd-presets-dropdown.md`
**RD TO:** `org/tier3_junior/0.3.4_RD_SecurityScanner/task_orders/SSCN_DIVDEF.008_presets_dropdown.md` (DE-authored, commit `d391963ef`)
**PRD:** `docs/architecture/SSCN_DIVDEF.md` v0.5 §A/§B/§C/§6.8 (commit `adbc3c34e`)
**Portal DEV commit:** `b05388dc` (6 files, +189 / -33)
**Workspace CLOUD commit:** see commit landing this log (TO close)

---

## Objective

Deliver the DIVZ default preset as an explicit, user-switchable `Presets:` dropdown — the
ONE authorized layout addition under SSCN_DIVDEF v0.5 (the v0.4 "pre-5/18 layout frozen"
rule otherwise stands). Refactor the hardcoded DIVZ-on-load seeding (the
`initializeDefaultsWithWeights` call SSCN_DIVDEF.007 kept) into a `PRESETS`-registry model.

## Implementation model

DE is PM/owner; 0.3.4_RD_SecurityScanner built the front-end under DE coordination. DE
authored a precise 4-file design spec (the RD TO), dispatched GO, then reviewed the RD
implementation, ran the compiler mandate, committed, and owns this RAVC2. RD ran
typecheck/lint + schema-check pre-handback; DE re-verified all gates.

## Work Completed (4 files + smoke)

### 1. `constants.ts`
Added the `Preset` interface (`{ id, label, universe, entries }`), the `PRESETS` registry
(single `divz` entry: `label: 'DIVZ -- Dividend'`, `universe: 'r1000'`, `entries:` references
`DEFAULT_PRESET` unchanged), and `DEFAULT_PRESET_ID = 'divz'`. `DEFAULT_PRESET` content
byte-identical — codes/weights/`group` unchanged (refactor, not content change).

### 2. `hooks/useScannerState.ts`
Added `applyPreset(presetId, allFactors)` — atomic set of universe + factor selection +
weights from a registry preset. Added a derived `activePresetId: string | null` (useMemo) —
the id of the preset whose universe + factor-code set + per-code weights exactly match the
live state, else `null` (the Custom state); a pure derive, so any manual edit naturally
falls back to Custom with no extra state or mutator changes. Removed the now-dead
`initializeDefaultsWithWeights` (superseded by `applyPreset`).

### 3. `components/ScannerHeaderPanel.tsx`
Added the labeled `Presets:` `<select>` first in the existing actions flex row, universe-
select styling matched exactly. Two new props (`activePresetId`, `onPresetChange`). The
`Custom` option renders only when `activePresetId === null` and is `disabled` (display-only
state). One new control — byte-identical to the post-.007 `904caed5` baseline otherwise;
nothing SSCN_DIVDEF.007 reverted is reopened.

### 4. `SecurityScanner.tsx`
On-load seeding `useEffect` now calls `applyPreset(DEFAULT_PRESET_ID, factorData.factors)`.
Import swap `DEFAULT_PRESET` -> `DEFAULT_PRESET_ID`; unused `FactorDefinition` type import
dropped. Two new props wired to `<ScannerHeaderPanel>`. Folded-in copy fix per the parent
TO: stale `across 6 universes` -> `across 5 universes` at both sites (line ~6 JSDoc, line
~74 `description`) — leftover from the `.005` 6->5 universe migration, surfaced by DE
during `.007`.

### 5. `.frontend-dev` smoke — scenario 5 added
`sscn_divdef_001_runner.mjs` + `sscn_divdef_001_smoke.json` extended with a new
`sscn-divdef-008-presets-dropdown` scenario: locates the two header `<select>`s by option
text, asserts AC1 (DIVZ selected on fresh load), AC3 (a universe edit via
`ElementHandle.select` flips the Presets select to `custom`), AC2 (re-selecting DIVZ
atomically re-applies — Presets `divz`, universe `r1000`).

---

## Acceptance Criteria Evidence

Smoke result JSON: `portal/.frontend-dev/screenshots/sscn_divdef_001/result.json` —
**21 / 21 assertions PASS** (15 retained from .005/.007 + 6 new .008).

| AC | Status | Evidence |
|----|--------|----------|
| AC1 | PASS | Smoke `AC008_1_divz_selected_on_load` — Presets select value = `divz` on fresh load; `AC008_1_preset_select_present` — both header selects located. Header screenshot `sscn-008-header-viewport.png`: "Presets: DIVZ -- Dividend" selected, 13 DIVZ factors + r1000 applied. |
| AC2 | PASS | Smoke `AC008_2_divz_reapply` — after a manual universe edit, re-selecting DIVZ restored preset=`divz` AND universe=`r1000` (atomic re-apply). |
| AC3 | PASS | Smoke `AC008_3_custom_on_manual_edit` — changing the universe select to `sp500` flipped the Presets select to `custom`. The derived `activePresetId` stops matching on any divergence. |
| AC4 | PASS | Header screenshot vs post-.007 baseline: the ONLY delta is the one new `Presets:` dropdown. comp-transform schema-check ScannerHeaderPanel clean (no MISSING from the 2 new props). No ranking control / rollup strip — .007 revert intact. |
| AC5 | PASS | `/frontend-dev` smoke 21/21 PASS; 0 console errors across all 5 scenarios. |
| AC6 | PASS | `bun run typecheck` exit 0; `bun run lint` exit 0, 0 errors, 11 pre-existing other-pod warnings, zero in SecurityScanner scope. |

---

## Compiler Tools

| Tool | Phase | Result | Notes |
|------|-------|--------|-------|
| `comp-transform schema-check ScannerHeaderPanel` | 1 (before write) | PASS | Post-.007 baseline: "All rendered fields match their response types." |
| `comp-cache collisions` | 2 (before commit) | PASS | No scanner-key collision. `applyPreset` drives the universe (which feeds `useScannerApi`) but introduces no new React Query key. |
| `bun run typecheck` | 2 (before commit) | exit 0 | Preset interface + PRESETS + activePresetId + applyPreset type-check end to end. |
| `bun run lint` | 2 (before commit) | exit 0, 0 errors | 11 pre-existing other-pod warnings; zero in scope. |
| `comp-transform schema-check ScannerHeaderPanel` | 3 (after) | PASS | Identical to Phase 1 — no MISSING field from the 2 new props. |
| `/frontend-dev` smoke | 3 (after) | 21/21 PASS | scenario 5 added for .008 AC1/AC2/AC3. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/SecurityScanner/constants.ts` | `Preset` interface + `PRESETS` registry + `DEFAULT_PRESET_ID` | Yes — DEV `b05388dc` |
| `portal/src/pages/SecurityScanner/hooks/useScannerState.ts` | `applyPreset` + derived `activePresetId`; removed `initializeDefaultsWithWeights` | Yes — DEV `b05388dc` |
| `portal/src/pages/SecurityScanner/components/ScannerHeaderPanel.tsx` | `Presets:` `<select>` + 2 props | Yes — DEV `b05388dc` |
| `portal/src/pages/SecurityScanner/SecurityScanner.tsx` | on-load `applyPreset`; import swap; "6"->"5 universes" copy fix | Yes — DEV `b05388dc` |
| `portal/.frontend-dev/testing/sscn_divdef_001_smoke.json` | scenario 5 (.008 Presets dropdown) | Yes — DEV `b05388dc` |
| `portal/.frontend-dev/runners/sscn_divdef_001_runner.mjs` | scenario 5 runner block | Yes — DEV `b05388dc` |
| `org/tier3_junior/0.3.4_RD_SecurityScanner/deliverables/page_inventory.xml` | RD core-doc update (4 rows) | RD-lane — RD commits under its own author |
| `org/tier3_junior/0.3.4_RD_SecurityScanner/logs/2026-05-20/sscn_divdef_008_presets_dropdown.md` | RD session log | RD-lane — RD commits |

---

## Current State

SSCN_DIVDEF.008 complete. Presets dropdown shipped to portal DEV (`b05388dc`); the DIVZ
default is now an explicit, switchable, registry-backed control. All 6 ACs PASS;
`/frontend-dev` smoke 21/21. RD implementation reviewed + accepted; RD commits its own
`page_inventory.xml` + session log under the RD author.

DEV only — PROD push is the TO-4/`.006` DT lane, bundling `.007` + `.008` (one DEV smoke,
one promotion), gated on `.003` close + Andrew DEV smoke.

## Next Steps

- [Dashboard Engineer] RAVC2 to `2.0.0_SA_COO` + CC `1.0.0_SA_CTO`; flip TO `<status>` to
  `complete` on RAVC2 send.
- [0.3.4_RD_SecurityScanner] Commit `page_inventory.xml` + RD session log under RD author.
- [DevOps 0.3.0_DT] Portal DEV `b05388dc` joins the push-ready stack; `.006` PROD push
  bundles `.007` (`a844f0dd`) + `.008` (`b05388dc`).
