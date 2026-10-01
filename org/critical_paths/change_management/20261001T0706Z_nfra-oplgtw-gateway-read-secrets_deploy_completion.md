# Deploy Completion Record
**Date opened:** 2026-10-01T07:06:09.770717+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-pr-1: three gateway read secrets and one exact-ARN GetSecretValue grant on opal-gateway-role
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~18
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| secrets | activation | Secrets Manager us-east-1 gateway/transcripts/bearer, gateway/mail/bearer, gateway/principals/rosters | describe-secret x3 ARNs |  | OPEN |
| grant | activation | aws_iam_role_policy.gw_gateway_read_secrets on opal-gateway-role (targeted safe-apply) | apply 1 added 0 changed 0 destroyed + get-role-policy |  | OPEN |
| simulate | verify | iam simulate-principal-policy 3 granted ARNs allowed + 1 sibling implicitDeny | pr.AC2.sh output |  | OPEN |
| host-read | verify | gateway host i-07dccb1615503ac99 reads rosters under its own role, shape only | pr.AC3.sh output |  | OPEN |

## Log

- 20261001T070609Z OPENED by 0.9.0_WK_NFRA_OPLGTW~18 with 4 leg(s)
