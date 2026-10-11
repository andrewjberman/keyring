# Deploy Completion Record
**Date opened:** 2026-10-11T10:25:37.787670+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN TO-APPLY-st30: install the ONE resident release -- root 37210c771a-st30 over the running e606008994-st27 on host i-0167fd745ad906a66, one restart, and read it back. NO removal leg: st30 stays unless V1 fails or the issuer orders X1. Artifacts PINNED by measured sha256: tar 37210c771a-st30.tar.gz e5a6b6251b0e5e971cf73d785770965d4c2f407a6b4d79286508b50a853da241 (999816 bytes), installer resident_host_install_37210c771a-st30.sh dd85725806894839bd46fc66d990ba195f966862015a2983bb7bbbef0964b969 (8705 bytes), both EQUAL to the order's declared prefixes, measured locally before the put. GO: both never-widen halves signed at packet blob f81df64584 -- COO half @b0c75d2f04, CTO half @e2346b95f8 (CTO msg 4690); this seat verified the packet's working-tree blob EQUALS f81df64584 and that b0c75d2f04 is an ancestor of HEAD.
**Authored by:** 0.7.0_AE_CloudOps~YC2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | s3-prefix | put the tar as ec2/investor-reporting-ycharts/resident/irpt-resident-37210c771a-st30.tar.gz and resident_host_install_37210c771a-st30.sh under the same prefix in opal-313476888478-lambda-artifacts | each key 404 BEFORE the put with a positive control in the same bucket, then read each back and recompute sha256 EQUAL to the measured value above; a different sha256 is a STOP (a rebuilt tar is a new pair) |  | OPEN |
| P1 | verify | host_read.py pre_read.sh -- the read-only pre-read, expect st27 running | the output prints 'P1 STOP-READ PASS' (IRPT_ANALYSIS_READY_QUEUE_URL reads 0 in the unit Environment, the running process and the unit files); on FAIL install nothing, send 2.0.0_SA_COO~G2 the output path, stop |  | OPEN |
| D2 | activation | host_read.py install_st30.sh, ONLY when irpt-generation reads 0 visible and 0 in flight -- the installer's own gate is NEVER forced | running root 37210c771a-st30, active, 0 tracebacks; any failure takes the installer's own rollback to st27 then STOPS and reports |  | OPEN |
| V1 | verify | the install read-back | allow list ("andrew@opalinvest.com",); producer_for svc = YCHARTS; packaged research row firms = 3; request schema names ticket_id; READ_BACK_RELEASE_VISIBILITY_S = 390; both queue binding counts 0; the running process environment count 0 -- reported to 2.0.0_SA_COO~G2 as V1 closed |  | OPEN |

## Log

- 20261011T102537Z OPENED by 0.7.0_AE_CloudOps~YC2 with 4 leg(s)
