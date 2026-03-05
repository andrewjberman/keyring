# SSCN_PORTAL-002 Shared Utils Extraction + Endpoint File — 0.3.0_DE_TradingOperations

**Date:** 2026-03-05
**Task Order:** `SSCN_PORTAL.001-002.shared-utils-extraction-proxy-routes.md`
**Status:** COMPLETE

---

## Work Completed

### 1. colorUtils.ts extraction

- Read `portal/src/pages/PortfolioManagement/utils/colorUtils.ts`
- Created `portal/src/utils/colorUtils.ts` (verbatim copy — identical exports)
  - `getGradientBackground(value, min, max, inverted?)`
  - `getWhiteToGreenGradient(value, min, max)`
- Updated consumers to `@/utils/colorUtils`:
  - `portal/src/pages/PortfolioManagement/tabs/ModelTab.tsx` (line 20)
  - `portal/src/pages/PortfolioManagement/components/PortfolioGrid.tsx` (line 6)
- Deleted PM-local `colorUtils.ts` (was untracked; rm'd from filesystem)

### 2. factorOrder.ts extraction

- Read `portal/src/pages/PortfolioManagement/utils/factorOrder.ts`
- Created `portal/src/utils/factorOrder.ts` (verbatim copy — identical exports)
  - `CANONICAL_GROUP_ORDER` (15-group PM/Yang taxonomy)
  - `CanonicalGroup` type
  - `canonicalGroupIndex(group)`
- Updated consumers to `@/utils/factorOrder`:
  - `portal/src/pages/PortfolioManagement/tabs/ModelTab.tsx` (line 21)
  - `portal/src/pages/PortfolioManagement/tabs/AlphaTab.tsx` (line 21)
  - `portal/src/pages/PortfolioManagement/components/SecurityDetailModal.tsx` (line 11)
- Deleted PM-local `factorOrder.ts` (was untracked; rm'd from filesystem)

### 3. Grep verification

Confirmed zero remaining imports from PM-local paths:
- Pattern `PortfolioManagement/utils/colorUtils` — 0 matches
- Pattern `PortfolioManagement/utils/factorOrder` — 0 matches
- Pattern `from '../utils/colorUtils'` — 0 matches
- Pattern `from '../utils/factorOrder'` — 0 matches

### 4. TSC gate (extraction)

`cd portal && bunx tsc -b` — PASSED (zero errors)

### 5. Extraction commit

```
commit 4b5aac8
Author: 0.3.0_DE_TradingOperations <0.3.0_DE_TradingOperations@opal.agent>
Message: 0.3.0_DE_TradingOperations: extract colorUtils + factorOrder to portal/src/utils/ (SSCN_PORTAL-002)
Files: 6 changed (2 new: shared utils; 4 modified: PM import paths)
```

### 6. security-scanner.ts endpoint file

Created `portal/src/api/endpoints/security-scanner.ts`:
- `UNIVERSE_IDS` constant (6 universes: sp500, r1000, r1000v, acwx, eafe, eafev)
- `UniverseId` type
- `getSecurityScannerFactors()` — GET /api/scoped/security-scanner/factors
- `getUniverseData(universeId)` — GET /api/scoped/security-scanner/universe/${universeId}/data
- `getUniverseScanner(universeId)` — GET /api/scoped/security-scanner/universe/${universeId}/scanner
- Return types: `any` with TODO comment pending RD's types.ts
- Auth: Bearer token from localStorage (dev-gated scoped route)

### 7. TSC gate (endpoint file)

`cd portal && bunx tsc -b` — PASSED (zero errors)

### 8. Endpoint commit

```
commit a796555
Author: 0.3.0_DE_TradingOperations <0.3.0_DE_TradingOperations@opal.agent>
Message: 0.3.0_DE_TradingOperations: add SSCN API endpoint functions (SSCN_PORTAL-001)
Files: 1 new file (security-scanner.ts, 98 lines)
```

---

## Signal to DT

**0.3.0_DT_TradingOperations: Wave 1 push is ready.**

Two commits on portal DEV:
1. `4b5aac8` — extraction (colorUtils + factorOrder to portal/src/utils/)
2. `a796555` — SSCN API endpoint file

Pre-push QA checklist (per task order SSCN_PORTAL.001-002.push-and-deploy.md, Requirement 2):
- [x] Grep confirms zero stale PM-local imports
- [x] `bunx tsc -b` passes (both after extraction and after endpoint commit)
- [x] ModelTab.tsx and PortfolioGrid.tsx import gradient utils from `@/utils/colorUtils` (verified)
- [ ] DT: push portal submodule DEV branch

After Wave 1 push: RD (0.3.4_RD_SecurityScanner) is unblocked to begin
DESIGN_SPEC.md. DE must review and approve DESIGN_SPEC.md before RD writes
any .tsx (SSCN_DESIGN_CONTRACT.md Section 10 gate).

---

## Task Order Status

`SSCN_PORTAL.001-002.shared-utils-extraction-proxy-routes.md` — COMPLETE
All 6 acceptance criteria met:
1. portal/src/utils/colorUtils.ts exists with identical exports
2. portal/src/utils/factorOrder.ts exists with identical exports
3. PM-local copies deleted
4. All PM files import from shared path (grep confirmed)
5. bunx tsc -b passes (extraction + endpoint commits)
6. portal/src/api/endpoints/security-scanner.ts exists with 3 functions + UNIVERSE_IDS
7. Two separate commits produced
