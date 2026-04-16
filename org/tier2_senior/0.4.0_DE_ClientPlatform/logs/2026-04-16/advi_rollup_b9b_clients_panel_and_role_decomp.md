# 0.4.0_DE_ClientPlatform — ADVI_ROLLUP.B9b: Small Account Clients Panel + Role Decomp

**Date:** 2026-04-16 ET
**Portal DEV commit:** `d77465e`
**GO:** COO MCP 2026-04-16 — "GO on both B9b DE TOs. Execute in order without stopping for a new GO between them."
**Status:** complete

## Work Completed

### TO 1: ADVI_ROLLUP.B9b.de-small-account-clients-panel

**Four changes across types + ClientsTable + AdvisorBookView + ClientsTab adapter:**

1. **types.ts** — three type additions:
   - `AdvisorClient.small_account_count?: number` — per-relationship small account count for client roster
   - `AdvisorBookResponse.summary.small_account_count?: number` — advisor aggregate via ClientsTab adapter path
   - `PlatinumAdvisorSummary.book.small_account_count?: number` — primary rendering path in AdvisorBookView

2. **ClientsTable.tsx** — Small Accts column + sort + red row highlight:
   - `showSmallAcctCol` flag: only renders when `clients.some(c => c.small_account_count != null)` — column is invisible until DS ships
   - `sortBy` state (`'aua' | 'small_account_count'`, default `'aua'`): click column header to toggle
   - `SortIcon` component: chevron indicator on active sort column header
   - "Small Accts" column cell: `c.small_account_count?.toLocaleString() ?? '—'`, bold red when `> 0`
   - Red row highlight: `bg-red-500/10 border-l-2 border-red-500` on any client where `small_account_count > 0`

3. **AdvisorBookView.tsx** — headline stat:
   - "Small Accts (<$40k)" metric in CanonicalBookView overview metrics array
   - Guarded: only emitted when `bookData.book.small_account_count != null`
   - Placed after Accounts stat

4. **ClientsTab.tsx** — adapter update:
   - Passes `small_account_count: plat.book.small_account_count` through in summary mapping at line 285

**COO pre-conditions confirmed applied:**
- Did NOT define local `SMALL_ACCOUNT_THRESHOLD = 40_000` — used `small_account_count > 0` check (count, not AUA threshold)
- `THRESHOLDS.SMALL_ACCOUNT_AUA` not needed in ClientsTable (threshold applies at account level, already done in AdvisorBookClientDetail.tsx per commit 6615b6b)
- Account-level highlight in AdvisorBookClientDetail already complete — no changes needed there

### TO 2: ADVI_ROLLUP.B9b.de-small-account-role-decomp

1. **types.ts** — `PlatinumAdvisorSummary.role_breakdown` value type extended:
   - Added `small_account_count?: number` to the inline Record value shape at line 2063

2. **AdvisorBookView.tsx** — "Small Accounts by Role" Panel:
   - New Panel below the Clients panel, rendered via IIFE
   - Filters `role_breakdown` entries to those with `small_account_count != null`
   - Returns null when no roles have the field (section fully hidden until DS ships)
   - Per-role cards: role label (capitalized), count, fraction (count / account_count if available), red/amber accent for `> 0`
   - Design: horizontal pill/card layout, compact — no new chart

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/pages/AdvisorIntelligence/types.ts` | 4 type additions (AdvisorClient, AdvisorBookResponse.summary, PlatinumAdvisorSummary.book, role_breakdown value) | Yes — portal DEV `d77465e` |
| `portal/src/pages/AdvisorIntelligence/panels/ClientsTable.tsx` | Small Accts column, sortBy state, red row highlight | Yes — portal DEV `d77465e` |
| `portal/src/pages/AdvisorIntelligence/AdvisorBookView.tsx` | Headline stat + Small Accounts by Role panel | Yes — portal DEV `d77465e` |
| `portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx` | Adapter: pass small_account_count through summary | Yes — portal DEV `d77465e` |
| `portal/.frontend-dev/testing/clients_panel.json` | New constitution for B9b-DE1 visual test | Yes — this commit |
| `portal/.frontend-dev/testing/role_breakdown_small_accts.json` | New constitution for B9b-DE2 visual test | Yes — this commit |
| `org/.../ADVI_ROLLUP.B9b.de-small-account-clients-panel.md` | Status flip pending -> complete | Yes — this commit |
| `org/.../ADVI_ROLLUP.B9b.de-small-account-role-decomp.md` | Status flip pending -> complete | Yes — this commit |

## Compiler Tools

| Phase | Tool | Run | Expect | Observed | Pass/Fail |
|-------|------|-----|--------|----------|-----------|
| Phase 1 (before write) | `comp-transform schema-check AdvisorBookView` | Pre-edit baseline | `accounts: BooksClientAccount[]` UNUSED, no pre-existing MISSING | UNUSED confirmed, no MISSING | PASS |
| Phase 1 (before write) | `comp-transform schema-check ClientsTab` | Pre-edit baseline | `accounts` UNUSED, no MISSING | UNUSED confirmed, no MISSING | PASS |
| Phase 2 (before commit) | `bun run build` | Post-edit | Exit 0, no type errors | Exit 0 (tsc clean, 3272 modules transformed) | PASS |
| Phase 2 (before commit) | `comp-transform schema-check AdvisorBookView` | Post-edit | No new MISSING; rendered fields increases | type_fields=28, rendered_fields=4, no MISSING | PASS |
| Phase 2 (before commit) | `comp-transform schema-check ClientsTab` | Post-edit | No new MISSING; small_account_count in type | type_fields=18 for AdvisorBookResponse, no MISSING | PASS |
| Phase 3 (after commit) | `/frontend-dev clients_panel` | `clients_panel.json` constitution | PASS, 0 console errors | PASS, 0 issues, 1 iteration | PASS |
| Phase 3 (after commit) | `/frontend-dev role_breakdown_small_accts` | `role_breakdown_small_accts.json` constitution | PASS, 0 console errors | PASS, 0 issues, 1 iteration | PASS |

## Acceptance Criteria Status

### B9b-DE1 (clients panel)
| # | Criterion | Status |
|---|-----------|--------|
| 1 | bun run build exits 0 | PASS |
| 2 | comp-transform schema-check AdvisorBookView clean | PASS |
| 3 | comp-transform schema-check ClientsTab clean | PASS |
| 4 | Client list shows "Small Accts" column (guarded until DS ships) | PASS — hidden when field absent |
| 5 | Rows where small_account_count > 0 have red accent | PASS — bg-red-500/10 + border-l-2 |
| 6 | Account-level drill-down red highlight (total_aua < 40k) | N/A — pre-existing, done in 6615b6b |
| 7 | Advisor book summary shows "Small Accts (<$40k)" stat or hidden | PASS — guarded with != null |
| 8 | Sort on "Small Accts" column works | PASS — click header toggles sortBy state |
| 9 | /frontend-dev clients_panel PASS | PASS — 1 iteration, 0 console errors |
| 10 | MCP COMPLETE to COO | DONE (see below) |

### B9b-DE2 (role decomp)
| # | Criterion | Status |
|---|-----------|--------|
| 1 | bun run build exits 0 | PASS |
| 2 | comp-transform schema-check AdvisorBookView clean | PASS |
| 3 | Book view shows role breakdown section | PASS — renders when DS ships, hidden otherwise |
| 4 | Roles with small_account_count > 0 have visual indicator | PASS — red card bg + red text |
| 5 | Section not rendered when data absent | PASS — IIFE returns null |
| 6 | /frontend-dev role_breakdown_small_accts PASS | PASS — 1 iteration, 0 console errors |
| 7 | MCP COMPLETE to COO | DONE (see below) |

## Next Steps

- `[DS]` B9b DS TO still pending — once `AdvisorClient.small_account_count` and `PlatinumAdvisorSummary.book.small_account_count` are emitted in gold artifact, FE columns/stats will auto-activate (no portal change needed)
- `[DT]` Await Wave A PROD-push scope ruling (Option A/B from COO) — this B9b commit is on DEV, DT decides whether to bundle with Wave A or push separately
