# NEVER-WIDEN SIGN-OFF PACKET -- the bounded Opal-class walk principal (created, walked by ~D, deleted)

**For:** `1.0.0_SA_CTO` (half 1; "yes in principle" msg 101080), and the second half as the CTO routes it.
**Prepared by:** `2.0.0_SA_COO~P`, 2026-09-26 ~02:4xZ. **Operator of the create and delete:** `2.0.0_SA_COO~P`.
**Walker:** `2.0.0_SA_COO~D`, which runs one signed-in PROD walk with a HAR.
**Authority:** Andrew-direct ~02:1xZ, *"have an agent do those walks and record HAR"* (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_021xZ_OPEN_CALLS_1_3_AND_AGENT_WALKS.md` @37025a10e9).
The Orion call rides Andrew's earlier "go" for ONE call on Purfeerst (plan 01209afb.., expires 2026-09-26T12:00Z).

**NOTHING IS CREATED BY THIS PACKET. STOP until both halves are at HEAD naming this file's blob.** Every line
citation is SOURCE at `@2df913f644`. The served bytes of the auth-handler, authorizer and edge were NOT compared this
run, and that is named.

## Why not the IB-rtf-3 principal

The signed IB-rtf-3 principal (packet blob a1f36b95) is a 49financial FIRM_ADVISOR. It reaches only the 49F retry:
- Purfeerst is Inflection, another firm.
- Y's Analysis upload refuses a partner-class principal (INPUT_ACCESS_DENIED, ~Y msg 101077).

Only an Opal-class principal reaches all three acts.

## K1 -- ONE `opal-users-v2` PROFILE item (the login)

| attribute | value | the line that reads it |
|---|---|---|
| `PK` / `SK` | `USER#usr_irptwalk_<epoch>` / `PROFILE` | `infra/aws/opalinvest_dev/lambda/auth-handler/src/db.ts:130` (GetItem by PK after the e-mail-index lookup) |
| `email` | `irpt-walk-<epoch>@opal.test`, lower-case | `auth.ts:86` (lower-cased lookup); the `.test` TLD never receives mail |
| `passwordHash` | bcrypt (12 rounds, as `password.ts:11`) of a random 32-byte password generated at run time | `db.ts:140`; `auth.ts:95` |
| `name` | `IRPT walk principal (Andrew-direct 20260926)` | `db.ts:141` |
| `role` | `user` | `db.ts:142`. `admin` would take every admin bypass: edge `index.mjs:204`, authorizer `index.mjs:86-101` |
| `firmId` | `opal-capital` | `db.ts:143`; `jwt.ts:168` gives `tier = internal`; `auth.ts:207` skips the partner lookup (also refresh `:543`, `/auth/me` `:577`) |
| `status` | `active` | `auth.ts:105` (login), `:254`, `:537` |
| `createdAt` | ISO instant | the refresh token's row binding |
| `createdBy` | `2.0.0_SA_COO~P walk-principal-20260926` | provenance; the census marker |

**Deliberately ABSENT:**
- `userType`: `Dev` is superadmin.
- `mfaEnabled` / `mfaChannel`: they read `false` / `none`, so the MFA gate at `auth.ts:115` is skipped and nothing is sent.
- `phoneNumber`.
- `mustChangePassword`.
- every advisor field.
- the `FIRM#opal-capital / MEMBER#` item.

**K1-CRED -- the handover:** one SSM SecureString `/irpt/walk-principal/<epoch>/password` (the aws/ssm key) holds the
password.
- The walker reads it BY NAME into browser memory only.
- Neither I nor the walker prints it, logs it, messages it or commits it.

**ROLLBACK:**
- K1: `DeleteItem {PK, SK}`, verified by a consistent `GetItem` returning no `Item`.
- K1-CRED: `delete-parameter`, verified by `ParameterNotFound`.
- Both tables have PITR, so the item survives in backups (named, not a defect).

## K2 -- the session (never recorded)

The access token is `tier=internal, role=user, firmId=opal-capital`. Its TTL is 15 min (`jwt.ts:17`).

The refresh token has a 7-day TTL (`jwt.ts:18`) but re-reads the row on each refresh, so it dies with K1. **Token
life therefore <= 60 min** (CTO limit 1): the walk runs inside 60 min of the login, K1 is deleted at the walk's end,
and the last access token dies <= 15 min after that.

## THE BLAST RADIUS -- wider than IB-rtf-3's, stated plainly

For its life, the principal holds **an internal Opal user's read reach**, the same class as Andrew's own login:
- **API authorizer:** tier `internal` -> ALL firms (`infra/aws/users/lambda/portal-authorizer/index.mjs:278-286`).
- **Edge:** tier `internal` takes the advisor bypass (`infra/aws/lambda-edge/auth-validator-edge/index.mjs:400-406`).
- **opal-partners-data:** `opal-capital` is admin-bypassed (`infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py:168-169, 1657-1659`),
  giving every firm's advisor intelligence.
- **IRPT:** OPAL_GLOBAL (`_authz/served.py:252-261`) across all three firms.
- **Listing:** it appears in the internal user listing (`db.ts:400-403`) while it exists.

**The mechanical bound is the interval, NOT the grant.** No mechanism stops an internal user from other reads during
the walk. CTO limit 2 binds the walker's script:
- **Allowed:** the page reads, the 49F Performance retry, Purfeerst's Performance (the armed one-use Orion call only),
  and ONE Analysis upload of `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/aapl-vnq-12.03.csv`.
- **Forbidden:** any export, a second vendor call, and any grant or admin action.
- **Proof:** the committed HAR is the whole call list (limit 3).

The one-use plan gate refuses any second Orion call mechanically (the PERFORMANCE_USE# row).

**Branches:**
- (a) **Walk completes.** Delete K1, then K1-CRED, then read the logs. Rollback = the deletes.
- (b) **Walk fails or is abandoned.** The same deletes, the same turn.
- (c) **The deletes fail.** Set K1 `status` to `disabled`: `auth.ts:105` refuses login and refresh refuses too. Then
  escalate loud. Never leave it half-landed (NEVER-2).

## THE SEQUENCE

1. **Open the ledger** `irpt-walk-principal-20260926` and commit its OPEN sentinel.
2. **Pre-read:** 0 users with the e-mail on the index, and `ParameterNotFound` on the name.
3. **Put K1-CRED, then K1** (conditional on `attribute_not_exists(PK)`). Read K1 back consistently and record a digest
   excluding `passwordHash`.
4. **Hand over to `2.0.0_SA_COO~D`:** the e-mail, the parameter NAME, these limits, and the deadline.
5. **~D walks.**
   - Login -> the 49F retry -> Purfeerst Performance -> the one upload.
   - ~D commits the HAR **scrubbed of credentials**: the login body's password, every `Authorization` header, every
     cookie, and the `accessToken`/`refreshToken` values in response bodies.
   - Client data in the HAR stays, as the record rules.
6. **Delete.**
   - Read the password into memory.
   - `DeleteItem` K1 and verify the failing read.
   - One login attempt with the password must be refused `Invalid email or password`, 1 of 1. It creates one
     throttle-counter item with a TTL, named in the ledger.
   - Delete K1-CRED and verify `ParameterNotFound`.
7. **Audit.**
   - The auth-handler log shows the principal's logins inside the interval, plus the one refused attempt after delete.
   - The IRPT function logs show no request after the last token's `exp`.
   - ~D confirms a page reload after the delete lands on `/login`.
   - Record the interval `[K1 put, max(K1 delete verified, last access exp)]`, then close and commit the ledger.
8. **Timing:** every step before 2026-09-26T12:00Z (CTO limit 4).

## WHAT THIS PACKET DOES NOT COVER

- Any second principal.
- Any grant, roster (`/opal/irpt/opal-principal-roster`), ownership-map or directory write.
- Any change to the auth-handler, authorizer, edge or JWT keys.
- Any export or render.
- Any vendor call beyond the armed plan.

## WHAT THE HALVES SIGN AGAINST

This file's committed blob, the key list K1 + K1-CRED + K2 above, and the sequence's rollback.
