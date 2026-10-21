# Deploy Completion Record
**Date opened:** 2026-10-21T14:22:25.579692+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T143127Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R34T: resident host r34s -> r34t (typed ETF priced, per-model dates, left-out line, risk tables, swap model leg)
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | pre-read: running root r34s, r34t root absent, queue 0 0 | P1 STOP-READ-0 PASS | P1 STOP-READ-0 PASS at 14:25:56Z (SSM 2d7b5146), r34s root running, r34t absent, queue 0 0 | CLOSED 20261021T143127Z |
| D1 | verify | three r34t keys uploaded under ec2/investor-reporting-ycharts/resident/ in opal-313476888478-lambda-artifacts | three VersionIds, read back equal | three keys uploaded 14:26Z and read back equal; VersionIds in A_AFTER_R34T.txt | CLOSED 20261021T143127Z |
| D2 | verify | install_r34.sh as root; running root becomes r34t | install rc 0, unit active, restarts 0 | install_r34.sh rc=0 at 14:27:19Z (SSM 9c544a52), running root r34t active restarts 0, 0 not OK of 324 | CLOSED 20261021T143127Z |
| V1 | verify | after-reads: members, sums, census, fix words, bindings, pool | V1 lines | members 9 of 9 MATCH, sums 324 of 324, census 9 changed 2 added 0 removed, fix words yes, bindings and pool as ordered | CLOSED 20261021T143127Z |
| V2 | verify | V2 script inside the service environment, V2S_WANT_ROOT r34t | V2S OK SPY KEPT and ZQXWVK NOT_KEPT | V2S OK SPY KEPT and ZQXWVK NOT_KEPT (SSM 0ac9e203, V2 script sha256 7817cf8c..., export V2S_WANT_ROOT=/opt/irpt-resident/0485393f3a-r34t, path conversion off); first send 14:28:14Z exited 62 on my path-mangled argument before any check; controls 4 of 4, backoff, door, pricing, budget, tier OK | CLOSED 20261021T143127Z |

## Log

- 20261021T142225Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261021T143127Z LEG P1 closed: P1 STOP-READ-0 PASS at 14:25:56Z (SSM 2d7b5146), r34s root running, r34t absent, queue 0 0
- 20261021T143127Z LEG D1 closed: three keys uploaded 14:26Z and read back equal; VersionIds in A_AFTER_R34T.txt
- 20261021T143127Z LEG D2 closed: install_r34.sh rc=0 at 14:27:19Z (SSM 9c544a52), running root r34t active restarts 0, 0 not OK of 324
- 20261021T143127Z LEG V1 closed: members 9 of 9 MATCH, sums 324 of 324, census 9 changed 2 added 0 removed, fix words yes, bindings and pool as ordered
- 20261021T143127Z LEG V2 closed: V2S OK SPY KEPT and ZQXWVK NOT_KEPT (SSM 0ac9e203, V2 script sha256 7817cf8c..., export V2S_WANT_ROOT=/opt/irpt-resident
- 20261021T143127Z CLOSED -- all 5 legs proven
