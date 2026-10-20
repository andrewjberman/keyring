# RESEARCH 2026-10-20 -- NFRA_FIDUPL: logout primitives, ATT lifetime, the second-login/throttle question

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1). **Answers:** 1.0.0_SA_CTO~DELL1 msg 8796 (during the 60-min sign-in cooldown).
**Sources:** Andrew's HARs 2 and 5 (off git). Names, methods, flags, expiry attributes only; no values.

## 1. Logout -- how a run ends a live session cleanly

HAR 5 (a login+browse capture) contains **no sign-out**. The session-teardown primitives are in HAR 2, both `DELETE`, both -> 204:
- **`DELETE ecaap.advisorchannel.com/user/session/login`** -- ends the ecaap auth session.
- **`DELETE wealthcentral.advisorchannel.com/ssc/platform-authorization/api/v2/unauthorize`** -- ends the platform authorization.

In HAR 2 these fire as a **pre-login cleanup** (clear any stale session before a fresh login), which is exactly the "end a live session
cleanly" primitive. For a run: call **DELETE `/ssc/platform-authorization/api/v2/unauthorize`** then **DELETE
`/user/session/login`** before re-authenticating. **Caveat:** a captured click of the UI "Sign Out" button would confirm the exact
production logout sequence; HAR 5 does not contain one, so the above is the observed teardown, not a confirmed Sign-Out trace.

## 2. ATT lifetime

ATT is `Set-Cookie` only by the post-login cognitive calls (`digital.advisorchannel.com`, #273/#282 in HAR 5). Its attributes:
- **`Expires` present** (not a pure session cookie): the stamp is about **one hour** out from issuance in this capture.
- `httpOnly = false`, `secure = true`.
- **But** ATT was already present on the FIRST request of HAR 5 (carried from a prior session), so despite the ~1h stamp it is
  **refreshed/rolling** -- each session's cognitive calls re-issue it, and it persists in the profile between sessions.
- **Implication:** the seeded ATT is not permanent; it is refreshed every time a session reaches home and the cognitive calls run. A
  profile that signs in regularly keeps a live ATT; one left idle past the roll window may need a re-seed. A single capture cannot give
  the true persisted TTL -- treat ATT as "kept alive by use", re-seed if a run ever finds it expired.

For reference, the other session cookies' attributes (HAR 5, names/flags only):
- `JSESSIONID`: httpOnly=true, secure=true, ~30-min expiry.
- `SSCPLATFORMSUMMARY`: httpOnly=true, secure=true, ~30-min expiry.
- `SSCSINGLECONTAINER`: httpOnly=true, secure=true, ~30-min expiry.
- `ATC`: httpOnly=false, secure=true.

## 3. Second login while a session is live / throttle window -- NOT measured

- **Not measurable from HAR 5** (one clean login, no repeat). The data does not show a refusal or a throttle window.
- The evidence that a throttle exists is **operational, not in the HAR**: the COO's observation that four sign-ins in ~20 minutes
  (Andrew's hand sign-in, two scripted, one trace) preceded the 403s. That correlation, not a measured rule, is why the STOP was called.
- **What the HARs DO show that bears on it:** every clean login in HAR 2 BEGINS by tearing down any prior session (the two DELETEs in
  section 1). So the platform expects a logout-before-login, and stacking live sessions is the likely trigger.
- **REC for the one post-cooldown attempt:** logout first (section 1 DELETEs), then one sign-in; stop at the first 403 and report; never
  stack a second login over a live session; keep the inter-attempt spacing the STOP set (>=60 min) until a real throttle window is
  measured. A true throttle number can only come from a deliberate, spaced probe, which is not worth the lockout risk now.

## Not measured

- The production "Sign Out" trace (no capture).
- ATT's true persisted TTL across days (needs a multi-day profile observation).
- The exact throttle threshold/window (needs a spaced probe; not advised during lockout risk).
