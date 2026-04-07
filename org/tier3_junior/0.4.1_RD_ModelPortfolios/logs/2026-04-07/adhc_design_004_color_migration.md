# ADHC_DESIGN-004 Color Migration + Design QA -- 0.4.1_RD_ModelPortfolios
**Date:** 2026-04-07
**Task Order:** ADHC_DESIGN.004.rd-color-migration-and-qa.md
**Status:** Complete

## Changes

### Color Migration (hex -> chartColors.ts imports)

**ModelPortfolios.tsx:**
- Added `import { PALETTE } from '@/lib/chartColors'`
- Replaced 7x `'#60a5fa'` fallback -> `PALETTE.blue400`
- Replaced 6x `'#C3CADA'` fallback -> `PALETTE.gray300`
- Replaced 2x `'#ffffff'` (ApexCharts donut labels) -> `PALETTE.white`
- Total: 15 hardcoded hex removed

**PeersTab.tsx:**
- Added `import { PALETTE, PEERS_QUARTILE_BANDS } from '@/lib/chartColors'`
- Replaced 1x `'#60a5fa'` fallback -> `PALETTE.blue400`
- Replaced `QUARTILE_COLORS` array (4 hardcoded HSL values) -> `PEERS_QUARTILE_BANDS` from chartColors.ts
- Total: 5 hardcoded color values removed

**chartColors.ts:**
- Added `PEERS_QUARTILE_BANDS` constant (4 HSL values for PeersTab quartile band fills)
- Exact same colors preserved: hsl(260,60%,50%), hsl(220,40%,60%), hsl(210,30%,70%), hsl(210,50%,45%)

### Design QA Fixes

1. **Focus indicators (PeersTab):** Added `focus:outline-none focus:ring-2 focus:ring-[hsl(var(--primary))]` to model selector buttons (lines 441-454)
2. **Tabular nums (PeersTab):** Added `tabular-nums` class to percentile value labels container

### Design QA Checklist Result

- Labels & Text: PASS (all control labels use canonical pattern)
- Color & Tokens: PASS (zero hardcoded hex after migration)
- Panels & Layout: PASS (Panel primitives used throughout)
- Interactions: PASS (hover states + focus indicators present)
- Consistency: PASS (text sizes and opacities consistent)

## Verification

- `bun run build`: SUCCESS (14.62s, no errors)
- Hex grep on both files: 0 matches
- Visual appearance preserved (all replacements are exact color matches)
