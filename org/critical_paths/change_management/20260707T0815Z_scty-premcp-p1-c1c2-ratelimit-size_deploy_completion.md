# Deploy Completion Record
**Date opened:** 2026-07-07T08:15:46.779432+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260707T082338Z
**Deploy:** SCTY_PREMCP P1 C1/C2: app-layer rate-limit (per-IP + per-identity) + request-size cap (m365-mcp-gateway)
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit: ratelimit.py + config RL_* + server.py middleware + lock-test | hash pushed | 495b2b213 pushed to CLOUD | CLOSED 20260707T081627Z |
| L2 | ec2-baked-asset | m365-mcp-gateway app/ on-instance via safe-ec2-deploy | SSM md5 of running ratelimit.py+server.py+config.py | SSM i-07dccb...: ratelimit.py=115c0d30d7f4d5dcf333296e706d6e2e server.py=ae677b5b994c8cac96c4c8e9e1c00469 config.py=852cc0d95ef6f3f17d140aa6d7fdde25 -- md5-IDENTICAL to local | CLOSED 20260707T081850Z |
| L3 | activation | gateway restart picks up the middleware; /health ok + /mcp 401 unchanged | SSM systemctl active + live probes | SSM systemctl active + /health=200 + /mcp unauth=401 (middleware loaded + wraps cleanly, no app breakage; import error would have downed the service) | CLOSED 20260707T081850Z |
| L4 | verify | CVO live-cert: 429-on-over-rate (per-IP + per-identity) + Retry-After + 413-on-oversize + legit passes + fail-open/closed + XFF right-most keying | CVO cert msg | CVO live-cert PASS (082305Z): EX-A per-IP-auth 429 at 21st + UN-SPOOFABLE right-most-XFF keying (vary-left/fixed-right 9.9.9.9 -> all one key); EX-B right-most differentiates (fixed-left/vary-right -> fresh keys); EX-C 1.3MiB->413; EX-D no-false-throttle (/health 200, single legit pass); per-identity+fail-modes via lock-test 6/6 | CLOSED 20260707T082337Z |

## Log

- 20260707T081546Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
- 20260707T081627Z LEG L1 closed: 495b2b213 pushed to CLOUD
- 20260707T081850Z LEG L2 closed: SSM i-07dccb...: ratelimit.py=115c0d30d7f4d5dcf333296e706d6e2e server.py=ae677b5b994c8cac96c4c8e9e1c00469 config.py=852c
- 20260707T081850Z LEG L3 closed: SSM systemctl active + /health=200 + /mcp unauth=401 (middleware loaded + wraps cleanly, no app breakage; import error w
- 20260707T082337Z LEG L4 closed: CVO live-cert PASS (082305Z): EX-A per-IP-auth 429 at 21st + UN-SPOOFABLE right-most-XFF keying (vary-left/fixed-right 9
- 20260707T082338Z CLOSED -- all 4 legs proven
