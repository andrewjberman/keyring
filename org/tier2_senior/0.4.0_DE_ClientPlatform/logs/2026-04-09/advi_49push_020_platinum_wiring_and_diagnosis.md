# ADVI_49PUSH.020 -- Platinum Wiring, Deployment, and End-to-End Diagnosis
**Date:** 2026-04-09
**Start Time:** 8:22 PM ET (2026-04-08)
**End Time:** 9:45 AM ET (2026-04-09)
**Task Orders:** ADVI_49PUSH.020 (e2e validation), ADVI_49PUSH.022 (auth refresh frontend trace)
**Status:** Frontend work complete; unblocked on DS fixes + AE chain re-run

**Portal DEV commits (8 commits ahead of origin, not pushed):**
- `7954f16` `.012` Books tab platinum wiring (ClientsTab, MixTimeseriesPanel, ConcentrationPanel, ClientDetailPage)
- `c5e61d7` `.013` PartnerAnalytics + Distribution platinum wiring
- `613916b` `.014` Advisors tab platinum wiring
- `bdcba19` Platinum types + API endpoints (advisor-intelligence.ts, types.ts, endpoint-mapping.ts)
- `d8b6c3b` TS build errors (DistributionTab + PartnerAnalytics)
- `3c6f196` Handle `split:true` in `getPlatinumFirmDashboard`
- `6687b8b` Advisor list window fallback + `FeeEfficiencyAdvisor` type alignment
- `82bab42` Fee efficiency scatter dots navigate to advisor page

**Deployed to opalinvest.dev:** s3://opalinvest-portal + CF invalidations (last: `IEZ3NBAGDF0JDPE2IG132YD5CK`)

---

## Work Summary

### Phase 1 -- Portal submodule commits (.012/.013/.014 + shared)

COO sent uncommitted portal changes on DEV for the 49PUSH platinum wiring wave. Grouped into the 4 commits COO specified. Verified the two platinum Lambda route URLs before committing:
- L2: `/api/scoped/partners/books/advisor/${id}/platinum-summary?firmId=${firmId}`
- L3: `/api/scoped/partners/books/relationship/${rel_id}/platinum-summary?firmId=${firmId}`

Both matched DT's M1 migration; committed on DEV without push per instructions.

### Phase 2 -- .020 execution (portal deploy + auth test + browser QA)

COO GO on .020 after DT confirmed Lambda deploy (`partners-api-v1.15.3`, `portal-auth-v1.11.4`).

**Build errors (5 TS errors in `d8b6c3b`):**

| File | Error | Fix |
|------|-------|-----|
| DistributionTab.tsx:53 | `PlatinumPlatinumCumulativeChartResponse` typo in import | Single-Platinum prefix |
| DistributionTab.tsx:833 | `data?.nna` -- field doesn't exist on `PlatinumCumulativeChartResponse` | `data?.nna_geo ?? data?.nna_adv` fallback |
| DistributionTab.tsx:1118 | `viewMode` index narrowing -- `'nna'` not indexable | Cast to `'geo' \| 'adv'` (already null-gated at line 1116) |
| DistributionTab.tsx:1311 | `data?.metadata` -- not on type | `(data as any)?.metadata` |
| DistributionTab.tsx multiple | Implicit `any` params in arrow callbacks | Type-annotated filter/reduce/forEach/map callbacks |
| PartnerAnalytics.tsx:1871 | `latest.endDate` -- not on derived `aggregatedGroData` type | Use `latest.period` / `latest.label` |

Build clean after fixes. Committed `d8b6c3b`, deployed via `aws s3 sync s3://opalinvest-portal/` with `--delete` then CF invalidation `I90MXS355C9P6SQT7SL0C45PI3`.

### Phase 3 -- .022 auth refresh investigation (parallel with DT .021)

COO reported `POST /auth/refresh -> 401`. Ran `git diff HEAD~5` on auth-related files:
- `portal/src/contexts/AuthContext.tsx` -- **zero changes**
- `portal/src/hooks/useAuth.ts` -- **zero changes**
- `portal/src/api/endpoints/auth.ts` -- **zero changes**

`endpoint-mapping.ts` diff only removed stale S3-direct platinum mappings. `API_BASE` unchanged (`VITE_AUTH_API_URL` fallback). Reported frontend clean; routed back to DT's `.021` as a backend issue.

### Phase 4 -- URGENT "ADVI shows no data" investigation

COO asked to investigate non-auth, non-S3-path vectors. Ran:
- `comp-cache collisions` -- no collisions
- `comp-transform schema-check AdvisorsTab / ClientsTab / DistributionTab / PartnerAnalytics` -- all rendered fields match their types

Verified the deployed build has the correct URLs (`partners/books/advisor/{id}/platinum-summary` in `dist/assets/index-*.js`, no stale `platinum/advisors/` or `platinum/clients/` S3-direct paths).

Then `curl -s -w "%{http_code}"` on a platinum firm endpoint with no JWT → `401 {"error":"Missing or invalid Authorization header"}` -- healthy response from `auth-validator-edge`, meaning the edge Lambda was propagated.

Andrew provided a JWT for `test_platinum_auth.py --tier internal --role admin --firm bd`. Initial output looked good: **22/24 passed**. Then I curled the leaderboard endpoint directly with the JWT and saw the body was `<!doctype html>` not JSON -- all "200 OK (1068 bytes)" responses were the SPA index.html shell. The auth smoke test only checks HTTP status, not Content-Type.

Sent a CORRECTION to COO: all 22 passes were false positives; CloudFront custom-error `403 -> 200+index.html` was masking origin errors. T6.1/T6.2 correctly caught the HTML via JSON parse failures.

### Phase 5 -- Split dashboard discovery

Andrew clarified the data IS there but `platinum/firm/dashboard.json` is a 224-byte stub:
```json
{"generated_at":"...","data_as_of":"...","firm_id":"49financial","headline":{...},"split":true}
```

D_04 emits the stub when the full payload exceeds a size threshold; the real payload lives in separate files. Asked whether to fix in frontend or in D_04 -- Andrew said frontend.

**Fix in `3c6f196` -- `getPlatinumFirmDashboard`:**
1. Detect `stub.split === true`
2. In parallel: `getFirmLeaderboard(firm)` (S3), `apiRequest<FeeEfficiencyResponse>` for `platinum/firm/fee_efficiency.json` (S3), `getClientsTab(firm)` (Lambda, pseudonymized)
3. Assemble into full `PlatinumFirmDashboard` and return

All three split sources independently `.catch(() => null)` so a single failure degrades gracefully instead of blocking the whole Books tab.

### Phase 6 -- Andrew flags two Books tab bugs

1. **Fee efficiency scatter -- all dots at 50th percentile** (yellow/median)
2. **No advisor list on Books tab**

Traced both:

**Fee efficiency** -- `FeeEfficiencyPanel.tsx:94` accessor defaulted `pctile` to 50 when `efficiency_pctile` was missing. Pulled deployed `platinum/firm/fee_efficiency.json` from S3; advisor objects have `efficiency_ratio`, `regression_residual_ratio`, etc. but **no `efficiency_pctile` field**. First attempted a computed-percentile fallback (rank `efficiency_ratio` ascending → 1..100), but Andrew said **DS owns this** and the script should provide the field. Reverted to just aligning the `FeeEfficiencyAdvisor` type (make fields optional, add platinum field names).

**Advisor list** -- `ClientsTab.tsx:306` hardcoded `lb.windows['1Y'].entries`. The platinum leaderboard only has `QTD` and `YTD` windows (verified from S3). No `1Y` → `advisorSummary` stayed empty → list showed "No advisor data available".

Fix in `6687b8b`:
- Initial load: fall back to first `available_windows` entry when `1Y` is absent
- `periodAdvisors` memo: same fallback chain

### Phase 7 -- Scatter click navigation

Andrew: clicking a scatter dot should take you to that advisor's page. The code at `FeeEfficiencyPanel.tsx:358` already had `onClick` on `<Scatter>`, but recharts' `onClick` doesn't reliably fire when a custom `shape` function is provided -- the handler has to be attached to the rendered SVG element directly.

Fix in `82bab42`:
- Moved `onClick` from the `<Scatter>` prop onto the shape's `<g>` wrapper
- Added a transparent `r = max(dotR + 4, 10)` hit target circle behind each visible dot so small dots are still clickable
- Cursor pointer only when `onAdvisorClick` is defined

### Phase 8 -- "Clicking advisor refreshes the Books tab" (root cause dig)

Andrew reported that clicking a scatter dot OR an advisor name in the list "very consistently" refreshes the Books tab instead of drilling into the advisor. Traced:

**Frontend silent fallback** -- `ClientsTab.tsx:372-374`:
```ts
.catch((err) => {
  console.error('[BooksTab] L2 fetch failed:', err)
  setAdvisorBookData(null)
  setIsLoadingAdvisor(false)
})
```
On error, leaves `selectedAdvisorId` **set** but nulls `advisorBookData`. Render logic:
- `selectedAdvisorId && advisorBookData` → FALSE
- `selectedAdvisorId && isLoadingAdvisor` → FALSE
- Falls through to N1 render -- looks identical to a page refresh

**Data gap** -- compared leaderboard to S3 files:
- `platinum/firm/leaderboard.json` -- **155 unique advisor names** across QTD+YTD windows
- `platinum/advisors/{id}/summary.json` -- **57 files** total
- **98 advisors in the leaderboard have no platinum file**

Sample missing: `aj_lenartowicz`, `alex_bright`, `alex_coggins`, `andrew_stafford`, `ava_smagacz`, `banks_wilson`, `brooke_smith`, `bryan_guzman`, `cameron_mcilhenny`, ... (~104 missing once dedupe is applied).

Andrew noted the run completed 20 min prior (S3 `LastModified: 2026-04-09T13:03:14Z` confirmed), so this was a D_02 logic bug not staleness. Andrew theorized: "may be it's only generating for advisors listed as architect vs any role (architect/consultant/implementor/local_ops)." **Confirmed:**

- **C_08** (`ROLES = ['architect', 'implementor', 'consultant', 'local_ops', 'additional_advisor']`) melts all 5 roles into a unified `advisor` column → 155 unique people in the leaderboard
- **D_02** loads only `['account_id', 'architect', 'implementor']` from `account_team` (line 228) and `build_advisor_books` iterates `latest_snap['architect'].dropna().unique()` (line 689) -- only architects
- D_02 does have a `build_implementor_leaderboard` (firm-level aggregate) but never writes per-implementor `book.json` files, nor anything for consultant / local_ops / additional_advisor
- **D_04** iterates whatever `book.json` files D_02 writes -- so it can never produce more summaries than D_02 writes

Reported the diagnosis to DS. DS shipped the D_02 multi-role fix within minutes:
- `account_team` load extended to all 5 role columns
- Role override extended from 2 → 5 roles
- `build_advisor_books` now unions advisor names across all 5 roles; filters `acct` where a person appears in ANY role; determines `primary_role` from whichever role has the most accounts
- `build_advisor_timeseries` had the same bug; fixed via melt-to-long-form + dedupe
- `book_type` now set from `primary_role` instead of hardcoded `'architect'`
- **AUA weighting caveat** -- unweighted, consistent with existing architect behavior (sum of all 5 role books will exceed firm AUA due to multi-counting; proper split-weighting would need SCD assignments join)

---

## Findings Reported (Not Frontend-Owned)

| Issue | Owner | Status |
|-------|-------|--------|
| Fee efficiency `efficiency_pctile` missing from `platinum/firm/fee_efficiency.json` | DS (C_08) -- initially flagged as stale deployed binary, then as D_02+D_03+D_04 sub-chain not including C_08 in prior re-run | Queued for AE chain re-run |
| `platinum/firm/fee_efficiency.json` uses gold field names (`managed_aua`, `implied_revenue`, `fee_yield_bps`) instead of portal contract (`aua`, `commission`, `fee_bps_weighted`) | DS (C_08) | Same chain re-run will fix; I aligned `FeeEfficiencyAdvisor` type to accept both |
| D_02 `build_advisor_books` only emits books for `architect` role -- 98 advisors (consultants, local_ops, additional_advisor, implementors not-also-architect) have no platinum summary file → clicks silently fail | DS (D_02) | **Fixed by DS in the same session**, py_compile clean, awaiting AE chain re-run |
| CloudFront custom-error `403 → 200+index.html` cascade on Lambda-proxied routes (T6.1 clients-tab, T6.2 partner-analytics) | DT (`.021`) | DT's PII block fix in progress |
| `test_platinum_auth.py` only checks HTTP status, not Content-Type or JSON-parseability; produces 22 false-positive passes when origin returns HTML under 200 | Test-owner -- noted to COO, not fixed | Noted |

---

## Frontend Issues Remaining (Defer Pending Data)

- `ClientsTab.tsx` still falls through to N1 silently on L2 fetch failure. Andrew flagged this is the root cause of the "refreshes the Books tab" UX. **Not fixed yet** -- Andrew was satisfied with the D_02 diagnosis as the priority. Worth an explicit error panel once the data gap is closed, to cover future edge cases. Offered to do it; Andrew didn't ask for it.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx | Staged for `.012` (Books tab wiring); advisor list window fallback in `6687b8b` | Yes -- DEV `7954f16`, `6687b8b` |
| portal/src/pages/AdvisorIntelligence/tabs/DistributionTab.tsx | `.013` platinum wiring + 5 TS build fixes | Yes -- DEV `c5e61d7`, `d8b6c3b` |
| portal/src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx | `.014` platinum wiring | Yes -- DEV `613916b` |
| portal/src/pages/AdvisorIntelligence/tabs/FeeEfficiencyPanel.tsx | Scatter onClick moved onto custom shape `<g>`; transparent hit target | Yes -- DEV `82bab42` |
| portal/src/pages/AdvisorIntelligence/components/PartnerAnalytics.tsx | `.013` wiring + `endDate -> period/label` TS fix | Yes -- DEV `c5e61d7`, `d8b6c3b` |
| portal/src/pages/AdvisorIntelligence/ClientDetail/panels/MixTimeseriesPanel.tsx | `.012` platinum wiring | Yes -- DEV `7954f16` |
| portal/src/pages/AdvisorIntelligence/ClientDetail/panels/ConcentrationPanel.tsx | `.012` platinum wiring | Yes -- DEV `7954f16` |
| portal/src/pages/AdvisorIntelligence/ClientDetail/ClientDetailPage.tsx | `.012` platinum wiring | Yes -- DEV `7954f16` |
| portal/src/pages/AdvisorIntelligence/AdvisorIntelligence.tsx | `.014` wiring | Yes -- DEV `613916b` |
| portal/src/pages/AdvisorIntelligence/types.ts | Platinum interfaces + `FeeEfficiencyAdvisor` field alignment | Yes -- DEV `bdcba19`, `6687b8b` |
| portal/src/api/endpoints/advisor-intelligence.ts | New platinum fetch functions; `split:true` handling | Yes -- DEV `bdcba19`, `3c6f196` |
| portal/src/api/endpoint-mapping.ts | Removed stale S3-direct platinum mappings | Yes -- DEV `bdcba19` |

---

## Task Order Status

| Task Order | Project | Status |
|---|---|---|
| ADVI_49PUSH.020 | ADVI_49PUSH | Portal deployed, auth test results false-positive (test script bug), real end-to-end blocked on DS `efficiency_pctile` + D_02 role-coverage chain re-run + DT `.021` PII cascade fix |
| ADVI_49PUSH.022 | ADVI_49PUSH | COMPLETE (frontend clean, backend 401 routed to DT) |

---

## Next Steps

1. **[AE 0.7.0]** Re-run gold chain `C_07 → C_08 → D_00 → D_02 → D_03 → D_04` to pick up DS's D_02 multi-role fix, C_08 current-version output (`efficiency_pctile`, portal-contract field names), and regenerate 155 `platinum/advisors/{id}/summary.json` files
2. **[DT 0.4.0_DT]** Complete `.021` PII block fix -- clients-tab + partner-analytics Lambda endpoints still return HTML masked as 200 via CF custom-error
3. **[DE 0.4.0 me]** After re-run, browser QA all 4 ADVI tabs and verify:
   - Books tab advisor list populates (QTD/YTD windows present)
   - Fee efficiency scatter renders with real percentile gradient (not all yellow)
   - Scatter dot clicks navigate to L2 advisor page for all 155 advisors
   - Split dashboard assembles cleanly (leaderboard + fee_efficiency + clients_tab)
4. **[DE 0.4.0 me]** Optional hardening -- replace silent `.catch(() => null)` fallback in `ClientsTab.tsx` L2 useEffect with an explicit "advisor data not available" panel + back button, so future data gaps surface as visible errors instead of looking like a page refresh
5. **[DT 0.4.0_DT]** Portal DEV push (8 commits ahead of origin on DEV, deliberately not pushed per COO instruction during the hotfix window)
