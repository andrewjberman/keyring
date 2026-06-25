# BD 49F Durable Auto-Auth -- CV-driven auto-login + OTP-relay (supersedes the manual-cookie interim)

**Author:** 3.0.0_SA_CVO | **Date:** 2026-06-25 | **Priority:** HIGH (Andrew-direct, un-defers the auto-login)
**For:** 1.0.0_SA_CTO (arch-gate) -> AE (build) | CVO drives + verifies | Andrew = OTP-relay recipient
**Supersedes:** the manual-cookie interim (docs/briefs/bd-49f-interim-cookie-solution-rest-api-20260625.md) -- which is correct as a BRIDGE but proven HIGH-TOUCH (see Why).

## Mandate (Andrew-direct, verbatim intent)
"I should NEVER need to [manually reseed]. Create an automatable structure that checks cookie status ahead of an ad-hoc or scheduled job and goes and gets the cookie. ASTN_WSJ&FT-style **kimi-attached layer with computer vision** that can SEE the login screen and engage as needed. If it really needs OTP, **an SMS notification with a request to provide the email or text OTP** I received (depending on how BD does multi-auth)."

## Why now (the interim is too high-touch)
Measured today: the `.bd.identity` absolute SSO cap is SHORT (~hours, not >=24h). Keepalive refreshes the idle/sliding timeout but CANNOT beat the absolute cap -> the cookie dies a few times/day -> the manual reseed is multiple-times-daily friction. The durable fix is auto **re-authentication** (a fresh login RESETS the absolute clock -- the one thing keepalive + manual-reseed can't do). Andrew has now un-deferred it.

## Architecture (4 components)
```
[scheduled/ad-hoc BD job]
      | (pre-flight)
      v
(1) COOKIE-FRESHNESS GATE  -- probe GET /datamining/auth/token; 200=proceed, 401=trigger refresh
      | (401)
      v
(2) CV-DRIVEN AUTO-LOGIN (the "kimi vision" layer)
      Playwright browser + a VISION model (Kimi) in a perceive->act loop:
      screenshot -> vision reads the screen -> decide action (fill user/pass, dismiss modal,
      detect OTP screen) -> Playwright executes -> repeat. Rides the RESIDENTIAL PROXY
      (ASTN_WSJ&FT pattern) so BD sees a real-looking egress (NOT an AWS datacenter IP).
      | (if OTP/MFA screen detected)
      v
(3) OTP-RELAY via SMS  -- SMS Andrew "BD needs your OTP -- reply with the email/text code".
      Andrew replies the CODE ONLY (not the whole login) -> automation enters it -> login completes.
      | (login complete)
      v
(4) CAPTURE .bd.identity -> Secrets Manager blackdiamond/49f/session -> the job proceeds.
      No manual reseed, ever. Andrew is pulled in ONLY for the OTP value, and ONLY when BD forces MFA.
```

## The CV / vision rationale (why vision, not selectors)
The old scrape died on a **modal/backdrop intercepting selector clicks** (SCRAPER_FAILURE_ANALYSIS.md) -- brittle CSS selectors break on UI changes/modals/MFA variants. A **vision model that SEES the rendered screen** + decides the action is robust to all of that (it's the "computer-use agent" pattern applied to the BD login). Kimi (vision-capable) reads the screenshot, classifies the state (login form / modal / OTP-challenge / logged-in), and drives the next step. This is what makes it "engage as needed" rather than a fixed script.

## Reuse (not from scratch)
- **`data/cot/scripts/bronze/cot_bd_session_fetch.py`** -- the EXISTING Playwright BD-login (OIDC flow, captures `.bd.identity` -> SM, has `FAILED_MFA_REQUIRED` detection). This is the base; add the vision-perception loop + the OTP-relay branch where it currently just fails on MFA.
- **ASTN_WSJ&FT residential proxy** -- creds in SM (astn/brightdata/residential-proxy); the proven "real-egress" pattern that defeated FT's datacenter-IP block. The auto-login rides this (also resolves the AWS-IP-anomaly concern on the keepalive).
- **The freshness-probe (`bd-49f-freshness-probe`)** -- already built; it IS component (1) the pre-flight gate (extend it to TRIGGER the refresh, not just alert).
- **OTP-relay precedent** -- the inf/Orion OTP-relay-automation (referenced in ADVI_INFLEC) -- prior art for the relay mechanism.

## Open design decisions (for CTO arch-gate)
1. **The OTP RETURN channel** -- Andrew replies the OTP HOW? Options: (a) two-way SMS (he texts the code back -> a webhook/poll reads it); (b) a one-field internal page / a Secrets-Manager value he sets that the automation polls; (c) the M365/Teams gateway (he replies in Teams -> the automation reads via the m365 MCP). (c) is attractive -- the Teams gateway is live + Andrew's already there.
2. **SMS egress** -- the SNS account is IN SANDBOX (no SMS origination identity) -> SMS to Andrew won't deliver today. Needs SNS SMS PRODUCTION ACCESS (account-owner, AWS request) OR a verified sandbox number. (Tracked as 0.6.0's non-blocking follow-up; this makes it blocking for the OTP-relay leg.) Email is the proven channel -- the OTP-request could go email-first if SMS lags.
3. **Where it RUNS** -- the CV-login needs a browser (Playwright + Chromium) + the vision model + the residential proxy. A Lambda (container image w/ Chromium) vs a small EC2 (the ASTN-box pattern). The residential-proxy egress is the constraint, not the compute.
4. **Vision model access** -- Kimi (Moonshot) API key/endpoint provisioning; or an alternative vision-capable model already wired. CTO confirms the available vision capability.
5. **Device-trust cookie** -- capture `bd_DeviceRegistration` on a successful login + inject it on subsequent logins to try to SKIP the OTP (the deferred device-trust probe -- it folds in here as "minimize how often Andrew is OTP-pinged").

## Lanes
- **CTO** -- arch-gate the 4 components + the 5 open decisions (esp. OTP-return-channel + SMS-production-access + the vision capability).
- **AE** -- build (extend cot_bd_session_fetch with the vision loop + OTP-relay branch; the residential-proxy egress; the freshness-gate trigger; the SM capture). 0.6.0 (the BD-runner owner) or 0.7.0 (ASTN/CV pattern owner).
- **CVO** -- drive + verify (the auto-login refreshes a live cookie end-to-end; the OTP-relay reaches Andrew + completes; firm-sep; no regression to the runners).
- **Andrew** -- the OTP value when BD forces MFA (the ONLY manual step, minimized by device-trust); the SNS-SMS-production-access request (account-owner); confirm the OTP-return channel.

## Interim coexistence
The manual-cookie interim STAYS the bridge until this lands (tonight's reseed still manual). This durable layer REPLACES the manual reseed; the keepalive + freshness-alarms + runners are all REUSED unchanged (this just adds the auto-refresh in front of them).
