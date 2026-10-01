# Deploy Completion Record
**Date opened:** 2026-10-01T07:25:49.234604+00:00
**Status:** OPEN
**Deploy:** Hop 7 diagnostic: ONE Analysis attempt for Cottonwood under svc-irpt-analysis on the st6 resident (one upload, one Overview submission, no retry); the first capture on library 0fec0ca9
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| J1 | verify | one K4 POST and one K5 POST, both halves at HEAD first | the solo gate printed clean; login 200; exactly one upload POST and one submission POST in the scrubbed call log; the request id |  | OPEN |
| J2 | verify | the job's terminal state by name, with the resident journal | irpt-jobs state and code; every EVICTION and ATTENTION line of the span; capture library 0fec0ca9 (three added ctx.close sites) named beside the outcome; the receipt's vendor request shapes if READY |  | OPEN |
| J3 | verify | no residue | irpt-generation and its dead-letter queue depths after the attempt; no second POST made |  | OPEN |

## Log

- 20261001T072549Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
