# NEVER-WIDEN SIGN-OFF PACKET -- the bounded admin + internal + Dev UI-walk principal (created, walked by ~D, deleted)

**For:** `1.0.0_SA_CTO` (half 1) and `4.0.0_SA_CRO` (half 2), per CTO msg 101151.
**Prepared by:** `2.0.0_SA_COO~P`, 2026-09-26 ~13:2xZ. **Operator of the create and delete:** `2.0.0_SA_COO~P`.
**Walker:** `2.0.0_SA_COO~D`: one signed-in PROD walk of `/investor-reporting` with a HAR scrubbed in-stream.
**Authority:** Andrew-direct, verbatim *"Agent on an admin+dev login"* (record addendum
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_021xZ_OPEN_CALLS_1_3_AND_AGENT_WALKS.md` @e2eae53ae3).
**Shape:** the same as the Opal-class walk packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_WALK_PRINCIPAL_20260926.md` (blob
fe8e8d89), with only the three role fields changed. That principal was created, walked and deleted, and ledger
`irpt-walk-principal-20260926` is closed.

**NOTHING IS CREATED BY THIS PACKET. STOP until both halves are at HEAD naming this file's blob.** Every citation is
SOURCE at `@2df913f644` unless stated. The served bytes of the auth-handler, the authorizer and the edge were not
compared this run; the CRO half @909dd40acc measured the auth-handler's served bytes for the same three status guards.

## Why this principal

The page `/investor-reporting` admits only a login that is all three of admin, internal and Dev
(`portal/src/components/ProtectedRoute.tsx:105-117`: `role === 'admin'`, `firmId === 'opal-capital'`,
`userType === 'Dev'`). The Opal-class principal (role user, no userType) was redirected to `/market` (~D msg 101106).

## K1 -- ONE `opal-users-v2` PROFILE item

This is identical to packet fe8e8d89's K1 except for the THREE role fields:

| attribute | value | the line that reads it |
|---|---|---|
| `PK` / `SK` | `USER#usr_irptuiwalk_<epoch>` / `PROFILE` | `infra/aws/opalinvest_dev/lambda/auth-handler/src/db.ts:130` |
| `email` | `irpt-uiwalk-<epoch>@opal.test`, lower-case | `auth.ts:86`; the `.test` TLD never receives mail |
| `passwordHash` | bcrypt, 12 rounds (`password.ts:4`), of a random password generated at run time | `db.ts:140`; `auth.ts:95` |
| `name` | `IRPT UI walk principal (Andrew-direct 20260926)` | `db.ts:141` |
| **`role`** | **`admin`** | `db.ts:142`; the page's `requireAdmin` (`ProtectedRoute.tsx:105`) |
| **`firmId`** | **`opal-capital`** | `db.ts:143`; `jwt.ts:168` -> `tier = internal`; `auth.ts:207` skips the partner lookup |
| **`userType`** | **`Dev`** | `db.ts:144`; the page's `requireDev` (`ProtectedRoute.tsx:115`) |
| `status` | `active` | `auth.ts:105` (login), `:254`, `:537` (refresh) |
| `createdAt` / `createdBy` | ISO instant / `2.0.0_SA_COO~P ui-walk-20260926` | the refresh binding / the census marker |

**Deliberately ABSENT:**
- `mfaEnabled` and `mfaChannel`: they read `false` / `none`, so the gate at `auth.ts:115` is skipped and nothing is
  sent. MFA is forced by no role or type: the gate reads only these row flags.
- `phoneNumber`.
- `mustChangePassword`.
- every advisor field.
- the `FIRM#` member item.

**K1-CRED:** one SSM SecureString, `/irpt/ui-walk-principal/<epoch>/password` (the `alias/aws/ssm` key). The walker
reads it by NAME into browser memory only. The ledger records the name and the interval, never the value.

**Rollback:**
- K1: `DeleteItem`, verified by a consistent `GetItem` returning no `Item`.
- K1-CRED: `delete-parameter`, verified by `ParameterNotFound`.

## K2 -- the session, never recorded

The access token's TTL is 15 min (`jwt.ts:17`). The refresh token re-reads the row (CRO @909dd40acc measured this on the
served bytes), so it dies with K1. **Token life <= 60 min:** the walk runs inside 60 min of the login, K1 is deleted at
the walk's end, and the last access token dies <= 15 min after.

## THE BLAST RADIUS -- stated plainly: admin bypasses everywhere for the principal's life

This is a SUPERADMIN session: `role admin` + `tier internal` + `userType Dev`. Every bypass keyed on any one of those
three admits it:

- **API authorizer:** ALL firms, `infra/aws/users/lambda/portal-authorizer/index.mjs:278-286`, where `userType Dev`
  alone is "Dev superadmin -- everything".
- **Edge:** the admin bypass (`infra/aws/lambda-edge/auth-validator-edge/index.mjs:204` role admin; `:400-406`
  internal / Dev).
- **opal-partners-data:** every firm's advisor intelligence at every level
  (`infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py:163-170, 1657-1659`).
- **IRPT:** OPAL_GLOBAL across all three firms (`infra/aws/lambda/investor-reporting/_authz/served.py:252-261`).
- **Auth admin WRITE surface** (the widening this packet exists to name), in
  `infra/aws/opalinvest_dev/lambda/auth-handler/src/index.ts`:
  - `POST /auth/admin/users` creates a user (`:415-420`);
  - `GET /auth/admin/users` lists users (`:427-432`);
  - `DELETE /auth/admin/users/{email}` deletes a user (`:439-447`);
  - `POST /auth/admin/users/{email}/reset` forces a password reset (`:452-460`).

  The session can create, delete or reset ANY user, including Andrew's.
- **Portal admin pages:** every route gated on `requireAdmin` / `requireDev` renders for it.

**The mechanical bound is the INTERVAL, not the grant.** Nothing in the platform stops an admin session from any of
the above for its life. The bound on what is done is the walker's script plus the HAR as the whole call list.
CTO limit, verbatim in substance:

- **Allowed:** page reads only.
- **Forbidden:**
  - any export;
  - any vendor call (the one-use plan gate refuses Orion without an armed plan, and none is armed);
  - any grant or admin act: no request to `/auth/admin/*`, and no write to any settings or user surface.

**The audit check for the write surface:** the committed HAR holds 0 requests whose method is not GET/HEAD to any path
outside `/auth/login` and `/auth/refresh`. It also holds 0 requests of any method to `/auth/admin/`, and ~D's HAR
census prints both counts with their denominator.

## Branches

- **(a) Walk completes:** delete K1, then K1-CRED, then audit.
- **(b) Walk fails or is abandoned:** the same deletes, the same turn.
- **(c) A delete refuses:** set K1 `status` to `disabled` the same turn. `auth.ts:105` refuses the login and `:537`
  refuses the refresh. Then escalate to `1.0.0_SA_CTO` and Andrew (the CTO's condition on fe8e8d89, carried).
- **(d) The HAR shows ANY admin or write request:** a finding, filed as a BLOCKING row. Run the same-turn read of the
  auth table's user census (any row created or deleted in the interval) and the users' `status` fields against the
  pre-walk census, then escalate to Andrew.

## THE SEQUENCE

1. **Disk and ledger:**
   - C: must read >= 5 GB free (CTO 101151).
   - Open ledger `irpt-ui-walk-principal-20260926` and commit its OPEN sentinel.
2. **Pre-read:**
   - 0 users with the e-mail on the index.
   - `ParameterNotFound` on the name.
   - A user census of `opal-users-v2` (count, and each PROFILE's `status` digest; no PII printed), the baseline for
     branch (d).
3. **Put K1-CRED, then K1** (`attribute_not_exists(PK)`). Read K1 back consistently; digest it with `passwordHash`
   excluded.
4. **Hand over to `2.0.0_SA_COO~D`:** the e-mail, the parameter NAME, the limits, and the 60-min deadline.
5. **~D walks `/investor-reporting`** with the HAR scrubbed in-stream (password, `Authorization` headers, cookies, token
   values). It grades IVE30-AC3, round 4's AC4s, and round 3's five NOT_EVALUATED (CTO 101151).
6. **Delete:**
   - `DeleteItem` K1, verified by a failing consistent read.
   - One login attempt with the password through the CloudFront route (`https://opalinvest.dev/auth/login`; the
     execute-api URL 403s at the origin guard before any row read) must be refused `Invalid email or password`,
     1 of 1.
   - Delete K1-CRED, verified by `ParameterNotFound`.
   - ~D reloads once and must land on `/login`.
7. **Audit:**
   - The HAR census (branch (d) check).
   - The user census re-read: equal to the pre-walk baseline.
   - IRPT and auth logs show no request after the last token's `exp`.
   - Record the interval `[K1 put, max(K1 delete verified, last access exp)]`; close and commit the ledger.

## WHAT THIS PACKET DOES NOT COVER

- Any second principal.
- Any `/auth/admin/*` request.
- Any settings, user, grant, roster, ownership-map or directory write.
- Any export or render.
- Any vendor call.
- Any change to the auth-handler, the authorizer, the edge or the JWT keys.

## WHAT THE HALVES SIGN AGAINST

This file's committed blob, the key list K1 + K1-CRED + K2 above, the stated superadmin radius, and the sequence's
rollback and audit.
