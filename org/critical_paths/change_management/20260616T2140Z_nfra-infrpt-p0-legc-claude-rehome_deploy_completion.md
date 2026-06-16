# Deploy-completion ledger -- NFRA_INFRPT.P0 leg-c (Claude re-home, Anthropic SDK)

**class:** deploy_completion
**status:** OPEN (deploy-start; small safe-apply pending -- monitor already in TF, no re-import)
**opened:** 20260616T2140Z
**closed:** --
**owner:** 0.7.0_AE_CloudOps~B
**project / TO:** NFRA_INFRPT / P0 leg-c (re-home §6 error-triage + §5 security-briefing to Claude)
**authorization:** Andrew-picked mechanism = Claude via Anthropic SDK (AskUserQuestion 2026-06-16, NOT Bedrock -- he ground-truthed the firm doesn't use Bedrock). COO re-GO 213433Z (leg-c NEXT, then DR2). CTO Bedrock ruling falsified + superseded.

## What this deploys
- §6 analyze_errors_with_ai + §5 security-briefing re-homed from the BROKEN OpenAI key fetch to Claude via
  the Anthropic SDK -- the firm's proven pattern (anthropic-sdk-deps layer + anthropic-api-key secret +
  claude-sonnet-4-6, same as exec-summary-generator). New get_anthropic_client + invoke_claude +
  generate_security_briefing; removed the OpenAI client/secret/model (the line-629 broken fetch is GONE).
- TF (infra-monitor.tf): runtime python3.11 -> **python3.12** (the anthropic-sdk-deps layer is 3.12-only) +
  attach the layer (data.aws_lambda_layer_version) + a scoped secretsmanager:GetSecretValue grant on
  anthropic-api-key-* (MonitorAnthropicSecretRead inline policy on opal-portal-lambda-role). No Bedrock grant
  (Anthropic API = outbound HTTPS). comp-iam gaps clean. Package stays dep-free (SDK from the layer).
- Reuses the WORKING anthropic-api-key secret (not a new one) -- the original triage died on a broken secret,
  so reuse the proven key to avoid re-introducing that fragility.
- Artifact: s3://opal-313476888478-lambda-artifacts/shared-infra/opal-infrastructure-monitor.zip
  (content-sha256 Chkm1OdBDw+x9z8Wp02YwPXyYNG+4+WXwtHzza37cXs=, 16.3KB).

## Close criteria
- safe-apply (HALTGT clear) + 0-diff re-plan; live CodeSha256 matches; runtime=python3.12; layer attached.
- CONTROLLED INVOKE verify (emitted report, not rc=0): §6 = Claude-generated per-error root-cause+severity
  (no "AI summary unavailable"); §5 = Claude security briefing. Report archives clean. P0 COMPLETE (a+b+c).
- RAVC2 to COO. Finish-in-session.

## Rollback
Revert the TF (runtime->3.11, drop layer+secret-policy) + redeploy the prior (a/b) artifact (S3 versioned).
Forward-only report-generator logic; reads live state each run; no data re-emit.
