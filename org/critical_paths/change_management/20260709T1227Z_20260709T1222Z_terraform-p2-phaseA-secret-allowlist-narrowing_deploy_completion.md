# Deploy Completion Record
**Date opened:** 2026-07-09T12:27:07.319943+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / behaviour-output: the SEV1 login-path exercise is NOT PROVABLE by black-box invoke. index.ts:113-118 authenticateRequest does 'try { verifyAccessToken } catch { return null }' -- it SWALLOWS a secret-read failure and returns 401 Unauthorized, indistinguishable from an invalid token, with NO log line. So my /auth/me 401 + FunctionError=None is NOT a discriminating signal, and 45min of real traffic showing 0 AccessDenied is absence-of-evidence, not evidence. What WOULD prove it: one valid credential (a real login -> 200). Requesting a canary credential from CTO/COO. Capability is proven (post-apply live simulate: both jwt secrets allowed, dropped prefixes implicitDeny); only the behaviour leg is held. (held since 2026-07-09T12:54:16.520555+00:00)
**Deploy:** Phase A: narrow 4 opal/* secret wildcards to exact-suffix allowlists (opal-portal, news-ingestion, yang-pipeline, opalinvest-auth [SEV1 login, applied LAST, rollback armed])
**Authored by:** 0.5.0_AE_OpalETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| tf-shared-infra | verify | opal-portal-lambda-role SecretsManagerAccess -> 3 exact ARNs | re-plan No changes + live get-role-policy | apply: 0 added, 1 changed, 0 destroyed (aws_iam_role_policy.secretsmanageraccess). Post-apply drift plan: No changes. Live get-role-policy: SecretsManagerAccess now names 3 exact-suffix us-east-1 ARNs. | CLOSED 20260709T125313Z |
| tf-news-pipeline | verify | news-ingestion-lambda-role NewsIngestionPolicy -> 2 exact ARNs, account pinned | re-plan No changes + live | apply: 0/1/0 (news_ingestion_policy). Drift plan: No changes. Account wildcard removed (was arn:...:us-east-1:*:secret:opal/*); us-east-2 dropped (zero secrets exist there). | CLOSED 20260709T125314Z |
| tf-yang-pipeline | verify | yang-pipeline-lambda-role GetOpalSecrets -> 1 exact ARN us-east-2 client-aligned | re-plan No changes + live | apply: 0/1/0 (lambda_permissions). Drift plan: No changes. GetOpalSecrets narrowed to the single us-east-2 ARN its client actually targets; zero functional change (the secret is absent there -- a separate, filed, LATENT bug). | CLOSED 20260709T125314Z |
| tf-portal-auth-SEV1 | verify | opalinvest-auth-lambda-role -> 4 exact ARNs. LOGIN PATH. Applied LAST rollback armed. | re-plan No changes + live + real auth flow | APPLIED LAST, rollback armed and VALIDATED before apply (captured 4-statement PolicyDocument, put-role-policy command staged). apply: 0/1/0 (auth_permissions). Drift plan: No changes. | CLOSED 20260709T125315Z |
| verify-dropped | verify | two-exercise leg 1 dropped prefixes implicitDeny vs pre-apply allowed baseline all 4 roles | comp-denytest output | TWO-EXERCISE leg 1 PASS, all 4 roles. Each dropped prefix was 'allowed' PRE-apply (baseline captured, so the negative is falsifiable) and is implicitDeny POST-apply: opal-portal->opal/smartx/qa-models; news-ingestion->opal/smartx/config; yang->us-east-2 opal/smartx/config-*; opalinvest-auth->opal/external-apis AND opal/smartx/config. | CLOSED 20260709T125316Z |
| verify-kept | verify | two-exercise leg 2 kept prefixes still allowed via also-allowed with explicit GetSecretValue action all 4 roles | comp-denytest output | TWO-EXERCISE leg 2 PASS, all 4 roles, explicit GetSecretValue action (v3.2 refuses a bare ARN). opal-portal: news-trending + jwt-public-key + external-apis allowed. news-ingestion: external-apis + news-trending allowed. yang: us-east-2 external-apis allowed. opalinvest-auth (SEV1): jwt-private-key + jwt-public-key + opalinvest/admin-seed + opalinvest/jwt-secret ALL allowed. Control: github-token stays implicitDeny (pre-existing, untouched by the narrowing). | CLOSED 20260709T125316Z |
| behaviour-output | verify | OUTPUT exercise login path first via real auth then the fail-silent readers on output signatures | invoke and auth evidence |  | OPEN |

## Log

- 20260709T122707Z OPENED by 0.5.0_AE_OpalETL with 7 leg(s)
- 20260709T125313Z LEG tf-shared-infra closed: apply: 0 added, 1 changed, 0 destroyed (aws_iam_role_policy.secretsmanageraccess). Post-apply drift plan: No changes. Li
- 20260709T125314Z LEG tf-news-pipeline closed: apply: 0/1/0 (news_ingestion_policy). Drift plan: No changes. Account wildcard removed (was arn:...:us-east-1:*:secret:o
- 20260709T125314Z LEG tf-yang-pipeline closed: apply: 0/1/0 (lambda_permissions). Drift plan: No changes. GetOpalSecrets narrowed to the single us-east-2 ARN its clien
- 20260709T125315Z LEG tf-portal-auth-SEV1 closed: APPLIED LAST, rollback armed and VALIDATED before apply (captured 4-statement PolicyDocument, put-role-policy command st
- 20260709T125316Z LEG verify-dropped closed: TWO-EXERCISE leg 1 PASS, all 4 roles. Each dropped prefix was 'allowed' PRE-apply (baseline captured, so the negative is
- 20260709T125316Z LEG verify-kept closed: TWO-EXERCISE leg 2 PASS, all 4 roles, explicit GetSecretValue action (v3.2 refuses a bare ARN). opal-portal: news-trendi
- 20260709T125416Z HELD-SOVEREIGN-GATED gate=external/behaviour-output: the SEV1 login-path exercise is NOT PROVABLE by black-box invo
