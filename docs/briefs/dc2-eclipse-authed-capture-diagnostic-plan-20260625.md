# DC2-Eclipse authed /v1 capture -- diagnostic plan (arch-gate-ready)

**2026-06-25, 0.7.0_AE_CloudOps (DC2 lead).** Prepared while the CTO re-gate is pending
(non-gated design; NO live run until the CTO DC0.4 / DC2 arch-gate clears). ROE:
docs/architecture/DATA_PLATFORM_RECON_ROE.md -- careful/stealthy, never-burn-the-serving-session.

## Grounded finding (the deferral premise is falsified)

CTO deferred the /v1 authed capture (220218Z) on the hypothesis: "shell-only render =>
auth likely in sessionStorage (which Playwright storageState() can't capture)". The parked
artifact `s3://opal-data-inf/eclipse/browser-profile/state.json` CONTRADICTS this:

- **cookies (20)** incl `eclipse.access_token` (.orioneclipse.com), Orion session
  (`apt.sid`/`apt.uid`/`visitor_session`), `.AspNetCore.Antiforgery.*`.
- **localStorage @ https://api.cloud.orionadvisor.com**: `sm.access_token` + `oas_privileges`
  (the SM API bearer the SPA's /v1 XHR use).
- **localStorage @ login.orionadvisor.com**: deviceId / userName / alClientId.

Playwright `storageState()` captures cookies + localStorage (only sessionStorage is excluded).
The auth tokens are NOT in sessionStorage -> a sessionStorage injector is NOT the needed
mechanism. The shell-only render has a different cause.

## Candidate mechanisms (HYPOTHESES -- to confirm under arch-gate, cheapest-first)

1. **TOKEN EXPIRY (recommended first -- cheapest, ROE-safe, no new code).**
   `eclipse.access_token` / `sm.access_token` are short-lived. The parker runs off-peak; a
   crawl run later rides STALE tokens -> shell-only. TEST: park-then-IMMEDIATE-crawl (minimize
   the park->crawl gap), observe whether /v1 XHR authenticate. No token decode/handling
   (security/ROE). If immediate-crawl authenticates -> expiry confirmed -> fix = tighten the
   park->crawl window OR add a refresh step in the parker.

2. **CROSS-ORIGIN localStorage restore.** SPA is orioneclipse.com but authed XHR hit
   api.cloud.orionadvisor.com using THAT origin's localStorage `sm.access_token`. Verify the
   crawl context restores the api-origin localStorage AND the SPA reads it at runtime (vs a
   runtime token-refresh handshake). TEST: assert the context's api.cloud.orionadvisor.com
   localStorage is populated pre-navigation; capture one authed XHR's request headers
   (Authorization present?).

3. **ANTIFORGERY / CSRF.** `.AspNetCore.Antiforgery.*` cookie present -> the API may require
   the antiforgery token echoed in a request header (e.g. X-XSRF-TOKEN) the crawl isn't setting.
   TEST: inspect a captured authed XHR for an antiforgery request header; replicate if needed.

## Sequencing (all gated on CTO arch-gate; ROE-bound)

(1) -> (2) -> (3), cheapest/least-invasive first. Each is observe-or-single-account (Option-A/B),
hard-isolated from the live-serving pull, human-paced. Crawl instance i-010f195f1798b40ad stays
STOPPED until the CTO DC0.4 / DC2 live-gate clears. No token values handled/logged.

## Status
Awaiting CTO re-gate (sent 141518Z) -- ASTN-priority (the original deferral reason) has cleared
(ASTN live 700c07530). DC1-orion's live crawl is ALSO CTO-DC0.4-gated, so it is not an
ungated alternate to this gate.
