# Deploy Completion Record
**Date opened:** 2026-07-09T12:27:07.319943+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260709T164352Z
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
| behaviour-output | verify | OUTPUT exercise login path first via real auth then the fail-silent readers on output signatures | invoke and auth evidence | TWO-STEP CANARY, both 200. POST /auth/login {demo@demo.test} -> 200 + accessToken PRESENT (775 chars) -> proves the jwt-PRIVATE-key read survives the narrowing (generateAccessToken -> getJwtPrivateKey, jwt.ts:63). GET /auth/me with THAT token -> 200 + a real user object (email demo@demo.test, role user) -> proves the jwt-PUBLIC-key read (verifyAccessToken -> getJwtPublicKey). FunctionError None on both. DISCRIMINATING because the token was minted valid seconds earlier: authenticateRequest's bare 'catch { return null }' collapses a denied public-key read into the same 401 an expired token produces, with no log line -- so a 401 here could ONLY have meant the read failed. The earlier invalid-token 401 returned the same value whether the claim was true or false and was correctly refused as evidence. CREDENTIAL HYGIENE: hashed with the portal's own bcryptjs@2.4.3 at SALT_ROUNDS=12, self-verified via compareSync before leaving the session; plaintext never printed/sent/committed and shredded after the run along with both response bodies; the access token never written to a log or message. REVOKE VERIFIED INDEPENDENTLY on live state (not on COO's self-report): demo@demo.test passwordHash is now $2b$12$... (the restored original), NOT my $2a$12$WcQFx9ph...; 17 attributes present; status active. NOT-YET-EXERCISED, restated: opal-portal-volatility-fetcher, opal-portal-data-proxy keyword-intelligence, news-trending-analysis, keyword-intelligence-generator have still not run post-apply; they close on their natural runs, per CTO. Their capability is proven; their behaviour is not, and that is written down rather than assumed. | CLOSED 20260709T164336Z |

## Log

- 20260709T122707Z OPENED by 0.5.0_AE_OpalETL with 7 leg(s)
- 20260709T125313Z LEG tf-shared-infra closed: apply: 0 added, 1 changed, 0 destroyed (aws_iam_role_policy.secretsmanageraccess). Post-apply drift plan: No changes. Li
- 20260709T125314Z LEG tf-news-pipeline closed: apply: 0/1/0 (news_ingestion_policy). Drift plan: No changes. Account wildcard removed (was arn:...:us-east-1:*:secret:o
- 20260709T125314Z LEG tf-yang-pipeline closed: apply: 0/1/0 (lambda_permissions). Drift plan: No changes. GetOpalSecrets narrowed to the single us-east-2 ARN its clien
- 20260709T125315Z LEG tf-portal-auth-SEV1 closed: APPLIED LAST, rollback armed and VALIDATED before apply (captured 4-statement PolicyDocument, put-role-policy command st
- 20260709T125316Z LEG verify-dropped closed: TWO-EXERCISE leg 1 PASS, all 4 roles. Each dropped prefix was 'allowed' PRE-apply (baseline captured, so the negative is
- 20260709T125316Z LEG verify-kept closed: TWO-EXERCISE leg 2 PASS, all 4 roles, explicit GetSecretValue action (v3.2 refuses a bare ARN). opal-portal: news-trendi
- 20260709T125416Z HELD-SOVEREIGN-GATED gate=external/behaviour-output: the SEV1 login-path exercise is NOT PROVABLE by black-box invo
- 20260709T133343Z HELD-SOVEREIGN-GATED gate=external/behaviour-output HELD on TWO things, both stated not assumed. (1) SEV1 LOGIN PAT
- 20260709T164317Z HOLD RELEASED -> OPEN
- 20260709T164336Z LEG behaviour-output closed: TWO-STEP CANARY, both 200. POST /auth/login {demo@demo.test} -> 200 + accessToken PRESENT (775 chars) -> proves the jwt-
- 20260709T164352Z CLOSED -- all 7 legs proven
