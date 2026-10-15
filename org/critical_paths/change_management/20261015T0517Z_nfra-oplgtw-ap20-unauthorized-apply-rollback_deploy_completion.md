# Deploy Completion Record
**Date opened:** 2026-10-15T05:17:10.079028+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261015T052253Z
**Deploy:** NFRA_OPLGTW OG-ap-20: ROLLBACK of an UNAUTHORIZED apply -- gateway-global-etfs-read-policy was applied during Phase A, which forbids any apply, with no ledger and no signed halves. 0.7.0_AE_CloudOps~Z's own error.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the unauthorized state is MEASURED before it is touched: gateway-global-etfs-read-policy live on gateway-global-internal-reader-role, and the role's other three policies read at their pre-act statement counts | get-role-policy on all four, with the document of the unauthorized one captured | The unauthorized state was MEASURED before it was touched and captured to W/G5A_UNAUTHORIZED_APPLY_CAPTURED.json (1660 bytes, the inner PolicyDocument, so it is replayable if the halves later bless it): gateway-global-etfs-read-policy live on gateway-global-internal-reader-role with 2 statements -- 9 s3:GetObject resources and a prefix-confined s3:ListBucket. The role's other three policies were read at the same moment: gateway-global-internal-reader-policy [json/*, platinum/*], gateway-global-harvest-read-policy (2 statements), gateway-global-portal-tiered-read-policy [json-tiered/market-overview/*]. | CLOSED 20261015T052252Z |
| L2 | activation | the policy is DESTROYED through safe-apply, targeted, restoring the state the halves will sign from | safe-apply output showing 1 destroyed, 0 added, 0 changed | safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply -destroy -target=aws_iam_role_policy.etfs_read, rc=0: 'Plan: 0 to add, 0 to change, 1 to destroy', 'aws_iam_role_policy.etfs_read: Destruction complete after 0s', 'Apply complete! Resources: 0 added, 0 changed, 1 destroyed'. Targeted at the ONE resource, so nothing else in the root was in the plan. NOTE the seat gate on this run: CROSSBOX-DEPLOY read overlap=hit verdict=STOP in WARN mode -- it did not block, and the overlap it saw is this very rollback ledger, but under ENFORCE it would have stopped the act and that is worth knowing before the next one. | CLOSED 20261015T052253Z |
| L3 | verify | the policy is GONE and the role's other three are untouched | get-role-policy returns NoSuchEntity for the destroyed name, and the other three read their pre-act statement counts and resource lists | The policy is GONE: get-role-policy for gateway-global-etfs-read-policy returns NoSuchEntity, and list-role-policies on the role returns exactly its three pre-act names (gateway-global-harvest-read-policy, gateway-global-internal-reader-policy, gateway-global-portal-tiered-read-policy) with the destroyed name absent. The three were re-read AFTER the destroy and their Resource lists are identical to the pre-rollback capture: internal-reader [json/*, platinum/*], portal-tiered [json-tiered/market-overview/*], harvest-read unchanged at 2 statements. So the live state is exactly what it was before the unauthorized apply, which is the state the three halves will sign from. | CLOSED 20261015T052253Z |

## Log

- 20261015T051710Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
- 20261015T052252Z LEG L1 closed: The unauthorized state was MEASURED before it was touched and captured to W/G5A_UNAUTHORIZED_APPLY_CAPTURED.json (1660 b
- 20261015T052253Z LEG L2 closed: safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply -destroy -target=aws_iam_role_policy.etfs_read, rc=0: 'Plan:
- 20261015T052253Z LEG L3 closed: The policy is GONE: get-role-policy for gateway-global-etfs-read-policy returns NoSuchEntity, and list-role-policies on 
- 20261015T052253Z CLOSED -- all 3 legs proven
