# Deploy Completion Record
**Date opened:** 2026-10-21T14:22:25.579692+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R34T: resident host r34s -> r34t (typed ETF priced, per-model dates, left-out line, risk tables, swap model leg)
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read: running root r34s, r34t root absent, queue 0 0 | P1 STOP-READ-0 PASS |  | OPEN |
| D1 | verify | three r34t keys uploaded under ec2/investor-reporting-ycharts/resident/ in opal-313476888478-lambda-artifacts | three VersionIds, read back equal |  | OPEN |
| D2 | verify | install_r34.sh as root; running root becomes r34t | install rc 0, unit active, restarts 0 |  | OPEN |
| V1 | verify | after-reads: members, sums, census, fix words, bindings, pool | V1 lines |  | OPEN |
| V2 | verify | V2 script inside the service environment, V2S_WANT_ROOT r34t | V2S OK SPY KEPT and ZQXWVK NOT_KEPT |  | OPEN |

## Log

- 20261021T142225Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
