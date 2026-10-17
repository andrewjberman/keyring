# Deploy Completion Record
**Date opened:** 2026-10-17T11:13:44.370380+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T112327Z
**Deploy:** IRPT_BCKEND TO-IB-hm-11 (cell IB-hm-11, FWD-21): the mdpf-pipeline root: ONE inline-policy change on the host role mdpf-daily-runner-ec2-role (aws_iam_role_policy.mdpf_runner): the statement IrptHmacListStageAssumeRole (sts:AssumeRole on the stage role only), text committed by IB-hm-10. Census 97 worktrees by content, the foreign ledger mdpf-gold-fwd10-cottonwood-supervised-20261017 CLOSED, HEAD holds c5dd8b293a and 2d2c906b87. Rollback: revert the two additions and safe-apply the reverse plan.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | tf-lambda | ONE safe-apply of infra/aws/terraform/mdpf-pipeline, plan 0 add 1 change 0 destroy at aws_iam_role_policy.mdpf_runner only, clean re-plan | plan counts, replan No changes | Apply complete 0 added 1 changed 0 destroyed at aws_iam_role_policy.mdpf_runner via safe-apply; replan No changes | CLOSED 20261017T112225Z |
| L2 | verify | policy read back from the host role: exactly one new statement IrptHmacListStageAssumeRole, no wildcard, every other statement byte-equal to the before-state | statement-by-statement compare | get-role-policy read back: 37 statements, 36 byte-equal to before (0 gone), 1 new IrptHmacListStageAssumeRole sts:AssumeRole on the stage role, no wildcard | CLOSED 20261017T112225Z |
| L3 | verify | the assume simulation: one allowed arm, three denied arms | simulation table | simulation one resource per call: assume_the_stage_role allowed; unrelated role, other sts action, wildcard resource all implicitDeny; no invoke | CLOSED 20261017T112226Z |
| L4 | git | the record, proof and ledger committed with explicit paths | commit ids | git 169e7cf8f7 on box/dell2 (record, criteria output, proof instance VALID); push state LOCAL | CLOSED 20261017T112327Z |

## Log

- 20261017T111344Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
- 20261017T112225Z LEG L1 closed: Apply complete 0 added 1 changed 0 destroyed at aws_iam_role_policy.mdpf_runner via safe-apply; replan No changes
- 20261017T112225Z LEG L2 closed: get-role-policy read back: 37 statements, 36 byte-equal to before (0 gone), 1 new IrptHmacListStageAssumeRole sts:Assume
- 20261017T112226Z LEG L3 closed: simulation one resource per call: assume_the_stage_role allowed; unrelated role, other sts action, wildcard resource all
- 20261017T112327Z LEG L4 closed: git 169e7cf8f7 on box/dell2 (record, criteria output, proof instance VALID); push state LOCAL
- 20261017T112327Z CLOSED -- all 4 legs proven
