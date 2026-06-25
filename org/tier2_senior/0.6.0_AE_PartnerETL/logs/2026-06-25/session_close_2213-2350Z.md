# Session Close — 0.6.0_AE_PartnerETL — cot reseed + interchangeability/perms verify + device-trust evidence

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE, COORDINATE
**Date:** 2026-06-25 (~2213-2350Z)
**Project:** ADVI_BDAPIMIG.P1 (durable auto-auth) + cot-parallel
**Driver:** 3.0.0_SA_CVO (BD verifier). Andrew-direct. CTO wind-down sweep. 0.7.0 box/IAM.

## Summary

Closing window of the BD durable-auto-auth day. Verified (not asserted) the one canonical script is
firm-interchangeable AND correctly firm-permissioned -- which surfaced + fixed a real S3 script-pull
firm-sep gap. **Cottonwood RESEEDED** through the identical script (BD_FIRM_ID=cot) -> cot's 2-day silent
freeze is OVER. Then ran the device-trust loose end to a grounded, evidence-based root cause (the
"Remember My Device" checkbox never actually toggled) and shipped the targeting fix. Wind-down: pause-safe,
nothing stranded, one near-term gap flagged.

## What happened

1. **Interchangeability + permissions verification (Andrew Q: "can it be used for 49 or cot + has the perms").**
   Grounded both box roles LIVE: bd-49f-auto-login-role = blackdiamond/49f/* + astn/kimi ONLY (Put on
   49f/session); cot-exporter-ec2-role = blackdiamond/cot/* + astn/kimi + explicit cross-firm Deny
   (opal-data-bd/inf). Each firm can do its OWN, neither can touch the other = firm-sep holds at IAM. **Found a
   GAP:** the canonical script lived ONLY at S3 ec2/bd-49f-auto-login/, but the cot role can read ONLY
   ec2/bd-cot-auto-login/* -> the cot box couldn't self-pull it (0.7.0's hand-deploy had masked it). **Fixed:**
   dual-prefix deploy (script to BOTH firm prefixes; each role pulls its own). Also firm-derived the last 49f
   literal (relay default, a1a49d27b) + the debug-shot S3 key (a69875e97).
2. **cot RESEEDED + RAVC'd.** CVO's run on the complete-fix + t3.large landed cot clean (step5 LOGGED_IN ->
   blackdiamond/cot/session; otpEntered guard fired). I independently verified cot/session fresh + it mints
   (GET token 200). cot UNFROZEN. (t3.small had failed purely on SPEED -- raced the SSM/OTP timeout.)
3. **Device-trust root-caused with EVIDENCE (Andrew: evidence not speculation).** Shipped evidence
   instrumentation (986b533ea: post-login cookie-NAMES dump + widened device-cookie capture + checkbox
   read-back). CVO's diagnostic run (BD_DEBUG_SHOTS=1) was conclusive: checkbox read-back checked=FALSE +
   screenshot shows the box EMPTY + post-login cookie list has NO device/trust cookie at all. ROOT CAUSE: the
   "Remember My Device" control is an unlabeled custom-styled <input type=checkbox> (no id/name/for-binding)
   that page.check() couldn't toggle. **Fix (28c929c52):** 3 strategies -- (a) click the label TEXT, (b)
   force-check the bare input, (c) Kimi vision-locate -- each VERIFIED by isChecked() read-back, stop when
   truly checked; the cookie-names dump then confirms whether BD sets the device cookie.
4. **Wind-down confirm (CTO sweep).** All committed+pushed, git clean, no half-applied box state (boxes pull
   from S3 at run-time). Both firms reseeded fresh tonight. Flagged the one near-term gap (below).

## Deployment Sequence + Verification (AE)

Commits to infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js (per-change detail in commit messages):
a69875e97 (firm-parameterize debug-shot S3 key), a1a49d27b (firm-derive relay default = fully firm-neutral),
986b533ea (device-trust evidence: cookie-names dump + widened capture + checkbox read-back), 28c929c52
(device-trust checkbox 3-strategy targeting). Each deployed to BOTH S3 prefixes
(ec2/bd-49f-auto-login/ + ec2/bd-cot-auto-login/).

Live verifications (grounded):
- IAM: aws iam get-role-policy on bd-49f-auto-login-role + cot-exporter-ec2-role -> firm-separated, confirmed.
- cot reseed: blackdiamond/cot/session LastChanged 22:53Z then 23:31Z (CVO's verification run); fresh + mints.
- 49F still healthy: 49f/session 21:13:26Z (this-session reseed), keepalive 204.
- git status CLEAN (my lane); 28c929c52 pushed.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| rail-checked aws iam | dump both box-role policies (comp-iam analyzes Lambda boto3, not EC2-box CLI roles) | firm-sep verified live |
| rail-checked aws (sm/s3/ec2) | session-freshness RAVC, dual-prefix deploy + verify, box-state ground | all PASS |
| comp-iam / comp-which | attempted for the role question | comp-iam is Lambda-source-oriented; routed to the rail-checked iam dump |

No comp-graph traversal: EC2-box auth script (not a pipeline/gold/route node) -- same rationale as the prior
two logs; verification is live AWS/IAM ground-truth + CVO's firm-sep certs.

## Current State (handoff -- zero prior context)

- **ONE canonical firm-parameterized script** `infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js` @
  **28c929c52**, deployed to BOTH S3 prefixes (ec2/bd-49f-auto-login/ + ec2/bd-cot-auto-login/). BD_FIRM_ID
  (49f|cot) derives blackdiamond/<firm>/{credentials,session,otp-relay} + hard firm-sep guard. Flow: Playwright
  native-IP -> Kimi-CV -> two-step MFA send-code -> getOtpCode (relay=bridge / gateway=durable canonical /
  teams=unbuilt) -> Remember-My-Device (3-strategy, read-back-verified) + Continue -> land on dashboard ->
  capture .bd.identity + any device cookie -> smPut blackdiamond/<firm>/session.
- **Both firms reseeded FRESH tonight:** 49f/session 21:13Z (alive, keepalive-covered), cot/session 23:31Z
  (fresh, mints). cot data UNFROZEN.
- **Durable OTP gateway** https://mcp.opalinvest.dev/otp/fetch LIVE (0.7.0); flip BD_OTP_ADAPTER=gateway to
  retire the relay (pending 0.5.0 box-client JWTs).
- **device-trust**: still ABSENT pre-28c929c52 (evidence: BD set no device cookie because the box never
  toggled). 28c929c52 = the targeting fix; UNVERIFIED until the next run's checked=true + cookie-names evidence.

## Next Steps

- **[0.6.0_AE_PartnerETL]** (#1 next-session, the re-freeze guard) BUILD the cot DETECTION LAYER (cot-keepalive
  + cot-freshness-probe + opal-bd-cot-cookie-alerts SNS, firm-parameterized twin of 49F's) AND wire cot's
  refresh to the canonical auto-login -- cot's 02:00 trigger still runs the OLD MFA-failing
  cot_bd_session_fetch.py, so cot will SILENTLY re-freeze in ~1d without this. Then read the device-trust
  evidence (28c929c52 verification run) + flip 49F+cot to BD_OTP_ADAPTER=gateway.
- **[3.0.0_SA_CVO]** the single cot verification run on 28c929c52 (checked=true + device-cookie evidence).
- **[0.7.0_AE_CloudOps]** bake dual-prefix (or firm-neutral) into the AE deploy convention; set BD_FIRM_ID
  explicitly in both boxes' secret-ids.env; cot box-client gateway bearer.

## Blockers

None. Pause-safe; the cot re-freeze risk is ~1d out and is the documented #1 next-session priority, not a
tonight-must (cot's fresh cookie is good ~20-24h).

## MCP traffic

~12 messages this window. Significant: Andrew "one process + perms" verification -> my found+fixed S3 firm-sep
gap; CVO cot-RESEEDED + device-trust-evidence root-cause -> my fixes; CTO wind-down sweep -> my pause-safe
confirm + cot re-freeze flag. All RAVC to CVO/CTO closed or event-driven-pending.
