# Deploy Completion Record
**Date opened:** 2026-09-17T18:03:35.509383+00:00
**Status:** OPEN
**Deploy:** OG-i-3: rename Schwab reader identities to builder names, create the read-only SSM document + operator pin, add the browser-download ALB listener rule
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| apply | activation | opal-gateway TF root: rename 5 replaced resources + create SSM document/pin policy/ALB rule | terraform apply plan JSON + live readback (iam get-role x2, ssm get-document, elbv2 describe-rules) |  | OPEN |
| readback | verify | OGI3-AC1..AC6 probe re-run against live state | probe VERDICT lines + printed measurements |  | OPEN |

## Log

- 20260917T180335Z OPENED by 0.9.0_WK_NFRA_OPLGTW~1 with 2 leg(s)
