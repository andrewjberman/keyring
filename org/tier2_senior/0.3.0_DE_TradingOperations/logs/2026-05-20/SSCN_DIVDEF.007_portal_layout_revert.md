# SSCN_DIVDEF.007 — Portal Layout Revert (PRD v0.4 §6.7)

**Agent:** 0.3.0_DE_TradingOperations
**Date:** 2026-05-20
**TO:** `org/tier2_senior/0.3.0_DE_TradingOperations/task_orders/SSCN_DIVDEF.007.de-portal-layout-revert-v0-4.md`
**PRD:** `docs/architecture/SSCN_DIVDEF.md` v0.4 §A/§B/§C/§6.7 (commit `d9b664e63`, 1.0.0_SA_CTO)
**Baseline commit:** `904caed5` — pre-`45ea7210` state of `ScannerHeaderPanel.tsx` (AC1 byte-identical target)
**Portal DEV commit:** `a844f0dd` (5 files, +341 / -110)
**Workspace CLOUD commit:** see commit landing this log (TO close + §3.5 patch)

---

## Objective

TO-1 (`45ea7210`, DEV-only) shipped the in-scope DIVZ default preset bundled with three
out-of-scope layout/functionality additions. PRD v0.4 (Yang / Andrew directive) froze the
Security Scanner layout at its pre-5/18 state — only data/indices and the default preset
are permitted changes. This TO surgically reverts the over-scope while preserving the
in-scope DIVZ preset seeding and the `.005` universe migration (`b302f5cf`).

Reverted (out of scope, absent pre-5/18):
- **B.** Ranking-method radiogroup ("Non-sector neutral / Sector neutral [disabled]")
- **C.** 4-group rollup chip strip ("Preset groups: Dividend 40% / ...")
- **D.** Weight input `step={0.1}` → restored `step={1}`

Preserved (in scope): DIVZ `DEFAULT_PRESET` + `initializeDefaultsWithWeights` seeding;
default universe `r1000`; the `.005` 5-universe migration.

---

## Work Completed

### 1. `components/ScannerHeaderPanel.tsx` — restored byte-identical to `904caed5`
`git checkout 904caed5 -- ScannerHeaderPanel.tsx`. Only `45ea7210` touched this file
between `904caed5` and HEAD (verified via `git log 904caed5..HEAD -- <file>`), so a full
restore is exact. Removes the ranking radiogroup, the rollup chip strip, the
`RankingMethod`/`DEFAULT_PRESET`/`PRESET_GROUP_ORDER` imports, the
`PRESET_GROUP_COLOR`/`PRESET_GROUP_TOTALS` constants, and reverts the weight input to
`step={1}`.

### 2. `hooks/useScannerState.ts` — surgical RankingMethod removal
Removed the `RankingMethod` type, the `rankingMethod` state + `setRankingMethodState`,
the `setRankingMethod` setter, and the two interface members. **KEPT**
`initializeDefaultsWithWeights` and the `useState<UniverseId>('r1000')` default — both
in-scope TO-1 seeding. NOT a full `904caed5` checkout (that file's pre-TO-1 state lacks
`initializeDefaultsWithWeights`).

### 3. `SecurityScanner.tsx` — surgical prop-wiring removal
Removed the `rankingMethod={...}` and `onRankingMethodChange={...}` props passed to
`ScannerHeaderPanel`. **KEPT** the `DEFAULT_PRESET` import and the seeding `useEffect`.

### 4. `constants.ts` — UNCHANGED (over-revert guard)
`DEFAULT_PRESET`, `PresetEntry`, `PresetGroup`, `PRESET_GROUP_ORDER`, `US_ONLY_UNIVERSES`
and the universe entries were not touched. `PRESET_GROUP_ORDER` is now unimported (its
only renderer, the rollup strip, is gone) — retained as forward-compat metadata per PRD
v0.4 §C; `lint` did not flag it (exported const, 0 errors).

### 5. `.frontend-dev` smoke constitution + runner — updated to v0.4 reverted state
`sscn_divdef_001_smoke.json` (tracked) + `sscn_divdef_001_runner.mjs` (was untracked — a
`.005` oversight; now committed for reproducibility) updated: scenario 1 asserts the
ABSENCE of "Preset groups" / "Non-sector neutral" / "Sector neutral"; scenario 2 asserts
`step=1` ×13 weight inputs and zero `step=0.1`; in-scope scenarios (Russell 1000 default,
13 factors, 5-universe dropdown) retained. One-constitution-per-feature-lineage convention
(COO~B-ratified under `.005`) — updated in place rather than a new `.007` constitution.

### 6. `SSCN_GROUP_TAXONOMY.md` §3.5 — patched
§3.5 "Group-rollup display" rewritten: the `group` field is preset metadata only, no UI
strip renders it post-v0.4; cites the `.007` revert + PRD §C (`group` retained as
forward-compat) + §B (registry-category display is correct pre-5/18 behavior). DS 0.3.0
coordination: DS confirmed `.003` RAVC2 COMPLETE landed (`1d6a73c95`), `SSCN_GROUP_TAXONOMY.md`
working tree clean, §3.5 untouched by their §5/§8 edits — clear to patch (MCP exchange
2026-05-20). No edit-window collision.

---

## Acceptance Criteria Evidence

| AC | Status | Evidence |
|----|--------|----------|
| AC1 | PASS | `git diff 904caed5 HEAD -- src/pages/SecurityScanner/components/ScannerHeaderPanel.tsx` returns EMPTY output (verified against committed portal HEAD `a844f0dd`). |
| AC2 | PASS | Over-revert guard: `constants.ts` `DEFAULT_PRESET` = 13 entries, weights `20+10+10 + 5x6 + 7.5x4 = 100.0`. `US_ONLY_UNIVERSES` + `UNIVERSE_IDS`/`UniverseId` union = 5 entries `sp500/r1000/rmidcap/sp400/msciusa`. Surgical revert did not over-revert into in-scope preset/universe work. |
| AC3 | PASS | Fresh DEV load (smoke scenario 1-2): "Russell 1000" rendered as default universe; "13 factors" badge present; 13 weight inputs seeded. Weights seeded from the unchanged `DEFAULT_PRESET` via the kept `initializeDefaultsWithWeights`. |
| AC4 | PASS | Smoke: `AC4_no_preset_groups_strip` (case-insensitive "preset groups" absent), `AC4_no_ranking_method_control` ("Non-sector neutral"/"Sector neutral" both absent), `AC4_step_1_count_gte_13` (13 inputs `step=1`), `AC4_no_step_0_1_inputs` (`step=0.1` count = 0). Header screenshot visually confirms no rollup strip + no ranking control. |
| AC5 | PASS | `/frontend-dev` smoke 16/16 PASS — `portal/.frontend-dev/screenshots/sscn_divdef_001/result.json`. Visual artifacts: `sscn-divdef-default-state-full.png`, `sscn-007-header-viewport.png` (same dir). Zero layout delta vs pre-5/18 is formally guaranteed by AC1 byte-identity — `ScannerHeaderPanel.tsx` is byte-for-byte the pre-5/18 component, so it renders the pre-5/18 layout; the only difference is the seeded factor list/weights (the permitted default-state change). No separate pre-5/18 baseline screenshot existed to pixel-diff; byte-identity is the stronger proof. |
| AC6 | PASS | `bun run typecheck` (`tsc -b --noEmit`) exit 0, zero errors. `bun run lint` exit 0, 0 errors, 11 warnings — all pre-existing in other pods (portfolio.ts, PerformanceHeatMap, RSIBars, PartnerAnalytics); zero in SecurityScanner scope. |

**Weight step (Andrew-overridable):** shipped the `step={1}` default per Yang's
"functionality frozen" directive. Andrew may elect to retain `step={0.1}`; that is a
one-line revert-back and does not re-open this TO. No Andrew override was relayed before
ship.

---

## Compiler Tools

| Tool | Phase | Result | Notes |
|------|-------|--------|-------|
| `comp-transform schema-check ScannerHeaderPanel` | 1 (before write) | PASS | Baseline: "All rendered fields match their response types." Zero MISSING/NOTE/UNUSED. |
| `comp-cache collisions` | 2 (before commit) | PASS | Collisions surface only for AdvisorIntelligence keys; zero scanner-key collisions. This TO removes state (`RankingMethod`) and adds none — confirmed no collision introduced. |
| `bun run typecheck` | 2 (before commit) | exit 0 | tsc clean — RankingMethod type/state/setter + prop-wiring removal left no dangling reference. |
| `bun run lint` | 2 (before commit) | exit 0, 0 errors | 11 warnings, all pre-existing other-pod; none in scope. `PRESET_GROUP_ORDER` unused-export not flagged. |
| `comp-transform schema-check ScannerHeaderPanel` | 3 (after) | PASS | Identical to Phase 1 baseline — "All rendered fields match their response types." No MISSING field post-revert. |
| `/frontend-dev` smoke (`sscn_divdef_001_runner.mjs`) | 3 (after) | 16/16 PASS | Headless Chrome CDP + puppeteer-core; result JSON `portal/.frontend-dev/screenshots/sscn_divdef_001/result.json`. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/SecurityScanner/components/ScannerHeaderPanel.tsx` | Restored byte-identical to `904caed5` (revert B/C/D) | Yes — DEV `a844f0dd` |
| `portal/src/pages/SecurityScanner/hooks/useScannerState.ts` | Removed `RankingMethod` type/state/setter; kept `initializeDefaultsWithWeights` | Yes — DEV `a844f0dd` |
| `portal/src/pages/SecurityScanner/SecurityScanner.tsx` | Removed `rankingMethod`/`onRankingMethodChange` prop wiring; kept seeding `useEffect` | Yes — DEV `a844f0dd` |
| `portal/.frontend-dev/testing/sscn_divdef_001_smoke.json` | Constitution updated to v0.4 reverted state | Yes — DEV `a844f0dd` |
| `portal/.frontend-dev/runners/sscn_divdef_001_runner.mjs` | Runner updated to v0.4 reverted state; newly tracked | Yes — DEV `a844f0dd` |
| `docs/architecture/security-scanner-source/SSCN_GROUP_TAXONOMY.md` | §3.5 patched — group taxonomy is preset metadata, no UI strip post-v0.4 | Yes — CLOUD (this commit) |

---

## Observation (out of scope — for COO)

`SecurityScanner.tsx:74` still renders `description="Multi-factor screening across 6
universes ..."` — stale copy after the `.005` 6→5 universe migration (also `SecurityScanner.tsx:6`
comment + `DESIGN_SPEC.md:117`). NOT touched here: copy correction is outside the `.007`
layout-revert scope, and the string is not in `ScannerHeaderPanel.tsx` (AC1 byte-identity
target). Flagging for COO as a `.005` follow-up nit.

---

## Current State

SSCN_DIVDEF.007 complete. Surgical layout revert committed to portal DEV (`a844f0dd`);
`ScannerHeaderPanel.tsx` byte-identical to pre-5/18 `904caed5`; in-scope DIVZ preset +
5-universe migration preserved (AC2 over-revert guard PASS). All 6 ACs PASS. `/frontend-dev`
smoke 16/16. §3.5 of `SSCN_GROUP_TAXONOMY.md` patched (DS-coordinated).

DEV only — PROD push is the TO-4/`.006` DT gate (gated on `.007` close + `.003` close +
Andrew DEV smoke).

## Next Steps

- [Dashboard Engineer] RAVC2 to `2.0.0_SA_COO` + CC `1.0.0_SA_CTO` with AC1-AC6 evidence;
  flip TO `<status>` to `complete` on RAVC2 send (DS-mode).
- [DevOps 0.3.0_DT] Portal DEV commit `a844f0dd` joins the push-ready stack. PROD push
  (`.006`) gated on `.007` close + `.003` close (DS `1d6a73c95`) + Andrew DEV smoke.
- [2.0.0_SA_COO] Stale "6 universes" copy in `SecurityScanner.tsx` — `.005` follow-up nit
  (see Observation above).
