# Deploy Completion Record
**Date opened:** 2026-07-01T19:41:52.229673+00:00
**Status:** OPEN
**Deploy:** SCTY_MCPGUARD guardrail landing to live m365-mcp-gateway (tier + G2 fail-closed denials + G6 tier-audit); scope-isolated SCTY-only YCharts-absent; roster andrew@=master alyssa@=write else=read-only; box i-07dccb1615503ac99. Author 0.5.0, verify+deploy 0.7.0~A.
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | scty-mcpguard-deploy-build commit = 0.5.0 integrated source + YCharts isolated in deploy tree | build-branch hash + 0.5.0 author-faithful ack + my hard-verify config/server SCTY-present YCharts-absent roster-correct + 47/47 on applied app package tree |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts/ec2/m365-mcp-gateway artifact + latest | s3 cp confirmation URI + artifact sha |  | OPEN |
| L3 | ec2-baked-asset | /opt/m365-mcp-gateway/app baked on i-07dccb1615503ac99 | SSM md5 of running app server/tools/config/audit.py + tier/guard/destructive_ops PRESENT + integrations ABSENT |  | OPEN |
| L4 | activation | systemctl restart m365-mcp-gateway.service | is-active active + fresh start-time/PID (restart not enable-now) |  | OPEN |
| L5 | verify | on-box smoke + CVO live-cert | /mcp 401 unauth + config.validate OK + IDENTITY_PROVIDER=alb_oidc + CVO 3-case cert READ_ONLY-mutating DENY / no-identity-mutating DENY / andrew@ PASS plus alyssa@ write |  | OPEN |

## Log

- 20260701T194152Z OPENED by 0.7.0_AE_CloudOps~A with 5 leg(s)
