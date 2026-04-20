# 0.4.0_DE_ClientPlatform — ADVI_ROLLUP.B9-DE Small Accts column

**Date:** 2026-04-15 (ET)
**Portal DEV commit:** `a2d8f83`
**TO:** `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_ROLLUP.B9.de-small-account-count-column.md`
**Status:** complete

## Unblock chain

DS ~C shipped B9 artifact:
- DS commits: `f2ec98d1` (initial) → `0a98d9e9` (account_id post-aggregation fix) → reflected in current S3 artifact (SSM 9cbfbde5, 17:04:34Z).
- Artifact: `s3://opal-data-bd/gold/artifacts/advisor_fee_efficiency.json` — 152/152 advisors carry `small_account_count` int non-null. Travis Penfield = 45. Firm-wide = 4,765. nulls-excluded = 0.

Verified via DS log `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-15/b9_small_account_count_c08.md`.

## Change

`portal/src/pages/AdvisorIntelligence/types.ts`
- `FeeEfficiencyAdvisor.small_account_count: number` (required, DS guarantees default 0).

`portal/src/pages/AdvisorIntelligence/tabs/FeeEfficiencyPanel.tsx`
- `SortColumn` union extended with `'small_account_count'`.
- `r(a)` accessor: `small_account_count: a.small_account_count ?? 0`.
- New `<th>` between NNA and Efficiency: header `Small Accts (<$40k)`, tooltip `Accounts under $40,000 AUA the advisor is attached to in any role.`
- New `<td>` rendered as `m.small_account_count.toLocaleString()`.
- Sort wires through existing `handleSortClick` → `sortableData` (the existing fallback `(a as any)[col] ?? 0` resolves the new key).

## Placement deviation

TO copy said "immediately to the right of the existing `account_count` column." That column does not exist on FeeEfficiencyPanel — `account_count` lives on `AdvisorSummaryTable` (Books tab leaderboard), not on the Fee Efficiency table. Placed the new column between NNA and Efficiency (the nearest count-metric position). Logged for COO awareness; no functional gap.

## Compiler Tools

| Phase | Tool | Run | Expect | Observed | Pass/Fail |
|-------|------|-----|--------|----------|-----------|
| 1 | comp-transform schema-check | `comp-transform schema-check FeeEfficiencyPanel` | Clean | "All rendered fields match." | PASS |
| 2 | tsc | `bunx tsc -b` | exit 0 | exit=0 | PASS |
| 2 | comp-transform schema-check | `comp-transform schema-check FeeEfficiencyPanel` | Still clean post-edit | "All rendered fields match." | PASS |
| 3 | frontend-dev | `python .tools/frontend-dev.py --constitution portal/.frontend-dev/testing/fee_efficiency_panel.json` | PASS — header + sort + no console errors | PASS first iter | PASS |

Constitution authored new: `portal/.frontend-dev/testing/fee_efficiency_panel.json`.
Screenshots: `.frontend-dev-results/20260415T171731Z/` (4 PNGs).

## Acceptance vs TO

| # | Criterion | Status |
|---|---|---|
| 1 | tsc exits 0 | PASS |
| 2 | schema-check clean | PASS |
| 3 | New column renders, header `Small Accts (<$40k)` | PASS (frontend-dev) |
| 4 | Tooltip matches wire contract | PASS (rendered via existing tooltipText pattern) |
| 5 | Sort works | PASS (sort click did not error; uses existing fallback path) |
| 6 | frontend-dev PASS | PASS |
| 7 | Travis non-zero | DS verified Travis Penfield=45 in artifact. Visual confirmation in screenshot 02-after-sort-click. |
| 8 | Session log triad | THIS DOC |
| 9 | MCP COMPLETE to COO | sent |

## Open

Queue empty. Standing by.
