# NEVER-WIDEN SIGN-OFF PACKET -- the bounded admin + internal + Dev UI-walk principal (created, walked by ~D, deleted)

**For:** `1.0.0_SA_CTO` (half 1) and `4.0.0_SA_CRO` (half 2), per CTO msg 101151.
**Prepared by:** `2.0.0_SA_COO~P`, 2026-09-26 ~13:2xZ. **Operator of the create and delete:** `2.0.0_SA_COO~P`.
**Walkers:** `2.0.0_SA_COO~D`: one signed-in PROD walk of `/investor-reporting` with a HAR scrubbed in-stream. In the
same window, `2.0.0_SA_COO~Y`: ONE Analysis upload of its v2 input, logged and scrubbed (Y msg 101161). This saves a
second create under a second packet.
**v6 (14:5xZ) -- WINDOW 2 (CTO 101240 YES).** The first principal (`irpt-uiwalk-1790430787`) was created 13:53:14Z,
deleted 14:22:22Z and audited; ledger `irpt-ui-walk-principal-20260926` is CLOSED. The diff against v5 is:
- a NEW principal: the same K1 shape under a new `<epoch>`, created only after both halves name this blob;
- its times;
- K6, the export-B BEFORE read, below.
K4 and K5 run again as signed in v5: the first K4 input is owned by the deleted principal, and the generate function
now carries `jsonschema` (85TXFzzv + irpt-common:5, LIVE 14:52:47Z, ledger `irpt-generate-jsonschema-fix-20260926`
CLOSED, deployed import census 59 modules / 0 failed). Export deploy (B) stays OUT of this window, so the superadmin
session never spans a deploy. Relationship-level Performance is NOT fixed yet, so no FWD-1 re-trace rides this window.
**AMENDED (v5, 14:1xZ): K5 also names the hop-6/7 recipe's YCharts reads and queue redelivery of at most 5 receives
(~Y 101209).**
**AMENDED (v4, 14:1xZ): K5 added -- runbook hop 3, ONE `POST /analysis` (Overview) by ~Y on K4's input (CTO 101204 YES,
cutoff 14:35Z). The diff vs v3 is K5 plus the limit, route and vendor lines that name it.**
**AMENDED (v3, 13:4xZ): K4 re-cut from ~Y's write set @5d70021540 -- K4 causes ONE resident YCharts GET, named.**
**AMENDED (v2) per the CRO's refusal @f8fa80bddc (msg 101163) and CTO msg 101166:**
- the audit grades the HAR by ROUTE;
- the page's own selection rows are named as K3;
- the limit is reworded;
- the CTO's two additions on blob 1301fcff are carried (>= 5 GB free before login; the walk script names each FWD and
  AC it grades);
- ~Y's one upload is added as K4, which the halves may strike without re-cutting anything else.
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

## K3 -- the page's own SELECTION rows (irpt-requests; written by the page, not by P)

- **Where:** each selection the page makes POSTs `/selections`. `_scope/selection_store.py:22-47` writes ONE item in
  `irpt-requests` with key `{tenant: <firm>, request_revision: SELECTION#sel_<64 hex>}` and one attribute,
  `selection_record` (`account_ids`, `account_set_id`, `directory_revision`, `firm_id`, `schema_version`).
- **Content-addressed and identity-free:** `sel_` is a sha256 of the selection (`_scope/selection.py:43`). The record
  names no principal. The write is conditional-put idempotent: a repeat of the same selection by ANY principal maps to
  the same row, and a mismatch refuses. 34 such rows exist today (scan 13:3xZ).
- **RETENTION, not rollback:** the rows are KEPT. Deleting one could break a reference another principal holds for the
  same selection; they carry no identity or credential. The ledger records each new `request_revision` the HAR shows the
  walk minted, as a before/after row census (count and ids).

## K4 -- ~Y's ONE Analysis upload (strike-able) -- RE-CUT (v3) from ~Y's write set

Source: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/K4_UPLOAD_WRITE_SET_20260926.md` @5d70021540, read from the
producer's own code.

- **The act:** exactly ONE `POST /api/scoped/investor-reporting/analysis/inputs` of
  `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/aapl-vnq-12.03.csv` (AAPL 10.01 / VNQ 2.02, USD box ticked,
  tenant `cottonwood`).
  - ~Y observes the outcome only through read-only DynamoDB and S3 reads, NEVER by re-POSTing the same `upload_token`
    (the browser's polling pattern).
  - A lost queue message is therefore not redriven: it stays RESOLVING and is reported as such.
- **Precondition:** `irpt-ycharts-generate` CodeSha256 `IJD6bd1IKKuVwHItl3gZLrAzj7gaqn3LW6DvOrk4wdo=` (LIVE 13:29:39Z,
  ledger `irpt-generate-closure-fix-20260926`), and ~Y's own `generate_package_closure.py` exits 0 on it.
- **K4 CAUSES ONE VENDOR CALL -- named:**
  - The POST sends one `resolve_upload` message.
  - The resident answers it with ONE batched YCharts `securities_info` GET: 2 symbols, no prices, lease-fenced
    (`intake/upload_resolution.py:3-9`; `ycharts/generate/resident_worker.py` `ResidentAssembly.resolve_upload`).
  - Authority: the standing host-workflow authorization, CTO 100667 (1), and this session's egress permission,
    CTO 101098. It is ledgered in this act's ledger with the resident's log line as its receipt.
  - It is the ONLY vendor call this window admits.
- **Write set by the POST** (`irpt-ycharts-generate`, `intake/uploads.py`, tenant `cottonwood`):
  - the retained original, an S3 object;
  - `irpt-requests` row `UPLOAD#<upload_id>`;
  - row `NORMALIZATION#<upload_id>#<revision>` (RESOLVING, `dispatched_at`);
  - ONE SQS `resolve_upload` message on the generation queue.
- **Write set by the resident, one of three branches:**
  - **NORMALIZED:** the NORMALIZED_PORTFOLIO S3 object, row `INPUT#<input_id>`, and the NORMALIZATION# row flipped
    RESOLVING -> NORMALIZED by a conditional put.
  - **NEEDS_CORRECTION:** the NORMALIZATION# row flipped with its reason and findings; no INPUT# row and no normalized
    object.
  - **RETRY** (provider outage): nothing flipped; the message returns to the queue and the row stays RESOLVING.
  - Also: any lease or journal entry the resident session writes around its GET is the session's own bookkeeping, named
    in ~Y's log from the resident's output.
- **RETENTION:** all of it is KEPT, as the acceptance evidence of ledger `irpt-upload-hop2-20260924` S1. ~Y's log names
  every row key and object key.

## K5 -- ~Y's ONE Analysis submission (hop 3) on K4's live input

- **The act:** exactly ONE `POST /api/scoped/investor-reporting/analysis` (Overview), by `2.0.0_SA_COO~Y` as this
  principal, on the input K4 normalized (`portfolio_99e76df8..`; full id and keys in
  `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/LIVE_UPLOAD_1203_EVIDENCE_20260926.md` @3cc73f2b79).
  - It is observed only by read-only DynamoDB and S3 reads: no re-POST and no retry.
  - A provider error is reported as the outcome, not repaired.
- **Why in this window:** the input's owner row binds `principal_id` to THIS principal, and the binding dies with it.
- **VENDOR WRITES, named:** the submission drives the YCharts hop-3 chain -- ONE `holdings_upload`, ONE
  `portfolio_create`, ONE `report_create` and ONE PDF download. It rides the API egress permission (CTO 101100 / 101098),
  ledgered.
- **VENDOR READS and redelivery, named** (~Y's act file
  `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/K5_SUBMISSION_ACT_20260926.md` @10b0ef1dae, runbook hops 6-7):
  - the hop-6/7 recipe's YCharts READS: identity, template, the upload echo, the 7-setting read-back and validate;
  - queue redelivery of at most 5 receives if the resident answers RETRY, each resuming from the job row's
    checkpoints, so no create repeats.
- **What it writes (Opal side):** the submission's own request, job and report rows and objects, which are the
  product's record. ~Y names every row and object key.
- **The YCharts objects it creates** (the holdings upload, portfolio, report and PDF) are named in the ledger and KEPT.
- **Order (window 2):** K4 first, then K5 on K4's new input, one POST each. No cutoff: both run inside the principal's
  60-min life, or not at all.

## K6 -- the export-B BEFORE read (CTO rulings (c) and 101240)

- **The act:** ONE account-level 49F Performance read by the PAGE, by `2.0.0_SA_COO~D`: a single-account 49F client
  selected, Performance opened (YTD).
  - Two requests: the page's own `POST /selections` (K3) and one `GET .../performance/{accountSetId}`.
  - The answer is recorded (HTTP status, `ok`, state, reason, and for a 200 the section count and completeness) as
    deploy (B)'s real BEFORE baseline.
- **What it writes:** a successful Performance read RETAINS its report, as every human read does: `REPORT#` and
  `RETENTION#` rows in `irpt-requests` plus the retained report object. These are named in the ledger and KEPT, since
  they are the product's record. A refusal writes nothing.
- **No vendor call:** 49F computes on Opal's own engine.

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

**THE LIMIT (reworded, CTO 101166):** "page use only: reads plus the page's own selection writes; no admin, export,
grant or vendor call." Plus K4: ~Y's ONE upload and the ONE resident `securities_info` GET it causes. Plus K5: ~Y's ONE
`/analysis` submission and the YCharts hop-3 writes it causes.

**THE AUDIT, GRADED BY ROUTE.** The combined log (~D's HAR plus ~Y's upload log) is censused request by request, with
its denominator printed. Every request must fall in exactly one admitted class:

| class | admitted |
|---|---|
| any method | `/auth/login`, `/auth/refresh` |
| POST | `/api/scoped/investor-reporting/directory/resolve` (page load); `/api/scoped/investor-reporting/selections` (each selection -> K3) |
| POST, exactly 1, by ~Y | `/api/scoped/investor-reporting/analysis/inputs` (K4) |
| POST, exactly 1, by ~Y | `/api/scoped/investor-reporting/analysis` (K5) |
| GET / HEAD | any page read, including K6's ONE 49F account-level Performance GET |

Any request outside these classes is branch (d). This includes, explicitly:
- any request of any method to `/auth/admin/`;
- any POST/PUT/PATCH/DELETE to any other path;
- any `/export` request;
- any second `/analysis/inputs` POST;
- any second `/analysis` POST.

The census prints the count per class, the count outside the classes (must be 0), and the denominator.

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
   - A SELECTION# row census of `irpt-requests` (count and ids), the baseline for K3.
3. **Put K1-CRED, then K1** (`attribute_not_exists(PK)`). Read K1 back consistently; digest it with `passwordHash`
   excluded.
4. **Hand over to `2.0.0_SA_COO~D`:** the e-mail, the parameter NAME, the limits, and the 60-min deadline.
5. **~D walks `/investor-reporting`** with the HAR scrubbed in-stream (password, `Authorization` headers, cookies, token
   values). It grades IVE30-AC3, round 4's AC4s, and round 3's five NOT_EVALUATED (CTO 101151), and the walk script
   names each FWD and AC it grades (CTO addition). In the same window, **~Y makes its ONE upload (K4)** and logs it,
   scrubbed.
6. **Delete:**
   - `DeleteItem` K1, verified by a failing consistent read.
   - One login attempt with the password through the CloudFront route (`https://opalinvest.dev/auth/login`; the
     execute-api URL 403s at the origin guard before any row read) must be refused `Invalid email or password`,
     1 of 1.
   - Delete K1-CRED, verified by `ParameterNotFound`.
   - ~D reloads once and must land on `/login`.
7. **Audit:**
   - The route-graded census of the HAR plus ~Y's log (branch (d) check).
   - The SELECTION# row census re-read: the new ids listed and each traced to a `/selections` POST in the HAR (K3).
   - ~Y's upload rows and objects named (K4).
   - The user census re-read: equal to the pre-walk baseline.
   - IRPT and auth logs show no request after the last token's `exp`.
   - Record the interval `[K1 put, max(K1 delete verified, last access exp)]`; close and commit the ledger.

## WHAT THIS PACKET DOES NOT COVER

- Any second principal.
- Any `/auth/admin/*` request.
- Any write beyond K3 (the page's own selections) and K4 (~Y's one upload): no settings, user, grant, roster,
  ownership-map or directory write.
- Any export or render.
- Any vendor call other than K4's one resident `securities_info` GET and K5's named hop-3 chain (its four writes, the
  recipe's reads, and redelivery of at most 5 receives resuming from checkpoints).
- Any change to the auth-handler, the authorizer, the edge or the JWT keys.

## WHAT THE HALVES SIGN AGAINST

This file's committed blob, the key list K1 + K1-CRED + K2 + K3 (retained) + K4 (retained, strike-able) + K5 (retained) + K6 (the BEFORE read; its retained report kept) above, for window 2's NEW
principal, the stated superadmin radius, and the sequence's
rollback and audit.
