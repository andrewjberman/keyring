# Deploy Completion Record
**Date opened:** 2026-10-01T15:04:02.191509+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T155126Z
**Deploy:** E3 Multi-Comp arm on the st9 resident, the trial of E2: leg P ONE liveness read, leg S ONE operator sign-in only if the session is not live, leg J ONE Multi-Comp attempt for Cottonwood (CTO batch 88 item 4)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | ONE GET of the report-template route, capture removed, both halves, the st9 root and the solo gate first | PROBE_VERDICT by name; output read for values before commit | 15:15:41Z, SSM 0b606c2a-2a9d-4ec2-98ca-00e48817814e: root gate st9, solo gate clean; ONE GET of the report-template route: HTTP 200 JSON, no WAF action; PROBE_VERDICT=LIVE; output read for values, 0 found | CLOSED 20261001T155126Z |
| S1 | verify | only if P1 reads NOT_LIVE: ONE operator sign-in under batch 88 item 3 | LEG_S_VERDICT by name with the redacted receipt -- or NOT RUN with P1's verdict | NOT RUN: P1 read LIVE. Sign-ins in this window 0; stored session LastChangedDate still 2026-10-01T08:21:20Z | CLOSED 20261001T155126Z |
| J1 | verify | one K4 POST and one K5 POST (two comparison keys) on a live session | root and solo gates clean; login 200; one upload POST and one submission POST; the request id and variant -- or NOT RUN | root and solo gates clean; login 200; ONE K4 POST 200 NORMALIZED 15:16:33Z; ONE K5 POST 200 QUEUED 15:16:39Z; REQ-a1d9abc0bc037ea3d9e4a7ed variant multicomp keys opal_short_term,opal_intermediate_term; 3 POSTs in the call log | CLOSED 20261001T155126Z |
| J2 | verify | the job's terminal state by name with EVERY receive quoted (time and status answer) | state and code; each READ_BACK line and redelivery interval; TOLERANCE_TYPE line; on READY the status-route read and the case trace; on a dead-letter the one redrive -- or NOT RUN | READY, report RPT-4acc921aa79afda98766192d4803f551. Receives: (1) 15:16:47Z status 200 calculating polls=1, READ_BACK_PENDING:CALCULATING, redelivered 122 s later; (2) 15:18:49Z step=template status=202, READ_BACK_PENDING:WAF_CHALLENGE, 900 s; (3) 15:33:55Z READ_BACK_DONE available, TOLERANCE_TYPE Static/Custom name=whole, handled 15:36:10Z. Status route READY with dates header; case trace 22 links 20 MATCH 0 MISMATCH. No dead-letter, no redrive | CLOSED 20261001T155126Z |
| J3 | verify | no residue | both queue depths; no second POST; sign-ins counted | irpt-generation 0/0 and irpt-generation-dlq 0/0 after the job; one K4 and one K5 POST only; sign-ins 0 | CLOSED 20261001T155126Z |

## Log

- 20261001T150402Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
- 20261001T155126Z LEG P1 closed: 15:15:41Z, SSM 0b606c2a-2a9d-4ec2-98ca-00e48817814e: root gate st9, solo gate clean; ONE GET of the report-template rout
- 20261001T155126Z LEG S1 closed: NOT RUN: P1 read LIVE. Sign-ins in this window 0; stored session LastChangedDate still 2026-10-01T08:21:20Z
- 20261001T155126Z LEG J1 closed: root and solo gates clean; login 200; ONE K4 POST 200 NORMALIZED 15:16:33Z; ONE K5 POST 200 QUEUED 15:16:39Z; REQ-a1d9ab
- 20261001T155126Z LEG J2 closed: READY, report RPT-4acc921aa79afda98766192d4803f551. Receives: (1) 15:16:47Z status 200 calculating polls=1, READ_BACK_PE
- 20261001T155126Z LEG J3 closed: irpt-generation 0/0 and irpt-generation-dlq 0/0 after the job; one K4 and one K5 POST only; sign-ins 0
- 20261001T155126Z CLOSED -- all 5 legs proven
