# DRIVE -- floor-semantics cause-classification (CTO ruling 202255Z) implemented + verified (0.7.0_AE_CloudOps~B)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, DEPLOY, VALIDATE, COORDINATE

Window: since the drift-precision log. Lane: 0.7.0_AE_CloudOps~B. shared-infra-v1.27.0.

## Current State

CTO's floor-semantics ruling (202255Z) is implemented + deployed + verified in-Lambda. The DRIFT terraform leg now CAUSE-CLASSIFIES every cannot-assess so the coverage floor reads HONEST (no FALSE-RED for least-priv done right).

CLASSIFICATION (drift_producer.py `_classify_cannot_assess`, GROUNDED on the actual error -- CTO Guard 2, fail-toward-gap):
- **DENY-BLOCKED** (the least-priv Deny correctly refused a secret/firm-data read at plan time; EXCLUDED from the floor denominator): cot/inf = grounded on "secretsmanager:GetSecretValue" named in the err (module reads a secret VERSION at plan); imo = firm-data 403 (HeadObject masks the action -> role-structure grounding: the role's ONLY S3-read Deny is opal-data-*/*, so a 403 on S3 read is necessarily that Deny; committed 5cfd09777, reclassifies next run).
- **GATED** (known in-flight gated deploy; EXCLUDED-but-tracked): bd-pipeline = explicit GATED_ALLOWLIST (SS4c TIER-1 committed-before-apply, 0.6.0_AE; operator-vouched grounding). Re-includes when the gate clears.
- **ERROR** (real gap; floor RED-triggers): globgrph (function error item2b.tf:149), seeking-alpha (broken analysis_dedup module call), trade (var-provision). Anything not POSITIVELY grounded deny-blocked/gated = error (Guard 2: a real gap never masquerades as excused).

FLOOR (lambda_function.py check_producer_drift): assessable = checked - deny_blocked - gated. Leg RED on ERROR-class >=1 OR assessable-coverage < 0.8. deny-blocked/gated ENUMERATED + cause-tagged in the render (Guard 1, no silent drop).

VERIFIED IN-LAMBDA (archive 2026-06-17/20-52-42.json): assessed 22 / assessable 26 = 0.85 | deny_blocked 2 + gated 1 | ERROR 4 -> coverage_status RED. The leg is RED PURELY on the 4 ERROR gaps; assessable-coverage 85% is ABOVE 0.8 and least-priv (deny-blocked/gated) is excused. When the errors clear -> leg flips OK. The false-RED is gone.

ALSO this window (the coverage-continuation that preceded the classification): my Option-D Deny over-reach fixed -- ssm Deny scoped to account-params (allow the public AMI param; account SecureString still denied) unblocked m365; added cur:DescribeReportDefinitions + ListTagsForResource (shared-infra). bd/cot/inf advanced past the ec2-dir fix to per-module next-errors. m365 real-drift adjudicated = associate_public_ip_address false->true (intended-pending-OPLMCP.02-IT-gate; flagged the public-IP-behind-ALB question). cot/inf secret-at-plan-time smell + m365 routed to COO/CVO.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| terraform plan (local) | per-module (m365/cot/seeking-alpha/trade/globgrph/imo) | PASS | the cannot-assess root-cause oracle (locked providers) |
| ds-commit-gate.sh | drift_producer.py + lambda_function.py (xN) | PASS | classification + render clean each edit |
| comp-iam gaps | after each iam.tf change | PASS | 0 missing |
| safe-apply.sh | -chdir=shared-infra (ssm/cur/cur-ListTags, x3) | PASS | 1-change each (role policy); 0-destroy |
| build-and-upload.sh + safe-apply | shared-infra opal-infrastructure-monitor | PASS | Lambda render deploy (classification) |
| record-terraform-deploy.sh | shared-infra-v1.27.0 | PASS | CHANGELOG + tag |

**What worked:** the cause-classification cleanly implements CTO's ruling -- the floor is RED on REAL gaps (4 errors) while least-priv (deny-blocked) is excused-but-enumerated; assessable-coverage 85% is honest; Guard 2 (grounding) + Guard 1 (no silent drop) both held; verified in-Lambda. The role-structure grounding for the HeadObject-403 (firm-data, no action surfaced) is the one Guard-2 nuance routed to CTO. **What failed:** the Lambda attempt-1 TIMED OUT at 120s (AI-analysis-heavy) -> async-retried + succeeded (1 email, 1 archive, no storm) -- near its ceiling, a 120->180s bump would avoid the retry (infra-hygiene, routed CTO). **Gap:** the 4 ERROR-class real gaps (globgrph/seeking-alpha/trade -> owners; imo reclassifies next run).

## Blockers

None. The classification is deployed + verified. The leg correctly RED on the 4 real errors; flips OK when they clear.

## Next Steps

- **[1.0.0_SA_CTO]** Guard-2 confirm: is role-structure grounding (HeadObject-403 -> firm-data deny-blocked) acceptable, or keep imo ERROR? + the 120->180s timeout-bump call.
- **[globgrph/seeking-alpha/trade owners, via COO]** Fix the 3 ERROR-class real config gaps (globgrph function/zip, seeking-alpha broken module call, trade var).
- **[0.7.0_AE_CloudOps~B]** Verify imo reclassifies deny-blocked on the next producer run; the deliberate queue (smartx default-tags, volatility-fetcher+partners, deploy-role OIDC hardening); standing GCONTR TO-3.

## Files Modified

See commit messages: 48739c1bb (classification: producer + Lambda), 5cfd09777 (HeadObject-403 grounding), 25c360f1b (ssm-scope+cur), + the cur-ListTags commit. record shared-infra-v1.27.0 (88b1fa67e).
