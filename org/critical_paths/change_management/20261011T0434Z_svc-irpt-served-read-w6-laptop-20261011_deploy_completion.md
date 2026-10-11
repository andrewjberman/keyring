# Deploy Completion Record
**Date opened:** 2026-10-11T04:34:03.087649+00:00
**Status:** OPEN
**Deploy:** TO30 AMENDMENT 4 WINDOW 6: svc-irpt reader window for dell2 IRPT_ANLREQ rev 6 live-call arm (R3/R4/R5), ledger irpt-ycdgen-served-read-20261009; REMOVE at G2 'R done' or ADD+30m, this seat holds the clock; no GetSecretValue
**Authored by:** 0.7.0_AE_CloudOps~CTL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 0.5h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| ADD | activation | svc-irpt secret resource policy set to the signed ADD file (window 6) | Live BEFORE set-equal at the start; signed ADD put with --block-public-policy; read-back ADD set-equal; dell2 allowed, dell1 explicitDeny, walker allowed; no GetSecretValue |  | OPEN |
| REMOVE | activation | svc-irpt secret resource policy restored to the signed BEFORE file at G2 R done or ADD+30m | Live ADD set-equal at the start; signed BEFORE put with --block-public-policy; read-back BEFORE set-equal; dell2 explicitDeny, dell1 explicitDeny, walker allowed; no GetSecretValue |  | OPEN |

## Log

- 20261011T043403Z OPENED by 0.7.0_AE_CloudOps~CTL with 2 leg(s)
