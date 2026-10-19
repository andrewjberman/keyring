# /canonical-drive COMM_ASSIST -- 2.0.0_SA_COO~CA, laptop, 2026-10-19 17:2xZ-18:2xZ

**archetype:** DEPLOY

Round 22 (CA-p-1 merged; CA-p-2 the deploy). Continues `drive_log_20261019T16Z_andrew.md`.

| time (UTC) | act |
|---|---|
| 17:2xZ | CVO half SIGNED @f104cc803d (adds none; branch-A after-hash `p4kaI5t0...` matched byte for byte against the issuer's build; reads `me.json` and finds `mail` non-empty). All three halves SIGNED on pin e6c37673c8 |
| 17:3xZ | GO written and committed @99de84ce8c (order `pending`); the CTO's condition is in it: the FIRST `me-without-mail` raise rolls back in the same window; apply never 20:00Z-21:45Z |
| 17:3xZ | `/mstr-spawn 0.7.0_AE_CloudOps~COMM1` (pre-flight: no process, no marker, 2 of 20 windows, 1d: only this order open); registered LIVE in ~1 minute; pointer-only hint (a first send with an imperative was refused by LD-0529 and resent citing the order id) |
| 17:43Z | APPLIED by ~COMM1: Branch A 0/2/0, hash `p4kaI5t0...`, env keys and `enforce` unchanged, AC1 ok, AC2 P2-LIVE ok, re-plan No changes, DLQ 0/0/0 (handler LastModified 17:43:55Z, ingress 17:43:49Z) |
| 17:5xZ | the AFTER log read was blocked: the gateway chats call has returned 504 since 17:40:18Z (3.5 minutes BEFORE the apply); every ingress run since 17:41Z times out and none reaches the mail step. No rollback: the changed code is not reached. Issuer's own reads at 17:55Z agree (both functions on the pinned hash, P2-LIVE ok=True). Gateway report sent to MSTR; the CTO named the owner (NFRA_OPLGTW, site Z; restart OG-rs-1 issued 17:51Z) and asked for the read-back to hold |
| 18:0xZ | the lane's row for the outage is `COMM_ASSIST-S5` (ARMED, disarm_owner this seat); its `C22D-S<k>` id form was refused by the row gate: my order's defect, amended @e53db813be |
| 18:2xZ | issuer's close reader `real_run_p2.py` reads `NO-MAIL-YET` (0 batches, 0 raises) through two 30-minute watch windows |

## Issuer rulings

- No rollback on the 17:43Z apply: the outage predates it and the changed code is not reached (the CTO agrees, msg 109855).
- `COMM_ASSIST-C22D-S<k>` is an invalid row id; the order's line is amended to `COMM_ASSIST-S<k>` (gate limb graded: (viii) placeholders, NONE). The round-21 residual ("the next deploy order of this root names it") was not carried into this order: the issuer's defect.
- Row S5 stays ARMED until the gateway answers, a post-apply mail batch reads clean (`REFUSES-HIS-OWN` or `NO-HIS-OWN-YET`, never `ME-RAISE`), and the lane closes ledger leg L4.

## State at the end of the hour

CA-p-1 merged. CA-p-2 applied and verified live; condition 8 (the first mail event after the apply) UNOBSERVED because the gateway is down. Waiting on site Z's restart. Owed once a mail batch reads: close the ledger and the order (the lane), disarm S5, compile and send the L8 packet to the CVO (WORLD round), the CTO's exercised read, and the "where it landed" line to MSTR for ms. The CVO's `real_run_p2` reading and the round-close are mine.

## Compiler Tools

- `mstr-spawn` pre-flight (process scan, marker scan, concurrency, `to-check.py --all --assignee`), `spawn-agent.ps1`: worked; the spawned lane registered in about a minute.
- `real_run_p2.py` (issuer reader, CloudWatch `FilterLogEvents`, counts only): worked at base and live; reads `NO-MAIL-YET`.
- `.tools/aws lambda get-function-configuration`, `check_p2_equiv.py` (both modes): worked.
- Gap: the opalgateway MCP tools hang while the gateway is down (my `whoami` exceeded 120 s and failed).
- Gap: `send_message` to a Tier-2 seat refuses any send with an act and no cited order id (LD-0529); information sends pass.
