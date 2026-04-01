# ADVI_ANONYM P3 + ADHC_HISTRY P1/P2 Session -- 2.0.0_SA_COO

**Date:** 2026-04-01
**Session:** 9 (continued)

---

## ADVI_ANONYM -- P1 through P3 COMPLETE

### P1 (serving layer pseudonymization)
- DS: pseudonymizer.py + 9 PII call sites (`3fdb9a51`)
- AE: Secrets Manager keys + IAM (`partners-api-v1.10.0`)
- DT: Lambda deploy + auth-validator-edge v9 + P0 gate removed (`partners-api-v1.11.0`)
- advisor/user gets hashed names. opal-capital/admin gets cleartext.

### P2 (frontend indicators)
- DE: canSeeCleartext() in AuthContext (`11ee364`)
- RD: indicators on 4 surfaces (`2ebf55b`)
- DT: portal-v2.1.20

### P3 (tier refactor + book scoping + test harness)

**Scope:** Remove tier entirely. firmId+role is the complete access model.
- DS: opal_auth refactor, pseudonymizer role-only gate, book-scoping (advisor_id/architect match), auth-handler tier cleanup, portal-authorizer advisorId (`a067e0fb`)
- AE: 13 opal-capital users tier=advisor, FIRM#mockadv, 3 test accounts (`923ad81b`)
- DT: 3 Lambda deploy (`59b7eef2`), schema cleanup .011 (`ec9ff6e2`), portal-v2.1.22 (`5038f0bd`)
- DE: Claims interface stripped (tier/regionId/officeId removed), ProtectedRoute, App, analytics (`1390fa1`)

**Login incident (P0):** 2026-04-01 18:29-18:34 ET (~5 min)
- Cause: bun build outputs `index.mjs` at zip root; Terraform had `handler=dist/index.handler`
- COO diagnosed via CloudWatch: `Runtime.ImportModuleError: Cannot find module 'index'`
- Fix: `aws lambda update-function-configuration --handler index.handler`
- DT hardened: Terraform updated to `handler=index.handler` (`4a36a4ef`)

**Final state:**
- portal-v2.1.22 (tier removed from portal)
- partners-api-v1.12.0 (P3 Lambda)
- portal-auth-v1.5.0 (schema cleanup)
- 4 test accounts: andrew, user@opal, travis (49F admin), chase (49F user, book scoping)

---

## ADHC_HISTRY -- P1/P2 in progress

### P0 COMPLETE (prior session)
BD transaction forensics investigation. RPS approach validated.

### P1 COMPLETE
- AE: 534→557 RPS silver partitions built
- DS: Phase 1 diagnostic — injection needed $402M, DIVZ $164M (acceptable)

### P2 ACTIVE
- DS: Rotation model scripts 02+03 (`2666dc1f`)
- AE: Gold rebuild running (.004, started ~17:16 ET) -- awaiting DIVZ result
- DS: Converter updated to `bronze/rps/` primary (`2c8a4470`)
- AE: 22 March RPS files migrated to `opal-data-schwab/bronze/rps/`, staging deleted

### Schwab bucket routing resolved
- DT .005: Root cause = SSE-AES256 requirement, NOT a write deny
- No IAM/policy changes needed. Fix callers, not the policy.

---

## Open items as of end of session

| Item | Owner | Status |
|------|-------|--------|
| ADHC_HISTRY .004 gold rebuild | AE CloudOps | IN FLIGHT |
| JWT tier removal | DT (TO not yet issued) | Pending COO TO |
| AE partner table data migration | AE CloudOps (TO not yet issued) | Deferred |

---

## Current State

**Status:** COMPLETE (core session work) + 1 in-flight
**Active branch:** `CLOUD`

ADVI_ANONYM P1+P2+P3 all deployed as of ~6:55 PM ET. Full pseudonymization + tier-removed firmId model live. Test matrix ready for Andrew to run manually. ADHC_HISTRY P2 gold rebuild in flight -- AE has the scripts, running full rebuild on EC2. COO needs to issue DT TO for JWT tier removal.

## Next Steps

1. **Wait for ADHC_HISTRY .004 gold rebuild result** -- AE will message when done. Verify DIVZ ~$150-160M.

2. **Issue DT TO for JWT tier removal** -- Remove `tier` from JWT payload (auth-handler jwt.ts) and portal-authorizer context. This completes the backend-side tier removal started by DS .007 and DT .011.

3. **Issue AE TO for partner table migration** -- Move allowedPages/allowedTabs from opal-users-v2 to opal-partner-49financial. Required for .011 Req 6.

4. **Andrew runs P3 test matrix** -- 4 accounts, 13 scenarios in ADVI_ANONYM_P3_PRD.md §Test Matrix.

5. **ADVI_GLDRST P3 activation** -- 12 TOs staged. Still awaiting explicit Andrew GO.
