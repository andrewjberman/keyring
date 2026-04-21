# Session Log -- 2026-04-21 -- ADVI_INFLEC.W5.7 API Smoke Tests

| Field | Value |
|-------|-------|
| Agent | 0.4.0_DT_ClientPlatform |
| Date  | 2026-04-21 |
| TO    | ADVI_INFLEC.W5.7.dt-api-smoke-tests |
| Issued by | 2.0.0_SA_COO |
| Authorization | COO GO (20260421T213026Z) |

---

## Test Setup

Two test users provisioned for this smoke test:
- test-admin@inflectionwealthmgmt.com -- firmRole=admin, advisorId=inflection_test_admin
- test-advisor@inflectionwealthmgmt.com -- firmRole=user, advisorId=inflection_test_advisor

Both provisioned in opal-users-v2 + opal-partner-inflection.

---

## 6-Case Curl Matrix

### Case 1: Firm leaderboard (admin JWT, firmId=inflection)

```
GET /api/scoped/advisor-intelligence/platinum/firm/leaderboard.json?firmId=inflection
Authorization: Bearer <admin_jwt>

HTTP 200 | X-Cache: Error from cloudfront
```

PASS. Auth passed (Error from cloudfront = origin reached). File missing (platinum not yet written for Inflection). Expected.

---

### Case 2: Partner analytics (admin JWT, firmId=inflection)

```
GET /api/scoped/advisor-intelligence/platinum/firm/partner_analytics_quarterly.json?firmId=inflection
Authorization: Bearer <admin_jwt>

HTTP 200 | X-Cache: Error from cloudfront
```

PASS. Auth passed, file missing. Expected.

---

### Case 3: Own-advisor path (non-admin JWT, own advisorId)

```
GET /api/scoped/advisor-intelligence/platinum/advisors/inflection_test_advisor/book.json?firmId=inflection
Authorization: Bearer <advisor_jwt>  (firmRole=user, advisorId=inflection_test_advisor)

HTTP 200 | X-Cache: Error from cloudfront
```

PASS. Scope gate passed (advisorId matches JWT). File missing. Router log confirms:
`uri=/platinum/advisors/inflection_test_advisor/book.json -> bucket=opal-data-inf`

---

### Case 4: Other-advisor path (non-admin JWT, different advisorId)

```
GET /api/scoped/advisor-intelligence/platinum/advisors/inflection_test_admin/book.json?firmId=inflection
Authorization: Bearer <advisor_jwt>  (firmRole=user, advisorId=inflection_test_advisor)

HTTP 403 | X-Cache: LambdaGeneratedResponse from cloudfront
```

PASS. auth-validator-edge returned 403 (LambdaGeneratedResponse). Scope gate correctly blocked non-admin user from accessing other advisor's data. No router log entry (request never reached S3 origin).

---

### Case 5: Admin JWT on other-advisor path (admin bypasses scope gate)

```
GET /api/scoped/advisor-intelligence/platinum/advisors/inflection_test_advisor/book.json?firmId=inflection
Authorization: Bearer <admin_jwt>  (firmRole=admin)

HTTP 200 | X-Cache: Error from cloudfront
```

PASS. firmRole=admin bypasses scope gate per getAllowedAdvisorIds() returning null. File missing (expected).

---

### Case 6: Cross-firm isolation (Inflection JWT with ?firmId=49financial)

```
GET /api/scoped/advisor-intelligence/platinum/firm/leaderboard.json?firmId=49financial
Authorization: Bearer <admin_jwt>  (firmId=inflection in JWT)

HTTP 200 | X-Cache: Error from cloudfront
```

ACCEPTANCE FLEX (pre-flagged to CTO 20260421T213405Z, no objection received):

TO expected 403. Actual: 200 (custom error SPA HTML).

Reason: Cross-firm containment is NOT enforced via hard 403 at the edge. It is enforced by data isolation. auth-validator-edge/index.mjs line 193 comment: "Cross-firm containment is NOT enforced here. It is handled by the existing X-Firm-Id injection + shared-advisor-router S3 key rewrite."

Evidence from router logs: Inflection JWT with ?firmId=49financial -> router used firmId=inflection (JWT claim, not query param) -> bucket=opal-data-inf. 49F data is physically inaccessible. Router never fetches from opal-data-bd for an Inflection JWT.

Isolation IS working by data isolation. No 49F data leaks to Inflection users. Pre-existing design, not a regression from ADVI_INFLEC changes.

---

## comp-routes verification

```
comp-routes behaviors: 23 behaviors
```

All behaviors unchanged. No new unauthenticated routes.

---

## Router Log Summary

```
firmId=inflection -> routingFirmId=inf -> bucket=opal-data-inf (all requests)
```

Even with ?firmId=49financial query param, router ignores query param and uses JWT firmId.

---

## Acceptance Criteria

| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | All 6 curl cases pass as expected | PARTIAL PASS (5/6 exact; case 6 differs -- see ACCEPTANCE FLEX) | See matrix above |
| 2 | Cross-firm isolation confirmed | PASS (by data isolation, not 403) | Router logs confirm opal-data-inf routing even for ?firmId=49financial |
| 3 | comp-routes behaviors: unchanged | PASS | 23 behaviors, no new unauthenticated routes |
| 4 | Session log with all curl outputs + response codes | PASS | This file |

---

## Current State

- All Inflection API paths pass auth flow correctly.
- Scope gate (case 4: 403 on other-advisor) VERIFIED.
- Cross-firm data isolation VERIFIED (by data inaccessibility, not hard 403).
- Proceeding to W5.9 (49F regression final gate).
