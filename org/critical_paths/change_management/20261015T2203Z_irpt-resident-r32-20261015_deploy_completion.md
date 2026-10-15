# Deploy Completion Record
**Date opened:** 2026-10-15T22:03:36.829193+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R32R (round 21, AR-g-97): resident r31 -> r32 on the resident host, leg R only: upload 3 keys, SSM pre-read, signed install (self-rollback on failed start), V1 after-reads and census; COO half blob 1c3023a9f1, CTO half msg 8693; tar sha256 3338a5c7...
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | SSM pre-read pre_read_r32.sh: running root r31, members at r31, added ABSENT, queue 0 0 | P1 STOP-READ-0 PASS and the printed table |  | OPEN |
| D1 | verify | upload tar, sums and host script to three keys (each 404 first), read back equal, record VersionIds | three sha256 equal and three VersionIds |  | OPEN |
| D2 | ec2-baked-asset | SSM install_r32.sh: running root r32 on the host | SSM output: running root and rc |  | OPEN |
| V1 | verify | after-reads: 25 members MATCH, sums 309 of 309, census 15 changed 11 added 0 removed, producer list, commentary x10 registered pricing off, queue 0 0 | the printed lines |  | OPEN |

## Log

- 20261015T220336Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 4 leg(s)
