# Deploy Completion Record
**Date opened:** 2026-10-02T19:12:31.336692+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rl-3: gateway-read-secrets-policy gains gateway/teams/bearer (4th ARN) and ALB rule 35 gains /hx/teams/* (targeted safe-apply of 2 resources)
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| iam | activation | aws_iam_role_policy.gw_gateway_read_secrets (targeted safe-apply) | apply 0 added 1 changed + ht.AC1 IAM arms: gateway/teams/bearer allowed, synthetic sibling implicitDeny, policy exactly four ARNs |  | OPEN |
| alb | activation | aws_lb_listener_rule.hx_capability rule 35 (targeted safe-apply) | apply changed + describe-rules shows three path values incl /hx/teams/* |  | OPEN |

## Log

- 20261002T191231Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 2 leg(s)
