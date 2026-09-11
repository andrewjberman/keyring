# Deploy Completion Record
**Date opened:** 2026-09-11T16:37:38.496983+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T170647Z
**Deploy:** IRPT_BCKEND IB-rt-7: the irpt-holdings Lambda and the api root's holdings route
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the IB-rt-7 source commit d9c940244a (handler, terraform root, contract flip, runner holdouts) | the commit hash is in the branch ancestry | source commit d9c940244a in the branch ancestry (handler, terraform root, contract flip with 153 insertions and 0 deletions, runner holdouts); sentinel commit 2f0cb688de committed BEFORE the act | CLOSED 20260911T170601Z |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-holdings.zip | head-object content-sha256 equals the built zip sha256 | build-and-upload.sh rc=0: import-closure ENFORCED (6 packaged .py, every top-level import satisfied) and index-gate ran-sentinel present (members=4 pin=2f0cb688de); zip sha256 yOiMCrewFEMtE6GCJzBjNdLQsRpliY8zrM3t1AMyynI= size 50073; S3 write VERIFIED, sha256 metadata match | CLOSED 20260911T170601Z |
| L3 | tf-lambda | module.irpt_holdings.aws_lambda_function.this in investor-reporting/holdings plus the route, integration and invoke permission in investor-reporting/api | safe-apply rc=0 on both roots | safe-apply rc=0 on holdings (Plan: 5 to add, 0 to change, 0 to destroy -- role, two policies, log group, function) and on api (Plan: 3 to add, 0 to change, 0 to destroy -- integration, route, invoke permission, every one keyed holdings; row W1-S15 records the third-line reading) | CLOSED 20260911T170601Z |
| L4 | verify | get-function-configuration CodeSha256, get-routes shows the holdings route under authorizer naqxlm, both roots plan No changes | every read taken AFTER the ledger is closed | get-function-configuration CodeSha256 yOiMCrewFEMtE6GCJzBjNdLQsRpliY8zrM3t1AMyynI= EQUALS the built zip by content; handler snapshot.lambda_handler, runtime python3.12, layer irpt-common:5, role irpt-holdings-role; get-routes shows GET /api/scoped/investor-reporting/holdings/{accountSetId} -> integrations/6ouz1v4 CUSTOM naqxlm; both roots plan No changes | CLOSED 20260911T170602Z |

## Log

- 20260911T163738Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 4 leg(s)
- 20260911T170601Z LEG L1 closed: source commit d9c940244a in the branch ancestry (handler, terraform root, contract flip with 153 insertions and 0 deleti
- 20260911T170601Z LEG L2 closed: build-and-upload.sh rc=0: import-closure ENFORCED (6 packaged .py, every top-level import satisfied) and index-gate ran-
- 20260911T170601Z LEG L3 closed: safe-apply rc=0 on holdings (Plan: 5 to add, 0 to change, 0 to destroy -- role, two policies, log group, function) and o
- 20260911T170602Z LEG L4 closed: get-function-configuration CodeSha256 yOiMCrewFEMtE6GCJzBjNdLQsRpliY8zrM3t1AMyynI= EQUALS the built zip by content; hand
- 20260911T170647Z CLOSED -- all 4 legs proven
