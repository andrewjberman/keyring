# Deploy-completion ledger — OPAL_BBGTML gateway secret grant (m365-mcp-gateway TF)

**Opened:** 2026-07-15 ~18:15Z by 0.2.0_DT_PortfolioAnalytics (sovereign delegate; CTO routing
ruling 20260715T172813Z option (a): merge-dark now, enable CTO-gated)
**Pipeline:** m365-mcp-gateway (Terraform)
**Change:** ONE additive aws_iam_role_policy `gw_opal_portal_secret_read` — instance role
GetSecretValue on the EXACT `opal/portal/svc-data-refresh` ARN (ycharts-iam.tf pattern; inert
until the CTO-gated ENABLED_INTEGRATIONS flip). Committed BEFORE apply @ ca3ea5689.

## Legs

| # | Leg | Status |
|---|---|---|
| 1 | Commit before apply (ca3ea5689, pushed) | CLOSED |
| 2 | terraform plan | CLOSED -- Plan: 1 to add, 0 to change, 0 to destroy (only gw_opal_portal_secret_read; init refreshed the archive-provider lock selection, committed) |
| 3 | safe-apply | CLOSED -- applied clean, outputs intact (instance_role_name=m365-mcp-gateway-role) |
| 4 | Second plan 0-diff | CLOSED -- "No changes. Your infrastructure matches the configuration." |
| 5 | Rule-22a live verify | CLOSED -- (a) APPLIED: get-role-policy shows Sid OpalPortalIntegrationSecretRead, GetSecretValue, EXACT ARN ...svc-data-refresh-4QLOH6 (no wildcard); (b) POSITIVE simulate (one --resource-arns): allowed; (c) NEGATIVE control, SEPARATE invocation (orion/jwt/current): implicitDeny -- instrument discriminates |

**CLOSED COMPLETE 2026-07-15 ~18:2xZ.** Tag m365-mcp-gateway-v1.6.0. The grant is live and inert
(integration disabled); nothing reads the secret until the CTO-gated ENABLED_INTEGRATIONS flip.

**Rollback:** `terraform destroy -target aws_iam_role_policy.gw_opal_portal_secret_read` or
remove opal-portal-iam.tf + apply. No dependency holds it — the integration is disabled.
