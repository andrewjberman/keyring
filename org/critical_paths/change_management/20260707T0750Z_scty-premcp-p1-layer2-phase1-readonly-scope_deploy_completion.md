# Deploy Completion Record
**Date opened:** 2026-07-07T07:50:18.072165+00:00
**Status:** OPEN
**Deploy:** SCTY_PREMCP P1 Layer-2 phase-1: READ_ONLY Graph-token scope-reduction (grant-level, m365-mcp-gateway)
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit: config.READ_ONLY_GRAPH_SCOPES + token_broker tier-scope + runbook | hash pushed | 7a59c10ef pushed to CLOUD | CLOSED 20260707T075110Z |
| L2 | ec2-baked-asset | m365-mcp-gateway app/ on-instance via safe-ec2-deploy | SSM md5 of running config.py+token_broker.py | SSM i-07dccb1615503ac99: /opt/m365-mcp-gateway/app/config.py=4b44462bc7f7ef1c3dd8f3ced6ec8b3a token_broker.py=13d042aa7d9c03264abad3b6ef88f2c8 -- md5-IDENTICAL to local (baked copy matches) | CLOSED 20260707T075422Z |
| L3 | activation | gateway service restart picks up the new app code | SSM systemctl status + a live get_token path | SSM systemctl is-active m365-mcp-gateway=active; deploy /health={ok:true} + /mcp unauth 401 (hard gate unchanged); READ_ONLY_GRAPH_SCOPES x4 + force_refresh x2 present on-box | CLOSED 20260707T075422Z |
| L4 | verify | CVO live-cert: read-only token -> write 403s AT GRAPH by-permission + read tools work + broker-error degrades to read-only | CVO cert msg |  | OPEN |

## Log

- 20260707T075018Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
- 20260707T075110Z LEG L1 closed: 7a59c10ef pushed to CLOUD
- 20260707T075422Z LEG L2 closed: SSM i-07dccb1615503ac99: /opt/m365-mcp-gateway/app/config.py=4b44462bc7f7ef1c3dd8f3ced6ec8b3a token_broker.py=13d042aa7d
- 20260707T075422Z LEG L3 closed: SSM systemctl is-active m365-mcp-gateway=active; deploy /health={ok:true} + /mcp unauth 401 (hard gate unchanged); READ_
