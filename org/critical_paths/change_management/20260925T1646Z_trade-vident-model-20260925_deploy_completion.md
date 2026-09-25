# Deploy Completion Record
**Date opened:** 2026-09-25T16:46:45.611867+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260925T165001Z
**Deploy:** trade-submission-handler stores an uploaded Vident model as-is (model_securities passthrough), @1aabca225a
**Authored by:** 1.0.0_SA_CTO
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | build-and-upload trade-pipeline trade-submission-handler | artifact content-sha256 | s3://opal-313476888478-lambda-artifacts/trade-pipeline/trade-submission-handler.zip 16:47:09Z content-sha256 eBRFcOa5CD+ZoGxu/6K9xjxt/ylHevKebEUqk7qRWuc= version 70Nf7H.J4e53jcfQT38uCK0SaLE4EBa5 (prior HHauZny3.. / cbPIaGVV..) | CLOSED 20260925T164806Z |
| L2 | activation | safe-apply -target aws_lambda_function.trade_submission_handler | apply output + CodeSha256 | safe-apply -target aws_lambda_function.trade_submission_handler: 0 added, 1 changed; live CodeSha256 eBRFcOa5CD+ZoGxu/6K9xjxt/ylHevKebEUqk7qRWuc= (= artifact content-sha256) 16:48:50Z Successful; rollback = prior s3_object_version cbPIaGVVFepqVG0Hyzx2IlZEh6mIWXO. (sha HHauZny3..) | CLOSED 20260925T165001Z |
| L3 | verify | re-plan no changes + legacy submit path unchanged (invoke 400 on bad model) | plan + invoke output | re-plan -target: No changes; invoke with model_securities target_weight 1.5 -> 400 'model_securities row 1 (X) target_weight 1.5 ... outside [0, 1]' (new validation, nothing written) | CLOSED 20260925T165001Z |

## Log

- 20260925T164645Z OPENED by 1.0.0_SA_CTO with 3 leg(s)
- 20260925T164806Z LEG L1 closed: s3://opal-313476888478-lambda-artifacts/trade-pipeline/trade-submission-handler.zip 16:47:09Z content-sha256 eBRFcOa5CD+
- 20260925T165001Z LEG L2 closed: safe-apply -target aws_lambda_function.trade_submission_handler: 0 added, 1 changed; live CodeSha256 eBRFcOa5CD+ZoGxu/6K
- 20260925T165001Z LEG L3 closed: re-plan -target: No changes; invoke with model_securities target_weight 1.5 -> 400 'model_securities row 1 (X) target_we
- 20260925T165001Z CLOSED -- all 3 legs proven
