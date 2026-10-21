# Deploy Completion Record
**Date opened:** 2026-10-21T01:30:12.113879+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T013500Z
**Deploy:** NFRA_FIDUPL FT-s-5: box role gains secretsmanager:PutSecretValue on the per-G list secret ARN only (whole root, 0 add 1 change 0 destroy)
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply of infra/aws/terraform/canonical-fidelity-ec2 (whole root, no -target) | apply output Apply complete! Resources: 0 added, 1 changed, 0 destroyed | safe-apply of the saved reviewed plan, whole root, no -target: Plan 0 to add, 1 to change, 0 to destroy (aws_iam_role_policy.box in place, one added statement PergSecretPut). Apply complete. Live get-role-policy shows PergSecretPut = secretsmanager:PutSecretValue on the perg-list-WIANxc ARN only. No seed run, no secret value written. | CLOSED 20261021T013459Z |
| L2 | verify | post-apply plan is No changes | terraform plan -detailed-exitcode rc=0 / No changes | terraform plan -detailed-exitcode after the apply: No changes. Your infrastructure matches the configuration. rc=0 | CLOSED 20261021T013500Z |
| L3 | verify | box role may put the per-G secret and not the credentials; root guard passes | fidupl_round_checks.py ft5i R1-FT5I-OK and fu6g R1-FU6G-OK | PARTIAL AS WRITTEN, stated plainly: fu6g R1-FU6G-OK (no ingress, no wildcard secret grant, no secret version, prevent_destroy present, every Resource star carries STAR-OK). fu13-style checker ft5i reads R1-FT5I-FAIL because it simulates two resource ARNs in one call (simulator collapses them; surprise row NFRA_FIDUPL-D1-S9). Equivalent evidence, one ARN per call: PutSecretValue on perg-list-WIANxc allowed, on wealthscape-credentials-gREoMF implicitDeny, positive control GetSecretValue on perg allowed. The deploy is landed and verified; FT-s-5-AC1 stays FAIL by its own invocation until the issuer fixes the checker. | CLOSED 20261021T013500Z |

## Log

- 20261021T013012Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
- 20261021T013459Z LEG L1 closed: safe-apply of the saved reviewed plan, whole root, no -target: Plan 0 to add, 1 to change, 0 to destroy (aws_iam_role_po
- 20261021T013500Z LEG L2 closed: terraform plan -detailed-exitcode after the apply: No changes. Your infrastructure matches the configuration. rc=0
- 20261021T013500Z LEG L3 closed: PARTIAL AS WRITTEN, stated plainly: fu6g R1-FU6G-OK (no ingress, no wildcard secret grant, no secret version, prevent_de
- 20261021T013500Z CLOSED -- all 3 legs proven
