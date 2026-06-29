# 0.6.2_AE_PartnerETL — work log 2026-06-29 (session ~13:46Z->14:2xZ)

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE

## Session: ADVI_BDAPIMIG.P1-DURABLE — port cot's durable self-re-mint auto-login to the 49f box (sole 49f unfreeze path); LEG0->LEG2 complete, 49f UNFROZEN

### Context
Respawn as Cottonwood/49f AE. /watcher armed persistent Monitor (task btopw5h28); registered live. Inbox = COO GO (durable 49f port = SOLE unfreeze path; Andrew lifted the login-automation hold + declined the manual reseed) + CTO arch-gate primer (the shared-mailbox OTP-collision firm-disambiguation = the load-bearing gate). TO ADVI_BDAPIMIG.P1-DURABLE pending. This is the firm-parameterized port of MY OWN cot work (61dc06e5d).

### LEG0 — grounded the live 49f box (NOT asserted) -> surfaced 2 forks the TO/repo missed
- 49f box i-0fa1846f04ed7e337 stopped; started read-only via SSM, read on-box config, restored to stopped.
- gateway-token blackdiamond/49f/otp-gateway-token EXISTS (49f-own). session captured_at 06-25T21:13Z (~4d stale); **bd_device_registration PRESENT-but-EMPTY** (cot had len28) -> device-trust re-inject is a no-op on run1 (fail-safe).
- **On-box secret-ids.env (NOT in S3 -- 0.7.0 baked it on-box, outside rule-12)**: BD_OTP_ADAPTER=**relay** (interim CVO bridge), **NO proxy** ("native AWS IP; Andrew-direct CVO 203246Z"), NO BD_FIRM_ID.
- **FORK 1 (proxy):** on-box=native-IP (Andrew-direct CVO) CONTRADICTS TO LEG1d + EC2_MANIFEST (both say proxy-ON). Halted for a ruling rather than reverse an Andrew-direct CVO call. COO RULED: keep native-IP; revert-trigger = a LEG2 nav/IP-block only.
- **FORK 2 (js deploy-drift, load-bearing):** the arch-critical window_seconds (20b19341f) + retry (65908e4a3) are in the REPO js (e6e5ee2e) but **NOT deployed** -- box js=627e2102 + S3=fb0bbcd2 BOTH `grep -c window_seconds = 0`. So env-only BD_OTP_WINDOW_SECONDS is INERT -> cross-firm OTP collision (NEVER#1) live-possible. LEG1 is NOT env-only; the canonical js MUST deploy. COO+CTO CONFIRMED = hard gate.

### Arch-gate (CTO) — grounded all 3, GATE A GO / GATE B held
- **Q4 (could-dissolve):** ONE shared mailbox -- otp.py:96 `cfg.OTP_MAILBOX`=andrew@opalinvest.com; per-firm bearer authorizes-not-routes. Does NOT dissolve the collision.
- **C1 (server clamp): PROVEN** -- otp.py:105/107 until_dt + :128-131 reject path (rdt>until_dt:continue) + :119 lower-bound $filter; config default 0=inert -> box must run repo js AND set window=120. Both halves.
- **C2 premise corrected:** the 49f LOGIN box is start-on-demand/freshness-triggered (instance.tf:13, main.tf:7), NOT cron(0 2). CTO had conflated it w/ the bd-49f-REST-runner. Shrinks exposure to "a 49f on-demand login inside cot's 02:00 window."
- **GATE A** (off-cycle mechanism proof) = GO. **GATE B** (unattended steady-state) = separate HOLD. CTO 2 blackout holes: (i) cot worst-case OTP span ~15-20min (3x300s poll+backoff) not ~3min; (ii) cot multi-path triggers (cron+keepalive rate15m+freshness-probe) = off-cycle login path. -> blackout disqualified. COO RULED GATE-B = the **gateway-side cross-firm OTP-fetch LOCK**.

### LEG1 — staged in repo (b93bda5a2)
- run-bd-auto-login.sh: **firm-safe device-trust** -- sources $BD_SESSION_SECRET_ID (=blackdiamond/49f/session), NOT cot's ${BD_FIRM_ID:-cot} default which on 49f (no BD_FIRM_ID) resolves to **COT = firm-sep breach**. Fail-safe; self-locating APP_DIR; native-IP.
- secret-ids.env (NEW, under repo->S3 standard): adapter relay->gateway, 49F-own token, BD_OTP_WINDOW_SECONDS=120, BD_MAX_LOGIN_ATTEMPTS=3, relay pointer revert-only, NO proxy.
- instance.tf: CVO proxy-drift fix (finding d85882171). EC2_MANIFEST.json blocked by owned-paths (0.7.0 lane) -> routed to 0.7.0 (committed e37635a2f).

### GATE-B lock contract — designed (09d0883cd)
org/tier2_senior/0.6.2_AE_PartnerETL/designs/bd-otp-cross-firm-lock-contract.md. Key insight: a gateway-only /otp/fetch lock is INSUFFICIENT (collision created box-side at cred-submit) -> lock held ACROSS cred-submit via /otp/acquire -> /otp/fetch[verify-held] -> /otp/release, state gateway-side (single global DDB item, conditional-write, TTL auto-expiry, fail-closed). Box-side wrap thin (my lane); gateway code = 0.7.0/base; CTO arch-gates. COO ACCEPTED, formalizing the lock TO.

### LEG2 — box-pull + off-cycle live test = 49f UNFROZEN (ledger 20260629T1409Z, CLOSED 4/4)
Gates pre-cleared: CTO box-pull GO (140455Z); 0.7.0 49F-blast CLEAN + OTP_BEARER count=2 live-verified (140802Z); comp-iam box role GetSecretValue 49f/*+kimi green.
- L1 git b93bda5a2 + 09d0883cd. L2 S3 push js e6e5ee2e + wrapper + env (md5==repo). L3 box bake: SSM md5 of /opt == committed (js e6e5ee2e, replaced 627e2102). L4 off-cycle live OTP test.
- **Live test cmd e748132b, 14:12-14:15Z, rc=0:** native-IP nav (no bot-block) -> MFA_OTP -> gateway adapter fetched OTP (window=120) -> Remember-My-Device checked -> LOGGED_IN -> .bd.identity to SM. Self-completed WITHOUT manual OTP.
- **GROUNDED on live SM (not rc=0):** captured_at 06-25T21:13Z -> **06-29T14:15:15Z** (advanced); bd_device_registration empty -> **present len30**; bd_identity len347; 8 cookies.
- **Native-IP VALIDATED for the login surface** (the unproven half) -- no proxy revert needed.

### Acceptance (TO)
AC#1 (no manual OTP) MET. AC#2 (captured_at advances) MET. AC#4 (firm-sep/window) MET. AC#3 (bd_silver lands) PENDING next bd-49f-runner reading the fresh cookie. AC#5 (>=24h no reseed + topic quiet) PENDING durability. bd-49f-authtoken-dead flips OK on next probe cycle. **GATE B held** -- box stopped, no unattended freshness-trigger armed; the cross-firm OTP lock gates the unattended future.

## Compiler Tools
| Tool | Why | Result |
|---|---|---|
| comp-iam service bd-49f-auto-login-role | AE mandate -- box role secret access before deploy | PASS -- GetSecretValue blackdiamond/49f/* (covers gateway-token+session+creds+relay) + astn/kimi/api-key; PutSecretValue session; s3:GetObject deploy-prefix. LEG2 IAM green. (DESIRED; CVO confirmed live policy matches.) |
| deploy_ledger.py open/close-leg/close | NEVER-law deploy-completion gate | PASS -- 4-leg ledger OPENED at deploy-start, all 4 proven, CLOSED. No stranded leg. |
| comp-freshness bd | TO mandate (accept) | GAP -- `bd` is not a valid subcommand (choices: chain/script/artifact/ddb/all); TO shorthand. 49f silver freshness deferred to next-runner anyway (cookie now fresh). |
| comp-pipescript deployed | TO mandate (box-script MATCH) | N/A-for-EC2 -- models gold scripts, not EC2 box wrappers (known gap, prior log 06-26). Box-script MATCH proven authoritatively via SSM md5 of /opt == committed e6e5ee2e (ledger L3). |

**What worked:** comp-iam gave the decisive pre-deploy IAM clearance; deploy_ledger enforced the no-half-baked-box discipline. Grounding the DEPLOYED js (not the repo) caught FORK-2 -- the load-bearing finding. **Gaps:** comp-freshness has no `bd` top-level alias (subcommand required); comp-pipescript doesn't model EC2 box wrappers (md5-verify is the substitute). Heavy operational AWS (SSM login orchestration, SM grounding, S3 bake, EC2 start/stop) off-rail by design -- no comp-tool runs a live BD login / SM grounding.

## Blockers
None blocking. AC#3/#5 = external scheduled gates (next bd-49f-runner + 24h). GATE-B lock = a follow-on TO (COO formalizing); not on this critical path.

## Next Steps
- **[next bd-49f-runner]** reads the fresh cookie -> bd_silver transactions/realized/unrealized unfreeze (AC#3). Watch bd-49f-authtoken-dead flip OK.
- **[GATE-B lock]** build per design 09d0883cd once COO's lock TO lands: box-side acquire/release wrap (my lane) + gateway code (0.7.0/base) + CTO arch-gate. Unattended 49f enablement gated on it.
- **[COO]** RAVC acceptance once silver lands; formalize lock TO.

## MCP traffic
~14 messages: LEG0 RAVC (COO+CTO), arch-gate grounding rounds (CTO C1/Q4/C2), FORK rulings (COO native-IP, GATE-B lock), GATE-B inputs, lock-design circulation (COO/CTO), 0.7.0 gates (blast+bearer+manifest), LEG2 RAVC (COO+CTO+0.7.0). CVO finding (proxy drift) actioned.
