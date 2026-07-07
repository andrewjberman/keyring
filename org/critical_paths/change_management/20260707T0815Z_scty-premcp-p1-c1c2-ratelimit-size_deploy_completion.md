# Deploy Completion Record
**Date opened:** 2026-07-07T08:15:46.779432+00:00
**Status:** OPEN
**Deploy:** SCTY_PREMCP P1 C1/C2: app-layer rate-limit (per-IP + per-identity) + request-size cap (m365-mcp-gateway)
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit: ratelimit.py + config RL_* + server.py middleware + lock-test | hash pushed |  | OPEN |
| L2 | ec2-baked-asset | m365-mcp-gateway app/ on-instance via safe-ec2-deploy | SSM md5 of running ratelimit.py+server.py+config.py |  | OPEN |
| L3 | activation | gateway restart picks up the middleware; /health ok + /mcp 401 unchanged | SSM systemctl active + live probes |  | OPEN |
| L4 | verify | CVO live-cert: 429-on-over-rate (per-IP + per-identity) + Retry-After + 413-on-oversize + legit passes + fail-open/closed + XFF right-most keying | CVO cert msg |  | OPEN |

## Log

- 20260707T081546Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
