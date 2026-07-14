# Deploy Completion Record
**Date opened:** 2026-07-14T08:42:28.890295+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260714T085811Z
**Deploy:** Z-plane Gate B: TARGETED safe-apply of the 6 fedobs producer resources ONLY (globgrph module). Auth: CTO~Z GO 083509Z (Andrew instantiation=routing), 3 conditions. Module total 7/1/0; targeted 6/0/0; SNS email sub + freeze_monitor EXCLUDED by target list.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | fedobs_producer.tf @ 78143ad7f on origin/CLOUD | commit on origin/CLOUD | 78143ad7f (fedobs_producer.tf) confirmed on origin/CLOUD via git branch -r --contains | CLOSED 20260714T084307Z |
| L2 | activation | safe-apply targeted 6 fedobs resources (globgrph) | targeted apply 6/0/0 + post-apply 0-diff re-plan on the targeted set | safe-apply of saved targeted plan gateB_fedobs_targeted.tfplan = 6 added/0 changed/0 destroyed (log-group+task-def+events-role+policy+rule+target); post-apply targeted re-plan = No changes (0-diff); SNS email sub NOT created, freeze_monitor NOT changed. task-def globgrph-fedobs-producer:1 live. | CLOSED 20260714T084549Z |
| L3 | verify | Rule 22a: simulate-principal-policy on NEW opal-globgrph-fedobs-producer-events role, ecs:RunTask on task-def ARN, one --resource-arns/call, positive control SEPARATE | three simulate outputs + live get-role-policy | Rule 22a: live get-role-policy shows exactly {RunTask on task-def globgrph-fedobs-producer:1; PassRole on emitter-task+derive-runner-execution}. simulate-principal-policy, 3 SEPARATE invocations one --resource-arns each: (1) RunTask on fedobs-producer:1=allowed; (2) NEG CONTROL RunTask on derive-runner:4=implicitDeny (discriminates, resource-scoped); (3) PassRole on emitter-task=allowed. Zero widening. | CLOSED 20260714T084942Z |
| L4 | verify | served handshake: run-task exercise -> marker_pin.pinned=true + verified_stable=true on served fedobs_observations.json | served row read (baseline: frozen 07-08, no marker_pin) | run-task 4dd7aabf (new :latest image) exited 0. Served fedobs_observations.json UNFROZEN: LastModified 2026-07-08 02:15Z -> 2026-07-14 08:51:01Z, size 6562 -> 426888, ETag 3dbf1bb9 -> b02376c6, computed_at 1783476909 -> 1784019051. marker_pin.pinned=True + verified_stable=True; pinned_snapshot_id=7392125655251158233; marker_head==marker_head_end (c155b488...) bracket-equal=stable vintage; source_table iceberg.globgrph.cse, cse_log_total=342. | CLOSED 20260714T085811Z |

## Log

- 20260714T084228Z OPENED by 0.7.0_AE_CloudOps~Z with 4 leg(s)
- 20260714T084307Z LEG L1 closed: 78143ad7f (fedobs_producer.tf) confirmed on origin/CLOUD via git branch -r --contains
- 20260714T084549Z LEG L2 closed: safe-apply of saved targeted plan gateB_fedobs_targeted.tfplan = 6 added/0 changed/0 destroyed (log-group+task-def+event
- 20260714T084942Z LEG L3 closed: Rule 22a: live get-role-policy shows exactly {RunTask on task-def globgrph-fedobs-producer:1; PassRole on emitter-task+d
- 20260714T085811Z LEG L4 closed: run-task 4dd7aabf (new :latest image) exited 0. Served fedobs_observations.json UNFROZEN: LastModified 2026-07-08 02:15Z
- 20260714T085811Z CLOSED -- all 4 legs proven
