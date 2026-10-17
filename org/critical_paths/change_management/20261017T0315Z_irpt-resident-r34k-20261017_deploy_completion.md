# Deploy Completion Record
**Date opened:** 2026-10-17T03:15:49.237069+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T032103Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R34K (cell AR-g-160): resident release r34k on the resident host (base: the running r34h root): three new S3 objects under ec2/investor-reporting-ycharts/resident/, root /opt/irpt-resident/0485393f3a-r34k, five members changed and two added (lib on the service path, the estate-form price tier, the door checker at the T-1 frontier), one restart. Worktree union read 2026-10-17T03:1xZ: see the census line in the record; open entries naming the resident names: none other than closed, rolled-back or the laptop-device sovereign hold (nfra-trnspt-a18, an IAM role refusal, not the host, unit or keys).
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read on the resident host: running root r34h, the three changed code members at r34h values, the two added absent, r34k root absent, queue 0 0 | P1 STOP-READ-0 PASS and STOP-READ-2 PASS | pre_read_r34.sh (sha256 c0b37d5d equal) AS ROOT: STOP-READ-0 PASS running root r34h, the three changed members MATCH, the two added ABSENT, r34k root absent, library and wrapper unmoved, queue 0 0, sign-in baseline 0 | CLOSED 20261017T032102Z |
| D1 | s3-prefix | three r34k objects (tar, sums, host script) under ec2/investor-reporting-ycharts/resident/, each 404 first, uploaded and read back sha256 equal | VersionIds recorded | three r34k keys read 404 first; tar ozzC2C9ERYoK2o8FtLHkAD.eSNL5Nu9j, sums hEcmkLv0NSbjQ4q8TkASU.AGfUTs30i5, host script p26NH6jQ134nRRP7ymVEdlOKcry2btL1 uploaded from C:/dev/irpt-release-r34w and read back sha256 equal | CLOSED 20261017T032102Z |
| D2 | activation | signed install of r34k by install_r34.sh as root, one restart, rolls itself back on a failed start | install rc and output | install_r34.sh (sha256 d724f140 equal) AS ROOT: install rc=0 at 03:18:57Z, running root r34k active restarts 0, P2b 5 of 5 MATCH, sums 0 of 316 not OK, imports OK, queue 0 0, no sign-in | CLOSED 20261017T032102Z |
| V1 | verify | after-reads: root r34k active restarts 0, 5 of 5 members MATCH, 316 of 316 sums, census 5 changed 2 added 0 removed, imports, pool pinned, queue 0 0 | each line as written | running root r34k active; members 5 of 5 MATCH; sums 316 of 316; census package scope 5 changed 2 added 0 removed; pool pinned equal, pricing estate yfinance ycharts, budget 6 by 390, producer list unchanged; queue 0 0 | CLOSED 20261017T032102Z |
| V2 | verify | V2 read INSIDE the service environment: V2S OK SPY KEPT and ZQXWVK NOT_KEPT with the six sub-lines | V2 script rc 0 | v2_service_env_r34k.sh (sha256 7817cf8c equal) AS ROOT: rc 0; V2S OK SPY KEPT (HISTORY_ROWS 22 rows) and ZQXWVK NOT_KEPT (NO_ROWS); controls 4 of 4, backoff, door, pricing, budget, tier OK; service path carries lib | CLOSED 20261017T032103Z |

## Log

- 20261017T031549Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261017T032102Z LEG P1 closed: pre_read_r34.sh (sha256 c0b37d5d equal) AS ROOT: STOP-READ-0 PASS running root r34h, the three changed members MATCH, th
- 20261017T032102Z LEG D1 closed: three r34k keys read 404 first; tar ozzC2C9ERYoK2o8FtLHkAD.eSNL5Nu9j, sums hEcmkLv0NSbjQ4q8TkASU.AGfUTs30i5, host script
- 20261017T032102Z LEG D2 closed: install_r34.sh (sha256 d724f140 equal) AS ROOT: install rc=0 at 03:18:57Z, running root r34k active restarts 0, P2b 5 of
- 20261017T032102Z LEG V1 closed: running root r34k active; members 5 of 5 MATCH; sums 316 of 316; census package scope 5 changed 2 added 0 removed; pool 
- 20261017T032103Z LEG V2 closed: v2_service_env_r34k.sh (sha256 7817cf8c equal) AS ROOT: rc 0; V2S OK SPY KEPT (HISTORY_ROWS 22 rows) and ZQXWVK NOT_KEPT
- 20261017T032103Z CLOSED -- all 5 legs proven
