# Deploy Completion Record
**Date opened:** 2026-10-16T04:35:23.713411+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R34B (AR-g-108): resident r32 -> r34 on the resident host: upload 3 keys, SSM pre-read, signed install (self-rollback on a failed start), V1 after-reads and census, V2 Yahoo reads (one yf.download and one YfinanceChecker call, both SPY); COO half blob f787a4eabc, CTO half msg 9040; tar sha256 861e6900...
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | SSM pre-read pre_read_r34.sh: running root r32, members at r32, added ABSENT, queue 0 0 | P1 STOP-READ-0 PASS and the printed table |  | OPEN |
| D1 | verify | upload tar, sums and host script to three keys (each 404 first), read back equal, record VersionIds | three sha256 equal and three VersionIds |  | OPEN |
| D2 | ec2-baked-asset | SSM install_r34.sh: running root r34 on the host | SSM output: running root and rc |  | OPEN |
| V1 | verify | after-reads: 10 members MATCH, sums 313 of 313, census 8 changed 4 added 0 removed, pool pinned, pricing off, producer list unchanged, queue 0 0 | the printed lines |  | OPEN |
| V2 | verify | Yahoo reads through the resident interpreter: one yf.download and one YfinanceChecker call for SPY (checker must read KEPT), pool loads | the printed V2 lines |  | OPEN |

## Log

- 20261016T043523Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 5 leg(s)
