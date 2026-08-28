# DEPLOY LEDGER -- ETFS_SATELLITES.TO-7-AE: the scoped satellites route (portal-auth)

**STATUS: CLOSED -- COMPLETE** at 2026-08-28T02:33Z. Applied in full in-session, verified on the
live plane, nothing half-landed. Opened at apply start per CLAUDE.md NEVER#2.

⚠ **CLOSED refers to the DEPLOY, not to the TO.** `T7AE-AC3`'s **EXERCISED** half is PARTIAL: the
route is live and auth-gated (discriminated in both directions), but the AUTHENTICATED fetch showing
served bytes match the object is outstanding on a credential this seat does not hold. Named in full
below. **Do not read this closure as TO-7-AE complete.**

| field | value |
|---|---|
| opened | 2026-08-28T02:28Z |
| seat | `0.7.0_AE_CloudOps~S` |
| issuer | `2.0.0_SA_COO~Z` (TO `ETFS_SATELLITES.TO-7-AE`, AC0b @`67a260c6ab`) |
| certifier | `3.0.0_SA_CVO~Z` |
| stack | `infra/aws/terraform/portal-auth/` |
| artifact commit | `0a2855cbe8` (AC0b fix + source-map hash) |
| router source | `@40697fe79d` (`0.7.0_AE_CloudOps~Y`, POSN_TENANCY.TO-4-AE) |
| closed | 2026-08-28T02:33Z |

## THE [STOP] AND ITS LIFT

`2.0.0_SA_COO~Z` placed a `[STOP]` on any `portal-auth` apply (msg 11907) because the apply would
have wired `/api/scoped/satellites/*` to `shared-advisor-router:24`, **which does not contain the
satellites code** -- the route would go live DEAD while every instrument read green.

`T7AE-AC0b` was made the **sole lift condition**. It is discharged (see below), and the issuer
pre-authorized the apply on that discharge: *"Discharge it and the apply is authorized without a
further word from me."*

## AC0b -- DISCHARGED, ALL THREE REQUIREMENTS

**(1) REBUILT + UPLOADED** via `infra/aws/lambda/ci/build-nodejs-lambda.sh portal-auth
shared-advisor-router` (Build Ladder rung 2 -- no new tooling):

    s3://opal-313476888478-lambda-artifacts/portal-auth/shared-advisor-router.zip
      2108 B | LastModified 2026-08-28T02:25:36Z (UTC, s3api)
      content-sha256 qrL3PFqRnq5RUyQ4SDJvZQWDreLnl7rmNWZ25IF8cx0=   (was 1xewzMSnrs/...)

**(2) CONTENT-VERIFIED, LITERALS ONLY** -- `bun build --format=esm` inlines deps and mangles
identifiers, so an identifier probe returns a FALSE ABSENCE:

    NEW artifact        '/api/scoped/satellites/'            PRESENT
                        'platinum/satellites/registry.json'  PRESENT
    NEGATIVE CONTROL    the SAME probe on the PREVIOUS artifact: both ABSENT  <- control fires
    POSITIVE CONTROL    carried-forward literals ('Platinum summary files must be accessed',
                        'platinum/advi/') present in BOTH  <- the probe reaches both

**(3) GATE COUNTS, from the SCRIPT's own run** (not my separate invocation): **27 pass / 0 fail**
across 2 files. 17 pre-satellites + 10 satellites = 27.

## THE DISCRIMINATING BEFORE/AFTER -- why AC0b was not a formality

    BEFORE the rebuild   Plan: 0 to add, 1 to change   (distribution only)
                         the new behavior would bind the LITERAL shared-advisor-router:24
    AFTER the rebuild    Plan: 0 to add, 2 to change
                         + aws_lambda_function.shared_advisor_router[0] updated
                         ~ s3_object_version  BT6gIE9F... -> N3w_OHAi...
                         ~ qualified_arn      :24 -> (known after apply)

**The plan itself changed shape.** Before, it would have added a route pointing at code six days
older than the feature. After, it publishes the code first and re-pins every behavior to the new
version. That difference IS the evidence AC0b was load-bearing rather than ceremonial.

⚠ **A reader will see four `lambda_arn = "...:24" -> null` lines and should not panic:** those are
the provider re-rendering the existing associations because `qualified_arn` is changing. The new
value is `(known after apply)`. Nothing is being unwired.

## WHAT IS BEING APPLIED

| resource | change |
|---|---|
| `aws_lambda_function.shared_advisor_router[0]` | in-place; new `s3_object_version` + `source_code_hash` -> publishes a new version |
| `aws_cloudfront_distribution.portal` | in-place; ADDS the `/api/scoped/satellites/*` behavior and re-pins existing behaviors to the new qualified_arn |

**0 to add, 2 to change, 0 to destroy.** No resource destroyed. No other stack touched.

## ROLLBACK

Re-upload the previous artifact (`content-sha256 1xewzMSnrs/sENR6Z998cqvZ8+jdPZtPM5hIWkaafM8=`,
still recoverable as a prior S3 object version) and re-apply, which republishes and re-pins; or
revert the behavior block. ⚠ **CloudFront distribution updates propagate and are not instant** --
a rollback is not immediate either, which is a reason the content check preceded the apply rather
than following it.

## NOT LIFTED BY THIS

The `ETFS_SATELLITES` **PROD promote** (Andrew's word, DT lane) · `D1_CATVIEWS` · `ETFS_INGEST`
anything · the **consumer seam** (`ETFS_SATELLITES.TO-8-DE`, `0.4.0_DE_ClientPlatform~S`) -- **a live
route with nothing reading it is still a page that renders empty.**

---

## COMPLETION -- APPLIED 2026-08-28T02:29:53Z

    APPLY        0 added, 2 changed, 0 destroyed
    RE-PLAN      "No changes. Your infrastructure matches the configuration."
    VERSION      shared-advisor-router:25 published 2026-08-28T02:29:53Z, CodeSize 2108
                 (v24 was 1998, 2026-08-21)
    BEHAVIORS    27 (was 26) -- exactly one added
    WIRING       /api/scoped/satellites/*
                   viewer-request   auth-validator-edge:18
                   origin-request   shared-advisor-router:25    <- the NEW version
                   origin-response  shared-advisor-router-response:5
    DISTRIBUTION Status "Deployed" (a CloudFront update is not instant; this was confirmed,
                 not assumed)

### The rung that mattered: does the DEPLOYED v25 carry the code?

Literals only -- `bun build --format=esm` mangles identifiers, so an identifier probe returns a
FALSE ABSENCE:

    '/api/scoped/satellites/'             v25 PRESENT   v24 ABSENT  <- control fires
    'platinum/satellites/registry.json'   v25 PRESENT   v24 ABSENT  <- control fires
    'unknown_satellites_resource'         v25 PRESENT   v24 ABSENT  <- control fires
    'satellites_unknown_leaf'             v25 PRESENT   v24 ABSENT  <- control fires
    POSITIVE CONTROL -- carried-forward literals present in BOTH, so the probe reaches both:
    'Platinum summary files must be accessed', 'platinum/advi/'

## AC3 -- APPLIED yes; EXERCISED **PARTIAL**, and the outstanding half is NAMED

**LIVE AND WIRED, discriminated rather than asserted:**

    /api/scoped/satellites/registry.json          HTTP 401  application/json   51 B
    /api/scoped/satellites/not-a-real-thing.json  HTTP 401  application/json   51 B
    KNOWN-GOOD CONTROL (existing scoped route)    HTTP 401  application/json   51 B  <- identical shape
    NO-BEHAVIOR CONTROL (/api/scoped/zzz-.../)    HTTP 403  application/xml   111 B  <- DIFFERENT shape
    body: {"error":"Missing or invalid Authorization header"}

>> **Before this apply the satellites path had no behavior and would have produced the 403/xml/111
   shape. It now produces the 401/json/51 shape byte-for-byte identical to a known-good scoped
   route.** That is positive evidence the new behavior is live and reaching `auth-validator-edge`,
   and it is discriminating in both directions.

⛔ **WHAT IS NOT SHOWN, AND I AM NOT CLAIMING IT:** an AUTHENTICATED fetch proving the rewrite
serves `platinum/satellites/registry.json` from `opal-data-cot` with served bytes matching the
object (size/ETag). **A 401 proves the route reaches the auth gate; it says NOTHING about what the
rewrite does after the gate.**

**BLOCKED ON:** a bearer. The committed exercise pattern
(`.../throwaway_catch/catch404.mjs:24-28`) mints one by POSTing `{email, password}` to
`/auth/login`, but takes them from `TEST_EMAIL`/`TEST_PASSWORD` (or `TEST_TOKEN`) -- **deliberately
not committed, which is correct.** None is set in this environment, and I did not go looking for
login material in Secrets Manager.

⭐ **The natural discharge path is `ETFS_SATELLITES.TO-8-DE`** (`0.4.0_DE_ClientPlatform~S`): the
consumer seam calls this route from the portal with a real session, so their exercise produces the
authenticated evidence as a by-product. Coordinating beats minting a second credential path.
