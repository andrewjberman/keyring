# Deploy Completion Record
**Date opened:** 2026-10-21T10:53:55.525265+00:00
**Status:** OPEN
**Deploy:** NFRA_FIDUPL FT-s-15: automation-execution/* added to the schedule policy (whole-root safe-apply, 1 in-place update), then ONE temporary one-shot EventBridge rule outside Terraform to prove the schedule role path, deleted after its read
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply of infra/aws/terraform/canonical-fidelity-ec2 (whole root, no -target): exactly 1 in-place update of aws_iam_role_policy.schedule (one added Resource) | apply output Apply complete! Resources: 0 added, 1 changed, 0 destroyed | BEFORE: simulator (schedule role, automation-execution/*, one resource) implicitDeny; ft15s FAIL; CloudTrail 10:45:04Z AccessDenied on automation-execution/*. safe-apply of the saved reviewed plan, whole root, no -target, about 10:56Z: Plan 0 to add, 1 to change, 0 to destroy (aws_iam_role_policy.schedule, one added Resource: automation-execution/*); Apply complete! Resources: 0 added, 1 changed, 0 destroyed. | CLOSED 20261021T105752Z |
| L2 | verify | ft15s R1-FT15S-OK on all 3 resource forms; post-apply plan No changes | ft15s; plan rc=0 | ft15s: R1-FT15S-OK schedule start allowed on all 3 resource forms; ft6r: R1-FT6R-OK the three schedule rules are ENABLED; post-apply plan No changes rc=0; fu6g OK. | CLOSED 20261021T105753Z |
| L3 | activation | ONE temporary rule fidelity-alongside-oneshot-proof-20261021 created, fired once, execution read | execution id, terminal status, step names, wrapper run record, metric counts, or CloudTrail errorMessage |  | OPEN |
| L4 | verify | the temporary rule and target are removed; only the three standing rules remain | list-rules --name-prefix fidelity-alongside-oneshot is empty; ft6r R1-FT6R-OK |  | OPEN |

## Log

- 20261021T105355Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 4 leg(s)
- 20261021T105752Z LEG L1 closed: BEFORE: simulator (schedule role, automation-execution/*, one resource) implicitDeny; ft15s FAIL; CloudTrail 10:45:04Z A
- 20261021T105753Z LEG L2 closed: ft15s: R1-FT15S-OK schedule start allowed on all 3 resource forms; ft6r: R1-FT6R-OK the three schedule rules are ENABLED
