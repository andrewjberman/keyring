# Deploy Completion Record
**Date opened:** 2026-10-01T07:27:18.725214+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T074251Z
**Deploy:** NFRA_OPLGTW OG-pr-1 RESUME (A2): restore three gateway read secrets and apply one exact-ARN GetSecretValue grant on opal-gateway-role
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~18
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| secrets | activation | Secrets Manager us-east-1 gateway/transcripts/bearer, gateway/mail/bearer, gateway/principals/rosters (restore-secret x3) | describe-secret x3 ARNs, no DeletedDate | restore-secret x3 rc=0, describe-secret DeletedDate null x3: transcripts/bearer-tY9tUO, mail/bearer-g8XFDo, principals/rosters-wg59oX (values preserved, creation script not re-run) | CLOSED 20261001T074250Z |
| grant | activation | aws_iam_role_policy.gw_gateway_read_secrets on opal-gateway-role (targeted safe-apply) | apply 1 added 0 changed 0 destroyed + get-role-policy | targeted terraform plan 1 to add 0 to change 0 to destroy; safe-apply targeted apply rc=0; live get-role-policy opal-gateway-role/gateway-read-secrets-policy: 1 statement, GetSecretValue, the 3 exact ARNs; pr.AC1.sh PASS | CLOSED 20261001T074250Z |
| simulate | verify | iam simulate-principal-policy 3 granted ARNs allowed + 1 sibling implicitDeny | pr.AC2.sh output | simulate-principal-policy ResourceSpecificResults: 3 granted ARNs allowed, sibling gateway/notgranted/probe implicitDeny. NOTE pr.AC2.sh itself reads FAIL: checker _pr.py does not parse the per-resource limb (row Z-W18-S3) | CLOSED 20261001T074251Z |
| host-read | verify | gateway host i-07dccb1615503ac99 reads rosters under its own role, shape only | pr.AC3.sh output | SSM 6b32df70 on i-07dccb1615503ac99 under host role: Success, ROSTERS master 1 write 2 all-pairs True (shape only). NOTE pr.AC3.sh host command SyntaxErrors on its own construction (row Z-W18-S4) | CLOSED 20261001T074251Z |

## Log

- 20261001T072718Z OPENED by 0.9.0_WK_NFRA_OPLGTW~18 with 4 leg(s)
- 20261001T074250Z LEG secrets closed: restore-secret x3 rc=0, describe-secret DeletedDate null x3: transcripts/bearer-tY9tUO, mail/bearer-g8XFDo, principals/r
- 20261001T074250Z LEG grant closed: targeted terraform plan 1 to add 0 to change 0 to destroy; safe-apply targeted apply rc=0; live get-role-policy opal-gat
- 20261001T074251Z LEG simulate closed: simulate-principal-policy ResourceSpecificResults: 3 granted ARNs allowed, sibling gateway/notgranted/probe implicitDeny
- 20261001T074251Z LEG host-read closed: SSM 6b32df70 on i-07dccb1615503ac99 under host role: Success, ROSTERS master 1 write 2 all-pairs True (shape only). NOTE
- 20261001T074251Z CLOSED -- all 4 legs proven
