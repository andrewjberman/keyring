# Deploy Completion Record
**Date opened:** 2026-10-16T22:24:19.818369+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T222806Z
**Deploy:** IRPT_ANLREQ TO-RUN-FWD5.live-cross-firm-s2-ib2 (AR-tz-73): SECOND sitting: mint TWO synthetic principals in opal-users-v2 (digests 28cb5947d068 run principal firm cottonwood, 7b925797fd61 control principal firm opal-capital allowedFirmIds 49financial), run the control then the firm-B run with the fixed driver (sends X-Contract-Version v1, grades report-side routes by the envelope) against the one synthetic ticket on the reused 5174 server (read-shaped GETs and the login only), remove both principals; stays OPEN until both read ABSENT; packet blob 3cc0ed6a87, CTO RE-SIGN 3; no write to any ticket, request or job
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | activation | TWO users rows (digests 28cb5947d068 and 7b925797fd61) minted once each by fwd5_mint.py with the stated scopes, entitlement_rows 0 | MINT-OK READBACK-OK and MINT-SCOPE lines for both | both mints MINT-OK READBACK-OK with MINT-SCOPE lines (cottonwood entitlement_rows 0; 49financial entitlement_rows 0); email-index count 1 for each | CLOSED 20261016T222805Z |
| C | verify | control run (--control) as the entitled identity with the fixed driver | driver exit 0 | control run exit 0 with the fixed driver: ticket-read ALLOWED, ticket-list ALLOWED, ALLOWED=2 DENIED=3 UNREACHED=2 EXCLUDED=2 of 9; r56 control OK (served checkout 75a71ae3 unchanged) | CLOSED 20261016T222805Z |
| F | verify | firm-B run (only after a control exit 0) | driver exit and report counts recorded | firm-B run exit 0: REFUSED=7 LEAK=0 UNREACHED=0 EXCLUDED=2 of 9; r56 report OK; r56 fence OK (fence SHOWN on ticket-list and ticket-read; INCONCLUSIVE on commentary-pdf, form-as-filled, opal-report, original-upload, report-pdf because the control did not read ALLOWED there) | CLOSED 20261016T222806Z |
| R | activation | removal of BOTH principals and ABSENT by the email GSI and a ConsistentRead for each, then r56_checks absent | R56-ABSENT-OK | both principals removed (REMOVE-OK, ABSENT GSI and ABSENT CONSISTENT for each); r56_checks absent R56-ABSENT-OK both principals no PROFILE row, index count 0 | CLOSED 20261016T222806Z |

## Log

- 20261016T222419Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
- 20261016T222805Z LEG M closed: both mints MINT-OK READBACK-OK with MINT-SCOPE lines (cottonwood entitlement_rows 0; 49financial entitlement_rows 0); em
- 20261016T222805Z LEG C closed: control run exit 0 with the fixed driver: ticket-read ALLOWED, ticket-list ALLOWED, ALLOWED=2 DENIED=3 UNREACHED=2 EXCLU
- 20261016T222806Z LEG F closed: firm-B run exit 0: REFUSED=7 LEAK=0 UNREACHED=0 EXCLUDED=2 of 9; r56 report OK; r56 fence OK (fence SHOWN on ticket-list
- 20261016T222806Z LEG R closed: both principals removed (REMOVE-OK, ABSENT GSI and ABSENT CONSISTENT for each); r56_checks absent R56-ABSENT-OK both pri
- 20261016T222806Z CLOSED -- all 4 legs proven
