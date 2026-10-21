# Deploy Completion Record
**Date opened:** 2026-10-21T06:56:19.614354+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R34R: resident release 34r (S249 comparison-path fix, lead token, audit projection) on the resident host: three S3 objects, pre-read, signed install, after-reads, V2 inside the service environment
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read as root: running root r34q, r34r root absent, queue 0 0 | P1 STOP-READ-0 PASS |  | OPEN |
| D1 | activation | upload the tar, the sums file and the host script, each read back by VersionId equal | three keys uploaded and read back equal |  | OPEN |
| D2 | activation | signed install as root: r34r root installed, unit restarted, polled | install success line and running root r34r |  | OPEN |
| V1 | verify | after-reads: sums, census, fix, bindings, pool, imports, IRPT_TICKETS_TABLE word | V1 lines |  | OPEN |
| V2 | verify | V2 inside the service environment | V2S OK SPY KEPT and ZQXWVK NOT_KEPT |  | OPEN |

## Log

- 20261021T065619Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
