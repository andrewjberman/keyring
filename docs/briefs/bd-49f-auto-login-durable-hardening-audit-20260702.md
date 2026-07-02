# bd-49f-auto-login re-mint chain — DURABLE-HARDENING AUDIT (findings list)

**Author:** 0.6.2_AE_PartnerETL | **Date:** 2026-07-02 | **For:** COO/CTO greenlight
**Scope:** hunt robustness gaps in `infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js` + `run-bd-auto-login.sh`
BEYOND the 2 already fixed today (0.7.0~A's flaky-Kimi UNKNOWN-loop = my 5d9cc4649 Kimi-guard; the perf-converter class).
**Grounding (Rule 22a):** each finding tagged SOURCE-GROUNDED (cited file:line) or HYPOTHESIS (needs a grounding probe). No fix built — greenlight-gated. Coordinate 0.7.0~A (box-owner) + 0.6.0 (build-lead).

---

## HIGH

### F1 — kimiVision has NO request timeout -> a hung Kimi connection HANGS the login indefinitely (SOURCE-GROUNDED)
`kimiVision()` (bd_49f_auto_login.js:81-87) does `https.request(...)` with NO `req.setTimeout` and no per-classify timeout in the step loop. A Kimi API that accepts the connection but never responds (hang, not error) leaves the `await` at :103 pending FOREVER -> the whole attempt hangs, MAX_STEPS never advances, the CTO-B 3-attempt retry NEVER fires (it only retries on a failed ATTEMPT, and a hang isn't a failure). **My 5d9cc4649 Kimi-guard covers THROW + EMPTY but NOT a hang** (a hang never throws). So a Kimi outage that manifests as a hung socket = a stuck box until the SSM executionTimeout (or forever if none). FIX: add `req.setTimeout(30000, () => req.destroy(new Error('kimi timeout')))` in kimiVision -> the reject flows into my guard's catch -> DOM-fallback recovers. This CLOSES the last Kimi-outage failure mode (the guard + the timeout together = complete). Priority HIGH — it's the residual of today's exact incident class.

### F2 — smPut (session write) failure returns rc=0 (FALSE SUCCESS) -> silent cookie-staleness (SOURCE-GROUNDED)
Capture block (:470-481): `if (!bd) { rc=1 } else { smPut(sessionId, {...fresh cookie...}); log('OK') }`. `rc` is already 0 (:347). **smPut is NOT in a try/catch.** If `PutSecretValue` fails (IAM hiccup, throttle, transient SM error), smPut THROWS -> caught by the outer catch (:483) which logs ERROR but does NOT reset rc -> the function returns rc=0 = SUCCESS, while the fresh `.bd.identity` was NEVER persisted to SM. Result: the login "succeeded" but the cookie isn't written -> the next run still reads the STALE cookie -> silent staleness (the exact freeze class the whole box exists to prevent), with a misleading rc=0. FIX: wrap smPut in try/catch; on failure `log('FATAL: session PutSecretValue failed -- cookie NOT persisted'); rc=1`. The persist IS the deliverable — a login that doesn't write the cookie is a FAILURE, not a success. Priority HIGH.

## MEDIUM

### F3 — OTP permanent-config vs transient failures are not distinguished -> a config error burns 3 attempts + backoff (SOURCE-GROUNDED)
`getOtpCode()` throws for BOTH permanent config errors (`OTP_GATEWAY_UNCONFIGURED` :175, `FAILED_MFA_REQUIRED_NO_OTP_ADAPTER` :210) AND transient (`OTP_GATEWAY_NO_CODE` :200 after 30x10s=5min polling). The main outer retry (:249-260) retries ALL of them equally -> a PERMANENT misconfig wastes 3 full attempts (each 5min gateway-poll + exponential backoff = ~15min+) before the LOUD rc=1. FIX: tag config/unconfigured throws as NON-RETRYABLE -> main fails FAST (rc=1 immediately, distinct log) on a config error; retry only the transient no-code-in-window. Saves ~15min + gives a clearer signal (misconfig != vendor-slow-OTP).

### F4 — native-IP bot-block is not detected/distinguished -> the proxy-revert contingency has no trigger (SOURCE-GROUNDED)
BrightData proxy was DROPPED 2026-06-25 (native AWS IP; run-bd-auto-login.sh note: re-add BD_PROXY_SECRET_ID "ONLY if a bot-detection IP-block proves native-IP cannot reach"). But there is NO bot-block DETECTION: if Schwab starts blocking the native AWS IP (402/robots/bot-challenge page — the earlier "bd3 402 robots refusal" class, :276), classifyState returns UNKNOWN -> UNKNOWN-loop -> generic rc=1. The Kimi-guard's DOM-fallback won't help (a bot-page isn't LOGIN/MFA/dashboard). So a bot-block is INDISTINGUISHABLE from other rc=1s -> the human-gated proxy-revert contingency is never SIGNALLED. FIX: add a bot-block classifier (detect 402 / "robots" / bot-challenge markers in classifyByDom or a URL/status check) -> a DISTINCT `BOT_BLOCK` state + alarm -> triggers the proxy-revert runbook. Turns a silent stuck-box into an actionable "revert to proxy" signal.

### F5 — no DIRECT alarm on the auto-login rc=1 exhaustion (HYPOTHESIS — needs grounding)
main (:258) exits rc=1 LOUD on attempt-exhaustion. The DOWNSTREAM alarms (bd-49f-keepalive 401 / authtoken-absence / session-stale) catch the CONSEQUENCE with lag. HYPOTHESIS: there is no alarm directly on the auto-login SSM `opal-bd-49f-session-fetch` rc!=0, so a login failure is only seen via the lagged staleness alarm. NEEDS GROUNDING: check CloudWatch/the SSM invocation for a direct rc!=0 alarm before asserting. IF absent -> FIX: alarm on the SSM command rc (catch the failure at the source, not via downstream lag). Flagging as a hypothesis per Rule 22a.

## LOW

### F6 — device-trust check failure silently degrades to OTP-every-run, no alarm (SOURCE-GROUNDED, alarm-absence a hypothesis)
If all 3 Remember-My-Device strategies fail (:421-438), the code logs `checked=false via=NONE-all-strategies-failed` and STILL clicks Continue (:439) -> the run succeeds but sets no device-trust cookie -> the NEXT run needs a full OTP again (higher OTP burn, Andrew pinged more). The failure is LOGGED but (hypothesis) not ALARMED -> a persistent device-trust regression degrades silently. FIX (if no alarm exists): alarm on repeated Remember-My-Device failure across runs. Low sev (functional, just costlier).

### F7 — captured .bd.identity has no freshness assertion (HYPOTHESIS, likely moot)
The capture writes whatever `.bd.identity` is present (:463,473). HYPOTHESIS: a stale cookie could in theory be persisted. LIKELY MOOT: the browser context is FRESH per attempt (:287) and device-trust injects `bd_DeviceRegistration` NOT `.bd.identity`, so a present `.bd.identity` is this-run-fresh. Flagging as defense-in-depth only (assert the cookie's issue/exp is fresh before persist) — low priority, probably unnecessary.

---

## Summary / recommended order
1. **F1 (kimi timeout)** — closes the last Kimi-outage mode (completes today's guard). Trivial fix, high value.
2. **F2 (smPut guard)** — kills a silent false-success staleness path. Trivial fix, high value.
3. F3 (OTP fail-fast on config), F4 (bot-block classifier+alarm) — medium robustness.
4. F5/F6 alarm-gaps — ground the alarm-absence first, then add if confirmed.
5. F7 — defense-in-depth, likely skip.

F1+F2 are the strongest (real, source-grounded, trivial fixes, high impact). Recommend greenlighting F1+F2 for immediate hardening (they're on the durable go-forward critical path); F3-F6 as a follow-up hardening batch. RAVC COO; coordinate 0.7.0~A (box-owner, executes on-box) + 0.6.0 (build-lead, authored the .js).
