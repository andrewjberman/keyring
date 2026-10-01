# Deploy Completion Record
**Date opened:** 2026-10-01T07:25:49.234604+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T075344Z
**Deploy:** Hop 7 diagnostic: ONE Analysis attempt for Cottonwood under svc-irpt-analysis on the st6 resident (one upload, one Overview submission, no retry); the first capture on library 0fec0ca9
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| J1 | verify | one K4 POST and one K5 POST, both halves at HEAD first | the solo gate printed clean; login 200; exactly one upload POST and one submission POST in the scrubbed call log; the request id | solo gate clean (0 non-terminal, queue 0/0); login 200 at 07:33:14Z; ONE K4 POST 200 then NORMALIZED; ONE K5 POST 200 QUEUED REQ-742fc48185221dc5dec14e65; 3 POSTs in the scrubbed call log HOP7/H7_overview_cottonwood.json | CLOSED 20261001T075343Z |
| J2 | verify | the job's terminal state by name, with the resident journal | irpt-jobs state and code; every EVICTION and ATTENTION line of the span; capture library 0fec0ca9 (three added ctx.close sites) named beside the outcome; the receipt's vendor request shapes if READY | irpt-jobs state ATTENTION code SESSION_REFRESH_ALREADY_USED at 07:48:34Z; journal: EVICTION verdict=EVICTED 07:33:32Z, retained_for_retry CAPTURE_FAILED:AUTH_FAILED 07:33:52Z, EVICTION then ATTENTION 07:48:34Z; capture library 0fec0ca9, same signature as on dfc87d83 (09-30 03:36Z); not READY, no receipt; print HOP7/J2_OUTCOME_20261001.md | CLOSED 20261001T075343Z |
| J3 | verify | no residue | irpt-generation and its dead-letter queue depths after the attempt; no second POST made | irpt-generation 0/0 and irpt-generation-dlq 0/0 read after the terminal state; no second POST; irpt-jobs ATTENTION 11, READY 5, non-terminal 0 | CLOSED 20261001T075343Z |

## Log

- 20261001T072549Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
- 20261001T075343Z LEG J1 closed: solo gate clean (0 non-terminal, queue 0/0); login 200 at 07:33:14Z; ONE K4 POST 200 then NORMALIZED; ONE K5 POST 200 QU
- 20261001T075343Z LEG J2 closed: irpt-jobs state ATTENTION code SESSION_REFRESH_ALREADY_USED at 07:48:34Z; journal: EVICTION verdict=EVICTED 07:33:32Z, r
- 20261001T075343Z LEG J3 closed: irpt-generation 0/0 and irpt-generation-dlq 0/0 read after the terminal state; no second POST; irpt-jobs ATTENTION 11, R
- 20261001T075344Z CLOSED -- all 3 legs proven
