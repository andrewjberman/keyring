# Session Log -- ADVI_49PUSH.018 Auth Architecture Document
**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-04-09
**Project:** ADVI_49PUSH
**Status:** Complete -- committed 928c4565, pushed to CLOUD.

---

## Summary

Wrote the permanent auth architecture document for Advisor Intelligence post-platinum. Verified all claims against actual source code (not ANONYM PRD assumptions).

Sources read and verified:
- `infra/aws/lambda-edge/auth-validator-edge/index.mjs`
- `infra/aws/users/lambda/portal-authorizer/index.mjs`
- `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py`
- `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/pseudonymizer.py`
- `portal/src/contexts/AuthContext.tsx`
- `portal/src/hooks/useAuth.ts`
- `portal/src/contexts/AuthContext.context.ts`
- `comp-routes auth-map` + `comp-routes behaviors`

---

## Key Findings

### Auth paths
Two distinct paths for ADVI:
- S3-direct (edge JWT only): `artifacts/*`, `entities/*`, `*.json` depth-1
- API GW (edge JWT + portal-authorizer + Lambda): `platinum/*` (catch-all), `partners/*`

All platinum currently goes through API GW + opal-partners-data Lambda.

### RBAC tiers (from portal-authorizer computeAllowedFirms)
- Dev superadmin → ALL
- internal → ALL
- partner admin → own firm + descendants (recursive DynamoDB scan)
- partner user → own firm only

### Pseudonymization
- Trigger: `user_role == "user"` → HMAC-SHA256 8-char hex with prefix
- Per-firm key at `opal/pseudonym/{firmId}` in Secrets Manager (lazy provisioned)
- Book-scoping: advisor-role users see own clients in cleartext
- Fields hashed: `relationship_name`, `client_name`, `label`, `book_name`, `account_id`, `relationship_id`, `client_key`, `key`, `city`, `state`

### Token lifecycle
- Access token in localStorage; refresh token in HttpOnly cookie
- 15s proactive refresh interval; 8-min stale-on-focus; 2-min idle warning

### Auth gaps identified (non-blocking)
1. allowedTabs claim exists but unused
2. Lazy HMAC key provisioning on first firm request
3. `label` field ambiguity in pseudonymizer (safe currently, footgun potential)
4. Non-PII platinum files go through full API GW + Lambda roundtrip (Phase 5 optimization opportunity)

---

## Files Modified

| File | Change |
|------|--------|
| `docs/architecture/ADVI_49PUSH_AUTH_ARCHITECTURE.md` | Wrote complete auth architecture doc (replaced ~B stub) |

---

## Commit

| Step | Result |
|------|--------|
| Commit SHA | `928c4565` |
| Push | origin/CLOUD up to date |

---

## Next Steps

[DT 0.4.0_DT] Auth gap #1 (allowedTabs enforcement) forwarded by COO for future TO.
