# Deploy Completion Record
**Date opened:** 2026-09-15T21:56:23.079484+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260915T222532Z
**Deploy:** POSN_AGGFIX AF1-s-10: deploy yang-generate-positioning (current weights, Opal-only aggregate key); the shared key's other writers yang-time-machine and rollback-protocol.sh restore by prefix and are NOT invoked; residual row POSN_AGGFIX-Z-S2
**Authored by:** 0.9.0_WK_POSN_AGGFIX~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | SITEZ carries TO-A2-1's lambda_function.py | commit hash | SITEZ carries TO-A2-1's lambda_function.py at 166ca71b8558bd71ab72ce92e258951f01fc7634 (the only commit on the function directory since last_deployed_commit dbe34de7b0; git rev-list --count = 1); drained @1c71fb87be | CLOSED 20260915T221130Z |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts yang-pipeline/yang-generate-positioning.zip | sha256 + VersionId | s3://opal-313476888478-lambda-artifacts/yang-pipeline/yang-generate-positioning.zip VersionId LCmMHmpdHvv0P3FB76_anxuuors0CIlr (rollback, sha256 yCdQVNMOoSqvTvWIc+d3RjDqe7yy25dCs/h50Ge9K9s=) -> RKnw3YkTo8okvldCf3vrTbDtWejlJjzs sha256 riByGXEfWXdFTEavKGG0nFRj/k4JUAjIiVKfm06Tdgk= 36447 bytes, write verified (a3_ac3.attempt2.out.txt @84fe842e09) | CLOSED 20260915T221130Z |
| L3 | verify | plan targeted to module.generate_positioning | 0 add 1 change 0 destroy | terraform plan -target=module.generate_positioning: Plan: 0 to add, 1 to change, 0 to destroy; module.generate_positioning.aws_lambda_function.this updated in-place (s3_object_version, source_code_hash) (a3_ac4.out.txt @84fe842e09) | CLOSED 20260915T221130Z |
| L4 | activation | safe-apply | apply summary | safe-apply 2026-09-15T22:08:5xZ: HALT-GATE scanned issuer 2.0.0_SA_COO~Z, tagauthz and tombstone gates PASSED, Apply complete! Resources: 0 added, 1 changed, 0 destroyed. (a3_ac5.attempt1.out.txt) | CLOSED 20260915T221130Z |
| L5 | verify | 0-diff re-plan and deployed CodeSha256 | No changes + sha equal | terraform plan -target=module.generate_positioning 22:10:25Z: No changes. Your infrastructure matches the configuration. (a3_ac6.out.txt); get-function-configuration 22:10:52Z CodeSha256 riByGXEfWXdFTEavKGG0nFRj/k4JUAjIiVKfm06Tdgk= == uploaded artifact sha256, LastModified 2026-09-15T22:09:30Z (a3_ac7.out.txt) | CLOSED 20260915T221237Z |
| L6 | activation | driven generator invoke + invalidation on recorded events | VersionIds before and after | a3_drive_and_read.py 22:12:11Z on execution 20260914_v1-9dbd2129 (0 RUNNING): yang-generate-positioning invoked once with the recorded GeneratePositioning input (770 chars sha256 8879bc84...), StatusCode 200 no FunctionError; yang-invalidate-cloudfront invoked once with its recorded input, StatusCode 200 no FunctionError (EVTSA9VEHNZVH InProgress, E2LPCXXBLDGWXY NoSuchDistribution). json/positioning/positioning_data.json VersionId aJ7nhwRKko3H_AMRzsNvvwkf1NiO9aou -> dFjRdciig4Y.4DBiK_F0eyHtn1.YBCOC; json/positioning/opal_aggregate.json ABSENT -> M8FOApCmYnAQB_3946XGOHSeqEzcL2j.; other keys under json/positioning/ unchanged 2 of 2 (a3_ac8.out.txt) | CLOSED 20260915T221421Z |
| L7 | verify | served reads, Branch A | five books non-aum identical, aum current, no AGG, new key OK | a3_drive_and_read.py --read-only-compare 22:13:45Z, parsed JSON (key order ignored): current_holdings keys prior UST ST INT LT ULT AGG, new UST ST INT LT ULT; BOOK NON-AUM IDENTICAL 5 of 5; book aum EQUAL to its own platinum row at VersionId OVcFBOpgjFywfYJGYjowX2VSVwLdiyez 5 of 5; top-level identical (data_as_of, note, benchmarks, portfolios, data_date); opal_aggregate.json status OK, weights sum 1.0, max \|weight - members/members_sum\| 0; served delta 7 paths all permitted, 0 other keys moved; controls fired; BRANCH A (a3_ac9.out.txt). Satellites yang_index: out 30 and extra maps identical, conflicts difference empty (a3_ac10.out.txt) | CLOSED 20260915T221736Z |
| L8 | git | record-terraform-deploy | commit hash | record-terraform-deploy.sh 22:18:28Z (8.3 python3 path first on PATH): commit 04ee6921d823a88eeeea6b9f408f6809350a02e4 'ci: record deploy yang-pipeline @ 84fe842e [skip ci]', verified by git show --stat HEAD: 1 file, infra/aws/lambda/ci/lambda-source-map.json; parsed diff 3 of 2418 leaves, yang-generate-positioning last_deployed_commit dbe34de7b0 -> 166ca71b85 and last_deployed_at, plus _last_deploy_recorded; the CHANGELOG helper failed (SyntaxError, POSN_ASTTAX W23-S4) and the entry is written by hand in the follow-up commit (a3_ac11.out.txt) | CLOSED 20260915T222222Z |

## Log

- 20260915T215623Z OPENED by 0.9.0_WK_POSN_AGGFIX~1 with 8 leg(s)
- 20260915T221130Z LEG L1 closed: SITEZ carries TO-A2-1's lambda_function.py at 166ca71b8558bd71ab72ce92e258951f01fc7634 (the only commit on the function 
- 20260915T221130Z LEG L2 closed: s3://opal-313476888478-lambda-artifacts/yang-pipeline/yang-generate-positioning.zip VersionId LCmMHmpdHvv0P3FB76_anxuuor
- 20260915T221130Z LEG L3 closed: terraform plan -target=module.generate_positioning: Plan: 0 to add, 1 to change, 0 to destroy; module.generate_positioni
- 20260915T221130Z LEG L4 closed: safe-apply 2026-09-15T22:08:5xZ: HALT-GATE scanned issuer 2.0.0_SA_COO~Z, tagauthz and tombstone gates PASSED, Apply com
- 20260915T221237Z LEG L5 closed: terraform plan -target=module.generate_positioning 22:10:25Z: No changes. Your infrastructure matches the configuration.
- 20260915T221421Z LEG L6 closed: a3_drive_and_read.py 22:12:11Z on execution 20260914_v1-9dbd2129 (0 RUNNING): yang-generate-positioning invoked once wit
- 20260915T221736Z LEG L7 closed: a3_drive_and_read.py --read-only-compare 22:13:45Z, parsed JSON (key order ignored): current_holdings keys prior UST ST 
- 20260915T222222Z LEG L8 closed: record-terraform-deploy.sh 22:18:28Z (8.3 python3 path first on PATH): commit 04ee6921d823a88eeeea6b9f408f6809350a02e4 '
- 20260915T222532Z CLOSED -- all 8 legs proven
