# Deploy Completion Record
**Date opened:** 2026-10-21T09:55:26.337675+00:00
**Status:** OPEN
**Deploy:** NFRA_FIDUPL FT-s-12: the three schedule rule targets gain the :$DEFAULT version suffix (whole-root safe-apply, 3 in-place target updates)
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply of infra/aws/terraform/canonical-fidelity-ec2 (whole root, no -target): exactly 3 in-place updates of aws_cloudwatch_event_target.window | apply output Apply complete! Resources: 0 added, 3 changed, 0 destroyed |  | OPEN |
| L2 | verify | all three target ARNs end in :$DEFAULT and the rules stay ENABLED; post-apply plan No changes | ft12t R1-FT12T-OK; ft6r R1-FT6R-OK; plan rc=0 |  | OPEN |

## Log

- 20261021T095526Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 2 leg(s)
