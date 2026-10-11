# Deploy Completion Record
**Date opened:** 2026-10-11T07:12:14.393513+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T071811Z
**Deploy:** NFRA_IAMROLES202609 IAM-x-2 PHASE B ACT 1: delete two dead inline policies off opal-smartx-lambda-role via the IAM API (A3-r7); no Terraform runs in smartx-pipeline
**Authored by:** 0.7.0_AE_CloudOps~IR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| DELETE | activation | opal-smartx-lambda-role inline opal-smartx-s3-access + opal-smartx-secrets | both delete-role-policy calls return rc=0, and AFTERWARDS list-role-policies reads EXACTLY ["opal-smartx-logs"] -- one name, not three. Rollback documents were committed BEFORE this leg at af85a44c38, each proven equal to a fresh live get-role-policy read | Both aws iam delete-role-policy calls returned rc=0, and list-role-policies moved from 3 names to EXACTLY 1: before ["opal-smartx-logs","opal-smartx-s3-access","opal-smartx-secrets"], after ["opal-smartx-logs"]. The two removed statements were the dead grants: opal-smartx-s3-access granted s3:GetObject+s3:ListBucket on opal-data-smartx and opal-code-smartx and their key patterns, ALL FOUR reading 404 re-confirmed at the act; opal-smartx-secrets granted secretsmanager:GetSecretValue on a us-east-2 ARN whose region holds 0 secrets. Target 1 was the only REAL squatting hazard in the round-7 set: an S3 bucket name is global, so that Allow would have granted read to whoever created either bucket name in any account. ROLLBACK DOCUMENTS WERE COMMITTED BEFORE THIS LEG at af85a44c38, each proven equal to a FRESH live get-role-policy read (compared canonically against a re-fetch into a scratch path, not against the file being written). No Terraform ran in smartx-pipeline, so the three Z-S21 Lambda drifts could not ride this act. | CLOSED 20261011T071810Z |
| READBACK | verify | opal-smartx-lambda-role | get-role-policy on each DELETED name reads NoSuchEntity, BESIDE A POSITIVE CONTROL: get-role-policy on opal-smartx-logs returns its document. Without that control a NoSuchEntity is indistinguishable from a broken call -- a failed retrieval returns a value | get-role-policy on each deleted name returns rc=254 NoSuchEntity -- opal-smartx-s3-access and opal-smartx-secrets. THE POSITIVE CONTROL IS WHAT MAKES THOSE READINGS MEAN ANYTHING, and it was run on the same call shape against the policy that must survive: get-role-policy on opal-smartx-logs returned rc=0 and its document, 1 statement. Without it a NoSuchEntity is indistinguishable from a call that cannot reach IAM at all -- a failed retrieval returns a value. So the absence is a fact about those two policies, not about the instrument. | CLOSED 20261011T071810Z |
| UNTOUCHED | verify | opal-smartx-lambda-role | the role itself is unchanged: trust still lambda.amazonaws.com, the four round-6 tags still exactly Environment ManagedBy Project System=SmartXPipeline, path / and max_session_duration 3600, 0 attached managed policies. This is a NARROWING: nothing added, no trust or tag moves | The role is unchanged, read live after both deletes: trust principal still {"Service":"lambda.amazonaws.com"}, path /, max_session_duration 3600, PermissionsBoundary None, description still "Lambda role for SmartX query functions", 0 attached managed policies, and list-role-tags returns EXACTLY the four round-6 tags Environment=Production ManagedBy=Terraform Project=OpalPortal System=SmartXPipeline. This was a NARROWING: two grants left, nothing was added, and no trust or tag moved. The surviving inline policy opal-smartx-logs is byte-intact (it returned its document as the control above). | CLOSED 20261011T071811Z |

## Log

- 20261011T071214Z OPENED by 0.7.0_AE_CloudOps~IR with 3 leg(s)
- 20261011T071810Z LEG DELETE closed: Both aws iam delete-role-policy calls returned rc=0, and list-role-policies moved from 3 names to EXACTLY 1: before ["op
- 20261011T071810Z LEG READBACK closed: get-role-policy on each deleted name returns rc=254 NoSuchEntity -- opal-smartx-s3-access and opal-smartx-secrets. THE P
- 20261011T071811Z LEG UNTOUCHED closed: The role is unchanged, read live after both deletes: trust principal still {"Service":"lambda.amazonaws.com"}, path /, m
- 20261011T071811Z CLOSED -- all 3 legs proven
