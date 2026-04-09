# ADVI_49PUSH.046 -- Fee Table UI Fixes (fix_1 + fix_2)
**Date:** 2026-04-09
**Instance:** 0.4.0_DE_ClientPlatform~D
**Task Order:** ADVI_49PUSH.046
**Status:** fix_1 and fix_2 complete; fix_3 blocked on DS .045

**Portal DEV commit:** `16f0552`

---

## Work Summary

### fix_1 -- Ordinal formatting utility

Created `portal/src/lib/formatOrdinal.ts` using `Intl.PluralRules('en-US', { type: 'ordinal' })`.
Handles all edge cases including 11th/12th/13th, 21st/22nd/23rd, 83rd, 91st, 92nd, 93rd.

Searched all ADVI components for naive ordinal patterns (`${n}th`, `Math.round.*th`).
Found exactly two occurrences, both in FeeEfficiencyPanel.tsx:
- Line 337 (scatter tooltip): `{Math.round(m.pctile)}th percentile` -> `{formatOrdinal(m.pctile)} percentile`
- Line 446 (table cell): `{Math.round(m.pctile)}th` -> `{formatOrdinal(m.pctile)}`

No other ADVI components had hardcoded ordinals.

### fix_2 -- Fee efficiency table: column sort + rounded edges

**Sort implementation:**
- Added `SortColumn` and `SortDirection` types (neutral/desc/asc)
- Sort state: `sortColumn` (default `'pctile'`), `sortDirection` (default `'desc'`)
- `handleSortClick`: clicking same column cycles neutral->desc->asc->neutral; clicking new column resets to desc
- `sortableData` useMemo now uses sort state instead of hardcoded commission sort
- `setSelectedPeriod` wrapper resets sort to `pctile` / `desc` on period window change

**Column headers:**
- All 6 columns are clickable; `ChevronDown` (desc, opacity 70%) and `ChevronUp` (asc, white) from lucide-react
- Active column header text = white; inactive = white/80
- `flex-row-reverse` on right-aligned headers so icon appears to the left of text (visually after label, natural reading order)

**HelpCircle tooltip on Efficiency header:**
- Hover tooltip: "Percentile rank based on fee cost relative to net new assets. Higher = more efficient. Advisors with negative NNA are ranked separately below positive-NNA peers."
- Click on HelpCircle stopPropagation so it doesn't trigger sort

**Rounded table container:**
- Changed outer `<div>` to `rounded-lg overflow-hidden` with `overflowY: 'auto'`
- `overflow-hidden` clips table cell corners so first/last rows respect border radius

**Drilldown console.error (per drilldown_note):**
- Table row `onClick` now logs `console.error('[FeeEfficiencyPanel] drilldown: onAdvisorClick not provided', { advisor, period })` when `onAdvisorClick` is absent
- This surfaces the failure mode (missing callback vs 404 vs 401) for the next diagnostic TO

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| portal/src/lib/formatOrdinal.ts | New utility -- Intl.PluralRules ordinal formatter | Yes -- DEV `16f0552` |
| portal/src/pages/AdvisorIntelligence/tabs/FeeEfficiencyPanel.tsx | fix_1 + fix_2 -- ordinals, sort, rounded edges, HelpCircle, drilldown error | Yes -- DEV `16f0552` |

---

## Task Order Status

| Task Order | Status |
|---|---|
| ADVI_49PUSH.046 fix_1 | DONE -- `16f0552` |
| ADVI_49PUSH.046 fix_2 | DONE -- `16f0552` |
| ADVI_49PUSH.046 fix_3 | BLOCKED -- awaiting DS .045 findings on ratio column identity |
| ADVI_49PUSH.026 | BLOCKED -- awaiting DS .025 + AE chain re-run |
| ADVI_49PUSH.020 | PENDING -- awaiting gold re-run completion + DT .021 PII fix |

---

## Next Steps

1. **[DS 0.4.0_DS]** DS .045 -- investigate ratio column in fee_efficiency.json (is it commission/nna, fee_bps as %, or regression_residual?). Report findings so DE can complete fix_3 (rename column label + confirm Efficiency tooltip accuracy).
2. **[DE ~D me]** Once DS .045 reports: apply fix_3 -- rename ratio column header, verify Efficiency tooltip language matches actual computation.
3. **[AE 0.7.0]** Gold chain re-run for .020 unblock + .026 unblock.
4. **[DT 0.4.0_DT]** Portal DEV push (now 4 commits ahead of origin/DEV after ~A/~B/~C work plus this commit).
