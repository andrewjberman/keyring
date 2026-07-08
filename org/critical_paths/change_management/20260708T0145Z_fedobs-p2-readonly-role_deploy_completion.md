# Deploy Completion Record
**Date opened:** 2026-07-08T01:45:52.125735+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260708T015019Z
**Deploy:** NFRA_FEDOBS.P2 productionization: apply the fedobs-trino read-only emitter role (Deny-overrides-Allow on semantic-truth prefixes = AC2 boundary made physical) on CVO measure-honesty cert
**Authored by:** 0.5.0_AE_OpalETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply (targeted, HALTGT) the 3 fedobs.tf resources: fedobs_emitter_task role + fedobs_write_scoped + fedobs_emitter_logs | apply complete + 0-diff re-plan | targeted plan post-refresh (refreshed against LIVE) = 'No changes, matches configuration' -- the 3 fedobs resources already APPLIED live (prior 0.7.0~B coordinated apply); 0-diff, no re-apply needed | CLOSED 20260708T015018Z |
| L2 | verify | aws iam get-role-policy FedobsWriteScoped shows the FedobsDenyWriteTruth Deny APPLIED (live, not TF-desired) | get-role-policy Deny statement present | get-role-policy FedobsWriteScoped: FedobsDenyWriteTruth = Deny PutObject/DeleteObject on warehouse/globgrph/* (covers cse) + tool_activity/* -- APPLIED live | CLOSED 20260708T015018Z |
| L3 | verify | AC2 write-fail-closed EXERCISE: a live PutObject to a truth prefix from the fedobs role -> AccessDenied (403), CVO boundary re-verify | 403 AccessDenied on truth-prefix write | AC2 write-403 EXERCISE (ecs run-task taskRoleArn=fedobs role in-VPC): cse prefix->AccessDenied(403); tool_activity->AccessDenied; fedobs_signals->ALLOWED (Deny correctly scoped). Boundary REAL/applied (Rule 22a). Litter cleaned. | CLOSED 20260708T015018Z |

## Log

- 20260708T014552Z OPENED by 0.5.0_AE_OpalETL with 3 leg(s)
- 20260708T015018Z LEG L1 closed: targeted plan post-refresh (refreshed against LIVE) = 'No changes, matches configuration' -- the 3 fedobs resources alre
- 20260708T015018Z LEG L2 closed: get-role-policy FedobsWriteScoped: FedobsDenyWriteTruth = Deny PutObject/DeleteObject on warehouse/globgrph/* (covers cs
- 20260708T015018Z LEG L3 closed: AC2 write-403 EXERCISE (ecs run-task taskRoleArn=fedobs role in-VPC): cse prefix->AccessDenied(403); tool_activity->Acce
- 20260708T015019Z CLOSED -- all 3 legs proven
