# Deploy Completion Record
**Date opened:** 2026-10-21T09:55:26.337675+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T095901Z
**Deploy:** NFRA_FIDUPL FT-s-12: the three schedule rule targets gain the :$DEFAULT version suffix (whole-root safe-apply, 3 in-place target updates)
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply of infra/aws/terraform/canonical-fidelity-ec2 (whole root, no -target): exactly 3 in-place updates of aws_cloudwatch_event_target.window | apply output Apply complete! Resources: 0 added, 3 changed, 0 destroyed | BEFORE: all three rule targets carried the document ARN with NO version suffix; simulator, schedule role, ssm:StartAutomationExecution on the suffixed ARN (one resource per call): allowed. safe-apply of the saved reviewed plan, whole root, no -target: Plan 0 to add, 3 to change, 0 to destroy (only aws_cloudwatch_event_target.window[leg-1..3] arn in place). Apply complete! Resources: 0 added, 3 changed, 0 destroyed, at about 09:57Z. No execution started by hand. | CLOSED 20261021T095901Z |
| L2 | verify | all three target ARNs end in :$DEFAULT and the rules stay ENABLED; post-apply plan No changes | ft12t R1-FT12T-OK; ft6r R1-FT6R-OK; plan rc=0 | terraform plan -detailed-exitcode after the apply: No changes rc=0. ft12t: R1-FT12T-OK rule targets: all 3 end in :$DEFAULT. ft6r: R1-FT6R-OK the three schedule rules are ENABLED. Live describe-rule: ENABLED with crons cron(45 9), cron(15 10), cron(45 10) unchanged. | CLOSED 20261021T095901Z |

## Log

- 20261021T095526Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 2 leg(s)
- 20261021T095901Z LEG L1 closed: BEFORE: all three rule targets carried the document ARN with NO version suffix; simulator, schedule role, ssm:StartAutom
- 20261021T095901Z LEG L2 closed: terraform plan -detailed-exitcode after the apply: No changes rc=0. ft12t: R1-FT12T-OK rule targets: all 3 end in :$DEFA
- 20261021T095901Z CLOSED -- all 2 legs proven
