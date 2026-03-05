# SSCN Wave 2 QA Fixes — 0.3.0_DE_TradingOperations

**Date:** 2026-03-05
**Task Order:** SSCN_PORTAL-002 (QA gate — design contract compliance)
**Status:** COMPLETE

---

## Context

RD (0.3.4_RD_SecurityScanner) shipped the full SecurityScanner page implementation at
commit `cf16ff4`. This log covers DE's QA pass and the two follow-on fix commits required
to achieve a clean `bunx tsc -b` and a correct XLSM-sourced category taxonomy.

---

## Fix 1 — TSC Errors in RD Implementation

**Commit:** `4460041`
**Author:** 0.3.0_DE_TradingOperations

### Error 1 — SecurityScanner.tsx:73

```
Type '(tab: TabType) => void' is not assignable to type '(tabId: string) => void'
```

Root cause: `useTabNavigation<TabType>` types `handleTabChange` as `(tab: TabType) => void`.
`TabNavigation.onTabChange` prop is `(tabId: string) => void`. `TabType` is narrower than
`string`, making direct assignment invalid under function parameter contravariance.

Fix (`SecurityScanner.tsx` line 73):
```typescript
// Before:
onTabChange={handleTabChange}
// After:
onTabChange={(id) => handleTabChange(id as TabType)}
```

### Errors 2 & 3 — UniverseScannerTab.tsx:151, :182

```
Type 'string | undefined' is not assignable to type 'string | number'
```

Root cause: AG Grid's `CellStyle` is `Record<string, string | number>`. RD's cellStyle
functions returned object literals with ternary operators that could produce `undefined`
values (e.g. `color: p.value != null ? '#000000' : undefined`).

Fix: Replaced object literal style with imperative conditional property assignment:
```typescript
const style: Record<string, string | number> = { textAlign: 'right', fontFamily: 'monospace', fontWeight: '600' }
if (p.value != null) style.color = '#000000'
if (bg) style.backgroundColor = bg
if (p.value == null) style.opacity = 0.4
return style
```
Applied to both compositeScore column (line 151) and pctlCols array (line 182).

TSC gate: `bunx tsc -b` PASSED after fix.

---

## Fix 2 — categoryOrder.ts: Wrong 11 Categories → Correct 18 XLSM Categories

**Commit:** `bb3759b`
**Author:** 0.3.0_DE_TradingOperations

### Root Cause

`categoryOrder.ts` was seeded with 11 categories derived from `V0_SYSTEM_REFERENCE.md`,
which is an aggregated/simplified view that does not reflect the actual XLSM Tab 3 row
data. The XLSM actually has 18 categories.

V0 had: `size, efficiency, growth, management, profitability, quality, sentiment,
systematic, value, yield, institutional`

RD's categories were wrong (e.g. `sentiment`, `systematic`, `yield`, `institutional`
do not exist in the XLSM; `solvency`, `analyst`, `governance`, `crowding`, `insider`,
`short`, `beta`, `volatility`, `liquidity`, `momentum`, `technical` are all XLSM-native
and were missing or miscategorized).

### Resolution

DE extracted Tab 3 ("3-Factor Data") from the XLSM directly via Python/openpyxl.
287 factors confirmed. 18 categories extracted with their actual XLSM names.

`categoryOrder.ts` updated:
```typescript
export const CANONICAL_CATEGORY_ORDER = [
  'size', 'efficiency', 'growth', 'management', 'solvency',
  'profitability', 'quality', 'value', 'analyst', 'governance',
  'crowding', 'insider', 'short', 'beta', 'volatility',
  'liquidity', 'momentum', 'technical',
] as const
```

Order mirrors `portal/src/utils/factorOrder.ts` for the 15 overlapping groups;
solvency, volatility, and liquidity inserted in logical positions.

Also updated: comment block referencing the 18-category XLSM source and noting
supersession of V0_SYSTEM_REFERENCE.md's 11-group aggregated view.

TSC gate: `bunx tsc -b` PASSED.

---

## XLSM Registry Rewrite (CLOUD branch)

In parallel, DE rewrote `infra/aws/lambda/opal_security_scanner_processor/factor_metadata_registry.json`
and `docs/architecture/security-scanner-source/factor_metadata_registry.json` on the CLOUD
branch (commit `7811afcb`). DS's registry used domain-knowledge-derived categories and null
IC/coverage values. DE replaced it with authoritative XLSM Tab 3 data:
- 287 factors (XLSM-exact)
- 18 categories (matching corrected categoryOrder.ts)
- Real IC, coveragePct, autocorrelationPct values from XLSM columns
- XLSM-validated relationship directions (Positive: 187, Inverse: 100)

---

## Full Portal DEV Commit Chain (ready for DT push)

| Commit | Author | Content |
|--------|--------|---------|
| `4b5aac8` | DE | colorUtils + factorOrder extraction to portal/src/utils/ |
| `a796555` | DE | security-scanner.ts endpoint file |
| `d473304` | RD | DESIGN_SPEC.md + types.ts |
| `cf16ff4` | RD | Full SecurityScanner page implementation |
| `4460041` | DE | TSC fixes (onTabChange cast + cellStyle undefined guards) |
| `bb3759b` | DE | categoryOrder.ts — 18 XLSM categories (was 11 wrong) |

Note: commits `b0a33d7` and `1c61990` appear between SSCN commits — these are unrelated
portal fixes that also need to go up with the branch push.

---

## Signal to DT

**0.3.0_DT_TradingOperations: Wave 2 push is ready.**

Portal DEV branch has all SSCN commits through `bb3759b`. `bunx tsc -b` passes.
Push the full portal submodule DEV branch. Per task order SSCN_PORTAL.001-002:
- [ ] DT: push portal submodule DEV branch
- [ ] DT: update deployment_map.xml per task order requirement 5

After push: AWS infrastructure is already live (AE deployed security-scanner-v1.0.0).
End-to-end validation requires a real FactSet upload via the presign route — that is
DevOps / first-use gate, not a DT gate.
