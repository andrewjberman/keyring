# Deploy Completion Record
**Date opened:** 2026-09-15T21:52:23.075412+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-i-1: opal-gateway-access-state table, runtime grant on opal-gateway-role, operator role opal-gateway-access-admin -- the first apply of the opal-gateway root, carrying the two WAF description backfills admitted by ruling 97237
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | infra/aws/terraform/opal-gateway/schwab_access_state.tf committed on wk-nfra_oplgtw-1-1b BEFORE the apply | commit hash |  | OPEN |
| L2 | activation | terraform apply of infra/aws/terraform/opal-gateway through .tools/safe-apply.sh: creates aws_dynamodb_table.access_state, aws_iam_role_policy.gw_access_state_runtime, aws_iam_role.access_admin, aws_iam_role_policy.access_admin_policy; updates the two admitted WAF sets in place | safe-apply rc 0 and the Apply complete line |  | OPEN |
| L3 | verify | COND-1 (OGI1-AC10): the plan's out-of-cell changes are EXACTLY two ~ description updates on aws_wafv2_ip_set.opal_blocked_ips_regional_v4 and _v6, addresses absent from the diff, nothing destroyed | saved-plan census and the in-apply plan judged by the approval guard |  | OPEN |
| L4 | verify | COND-2 (OGI1-AC11): aws wafv2 get-ip-set on both sets immediately before and immediately after the apply reads identical address lists, counts printed | PRE and POST read times, counts and sha256 of each sorted list |  | OPEN |
| L5 | verify | COND-3: plan and apply in ONE safe-apply run, never a saved planfile, so the lock token is fresh; a WAFOptimisticLockException is a clean abort and a re-run, never a forcing retry. COND-4 (OGI1-AC12): after the apply a fresh plan of the root reads 0 changes on both sets and the four created resources -- run AFTER this entry closes (open, commit, act, close, commit, read; row NFRA_OPLGTW-W1-S4) | the apply record: one run, its answer, the lock-exception flag |  | OPEN |

## Log

- 20260915T215223Z OPENED by 0.9.0_WK_NFRA_OPLGTW~1 with 5 leg(s)
