# Deploy Completion Record
**Date opened:** 2026-09-30T23:52:50.521654+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T000839Z
**Deploy:** MDPF_TAXSMA TX-i-1: two scoped Tax prelude roles (mdpf-49f-taxsma-role, mdpf-cot-taxsma-role) + mdpf-gold-taxsma-policy on the Gold role; mdpf-pipeline root, 5 creates, nothing else
**Authored by:** 4.0.0_SA_CRO
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | fresh saved plan of infra/aws/terraform/mdpf-pipeline from the shared tree @69521a6c4f | Plan 5/0/0 = exactly the five TX-i-1 resources; the only other line is the pre-existing output drift mdpf_route_bindings_sha256 | Saved plan 23:4xZ from the shared tree @69521a6c4f (terraform on PATH, lock on): Plan 5 to add, 0 to change, 0 to destroy = aws_iam_role.taxsma_49f, aws_iam_role.taxsma_cot, aws_iam_role_policy.taxsma_49f, aws_iam_role_policy.taxsma_cot, aws_iam_role_policy.mdpf_gold_taxsma. Outputs: pre-existing mdpf_route_bindings_sha256 drift c9e5->98f5 (state only; opal-assets pins a typed literal, comp-find 1 DEF hit of 24 files) + two new role ARN outputs. Baseline plan 22:1xZ before any edit: 0 resource changes, the same output drift. | CLOSED 20260930T235539Z |
| D1 | activation | safe-apply of the saved plan | apply complete 5 added; re-plan No changes | safe-apply 00:03:55Z of the saved plan (vendored terraform 1.9.8; naming plan limb WARN 49 graded, 0 REFUSE; comp-tagauthz PASSED): Apply complete, 5 added 0 changed 0 destroyed -- mdpf-49f-taxsma-role, mdpf-cot-taxsma-role, mdpf-49f-taxsma-policy, mdpf-cot-taxsma-policy, mdpf-gold-taxsma-policy. Re-plan 00:06Z: No changes. Two earlier wrapper runs applied nothing: 23:55Z fail-closed on a backend hash (root had been initialised with terraform 1.14.5 on PATH; re-initialised with the vendored binary), 23:59Z naming REFUSE on two policy names (fixed @bb9a291faa). | CLOSED 20261001T000733Z |
| V1 | verify | role sessions exercised live | 49f session: own-prefix list OK, cottonwood bucket AccessDenied, served portal-v2 put AccessDenied; cot session mirror; simulation and exercise recorded separately | SIMULATED, NOT EXERCISED. iam simulate-principal-policy 2026-10-01T00:07Z, 30 rows, one resource per call, aws:PrincipalArn and s3:prefix passed as context, each firm bucket's live policy passed as the resource policy: 30 of 30 as expected. 49f role allowed on 0833/0824 Silver, the global workbook Bronze/Silver, its own dispositions (get, get-by-version, put), its taxsma_assets, bucket versioning, the capability secret pattern; denied on another secret, Black Diamond cottonwood (implicit), the cottonwood bucket (explicitDeny, the fence), both served portal-v2 puts, and other prefixes of its own bucket. cot role the mirror, and denied the secret. Gold role allowed to assume both and put the control; its ambient read of the 49financial bucket explicitDeny. EXERCISE from a role session is not possible from this seat (the roles trust only mdpf-gold-lambda-role) and is owed at the first Gold run with the role env set (TX-r-3), including the first-run NoSuchKey read of dispositions under a prefix-conditioned ListBucket. | CLOSED 20261001T000839Z |

## Log

- 20260930T235250Z OPENED by 4.0.0_SA_CRO with 3 leg(s)
- 20260930T235539Z LEG P1 closed: Saved plan 23:4xZ from the shared tree @69521a6c4f (terraform on PATH, lock on): Plan 5 to add, 0 to change, 0 to destro
- 20261001T000733Z LEG D1 closed: safe-apply 00:03:55Z of the saved plan (vendored terraform 1.9.8; naming plan limb WARN 49 graded, 0 REFUSE; comp-tagaut
- 20261001T000839Z LEG V1 closed: SIMULATED, NOT EXERCISED. iam simulate-principal-policy 2026-10-01T00:07Z, 30 rows, one resource per call, aws:Principal
- 20261001T000839Z CLOSED -- all 3 legs proven
