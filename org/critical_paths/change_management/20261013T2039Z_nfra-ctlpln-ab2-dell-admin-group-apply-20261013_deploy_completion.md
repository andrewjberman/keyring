# Deploy Completion Record
**Date opened:** 2026-10-13T20:39:40.877698+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN TO-CT-ab-2: ONE safe-apply of infra/aws/terraform/nfra-ctlpln-identity at pin 738bbc654f (tree 355c1c13bb92), 2 add / 3 change / 2 destroy, exactly six keys: K1 aws_iam_user_group_membership.dell1_admin and K2 .dell2_admin (both Dell agent users join AdministratorAccessOpalCapital), K3 aws_iam_policy.dell_agent_deploy, K4 .dell_agent_iam_roles, K5 .dell2_ssm (Deny statements removed in place), K6 aws_iam_policy.dell_agent_routes_fn[0] + its group attachment (destroyed); four Denies kept; consumers: the two Dell users' sessions on dell1 and dell2; previous tree id b2b7307c28ddb4eaf4bc81238da8933cd066691a (a71a0b4f68 identity root) recorded before the apply; ROLLBACK = one re-apply of that previous tree (it reverses all six keys and RESTORES the Denies the ruling removed); pair 6 COO half 024c2fd428 + CTO half signed at 738bbc654f; Andrew rec (b)
**Authored by:** 0.7.0_AE_CloudOps~U7
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | start condition and PRE reads: both halves SIGNED at 738bbc654f, pin hashes and tree id recomputed from git show, PRE-1 group + user groups, PRE-2 plan text saved | reads printed |  | OPEN |
| L2 | activation | ONE .tools/safe-apply.sh apply of the saved planfile (built from a worktree at the pin); Apply complete 2 added 3 changed 2 destroyed | apply line |  | OPEN |
| L3 | verify | POST-1 both users in both groups, POST-2 five actions allowed per user, POST-3 four actions explicitDeny per user (any allowed = roll back at once), re-plan 0 diff | reads printed |  | OPEN |

## Log

- 20261013T203940Z OPENED by 0.7.0_AE_CloudOps~U7 with 3 leg(s)
