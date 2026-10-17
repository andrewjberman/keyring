# Deploy Completion Record
**Date opened:** 2026-10-17T02:04:45.850213+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R34J (cell AR-g-156): resident release r34j on the resident host (base: the running r34h root): three new S3 objects under ec2/investor-reporting-ycharts/resident/, root /opt/irpt-resident/0485393f3a-r34j, four members changed and two added (the estate-form price tier and the door checker at the T-1 frontier), one restart. Worktree union read 2026-10-17T02:0xZ: 101 worktrees, 2109 marker files, 6 naming the resident names: r31, r34b, r34e, yf-pydeps CLOSED, r34d ROLLED-BACK (terminal), nfra-trnspt-a18 HELD-SOVEREIGN-GATED (an IAM role refusal on the laptop device, not the host, unit or keys; not a stop); r34g, r34h and r34i closed or rolled back.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read on the resident host: running root r34h, the two changed code members at r34h values, the two added absent, r34j root absent, queue 0 0 | P1 STOP-READ-0 PASS and STOP-READ-2 PASS |  | OPEN |
| D1 | s3-prefix | three r34j objects (tar, sums, host script) under ec2/investor-reporting-ycharts/resident/, each 404 first, uploaded and read back sha256 equal | VersionIds recorded |  | OPEN |
| D2 | activation | signed install of r34j by install_r34.sh as root, one restart, rolls itself back on a failed start | install rc and output |  | OPEN |
| V1 | verify | after-reads: root r34j active restarts 0, 4 of 4 members MATCH, 316 of 316 sums, census 4 changed 2 added 0 removed, imports, pool pinned, queue 0 0 | each line as written |  | OPEN |
| V2 | verify | V2 read INSIDE the service environment: V2S OK SPY KEPT and ZQXWVK NOT_KEPT with the six sub-lines | V2 script rc 0 |  | OPEN |

## Log

- 20261017T020445Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
