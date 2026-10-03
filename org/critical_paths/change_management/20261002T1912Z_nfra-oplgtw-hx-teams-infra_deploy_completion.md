# Deploy Completion Record
**Date opened:** 2026-10-02T19:12:31.336692+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T191828Z
**Deploy:** NFRA_OPLGTW OG-rl-3: gateway-read-secrets-policy gains gateway/teams/bearer (4th ARN) and ALB rule 35 gains /hx/teams/* (targeted safe-apply of 2 resources)
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| iam | activation | aws_iam_role_policy.gw_gateway_read_secrets (targeted safe-apply) | apply 0 added 1 changed + ht.AC1 IAM arms: gateway/teams/bearer allowed, synthetic sibling implicitDeny, policy exactly four ARNs | targeted plan 0 to add 2 to change 0 to destroy; safe-apply of the saved plan rc=0: Apply complete! Resources: 0 added, 2 changed, 0 destroyed; ht.AC1.sh arms 1-3 OK: policy statements 1, arns 4, wildcard 0, gateway/teams/bearer allowed, synthetic sibling implicitDeny | CLOSED 20261002T191827Z |
| alb | activation | aws_lb_listener_rule.hx_capability rule 35 (targeted safe-apply) | apply changed + describe-rules shows three path values incl /hx/teams/* | same apply (rule 35 modified in place); ht.AC1.sh arm 4 OK: rule 35 path values 3: /hx/mail/* /hx/teams/* /hx/transcripts/*; INFRA ARMS 4 of 4 RESULT: PASS | CLOSED 20261002T191827Z |

## Log

- 20261002T191231Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 with 2 leg(s)
- 20261002T191827Z LEG iam closed: targeted plan 0 to add 2 to change 0 to destroy; safe-apply of the saved plan rc=0: Apply complete! Resources: 0 added, 
- 20261002T191827Z LEG alb closed: same apply (rule 35 modified in place); ht.AC1.sh arm 4 OK: rule 35 path values 3: /hx/mail/* /hx/teams/* /hx/transcript
- 20261002T191828Z CLOSED -- all 2 legs proven
