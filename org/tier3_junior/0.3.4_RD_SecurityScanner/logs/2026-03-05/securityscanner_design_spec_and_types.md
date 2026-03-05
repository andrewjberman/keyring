# SecurityScanner DESIGN_SPEC.md + types.ts — 0.3.4_RD_SecurityScanner

**Date:** 2026-03-05
**Portal DEV commit:** `d473304`

## Objective

Execute first phase of task order SSCN_PORTAL.001-002.page-implementation.md.
Ship the two pre-gate deliverables that have no DE dependency:
1. DESIGN_SPEC.md — blueprint document that gates all .tsx work
2. types.ts — 6 TypeScript interfaces from SSCN_DATA_CONTRACT.md Section 5

---

## Work Completed

### 1. Startup orientation

Read AGENT_START_HERE.md, agent README + prompt, page_inventory.xml, task order
SSCN_PORTAL.001-002.page-implementation.md. Read both contracts:
- docs/architecture/SSCN_DESIGN_CONTRACT.md (component reuse, table primitives,
  gradient semantics, page shell, ScannerHeaderPanel, DESIGN_SPEC gate)
- docs/architecture/SSCN_DATA_CONTRACT.md (field names, TypeScript interfaces,
  API routes, null semantics)

Read thread receipt SSCN_PORTAL-002 (all 8 turns). Confirmed all design decisions
are locked. Checked DE upstream log (2026-03-05/sscn_data_contract_deliverable.md):
- Data contract complete. DE confirmed I can start DESIGN_SPEC.md + types.ts now.
- DE task order SSCN_PORTAL.001-002.shared-utils-extraction-proxy-routes.md is
  PENDING — shared utils extraction not yet committed. Correctly enforcing gate:
  will not wire @/utils/colorUtils imports until DE signals extraction committed.

Read reference files:
- docs/architecture/security-scanner-source/V0_SYSTEM_REFERENCE.md
  -> confirmed 11 factor categories in canonical order
- portal/src/pages/PortfolioManagement/tabs/AlphaTab.tsx
  -> AlphaTab visual language reference (table styling, header actions, sort)
- portal/src/pages/PortfolioManagement/components/OptimizationSummaryHeader.tsx
  -> sticky panel pattern for ScannerHeaderPanel

### 2. Authored portal/src/pages/SecurityScanner/DESIGN_SPEC.md

Full blueprint covering all 9 required content items per SSCN_DESIGN_CONTRACT.md
Section 10:

| Item | Location in doc |
|------|----------------|
| ASCII layout (page shell + 4 tabs) | Sections 4, 5A-5E |
| AG Grid mandate Tabs 2+4 + justification | Section 8 |
| Tab 4 default columns (raw hidden, toggle far right) | Section 5E-1, 5E-2 |
| Shared util import paths | Section 2 |
| SSCN-local category order path | Section 2 |
| ScannerHeaderPanel sticky above TabNavigation | Section 6 |
| 11 SSCN factor categories in canonical order | Section 3 |
| Panel hierarchy per tab | Sections 5B-5E |
| Design tokens reference | Section 11 |

Also documented: gradient formula (Section 5E-3), composite/rank computation
(Section 5E-4), ScannerHeaderPanel props interface (Section 6), FactorChip
(Section 7), API hooks pattern (Section 9), state hook shape (Section 10),
loading/error/empty state requirement (Section 12).

### 3. Authored portal/src/pages/SecurityScanner/types.ts

All 6 interfaces from SSCN_DATA_CONTRACT.md Section 5 with exact field names:
- FactorDefinition (9 fields including systematic 'Yes'|'No')
- UniverseDataRow (8 fields including country: string | null, values Record)
- ScannerRow (8 fields including pctls Record — sign inversion already applied server-side)
- FactorMetadataResponse, UniverseDataResponse, ScannerDataResponse (envelopes)

Client-computed extension:
- ScannerRowWithScore extends ScannerRow { compositeScore: number | null; rank: number }

Additional page types:
- TabType ('factor-bank' | 'universe-data' | 'factor-data' | 'universe-scanner')
- UniverseId ('sp500' | 'r1000' | 'r1000v' | 'acwx' | 'eafe' | 'eafev')
  (defined here so useScannerState can be typed without importing from pending
  DE endpoint file; DE can re-export or align when creating security-scanner.ts)

### 4. Updated page_inventory.xml

Changed status from "scaffold -- no files shipped yet" to "in progress".
Added file entries for DESIGN_SPEC.md and types.ts with status annotations.
Updated api_calls comment to reference correct data contract path.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Define UniverseId in types.ts (not only in DE's endpoint file) | DE's security-scanner.ts is pending. useScannerState needs this type. Can be aligned/re-exported when DE creates the endpoint file. |
| Gradient formula documented as p-50, -50, 50 (not p, 0, 100) | Per SSCN_DESIGN_CONTRACT.md Section 5 — approved by DE in thread turn 6. Centers neutral at 50th pctl. |
| setEqualWeight uses Math.floor + remainder to first | Simple integer distribution; avoids floating point weight inputs that sum to 99.9%. Decision deferred to implementation but flagged here. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/SecurityScanner/DESIGN_SPEC.md` | Created — full design blueprint | Yes — `d473304` (portal DEV) |
| `portal/src/pages/SecurityScanner/types.ts` | Created — 6 interfaces + extensions | Yes — `d473304` (portal DEV) |
| `org/tier3_junior/0.3.4_RD_SecurityScanner/deliverables/page_inventory.xml` | Status updated; file entries added | Yes — parent CLOUD commit |
| `org/tier3_junior/0.3.4_RD_SecurityScanner/logs/2026-03-05/securityscanner_design_spec_and_types.md` | This log | Yes — parent CLOUD commit |

---

## Blockers

- BLOCKED (soft gate) on `0.3.0_DE_TradingOperations`:
  DESIGN_SPEC.md must be reviewed and approved before any .tsx file is written.
  Evidence: SSCN_DESIGN_CONTRACT.md Section 10 ("Gate") + task order requirement 2.
  DE's task order SSCN_PORTAL.001-002.shared-utils-extraction-proxy-routes.md
  is pending — when DE completes it, DESIGN_SPEC approval is the expected next
  signal before I proceed with components.

- DEPENDENCY on `0.3.0_DE_TradingOperations`:
  shared-utils-extraction (colorUtils + factorOrder to @/utils/) must be committed
  before I wire any import from @/utils/colorUtils in SSCN component files.
  Not blocking DESIGN_SPEC.md or types.ts. Will block .tsx wiring step.

---

## Current State

**Status:** IN PROGRESS (gated on DE review of DESIGN_SPEC.md)
**Active branch:** portal submodule DEV | parent repo CLOUD

DESIGN_SPEC.md and types.ts are committed to portal DEV (`d473304`).
page_inventory.xml updated. Session log written. Parent CLOUD commit pending.

All design decisions from SSCN_PORTAL-002 are reflected in DESIGN_SPEC.md.
types.ts has zero imports — it is a pure type definition file. tsc will pass
trivially for these two files; full tsc gate runs after .tsx components are wired.

Waiting on: DE approval of DESIGN_SPEC.md before writing any .tsx file.

---

## Next Steps

1. **[0.3.0_DE_TradingOperations] Review and approve DESIGN_SPEC.md** — gate for
   all .tsx work. Review portal DEV commit `d473304`. Signal approval in their
   session log or task order update.

2. **[0.3.0_DE_TradingOperations] Complete shared-utils extraction** — move
   colorUtils.ts + factorOrder.ts to @/utils/; create security-scanner.ts endpoint.
   This unblocks SSCN .tsx wiring step.

3. **[0.3.4_RD_SecurityScanner] After DE approval + extraction** — proceed in order:
   a. utils/categoryOrder.ts (11 categories, no DE dependency)
   b. utils/quintileUtils.ts (null detection, cell style factory)
   c. components/FactorChip.tsx
   d. hooks/useScannerState.ts
   e. hooks/useScannerApi.ts (imports from DE's security-scanner.ts)
   f. components/ScannerHeaderPanel.tsx
   g. SecurityScanner.tsx (page shell)
   h. tabs/FactorBankTab.tsx, FactorDataTab.tsx (HTML tables, no AG Grid)
   i. tabs/UniverseDataTab.tsx, UniverseScannerTab.tsx (AG Grid)
   j. index.ts (re-export)

4. **[0.3.4_RD_SecurityScanner] TSC gate** — run bunx tsc -b from portal/ before
   signaling DT. Must pass with zero errors.

5. **[0.3.0_DT_TradingOperations] Push portal DEV** — after RD signals complete
   and tsc passes.

**Files to touch next (in order, after DE approval):**
- `portal/src/pages/SecurityScanner/utils/categoryOrder.ts` — 11 categories,
  CANONICAL_CATEGORY_ORDER, canonicalCategoryIndex
- `portal/src/pages/SecurityScanner/utils/quintileUtils.ts` — null helpers,
  cell style factory for AG Grid
- `portal/src/pages/SecurityScanner/components/FactorChip.tsx` — factor pill UI

**Do NOT:**
- Write any .tsx file until DESIGN_SPEC.md is approved by 0.3.0_DE_TradingOperations
- Import from portal/src/pages/PortfolioManagement/utils/ in any SSCN file
  (those paths are being removed by DE extraction)
- Import from @/utils/colorUtils until DE confirms extraction is committed
- Import from @/api/endpoints/security-scanner until DE creates that file
