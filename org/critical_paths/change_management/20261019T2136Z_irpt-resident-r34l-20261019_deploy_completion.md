# Deploy Completion Record
**Date opened:** 2026-10-19T21:36:09.958387+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R34L: resident r34k -> r34l (report sections without value dropped and counted; pricing as-of at the trading-calendar frontier)
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read: running root r34k, r34l root absent, queue 0 0 | P1 STOP-READ-0 PASS |  | OPEN |
| D1 | s3-prefix | three r34l keys under ec2/investor-reporting-ycharts/resident/ | three VersionIds read back equal |  | OPEN |
| D2 | activation | signed install on the resident host (root /opt/irpt-resident/0485393f3a-r34l) | install output, unit active restarts 0 |  | OPEN |
| V1 | verify | after-reads: members MATCH, sums 316 of 316, census 4 changed | printed counts |  | OPEN |
| V2 | verify | V2 inside the service environment | V2S OK SPY KEPT and ZQXWVK NOT_KEPT |  | OPEN |

## Log

- 20261019T213609Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
