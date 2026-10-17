# Deploy Completion Record
**Date opened:** 2026-10-17T20:44:03.516270+00:00
**Status:** CLOSED -- STOPPED AT U (the door authorized the actor and answered RESOLVING, no input_id); 6 of 7 synthetic keys deleted and ABSENT; ONE LEFTOVER BLOB (the upload original holdings CSV, delete AccessDenied, see LEFTOVER.txt); 0 ticket, 0 request; closed 20261017T2050Z
**Deploy:** IRPT_ANLREQ TO-RUN-COMMENTARY-E2E-2: the second ONE fresh synthetic commentary run end to end, now with ONE synthetic named advisor (fwd1_advisor.py) so the upload door can authorize; then delete by recorded key (users, partner, ticket, request, job, artifacts, upload rows); COO half 394e573a4a plus ADDENDUM 1 02149564860; CTO half fec24f492d; nothing deployed
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | activation | mint the synthetic staff user and the synthetic advisor (users and partner rows) and record every key created | mint read-backs present | synthetic staff user and synthetic advisor (users and partner rows) minted once each, read-backs ok (2026-10-17T20:45:42Z); login ok | CLOSED 20261017T204808Z |
| S | activation | login, upload with advisor_email, ticket and submit once each | closed states and the REQ id | NOT RUN beyond the upload: the door authorized the actor with advisor_email and answered RESOLVING (no input_id); one upload try per the order, so a STOP at U; no ticket, no request created | CLOSED 20261017T204808Z |
| P | verify | poll job READY, commentary_ref, draft artifact, packager line, PDF artifact within 30 minutes | the hop results | NOT RUN: stopped at U; nothing to poll | CLOSED 20261017T204808Z |
| R | verify | the commentary-pdf route read as the same user | pass or the closed code | NOT RUN: stopped at U; no request, so no route read | CLOSED 20261017T204808Z |
| D | activation | delete exactly the recorded synthetic keys including the advisor rows, each read back ABSENT | keys deleted of recorded | 6 of 7 recorded keys deleted and read ABSENT (staff user, advisor users and partner rows, the upload's three index rows; fresh reads agree; Monday's advisor untouched and ABSENT); ONE leftover: the upload's original holdings CSV blob, delete AccessDenied for this principal, reported in LEFTOVER.txt; dead letter 1 before and 1 after | CLOSED 20261017T204808Z |

## Log

- 20261017T204403Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261017T204808Z LEG A closed: synthetic staff user and synthetic advisor (users and partner rows) minted once each, read-backs ok (2026-10-17T20:45:42
- 20261017T204808Z LEG S closed: NOT RUN beyond the upload: the door authorized the actor with advisor_email and answered RESOLVING (no input_id); one up
- 20261017T204808Z LEG P closed: NOT RUN: stopped at U; nothing to poll
- 20261017T204808Z LEG R closed: NOT RUN: stopped at U; no request, so no route read
- 20261017T204808Z LEG D closed: 6 of 7 recorded keys deleted and read ABSENT (staff user, advisor users and partner rows, the upload's three index rows;
- 20261017T204808Z CLOSED -- all 5 legs proven
