# Deploy Completion Record
**Date opened:** 2026-08-27T15:11:48.101669+00:00
**Status:** OPEN
**Deploy:** COT session-chain parity R1: restore cot-session-complete (SSM session-fetch Success -> bronze-run). Carries the Lever-A MINT leg, which terminates at the mint without it -- 2/2 mint days lost bronze since the 08-14 kill. Spec ctoZ_SPEC_COT_SESSION_CHAIN_PARITY_20260827, Andrew-direct.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | SITEZ commit of cot-pipeline/eventbridge.tf | commit hash + commit-gate clean (LOCAL, rides integration) |  | OPEN |
| L2 | activation | cot-session-complete rule+target+permission TF apply | safe-apply 3-add/0-change/0-destroy + 0-diff replan -detailed-exitcode rc=0 |  | OPEN |
| L3 | verify | A1 rule exists ENABLED with correct pattern+target | live aws events describe-rule + list-targets-by-rule output |  | OPEN |
| L4 | verify | A2 the rule ACTUALLY FIRES on a real session-fetch Success | CloudWatch: cot-bd-session-trigger re-invoked with mode=bronze-run and an opal-cot-bronze-run SSM dispatch |  | OPEN |
| L5 | verify | A3 NEGATIVE CONTROL: does NOT fire on non-Success or a different document | a real non-matching event occurred and the rule stayed silent WHILE the positive case fired -- must not pass by absence |  | OPEN |
| L6 | verify | A5 end-to-end: bronze lands after a mint | opal-data-cot forwardfill_v2 partition + _BRONZE_COMPLETE.json for the mint day |  | OPEN |
| L7 | verify | A6 no regression to the Lever-A skip leg | young-cookie session-refresh still logs Lever A SKIP and dispatches bronze directly (single-fire, no double bronze) |  | OPEN |

## Log

- 20260827T151148Z OPENED by 0.7.0_AE_CloudOps~Z with 7 leg(s)
