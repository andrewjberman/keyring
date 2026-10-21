# Deploy Completion Record
**Date opened:** 2026-10-21T10:33:34.389715+00:00
**Status:** OPEN
**Deploy:** NFRA_FIDUPL FT-s-14: revoke ssm:GetCommandInvocation from ListOwnCommandStar (whole-root safe-apply, 1 in-place policy update), applied only after the 10:45Z leg's execution is terminal
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply of infra/aws/terraform/canonical-fidelity-ec2 (whole root, no -target): exactly 1 in-place update of aws_iam_role_policy.automation (one action removed), AFTER the 10:45Z execution is terminal | apply output Apply complete! Resources: 0 added, 1 changed, 0 destroyed |  | OPEN |
| L2 | verify | the automation role no longer allows ssm:GetCommandInvocation on *; rules stay ENABLED; post-apply plan No changes | ft14a R1-FT14A-OK; ft6r R1-FT6R-OK; plan rc=0 |  | OPEN |

## Log

- 20261021T103334Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 2 leg(s)
