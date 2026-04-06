# ADVI_ANONYM P3 -- Auth Schema Cleanup & S3 Deprecation Sweep

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-01
**Status:** COMPLETE

---

## Session Summary

Two workstreams in one session:

1. **ADVI_ANONYM.007** (P3 tier refactor) -- code changes across 8 files
2. **Auth schema architecture discussion + cleanup** -- Andrew-directed simplification of opal-users-v2, task order for DT, and S3 deprecated file deletion

---

## Workstream 1: ADVI_ANONYM.007 Tier Refactor

**Commit:** a067e0fb on CLOUD (not pushed)

Removed `internal` tier concept from the entire auth/pseudonymization stack:

- opal_auth: `is_internal` checks `firm_id == 'opal-capital'` instead of `tier == 'internal'`
- pseudonymizer: `user_tier` parameter removed entirely, role-only PII gate, added `advisor_id` book-scoping via `_should_hash`
- lambda_function: extracts `advisorId` from auth context, internal fallback uses `user_firm_id == 'opal-capital'`, all 9 `_pseudonymize_s3_response` call sites updated
- auth-handler (db.ts, jwt.ts, types.ts): tier fallbacks `'internal'` -> `'advisor'`, `advisorId` added to JWT payload
- portal-authorizer: `advisorId` added to context block
- ARCHITECTURE.md + OPAL_USERS_V2_SCHEMA.md updated

---

## Workstream 2: Auth Architecture Discussion

Andrew clarified the target auth model:

### Decisions Made

1. **Only two roles matter: admin and user.**
   - admin = full access to all data in their firm (opal-capital admin = everything)
   - user = access scoped to them (e.g., 49F architect sees own-book clients only)

2. **tier is deprecated.** Internal access determined by `firmId == 'opal-capital'`, not tier. The subadvisor/branch hierarchy is unused.

3. **opal-users-v2 is identity + auth only.** Fields that belong there:
   - PK, SK, userId, email, passwordHash, name, role, firmId, userType, status
   - mustChangePassword, createdAt, createdBy, updatedAt, lastLogin, passwordChangedAt
   - reset_token, reset_token_expires

4. **Removed from opal-users-v2 (partner-specific scoping):**
   - tier, regionId, officeId, allowedPages, allowedTabs
   - These belong in the partner-specific table (opal-partner-49financial)

5. **Two-table model confirmed:**
   - `opal-users-v2`: single roster, all users across all firms, auth credentials
   - `opal-partner-49financial`: advisor identity mapping + scoped permissions (advisorKey, advisorName, advisorRole, allowedPages, allowedTabs)

6. **Partner table lookup gate:** changed from `allowedPages.includes('advisor-intelligence')` to `firmId !== 'opal-capital'`

7. **status field:** exists but never checked at login. Needs one guard line wired in: `if (user.status !== 'active') throw new Error('Account disabled')`

### Task Order Issued

ADVI_ANONYM.011 drafted for DT at:
`org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_ANONYM.011.dt-user-schema-cleanup.md`

DT completed it same session (commit ec9ff6e2, tag portal-auth-v1.5.0). Note: login was broken 18:29-18:34 ET due to handler path mismatch (dist/index.handler vs index.mjs at zip root). COO hotfix applied handler=index.handler.

Req 6 (data migration of allowedPages/allowedTabs to partner table) deferred to AE.

---

## Workstream 3: S3 Deprecated File Cleanup

Andrew asked about stale files in the advisor intelligence gold layer. Cross-referenced every S3 key the Lambda reads against the stale file list.

### Deleted from opal-data-bd/gold/ (all deprecated, none consumed by any endpoint):

| File | Size | Last Modified |
|------|------|---------------|
| flows_chart.json | 207 KB | Feb 12 |
| aua_chart.json | 643 B | Mar 26 |
| client_concentration_timeseries.parquet | 317 MB | Mar 26 |
| client_mix_timeseries.parquet | 56 MB | Mar 26 |
| account_quality_tiers.parquet | 343 KB | Mar 31 |
| account_quality_tiers_2026-03-27.json | 1.8 KB | Mar 31 |
| trigger-pending.json | 127 B | Mar 31 |
| placeholder.json | 98 B | Feb 17 |

Confirmed clean in opal-data-portal-v2 (no matches).

---

## COO Messages Sent

1. ADVI_ANONYM P3 complete -- commit a067e0fb, findings, TypeScript notes
2. ADVI_ANONYM.011 task order drafted for DT -- schema cleanup scope
