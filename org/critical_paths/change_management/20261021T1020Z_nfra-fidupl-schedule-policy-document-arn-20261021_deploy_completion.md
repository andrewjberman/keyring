# Deploy Completion Record
**Date opened:** 2026-10-21T10:20:50.538390+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T103013Z
**Deploy:** NFRA_FIDUPL FT-s-13: the schedule role policy gains the document/ ARN form of the one run document (whole-root safe-apply, 1 in-place policy update)
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply of infra/aws/terraform/canonical-fidelity-ec2 (whole root, no -target): exactly 1 in-place update of aws_iam_role_policy.schedule (one added Resource) | apply output Apply complete! Resources: 0 added, 1 changed, 0 destroyed | BEFORE: simulator (schedule role, document/ ARN form, one resource) implicitDeny; ft13s FAIL; CloudTrail AccessDenied for the schedule role on the document/ ARN at 09:45:22Z and 10:15:02Z. Apply #1 10:23Z, safe-apply of the saved reviewed plan, whole root, no -target: Plan 0 to add, 1 to change, 0 to destroy (aws_iam_role_policy.schedule, one added Resource); Apply complete! Resources: 0 added, 1 changed, 0 destroyed. Apply #2 10:26Z (step 2B, CTO 9055): aws_iam_role_policy.automation, ssm:GetCommandInvocation added to ListOwnCommandStar, Plan 0 to add, 1 to change, 0 to destroy; Apply complete! Resources: 0 added, 1 changed, 0 destroyed. | CLOSED 20261021T103013Z |
| L2 | verify | the schedule role may start the run on the document/ form; rules stay ENABLED; post-apply plan No changes | ft13s R1-FT13S-OK; ft6r R1-FT6R-OK; plan rc=0 | AFTER: simulator (schedule role, document/ ARN form) allowed; ft13s: R1-FT13S-OK schedule start allowed on the document/ ARN form; ft6r: R1-FT6R-OK the three schedule rules are ENABLED; simulator (automation role, ssm:GetCommandInvocation on *, one resource) allowed; post-apply plan No changes rc=0; fu6g OK. Step 3B manual start succeeded (separate ledger nfra-fidupl-schedule-doc-manual-start-20261021). | CLOSED 20261021T103013Z |

## Log

- 20261021T102050Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 2 leg(s)
- 20261021T103013Z LEG L1 closed: BEFORE: simulator (schedule role, document/ ARN form, one resource) implicitDeny; ft13s FAIL; CloudTrail AccessDenied fo
- 20261021T103013Z LEG L2 closed: AFTER: simulator (schedule role, document/ ARN form) allowed; ft13s: R1-FT13S-OK schedule start allowed on the document/
- 20261021T103013Z CLOSED -- all 2 legs proven
