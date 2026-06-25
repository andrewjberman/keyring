# Cottonwood durable auto-auth — the cot-parallel of ADVI_BDAPIMIG (firm-separated)

**Author:** 0.6.0_AE_PartnerETL · **Date:** 2026-06-25 · **Driver:** 3.0.0_SA_CVO (verifies both firm-separated)
**Trigger:** Andrew-direct "we need the OTP solution for BOTH cottonwood and 49" + both firms now on BD 2FA.
**Status:** SCOPING (49F is the proven reference; this replicates it cot-bound).

## Why (grounded)

cot's BD session is DOWN on the **same MFA wall** as 49F. Ground truth (SSM log, cot-bd-session-trigger
06-25 02:00, command 6a6e5d71): `ERROR: FAILED_MFA_REQUIRED -- BD prompted MFA/OTP; manual OTP path needed`.
cot's exporter `cot_bd_session_fetch.py` (login `Andrew.Opal`) fills creds + submits but has **no OTP
handling** -> dies at MFA -> cot session frozen at **06-23** (silver/bronze/platinum all ~2 trading days
stale). And **worse than 49F**: cot has NO keepalive / NO freshness-probe / NO alarm -> the failure was
INVISIBLE for ~2 days. 49F at least alarmed.

## NEVER#1 — firm separation is law for this whole build

cot is a COMPLETELY separate firm pipeline. Every artifact cot-bound, never shared/mirrored with bd:
cot creds -> `blackdiamond/cot/credentials`; cot session -> `blackdiamond/cot/session`; cot relay ->
`blackdiamond/cot/otp-relay`; data -> `opal-data-cot`; cot-firm box/role; cot SNS topic. The 49F IAM has
an explicit cot Deny and vice-versa — preserve it.

## Reuse vs build (the efficient path)

cot does NOT need a new EC2 box — it has a running exporter box (`i-0643a5bee8a8feabf`,
`cot-bd-session-trigger` env: COT_CREDS_SECRET / COT_SESSION_SECRET / COT_DATA_BUCKET=opal-data-cot).
The build is an **upgrade of the cot login path** + the detection layer 49F has and cot lacks.

### Component map (49F reference -> cot-parallel)

| 49F (proven) | cot-parallel | Action |
|---|---|---|
| `bd_49f_auto_login.js` (CV-login + OTP adapter + device-trust + cookie capture) | upgrade `cot_bd_session_fetch.py`'s login OR port the JS pattern cot-bound | the OTP-consume is the missing link; same relay/gateway adapter, cot secrets |
| EC2 box `i-0fa1846f04ed7e337` | REUSE cot exporter `i-0643a5bee8a8feabf` | no new box; add node/Playwright/Chromium if not present |
| `blackdiamond/49f/{credentials,session}` | `blackdiamond/cot/{credentials,session}` | exist already |
| `blackdiamond/49f/otp-relay` (bridge) | `blackdiamond/cot/otp-relay` | CREATE (transient, cot-bound) |
| OTP gateway `/otp/fetch` (model-A bearer) | reuse same gateway, cot-scoped mailbox/sender | gateway reads Andrew's mailbox; see OTP-disambiguation risk below |
| `bd-49f-keepalive` @ rate(15m) | `cot-keepalive` | BUILD (cot has none) |
| `bd-49f-freshness-probe` + 5 TradingDayLag alarms | `cot-freshness-probe` + cot stale alarms | BUILD (cot has none — the invisible-failure gap) |
| `opal-bd-49f-cookie-alerts` SNS | `opal-bd-cot-cookie-alerts` SNS | BUILD |

## Open question to ground (same step we did for 49F)

**Where does cot's OTP land?** 49F's went to `Andrew@opalinvest.com` (sender `noreply@bdreporting.com`,
subject "Authentication Code You Requested"). cot login is `Andrew.Opal` — likely the SAME mailbox, but
UNCONFIRMED. The cot completing-run (relay) grounds it, exactly as the 49F smoke did.

**OTP-disambiguation risk (NEW, both-firms):** if cot + 49F logins fire close together, TWO OTP emails
from the SAME sender/subject land in the same mailbox -> the relay/gateway freshness-gate could grab the
wrong firm's code. Mitigations: (a) STAGGER the two firms' refreshes (different cron minutes — they already
differ: 49F vs cot 02:00); (b) the freshness `ts >= loginStart` gate already scopes to the most-recent;
(c) if BD ever distinguishes firm in the body, match on it. Lowest-risk: never run both completing-logins
concurrently. Document in the runbook.

## Sequence (post tonight's 49F solve)

1. Ground the cot OTP mailbox/sender (a cot relay completing-run, same as 49F tonight).
2. Port the proven CV-login + OTP-relay(+gateway) + device-trust + cookie-capture into the cot login path,
   cot-secret-bound; create `blackdiamond/cot/otp-relay`.
3. Build the cot detection layer: cot-keepalive (mint-probe) + cot-freshness-probe (TradingDayLag alarms)
   + `opal-bd-cot-cookie-alerts` SNS. (This closes cot's invisible-failure gap.)
4. Verify firm-separated (CVO): cot writes ONLY opal-data-cot/blackdiamond/cot/*; the 49F<->cot Deny holds.
5. Deploy-completion ledger; CVO certs both firms.

## Scope owner

0.6.0_AE_PartnerETL builds (owns the cot-exporter pattern); CVO verifies firm-separated; CTO arch on the
shared gateway's cot-scoping; COO sequences. Mirrors ADVI_BDAPIMIG.P1, cot-bound.
