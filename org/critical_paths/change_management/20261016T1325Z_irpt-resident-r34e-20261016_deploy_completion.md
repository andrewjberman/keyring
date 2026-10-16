# Deploy Completion Record
**Date opened:** 2026-10-16T13:25:53.901099+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R34E (AR-g-127): the resident r34c -> r34e, the symbol-404 rule (root 0485393f3a-r34e, tar a96fbfb7..., 314 members, 3 changed: intake/yfinance_check.py, SHA256SUMS, reports/resident_bindings.json): P1 pre-read, D1 three new keys, D2 install_r34.sh, V1 after-reads, V2 in the service's own environment (SPY KEPT, ZQXWVK NOT_KEPT and CONTROLS OK 4 of 4, else rollback to r34c); EVERY HOST SCRIPT SENT AS ROOT; COO half blob fd4c17188b, CTO half 5699c80f35 (msgs 9345 and 9354 conditions)
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | resident host running root 0485393f3a-r34c (pre_read_r34.sh, as root) | P1 STOP-READ-0 PASS, member at r34c value, r34e root absent, queue 0 0 |  | OPEN |
| D1 | s3-prefix | ec2/investor-reporting-ycharts/resident/ three r34e keys (tar, sums, host script) | three keys read 404 first, uploaded, read back sha256 equal, VersionIds |  | OPEN |
| D2 | verify | resident host install (install_r34.sh, as root) | install output, rc, running root r34e |  | OPEN |
| V1 | verify | after-reads: root, unit, 1 member MATCH, sums 313 of 313, census 3/0/0, imports, pool pin, pricing off, producer list, queue | the printed reads |  | OPEN |
| V2 | verify | V2 in the service's own environment (v2_service_env_r34e.sh, as root) | V2S OK SPY KEPT and ZQXWVK NOT_KEPT and V2S CONTROLS OK 4 of 4 |  | OPEN |

## Log

- 20261016T132553Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 5 leg(s)
