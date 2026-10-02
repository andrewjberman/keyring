# Deploy Completion Record
**Date opened:** 2026-10-02T09:39:08.105986+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T101609Z
**Deploy:** sign-in option C: ONE scripted operator sign-in on the st12 host, then ONE Overview job only if it authenticates (CTO batches 130-131); window packet, both halves
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | ONE leg S on i-0167fd745ad906a66 through Systems Manager | LEG_S_VERDICT by name; redacted receipt; the stored session's dates and fence | LEG_S_VERDICT=AUTHENTICATED (SIGNIN_C/LEG_S_OUTPUT_20261001.txt, SSM faadcb05-eade-4e47-b2e1-b83d8f3b9cc1, end 09:45:46Z): steps CH-SIGNIN_FORM then CH-AUTHENTICATED, no challenge; probe 200 LIVE; identity read; persisted fence 23 (previous 21); stored session last changed 2026-10-02T09:45:44.610Z (a new version). The stored bundle's own probe before the sign-in read 403 EVICTED_HARD (concurrent sign-in). Output read for value-shaped strings: 0 | CLOSED 20261002T094708Z |
| J1 | verify | ONE K4 and ONE K5 POST for Cottonwood, only on S1 AUTHENTICATED | the two responses; NOT RUN with S1's verdict otherwise | login 200; K4 200 NORMALIZED UP-bb72ac61..; K5 200 QUEUED REQ-c07e64ca6c74b8e5310f56e0 at 09:57:37Z (SIGNIN_C/LEG_J_RUN_20261002.txt) | CLOSED 20261002T101609Z |
| J2 | verify | the job's terminal state | state by name with the journal incl. IRPT_SESSION_ROTATION lines and the secret's version list; NOT RUN otherwise | READY 10:14:06Z report RPT-819429e0bd7084a11cdc74f023a9c48c certification 2226e093..; journal: 4 IRPT_SESSION_ROTATION kept=1 (multidb_pin_writes), 0 eviction/refresh/capture lines, TOLERANCE_TYPE name=cut; stored session OK fence 23 generation 6ce12b3c (SIGNIN_C/LEG_J_READ_20261002.txt, SECRET_VERSIONS_20261002.txt) | CLOSED 20261002T101609Z |
| J3 | verify | both queues after the window | irpt-generation and dead-letter depths | irpt-generation 0/0 at 10:15:18Z (SIGNIN_C/LEG_J_READ_20261002.txt) | CLOSED 20261002T101609Z |

## Log

- 20261002T093908Z OPENED by 2.0.0_SA_COO~Y with 4 leg(s)
- 20261002T094708Z LEG S1 closed: LEG_S_VERDICT=AUTHENTICATED (SIGNIN_C/LEG_S_OUTPUT_20261001.txt, SSM faadcb05-eade-4e47-b2e1-b83d8f3b9cc1, end 09:45:46Z
- 20261002T101609Z LEG J1 closed: login 200; K4 200 NORMALIZED UP-bb72ac61..; K5 200 QUEUED REQ-c07e64ca6c74b8e5310f56e0 at 09:57:37Z (SIGNIN_C/LEG_J_RUN_
- 20261002T101609Z LEG J2 closed: READY 10:14:06Z report RPT-819429e0bd7084a11cdc74f023a9c48c certification 2226e093..; journal: 4 IRPT_SESSION_ROTATION k
- 20261002T101609Z LEG J3 closed: irpt-generation 0/0 at 10:15:18Z (SIGNIN_C/LEG_J_READ_20261002.txt)
- 20261002T101609Z CLOSED -- all 4 legs proven
