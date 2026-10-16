# Deploy Completion Record
**Date opened:** 2026-10-16T22:24:19.818369+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-RUN-FWD5.live-cross-firm-s2-ib2 (AR-tz-73): SECOND sitting: mint TWO synthetic principals in opal-users-v2 (digests 28cb5947d068 run principal firm cottonwood, 7b925797fd61 control principal firm opal-capital allowedFirmIds 49financial), run the control then the firm-B run with the fixed driver (sends X-Contract-Version v1, grades report-side routes by the envelope) against the one synthetic ticket on the reused 5174 server (read-shaped GETs and the login only), remove both principals; stays OPEN until both read ABSENT; packet blob 3cc0ed6a87, CTO RE-SIGN 3; no write to any ticket, request or job
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | activation | TWO users rows (digests 28cb5947d068 and 7b925797fd61) minted once each by fwd5_mint.py with the stated scopes, entitlement_rows 0 | MINT-OK READBACK-OK and MINT-SCOPE lines for both |  | OPEN |
| C | verify | control run (--control) as the entitled identity with the fixed driver | driver exit 0 |  | OPEN |
| F | verify | firm-B run (only after a control exit 0) | driver exit and report counts recorded |  | OPEN |
| R | activation | removal of BOTH principals and ABSENT by the email GSI and a ConsistentRead for each, then r56_checks absent | R56-ABSENT-OK |  | OPEN |

## Log

- 20261016T222419Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
