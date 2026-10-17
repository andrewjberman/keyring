# Deploy Completion Record
**Date opened:** 2026-10-17T11:13:44.370380+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-hm-11 (cell IB-hm-11, FWD-21): the mdpf-pipeline root: ONE inline-policy change on the host role mdpf-daily-runner-ec2-role (aws_iam_role_policy.mdpf_runner): the statement IrptHmacListStageAssumeRole (sts:AssumeRole on the stage role only), text committed by IB-hm-10. Census 97 worktrees by content, the foreign ledger mdpf-gold-fwd10-cottonwood-supervised-20261017 CLOSED, HEAD holds c5dd8b293a and 2d2c906b87. Rollback: revert the two additions and safe-apply the reverse plan.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | tf-lambda | ONE safe-apply of infra/aws/terraform/mdpf-pipeline, plan 0 add 1 change 0 destroy at aws_iam_role_policy.mdpf_runner only, clean re-plan | plan counts, replan No changes |  | OPEN |
| L2 | verify | policy read back from the host role: exactly one new statement IrptHmacListStageAssumeRole, no wildcard, every other statement byte-equal to the before-state | statement-by-statement compare |  | OPEN |
| L3 | verify | the assume simulation: one allowed arm, three denied arms | simulation table |  | OPEN |
| L4 | git | the record, proof and ledger committed with explicit paths | commit ids |  | OPEN |

## Log

- 20261017T111344Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
