# Deploy Completion Record
**Date opened:** 2026-10-01T10:33:01.951853+00:00
**Status:** OPEN
**Deploy:** Hop 8 window on the st7 resident: leg P ONE liveness read, leg S ONE operator sign-in only if the session is not live, leg J ONE Analysis attempt for Cottonwood (CTO batch 76 item 5)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | ONE GET of the report-template route, capture removed, both halves, the st7 root and the solo gate first | PROBE_VERDICT by name; output read for values before commit |  | OPEN |
| S1 | verify | only if P1 reads NOT_LIVE: ONE operator sign-in as the resident's user on the st7 library | LEG_S_VERDICT by name with the redacted receipt and the session's dates -- or NOT RUN with P1's verdict |  | OPEN |
| J1 | verify | one K4 POST and one K5 POST on a live session | root and solo gates clean; login 200; one upload POST and one submission POST; the request id -- or NOT RUN |  | OPEN |
| J2 | verify | the job's terminal state by name with the resident journal | state and code; every RESOLVE, EVICTION, ATTENTION, READ_BACK, TOLERANCE, REFUSED_PDF and retained line; on a kept PDF the live status read first; on READY the receipt shapes and case trace -- or NOT RUN |  | OPEN |
| J3 | verify | no residue | both queue depths; no second POST; sign-ins counted |  | OPEN |

## Log

- 20261001T103301Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
