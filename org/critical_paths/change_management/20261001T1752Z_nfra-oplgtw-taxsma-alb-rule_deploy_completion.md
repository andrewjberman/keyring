# Deploy Completion Record
**Date opened:** 2026-10-01T17:52:32.036324+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-tt-1: one forward-only ALB listener rule taxsma_capability (priority 36, exactly /ms/taxsma-workbook) on the opal-gateway https listener
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~18
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| rule | activation | aws_lb_listener_rule.taxsma_capability on the opal-gateway https listener (targeted safe-apply) | apply 1 added 0 changed 0 destroyed + describe-rules shows one /ms/taxsma-workbook rule at priority 36 |  | OPEN |
| probe | verify | unauthenticated GET /ms/taxsma-workbook reaches the app (no sign-in); unknown /ms path and / 302; /ms/sites 401 | tt.AC2.sh output |  | OPEN |

## Log

- 20261001T175232Z OPENED by 0.9.0_WK_NFRA_OPLGTW~18 with 2 leg(s)
