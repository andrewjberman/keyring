# Deploy Completion Record
**Date opened:** 2026-10-01T10:33:01.951853+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T112303Z
**Deploy:** Hop 8 window on the st7 resident: leg P ONE liveness read, leg S ONE operator sign-in only if the session is not live, leg J ONE Analysis attempt for Cottonwood (CTO batch 76 item 5)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | ONE GET of the report-template route, capture removed, both halves, the st7 root and the solo gate first | PROBE_VERDICT by name; output read for values before commit | PROBE_VERDICT=LIVE at 10:47:46Z on the st7 root: one template GET, 200 application/json, no WAF action, not a login page; session of 08:21:20Z; output read for values: none | CLOSED 20261001T112302Z |
| S1 | verify | only if P1 reads NOT_LIVE: ONE operator sign-in as the resident's user on the st7 library | LEG_S_VERDICT by name with the redacted receipt and the session's dates -- or NOT RUN with P1's verdict | NOT RUN: P1 read LIVE; 0 sign-ins in the window | CLOSED 20261001T112303Z |
| J1 | verify | one K4 POST and one K5 POST on a live session | root and solo gates clean; login 200; one upload POST and one submission POST; the request id -- or NOT RUN | root gate a3b35fd376-st7 and solo gate clean; login 200 10:49:23Z; ONE K4 POST 200 then NORMALIZED 10:49:34Z (RESOLVE READY on the first receive: the sessionless lookup served); ONE K5 POST 200 QUEUED REQ-7c7a9e45eb496564f635754a; 3 POSTs in HOP8/H8_overview_cottonwood.json | CLOSED 20261001T112303Z |
| J2 | verify | the job's terminal state by name with the resident journal | state and code; every RESOLVE, EVICTION, ATTENTION, READ_BACK, TOLERANCE, REFUSED_PDF and retained line; on a kept PDF the live status read first; on READY the receipt shapes and case trace -- or NOT RUN | state ATTENTION code TOLERANCE_REQUIRES_STATIC 11:05:43Z; journal: READ_BACK_RELEASE 202 then retained WAF_CHALLENGE 10:50:03Z, READ_BACK_DONE 200 11:05:09Z, TOLERANCE_TYPE type=- as_of=-, TOLERANCE_ROWS pages=23 table_pages=1 name_lines=0 accepted=0, REFUSED_PDF kept=1 artifact ART-58f132884b3f5dc8; live status read first: DOCUMENT_VERDICT=NONE_SERVED; kept PDF prints the name cut at 47 characters with an ellipsis, row cells Static and Custom; offline certification of the kept PDF PUBLISHED; print HOP8/OUTCOME_20261001.md | CLOSED 20261001T112303Z |
| J3 | verify | no residue | both queue depths; no second POST; sign-ins counted | irpt-generation 0/0 and irpt-generation-dlq 0/0; no second POST; 0 sign-ins; stored session last changed 08:21:20Z unchanged | CLOSED 20261001T112303Z |

## Log

- 20261001T103301Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
- 20261001T112302Z LEG P1 closed: PROBE_VERDICT=LIVE at 10:47:46Z on the st7 root: one template GET, 200 application/json, no WAF action, not a login page
- 20261001T112303Z LEG S1 closed: NOT RUN: P1 read LIVE; 0 sign-ins in the window
- 20261001T112303Z LEG J1 closed: root gate a3b35fd376-st7 and solo gate clean; login 200 10:49:23Z; ONE K4 POST 200 then NORMALIZED 10:49:34Z (RESOLVE RE
- 20261001T112303Z LEG J2 closed: state ATTENTION code TOLERANCE_REQUIRES_STATIC 11:05:43Z; journal: READ_BACK_RELEASE 202 then retained WAF_CHALLENGE 10:
- 20261001T112303Z LEG J3 closed: irpt-generation 0/0 and irpt-generation-dlq 0/0; no second POST; 0 sign-ins; stored session last changed 08:21:20Z uncha
- 20261001T112303Z CLOSED -- all 5 legs proven
