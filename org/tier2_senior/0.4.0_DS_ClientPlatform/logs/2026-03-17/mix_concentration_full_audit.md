# Mix + Concentration Full Audit — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-17

## Objective

Full audit of every layer of the Mix and Concentration views: firm-level Assets Overview,
advisor-level, and client-level. Covers the $60M insurance appear/disappear pattern, the
5000% display bug, the firm-level architecture flaws, and the client-level stub state.

---

## Work Completed

### 1. 5000% Display Bug — Root Cause Confirmed

**Location:** `handle_books_composition` in opal-partners-data Lambda
**Affected surfaces:** `FirmCompositionSnapshot` (Assets Overview Mix panel), `ClientsTab.tsx`
  composition snapshot

**Root cause:** The Lambda sends `pct` as a 0-100 value:
```python
# Lambda (line 904 and 931):
'pct': round(float(mv) / total_mv * 100, 2)  # e.g., 62.5 means 62.5%
```

The frontend treats it as 0-1 and multiplies by 100 again:
```typescript
// PartnerAnalytics.tsx line 2297, ClientsTab.tsx line 824, 872:
{(item.pct * 100).toFixed(1)}%   // 62.5 * 100 = 6250.0%
```

A 62.5% equity allocation renders as "6250.0%". This is why every mix/concentration snapshot
on the portal shows values in the thousands of percent.

**The pie chart is also broken:** `concPieData` uses `value: it.pct` where pct=62.5. All
pie segments are ~60-80, so the pie chart renders roughly equal-sized regardless of actual
allocation (the proportions are correct but the absolute scale is meaninglessly large, which
Recharts normalizes to fill the circle — the chart looks visually OK but it's arithmetically
wrong if you ever add a denominator check).

**Fix is a one-liner:** Change Lambda `pct` to `round(float(mv) / total_mv, 6)` (remove `* 100`),
or change all frontend `(item.pct * 100)` to `(item.pct).toFixed(1)`. Lambda-side fix is
cleaner — the frontend convention everywhere else is 0-1 for pct values.

---

### 2. $60M Insurance Appearing/Disappearing — Diagnosis

**Symptom:** ~$60M labeled as structured_notes (insurance/annuities) appears in certain
quarters, disappears in others, then re-appears.

**Root cause hypothesis (AP gate + reporting cadence):**

The `06b` gold script applies the AP active gate:
```python
AP_GATE_DAYS = 45
last_seen = pos['account_id'].map(ap_last_seen).fillna(pd.Timestamp.min)
pos = pos[last_seen >= cutoff]  # cutoff = date - 45 days
```

This gate excludes any account not seen in `account_performance` within 45 days of the
snapshot date. This is CORRECT for standard BD accounts (prevents $371M stale-holdings
inflation). But insurance/annuity accounts present differently:

- **Insurance/annuity products** (SHIELD, BUFFER, variable annuities) are often held via
  insurance carriers, not standard custodians. Their position data in `positions_cube` may
  only update monthly or quarterly (statement-cycle reporting), not daily.
- If an insurance account's last `account_performance` entry was 47 days ago (just outside
  the 45-day gate), ALL its holdings are excluded from that day's snapshot.
- The next day, if a new account_performance entry arrives (end of month), the account
  reappears — and so does the $60M.

This creates the pattern Andrew observed: present for a few weeks, absent for 1-6 weeks,
present again.

**Secondary hypothesis (classification volatility):**

The `_RE_STRUCTURED` regex matches:
```python
r'SHIELD|ANNUIT|BUFFER|MANAGED FLOOR|FLOOR ETF|YR -|YEAR -|CAP 20%|CAP 15%|CAP 10%'
```

If the asset_name field for these products is inconsistent across different positions_cube
dates (e.g., "ALLIANZ STRUCTURED ALPHA" vs "ALLIANZ STRUCT. ALPHA" — one matches SHIELD/none
of the patterns), the classification could flip between structured_notes and equity/other
quarter to quarter. This would cause the apparent appearance/disappearance of the structured
notes bucket even when the accounts are continuously present.

**To differentiate:** Need to check:
1. Do the $60M accounts appear/disappear in `account_performance` (AP gate issue)?
2. Does the asset_name string for these products change across dates (classification volatility)?
3. Is the market value $60M or near-zero when they reappear (pricing issue)?

Both can coexist. The AP gate is more likely the primary driver given the quarterly
cadence of insurance reporting.

**Proposed fix for AP gate sensitivity:**
- Do NOT simply increase AP_GATE_DAYS globally — that would re-introduce the $371M stale
  positions from closed accounts.
- Instead: identify insurance/annuity account_ids via a flag in accounts_dimension
  (e.g., `is_insurance_custodian` or `reporting_frequency = 'monthly'`) and apply a longer
  gate (90-180 days) only to those accounts.
- Or: skip the AP gate for accounts classified as insurance custodians entirely (their
  positions don't go stale the same way as BD accounts).

**This requires investigation before designing a fix.** Need to look at the specific
account_ids driving the $60M, check their `account_performance` last_seen dates, and
verify whether they're insurance/annuity products with the AP gate as root cause.

---

### 3. Firm-Level Mix — Architecture Summary (from prior investigation)

Three compounding problems documented in `assets_overview_mix_investigation.md`:
1. Dollar amounts stripped from gold output (06b stores pct only)
2. Firm-level '0' aggregate not explicitly built
3. Frontend period aggregation (firmMixData useMemo) is out-of-pattern

Andrew confirmed option B: absolute dollar stacked bars (bar height = total AUA, each
segment = dollar amount of that asset class). This requires dollar amounts in the gold output.

---

### 4. Client-Level Mix/Concentration — Current State

**`ClientDetailPage.tsx`** (the main client detail view):
```typescript
// TODO: Replace with actual API call
setTimeout(() => {
  setClientData(null)
  setIsLoading(false)
}, 300)
```
The client detail page has a hardcoded stub. It always shows null client data. The
`MixTimeseriesPanel` and `ConcentrationPanel` components exist and are wired up with the
API functions (`getMixTimeseries`, `getConcentrationTimeseries`), but `ClientDetailPage`
doesn't render them — it only renders `AISummaryPanel`, `PortfolioBalancePanel`, and
`TimeSeriesPanel` (which also appear to be stub/mock state given the TODO comment).

The Books tab's `ClientsTab.tsx` DOES render the composition snapshot (the `FirmCompositionSnapshot`
pattern) for individual clients/advisors, but through the `getBooksFirmComposition` endpoint
which computes from live `holdings_lots` snapshots — NOT from the `06b` per-relationship
timeseries. This is the surface showing the 5000% pct bug.

**Per-relationship timeseries panels** (`MixTimeseriesPanel`, `ConcentrationPanel`):
- These call the correct endpoint (`mix-timeseries`, `concentration-timeseries`)
- But they fall back to MOCK_DATA when no real data arrives (line 95: `const chartData = isPlaceholder ? MOCK_DATA : data`)
- They are not wired into `ClientDetailPage` — they're orphaned components

**What's actually live for client-level:**
- `BooksClientDetailResponse` from `bd-portal-advisor-publisher` (AISummary, PortfolioBalance, TimeSeries)
- `BooksCompositionResponse` from `handle_books_composition` (live holdings_lots snapshot)
- Mix pct bug present on the composition snapshot

**What's NOT live:**
- Per-relationship daily mix timeseries (MixTimeseriesPanel)
- Per-relationship daily concentration timeseries (ConcentrationPanel)
- These require 06b to have run and written per-relationship JSONs, PLUS wiring into ClientDetailPage

---

### 5. Advisor-Level Mix — Not Built Yet

No advisor-level mix endpoint exists. No task order has been issued for it. The existing
advisor book endpoint (`/api/shared/advisor-intelligence/advisors/{id}/book`) includes
`portfolio_composition: AdvisorPortfolioComposition` which has:
```typescript
interface AssetAllocationItem {
  category: string
  label: string
  pct: number  // also likely 0-1 convention, unverified
}
```
This is a snapshot, not a timeseries, and comes from the `bd-portal-advisor-publisher`
script — not from 06b. The pct scale convention for this endpoint is unverified.

**To add advisor-level mix timeseries:**
- Option A: Use 06b output per relationship, aggregate per-advisor server-side
  (requires knowing which relationship_ids belong to each advisor — the rel_architect_lookup)
- Option B: Add an advisor aggregation step to 06b (writes `gold/advisors/{advisor_id}/mix.json`)
  analogous to how advisor book.json is written
- Option B is cleaner — same pattern as advisor/book.json

---

## Bugs and Issues Summary

| # | Issue | Location | Severity | Fix Complexity |
|---|-------|----------|----------|----------------|
| B1 | pct scale: Lambda sends 0-100, frontend expects 0-1 | Lambda `handle_books_composition`, `PartnerAnalytics.tsx`, `ClientsTab.tsx` | CRITICAL | Trivial (one-liner in Lambda) |
| B2 | Insurance $60M appears/disappears | `06b` AP gate, positions_cube reporting cadence | High | Medium (requires investigation + targeted gate override) |
| B3 | Firm-level mix shows no dollars, uses wrong methodology | `06b` gold output, `firmMixData` useMemo | High | Large (new gold output, new endpoint, new chart) |
| B4 | Firm-level '0' aggregate not explicitly built | `06b` | High | Medium (add firm aggregation step) |
| B5 | Frontend period aggregation for mix | `PartnerAnalytics.tsx` `firmMixData` useMemo | Medium | Small (once gold output is fixed) |
| B6 | `ClientDetailPage` shows stub data, MixTimeseriesPanel orphaned | `ClientDetailPage.tsx` | Medium | Medium (wiring) |
| B7 | Advisor-level mix does not exist | gold layer, Lambda | Medium | Large (new workstream) |
| B8 | Pie chart uses wrong pct as value (works visually but wrong arithmetically) | `PartnerAnalytics.tsx`, `ClientsTab.tsx` | Low | Trivial (same fix as B1) |

---

## Project Scope Assessment

This is too large for a single task order to a single agent. The work spans:
- Data science (classification audit, AP gate investigation, gold layer redesign)
- Lambda/infrastructure (new endpoints, pct fix)
- Dashboard engineering (firm-level chart redesign, client-level wiring)
- React design (absolute dollar bar chart, client detail page)
- DevOps (06b deploy to EC2, Lambda deploy)

**Recommended decomposition into a registered project (ADVI_MIXV2 or similar):**

| Workstream | Description | Primary Agent |
|------------|-------------|---------------|
| WS1 | B1 pct bug: Lambda fix (5 min) | DS or DE |
| WS2 | B2 Insurance AP gate: investigation + targeted fix | DS |
| WS3 | B3/B4/B5 Firm-level mix: 06b aggregation + period views + Lambda endpoint | DS + DT/AE |
| WS4 | B3 frontend: absolute dollar bars, replace useMemo | DE + RD |
| WS5 | B6 Client-level wiring: ClientDetailPage + MixTimeseriesPanel | DE + RD |
| WS6 | B7 Advisor-level mix: 06b advisor aggregation + endpoint | DS + DT/AE |

WS1 is an immediate hotfix — should be committed today, independent of PRD.
WS2 blocks WS3 (you don't want to ship the pre-computed firm mix if $60M of it is volatile).
WS3 blocks WS4.
WS5 and WS6 are independent and can run in parallel with WS2-4.

---

## Current State

**Status:** COMPLETE (audit only)
**Active branch:** CLOUD

Full audit complete. Five distinct problem areas identified with root causes and
fix complexity mapped. Recommend PRD for the full project, with B1 (pct bug) issued
as an immediate hotfix task order before the PRD is drafted.

---

## Next Steps

1. **[Andrew] Decide** whether to elevate to a registered project with PRD (ADVI_MIXV2) or
   issue as ad-hoc task orders
2. **[0.4.0_DS_ClientPlatform] Issue B1 hotfix** — Lambda pct fix is trivial and should not
   wait for the PRD
3. **[0.4.0_DS_ClientPlatform] Investigate B2** — pull the $60M account_ids, check
   account_performance last_seen dates, check asset_name consistency for structured_notes hits
4. **[Andrew] Confirm PRD scope** — does advisor-level mix (WS6) belong in this project or
   is it a separate initiative?

**Do NOT:**
- Ship the firm-level mix redesign (WS3) before investigating B2 — a volatile $60M bucket
  will be baked into the pre-computed views
- Increase AP_GATE_DAYS globally — that would re-introduce the $371M stale-positions problem
