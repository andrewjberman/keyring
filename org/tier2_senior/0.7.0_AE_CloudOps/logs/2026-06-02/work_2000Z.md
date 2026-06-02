# work cycle — 0.7.0_AE_CloudOps — 2026-06-02 ~2000Z

## ADVI_INFPRM.W4a — provision Peter firmRole=admin + edge admin-path + ownership_map — COMPLETE

COO dispatched W4a (IMMEDIATE) as the answer to my own pre-smoke flag (193340Z): Andrew ruled
the access model (admins = full Books/relationship drills; non-admins = Profile-only). Fix =
firmRole=admin (edge-exempt from advisorId), NOT advisorId=peter_lee. DT offline -> routed to AE
(DynamoDB = CloudOps domain + AE traced the record).

### (a) PROVISION — DONE / LIVE
opal-users-v2 PK=USER#peter@inflectionwealth.com SK=PROFILE -> SET firmRole=admin via scoped
UpdateItem (ConditionExpression attribute_exists(PK); --return-values ALL_NEW read-back).
Verified after: firmRole=admin; role=user / tier=advisor / firmId=inflection / advisorId=null
UNCHANGED. Patrick/Joe NOT touched (stay non-admin). No DT per-user provisioning script exists
(migrations 001-004 = table/firm setup), so the CTO-traced scoped UpdateItem was correct.

### (c) EDGE ADMIN-PATH — CONFIRMED (code-traced)
firmRole record -> JWT -> edge:
- auth-handler login: src/lib/partner/index.ts:30 reads firmRole from PROFILE -> auth.ts:156 ->
  jwt.ts:81 adds firmRole to JWT claims (truthy 'admin') -> portal-authorizer index.mjs:210
  propagates to authorizer context.
- auth-validator-edge:310 isAdmin = role==='admin' || firmRole==='admin'; :311 `if (!isAdmin)`
  wraps the WHOLE 004c block (advisorId requirement :312 + getOwnershipMap :329). firmRole=admin
  -> isAdmin=true -> block SKIPPED -> relationship/client/account drills no longer 403.
- Lambda: opal-partners-data _is_admin_bypass includes firm_role=='admin' -> books relationship
  platinum-summary serves firm-scoped data (firmId via W2 fallback). e2e: edge admin-pass ->
  Lambda serve -> 200-with-data.

### (d) OWNERSHIP_MAP — NOT NEEDED
getOwnershipMap is inside `if (!isAdmin)`; admins never reach it. The absent
platinum/inflection/ownership_map.json is irrelevant for admin Peter. No production. (Would only
matter for a non-admin advisor-scoped user; per Andrew's model Inflection has none on the drills.)

### CRITICAL re-smoke gate
firmRole is baked into the JWT at LOGIN. Peter's current session (lastLogin 18:56Z, pre my 19:58Z
change) carries firmRole=null -> STILL 403. Andrew must LOG OUT + LOG BACK IN as Peter for a fresh
JWT before re-smoking the Segment relationship-data.

### Outcome
RAVC2 to COO (200046Z) + CTO + CVO. AC-W4a ✓ / AC-W4c ✓ / AC-W4d N/A. Pairs with RD~C W4b (FE
admin/non-admin tab-gating). DynamoDB write (no code-file commit); TO status + this log document it.
