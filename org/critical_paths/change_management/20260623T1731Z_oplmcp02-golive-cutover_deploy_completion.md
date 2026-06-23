# Deploy Completion Record
**Date opened:** 2026-06-23T17:31:55.697925+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260623T180405Z
**Deploy:** OPLMCP.02 go-live cutover -- M365 MCP gateway: STEP-A(secrets+IAM+forced EC2-replace) -> STEP-B(code-deploy MOCK_GRAPH=0 /health-green) -> STEP-C(authenticate-oidc listener swap = GO-LIVE)
**Authored by:** 0.7.0_AE_CloudOps~B
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | infra/aws/terraform/m365-mcp-gateway | post-apply 0-diff re-plan (converged) + tag m365-mcp-gateway-vX pushed --follow-tags | safe-apply tfplan.stepa = 3 add/0 change/2 destroy (EC2 replace i-01d75141177c88b96->i-07dccb1615503ac99 + aws_iam_role_policy.gw_golive created); post-apply re-plan = 'No changes. Your infrastructure matches the configuration' (converged); new box running PublicIP 44.203.66.93 + latest AMI + profile w/ gw_golive; EC2_MANIFEST updated; tagged m365-mcp-gateway-v1.1.0; pushed bc31279c5 CLOUD. | CLOSED 20260623T174026Z |
| B | ec2-baked-asset | EC2 m365-mcp-gateway(new id):/opt/m365-mcp-gateway | SSM md5 of RUNNING app/server.py + /health 200 + TG healthy + MOCK_GRAPH=0 in .env | safe-ec2-deploy SSM deploy=Success (ssm:29861a93). Independently verified ON-BOX (not wrapper self-report): systemd m365-mcp-gateway ACTIVE; /health={ok:true}; MOCK_GRAPH=0; TENANT_ID(36c)/CLIENT_ID(36c)/CLIENT_SECRET(40c)/FERNET_KEY(44c) all SET; .env perms 600; app/server.py md5=77c43d975f03fdf8b5cec2ff5e233d10; ALB->gateway SG path open (gw SG 8080 from ALB SG sg-0920efdb81831611f). deployed_commit 628c29ca6, manifest ccd684c57. TG=unused/NotInUse (CORRECT pre-forward -- AWS only health-checks an in-use TG; TG-healthy is structurally gated to the STEP-C forward + verified there). Fixed a latent jq-Rs SSM-passing bug in the never-run staged deploy script; wrapper charmap-crashed post-success (non-blocking, flagged). | CLOSED 20260623T175533Z |
| C | verify | aws_lb_listener.https authenticate-oidc swap | post-apply 0-diff + curl-through-OIDC returns gateway NOT 503 (go-live VERIFIED) | STEP-C safe-apply tfplan.stepc = 0 add/1 change/0 destroy (listener in-place 503->authenticate-oidc+forward, ARN preserved); real client_secret CLI-set via aws elbv2 modify-listener (out of TF state; lifecycle ignore_changes); post-apply re-plan = 'No changes. Your infrastructure matches the configuration' (CONVERGED). GO-LIVE VERIFIED: curl https://mcp.opalinvest.dev/ = HTTP 302 -> login.microsoftonline.com/6810043e.../oauth2/v2.0/authorize (correct client_id 53360468/redirect_uri/scope openid+profile+email; NOT the 503); TG target i-07dccb1615503ac99 = HEALTHY; tag m365-mcp-gateway-v1.2.0. AC2 (authenticated gateway reach + per-user-scope) = CVO post-go-live cert on synthetic mailboxes. | CLOSED 20260623T180405Z |

## Log

- 20260623T173155Z OPENED by 0.7.0_AE_CloudOps~B with 3 leg(s)
- 20260623T174026Z LEG A closed: safe-apply tfplan.stepa = 3 add/0 change/2 destroy (EC2 replace i-01d75141177c88b96->i-07dccb1615503ac99 + aws_iam_role_
- 20260623T175533Z LEG B closed: safe-ec2-deploy SSM deploy=Success (ssm:29861a93). Independently verified ON-BOX (not wrapper self-report): systemd m365
- 20260623T180405Z LEG C closed: STEP-C safe-apply tfplan.stepc = 0 add/1 change/0 destroy (listener in-place 503->authenticate-oidc+forward, ARN preserv
- 20260623T180405Z CLOSED -- all 3 legs proven
