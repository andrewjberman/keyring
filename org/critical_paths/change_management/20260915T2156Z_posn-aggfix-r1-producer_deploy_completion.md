# Deploy Completion Record
**Date opened:** 2026-09-15T21:56:23.079484+00:00
**Status:** OPEN
**Deploy:** POSN_AGGFIX AF1-s-10: deploy yang-generate-positioning (current weights, Opal-only aggregate key); the shared key's other writers yang-time-machine and rollback-protocol.sh restore by prefix and are NOT invoked; residual row POSN_AGGFIX-Z-S2
**Authored by:** 0.9.0_WK_POSN_AGGFIX~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | SITEZ carries TO-A2-1's lambda_function.py | commit hash |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts yang-pipeline/yang-generate-positioning.zip | sha256 + VersionId |  | OPEN |
| L3 | verify | plan targeted to module.generate_positioning | 0 add 1 change 0 destroy |  | OPEN |
| L4 | activation | safe-apply | apply summary |  | OPEN |
| L5 | verify | 0-diff re-plan and deployed CodeSha256 | No changes + sha equal |  | OPEN |
| L6 | activation | driven generator invoke + invalidation on recorded events | VersionIds before and after |  | OPEN |
| L7 | verify | served reads, Branch A | five books non-aum identical, aum current, no AGG, new key OK |  | OPEN |
| L8 | git | record-terraform-deploy | commit hash |  | OPEN |

## Log

- 20260915T215623Z OPENED by 0.9.0_WK_POSN_AGGFIX~1 with 8 leg(s)
