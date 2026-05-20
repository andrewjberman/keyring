# SSCN_DIVDEF.005 — Portal UNIVERSE_IDS Swap v0.2 Addendum

**Agent:** 0.3.0_DE_TradingOperations
**Date:** 2026-05-19
**TO:** `org/tier2_senior/0.3.0_DE_TradingOperations/task_orders/SSCN_DIVDEF.005.de-portal-universe-ids-swap-v0-2-addendum.md`
**PRD:** `docs/architecture/SSCN_DIVDEF.md` v0.2 §6.5 (1.0.0_SA_CTO~B, commit `c34f16d13` 2026-05-19, parent CLOUD)
**Portal DEV commit:** `b302f5cf` (4 files, +68 / -10)
**Prior DE commits on this DIVZ feature:** `45ea7210` (TO-1 functional ship) + `2254437c` (TO-1 smoke constitution)

---

## Objective

Migrate the portal universe set 6 → 5 US-equity (Q7 LOCKED descriptive tokens) to align with the PRD v0.2 ratified source-XLSX universe-column-set (`wt_ivv` / `wt_iwb` / `wt_iwr` / `wt_ijh` / `wt_csus`). FE-only; PARALLEL-OK with TO-AE-1 Lambda redeploy + TO-2 data refresh. Universe-set-independent TO-1 work (`45ea7210`) preserved verbatim.

---

## Work Completed (3 surfaces + smoke)

### 1. `portal/src/api/endpoints/security-scanner.ts:28-35`
UNIVERSE_IDS swap to the new 5 entries:

| Token | sourceColumn | Label |
|---|---|---|
| `sp500` | `wt_ivv` | S&P 500 |
| `r1000` | `wt_iwb` | Russell 1000 |
| `rmidcap` | `wt_iwr` | Russell Midcap |
| `sp400` | `wt_ijh` | S&P MidCap 400 |
| `msciusa` | `wt_csus` | MSCI USA Index |

Dropped: `r1000v`, `acwx`, `eafe`, `eafev` (no source column in DIVZ feed). Their `latest/universes/{token}/*` S3 objects retained forensic per PRD v0.2 §3.5 (DO-NOT-DELETE rule); no FE code references them post-migration.

Inline comment documents the migration date + the legacy-retention contract for future agents.

### 2. `portal/src/pages/SecurityScanner/types.ts:27`
UniverseId union swap (explicit edit per existing thread convention, even though `keyof typeof UNIVERSE_IDS` would type-drive it). Result: `'sp500' | 'r1000' | 'rmidcap' | 'sp400' | 'msciusa'`.

### 3. `portal/src/pages/SecurityScanner/constants.ts:11-15`
US_ONLY_UNIVERSES — **Set form retained** per PRD v0.2 §6.5 AC2 framework + DE lean (ratified). 5 new tokens listed.

**Decision rationale (committed):** all 5 v0.2 universes are US-only, so US_ONLY_UNIVERSES technically equals "every UniverseId". A `true` constant would express that intent more directly, BUT the Set has zero overhead, all existing consumers already query via `.has()`, and a future PRD re-introducing an ex-US universe (e.g. `acwx` returning, or a new EAFE-equivalent feed) would need to rewire every consumer if the Set were collapsed. Forward-compat is cheap; retain.

### 4. `portal/.frontend-dev/testing/sscn_divdef_001_smoke.json`
Extended with a new 4th scenario `sscn-divdef-005-universe-dropdown-set` carrying 5 sub-assertions for AC10:
 - AC10.1 dropdown options.length === 5
 - AC10.2 values deep-equal `['sp500', 'r1000', 'rmidcap', 'sp400', 'msciusa']` (v0.2 §3.5 order)
 - AC10.3 labels include all 4 new ones (Russell 1000, Russell Midcap, S&P MidCap 400, MSCI USA Index)
 - AC10.4 legacy 4 tokens NOT present (negative-assert r1000v/acwx/eafe/eafev)
 - AC10.5 default-selected === 'r1000'

Used a new `expect_substring` assertion shape (substring match against returned JSON string from `js_eval`). Runner extended to handle it; backward-compatible with `expect_min` + `assert_no_console_errors` from TO-1 scenarios.

Smoke constitution extension was the COO~B-ratified path (one constitution per feature lineage, not per-TO).

---

## Compiler Tools

| Tool | Phase | Result | Notes |
|------|-------|--------|-------|
| `comp-routes trace getUniverseScanner` | Phase 1 | PASS | URL stable: `/api/general/security_scanner/latest/universes/{param}/scanner_data.json`. CF behavior `/api/general/*` → S3 origin via edge JWT auth. `{param}` is whatever portal sends (UNIVERSE_IDS keys) — route is universe-token-agnostic. |
| `comp-cache collisions \| grep -i scanner` | Phase 1 | PASS (clean) | No new React Query keys; the v0.2 token swap reuses the existing `getUniverseScanner` key shape (universe-token-parameterized). |
| `comp-routes trace getUniverseScanner` | Phase 4 (re-run) | PASS | Identical state — no regression. |
| `comp-cache collisions \| grep -i scanner` | Phase 4 (re-run) | PASS (identical) | No new collisions. |
| `comp-transform schema-check SecurityScanner` | Phase 4 (AC6) | PASS | "All rendered fields match their response types." Zero MISSING; zero unexpected UNUSED. |
| `bun run typecheck` | Phase 4 | exit 0 | tsc -b --noEmit clean. The two UniverseId declarations (endpoint + types) now both list the same 5-entry union; TS narrowed selectedUniverseId='r1000' default to the new union without issue. |
| `bun run lint` | Phase 4 | 10 warnings (other pods) | Identical pre-existing warnings in portfolio.ts (7×any), PerformanceHeatMap (1×unused), RSIBars (1×unused), PartnerAnalytics (1×memoization). Zero warnings in this TO's scope. |
| `comp-transform fields SecurityScanner` | After-commit mandate | INFO (0 fields) | Expected — orchestrator composes tabs; field rendering is inside UniverseDataTab / UniverseScannerTab / FactorBankTab. SecurityScanner.tsx itself doesn't render fetched data fields directly. Same result as TO-1; not a regression. |

---

## Acceptance Criteria Evidence

Smoke runner: `portal/.frontend-dev/runners/sscn_divdef_001_runner.mjs` (extended for `expect_substring`). Result JSON: `portal/.frontend-dev/screenshots/sscn_divdef_001/result.json`. New screenshot: `portal/.frontend-dev/screenshots/sscn_divdef_001/sscn-divdef-005-universe-dropdown-set.png`.

**Summary: 24 / 24 assertions PASS across all 4 scenarios.**
 - TO-1 scenarios (default-state + 13-factors-and-step + scanner-tab): 13 + 4 + 2 = 19 PASS — no regression from `45ea7210`.
 - TO-1b scenario (AC10 dropdown-set): 5 sub-AC PASS + no console errors.

| AC | Status | Evidence |
|----|--------|----------|
| AC1 — UNIVERSE_IDS exactly 5 entries with §3.5 values | PASS | `git diff portal/src/api/endpoints/security-scanner.ts:28-37` shows 5 entries: sp500/wt_ivv, r1000/wt_iwb, rmidcap/wt_iwr, sp400/wt_ijh, msciusa/wt_csus. Legacy 4 removed. |
| AC2 — US_ONLY_UNIVERSES contains all 5; Set form retained; decision documented | PASS | `constants.ts:11-19` retains `ReadonlySet<UniverseId>`. Decision rationale captured in commit message + this log. |
| AC3 — UniverseId union = 5 v0.2 entries | PASS | `types.ts:30` = `'sp500' \| 'r1000' \| 'rmidcap' \| 'sp400' \| 'msciusa'`. Legacy 4 dropped. |
| AC4 — DEV first-load: 5 dropdown options in §3.5 order; r1000 preselected; 3 new universes 404 OK pre-TO-2 | PASS | Smoke AC10.1-AC10.5 raw observed: `count:5, values:["sp500","r1000","rmidcap","sp400","msciusa"], labels:["S&P 500","Russell 1000","Russell Midcap","S&P MidCap 400","MSCI USA Index"], selected_value:"r1000"`. 3-new-universe 404 caveat NOT exercised in this smoke (smoke stayed on default Russell 1000 path; would 404 if user switched to rmidcap/sp400/msciusa pre TO-AE-1+TO-2; acceptable DEV state per TO context). |
| AC5 — Country column hidden across all 5 universes (US-only) | PASS (structural) | US_ONLY_UNIVERSES Set contains all 5 v0.2 tokens; consumers query `.has(universeId)` and resolve true for any selection. No live universe-switch exercised in smoke; verified by code path. |
| AC6 — comp-transform schema-check SecurityScanner PASS | PASS | Phase 4 result: "All rendered fields match their response types." |
| AC7 — bun typecheck + lint exit 0 | PASS | Both clean; zero new warnings in scope. |
| AC8 — Playwright smoke against extended constitution PASS modulo AC4 caveat | PASS | 24/24 assertions across 4 scenarios. AC4 caveat path not exercised; rest of AC8 verified end-to-end. Console errors = 0 across all scenarios. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/api/endpoints/security-scanner.ts` | UNIVERSE_IDS swap 6→5 (rmidcap/sp400/msciusa added; r1000v/acwx/eafe/eafev removed) | Yes — DEV `b302f5cf` |
| `portal/src/pages/SecurityScanner/types.ts` | UniverseId union swap | Yes — DEV `b302f5cf` |
| `portal/src/pages/SecurityScanner/constants.ts` | US_ONLY_UNIVERSES tokens updated (Set form retained) | Yes — DEV `b302f5cf` |
| `portal/.frontend-dev/testing/sscn_divdef_001_smoke.json` | Extended with `sscn-divdef-005-universe-dropdown-set` scenario (5 AC10 sub-assertions) | Yes — DEV `b302f5cf` |

`b302f5cf` net delta: 4 files, +68 / -10. Two prior DE commits on this DIVZ feature lineage:
 - `45ea7210` (TO-1 functional ship)
 - `2254437c` (TO-1 smoke constitution add)

Total push-ready stack on portal DEV from this DIVZ feature: **3 commits, 9 files, +300 / -25**.

---

## Current State

All 8 acceptance criteria met. Portal commit `b302f5cf` ready for DT push to remote DEV. Universe-set migration is FE-only and structurally orthogonal to TO-AE-1 (Lambda redeploy) — the 3 new universes will 404 on data load until TO-AE-1 + TO-2 re-fire writes `latest/universes/{rmidcap,sp400,msciusa}/`; DEV-only transient state, acceptable per TO context. PROD push gates per TO-4 framework (TO-1 + TO-1b + TO-3 close + Andrew DEV smoke).

## Next Steps

- [Dashboard Engineer] RAVC2 to `2.0.0_SA_COO~B` + CC `1.0.0_SA_CTO~B` with `b302f5cf` + smoke evidence (this log).
- [Dashboard Engineer] Flip TO status to `complete` on RAVC2 receipt.
- [Dashboard Engineer] MCP `0.3.0_DT_TradingOperations` updating push-ready inventory: now 3 commits (`45ea7210` + `2254437c` + `b302f5cf`), 9 files, +300/-25 on portal DEV.
- [DevOps 0.3.0_DT] PROD push remains gated on TO-3 close + Andrew DEV smoke + AE TO-AE-1 close (the 3-new-universe AC4 data-load can only verify post-Lambda redeploy + data re-fire).
