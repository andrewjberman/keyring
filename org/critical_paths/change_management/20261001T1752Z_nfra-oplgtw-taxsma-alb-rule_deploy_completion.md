# Deploy Completion Record
**Date opened:** 2026-10-01T17:52:32.036324+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T175733Z
**Deploy:** NFRA_OPLGTW OG-tt-1: one forward-only ALB listener rule taxsma_capability (priority 36, exactly /ms/taxsma-workbook) on the opal-gateway https listener
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~18
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| rule | activation | aws_lb_listener_rule.taxsma_capability on the opal-gateway https listener (targeted safe-apply) | apply 1 added 0 changed 0 destroyed + describe-rules shows one /ms/taxsma-workbook rule at priority 36 | targeted terraform plan 1 to add 0 to change 0 to destroy; safe-apply of the saved plan rc=0: Apply complete! Resources: 1 added, 0 changed, 0 destroyed.; rule arn .../listener-rule/app/opal-gateway/89166a68f337e5a4/2904a0140214f982/3a86fd5003423b64; live describe-rules priority 36: /ms/taxsma-workbook, forward; tt.AC1.sh PASS | CLOSED 20261001T175733Z |
| probe | verify | unauthenticated GET /ms/taxsma-workbook reaches the app (no sign-in); unknown /ms path and / 302; /ms/sites 401 | tt.AC2.sh output | tt.AC2.sh: 1 live Tax rule; probe tax 404 no sign-in; ms_unknown 302 sign-in; root 302 sign-in; ms_sites 401; only the sentinel-at-HEAD line pending the close commit | CLOSED 20261001T175733Z |

## Log

- 20261001T175232Z OPENED by 0.9.0_WK_NFRA_OPLGTW~18 with 2 leg(s)
- 20261001T175733Z LEG rule closed: targeted terraform plan 1 to add 0 to change 0 to destroy; safe-apply of the saved plan rc=0: Apply complete! Resources:
- 20261001T175733Z LEG probe closed: tt.AC2.sh: 1 live Tax rule; probe tax 404 no sign-in; ms_unknown 302 sign-in; root 302 sign-in; ms_sites 401; only the s
- 20261001T175733Z CLOSED -- all 2 legs proven
