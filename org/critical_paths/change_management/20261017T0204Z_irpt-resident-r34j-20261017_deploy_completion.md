# Deploy Completion Record
**Date opened:** 2026-10-17T02:04:45.850213+00:00
**Status:** ROLLED-BACK -- r34j rolled back to r34h the same session (V2S FAIL: SPY read CHECK_FAILED EXCEPTION in the service's own environment, not reproduced on the second ask); P1, D1, D2, V1 proven; nothing stranded; r34j root and its three S3 objects kept; closed 20261017T021047Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R34J (cell AR-g-156): resident release r34j on the resident host (base: the running r34h root): three new S3 objects under ec2/investor-reporting-ycharts/resident/, root /opt/irpt-resident/0485393f3a-r34j, four members changed and two added (the estate-form price tier and the door checker at the T-1 frontier), one restart. Worktree union read 2026-10-17T02:0xZ: 101 worktrees, 2109 marker files, 6 naming the resident names: r31, r34b, r34e, yf-pydeps CLOSED, r34d ROLLED-BACK (terminal), nfra-trnspt-a18 HELD-SOVEREIGN-GATED (an IAM role refusal on the laptop device, not the host, unit or keys; not a stop); r34g, r34h and r34i closed or rolled back.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read on the resident host: running root r34h, the two changed code members at r34h values, the two added absent, r34j root absent, queue 0 0 | P1 STOP-READ-0 PASS and STOP-READ-2 PASS | pre_read_r34.sh (sha256 65a7f234 equal) AS ROOT: STOP-READ-0 PASS running root r34h, the two changed members MATCH, the two added ABSENT, r34j root absent, library and wrapper unmoved, queue 0 0, sign-in baseline 0 | CLOSED 20261017T021046Z |
| D1 | s3-prefix | three r34j objects (tar, sums, host script) under ec2/investor-reporting-ycharts/resident/, each 404 first, uploaded and read back sha256 equal | VersionIds recorded | three r34j keys read 404 first; tar nvKQTRJyCuDB.3HTwqvgNG3NVqgHH6xM, sums PM9ULTE279ZCO7GREOcF1gffvuwRWuvi, host script wj1JM.ioWmblbT90bVCfY4W0tBeVfA.C uploaded from C:/dev/irpt-release-r34u and read back sha256 equal | CLOSED 20261017T021047Z |
| D2 | activation | signed install of r34j by install_r34.sh as root, one restart, rolls itself back on a failed start | install rc and output | install_r34.sh (sha256 191d34cd equal) AS ROOT: install rc=0 at 02:07:04Z, running root r34j active restarts 0, P2b 4 of 4 MATCH, sums 0 of 316 not OK, imports OK, queue 0 0, no sign-in | CLOSED 20261017T021047Z |
| V1 | verify | after-reads: root r34j active restarts 0, 4 of 4 members MATCH, 316 of 316 sums, census 4 changed 2 added 0 removed, imports, pool pinned, queue 0 0 | each line as written | running root r34j active; members 4 of 4 MATCH; sums 316 of 316; census package scope 4 changed 2 added 0 removed; pool pinned equal, pricing estate yfinance ycharts, budget 6 by 390, producer list unchanged; queue 0 0 | CLOSED 20261017T021047Z |
| V2 | verify | V2 read INSIDE the service environment: V2S OK SPY KEPT and ZQXWVK NOT_KEPT with the six sub-lines | V2 script rc 0 | V2 FAILED (v2_service_env_r34j.sh sha256 f2ac6e5b equal, AS ROOT): six sub-lines OK but SPY CHECK_FAILED EXCEPTION (0 rows; not reproduced on the second ask) so V2S FAIL, rc 1; ROLLED BACK the same session: rollback_r34.sh rc 0, r34h running since 02:08:47Z restarts 0, members at P1 values, queue 0 0, no sign-in; r34j root and three S3 objects kept | CLOSED 20261017T021047Z |

## Log

- 20261017T020445Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261017T021046Z LEG P1 closed: pre_read_r34.sh (sha256 65a7f234 equal) AS ROOT: STOP-READ-0 PASS running root r34h, the two changed members MATCH, the 
- 20261017T021047Z LEG D1 closed: three r34j keys read 404 first; tar nvKQTRJyCuDB.3HTwqvgNG3NVqgHH6xM, sums PM9ULTE279ZCO7GREOcF1gffvuwRWuvi, host script
- 20261017T021047Z LEG D2 closed: install_r34.sh (sha256 191d34cd equal) AS ROOT: install rc=0 at 02:07:04Z, running root r34j active restarts 0, P2b 4 of
- 20261017T021047Z LEG V1 closed: running root r34j active; members 4 of 4 MATCH; sums 316 of 316; census package scope 4 changed 2 added 0 removed; pool 
- 20261017T021047Z LEG V2 closed: V2 FAILED (v2_service_env_r34j.sh sha256 f2ac6e5b equal, AS ROOT): six sub-lines OK but SPY CHECK_FAILED EXCEPTION (0 ro
- 20261017T021047Z CLOSED -- all 5 legs proven
