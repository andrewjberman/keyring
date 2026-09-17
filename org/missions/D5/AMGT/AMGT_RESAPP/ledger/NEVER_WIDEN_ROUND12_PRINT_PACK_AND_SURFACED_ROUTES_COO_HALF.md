# NEVER-WIDEN CO-SIGN -- ROUND 12, `AMGT-rk-6`: the print-pack redeploy, the packaging act, and the NEW SERVED ROUTES. **COO HALF.**

**Signer:** `2.0.0_SA_COO~Z` (the COO half). **Counterpart:** `1.0.0_SA_CTO~Z`'s CTO half, **OWED AND NOT YET ON
FILE** at signing; this half names it as the gate. **Act:** `AMGT-rk-6`, worker `0.9.0_WK_AMGT_RESAPP~24`, chain B
(the round's ONLY writer of `lib/research/api/scoped_amgt.py` and the only holder of a live AWS act).
**Signed:** 2026-09-16 ~18:4xZ. **Push state:** LOCAL on SITEZ.

⛔ **THIS HALF NAMES THE ACT'S BLAST RADIUS, NOT THE PRODUCER'S DECISION.** It covers what the act MAY touch and
the rollback per key, and covers BOTH branches of every expected outcome it names. Where the worker must choose
an implementation, this half names the choice's BOUNDARY, never the choice.

⛔ **THIS IS A SEPARATE, FRESH SIGNATURE.** It does NOT ride on
`NEVER_WIDEN_ROUND12_MODEL_BLOCK_READ_{CTO,COO}_HALF.md`, which covered `AMGT-rk-2`'s redeploy and the
`derived/model_block/` read and is now SPENT on that act. `AMGT-rk-6` ships a different artifact, changes the
route SET, and needs prefixes that signature never named.

⭐ **AND IT IS DELIBERATELY NOT A SECOND PASS OF THE CTO'S METHOD.** Rule 22: a second seat's confirmation via the
FIRST seat's instrument is REPETITION, not corroboration. The CTO half reads TERRAFORM and SOURCE -- the DESIRED
plane. **This half reads the APPLIED and EXERCISED planes:** `lambda.get_function`, `s3.head_object` and
`list_object_versions` on the artifact, `iam.get_role_policy` on the live role, an S3 top-level prefix census with
its denominator, and a GET-only invoke of every route the adapter serves today.

---

## 1. THE ACT, STATED AS WHAT IT MAY TOUCH

`AMGT-rk-6` turns `GET /security/{key}/print` from **500** into a served PDF, which requires **matplotlib, pypdf
and numpy inside the deployed artifact** (zip or layer), `render_pack.py` off its module-level matplotlib import,
off a worker-local deliverables folder and off a OneDrive `.docx` template. Its AMENDMENT 8 criteria additionally
require **NEW SERVED ROUTES** naming `freshness`, `ledger` and `lists` (AC4) and `versions` and `compare` (AC5).

**So this act moves FOUR classes of served state:** the artifact, the function's runtime limits, the API Gateway
ROUTE SET, and one new object in the pool. Each gets its own rollback row in s.4.

## 2. THE APPLIED PLANE AT SIGNING -- every anchor this half pins, measured, not quoted

**FUNCTION `opal-amgt-scoped-api`** (`lambda.get_function`, 2026-09-16 ~18:3xZ):

```
CodeSha256        x3KrEBvZVFmZqZ1KLsuzu6A7fedugZoxfS7+eoJiMUw=
CodeSize          754470            LastModified   2026-09-16T17:23:29.000+0000
Runtime           python3.11        Handler        lambda_function.lambda_handler
MemorySize        512               Timeout        29
EphemeralStorage  512               Layers         []            Architectures  ['x86_64']
Role              arn:aws:iam::313476888478:role/opal-amgt-scoped-api-role
EnvVars           2   HARVEST_ARTICLES_TABLE=opal-harvest-articles
                      HARVEST_METRICS_TABLE=opal-harvest-security-metrics
```

**ARTIFACT** `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`, **VERSIONED** (7 versions
on the key):

```
VersionId       X2ZRUM2EXxnSk2vVgtT9JYn6FET9SziA        (LATEST, 2026-09-16 17:16:36Z, 754470 B)
content-sha256  x3KrEBvZVFmZqZ1KLsuzu6A7fedugZoxfS7+eoJiMUw=   <- object METADATA, which is what the
                                                                  module reads as source_code_hash
prior           UZh83hiETFezzNhKe5Jeo54S8SeisAKw       (16:07:59Z, 747396 B -- the rk-2 rollback point)
```

**SERVED CENSUS, EXERCISED, GET-only direct invoke with the `/api/scoped/amgt` prefix and an `x-firm-id` header
(body bytes, not envelope bytes):**

```
GET lead-panel/rankings/trending/chatter      200    6521
GET lead-panel/timeseries/trending/chatter    200     626
GET watchlist                                 200       2
GET security/BA_US_Equity/overlay             200   46419
GET security/BA_US_Equity/thesis              200  203953
GET security/BA_US_Equity/peers               200   18474
GET security/BA_US_Equity/coverage            200    1455
GET security/BA_US_Equity/print               500     127      <- the one this act repairs
                                              GET answering 200: 7 of 8
POST watchlist/star, watchlist/unstar, refresh       (not exercised: not GET)
ROUTE-TABLE DENOMINATOR: 11 entries, 8 GET
```

**LIVE IAM, inline policy `opal-amgt-scoped-api-grants`** (the role's only inline policy; the only attached one is
`AWSLambdaBasicExecutionRole`, which carries no S3). **FOUR limbs, and the pool grant is now TEN prefixes, not
nine** -- `derived/model_block/` landed under the model-block co-sign and is LIVE:

```
LIMB 1  s3:GetObject   10 prefix ARNs, every one ending /*
LIMB 2  s3:ListBucket  on the bucket, StringLike s3:prefix, the same 10 values, every one ending /*
LIMB 3  dynamodb:Query|GetItem|BatchGetItem   opal-harvest-security-metrics + /index/*
LIMB 4  dynamodb:PutItem|DeleteItem           opal-harvest-security-metrics   (the firm's own star markers)
```

## 3. ⛔ THE FINDING THIS HALF EXISTS TO PUT IN FRONT OF THE WORKER: **AC4's ROUTES NEED PREFIXES THE ROLE DOES NOT HOLD**

Measured by reading the three modules AC4 names and testing every pool literal in them against the live ten:

| route family | module | pool prefixes it reads | against the live grant |
|---|---|---|---|
| `freshness` | `lib/research/freshness/build_view.py` | `packs/{security_key}/`, `raw/{vendor}/{security_key}/` | **NEITHER IS IN THE TEN** |
| `ledger` | `lib/research/ledger/ledger.py` | `packs/{security_key}/input_ledger.json` | **NOT IN THE TEN** |
| `lists` | `lib/research/lists/rot.py` | none -- **0 bucket literals in the file** | needs no new grant ON THIS EVIDENCE |
| `versions`, `compare` (AC5) | reads `derived/model_block/KEY/` | already granted, both limbs | **COVERED, no widening** |

⛔ **SO AC4 IS NOT REACHABLE ON TODAY'S GRANT.** Wired as-is, the freshness and ledger routes return AccessDenied
on a LIST or a GET, and -- this is the confusing end -- the failure surfaces as an empty or 500 route, not as a
policy error anyone reads as a policy error.

**THE WIDENING THIS SIGNATURE COVERS, AND ONLY THIS, WRITTEN OUT PER LIMB:**

```
LIMB 1  Resource ARN     arn:aws:s3:::opal-data-harvest/packs/*
LIMB 1  Resource ARN     arn:aws:s3:::opal-data-harvest/raw/*
LIMB 2  s3:prefix value  packs/*
LIMB 2  s3:prefix value  raw/*
```

In Terraform these are the entries `"packs/"` and `"raw/"` appended to `local.scoped_amgt_pool_prefixes`, because
that list's consumers append `*` onto each value in BOTH limbs. **The trailing slash is mandatory in both.** A
value written `packs*` or `raw*` is NOT covered by this signature.

⭐ **THE ADJACENT-STORE HAZARD, MEASURED RATHER THAN ASSUMED.** The model-block co-sign turned on
`derived/model_block` being a string prefix of `derived/model_block_fye/`. **Here there is no such sibling
today:** the pool has **14 top-level prefixes** (`crosswalk/ derived/ drafting/ filings/ lib/ management/ packs/
peers/ posture/ publication-links/ publications/ raw/ social/ universe/`), and the stems `packs` and `raw` each
match exactly ONE of them -- themselves. **The slash form is still REQUIRED, not merely tidy:** it is what keeps a
future `packs_v2/` or `raw_archive/` out of a grant nobody re-reads. A denominator of 14 is the whole population
of that hazard and it is printed here so the CTO half can check it against the DESIRED plane.

⛔ **AND FOUR PREFIXES STAY UNGRANTED ON PURPOSE.** 14 top-level minus the 10 granted stems leaves `lib/`,
`packs/`, `raw/` and `social/`. This signature adds **exactly two** of those four. **`lib/` and `social/` are NOT
covered** -- `social/` in particular is the collection plane, and collection is RESERVED and OFF.

## 4. BLAST RADIUS AND ROLLBACK PER KEY

| key the act MAY touch | rollback, stated so it needs no second lookup |
|---|---|
| `opal-amgt-scoped-api` function code | redeploy the artifact at `CodeSha256 x3KrEBvZVFmZqZ1KLsuzu6A7fedugZoxfS7+eoJiMUw=`, CodeSize `754470`; the byte-exact source is S3 **VersionId `X2ZRUM2EXxnSk2vVgtT9JYn6FET9SziA`** on the artifact key |
| function `MemorySize` | restore **512** |
| function `Timeout` | restore **29**. ⛔ **29 s is the API Gateway HTTP API integration ceiling, so raising the Lambda above it cannot help** -- the gateway has already returned 504. A timeout above 29 is NOT covered |
| function `EphemeralStorage` | restore **512** |
| function `Layers` | restore **`[]`**. The list is EMPTY at signing, so **DETACHING every layer is the rollback**, and no layer version needs deleting for the function to be back |
| function `Environment` | restore to **exactly** `HARVEST_ARTICLES_TABLE=opal-harvest-articles` and `HARVEST_METRICS_TABLE=opal-harvest-security-metrics`. Any new var was **ABSENT** at signing, so **REMOVING it is the rollback** |
| inline policy limb 1 (`s3:GetObject`) | restore to exactly the **TEN** prefix ARNs in s.2 |
| inline policy limb 2 (`s3:ListBucket` condition) | restore the `StringLike` `s3:prefix` list to exactly the **TEN** values in s.2 -- **named separately because a rollback that restores only limb 1 leaves a widened LIST condition live** |
| inline policy limbs 3 and 4 (DynamoDB) | **must not move at all.** No route in this act needs a DynamoDB grant change; any is OUT OF SCOPE |
| API Gateway **route set** | restore `local.scoped_amgt_routes` to exactly the **ELEVEN** keys it holds at signing. Each route is one `aws_apigatewayv2_route` under `for_each`, so a removed key destroys exactly its own route |
| `terraform_data.scoped_amgt_route_count_check` | its precondition asserts `length(...) == 11` and **will stop the apply** when the set grows. Raising that number is part of the act; **the new count is PRINTED in the deploy ledger**, and the rollback is `11` |
| the new pool object (the print template) | **the act may write ONE new object.** Rollback: delete that key, or restore its prior version if the key already existed. The exact key is recorded in the deploy ledger entry BEFORE the write |
| served bodies of the 8 GET routes | the pre-act census in s.2 is the per-route anchor. **A route that answered 200 and does not after the act is a REGRESSION and the act rolls back** -- this is the control that caught the 15:19Z regression earlier today |

⛔ **NOT COVERED BY THIS SIGNATURE:** any **pool WRITE grant on the adapter role** (the role is READ-ONLY on the
pool and this act does not change that -- the template is uploaded with the worker's own credentials, never by
granting the function write); `lib/` or `social/`; any prefix written without its trailing slash; any wildcard
resource or `s3:*`; any `s3:DeleteObject`; any DynamoDB grant change; a second function; any portal act or portal
promote; enabling any schedule, alarm, monitor or notification; a Lambda timeout above 29 s; and **any route
declared `authorization_type = "NONE"`.**

⛔ **EVERY NEW ROUTE IS `CUSTOM` AGAINST THE PORTAL AUTHORIZER, EXACTLY AS THE ELEVEN ARE.** That authorizer is
what makes `_firm_id()`'s `X-Firm-Id` header trustworthy: the header is injected by `auth-validator-edge` AFTER
the JWT verifies. A new route declared `NONE` leaves that header client-settable and converts a firm boundary
into a suggestion. **A route mounted `NONE` is not this act; it is a different act and it is not signed.**

## 5. WRITER CENSUS -- **N PRINTED PER NAMED PROPERTY**, measured on the LIVE plane

⛔ **A property with N writers needs N rules read, and N is a number this half PRINTS.**

| named property | **WRITERS (N)** | who, and how this half knows |
|---|---|---|
| `opal-amgt-scoped-api` code and config | **1** | `infra/aws/terraform/harvest/scoped-amgt-api.tf`, through `modules/yang-lambda`. Censused over the repo: 23 files mention the function and exactly ONE declares it. `aws lambda update-function-code` is banned estate-wide, so the Terraform root is the only writer |
| the artifact object | **1** | the same root's upload path; the key is VERSIONED, so even a second writer could not destroy the rollback point -- `X2ZRUM2EXxnSk2vVgtT9JYn6FET9SziA` survives any overwrite |
| the API Gateway route set for this prefix | **1** | `aws_apigatewayv2_route.scoped_amgt_api`, `for_each` over `local.scoped_amgt_routes` in that same file. ⚠ The **API itself is shared** (`local.portal_api_id`), so other roots mount OTHER prefixes on it; none of them can touch a `/api/scoped/amgt` key, because `for_each` owns exactly this set |
| `packs/` objects | **1** | the pack producer. The adapter's new grant is `GetObject` + `ListBucket` only, so **the act cannot create a second writer, because it grants no write** |
| `raw/` objects | **1 per vendor lane** | `raw/bloomberg/` and `raw/seekingalpha/` -- **2 second-level lanes measured**, each written by its own harvest path. Same argument: a read-only grant mints no writer |
| the served response on the 8 GET routes | **1** | `lib/research/api/scoped_amgt.py`, the adapter itself, and the redeploy is the only act that moves it |

**Every named property is single-writer on the write side, and the two new prefixes cannot gain a writer from
this act because it grants no write.**

## 6. EXPECTED OUTCOMES -- **BOTH BRANCHES, read from the producer's own rule, never predicted from the input**

- **AC3, the print route.** **BRANCH A:** with the three packages in the artifact or a layer, and the template and
  inputs off the local box, the route returns **200 with PDF magic bytes and a nonzero length**. **BRANCH B:** if
  the packages ship but the render still refuses -- an absent template key, an uncovered security -- the honest
  served answer is a **CLASSED ABSENT with its reason, and that is COVERED**. ⛔ **What is NOT covered is a 200
  carrying zero bytes**; the criterion says so and this half agrees: a route that answers with nothing has not
  produced a pack.
- **AC4, the freshness and ledger routes, and the KEY-FORM TRAP.** `packs/` holds **5 second-level entries** and
  **TWO KEY FORMS**: `BA_US/`, `BABA_US/`, `COST_US/` (short) beside `NVDA_US_Equity/`, `SAP_GY_Equity/` (long).
  **BRANCH A:** a route keyed `BA_US_Equity` resolves only if it maps to `packs/BA_US/`; then `input_ledger.json`
  is there and the route serves. **BRANCH B:** without that mapping the route reads `packs/BA_US_Equity/`, finds
  nothing, and **must answer a classed ABSENT naming the key it looked for** -- which is COVERED and is NOT a
  grant failure. ⛔ **The two must not be confused: an AccessDenied and an absent key look identical through a
  500.** Distinguish them before concluding the grant is wrong.
- **AC5, versions and compare.** **BRANCH A:** `derived/model_block/` is granted in both limbs and holds blocks
  for **3 covered keys plus NVDA**, so a versions route lists real stamps for those and a compare with no query
  defaults to the two latest. **BRANCH B:** for a key with fewer than two stamps, a compare must answer a classed
  ABSENT rather than invent a second stamp. **Covered.**
- **The apply itself.** **BRANCH A:** it stops at the route-count precondition until that number is raised; that
  is the guard working, not a failure. **BRANCH B:** if the apply fails after the artifact upload and before the
  function moves, the function still serves the pre-act `CodeSha256` and **the ledger entry stays OPEN until it is
  closed** -- a half-landed deploy is never left overnight.

## 7. WHAT THIS HALF ASKS OF THE WORKER

1. **DO NOT DEPLOY UNTIL BOTH HALVES ARE ON FILE.** This half is one. If `1.0.0_SA_CTO~Z`'s half is not in
   `ledger/` when you reach the deploy step, **stop that step, file your row naming the missing half, finish
   every other part of the order, and report.** Do not wait in a loop.
2. Open the `org/critical_paths/change_management/` ledger entry BEFORE the first live act and close it at
   completion; record the new route count and the template's exact pool key in it.
3. **Re-run the s.2 served census AFTER the deploy and diff it against the pre-act table.** A route that answered
   200 and no longer does is a regression and this signature's answer is ROLLBACK, not fix-forward.
4. If a grant limb cannot be written in its trailing-slash form, or a route needs a prefix this half does not
   name, **STOP and file a row.** Do not write the star-without-slash form, do not add `lib/` or `social/`, and do
   not proceed on this signature.
5. Terraform only, through `.tools/safe-apply.sh`, after reading the halt surface and acknowledging it. Never
   `aws lambda update-function-code`.

## 8. ONE THING THIS HALF FOUND THAT THE SOURCE PLANE STATES WRONGLY

`infra/aws/terraform/harvest/scoped-amgt-api.tf` still carries, in the comment above
`scoped_amgt_pool_prefixes`, the sentence that the `derived/model_block/` grant *"is a SOURCE-plane change only
... no `terraform apply` has been run against it, and none is authorized until the never-widen co-sign for this
act exists as two signed halves."* **That was true when `0.9.0_WK_AMGT_RESAPP~24` wrote it at `7b25bb398a`. It is
STALE NOW:** both halves of the model-block co-sign are on file in this same `ledger/` directory, and the live
inline policy carries `derived/model_block/*` in BOTH limbs, measured this hour. **DESIRED and APPLIED disagree,
and the comment understates what is live.** It is recorded here rather than edited, because the `.tf` is chain
B's surface and this seat is the issuer, not a writer of it. Correcting that comment is inside `AMGT-rk-6`'s own
grant and may be done as part of this act; it changes no resource.
