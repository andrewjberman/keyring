# Deploy Completion Record
**Date opened:** 2026-10-01T12:02:46.767432+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T124850Z
**Deploy:** Second hop-8 window on the st8 resident: leg P ONE liveness read, leg S ONE operator sign-in only if the session is not live, leg J ONE Analysis attempt for Cottonwood (CTO batches 76 and 83)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | ONE GET of the report-template route, capture removed, both halves, the st8 root and the solo gate first | PROBE_VERDICT by name; output read for values before commit | PROBE_VERDICT=LIVE at 12:12:35Z on the st8 root: one template GET, 200 application/json, no WAF action, not a login page; session of 08:21:20Z; output read for values: none | CLOSED 20261001T124850Z |
| S1 | verify | only if P1 reads NOT_LIVE: ONE operator sign-in as the resident's user | LEG_S_VERDICT by name with the redacted receipt -- or NOT RUN with P1's verdict | NOT RUN: P1 read LIVE; 0 sign-ins in the window | CLOSED 20261001T124850Z |
| J1 | verify | one K4 POST and one K5 POST on a live session | root and solo gates clean; login 200; one upload POST and one submission POST; the request id -- or NOT RUN | root gate 9ac9b56d3c-st8 and solo gate clean; login 200 12:14:10Z; ONE K4 POST 200 then NORMALIZED 12:14:22Z; ONE K5 POST 200 QUEUED REQ-a69e5751d42c374f1d2354f9; 3 POSTs in HOP8B/H8B_overview_cottonwood.json | CLOSED 20261001T124850Z |
| J2 | verify | the job's terminal state by name with the resident journal | state and code; the TOLERANCE_TYPE line with its name= field quoted; every RESOLVE, EVICTION, ATTENTION, READ_BACK, TOLERANCE, REFUSED_PDF and retained line; on READY the receipt shapes, the status-route read and the case trace -- or NOT RUN | state READY 12:31:12Z, report RPT-ec30778a867a59f3805be6e7f07d35cb; journal: READ_BACK_RELEASE 202 then retained WAF_CHALLENGE 12:14:53Z, READ_BACK_DONE 200 12:29:59Z, IRPT_RESIDENT_TOLERANCE_TYPE type=Static as_of=Custom name=cut 12:30:22Z, no EVICTION, ATTENTION or REFUSED_PDF; status-route read DOCUMENT_VERDICT=SERVED:sections-by-request; case trace 22 links 20 MATCH 0 MISMATCH 2 NOT_EVALUATED; receipt carries no vendor_requests (filed as a row); print HOP8B/OUTCOME_20261001.md | CLOSED 20261001T124850Z |
| J3 | verify | no residue | both queue depths; no second POST; sign-ins counted | irpt-generation 0/0 and irpt-generation-dlq 0/0; no second POST; 0 sign-ins; stored session last changed 08:21:20Z unchanged | CLOSED 20261001T124850Z |

## Log

- 20261001T120246Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
- 20261001T124850Z LEG P1 closed: PROBE_VERDICT=LIVE at 12:12:35Z on the st8 root: one template GET, 200 application/json, no WAF action, not a login page
- 20261001T124850Z LEG S1 closed: NOT RUN: P1 read LIVE; 0 sign-ins in the window
- 20261001T124850Z LEG J1 closed: root gate 9ac9b56d3c-st8 and solo gate clean; login 200 12:14:10Z; ONE K4 POST 200 then NORMALIZED 12:14:22Z; ONE K5 POS
- 20261001T124850Z LEG J2 closed: state READY 12:31:12Z, report RPT-ec30778a867a59f3805be6e7f07d35cb; journal: READ_BACK_RELEASE 202 then retained WAF_CHA
- 20261001T124850Z LEG J3 closed: irpt-generation 0/0 and irpt-generation-dlq 0/0; no second POST; 0 sign-ins; stored session last changed 08:21:20Z uncha
- 20261001T124850Z CLOSED -- all 5 legs proven
