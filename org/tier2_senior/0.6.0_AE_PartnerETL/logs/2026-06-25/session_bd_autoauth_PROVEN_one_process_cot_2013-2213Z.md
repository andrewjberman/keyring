# Session Log — 0.6.0_AE_PartnerETL — BD durable auto-auth PROVEN + one-process refactor + cot unfreeze

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE, DEPLOY, DIAGNOSE
**Date:** 2026-06-25 (~2013-2213Z)
**Project:** ADVI_BDAPIMIG.P1 (durable auto-auth) + cot-parallel
**Driver:** 3.0.0_SA_CVO (BD lane verifier). Andrew-direct throughout. COO org-law. 0.7.0 box/gateway. CTO arch.

## Summary

The durable BD-49F auto-auth went from "login core proven" to **fully PROVEN end-to-end AND solved tonight's
live cookie incident** in one run -- no manual paste. Then, per Andrew-direct, refactored the script into the
**ONE canonical firm-parameterized process** (BD_FIRM_ID selects partner; COO made it org-law). Grounded that
**Cottonwood is down on the same MFA wall** (invisibly frozen since 06-23) and staged its unfreeze as a
firm-config of the same script. The durable OTP gateway (0.7.0) went live; my adapter already matches it.
Closed with the cot cookie-capture fix (CV-classify tune + complete-the-sign-in + device-trust), cot re-fire
in flight.

## What happened (the arc)

1. **49F durable auto-login PROVEN + tonight's reseed SOLVED LIVE.** The cookie died ~18:00Z; COO/Andrew thought
   it was reseeded -- I LIVE-grounded it was NOT (session 13:31Z, keepalive mint=401), caught a false "done."
   Then drove the auto-login to a COMPLETING run: native-IP egress -> Kimi-CV login -> MFA two-step send-code ->
   CVO relayed the gateway-grabbed OTP -> entered -> LOGGED_IN -> captured fresh .bd.identity to
   blackdiamond/49f/session. VERIFIED: session LastChanged 21:13:26Z, bd-49f-keepalive {"ok":true,"status":204}.
   Green-lit COO; 22:30Z fees-run + 02:00Z runner SAFE.
2. **cot root-caused (Andrew "verify COT" / both-firms).** Live-grounded: cot has the recovery trigger
   (cot-bd-session-trigger daily 02:00) but ZERO detection layer (no keepalive/freshness/alarms). Read the cot
   06-25 02:00 SSM result: Status=Failed, `ERROR: FAILED_MFA_REQUIRED` -- cot hit the SAME MFA wall as 49F, its
   exporter cot_bd_session_fetch.py has no OTP handling -> cot session frozen 06-23, invisibly (no alarm).
3. **ONE-PROCESS refactor (Andrew-direct: "one process, alt creds per partner").** Made
   bd_49f_auto_login.js firm-parameterized: BD_FIRM_ID derives blackdiamond/<firm>/{credentials,session,
   otp-relay} + a hard firm-sep guard (aborts cross-firm, NEVER#1). Removed the DEAD app-reg 'graph' adapter
   (CTO/Andrew killed app-reg). COO propagated as org-law (I own the one script; others support).
4. **Durable OTP gateway LIVE (0.7.0's /otp/fetch).** Ground-verified myself: /otp/health no-bearer=401,
   with-bearer={"ok":true}. Inline-gateway OTP read = the canonical steady-state; my adapter matches model-A
   exactly. Relay = retiring bridge.
5. **cot unfreeze staged + cookie-capture fix.** Created blackdiamond/cot/otp-relay; 0.7.0 did cot-box IAM
   (firm-sep verified). First cot run AUTHENTICATED (BD_FIRM_ID=cot worked) but HUNG: Kimi misread cot's loaded
   dashboard ("Please Wait/186 Items Ready") as MFA_OTP -> re-read consumed relay -> SSM TimedOut. Shipped the
   fix per Andrew's steer: tuned classifyState (CV authoritative) + complete-the-sign-in (land + device-trust)
   + otpEntered guard + cookie-presence anti-hang seatbelt.

## Deployment Sequence + Verification (AE)

All commits to infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js, deployed to
s3://opal-313476888478-lambda-artifacts/ec2/bd-49f-auto-login/. See commit messages for per-change detail:
160e848c4 (proxy-encoding, superseded), 7df94867e (native-IP form-fill + pickSel await-bug), a15c1519d
(MFA masked-dest dump), 7675fe83f (MFA two-step send-code), 2ef136abf (debug-shots->S3 + 5min OTP window),
7e517db99 (device-trust + pinned regex), 1e923c38d (ROE-mask shots), 7d45b85a1 (gateway OTP adapter seam),
d44ef61d5 (relay OTP adapter = tonight's bridge), 90023027a (MFA input/checkbox dump), **157a6fbb0 (ONE
firm-parameterized process: BD_FIRM_ID + firm-sep guard; removed dead app-reg)**, 25fb902e9 (cookie-presence
+ otpEntered guard), **a77d58e45 (complete-the-sign-in + tuned Kimi classify + seatbelt)**. Plus brief
fd450db6b (cot-parallel scope).

Live verifications (grounded, not self-report):
- 49F reseed: `session LastChanged 21:13:26Z` + `bd-49f-keepalive -> {"ok":true,"status":204}` (was 401).
- Durable gateway: `curl /otp/health` no-bearer=401, with-bearer={"ok":true} HTTP 200.
- cot root cause: SSM get-command-invocation (cot 06-25 02:00) = Failed/`FAILED_MFA_REQUIRED`.
- cot box: i-0643a5bee8a8feabf STOPPED (no in-flight export) before 0.7.0's deploy.

Secrets created: blackdiamond/49f/otp-relay, blackdiamond/cot/otp-relay (both transient, firm-bound).

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp-which | "who owns data/cot/scripts/bronze/..." ownership lookup | routed to comp-grep (no rich tool fits); confirmed 0.6.2 prior author |
| comp-freshness | cot served-freshness attempt | NO cot rows (cot not in registry -> rail-checked s3 ls instead) |
| rail-checked aws | SM describe/list, lambda invoke (keepalive mint), cloudwatch, ssm get-command, ec2 describe, s3 cp, curl /otp/health | all live ground-truth for the verifications above |

No comp-graph traversal: the durable auto-auth is a new EC2-box auth script (not a pipeline/gold/route graph
node), so Rule-20/21 graph checks don't apply; verification was live AWS/SSM ground-truth + CVO's firm-sep
certs (same rationale as the prior window's log).

## Current State

- **ONE canonical script** `infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js` @ a77d58e45 (deployed to S3):
  Playwright+Chromium (native AWS IP, no proxy) -> Kimi-CV perceive-act (classifyState/locate) -> two-step MFA
  send-code -> getOtpCode (adapter: gateway=canonical inline OPLMCP read / relay=bridge / teams=unbuilt SMS
  fallback) -> Remember-My-Device + Continue -> land on dashboard -> capture .bd.identity + bd_DeviceRegistration
  -> smPut blackdiamond/<firm>/session. Firm-parameterized by **BD_FIRM_ID** (49f|cot) with a hard firm-sep guard.
- **49F: HEALTHY** -- session 21:13:26Z, mints 204. Device-trust was ABSENT on that run (pre-fix); the next 49F
  refresh on a77d58e45 should capture it.
- **Durable OTP gateway**: https://mcp.opalinvest.dev/otp/fetch (0.7.0, model-A static bearer
  blackdiamond/<firm>/otp-gateway-token). LIVE + verified. Flip BD_OTP_ADAPTER=gateway to retire the relay.
- **cot: FROZEN since 06-23, unfreeze IN FLIGHT** -- cot-box i-0643a5bee8a8feabf has the canonical script at
  /opt/bd-cot-auto-login/ (BD_FIRM_ID=cot env, cot IAM firm-sep verified ledger e10870ed6). CVO re-firing the
  cot completing-run ONCE on a77d58e45 (re-pull the fixed script first). cot OTP confirmed lands in the same
  mailbox (Andrew@opalinvest.com/noreply@bdreporting.com); no firm-picker blocker.

## Next Steps

- **[3.0.0_SA_CVO]** re-fire the cot completing-run on a77d58e45 (grab fresh cot OTP via gateway) -> writes
  blackdiamond/cot/session. Verify firm-separated.
- **[0.6.0_AE_PartnerETL]** verify cot mint + device-trust=present the instant cot/session lands; then BUILD
  the cot DETECTION LAYER (cot-keepalive + cot-freshness-probe + opal-bd-cot-cookie-alerts SNS -- the
  firm-parameterized twin of 49F's, closing the invisible-failure gap). Then coordinate the 49F+cot flip to
  BD_OTP_ADAPTER=gateway (retire the relay bridge) once box-client JWTs onboard (0.5.0).
- **[0.7.0_AE_CloudOps]** gateway liveness probe (alert if Andrew's delegated refresh lapses); cot box-client
  bearer (blackdiamond/cot/otp-gateway-token) for the cot gateway flip.

## Blockers

None mine. cot unfreeze is gated only on CVO's single re-fire (in flight) + her OTP-grab -- not blocked, in motion.

## MCP traffic

~30+ messages this window (tight CVO/COO/0.7.0/Andrew iteration). Significant: COO false-"done" status-check ->
my LIVE-grounded NOT-DONE RAVC; Andrew-direct one-process + canonical-architecture lock; COO org-law (singular
BD-auth, I own it); 0.7.0 durable-gateway-golive; the cot cookie-capture fix chain (5 crossed CVO refinements
-> one complete ship a77d58e45). All RAVC loops to COO/CVO closed or in-flight-verify.
