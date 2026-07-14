# Deploy Completion Record
**Date opened:** 2026-07-14T07:11:55.710050+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260714T072301Z
**Deploy:** OPAL_ASSETS.C2 cot-map ruling apply: mirror cot row bronze/->forwardfill_v2/ + provenance rider (templates) + router read grant re-scope. Gated: CTO GO 070349Z on 59249227c. Expected plan 0/2/0.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of source-map artifact_sha256 bump (code already committed 59249227c) | hash pushed to origin/CLOUD | 4f516eae7 pushed to origin/CLOUD (742bd34a8..4f516eae7); source code itself already on CLOUD at gated 59249227c, tree==gate verified by empty git diff | CLOSED 20260714T071337Z |
| L2 | s3-prefix | mirror zip -> s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-ingest-mirror.zip | build-and-upload VERIFIED line (size+sha256 metadata head-object match) | build-and-upload.sh write VERIFIED: s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-ingest-mirror.zip size=8618 + content-sha256 metadata head-object match (fail-closed gate, not rc) | CLOSED 20260714T071337Z |
| L3 | activation | safe-apply infra/aws/terraform/opal-assets (router policy + mirror code) | 0-diff plan after apply + live CodeSha256 == planned | safe-apply of saved plan c2-cot-map-apply-fresh.tfplan (0/2/0: aws_iam_role_policy.router_read_sources + module.mirror.aws_lambda_function.this); post-apply plan = 'No changes' 0-diff; live get-function-configuration CodeSha256=VQ3Rw79KKqPDvOQeY0blyzclC9mFthmpektm0NA5vk4= == planned source_code_hash, LastUpdateStatus=Successful State=Active | CLOSED 20260714T072013Z |
| L4 | verify | Rule 22a IAM half: live get-role-policy + simulate x3 SEPARATE (forwardfill_v2 Allow / positive control isolated / cot bronze data key implicitDeny) | three simulate outputs + get-role-policy live read | Rule 22a battery, 4 SEPARATE invocations, one --resource-arns each, REAL keys: (1) TARGET cot/forwardfill_v2/allocations/ALLOCATIONS_DAILY_2026-04-22.xlsx GetObject=allowed; (2) POSITIVE CONTROL isolated inf/bronze/assets/2020-04-28.jsonl.gz GetObject=allowed; (3) DROPPED cot/bronze/2026-06-13/_BRONZE_COMPLETE.json GetObject=implicitDeny; (4) RIDER cot/code/bronze/templates/allocations.json GetObject=allowed (rail-checked marker logged). APPLIED truth: live get-role-policy shows cot={forwardfill_v2/*, code/bronze/templates/*} no bronze/*, inf bronze/* untouched, ListBucket conditions match prefixes. | CLOSED 20260714T072301Z |

## Log

- 20260714T071155Z OPENED by 0.7.0_AE_CloudOps with 4 leg(s)
- 20260714T071337Z LEG L1 closed: 4f516eae7 pushed to origin/CLOUD (742bd34a8..4f516eae7); source code itself already on CLOUD at gated 59249227c, tree==g
- 20260714T071337Z LEG L2 closed: build-and-upload.sh write VERIFIED: s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-ingest-mirror.zip si
- 20260714T072013Z LEG L3 closed: safe-apply of saved plan c2-cot-map-apply-fresh.tfplan (0/2/0: aws_iam_role_policy.router_read_sources + module.mirror.a
- 20260714T072301Z LEG L4 closed: Rule 22a battery, 4 SEPARATE invocations, one --resource-arns each, REAL keys: (1) TARGET cot/forwardfill_v2/allocations
- 20260714T072301Z CLOSED -- all 4 legs proven
