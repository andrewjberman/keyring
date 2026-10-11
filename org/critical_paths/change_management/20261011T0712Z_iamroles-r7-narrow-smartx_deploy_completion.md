# Deploy Completion Record
**Date opened:** 2026-10-11T07:12:14.393513+00:00
**Status:** OPEN
**Deploy:** NFRA_IAMROLES202609 IAM-x-2 PHASE B ACT 1: delete two dead inline policies off opal-smartx-lambda-role via the IAM API (A3-r7); no Terraform runs in smartx-pipeline
**Authored by:** 0.7.0_AE_CloudOps~IR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| DELETE | activation | opal-smartx-lambda-role inline opal-smartx-s3-access + opal-smartx-secrets | both delete-role-policy calls return rc=0, and AFTERWARDS list-role-policies reads EXACTLY ["opal-smartx-logs"] -- one name, not three. Rollback documents were committed BEFORE this leg at af85a44c38, each proven equal to a fresh live get-role-policy read |  | OPEN |
| READBACK | verify | opal-smartx-lambda-role | get-role-policy on each DELETED name reads NoSuchEntity, BESIDE A POSITIVE CONTROL: get-role-policy on opal-smartx-logs returns its document. Without that control a NoSuchEntity is indistinguishable from a broken call -- a failed retrieval returns a value |  | OPEN |
| UNTOUCHED | verify | opal-smartx-lambda-role | the role itself is unchanged: trust still lambda.amazonaws.com, the four round-6 tags still exactly Environment ManagedBy Project System=SmartXPipeline, path / and max_session_duration 3600, 0 attached managed policies. This is a NARROWING: nothing added, no trust or tag moves |  | OPEN |

## Log

- 20261011T071214Z OPENED by 0.7.0_AE_CloudOps~IR with 3 leg(s)
