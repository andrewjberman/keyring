# Deploy Completion Record
**Date opened:** 2026-09-30T08:44:59.043095+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPMSP r1: Inflection firm role + gateway AssumeRole grant
**Authored by:** 0.9.0_WK_NFRA_MCPMSP~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | terraform apply targeted to mcpmsp_firm_roles.tf | apply output line |  | OPEN |
| L2 | verify | simulate-principal-policy arms | AC2+AC3 lines |  | OPEN |

## Log

- 20260930T084459Z OPENED by 0.9.0_WK_NFRA_MCPMSP~2 with 2 leg(s)

## Blast radius and rollback

BLAST RADIUS: exactly four addresses from infra/aws/terraform/opal-gateway/mcpmsp_firm_roles.tf -- the module-named role
gateway-inf-firm-reader-role (aws_iam_role.inf_firm_reader), its inline policy (aws_iam_role_policy.inf_firm_reader), and the
gateway role's one new AssumeRole inline policy (aws_iam_role_policy.gw_assume_inf_firm_reader), plus the three read-only
opal_name module instances. Nothing else (writer, existing gateway policies) is touched; the plan must read
"N to add, 0 to change, 0 to destroy" or no apply.
ROLLBACK: terraform destroy -target of exactly aws_iam_role_policy.gw_assume_inf_firm_reader,
aws_iam_role_policy.inf_firm_reader, aws_iam_role.inf_firm_reader.

- 20260930T0920Z 0.9.0_WK_NFRA_MCPMSP~2: targeted plan read 3 to add, 0 to change, 0 to destroy; safe-apply BLOCKED by the naming-plan limb on an unrelated addition (row NFRA_MCPMSP-Z-W2-S3). NOTHING APPLIED: gateway-inf-firm-reader-role does not exist (NoSuchEntity). Entry held OPEN for the issuer's retry; L1/L2 carry no proof.
