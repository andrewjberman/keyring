# Deploy Completion Record
**Date opened:** 2026-10-21T10:20:50.538390+00:00
**Status:** OPEN
**Deploy:** NFRA_FIDUPL FT-s-13: the schedule role policy gains the document/ ARN form of the one run document (whole-root safe-apply, 1 in-place policy update)
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply of infra/aws/terraform/canonical-fidelity-ec2 (whole root, no -target): exactly 1 in-place update of aws_iam_role_policy.schedule (one added Resource) | apply output Apply complete! Resources: 0 added, 1 changed, 0 destroyed |  | OPEN |
| L2 | verify | the schedule role may start the run on the document/ form; rules stay ENABLED; post-apply plan No changes | ft13s R1-FT13S-OK; ft6r R1-FT6R-OK; plan rc=0 |  | OPEN |

## Log

- 20261021T102050Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 2 leg(s)
