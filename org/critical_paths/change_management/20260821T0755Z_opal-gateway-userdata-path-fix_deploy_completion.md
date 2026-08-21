# Deploy Completion Record
**Date opened:** 2026-08-21T07:55:42.306719+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260821T080355Z
**Deploy:** opal-gateway user_data path fix (main.tf:191/:193) -- Andrew-direct sovereign approval + apply-now ruling
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | terraform plan reads in-place 0-destroy | plan output pinned | plan: 0 to add, 1 to change, 0 to destroy; ~ aws_instance.gw updated IN-PLACE, user_data e30a45cb->8b3d8fe1. ignore_changes covers ami only, so replacement was a live question; plan answered it | CLOSED 20260821T080355Z |
| L2 | activation | safe-apply of aws_instance.gw user_data | apply rc + resource updated | safe-apply.sh apply (Rule 18, HALT_ACK=1 for routine pending), rc=0. aws_instance.gw modified ~1m40s. APPLIED TRUTH read back from AWS via describe-instance-attribute --attribute userData: holds /opt/opal-gateway and the resolving citation | CLOSED 20260821T080355Z |
| L3 | verify | 0-diff re-plan | plan shows no changes | terraform plan -detailed-exitcode -> 'No changes. Your infrastructure matches the configuration.' TRUE rc=0 UNPIPED | CLOSED 20260821T080355Z |
| L4 | verify | gateway live after the bounce | systemd active + /mcp 401 through ALB | ON-BOX via SSM: systemd active + enabled, MainPID cwd=/opt/opal-gateway, on-box /health 200, up 4 minutes. THROUGH ALB: /mcp 401 x3 (auth enforcing, identical to pre-state), ALB target healthy. IP changed 3.83.108.63 -> 13.221.151.249 as predicted; instance ID unchanged (not replaced) | CLOSED 20260821T080355Z |

## Log

- 20260821T075542Z OPENED by 0.7.0_AE_CloudOps with 4 leg(s)
- 20260821T080355Z LEG L1 closed: plan: 0 to add, 1 to change, 0 to destroy; ~ aws_instance.gw updated IN-PLACE, user_data e30a45cb->8b3d8fe1. ignore_chan
- 20260821T080355Z LEG L2 closed: safe-apply.sh apply (Rule 18, HALT_ACK=1 for routine pending), rc=0. aws_instance.gw modified ~1m40s. APPLIED TRUTH read
- 20260821T080355Z LEG L3 closed: terraform plan -detailed-exitcode -> 'No changes. Your infrastructure matches the configuration.' TRUE rc=0 UNPIPED
- 20260821T080355Z LEG L4 closed: ON-BOX via SSM: systemd active + enabled, MainPID cwd=/opt/opal-gateway, on-box /health 200, up 4 minutes. THROUGH ALB: 
- 20260821T080355Z CLOSED -- all 4 legs proven
