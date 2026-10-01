# Deploy Completion Record
**Date opened:** 2026-10-01T08:20:54.504963+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T082634Z
**Deploy:** NFRA_OPLGTW OG-al-1 PHASE B: one forward-only ALB listener rule hx_capability (priority 35, /hx/transcripts/* and /hx/mail/*) on the opal-gateway https listener
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~18
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| rule | activation | aws_lb_listener_rule.hx_capability on the opal-gateway https listener (targeted safe-apply) | apply 1 added 0 changed 0 destroyed + describe-rules shows one /hx/ rule at priority 35 | targeted terraform plan 1 to add 0 to change 0 to destroy; safe-apply of the saved plan rc=0: Apply complete! Resources: 1 added, 0 changed, 0 destroyed.; live describe-rules priority 35: /hx/transcripts/* and /hx/mail/*, forward; al.AC1.sh PASS | CLOSED 20261001T082634Z |
| probe | verify | unauthenticated GET /hx/transcripts/x and /hx/mail/x refused by the app (4xx, no sign-in); / 302; /mcp 401 | al.AC2.sh output | al.AC2.sh: 1 live /hx/ rule; probe hx_mail 404 and hx_transcripts 404 refused by the app, no sign-in; control 302 sign-in; root 302 sign-in; mcp 401 unchanged; only the sentinel-at-HEAD line pending the close commit | CLOSED 20261001T082634Z |

## Log

- 20261001T082054Z OPENED by 0.9.0_WK_NFRA_OPLGTW~18 with 2 leg(s)
- 20261001T082634Z LEG rule closed: targeted terraform plan 1 to add 0 to change 0 to destroy; safe-apply of the saved plan rc=0: Apply complete! Resources:
- 20261001T082634Z LEG probe closed: al.AC2.sh: 1 live /hx/ rule; probe hx_mail 404 and hx_transcripts 404 refused by the app, no sign-in; control 302 sign-i
- 20261001T082634Z CLOSED -- all 2 legs proven
