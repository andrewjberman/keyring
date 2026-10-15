# Deploy Completion Record
**Date opened:** 2026-10-15T06:22:53.629822+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R31R: install the resident release 31 (leg R) -- root 0485393f3a-r31 over the running 0485393f3a-r29 on host i-0167fd745ad906a66. 15 of 299 members differ (analysis_ready send, commentary_ready consume, packager attach wirings, acceptance.py; dormant until Andrew's act f61b); none added, none removed; capture library and wrapper NOT moved. Tar 22193944..., host script 6f559089..., package sums 4710d4ea.... Pair: COO half blob 8fb19a3356 (verified by hash-object), CTO half msg 7890. GO: COO~Y2 msg 8142 (legs L and A closed). NO removal leg; rollback_r31.sh not run without a new word. Rollback order R, A, L.
**Authored by:** 0.7.0_AE_CloudOps~YC2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | s3-prefix | put the tar, host script and package SHA256SUMS under ec2/investor-reporting-ycharts/resident/ in opal-313476888478-lambda-artifacts (3 new keys) | each key 404 before the put, read back with sha256 equal to the order's value; a different sha256 is a STOP |  | OPEN |
| P1 | verify | host_read.py pre_read_r31.sh -- read-only pre-read, expect r29 running and r31 absent, SIX STOPs | six PASS lines P1 STOP-READ-0, STOP-READ, -2, -3, -4, -5; any FAIL installs nothing |  | OPEN |
| D2 | activation | host_read.py install_r31.sh ONLY when irpt-generation reads 0 visible and 0 in flight | running root 0485393f3a-r31, active, 0 tracebacks, polls at least 1; any failure takes the installer's own rollback to r29, then STOP |  | OPEN |
| V1 | verify | the install read-back, every expectation of order step 7 plus V-R (U3, U4, U6 after) of step 8 | 15 members MATCH, sha256sum -c 0 of 298 not OK, producer list two entries, library and wrapper unmoved, r29 root present, no sign-in; queues 0, no DLQ grew, packager secret LastAccessedDate unchanged |  | OPEN |

## Log

- 20261015T062253Z OPENED by 0.7.0_AE_CloudOps~YC2 with 4 leg(s)
