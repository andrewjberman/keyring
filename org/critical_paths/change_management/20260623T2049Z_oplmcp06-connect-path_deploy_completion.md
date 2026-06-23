# Deploy Completion Record
**Date opened:** 2026-06-23T20:49:31.209498+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260623T210942Z
**Deploy:** OPLMCP.06 connect-path -- gateway OAuth-AS Model-B cutover: APPLY-A(secrets-iam grant) -> S4 code-deploy + on-box enforce-smoke HARD GATE -> APPLY-B(ALB OIDC-bypass rules) -> S5 live-through-ALB verify
**Authored by:** 0.7.0_AE_CloudOps~B
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | infra/aws/terraform/m365-mcp-gateway secrets-iam gw_golive grant | targeted safe-apply 1 change/0 other + 4th secret ARN live in policy | APPLY-A safe-apply -target=aws_iam_role_policy.gw_golive = 'Apply complete! 0 added, 1 changed, 0 destroyed' (HALTGT passed clean). Live confirm: aws iam get-role-policy m365-mcp-gateway-golive GatewaySecretsRead now lists all 4 ARNs incl opal/mcp/m365-gateway-jwt-lKbCyS (other 3 untouched = least-privilege). | CLOSED 20260623T205026Z |
| B | ec2-baked-asset | EC2 m365-mcp-gateway /opt/m365-mcp-gateway RUNNING app | SSM Success + ON-BOX health 200 + AS-doc 200 + /mcp unauth 401 (HARD GATE) + jwks kid==ac4c49e6c8bec6d4 + .env/.jwt_key.pem 600 | Re-deploy ssm:bc1bdf1c Success (restart-fixed script e4d16d432). ON-BOX smoke on NEW code: systemd active; /health 200; 'OK: AS metadata serves' (/.well-known/oauth-authorization-server 200 JSON); /mcp unauth -> 401 (Bearer-enforce HARD GATE PASSED, new code); jwks kid==ac4c49e6c8bec6d4 (==S1-created key, chain-of-custody); server.py md5 c23d9181ae9c462f05ed212aa88578c9. Root-caused+fixed the enable--now-vs-restart stale-process bug (old .02 process had survived the first deploy); redeploy proves restart reloads new code. Instance whitelisted AutoShutdown=disabled (Andrew-direct). | CLOSED 20260623T210616Z |
| C | verify | aws_lb_listener rules pri10/20 OIDC-bypass | targeted safe-apply 2 add/0 other + post-apply 0-diff convergence | APPLY-B safe-apply -target=both listener rules = 'Apply complete! 2 added, 0 changed, 0 destroyed' (pri10 mcp_oauth_core + pri20 mcp_oauth_discovery created, HALTGT passed). Final untargeted terraform plan = 'No changes. Your infrastructure matches the configuration' (CONVERGED: grant+2 rules+AutoShutdown tag all match TF, zero drift). | CLOSED 20260623T210942Z |
| D | verify | live-through-ALB https://mcp.opalinvest.dev | /mcp unauth 401+WWW-Authenticate + /.well-known 200 JSON + jwks-kid-match + minted-token aud==/mcp + tag m365-mcp-gateway-v pushed | S5 live-through-ALB (curl https://mcp.opalinvest.dev): /mcp unauth -> HTTP 401 + 'WWW-Authenticate: Bearer resource_metadata=https://mcp.opalinvest.dev/.well-known/oauth-protected-resource, error=invalid_token' (NOT 302 = the no-popup fix); /.well-known/oauth-protected-resource + oauth-authorization-server -> 200 JSON (resource=aud=https://mcp.opalinvest.dev/mcp, four-way consistent); jwks kid==ac4c49e6c8bec6d4 THROUGH the ALB (==S1 key, e2e chain-of-custody); /authorize -> 307 to Entra App-2 (client adb3c23, bridge live); / root -> 302 ALB-OIDC (GUI path still gated). Tag m365-mcp-gateway-v1.3.0 pushed. | CLOSED 20260623T210942Z |

## Log

- 20260623T204931Z OPENED by 0.7.0_AE_CloudOps~B with 4 leg(s)
- 20260623T205026Z LEG A closed: APPLY-A safe-apply -target=aws_iam_role_policy.gw_golive = 'Apply complete! 0 added, 1 changed, 0 destroyed' (HALTGT pas
- 20260623T210616Z LEG B closed: Re-deploy ssm:bc1bdf1c Success (restart-fixed script e4d16d432). ON-BOX smoke on NEW code: systemd active; /health 200; 
- 20260623T210942Z LEG C closed: APPLY-B safe-apply -target=both listener rules = 'Apply complete! 2 added, 0 changed, 0 destroyed' (pri10 mcp_oauth_core
- 20260623T210942Z LEG D closed: S5 live-through-ALB (curl https://mcp.opalinvest.dev): /mcp unauth -> HTTP 401 + 'WWW-Authenticate: Bearer resource_meta
- 20260623T210942Z CLOSED -- all 4 legs proven
