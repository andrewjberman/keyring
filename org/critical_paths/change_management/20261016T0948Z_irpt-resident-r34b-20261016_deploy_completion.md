# Deploy Completion Record
**Date opened:** 2026-10-16T09:48:30.644537+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R34C (AR-g-108): the resident r32 -> r34c under its own names (root 0485393f3a-r34c, tar 272d5c54..., 314 members 10 changed 4 added): P1 pre-read, D1 three new keys, D2 install_r34.sh, V1 after-reads, V2 Yahoo reads (SPY must read KEPT), V3 UpdateItem on irpt-jobs (must be allowed); library gate confirmed (ledger irpt-yf-pydeps-20261016 CLOSED, imports ok); COO half blob 6feb7b728c, CTO half b249e74f7a (msg 9138)
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | resident host running root 0485393f3a-r32 (pre_read_r34.sh) | P1 STOP-READ-0 PASS, queue 0 0 | pre_read_r34.sh (sha256 3fa24948... equal) by Systems Manager as ec2-user: P1 STOP-READ-0 PASS running root /opt/irpt-resident/0485393f3a-r32, unit active restarts 0; every changed member at its r32 value, every added member ABSENT; r34c root absent; library and wrapper are release 32; queue 0 0; producer list andrew@opalinvest.com and fwd1-staff-r41b@opal.invalid; no sign-in lines; library gate before it: yfinance 1.2.0 pandas 2.3.3 numpy 2.4.2 requests 2.32.5 import ok from pydeps | CLOSED 20261016T094923Z |
| D1 | s3-prefix | ec2/investor-reporting-ycharts/resident/ three r34c keys (tar, sums, host script) | three keys read 404 first, uploaded, read back sha256 equal, VersionIds | three r34c keys read 404 first; tar, sums, host script uploaded from the stage folder and read back by VersionId with sha256 equal (272d5c54..., 55d48fb6..., c7d165d8...); VersionIds wPL6V1T2w0MoZvOO9t2x.j2g2XqGcTfm, eitNfE.TIhIQzD.zNiBDDVRGfgPkfNJX, wx3zk9Kvvck_BhbQiiI6ALOHuY_pKb0x | CLOSED 20261016T094957Z |
| D2 | verify | resident host install (install_r34.sh) | install output, rc, running root r34c |  | OPEN |
| V1 | verify | after-reads: root, unit, 12 members MATCH, sums 313 of 313, census 10/4/0, imports, pool pin, producer list, queue | the printed reads |  | OPEN |
| V2 | verify | Yahoo reads: one yf.download and one YfinanceChecker for SPY | checker KEPT, pool loads |  | OPEN |
| V3 | verify | simulator read dynamodb:UpdateItem on irpt-jobs for the host role | allowed |  | OPEN |

## Log

- 20261016T094830Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 6 leg(s)
- 20261016T094923Z LEG P1 closed: pre_read_r34.sh (sha256 3fa24948... equal) by Systems Manager as ec2-user: P1 STOP-READ-0 PASS running root /opt/irpt-re
- 20261016T094957Z LEG D1 closed: three r34c keys read 404 first; tar, sums, host script uploaded from the stage folder and read back by VersionId with sh
