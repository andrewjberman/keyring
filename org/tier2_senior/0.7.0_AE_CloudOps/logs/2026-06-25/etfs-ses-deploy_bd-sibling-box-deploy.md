# 0.7.0_AE_CloudOps -- ETFS-SES push-infra deployed + BD 49F durable-auth sibling box deployed+certed
**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, COORDINATE
**date:** 2026-06-25
**window:** 1930Z -> 2005Z (since last log: td3-scorer-full_limb-committed_ses-domain-confirmed.md)

## Summary
Two clean end-to-end deploys this window, both CVO/COO-tracked with NEVER-law ledgers opened+closed
in-session: (1) the ETFS presentation SES push-infra (identity-scoped ses:SendEmail Sid + SES_SENDER);
(2) a NEW EC2 sibling box for the BD 49F durable auto-auth (CV-login + OTP-relay), built from scratch,
deployed, live-verified, and CVO-certed. Plus source-grounded grounding handed to 0.6.0 on the ASTN box.

## Work done

### 1. ETFS-SES push-infra (COO GO 192212Z) -- deployed shared-infra-v1.32.1
Ground-truth reshaped the task: the sender identity ALREADY EXISTED (noreply@opalinvest.dev sends via
the verified opalinvest.dev DOMAIN identity, DKIM SUCCESS, in production by portal-auth) -- nothing to
provision. The real work (IAM Sid + env) lives in MY etfs-presentation.tf, so I did it own-lane (the GO
assumed 0.5.0 owned that TF; it doesn't -- surfaced the reconciliation to COO).
- `a28b02ebf` -- aws_iam_role_policy ses-send-noreply (ses:SendEmail/SendRawEmail -> identity/opalinvest.dev
  + Condition ses:FromAddress=noreply@opalinvest.dev) + env SES_SENDER=noreply@opalinvest.dev. SES_RECIPIENTS
  left UNSET -> push INERT (handler needs both). Tagged shared-infra-v1.32.1.
- Verified live: IAM policy present, Lambda env correct, post-apply 0-diff. Ledger `06ade759c` (open+close).
- Sandbox note (us-east-1 Prod=false but SendingEnabled/HEALTHY): internal @opalinvest.com team addresses
  largely already SES-verified -> internal push works in sandbox now; only external recipients need verify.
- REMAINING: set SES_RECIPIENTS when Andrew's recipient list lands = one env add + apply. RAVC'd COO+0.5.0.

### 2. BD 49F durable auto-auth SIBLING box (CTO arch: Kimi-VL + ASTN-stack) -- deployed + certed
NEW TF root infra/aws/terraform/bd-49f-auto-login/ (main+instance+iam). Built from the ASTN box pattern;
incorporated two live refinements (CVO 195133Z env-var-linked-not-hardcoded; 0.6.0 195511Z SM-direct script).
- `3f28ccd3c` -- TF root: EC2 (AL2023/t3.medium, SSM-managed no-keypair, IMDSv2-required, encrypted root,
  ephemeral public IP, bootstrap node+Chromium libs+Xvfb) + SG (egress-all/no-inbound) + least-priv role +
  secret-id ENV pointers (names not values) to /opt/bd-49f-auto-login/secret-ids.env.
- `ad627bc22` -- env aligned to the script contract (BD_KIMI_SECRET_ID rename, BD_HEADLESS=1/BD_OTP_ADAPTER=graph,
  BD_APP_URL/BD_GRAPH/BD_OTP_* TODOs). IAM unchanged (already matched).
- `154c32b26` -- EC2_MANIFEST registered + deploy ledger closed.
- DEPLOYED via safe-apply: instance i-0fa1846f04ed7e337 (running, IMDSv2, profile attached), 6 added/0-diff.
- Role bd-49f-auto-login-role: GetSecretValue blackdiamond/49f/* + astn/kimi/api-key-* + astn/brightdata/
  residential-proxy-*; PutSecretValue blackdiamond/49f/session-* ONLY; scoped artifact pull; SSM core.
  FIRM-SEP CLEAN: zero cot/inf/firm-bucket, NO SES, NO ec2:* control-plane.
- CVO CERT PASS (200526Z, independently comp-iam-verified per Rule 22 -- not my self-report): firm-sep +
  least-priv confirmed, no over-grant. One non-blocking observation (49f/* read wildcard, intentional for
  the future app-reg). Cleared from the IAM side for the live run.

### 3. ASTN box grounding for the BD co-opt (handed to 0.6.0)
Source-grounded (read tools/astn_wsjft/ + EC2_MANIFEST, not recollection) + corrected 0.6.0's premise:
Playwright+Chromium YES, residential-proxy YES (flip to always-on for BD's datacenter-IP block), vision =
TEXT-LLM-only today (Kimi-VL is new code). Recommended SIBLING box over co-residence (ASTN self-stops daily).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-iam service bd-49f-auto-login-role | pre-apply declared-perms check + post-apply realized reconcile | PASS -- 5 stmts, no drift, firm-sep clean |
| comp-which "SES identity terraform config" | locate SES IaC | PARTIAL -- dead-routed to generic grep; fell back to typed Grep on *.tf |
| terraform plan (shared-infra + bd-49f root) | drift check + apply preview | PASS -- only my diffs, 0 unrelated drift |

**What worked:** comp-iam was the decisive firm-sep verifier on BOTH ends (my pre-apply check + the CVO's
independent cert) -- exactly the relationship-aware IAM tool the rail intends over raw get-role-policy.
**What failed:** comp-which dead-routed on the SES-IaC question (generic grep, not the SES resource); used
the typed Grep tool instead. Minor.
**Gap found:** the rail HUD false-triggers on `git log -- infra/...` (history, not a .tf search) -- benign
but a repeat papercut; noting for the COMPRAIL backlog (git-log is not an inspection).

## Deployment Sequence + Verification (AE role-additions)
1. ETFS-SES: edit etfs-presentation.tf -> validate -> targeted+full plan (1 add/1 change) -> commit a28b02ebf
   -> open ledger -> safe-apply (1 added/1 changed) -> verify live (IAM+env) -> 0-diff -> tag v1.32.1 -> push
   -> close ledger 06ade759c.
2. BD box: write 3 TF files -> init+validate+plan (6 add) -> commit 3f28ccd3c -> (0.6.0 IAM-update) edit env
   -> commit ad627bc22 -> comp-iam declared-check -> open ledger -> safe-apply (6 added) -> verify live
   (instance running/IMDSv2; comp-iam realized no-drift) -> 0-diff -> register manifest -> commit 154c32b26
   -> close ledger -> push. CVO cert PASS.

## Current State
- ETFS-SES: deployed (shared-infra-v1.32.1). etf-ownership-dashboard role has ses-send-noreply; env
  SES_SENDER set, SES_RECIPIENTS unset (push inert). Activation = SES_RECIPIENTS when Andrew's list lands.
- BD box: i-0fa1846f04ed7e337 LIVE + CVO-certed. role bd-49f-auto-login-role. TF infra/aws/terraform/
  bd-49f-auto-login. Deploy path s3://opal-313476888478-lambda-artifacts/ec2/bd-49f-auto-login/ -> SSM.
  Hosts 0.6.0's bd_49f_auto_login.js (not yet code-deployed). Secret-id pointers in /opt/.../secret-ids.env
  (orchestrator must source -- SSM non-login shell won't auto-source).
- DC2-eclipse: armed 06-26 08:15 UTC.

## Next Steps
- [0.6.0_AE_PartnerETL] code-deploy bd_49f_auto_login.js (S3->SSM) + fix the proxy-secret-shape bug CVO
  caught + provide BD_APP_URL; pair on the residential-always config + first smoke test.
- [0.7.0_AE_CloudOps] wire BD_GRAPH_SECRET_ID env + (if outside 49f/) the GetSecretValue ARN delta when the
  Graph app-reg secret is named post-Andrew-consent; CVO re-certs the delta.
- [0.7.0_AE_CloudOps] set ETFS SES_RECIPIENTS when Andrew's recipient list lands.
- [0.7.0_AE_CloudOps] 06-26 AM: DC2 artifact review -> disable rule -> RAVC CTO/COO.

## Blockers
None. BD live-run gated on 0.6.0's script-bug fix + code deploy (their lane); ETFS push-activation gated on
Andrew's recipient list -- both genuine external/cross-lane gates, not blockers on my work (all my legs landed).
