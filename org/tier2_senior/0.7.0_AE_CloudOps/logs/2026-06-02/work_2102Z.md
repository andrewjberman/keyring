# work cycle — 0.7.0_AE_CloudOps — 2026-06-02 ~2102Z

## ANDREW-DIRECT URGENT (COO 205802Z): verify Joe's JWT advisorId — found a TABLE CORRECTION

### Root: JWT identity claims come from opal-partner-{firmId}, NOT opal-users-v2
auth-handler (infra/aws/opalinvest_dev/lambda/auth-handler/): getPartnerIdentity(email,firmId)
(db.ts:29) -> getPartnerProfile (lib/partner/index.ts) reads opal-partner-{firmId}
(tableName.ts -> opal-partner-inflection), key=email. JWT mint (auth.ts:152-156, jwt.ts:80-81):
advisorId=partnerIdentity.advisorKey, firmRole=partnerIdentity.firmRole. opal-users-v2 =
AUTH ONLY (verifyPassword + getUser). So firmRole/advisorId set on opal-users-v2 do NOT reach
the JWT.

### Joe — FIXED
Created opal-users-v2 record earlier (auth OK) but NO opal-partner-inflection entry ->
partnerIdentity=null -> JWT no advisorId/firmRole -> "Advisor Identity Unavailable". Created
opal-partner-inflection joe@inflectionwealth.com: advisorKey=joe_brandenburg, advisorName=Joe
Brandenburg, advisorRole=architect, firmRole=user (NON-admin; mirrors template
test-advisor@inflectionwealthmgmt.com architect/user). Read-back verified. Fresh login ->
advisorId=joe_brandenburg + firmRole=user -> Profile resolves own book (joe_brandenburg/book.json
41KB exists). opal-users-v2 advisorId field is inert-but-harmless (record needed for password auth).

### Peter — already correct in JWT-source table
opal-partner-inflection peter@inflectionwealth.com ALREADY = advisorKey=peter_lee,
advisorName=Peter Lee, advisorRole=architect, firmRole=admin (created 5/28 by CTO). So Peter's
fresh-login JWT = admin + advisorId=peter_lee. His "no data" = STALE JWT only (re-login). My W4a
opal-users-v2 firmRole=admin edit was on the inert table (harmless, didn't drive JWT — partner
table already had admin).

### Correction to W4a premise
The "Peter non-admin/empty-advisorId -> 403" diagnosis (+ 2 senior confirmations) read
opal-users-v2; the JWT-source (opal-partner-inflection) had Peter correctly admin all along.
Access-model conclusions + CTO RULING-a stand; the provisioning lever is the partner table.

### Outcome
RAVC2 to COO (210210Z) + CTO+CVO+RD~C. Both Peter+Joe correct on FRESH logins. Memory:
reference_jwt_identity_claims_from_opal_partner_firmid_not_users_v2. Asked COO whether to revert
the inert opal-users-v2 edits (rec: leave+document).
