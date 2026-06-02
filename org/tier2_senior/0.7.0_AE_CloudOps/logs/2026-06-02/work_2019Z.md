# work cycle — 0.7.0_AE_CloudOps — 2026-06-02 ~2019Z

## ANDREW-DIRECT URGENT (via COO 201604Z) — Peter re-confirm + Joe create. All DynamoDB (no Cognito).

### TASK 1 — Peter firmRole=admin RE-CONFIRMED
Read-back opal-users-v2 USER#peter@inflectionwealth.com SK=PROFILE: firmRole=admin persisted
(b3ae5720e), role=user, firmId=inflection, tier=advisor, advisorId=absent, status=active.
The flag DID take -> Andrew's "no full data" = STALE JWT (logged in 18:56Z, before the 19:58Z
firmRole change; token still firmRole=null). Record correct; needs fresh login.

### TASK 2 — Joe CREATED as NON-admin advisor
PutItem USER#joe@inflectionwealth.com SK=PROFILE (attribute_not_exists(PK) create-guard,
read-back verified):
- email=joe@inflectionwealth.com, name=Joe Brandenburg
- role=user, firmRole=ABSENT (non-admin -- Profile-only path test), firmId=inflection, tier=advisor
- advisorId=joe_brandenburg (Andrew-directed: non-admins need advisorId for own-scope; edge :312
  admits for own book)
- password=inflectionwm7 (same as Peter): passwordHash + password_hash set to Peter's exact bcrypt
  hash ($2b$12$IHAlPUE1...). auth-handler auth.ts:48 verifyPassword(pw, user.password_hash);
  db.ts:108 maps passwordHash||password_hash. Reusing Peter's working hash = format-compat + same
  plaintext. mustChangePassword=false (no force-reset).
- joe_brandenburg/book.json EXISTS (41KB) -> Profile renders own book.
- Shape mirrors the inflection PROFILE / 49F non-admin advisor template; only delta from Peter =
  no firmRole + advisorId added, per the access model.

### CRITICAL — both need FRESH logins (role/advisorId baked into JWT at login)
- Peter re-login -> firmRole=admin -> full Books tab.
- Joe login (joe@inflectionwealth.com / inflectionwm7) -> advisorId=joe_brandenburg, firmRole=null
  -> Profile-only own-book (non-admin; W4b FE tab-gating RD~C).

### Outcome
RAVC2 to COO (201900Z) + CTO + CVO + RD~C. Both ready for Andrew's admin-vs-non-admin smoke
contrast. DynamoDB writes (no code-file); this log + the read-backs are the audit trail.
