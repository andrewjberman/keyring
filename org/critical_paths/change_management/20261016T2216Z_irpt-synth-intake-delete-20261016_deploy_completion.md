# Deploy Completion Record
**Date opened:** 2026-10-16T22:16:23.939366+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T221751Z
**Deploy:** IRPT_ANLREQ TO-DELETE-SYNTH-INTAKE (AR-y-376): delete 24 named fabric-made synthetic object versions in opal-data-irpt (FWD-1 probe sets, SET2, SET3 and RUN of run 3: 16; the release-33 sitting normalized_portfolios: 8), each by its listed key AND VersionId, head-read first and read back absent; authority: Andrew-direct standing word recorded by the CTO @c2b2f1e950 (synthetic and test files deletable any time, by listed key and VersionId); NO prefix delete, NO listing-driven delete, NO retry on AccessDenied; the r29 sitting's 6 objects and window 4 (0 objects) are not in this order; no overlap read between the 24 ART ids and the synthetic ticket or job (0 of 2)
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P | activation | the 16 run-3 rows (probe set 1: 5, SET2: 5, SET3: 5, RUN: 1) deleted by VersionId and read back absent | DEL lines ABSENT | BLOCKED, not done: the FIRST delete of the 24 (a run-3 probe-set row) returned AccessDenied; per the order nothing else was attempted; the version still reads present by head-object by key and VersionId with a positive control; failures written in A_DELETE_SYNTH.txt (DEL_TOTAL deleted=0 failed=24); the issuer routes the act to the laptop seat | CLOSED 20261016T221751Z |
| Q | activation | the 8 release-33 rows (normalized_portfolios) deleted by VersionId and read back absent | DEL lines ABSENT | BLOCKED, not done: not attempted after the first AccessDenied (the order stops); the 8 release-33 rows still present; failure lines written | CLOSED 20261016T221751Z |

## Log

- 20261016T221623Z OPENED by 0.7.0_AE_CloudOps~IB2 with 2 leg(s)
- 20261016T221751Z LEG P closed: BLOCKED, not done: the FIRST delete of the 24 (a run-3 probe-set row) returned AccessDenied; per the order nothing else 
- 20261016T221751Z LEG Q closed: BLOCKED, not done: not attempted after the first AccessDenied (the order stops); the 8 release-33 rows still present; fa
- 20261016T221751Z CLOSED -- all 2 legs proven
