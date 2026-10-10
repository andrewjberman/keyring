# Deploy Completion Record
**Date opened:** 2026-10-10T13:40:12.598254+00:00
**Status:** OPEN
**Deploy:** ADHOC four approved AWS deletes on Andrew's verbatim per-item word (record @d02b5d81e1 rows 8-10, verified at the pin): T1 canonical-schwab-si2-schedule/tfstate, T2 opal-assets-absence/tfstate, T3 log group /aws/lambda/opal-assets-absence-check, T4 demand_state ETFS_RIVALS-HISTORY-OWED-DAILY/state.json; exact keys only, bytes saved and hashed before each delete
**Authored by:** 0.7.0_AE_CloudOps~CTL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| T1 | activation | delete s3://opal-313476888478-terraform-state/canonical-schwab-si2-schedule/tfstate | before read with size/ETag/VersionId, resources list EMPTY, no backend reader with denominator and positive control, bytes saved and hashed, delete-object on the exact key, absence read with a sibling 200 control |  | OPEN |
| T2 | activation | delete s3://opal-313476888478-terraform-state/opal-assets-absence/tfstate | same guards as T1 |  | OPEN |
| T3 | activation | delete CloudWatch log group /aws/lambda/opal-assets-absence-check | exact-name describe before, Lambda opal-assets-absence-check ResourceNotFound, metadata saved and hashed, delete-log-group on the exact name, exact-name describe 0 after with a sibling 1 control |  | OPEN |
| T4 | activation | delete s3://opal-data-assets/bloomberg/global/silver/demand_state/request=ETFS_RIVALS-HISTORY-OWED-DAILY/state.json | before read, no scheduled reader names the request id with denominator printed, bytes saved and hashed, delete-object on the exact key, absence read with a sibling 200 control |  | OPEN |

## Log

- 20261010T134012Z OPENED by 0.7.0_AE_CloudOps~CTL with 4 leg(s)
