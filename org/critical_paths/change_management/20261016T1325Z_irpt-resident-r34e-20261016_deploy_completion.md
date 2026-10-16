# Deploy Completion Record
**Date opened:** 2026-10-16T13:25:53.901099+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T133055Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R34E (AR-g-127): the resident r34c -> r34e, the symbol-404 rule (root 0485393f3a-r34e, tar a96fbfb7..., 314 members, 3 changed: intake/yfinance_check.py, SHA256SUMS, reports/resident_bindings.json): P1 pre-read, D1 three new keys, D2 install_r34.sh, V1 after-reads, V2 in the service's own environment (SPY KEPT, ZQXWVK NOT_KEPT and CONTROLS OK 4 of 4, else rollback to r34c); EVERY HOST SCRIPT SENT AS ROOT; COO half blob fd4c17188b, CTO half 5699c80f35 (msgs 9345 and 9354 conditions)
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | resident host running root 0485393f3a-r34c (pre_read_r34.sh, as root) | P1 STOP-READ-0 PASS, member at r34c value, r34e root absent, queue 0 0 | pre_read_r34.sh (sha256 a21079c9... equal) by Systems Manager AS ROOT: P1 STOP-READ-0 PASS running root /opt/irpt-resident/0485393f3a-r34c; intake/yfinance_check.py at its r34c value 343ab79c... MATCH; r34e root absent (STOP-READ-2 PASS); library and wrapper unmoved (3, 4 PASS); kept-copy path absent (5 PASS); queue 0 0; no sign-in lines; census 74 worktrees read, the only open entry naming a resident surface is my own held run-3 ledger irpt-fwd1-run3-20261016 (no host write; sequenced behind this ledger by the CTO); the r31, r34, r34b, r34d resident ledgers are terminal | CLOSED 20261016T132708Z |
| D1 | s3-prefix | ec2/investor-reporting-ycharts/resident/ three r34e keys (tar, sums, host script) | three keys read 404 first, uploaded, read back sha256 equal, VersionIds | three r34e keys read 404 first; tar, sums, host script uploaded from the stage folder C:/dev/irpt-release-r34h and read back by VersionId with sha256 equal (a96fbfb7..., faa98a0a..., 5b73c2fa...); VersionIds _mUTq5xhLjxWfPE7Ah2nMPEYc4YgvouU, NABW.idQCWVW1KzFNnV2O_8hjNFo6S4k, U30E3TmJ.ZV.ooUUIGXX2db6KzWJvD95 | CLOSED 20261016T132750Z |
| D2 | verify | resident host install (install_r34.sh, as root) | install output, rc, running root r34e | install_r34.sh (sha256 7d2886e3... equal) AS ROOT by Systems Manager: install 0485393f3a-r34e rc=0, running root r34e, MainPID 1104497, restarts 0, queue 0 0, stderr empty | CLOSED 20261016T133054Z |
| V1 | verify | after-reads: root, unit, 1 member MATCH, sums 313 of 313, census 3/0/0, imports, pool pin, pricing off, producer list, queue | the printed reads | running root r34e active restarts 0; P2b 1 of 1 MATCH (intake/yfinance_check.py 4df9b66c...); sums 313 of 313 (0 not OK); package-scope census 3 changed (SHA256SUMS, intake/yfinance_check.py, reports/resident_bindings.json) 0 only in r34e 0 only in r34c, library scope 0; imports ok; pool bf047533... pinned, opal_pricing false, producer list unchanged; queue 0 0; no sign-in lines | CLOSED 20261016T133055Z |
| V2 | verify | V2 in the service's own environment (v2_service_env_r34e.sh, as root) | V2S OK SPY KEPT and ZQXWVK NOT_KEPT and V2S CONTROLS OK 4 of 4 | v2_service_env_r34e.sh (sha256 32d52a15...d5ea6 equal to the signed packet, issuer msg 9379) AS ROOT in the service's own environment: SPY KEPT HISTORY_ROWS rows 22, ZQXWVK NOT_KEPT NO_ROWS; V2S CONTROLS OK 4 of 4; V2S OK SPY KEPT and ZQXWVK NOT_KEPT; transient unit rc=0, script rc 0; two Yahoo calls | CLOSED 20261016T133055Z |

## Log

- 20261016T132553Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 5 leg(s)
- 20261016T132708Z LEG P1 closed: pre_read_r34.sh (sha256 a21079c9... equal) by Systems Manager AS ROOT: P1 STOP-READ-0 PASS running root /opt/irpt-reside
- 20261016T132750Z LEG D1 closed: three r34e keys read 404 first; tar, sums, host script uploaded from the stage folder C:/dev/irpt-release-r34h and read 
- 20261016T133054Z LEG D2 closed: install_r34.sh (sha256 7d2886e3... equal) AS ROOT by Systems Manager: install 0485393f3a-r34e rc=0, running root r34e, M
- 20261016T133055Z LEG V1 closed: running root r34e active restarts 0; P2b 1 of 1 MATCH (intake/yfinance_check.py 4df9b66c...); sums 313 of 313 (0 not OK)
- 20261016T133055Z LEG V2 closed: v2_service_env_r34e.sh (sha256 32d52a15...d5ea6 equal to the signed packet, issuer msg 9379) AS ROOT in the service's ow
- 20261016T133055Z CLOSED -- all 5 legs proven
