# Deploy Completion Record
**Date opened:** 2026-10-01T07:06:09.770717+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T071632Z
**Deploy:** NFRA_OPLGTW OG-pr-1: three gateway read secrets and one exact-ARN GetSecretValue grant on opal-gateway-role
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~18
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| secrets | activation | Secrets Manager us-east-1 gateway/transcripts/bearer, gateway/mail/bearer, gateway/principals/rosters | describe-secret x3 ARNs | ROLLED BACK: delete-secret --recovery-window-in-days 7 x3, DeletedDate 2026-10-01T03:14 -04:00 (restorable until 2026-10-08) | CLOSED 20261001T071631Z |
| grant | activation | aws_iam_role_policy.gw_gateway_read_secrets on opal-gateway-role (targeted safe-apply) | apply 1 added 0 changed 0 destroyed + get-role-policy | ROLLED BACK: NOT APPLIED -- safe-apply BLOCKED by naming plan limb (LGIC_ENFORCE DEC-6) rc=7 before any plan or apply; no role policy created; 1 to add 0 to change 0 to destroy was the plan reading | CLOSED 20261001T071631Z |
| simulate | verify | iam simulate-principal-policy 3 granted ARNs allowed + 1 sibling implicitDeny | pr.AC2.sh output | ROLLED BACK: not run, no grant exists | CLOSED 20261001T071632Z |
| host-read | verify | gateway host i-07dccb1615503ac99 reads rosters under its own role, shape only | pr.AC3.sh output | ROLLED BACK: not run, secrets deleted and no grant exists | CLOSED 20261001T071632Z |

## Log

- 20261001T070609Z OPENED by 0.9.0_WK_NFRA_OPLGTW~18 with 4 leg(s)
- 20261001T070805Z LEG secrets closed: describe-secret x3 ARNs: gateway/transcripts/bearer-tY9tUO, gateway/mail/bearer-g8XFDo, gateway/principals/rosters-wg59o
- 20261001T071631Z LEG secrets closed: ROLLED BACK: delete-secret --recovery-window-in-days 7 x3, DeletedDate 2026-10-01T03:14 -04:00 (restorable until 2026-10
- 20261001T071631Z LEG grant closed: ROLLED BACK: NOT APPLIED -- safe-apply BLOCKED by naming plan limb (LGIC_ENFORCE DEC-6) rc=7 before any plan or apply; n
- 20261001T071632Z LEG simulate closed: ROLLED BACK: not run, no grant exists
- 20261001T071632Z LEG host-read closed: ROLLED BACK: not run, secrets deleted and no grant exists
- 20261001T071632Z CLOSED -- all 4 legs proven
