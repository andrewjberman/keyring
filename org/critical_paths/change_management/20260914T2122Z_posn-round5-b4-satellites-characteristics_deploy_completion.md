# Deploy Completion Record
**Date opened:** 2026-09-14T21:22:07.408537+00:00
**Status:** OPEN
**Deploy:** POSN_ASTTAX B4: cot-satellites-characteristics-producer (new function)
**Authored by:** 0.9.0_WK_POSN_ASTTAX~20
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | SITEZ commit of producer + trigger + build_package + tf | hash | SITEZ branch wk-posn_asttax-5-20: code 7c90a973ae03e295b9b7846b66082331730fd2d9 (producer + trigger + build_package + tf, commit-gate 4 of 4 clean); record f2180794dfee96f02455c6ef03e4b6ef1286a93d (lambda-source-map.json, verified by git show --stat); record(2) 909e9783f3 (CHANGELOG entry + map re-escape + 3 rows). LOCAL on the worker branch, not pushed. | CLOSED 20260914T220114Z |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts cot-pipeline/cot-satellites-characteristics-producer.zip | sha256 | s3://opal-313476888478-lambda-artifacts/cot-pipeline/cot-satellites-characteristics-producer.zip VersionId sZ0o.m4CGbylNMV7KPN1oR9bgRZnlEml, 36184 bytes, Metadata content-sha256=6M4Co5N81OD/SxD+fS0/pzbByeBKeYaVh8z/kszV3Vk= (s3api head-object, read back after the put). Built from pin 7c90a973ae by build_package.py; 3 members + BUILD_MANIFEST at the repo-mirroring layout; a moving ref (--pin HEAD) REFUSED rc=1. | CLOSED 20260914T220114Z |
| L3 | verify | plan (new function + role + policies + rule + target + permission) | summary | terraform plan -target x8 -out C:/tmp/wk-posn-5-20/.scratch/b4.tfplan: 'Plan: 9 to add, 0 to change, 0 to destroy.' All nine named and all mine (role, 2 role policies, 1 attachment, event rule, event target, lambda permission, module lambda function, module log group). | CLOSED 20260914T220114Z |
| L4 | activation | safe-apply | summary | .tools/safe-apply.sh apply of that saved plan: 'Apply complete! Resources: 9 added, 0 changed, 0 destroyed.' HALT-GATE line: 'worker 0.9.0_WK_POSN_ASTTAX~20 has no inbox; scanning its issuer 2.0.0_SA_COO~Z'. comp-tagauthz PASSED (0 candidates overwrite an access-granting tag); tombstone-gate CLEAN on 9 creates against 7 tombstones. | CLOSED 20260914T220114Z |
| L5 | verify | 0-diff | No changes | terraform plan (UNSCOPED, whole cot-pipeline root): 'No changes. Your infrastructure matches the configuration.' DISCRIMINATING because the same unscoped plan was run BEFORE the .tf existed and also read 'No changes.' -- so the 9 adds landed exactly as configured and perturbed nothing else in the stack. | CLOSED 20260914T220114Z |
| L6 | verify | QA invocation lands characteristics.json | s3api head + content read | aws lambda invoke --payload {} -> StatusCode 200, no FunctionError, response rc=0 naming platinum/satellites/characteristics.json. s3api head-object on that key: 200, ContentLength 54825, VersionId rt61ogajZQy79meUlsY1X_mIdPngxJTZ. Body read back: 9 of 9 satellites' coverage pairs EQUAL the V4-AC3 local run, and the whole satellites block is identical. QA proof on demand, never production evidence. | CLOSED 20260914T220115Z |
| L7 | verify | schedule enabled with the function as target | describe-rule + list-targets | events describe-rule cot-satellites-characteristics-producer-daily: State ENABLED, ScheduleExpression cron(20 7 * * ? *). list-targets-by-rule: one target, id CotSatellitesCharacteristicsProducerDaily, arn arn:aws:lambda:us-east-1:313476888478:function:cot-satellites-characteristics-producer. | CLOSED 20260914T220115Z |
| L8 | verify | next scheduled 07:20Z fire lands organically (the negative arm; recorded by the COO) | head after the fire |  | OPEN |

## Log

- 20260914T212207Z OPENED by 0.9.0_WK_POSN_ASTTAX~20 with 8 leg(s)
- 20260914T220114Z LEG L1 closed: SITEZ branch wk-posn_asttax-5-20: code 7c90a973ae03e295b9b7846b66082331730fd2d9 (producer + trigger + build_package + tf
- 20260914T220114Z LEG L2 closed: s3://opal-313476888478-lambda-artifacts/cot-pipeline/cot-satellites-characteristics-producer.zip VersionId sZ0o.m4CGbylN
- 20260914T220114Z LEG L3 closed: terraform plan -target x8 -out C:/tmp/wk-posn-5-20/.scratch/b4.tfplan: 'Plan: 9 to add, 0 to change, 0 to destroy.' All 
- 20260914T220114Z LEG L4 closed: .tools/safe-apply.sh apply of that saved plan: 'Apply complete! Resources: 9 added, 0 changed, 0 destroyed.' HALT-GATE l
- 20260914T220114Z LEG L5 closed: terraform plan (UNSCOPED, whole cot-pipeline root): 'No changes. Your infrastructure matches the configuration.' DISCRIM
- 20260914T220115Z LEG L6 closed: aws lambda invoke --payload {} -> StatusCode 200, no FunctionError, response rc=0 naming platinum/satellites/characteris
- 20260914T220115Z LEG L7 closed: events describe-rule cot-satellites-characteristics-producer-daily: State ENABLED, ScheduleExpression cron(20 7 * * ? *)
