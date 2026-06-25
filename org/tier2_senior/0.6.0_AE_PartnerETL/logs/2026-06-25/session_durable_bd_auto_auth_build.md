# Session Log — 0.6.0_AE_PartnerETL — durable BD auto-auth build (CV-login + Graph OTP)

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE, DEPLOY
**Date:** 2026-06-25 (~1925–2013Z)
**Project:** ADVI_BDAPIMIG.P1 (durable auto-auth extension)
**Driver:** 3.0.0_SA_CVO (BD lane). Andrew-direct GO. CTO arch-gate. 0.7.0 box. 0.5.0 m365.

## Summary

Andrew-direct GO (via CVO) to build the DURABLE BD-49F auto-RE-AUTHENTICATION — the permanent
kill for the manual cookie reseed (the dead-cookie caught in today's live-health verify; measured
absolute SSO cap is SHORT ~hours, so only a fresh LOGIN resets the clock). Launched, got all
rulings, authored the full auto-login (box-Node), deployed to the live sibling box, and iterated
2 live-smoke fixes with CVO — now one re-fire from the login form + the MFA-mailbox grounding.

## Rulings obtained (the gating decisions, all resolved this window)
- **CTO:** vision = Kimi-VL (already wired, `astn/kimi/api-key`; reuse `harvest_ft_session.js`
  grid-localization); compute = co-opt the ASTN CV stack (EC2 — a Lambda can't hold the OTP wait);
  runtime-bridge = **Option A** (box-side app-only Graph `Mail.Read` + Exchange ApplicationAccessPolicy
  single-mailbox).
- **Andrew:** Path A (auto-read the OTP email; never pinged) + the creds in SM (`blackdiamond/49f/credentials`),
  env-var-linked secret-ID, NO literals.
- **CVO:** locked the 5-point email-read ROE; ruled box-Node core (not idle); caught 2 live bugs (below).
- **0.5.0:** the m365 gateway is Andrew's OWN identity (not a bot) + the BD OTP is NOT in Andrew's mailbox
  → mailbox is TBD (tonight's reseed/the smoke grounds it).
- **0.7.0:** sibling box LIVE `i-0fa1846f04ed7e337` (node+chromium+aws-CLI, IAM cert-pass, secret-id pointers baked).

## What I built (see commit messages 2375d8795 → 35fc89587)
`infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js` (+ `run-bd-auto-login.sh`, `package.json`):
- **L1 core:** Playwright+Chromium on the always-on BrightData residential proxy → Kimi-VL perceive-act
  loop (`classifyState` login/mfa_otp/modal/logged_in + `locate` grid-localize, reusing the harvest_ft
  `kimiVision` pattern) → DOM-first fill + vision fallback → `.bd.identity`+`bd_DeviceRegistration` capture.
- **L2 OTP-adapter (Option A):** `getOtpCode('graph')` = app-only Graph token → sender-pinned +
  time-windowed (loginStart) + top-1 + regex-in-memory + read-only; config-driven (mailbox/sender/app-reg).
- **L3 device-trust inject:** inject a prior `bd_DeviceRegistration` pre-login to skip the OTP screen.
- **SM-direct:** all secrets read at runtime via `BD_*_SECRET_ID` env (aws-CLI); session written straight
  to SM; **zero credential/OTP/cookie literals or logs** (self-grep verified).
- **L5 orchestrator (thin):** sources secret-id pointers, sets `BD_APP_URL`, runs node.

## Live-smoke iteration with CVO (on `i-0fa1846f04ed7e337`)
- **Validated:** box, node+npm, `playwright install chromium` rc=0, all 3 artifacts pulled from S3, the
  orchestrator launched, proxy loaded.
- **Fix 1 (20fa8e7e7):** the proxy secret is a JSON object `{host,port,...}`, not colon-delim → `JSON.parse`.
- **Fix 2 (35fc89587):** BrightData MITM-intercepts TLS → `ignoreHTTPSErrors:true` (scoped to the context).
- Both committed + re-deployed to S3; CVO re-fires. No creds submitted yet (died at nav) → mailbox still open.

## Current State
- Script (L1-L3 + SM-direct + 2 fixes) deployed at `s3://opal-313476888478-lambda-artifacts/ec2/bd-49f-auto-login/`.
- Box `i-0fa1846f04ed7e337` ready (IAM/env/deps in place); `BD_APP_URL=https://bd3.bdreporting.com`.
- The next re-fire reaches the login form → fills SM creds → fires the MFA email = grounds the mailbox.
- The 49F `.bd.identity` cookie is DEAD (token→200-empty, keepalive→401); CVO+Andrew reseed manual tonight; this auto-auth is the going-forward kill.

## Next Steps
- **[3.0.0_SA_CVO]** re-fire the SSM smoke; locate where the MFA OTP lands → the mailbox/sender.
- **[0.6.0_AE_PartnerETL]** wire `BD_OTP_MAILBOX`/`SENDER` (post-mailbox-grounding) + `BD_GRAPH_SECRET_ID`
  (post app-reg consent) into the box env → full unattended auto-reseed; then **L4** (freshness-probe →
  trigger-on-401, GATED to avoid a failed-login storm while the cookie's dead); tune the Kimi-VL prompts
  off the box log if a state misread.
- **[Andrew]** the Graph app-reg consent (CTO surfaces); observe the MFA channel in tonight's reseed.

## Blockers
None mine. The full end-to-end is gated on the OTP mailbox (CVO's smoke/the reseed) + the app-reg consent (Andrew) — both routed, both imminent.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| (none — build + multi-agent coordination) | this window is JS authoring + live-smoke iteration + RAVC; no comp-graph traversal | n/a |
| rail-checked aws/grep | SM-secret-shape verify (proxy bug), S3 deploy, a .js ROE self-grep | markers logged |

No comp-graph tools: the durable auto-auth is a new EC2-box auth script (not a pipeline/gold/route
graph node), so the Rule-20/21 graph checks don't apply; the relevant verification was the live
SSM smoke on the box + CVO's Rule-22 secret-shape ground-truthing.
