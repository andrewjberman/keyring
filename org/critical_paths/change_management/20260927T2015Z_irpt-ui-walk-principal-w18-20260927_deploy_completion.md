# Deploy Completion Record
**Date opened:** 2026-09-27T20:15:32.346973+00:00
**Status:** OPEN
**Deploy:** Window 18: ~D round-8 read-only walk (DEV 3b98939b) + K7/K8 on the async export Ulim/gmf + ~Y's 4 identity reads on the resident session; walker ~D; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | both halves at HEAD naming the W18 blob; CRO walker DISARMED reported; pins re-read equal; pre-read + censuses; put + read-back |  | OPEN |
| K1C | verify | K1-CRED deleted after the login | ParameterNotFound |  | OPEN |
| K8 | verify | ONE export on the async path | POST QUEUED exr_ under 29 s (HAR); pointer BUILDING -> SUBMITTED with binding; receipt READY %PDF or named FAILED; grant/receipt name the caller; owner unchanged; exactly 2 invocations for the POST |  | OPEN |
| Y1 | verify | 4 identity reads | ONE SSM run of comparison_identity_read_20260927.sh: 4 statuses or a recorded stop; lease holder empty after; queue 0/0 before/after; evidence file sha256 |  | OPEN |
| D1 | verify | K1 delete after every job is terminal (<= 120 min) | failing consistent read |  | OPEN |
| A1 | verify | route audit + write trace | 0 outside the classes; writes traced; users == baseline; 0 new media; K1 absent |  | OPEN |

## Log

- 20260927T201532Z OPENED by 2.0.0_SA_COO~P with 6 leg(s)
