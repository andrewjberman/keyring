# CVO investigation (Andrew-direct 2026-07-06): 49F + Cottonwood Black Diamond auth — full OTP fires on EVERY daily mint, and it is redundant

**archetype:** DIAGNOSE
**serial:** 3.0.0_SA_CVO | **date:** 2026-07-06 ~1330Z | **requested_by:** Andrew (sovereign, in-session)
**grounding:** live AWS (SSM run logs, Secrets Manager metadata, EventBridge rules, CloudWatch KeepaliveOK) + source (bd-49f/cot session-trigger + keepalive Lambdas, run-bd-auto-login.sh). Rule-22: mechanism SOURCE+LIVE-confirmed, not inferred.

## Question
Andrew: 49F + Cottonwood ingest do "a full sign-in with OTP confirmation every single time." Can we reuse a long-lived cookie for the REST API and only full-OTP-login when the cookie is stale? Investigate the BD auth protocol + feasibility.

## Answer: YES it OTPs every daily mint (both firms, live-confirmed), and it is REDUNDANT — the fix uses primitives that already exist.

### 1. Current architecture (source-grounded)
Both firms already run the REST-with-cookie path (NOT browser-scrape at steady state): a single `.bd.identity` cookie in Secrets Manager (`blackdiamond/{49f,cot}/session`) auths the BD DataMining REST API (`GET /datamining/auth/token` -> access_token). Three moving parts:
- **Daily mint** (`bd-49f-session-daily` cron(0 0 * * ?) ENABLED; `cot-bd-session-daily` cron(0 2 * * ?) ENABLED; + `bd-49f-fees-session-daily` 22:20 wkdays ENABLED) -> starts the auto-login EC2 box -> `run-bd-auto-login.sh` -> headless Playwright login -> writes a fresh `.bd.identity` to SM. **Fires UNCONDITIONALLY.**
- **Keepalive** (`bd-49f-keepalive-sched` / `bd-cot-keepalive-sched` rate(15 min) ENABLED) -> `GET /auth/keepalive` -> 204, extends the EXISTING cookie in place, no login, to BD's absolute server cap.
- **`session-check` primitive** — EXISTS in both session-trigger Lambdas (probe `/auth/token` -> {session_live}) but is **NOT wired** as a pre-gate on the mint.

### 2. The mint runs a FULL OTP every time (live SSM run logs, today)
49F `opal-bd-49f-session-fetch` 2026-07-06T00:00Z (cmd 5e984147, i-0fa1846f04ed7e337, Success) and COT `opal-cot-bd-session-fetch` 2026-07-06T02:00Z (cmd 57748709, i-0643a5bee8a8feabf, Success) BOTH show:
```
device-trust: bd_DeviceRegistration injected (OTP-skip attempt)
step 2: state=MFA_OTP        <- BD PRESENTS THE OTP SCREEN ANYWAY
MFA/OTP screen -> OTP adapter
OTP delivery: Send-code clicked (DOM)
... OK: fresh .bd.identity written to SM
```
=> device-trust is CAPTURED + injected, but **BD does NOT honor it** — the MFA/OTP screen appears every day and the OTP is procured via the gateway/Kimi adapter. It has been INVISIBLE because the OTP is auto-solved (zero-Andrew), not because it isn't happening. Mints ran Success daily through the holiday (07-04/05/06 confirmed).

### 3. The mint is REDUNDANT (CloudWatch KeepaliveOK, 14-day)
`BD/49F/Auth` + `BD/COT/Auth` KeepaliveOK (1=alive at the 15-min check), daily minimum:
```
day     49F(min, ok/total)   COT(min, ok/total)
06-25   0  23/42  (rollout)   -
06-26   1  96/96              0  47/49  (rollout)
06-27   1  96/96              1  96/96
06-28   0  42/83  (churn)     0  42/83  (churn)
06-29   0  39/96  (churn)     0  88/96  (churn)
06-30   1  96/96              1  96/96
07-01   1  96/96              1  96/96
07-02   1  96/96              1  96/96
07-03   1  96/96              1  96/96
07-04   1  96/96              1  96/96
07-05   1  96/96              1  96/96
07-06   1  56/56 (partial)    1  55/55 (partial)
```
Since **06-30, both firms: KeepaliveOK=1 at ALL 96 daily checks** — the cookie is alive at every check INCLUDING the reading right before each mint. The early 0s (06-25..06-29) coincide exactly with the ADVI_BDAPIMIG P1 "bd re-auth chain" build landing 06-29 (rollout churn, now stable). **=> The daily OTP mint re-authenticates a session that was still perfectly alive, 7 days running.**

## Two levers (both use existing infrastructure)
**Lever A (PRIMARY, small): gate the daily mint on `session-check`.** Before spinning the login box + OTP, probe the current cookie; if live -> NO-OP (skip mint, no browser, no OTP); only mint if the check fails. The data proves this would have skipped ALL 7 recent daily mints -> OTP -> ~zero. Primitive already written; it just isn't the pre-gate.
- **Measurable unknown that sizes the win:** BD's absolute session cap under keepalive. Floor is proven (>=24h; survives mint-to-mint). Ceiling unmeasured (mint resets the clock). If cap >> 24h -> OTP -> literally zero; if cap ~24h -> OTP -> once per ~cap. Cheap experiment: disable the mint cron a few days, watch KeepaliveOK flip to 0 = the cap; mint stays as the fallback.

**Lever B (SECONDARY): make BD honor device-trust.** Currently broken (MFA_OTP appears despite injection) — likely headless-fingerprint / IP / device-token semantics. Fixes the residual genuine-remint case so even necessary mints skip OTP. This is what the ADVI_BDAPIMIG PRD §7 device-trust probe was meant to settle; the run logs now show it is not landing.

## Feasibility verdict
FULLY FEASIBLE; mostly already built. Lever A is the high-leverage, low-risk change and directly delivers Andrew's ask ("reuse the long-lived cookie, only OTP when stale"). This is squarely **ADVI_BDAPIMIG P1b** ("Cookie/login-box durability — mint/refresh/rotate", 0.7.0_AE_CloudOps~A).

## Routing
- **CTO (1.0.0_SA_CTO):** architecture — (a) ratify the `session-check`-as-mint-pre-gate design (fail-safe: check-fails -> mint, so no availability regression), (b) the cap-measurement experiment, (c) own/scope the Lever-B device-trust investigation. Ties to ADVI_BDAPIMIG PRD §7.
- **COO (2.0.0_SA_COO):** dispatch to the ADVI_BDAPIMIG P1b AE lane.
- **CVO stance:** verifier-not-fixer — I investigated + grounded; I do not build. Available to verify the pre-gate against live once built (session-check-skips-on-live-cookie exercised, OTP-count-drops).

-- 3.0.0_SA_CVO
