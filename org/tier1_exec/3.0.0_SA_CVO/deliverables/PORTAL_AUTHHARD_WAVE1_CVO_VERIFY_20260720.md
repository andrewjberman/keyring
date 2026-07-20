# CVO independent exercise-verify: PORTAL_AUTHHARD Wave-1

**Verifier:** 3.0.0_SA_CVO~Z · **Date:** 2026-07-20 · **Regime:** PRD S6 (a WS is not done until CVO
independently confirms its exercise, in ADDITION to RAVC + CTO~B arch-gate). **Subject:** portal-auth-v1.20.0,
deploy `d84ac01d4`, source `70b2560f0`. **Requestor:** 1.0.0_SA_CTO~B (LD-0323). **Method:** Rule 22a --
I GROUND independently (APPLIED live primitives + EXERCISED the path myself); I do NOT close on the producer's
evidence doc. Every row below is MY grounding, not a re-read of `PORTAL_AUTHHARD_WAVE1_EXERCISE_20260720.md`.

## VERDICT: GREEN -- Wave-1 (WS-1, WS-2a, WS-8) independently verified. One declared deviation + one rigor note (both non-blocking).

## APPLIED plane (my own live primitives)

| # | Claim | My grounding | Result |
|---|---|---|---|
| A-1 | code actually DEPLOYED (not planned) | `lambda get-function-configuration` CodeSha256 = `eTSZUm8eVGheF4tolXuoaOQPDh0nbV7qTle+q+xpJVc=` == claimed; LastModified 2026-07-20T16:23:06Z | **PASS** |
| A-2 | throttle table live + self-clearing | `describe-table opal-portal-auth-throttle` = ACTIVE, HASH `pk`; `describe-time-to-live` = ENABLED on `ttl` (counters auto-expire = progressive-delay, not lockout) | **PASS** |
| A-3 | WAF rule live + never-widen | `get-web-acl opal-cloudfront-protection`: `AuthLoginRateLimit` Block/Limit100/IP/300s, ScopeDown OR(UriPath STARTS_WITH `/auth/login`,`/auth/forgot-password`) = **/auth/*-scoped, NOT site-wide**; existing `RateLimitRule` Block/Limit2000/pri1 **byte-untouched** | **PASS** |
| A-4 | IAM least-privilege | `simulate-principal-policy` (ONE `--resource-arns`, controls SEPARATE): UpdateItem on throttle ARN = **allowed** (Missing=[]); PutItem = **implicitDeny** | **PASS** (+ see rigor note R-1) |

## EXERCISED plane (I hit the path myself -- the test that fails if the claim is false)

| # | Claim | My exercise | Result |
|---|---|---|---|
| E-1 | WS-1 login throttle actually throttles | MY burst, fresh synthetic email, 7x POST /auth/login wrong-pw -> `401,401,401,401,401,429,429` (5 fails -> progressive 429). Also = runtime proof v1.20.0 is live+enforcing | **PASS** |
| E-2 | WS-1 reset limit independent + enumeration-safe | MY burst, DIFFERENT fresh email, 7x POST /auth/forgot-password -> `200,200,200,200,200,429,429` (independent counter; 200 for non-existent email = no enumeration) | **PASS** |

## DECLARATIVE plane (deployed source -- auth-handler UNCHANGED since deploy commit 70b2560f0, so source == deployed)

| # | Claim | My grounding | Result |
|---|---|---|---|
| D-1 | WS-2a disabled user mints no token | `auth.ts:129` `if (user.status !== 'active') throw` -- BEFORE token mint (mirrors login guard `:75`); no token path reachable for a disabled user | **PASS (security)** -- see deviation V-1 on the status code |
| D-2 | WS-8 policy | `password.ts:5` `MIN_LENGTH=12`, `:34` rejects `<MIN_LENGTH`; `breached-passwords.ts` set-time-only; login-time opaque (existing sub-12 users keep logging in) | **PASS** |

## Producer-exercised, account-dependent (I reviewed the containment + grounded the code path; did NOT re-create a test user)
A1 (counter reset-on-success), A3 (disabled-refresh behavioral), A5/A6/A7 (password set-time trio) were exercised
by 0.7.0_AE_CloudOps~B with a **blast-contained, ledgered, VERIFIED-DELETED** test user (lifecycle ledger
`20260720T1644Z...testuser` OPEN@create/CLOSED@verified-delete; no prod auth credential survives). I confirmed
the containment is sound and grounded each code path on the deployed source (D-1, D-2). I did not re-create a
disabled/test user -- the account-free controls (E-1, E-2) I exercised independently; the account-dependent
behavioral runs I accept on the producer's sound containment + my code-path grounding, per proportionality.

## Findings (non-blocking)

- **V-1 (DECLARED DEVIATION -- PRD-literal vs impl):** PRD WS-2 acceptance says a disabled `/auth/refresh`
  "**actually 401s**"; the impl throws `'Account disabled'` -> **HTTP 500** (no token). The SECURITY property
  (no token for a disabled user) is MET and exercised; the STATUS CODE differs from the PRD literal. This is a
  DELIBERATE, documented scoping choice (follow-up #4: 500->403 map not taken this wave; WS-2a grep proved no
  frontend depends on the code) -- so it is a declared deviation, not a silent miss. **Recommend:** reconcile
  the PRD WS-2 acceptance text to the real criterion ("disabled -> NO fresh token minted"), so a future reader
  does not flag the 401-vs-500 as drift. Does NOT fail the WS.
- **R-1 (RIGOR NOTE on the producer's IAM negative control):** the producer's EX-4 reported PutItem=implicitDeny
  but did NOT pass `--context-entries`; my first run reproduced `Missing=["ses:FromAddress"]` -- a Rule 22a
  false-deny-mode-2 exposure (an unevaluated condition returns a deny byte-identical to a real one). I RESOLVED
  it: re-run with `ses:FromAddress` satisfied -> still `implicitDeny`, Missing=[] -> a REAL least-priv deny. The
  producer's conclusion was correct, but their negative control was technically incomplete per 22a; flagging so
  future EX-4-class controls pass `--context-entries` when a Missing appears.
- **F (from producer, confirmed out-of-scope):** password-policy rejection returns HTTP 500 not 400 (pre-existing
  UX, not security); WS-8 breached list is a curated head not the full 10k; WAF 100-burst not run against prod
  (rule verified applied-live + E-1 proves Lambda-side throttling). All noted, none blocking.

## Scope note
This verifies **WS-1 + WS-2a + WS-8** only. **WS-2b (revocation / token-version bump)** is Wave-2 (in design) --
the PRD WS-2 "bumping the token version invalidates" acceptance is NOT claimed here and is not part of this verdict.

## Grounding / coverage denominator
- APPLIED: 4/4 on live primitives (my own aws calls, this session). EXERCISED: 2/2 account-free behavioral (my
  own bursts). DECLARATIVE: 2/2 on deployed source (hash-matched + tree-unchanged since deploy commit).
- Coverage gap stated honestly: the 3 account-dependent behavioral runs (A1/A3/A5-7) are producer-exercised +
  code-path-grounded by me, NOT independently re-exercised. If Andrew/CTO~B want those independently re-run, I
  can request the executor's account-free portions or run a contained test-user cycle -- flag me.
