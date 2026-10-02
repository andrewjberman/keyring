# Deploy Completion Record
**Date opened:** 2026-10-02T09:39:08.105986+00:00
**Status:** OPEN
**Deploy:** sign-in option C: ONE scripted operator sign-in on the st12 host, then ONE Overview job only if it authenticates (CTO batches 130-131); window packet, both halves
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | ONE leg S on i-0167fd745ad906a66 through Systems Manager | LEG_S_VERDICT by name; redacted receipt; the stored session's dates and fence | LEG_S_VERDICT=AUTHENTICATED (SIGNIN_C/LEG_S_OUTPUT_20261001.txt, SSM faadcb05-eade-4e47-b2e1-b83d8f3b9cc1, end 09:45:46Z): steps CH-SIGNIN_FORM then CH-AUTHENTICATED, no challenge; probe 200 LIVE; identity read; persisted fence 23 (previous 21); stored session last changed 2026-10-02T09:45:44.610Z (a new version). The stored bundle's own probe before the sign-in read 403 EVICTED_HARD (concurrent sign-in). Output read for value-shaped strings: 0 | CLOSED 20261002T094708Z |
| J1 | verify | ONE K4 and ONE K5 POST for Cottonwood, only on S1 AUTHENTICATED | the two responses; NOT RUN with S1's verdict otherwise |  | OPEN |
| J2 | verify | the job's terminal state | state by name with the journal incl. IRPT_SESSION_ROTATION lines and the secret's version list; NOT RUN otherwise |  | OPEN |
| J3 | verify | both queues after the window | irpt-generation and dead-letter depths |  | OPEN |

## Log

- 20261002T093908Z OPENED by 2.0.0_SA_COO~Y with 4 leg(s)
- 20261002T094708Z LEG S1 closed: LEG_S_VERDICT=AUTHENTICATED (SIGNIN_C/LEG_S_OUTPUT_20261001.txt, SSM faadcb05-eade-4e47-b2e1-b83d8f3b9cc1, end 09:45:46Z
