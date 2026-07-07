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
| L1 | git | CLOUD commit: config.READ_ONLY_GRAPH_SCOPES + token_broker tier-scope + runbook | hash pushed |  | OPEN |
| L2 | ec2-baked-asset | m365-mcp-gateway app/ on-instance via safe-ec2-deploy | SSM md5 of running config.py+token_broker.py |  | OPEN |
| L3 | activation | gateway service restart picks up the new app code | SSM systemctl status + a live get_token path |  | OPEN |
| L4 | verify | CVO live-cert: read-only token -> write 403s AT GRAPH by-permission + read tools work + broker-error degrades to read-only | CVO cert msg |  | OPEN |

## Log

- 20260707T075018Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
