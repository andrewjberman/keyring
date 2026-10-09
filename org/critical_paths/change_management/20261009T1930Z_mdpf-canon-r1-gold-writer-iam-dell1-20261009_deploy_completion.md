# Deploy Completion Record
**Date opened:** 2026-10-09T19:30:50.686582+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-a-1: targeted apply of the three per-firm gold-writer roles, their policies, and the gold Lambda's writer policy -- IAM only
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | targeted safe-apply of the seven IAM resources in infra/aws/terraform/mdpf-pipeline (three gw roles, their three role policies, and aws_iam_role_policy.mdpf_gold_writers) | C2: the plan reads 7 to add, 0 to change, 0 to destroy with no aws_lambda_function in it; the safe-apply line |  | OPEN |
| L2 | verify | the live roles, trusts, policies and the gold Lambda's writer policy | C3 three get-role plus get-role-policy reads, C4 the per-firm scoping arms, C5 the gold Lambda's AssumeRole and composite-gold grants |  | OPEN |

## Log

- 20261009T193050Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 2 leg(s)
