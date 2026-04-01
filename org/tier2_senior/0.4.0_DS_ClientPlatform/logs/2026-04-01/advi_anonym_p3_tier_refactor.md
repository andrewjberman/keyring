# ADVI_ANONYM P3 -- Tier Refactor, Role-Only PII Gate, Book Scoping

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-01
**Task Order:** ADVI_ANONYM.007.ds-tier-refactor-book-scoping
**Status:** COMPLETE

---

## Summary

Removed `internal` tier as a concept from the auth/pseudonymization stack.
Internal access is now determined by `firmId == 'opal-capital'` instead of
`tier == 'internal'`. Pseudonymization is now role-only (no tier check).
Added advisor_id book-scoping so advisor-user sees cleartext for own-book clients.

## Files Modified (8 total)

### 1. opal_auth/__init__.py
- `is_internal` property: `tier == 'internal'` -> `firm_id == 'opal-capital'`
- Removed 'internal' from tier docstring
- Updated `require_internal` docstring

### 2. pseudonymizer.py
- Removed `user_tier` parameter from `needs_pseudonymization()` and `pseudonymize_response()`
- Added `advisor_id` parameter to `pseudonymize_response()`
- Implemented `_should_hash(user_role, advisor_id, field_architect)` for book-scoping
- Updated `_walk` and `_transform_field` to propagate `architect` field from parent objects
- Own-book clients (where architect == advisor_id) get cleartext for advisor/user

### 3. lambda_function.py
- Added `advisor_id = auth_context.get('advisorId', None)` extraction
- Added `user_firm_id = auth_context.get('firmId', '')` extraction
- Changed internal fallback: `user_tier == 'internal'` -> `user_firm_id == 'opal-capital'`
- Updated `_pseudonymize_s3_response` signature: removed `user_tier`, added `advisor_id`
- Updated all 9 call sites to pass `user_role, firm_id, advisor_id`
- Renamed path-param `advisor_id` to `path_advisor_id` to avoid shadowing auth context variable

### 4. auth-handler/db.ts
- Line 101: tier fallback `'internal'` -> `'advisor'`
- Line 144: tier fallback `'internal'` -> `'advisor'`

### 5. auth-handler/jwt.ts
- Line 66: tier fallback `'internal'` -> `'advisor'`
- Added `advisorId: partnerIdentity.advisorKey` to JWT payload (maps advisorKey as advisorId)

### 6. auth-handler/types.ts
- Line 22: Removed 'internal' from User tier comment
- Line 49: Removed 'internal' from AccessTokenPayload tier comment
- Added `advisorId?: string` to AccessTokenPayload

### 7. portal-authorizer/index.mjs
- Added `advisorId: decoded.advisorId || 'null'` to context block

### 8. Documentation
- portal/partners/OPAL_USERS_V2_SCHEMA.md: removed 'internal' tier, added advisorId field,
  updated permission matrix to use firmId=opal-capital, updated examples
- infra/aws/auth/ARCHITECTURE.md: removed 'internal' tier, updated permission resolution
  algorithm, updated code examples

## IAM Check
IAM already includes `secretsmanager:GetSecretValue` and `secretsmanager:CreateSecret`
for `opal/pseudonym/*` at partners-api/iam.tf:81-84. No blocker.

## TypeScript Notes
auth-handler changes are straightforward (fallback string replacements + one new field
in JWT payload). No complex TypeScript logic changed. advisorId maps from the existing
partnerIdentity.advisorKey which is already sourced from opal-partner-49financial DynamoDB.
Confident in correctness.

## Architecture Decision: advisor_id Shadowing
In lambda_function.py, the `/advisors/{id}/book` handler previously used `advisor_id`
as a local variable for the path parameter, which shadows the auth_context `advisor_id`.
Renamed to `path_advisor_id` to keep both distinct. Same for `/advisors/{id}/mix-views`.
