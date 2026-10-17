# Deploy Completion Record
**Date opened:** 2026-10-17T00:37:16.369705+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T004247Z
**Deploy:** IRPT_ANLREQ TO-RUN-FWD5.live-cross-firm-s3-ib2 (third sitting, round 65, cell AR-tz-75): two scoped principals (digests 28cb5947d068 and 7b925797fd61) minted once each in opal-users-v2, a control then a firm-B run for each of two targets (packaged and synthetic ticket), then BOTH removed. Worktree union read 2026-10-17T00:4xZ: 99 worktrees, 2050 marker files, 16 naming the users table, ticket service or FWD5, all 16 ledgers CLOSED.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | activation | TWO users rows (digests 28cb5947d068 and 7b925797fd61) minted once each by fwd5_mint.py with the stated scopes, entitlement_rows 0 | MINT-OK READBACK-OK and MINT-SCOPE lines for both | both mints MINT-OK READBACK-OK with MINT-SCOPE lines (cottonwood entitlement_rows 0; 49financial entitlement_rows 0); email-index count 1 for each | CLOSED 20261017T004209Z |
| C1 | verify | PACKAGED target control run (--control) as the entitled identity | driver exit 0 | packaged control exit 0: ticket-read ALLOWED, ticket-list ALLOWED, ALLOWED=2 DENIED=11 UNREACHED=0 EXCLUDED=2 of 15; the file routes original-upload, report-pdf, commentary-pdf DENIED NOT_AUTHORIZED (broken control there, RE-SIGN 4) | CLOSED 20261017T004209Z |
| F1 | verify | PACKAGED target firm-B run (only after a control exit 0) | driver exit and report counts recorded | packaged firm-B run exit 0: REFUSED=13 LEAK=0 UNREACHED=0 EXCLUDED=2 of 15 | CLOSED 20261017T004210Z |
| C2 | verify | SYNTHETIC target control run (--control) | driver exit 0 | synthetic control exit 0: ticket-read ALLOWED, ticket-list ALLOWED, ALLOWED=6 DENIED=7 UNREACHED=0 EXCLUDED=2 of 15 | CLOSED 20261017T004210Z |
| F2 | verify | SYNTHETIC target firm-B run (only after a control exit 0) | driver exit and report counts recorded | synthetic firm-B run exit 0: REFUSED=13 LEAK=0 UNREACHED=0 EXCLUDED=2 of 15; r56 report OK; r56 fence FAIL on the packaged target (control did not serve 3 file routes) | CLOSED 20261017T004210Z |
| R | activation | removal of BOTH principals and ABSENT by the email GSI and a ConsistentRead for each, then r56_checks absent | R56-ABSENT-OK | both principals removed (REMOVE-OK, ABSENT GSI and ABSENT CONSISTENT for each); r56_checks absent R56-ABSENT-OK both principals no PROFILE row, index count 0 | CLOSED 20261017T004210Z |

## Log

- 20261017T003716Z OPENED by 0.7.0_AE_CloudOps~IB2 with 6 leg(s)
- 20261017T004209Z LEG M closed: both mints MINT-OK READBACK-OK with MINT-SCOPE lines (cottonwood entitlement_rows 0; 49financial entitlement_rows 0); em
- 20261017T004209Z LEG C1 closed: packaged control exit 0: ticket-read ALLOWED, ticket-list ALLOWED, ALLOWED=2 DENIED=11 UNREACHED=0 EXCLUDED=2 of 15; the
- 20261017T004210Z LEG F1 closed: packaged firm-B run exit 0: REFUSED=13 LEAK=0 UNREACHED=0 EXCLUDED=2 of 15
- 20261017T004210Z LEG C2 closed: synthetic control exit 0: ticket-read ALLOWED, ticket-list ALLOWED, ALLOWED=6 DENIED=7 UNREACHED=0 EXCLUDED=2 of 15
- 20261017T004210Z LEG F2 closed: synthetic firm-B run exit 0: REFUSED=13 LEAK=0 UNREACHED=0 EXCLUDED=2 of 15; r56 report OK; r56 fence FAIL on the packag
- 20261017T004210Z LEG R closed: both principals removed (REMOVE-OK, ABSENT GSI and ABSENT CONSISTENT for each); r56_checks absent R56-ABSENT-OK both pri
- 20261017T004247Z CLOSED -- all 6 legs proven
