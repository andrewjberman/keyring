# Deploy Completion Record
**Date opened:** 2026-10-16T12:10:51.969382+00:00
**Status:** ROLLED-BACK -- r34d rolled back to r34c the same session (V2S FAIL: ZQXWVK read CHECK_FAILED EXCEPTION in the service's own environment; SPY KEPT); P1, D1, D2, V1 proven; nothing stranded; r34d root and its three S3 objects kept; closed per the ledger tool below (the tool wrote CLOSED; this line was set to ROLLED-BACK by hand as the order says). Tool line was: CLOSED -- nothing stranded -- closed 20261016T121811Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R34D (AR-g-123): the resident r34c -> r34d, the checker fix (root 0485393f3a-r34d, tar 9a088a5c..., 314 members, 3 changed: intake/yfinance_check.py, SHA256SUMS, reports/resident_bindings.json): P1 pre-read, D1 three new keys, D2 install_r34.sh, V1 after-reads, V2S in the service's own environment (SPY KEPT and ZQXWVK NOT_KEPT, else rollback to r34c); EVERY HOST SCRIPT SENT AS ROOT; COO half blob 60cf9b70bc, CTO half b8554e2112 (msg 9291 conditions)
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | resident host running root 0485393f3a-r34c (pre_read_r34.sh, as root) | P1 STOP-READ-0 PASS, member at r34c value, r34d root absent, queue 0 0 | pre_read_r34.sh (sha256 7769f373... equal) by Systems Manager AS ROOT: P1 STOP-READ-0 PASS running root /opt/irpt-resident/0485393f3a-r34c; intake/yfinance_check.py at its r34c value 343ab79c... MATCH; r34d root absent (STOP-READ-2 PASS); library and wrapper unmoved (3, 4 PASS); kept-copy path absent (5 PASS); queue 0 0; no sign-in lines; census: 73 worktrees read, the only open entry naming a resident surface is my own held run-3 ledger irpt-fwd1-run3-20261016 (no host write; the CTO sequences run 3 behind this ledger), the r31, r34 and r34b resident ledgers are terminal | CLOSED 20261016T121219Z |
| D1 | s3-prefix | ec2/investor-reporting-ycharts/resident/ three r34d keys (tar, sums, host script) | three keys read 404 first, uploaded, read back sha256 equal, VersionIds | three r34d keys read 404 first; tar, sums, host script uploaded from the stage folder C:/dev/irpt-release-r34g and read back by VersionId with sha256 equal (9a088a5c..., 9220275a..., 1a9e6c44...); VersionIds 3cIv32VVkycbrMIRGHl4YtydxEcHU2Vr, UL5SGK10g3j7xKz8_n8y3Fc1tW0zxadD, cMcZT1Y26IYE4LQgSC1dAeKxtaUA6ZDT | CLOSED 20261016T121249Z |
| D2 | verify | resident host install (install_r34.sh, as root) | install output, rc, running root r34d | install_r34.sh (sha256 6644430f... equal) AS ROOT by Systems Manager: install 0485393f3a-r34d rc=0, running root r34d, MainPID 1101395, restarts 0, factory OK, queue 0 0, stderr empty | CLOSED 20261016T121811Z |
| V1 | verify | after-reads: root, unit, 1 member MATCH, sums 313 of 313, census 3/0/0, imports, pool pin, pricing off, producer list, queue | the printed reads | running root r34d active restarts 0; P2b 1 of 1 MATCH (intake/yfinance_check.py b90c0426...); sums 313 of 313 (0 not OK); package-scope census 3 changed (SHA256SUMS, intake/yfinance_check.py, reports/resident_bindings.json) 0 only in r34d 0 only in r34c, library scope 0; imports ok; pool bf047533... pinned, opal_pricing false, producer list unchanged; queue 0 0; no sign-in lines | CLOSED 20261016T121811Z |
| V2 | verify | V2 in the service's own environment (v2_service_env_r34d.sh, as root) | V2S OK SPY KEPT and ZQXWVK NOT_KEPT | V2 FAILED (v2_service_env_r34d.sh sha256 90802b18... as root, command 46aae874-a210-45e3-ac88-d3b6cce77192): in the service's own environment SPY KEPT HISTORY_ROWS rows 22 but ZQXWVK CHECK_FAILED reason EXCEPTION (want NOT_KEPT NO_ROWS), script printed V2S FAIL, rc 1; ROLLED BACK the same session to r34c by rollback_r34.sh (sha256 56a484ad... as root, command cf611d15-75a1-4707-b3fc-9cb818a44c84): running root r34c, restarts 0, member at its r34c value, queue 0 0, no sign-in; r34d root and the three S3 objects kept | CLOSED 20261016T121811Z |

## Log

- 20261016T121051Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 5 leg(s)
- 20261016T121219Z LEG P1 closed: pre_read_r34.sh (sha256 7769f373... equal) by Systems Manager AS ROOT: P1 STOP-READ-0 PASS running root /opt/irpt-reside
- 20261016T121249Z LEG D1 closed: three r34d keys read 404 first; tar, sums, host script uploaded from the stage folder C:/dev/irpt-release-r34g and read 
- 20261016T121811Z LEG D2 closed: install_r34.sh (sha256 6644430f... equal) AS ROOT by Systems Manager: install 0485393f3a-r34d rc=0, running root r34d, M
- 20261016T121811Z LEG V1 closed: running root r34d active restarts 0; P2b 1 of 1 MATCH (intake/yfinance_check.py b90c0426...); sums 313 of 313 (0 not OK)
- 20261016T121811Z LEG V2 closed: V2 FAILED (v2_service_env_r34d.sh sha256 90802b18... as root, command 46aae874-a210-45e3-ac88-d3b6cce77192): in the serv
- 20261016T121811Z CLOSED -- all 5 legs proven
