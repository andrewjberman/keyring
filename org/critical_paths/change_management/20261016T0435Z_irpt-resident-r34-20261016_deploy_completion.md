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
| P1 | verify | SSM pre-read pre_read_r34.sh: running root r32, members at r32, added ABSENT, queue 0 0 | P1 STOP-READ-0 PASS and the printed table | SSM 416cf2e5-7d9f-41e5-8c2e-04d9669d0970 Success rc 0 at 04:36Z: P1 STOP-READ-0 PASS, running root r32 active since 22:08:32Z restarts 0; 6 changed members at their r32 values and 4 added members ABSENT (10 of 10 MATCH); producer list unchanged; unit and process free of IRPT_ANALYSIS_READY_QUEUE_URL; library and wrapper unmoved; r34 root and kept-copy path absent; queue 0 0; journal polls 3 tracebacks 0 | CLOSED 20261016T043728Z |
| D1 | verify | upload tar, sums and host script to three keys (each 404 first), read back equal, record VersionIds | three sha256 equal and three VersionIds | three keys each 404 first, uploaded from the stage folder irpt-release-r34c, each read back by download: tar sha256 861e6900... 1117483 bytes VersionId 4BBk39y8KL4tl.OzFnZDHkrwcJLTcxSn; sums sha256 d647a499... 34370 bytes VersionId JQPVyzC44QNFMZeVD3bV_8VxNy4RceAn; host script sha256 91d57fb6... 8641 bytes VersionId klFOM6bDxCtZ1a17EGo67BaNqpbElIE6 | CLOSED 20261016T043931Z |
| D2 | ec2-baked-asset | SSM install_r34.sh: running root r34 on the host | SSM output: running root and rc | SSM 36162a8a-8294-4e38-999d-93f473ac9573 Success rc 0, 04:39:31Z to 04:40:36Z: install script and sums fetched by key and sha256-verified on the host, guards read root r32 and unit env 0, queue 0 0 twice, factory OK, install 0485393f3a-r34 rc=0, 30 s poll polls 2 tracebacks 0, no rollback; running root /opt/irpt-resident/0485393f3a-r34 MainPID 1083614 restarts 0 ActiveEnterTimestamp 04:40:03Z | CLOSED 20261016T044142Z |
| V1 | verify | after-reads: 10 members MATCH, sums 313 of 313, census 8 changed 4 added 0 removed, pool pinned, pricing off, producer list unchanged, queue 0 0 | the printed lines | V1 04:40Z to 04:43Z (install output SSM 36162a8a-..., census SSM ce2f081b-6b09-4144-acec-13ba2506c5bf): running root r34 active restarts 0; member table 10 of 10 MATCH; sums 0 of 313 not OK; census r32 3784 r34 3788 files, 3776 identical, 8 differ, 4 only in r34, 0 only in r32 (pyc excluded, counted), names equal the packet's table; imports incl swap_pass yahoo_history_days yfinance_check resident_session exit 0, intake/yfinance_check.py present; pool file sha256 bf047533... equals binding opal_swap_pool; opal_pricing enabled false; bindings differ from r32 by opal_swap_pool and provenance only; producer list unchanged (andrew, r41b); queue 0 0; journal sign-in lines 0; r32 root and kept library present | CLOSED 20261016T044427Z |
| V2 | verify | Yahoo reads through the resident interpreter: one yf.download and one YfinanceChecker call for SPY (checker must read KEPT), pool loads | the printed V2 lines |  | OPEN |

## Log

- 20261016T043523Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 5 leg(s)
- 20261016T043728Z LEG P1 closed: SSM 416cf2e5-7d9f-41e5-8c2e-04d9669d0970 Success rc 0 at 04:36Z: P1 STOP-READ-0 PASS, running root r32 active since 22:0
- 20261016T043931Z LEG D1 closed: three keys each 404 first, uploaded from the stage folder irpt-release-r34c, each read back by download: tar sha256 861e
- 20261016T044142Z LEG D2 closed: SSM 36162a8a-8294-4e38-999d-93f473ac9573 Success rc 0, 04:39:31Z to 04:40:36Z: install script and sums fetched by key an
- 20261016T044427Z LEG V1 closed: V1 04:40Z to 04:43Z (install output SSM 36162a8a-..., census SSM ce2f081b-6b09-4144-acec-13ba2506c5bf): running root r34
