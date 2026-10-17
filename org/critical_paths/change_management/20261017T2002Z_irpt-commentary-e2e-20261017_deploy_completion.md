# Deploy Completion Record
**Date opened:** 2026-10-17T20:02:36.881714+00:00
**Status:** CLOSED -- STOPPED AT U (the upload door refused NOT_AUTHORIZED, the expected first stop); 1 synthetic users row created and deleted, nothing else created; 0 ticket, 0 request; closed 20261017T2012Z
**Deploy:** IRPT_ANLREQ TO-RUN-COMMENTARY-E2E: ONE fresh synthetic commentary run end to end (one synthetic staff user, one upload, one ticket, one request, resident, drafter, packager, commentary route read), then delete by recorded key; COO half blob 394e573a4a, CTO half f0fbfde004; nothing deployed
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | activation | mint the one synthetic staff user (opal-users-v2) and record every key created | mint read-back present | synthetic staff user minted once through the existing fwd1 mint (MINT-OK READBACK-OK) at 2026-10-17T20:10:01Z; login ok | CLOSED 20261017T201154Z |
| S | activation | login, upload, ticket and submit once each as the synthetic actor | closed states and the REQ id | NOT RUN beyond the upload: the door refused NOT_AUTHORIZED at 20:10:06Z (the CTO condition 3 expected first stop); no second upload, no ticket, no request created | CLOSED 20261017T201154Z |
| P | verify | poll job READY, commentary_ref, draft artifact, packager line, PDF artifact within the 30 minute budget | the hop results | NOT RUN: stopped at U; nothing to poll | CLOSED 20261017T201154Z |
| R | verify | the commentary-pdf route read as the same user | pass or the closed code | NOT RUN: stopped at U; no request, so no route read | CLOSED 20261017T201155Z |
| D | activation | delete exactly the recorded synthetic keys, each read back ABSENT | keys deleted of recorded | 1 of 1 recorded keys deleted and read ABSENT (the users row; ConsistentRead and the email index both ABSENT, re-read fresh); nothing else was created; dead letter 1 before and 1 after | CLOSED 20261017T201155Z |

## Log

- 20261017T200236Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261017T201154Z LEG A closed: synthetic staff user minted once through the existing fwd1 mint (MINT-OK READBACK-OK) at 2026-10-17T20:10:01Z; login ok
- 20261017T201154Z LEG S closed: NOT RUN beyond the upload: the door refused NOT_AUTHORIZED at 20:10:06Z (the CTO condition 3 expected first stop); no se
- 20261017T201154Z LEG P closed: NOT RUN: stopped at U; nothing to poll
- 20261017T201155Z LEG R closed: NOT RUN: stopped at U; no request, so no route read
- 20261017T201155Z LEG D closed: 1 of 1 recorded keys deleted and read ABSENT (the users row; ConsistentRead and the email index both ABSENT, re-read fre
- 20261017T201155Z CLOSED -- all 5 legs proven
