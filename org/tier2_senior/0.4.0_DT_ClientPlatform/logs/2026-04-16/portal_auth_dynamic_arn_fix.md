# Session Log -- 2026-04-16 -- portal-auth-v1.12.4 dynamic Lambda@Edge ARN fix

| Field | Value |
|-------|-------|
| Agent | 0.4.0_DT_ClientPlatform |
| Date | 2026-04-16 |
| TO | standalone fix (pin-drift incident 2026-04-15) |
| Authorization | Andrew "go" 2026-04-16 |

## Objective

Commit and deploy the `cloudfront-distribution.tf` change that replaces hardcoded
Lambda@Edge version literals (`:12`, `:13`, etc.) with dynamic `qualified_arn`
references from the managed `aws_lambda_function` resources when `enable_lambda_edge=true`.

Root cause of fix: 2026-04-15 auth-validator-edge v13 was published via terraform apply
but CloudFront stayed pinned at `:12` because the local in cloudfront-distribution.tf
was not updated. Required a manual bump commit (ADVI_PROFIL.004c). This pattern was
fragile on all 4 edge functions -- one missed bump = wrong version in CF.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | comp-routes behaviors | 23 behaviors, 4 edge functions confirmed; no custom error response surprises |
| 2 | git commit --only cloudfront-distribution.tf | `80399e3e` |
| 3 | terraform plan | **No changes. Infrastructure is up-to-date.** (0-diff on first plan -- cosmetic Terraform refactor, resolved ARNs identical to current deployed state) |
| 4 | record-terraform-deploy.sh portal-auth | Source map updated (7 functions), CHANGELOG.json write failed (git log JSON parse on commit message characters -- not a blocker; source map committed at `76a6b0ca`) |
| 5 | Update deployment_map.xml | portal-auth current_tag -> portal-auth-v1.12.4; recent_deployments entry added |
| 6 | git tag | `portal-auth-v1.12.4` |
| 7 | git push origin CLOUD --follow-tags | b3f6b1ee..76a6b0ca + new tag pushed |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| portal-auth | portal-auth-v1.12.4 | 80399e3e (CF change) + 76a6b0ca (source map) |

## Verification

Plan output: `No changes. Your infrastructure matches the configuration.`
Warnings (non-blocking): `Redundant ignore_changes element` on `qualified_arn` in
lambda-edge.tf (5 instances across 4 edge functions + 1 tier-router). Provider-computed
attribute cannot be in ignore_changes -- no effect, safe to remove in a future cleanup
commit. Filed as known-gotcha.

## Compiler Tools

| Tool | Run | Result | Notes |
|------|-----|--------|-------|
| comp-routes behaviors | Before commit | 23 behaviors output; all 4 edge functions present on correct paths; custom error responses (403/404 -> 200 /index.html) unchanged | DT minimum: before CF changes |
| terraform plan | Before tag | No changes (0-diff) | Confirms dynamic refs resolve to identical ARNs as hardcoded literals |

## Known Issues / Follow-up

- CHANGELOG.json write failure: `record-terraform-deploy.sh` emits a Bun JSON parse error
  when commit messages contain certain characters. This is a pre-existing script bug;
  source map write (the critical path) succeeded. Low priority -- CHANGELOG.json is
  informational only.
- `ignore_changes = [qualified_arn]` on lambda-edge.tf Lambda resources: Terraform warns
  these are redundant (provider-computed attributes can't have configured values to
  compare). Clean-up commit can remove them, no functional impact either way.

## Files Modified

| File | Change |
|------|--------|
| infra/aws/terraform/portal-auth/cloudfront-distribution.tf | Dynamic qualified_arn refs replacing hardcoded :version literals |
| infra/aws/lambda/ci/lambda-source-map.json | Deployed commit bumped for 7 portal-auth functions (record-deploy auto) |
| org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/deployment_map.xml | current_tag -> v1.12.4; recent_deployments entry added |
| org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-04-16/portal_auth_dynamic_arn_fix.md | This file |

## Current State

portal-auth at `portal-auth-v1.12.4`, pushed. CloudFront now auto-tracks Lambda@Edge
published versions on every deploy -- no manual ARN bump needed on future edge deploys.

Active TO `ADVI_49EXEC.004` remains pending, blocked on DS TO 2 (Lambda source).

## Next Steps

- [self] Commit deployment_map + this log via --only.
- [self] Standby on ADVI_49EXEC.004 -- resume Phase 2 when 0.4.0_DS MCP signals TO 2 complete.
- [0.4.0_DS_ClientPlatform] MCP when Lambda source dir is ready so TO 4 Phase 2 can proceed.
