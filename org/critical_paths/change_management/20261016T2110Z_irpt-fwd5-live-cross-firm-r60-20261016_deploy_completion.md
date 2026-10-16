# Deploy Completion Record
**Date opened:** 2026-10-16T21:10:02.894947+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T211611Z
**Deploy:** IRPT_ANLREQ TO-RUN-FWD5.live-cross-firm-ib2 (AR-tz-71): mint TWO synthetic principals in opal-users-v2 (digests 28cb5947d068 run principal firm cottonwood, 7b925797fd61 control principal firm opal-capital allowedFirmIds 49financial), run the control then the firm-B run against the one synthetic ticket on the reused 5174 server (read-shaped GETs and the login only), remove both principals; stays OPEN until both read ABSENT; pair re-signed on packet blob 57052520eb, CTO half RE-SIGN 2 @e1062579f2; no write to any ticket, request or job
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | activation | TWO users rows (digests 28cb5947d068 and 7b925797fd61) minted once each by fwd5_mint.py with the stated scopes, entitlement_rows 0 | MINT-OK READBACK-OK and MINT-SCOPE lines for both | both mints MINT-OK READBACK-OK with MINT-SCOPE lines (cottonwood entitlement_rows 0; 49financial entitlement_rows 0); email-index count 1 for each | CLOSED 20261016T211610Z |
| C | verify | control run (--control) as the entitled identity: ticket-read and ticket-list ALLOWED | driver exit 0 | control run exit 0: ticket-read ALLOWED, ticket-list ALLOWED, ALLOWED=6 DENIED=1 UNREACHED=0 EXCLUDED=2 of 9; r56 control OK | CLOSED 20261016T211610Z |
| F | verify | firm-B run: every made call REFUSED, no LEAK (runs only after a control exit 0) | driver exit 0, report 7 REFUSED 0 LEAK 0 UNREACHED | firm-B run done (one run, no retry): exit 1, REFUSED=3 LEAK=4 UNREACHED=0 EXCLUDED=2; LEAK routes original-upload, opal-report, report-pdf, commentary-pdf (status 200); fence and report checks FAIL; reported to T2 and the CTO; the sitting stopped and removed both principals first | CLOSED 20261016T211611Z |
| R | activation | removal of BOTH principals and ABSENT by the email GSI and a ConsistentRead for each, then r56_checks absent | R56-ABSENT-OK | both principals removed (REMOVE-OK, ABSENT GSI and ABSENT CONSISTENT for each); r56_checks absent R56-ABSENT-OK both principals no PROFILE row, index count 0 | CLOSED 20261016T211611Z |

## Log

- 20261016T211002Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
- 20261016T211610Z LEG M closed: both mints MINT-OK READBACK-OK with MINT-SCOPE lines (cottonwood entitlement_rows 0; 49financial entitlement_rows 0); em
- 20261016T211610Z LEG C closed: control run exit 0: ticket-read ALLOWED, ticket-list ALLOWED, ALLOWED=6 DENIED=1 UNREACHED=0 EXCLUDED=2 of 9; r56 contro
- 20261016T211611Z LEG F closed: firm-B run done (one run, no retry): exit 1, REFUSED=3 LEAK=4 UNREACHED=0 EXCLUDED=2; LEAK routes original-upload, opal-
- 20261016T211611Z LEG R closed: both principals removed (REMOVE-OK, ABSENT GSI and ABSENT CONSISTENT for each); r56_checks absent R56-ABSENT-OK both pri
- 20261016T211611Z CLOSED -- all 4 legs proven
