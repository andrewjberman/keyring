# 0.4.0_DE_ClientPlatform — ADVI_ROLLUP.B3b: Fee Window Revenue Binding

**Date:** 2026-04-16 ET
**Portal DEV commit:** `3ca28d0`
**GO:** COO MCP 2026-04-16 — "GO — ADVI_ROLLUP.B3b.de-fee-window-revenue-binding (commit 348cd0b4)"
**Status:** complete

## Work Completed

Three changes across types.ts + FeeSummaryPanel.tsx:

### 1. Types (types.ts)

- `FeeAccountTeamShare.window_fee_share_usd?: { qtd: number; ytd: number; max: number }` — window-scoped fee share per team attribution entry (optional until DS B3b ships)
- `FeeSummaryByAccount.window_revenue?: { qtd/ytd/max: { firm_revenue_usd, advisor_revenue_usd } }` — DS-aggregated window-scoped firm + advisor revenue (optional until DS B3b ships)

### 2. Revenue binding (FeeSummaryPanel.tsx — Relationship Summary)

Replaced hardcoded `annual_implied_revenue` with:
- `totalFirmRevenue = data.window_revenue?.[effectiveWindow]?.firm_revenue_usd ?? data.annual_implied_revenue`
- `windowAdvisorRevenue = data.window_revenue?.[effectiveWindow]?.advisor_revenue_usd ?? null` (DS aggregate path)
- `teamAdvisorRevenue` = sum of `share.window_fee_share_usd?.[effectiveWindow] ?? share.fee_share_usd` over team_attribution (existing per-share path, now window-aware)
- `advisorRevenue = windowAdvisorRevenue ?? teamAdvisorRevenue` — prefers DS aggregate when available

### 3. Team attribution split binding (FeeSummaryPanel.tsx — Accounts Summary table)

- `pickAdvisorSplitBps` extended: new optional `window` param; uses `share.window_fee_share_usd?.[window] ?? share.fee_share_usd` for bps calculation
- Accounts table call-site updated: `pickAdvisorSplitBps(feeRow, profileAdvisorId, effectiveWindow)`

**Fallback rule:** all paths fall back to annualized figures (`annual_implied_revenue`, `fee_share_usd`) when window fields are absent — panel renders correctly before DS artifact lands.

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/types.ts` | FeeAccountTeamShare.window_fee_share_usd?, FeeSummaryByAccount.window_revenue? | Yes — portal DEV `3ca28d0` |
| `portal/src/pages/AdvisorIntelligence/tabs/FeeSummaryPanel.tsx` | Revenue binding + pickAdvisorSplitBps window-aware | Yes — portal DEV `3ca28d0` |
| `portal/.frontend-dev/testing/fee_summary_window.json` | New constitution for B3b visual test | Yes — this org commit |
| `org/.../ADVI_ROLLUP.B3b.de-fee-window-revenue-binding.md` | Status flip pending -> complete | Yes — this org commit |

## Compiler Tools

| Phase | Tool | Run | Expect | Observed | Pass/Fail |
|-------|------|-----|--------|----------|-----------|
| Phase 1 (before write) | `comp-transform schema-check FeeSummaryPanel` | Pre-edit baseline | annual_implied_revenue in rendered set, window_revenue absent | Clean — all rendered fields match types | PASS |
| Phase 2 (before commit) | `bun run build` | Post-edit | Exit 0, no type errors | Exit 0 (tsc clean) | PASS |
| Phase 2 (before commit) | `comp-transform schema-check FeeSummaryPanel` | Post-edit | window_revenue in rendered set, no new MISSING | Clean — all rendered fields match types | PASS |
| Phase 3 (after commit) | `/frontend-dev fee_summary_window` | `fee_summary_window.json` | PASS, 0 console errors, annualized fallback renders | PASS, 1 iteration, 0 console errors | PASS |

## Next Steps

- `[DS]` B3b DS TO pending — once `window_revenue` and `window_fee_share_usd` land in client_detail.json artifact, window toggle on Fee Summary will auto-activate revenue values
- `[DT]` New portal DEV commits (B9b + B3b = `d77465e`, `3ca28d0`) pending PROD bundle decision from COO
