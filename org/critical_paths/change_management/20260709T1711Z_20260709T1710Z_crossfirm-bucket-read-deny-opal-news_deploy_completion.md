# Deploy Completion Record
**Date opened:** 2026-07-09T17:11:22.767646+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260709T171330Z
**Deploy:** NEVER#1 control: cross-firm bucket READ Deny on opal-news-lambda-role (AmazonS3ReadOnlyAccess grants s3:Get*/List* on * -- AWS-managed, invisible to any lint over our TF). Reach is unused: layer3 reads only opal-data-news-v2.
**Authored by:** 0.5.0_AE_OpalETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| tf-apply | verify | news-pipeline: create aws_iam_role_policy cross-firm-bucket-read-deny | apply + re-plan No changes | safe-apply: 1 added, 0 changed, 0 destroyed (aws_iam_role_policy.opal_news_cross_firm_bucket_read_deny). Post-apply drift plan: 'No changes.' | CLOSED 20260709T171329Z |
| exposure-closed | verify | s3:GetObject on opal-data-{bd,cot,inf} -> explicitDeny vs a 3/3 allowed pre-belt baseline + a discriminator | comp-denytest | comp-denytest --from-plan --baseline, rc=0 PASS. Change type DERIVED from the plan: a Deny-add -> expected explicitDeny (the inverse of an allow-removal's implicitDeny; the author declared nothing). 3/3 explicitDeny on s3:GetObject into opal-data-{bd,cot,inf}/gold/, against a pre-belt baseline recording all three as ALLOWED -- falsifiable. DISCRIMINATOR partners-lambda-role stays 'allowed' on the same three resources, proving the verdict is attributable to THIS belt and not to default-deny. Directly: GetObject opal-data-bd -> explicitDeny; ListBucket opal-data-cot -> explicitDeny. The Deny overrides AmazonS3ReadOnlyAccess, which is AWS-managed and therefore invisible to any grant-shape lint over our own terraform -- the same blind spot as SecretsManagerReadWrite (B1) and the unmanaged inline S3Access on lambda-execution-role. | CLOSED 20260709T171329Z |
| no-collateral | verify | s3:GetObject on opal-data-news-v2 (the ONE bucket layer3 reads) still allowed | simulate | s3:GetObject on opal-data-news-v2 -> ALLOWED (the ONE bucket opal-news-layer3-curation actually reads: S3_BUCKET env, get_object at lambda_function.py:327, grounded on the deployed artifact). secretsmanager:GetSecretValue on opal/openai/layer3-curation -> ALLOWED (B1's scoped grant untouched). SAFETY-CHECKED BEFORE AUTHORING: this role carries no sanctioned firm-bucket read to preserve (inline = cross-firm-secret-deny, invoke-trending-publisher, opal-news-secrets-read); layer3-bd-securities-read lives on lambda-execution-role, NOT here -- which is why a read-scoped Deny is safe here and would have been destructive there. BEHAVIOUR: opal-news-layer3-curation is LIVE (ran 2026-07-08 21:17Z), writes DynamoDB and invokes the portal publisher, so it is not safely invocable on demand; its next scheduled run is the behaviour proof. Capability proven now; behaviour NOT-YET-EXERCISED, stated rather than skipped. | CLOSED 20260709T171330Z |

## Log

- 20260709T171122Z OPENED by 0.5.0_AE_OpalETL with 3 leg(s)
- 20260709T171329Z LEG tf-apply closed: safe-apply: 1 added, 0 changed, 0 destroyed (aws_iam_role_policy.opal_news_cross_firm_bucket_read_deny). Post-apply drif
- 20260709T171329Z LEG exposure-closed closed: comp-denytest --from-plan --baseline, rc=0 PASS. Change type DERIVED from the plan: a Deny-add -> expected explicitDeny 
- 20260709T171330Z LEG no-collateral closed: s3:GetObject on opal-data-news-v2 -> ALLOWED (the ONE bucket opal-news-layer3-curation actually reads: S3_BUCKET env, ge
- 20260709T171330Z CLOSED -- all 3 legs proven
