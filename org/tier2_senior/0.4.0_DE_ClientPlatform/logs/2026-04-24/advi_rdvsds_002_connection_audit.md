# Session Log — ADVI_RDVSDS TO 002 — DE Connection Audit
**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-04-24
**TO:** ADVI_RDVSDS TO 002 (CTO GO received 20260424 inbox)
**Project:** ADVI_RDVSDS — Inflection portal shows no data

## Audit Results

| Check | Status | File:Line | Evidence |
|-------|--------|-----------|----------|
| 1. FIRM_BUCKET_MAP auth-validator-edge | PASS | `infra/aws/lambda-edge/auth-validator-edge/index.mjs:104` | `'inflection': 'inf'` present in FIRM_BUCKET_MAP |
| 1b. FIRM_BUCKET_MAP shared-advisor-router | PASS | `infra/aws/lambda-edge/shared-advisor-router/index.mjs:178` | `'inflection': 'inf'` present |
| 2. firmId propagation — inflection/index.tsx | PASS | `portal/src/pages/AdvisorIntelligence/_partners/inflection/index.tsx:132` | `firmOverride = internal ? FIRM_ID : undefined` where `FIRM_ID = 'inflection'` (constants.ts:1). External Inflection users: `firmOverride=undefined`, JWT X-Firm-Id routes to opal-data-inf via auth-validator-edge. All shared components (PartnerAnalytics, DistributionTab, AdvisorsTab, BooksTab) receive firmOverride correctly. |
| 3. 49financial hardcodes — advisor-intelligence.ts | PASS WITH NOTE | `portal/src/api/endpoints/advisor-intelligence.ts:71` | Only one `'49financial'` string: `const LAMBDA_FIRM_ID: Record<string, string> = { bd: '49financial' }`. This is a correct BD→DDB key mapping (not a default fallback). For Inflection, `LAMBDA_FIRM_ID['inflection'] ?? 'inflection'` = `'inflection'`. PRD's "10 hardcoded defaults" does not match current code — no silent 49F fallbacks found. |
| 4. FIRM_ACCOUNT_NAME — AdvisorsTab.tsx:76 | **FAIL** | `portal/src/pages/AdvisorIntelligence/_shared/tabs/AdvisorsTab.tsx:76` | `const FIRM_ACCOUNT_NAME = '49F House'` hardcoded at module level. `PINNED_BOTTOM_NAMES = new Set([FIRM_ACCOUNT_NAME, 'Unassigned'])` uses it. For Inflection, the leaderboard's firm-aggregate entry has `advisor_id: 'firm'` and `name: 'Inflection Wealth Management'` — no match to `'49F House'`. Firm aggregate will NOT be pinned to bottom; it will sort into the main leaderboard as a regular row. |
| 5. DynamoDB FIRM#inflection row | PASS | `opal-users-v2 PK=FIRM#inflection SK=META` | Row exists: `s3Bucket=opal-data-inf`, `firmId=inflection`, `status=active`, `createdBy=0.7.0_AE_CloudOps` (2026-04-21). Lambda-routed endpoints will resolve Inflection → opal-data-inf correctly. |

## Impact Assessment

### Checks that could cause blank views
- Check 1 (FIRM_BUCKET_MAP): PASS — S3 routing is correct; requests with `?firm=inflection` route to opal-data-inf
- Check 5 (DynamoDB): PASS — Lambda-routed endpoints can resolve Inflection bucket
- **Neither wiring check is a direct cause of blank views**

### Connection architecture for external Inflection users
```
Portal static S3 calls (no firmOverride):
  /api/scoped/.../timeseries_overview.json (no ?firm=)
  → auth-validator-edge reads X-Firm-Id from JWT
  → rewrites request to opal-data-inf/platinum/firm/...
  → 200 IF artifact exists in opal-data-inf bucket

Portal Lambda-routed calls (firmId = 'inflection'):
  /api/scoped/partners/books/...?firmId=inflection
  → opal-partners-data Lambda
  → DynamoDB FIRM#inflection META → s3Bucket=opal-data-inf CONFIRMED
  → 200 IF artifact exists
```

**Implication:** If S3 artifacts exist in opal-data-inf with correct values, portal SHOULD show data. The connection layer is verified. **Blank views = DS artifact issue (missing or zero-valued artifacts in opal-data-inf).**

### FIRM_ACCOUNT_NAME bug (display-layer, not blank-cause)
The `'49F House'` hardcode will cause Inflection's firm-aggregate leaderboard row to not be pinned to the bottom. It will appear as a regular row sorted by NNA. This is a data-display bug, but does NOT cause blank views.

## Fix List

### Fix 1 (DE) — FIRM_ACCOUNT_NAME parameterization
**File:** `portal/src/pages/AdvisorIntelligence/_shared/tabs/AdvisorsTab.tsx:76`
**Change:**
- Add `firmAccountName?: string` to `AdvisorsTabProps`
- Replace `const FIRM_ACCOUNT_NAME = '49F House'` with `const effectiveFirmAccountName = firmAccountName ?? '49F House'`
- Update `PINNED_BOTTOM_NAMES = new Set([effectiveFirmAccountName, 'Unassigned'])`
- Update all internal uses of `FIRM_ACCOUNT_NAME` to `effectiveFirmAccountName`

**Callers to update:**
- `portal/src/pages/AdvisorIntelligence/_partners/49financial/index.tsx` — no change needed (default fallback = '49F House')
- `portal/src/pages/AdvisorIntelligence/_partners/inflection/index.tsx:219` — add `firmAccountName={FIRM_DISPLAY_NAME}` to AdvisorsTab prop

**Effort:** ~20 min. Low risk (prop with safe default).

## Compiler Tools

| Phase | Tool | Result |
|-------|------|--------|
| Before write | `comp-blast AdvisorIntelligence` (check 4 blast radius) | Did not run — audit-only TO, no code changes this session. Mandated before Fix 1 TO authoring. |
| Investigation | grep auth-validator-edge, shared-advisor-router | Both have inflection:inf entry — PASS |
| Investigation | grep advisor-intelligence.ts for '49financial' | 1 result, correct mapping — PASS |
| Investigation | aws dynamodb get-item FIRM#inflection | `s3Bucket=opal-data-inf` — PASS |

NOTE: This is a read-only diagnostic TO. No code changes made this session. Compiler gate runs will be part of the Fix 1 TO.

## Next Steps

- [CTO] MCP with audit findings — blast radius / root cause steer
- [DE] Await CTO Fix phase dispatch — ready to author Fix 1 (FIRM_ACCOUNT_NAME) TO immediately
- [DE] Hypothesis to CTO: blank views are likely DS artifact gap in opal-data-inf (not a wiring issue). Connection layer verified clean.

## Status

TO 002 Connection Audit: **complete**
