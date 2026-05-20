# Session Log — SSCN_DIVDEF.011 Equal Weight remainder spread fix

**Agent:** 0.3.0_DE_TradingOperations (Dashboard Engineer — Trading Operations PM)
**Date:** 2026-05-20
**Task Order:** SSCN_DIVDEF.011 (issued by 2.0.0_SA_COO; root-caused + specified by 1.0.0_SA_CTO)
**Portal DEV commit:** `d71ac15b`
**Workspace CLOUD commit:** none (portal-only change)

## Current State

SSCN_DIVDEF.011 complete. The 2-line `buildEqualWeights()` fix shipped to portal DEV
(`d71ac15b`). All 4 ACs PASS. `/frontend-dev` smoke 25/25 green (Scenario 6 added to the
SSCN_DIVDEF runner). DEV only — PROD push is the DT lane (`.006` bundle: `.007` + `.008`
+ `.010` + `.011`).

## Postmortem: Equal Weight produced a broken distribution

### Root Cause

`portal/src/pages/SecurityScanner/hooks/useScannerState.ts` -> `buildEqualWeights()`
dumped the entire integer remainder onto `factors[0]`:

```
result[f.code] = i === 0 ? base + remainder : base
```

With the 13-factor DIVZ preset: `base = floor(100/13) = 7`, `remainder = 100 - 91 = 9`.
factor[0] got `7 + 9 = 16`, the other twelve got 7. Total summed to 100 but the
distribution was visibly broken — one outlier at 16%, twelve at 7%. Surfaced by Andrew's
2026-05-20 DEV smoke of the SSCN bundle.

### Resolution

Spread the remainder one point each across the first `remainder` factors:

```
result[f.code] = i < remainder ? base + 1 : base
```

13 factors -> factors 0-8 (i < 9) get 8, factors 9-12 get 7 -> 9x8 + 4x7 = 100, every
factor within 1 point of every other. Docstring updated to match.

## Work Completed

| File | Change | Committed |
|------|--------|-----------|
| portal/src/pages/SecurityScanner/hooks/useScannerState.ts | `buildEqualWeights()` line ~40 ternary + line ~32 docstring — spread remainder one point each | Yes — DEV `d71ac15b` |
| portal/.frontend-dev/runners/sscn_divdef_001_runner.mjs | Added Scenario 6 (Equal Weight smoke) — test harness, untracked, not committed | No (test tooling) |

Touched ONLY `buildEqualWeights()`. No other function, no other file in the fix commit.

Note (out of scope, follow-up nit): `portal/src/pages/SecurityScanner/DESIGN_SPEC.md`
lines 374 + 500 still describe "remainder to first factor". Left untouched per the TO
`do_not` rule (no other file). Flagged for a future doc-sync pass.

## Acceptance Criteria — Evidence

| AC | Result | Evidence |
|----|--------|----------|
| AC1 — DIVZ 13-factor Equal Weight = nine 8s + four 7s, sum 100 | PASS | Browser Scenario 6: weight inputs read `[8,7,7,8,7,7,8,8,8,8,8,8,8]` — count=13, eights=9, sevens=4, sum=100. Function assertion for 13 inputs also PASS. |
| AC2 — no factor more than 1 point off any other (max-min <= 1) | PASS | Scenario 6: `max-min=1`. |
| AC3 — `/frontend-dev` smoke green | PASS | `sscn_divdef_001_runner.mjs` 25/25 PASS (24 prior + 4 new `AC011_*`), 0 console errors across all 6 scenarios. result.json: `portal/.frontend-dev/screenshots/sscn_divdef_001/result.json`. |
| AC4 — `bun run typecheck` clean + `bun run lint` clean | PASS (with note) | `tsc -b --noEmit` 0 errors. `eslint` on the changed file `useScannerState.ts`: 0 errors, 0 warnings. Project-wide lint exits 1 on 11 PRE-EXISTING warnings (`react-hooks/preserve-manual-memoization`) in an unrelated AUA/Distribution component — not introduced by this change; `useScannerState.ts` is the only modified file (`git status` confirms). |

The 8s/7s are non-contiguous in the displayed table (`[8,7,7,8,...]`) because the factor
table renders `sortedFactors` (category-sorted) while `buildEqualWeights` assigns +1 by
`selectedFactors` (preset-entry) order. Cosmetically irrelevant — every factor is still
within 1 point (AC2 holds).

## Compiler Tools

| Tool | Result |
|------|--------|
| (none) | Per the TO `compiler_tools_mandate` phase 1, documented by CTO: this is a pure-logic 2-line helper fix with no rendered-field/schema surface — `comp-transform schema-check` is N/A. Phase 2/3 mandate is tsc + lint + `/frontend-dev` smoke, all run and green. |

## Decisions Made

- Extended the existing `sscn_divdef_001_runner.mjs` with Scenario 6 rather than writing
  a separate harness — keeps the SSCN_DIVDEF smoke a single 25-assertion suite. Runner is
  untracked test tooling, not committed (fix commit is `useScannerState.ts`-only).
- Did not commit the DESIGN_SPEC.md docstring drift — out of TO scope (`do_not`: no other
  file). Logged as a follow-up nit instead.

## Next Steps

- `[2.0.0_SA_COO]` RAVC4 on SSCN_DIVDEF.011 (RAVC2 COMPLETE sent with AC1-AC4 evidence).
- `[0.3.0_DT_TradingOperations]` Portal DEV commit `d71ac15b` joins the `.006` PROD bundle
  (`.007` + `.008` + `.010` + `.011`). Post-`.011`-close sequence per the TO: DT DEV push
  origin/DEV + :5175 refresh -> Andrew re-smoke of the Equal Weight fix -> `.006` PROD GO.
- `[1.0.0_SA_CTO]` CC'd on RAVC2 — may note `.011` in the v0.6 closeout.
