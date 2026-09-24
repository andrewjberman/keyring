# Deploy Completion Record
**Date opened:** 2026-09-24T00:15:07.243133+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T001845Z
**Deploy:** YCharts roles: canonical current-authority reader grants; runner host AutoShutdown opt-out tag (no start)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | Saved plan 1de76039 via safe-apply | apply receipt: 0 add 3 change 0 destroy | Saved plan 1de760399ca1cd7f42e4b570c705f8e464500a1ba31a3da64a6a329d4c35006d applied via safe-apply from irpt-smoke-p-backend-20260923 at 2026-09-24T00:17:29Z under CTO GO 99821 item 3: 0 added, 3 changed (aws_iam_role_policy.generate, aws_iam_role_policy.runner, aws_instance.runner tags), 0 destroyed; halt gate 22 routine acknowledged, naming WARN only, tagauthz PASSED, tombstone CLEAN; .runtime/ycharts-authority/apply.log | CLOSED 20260924T001845Z |
| V1 | verify | Both role policies carry the three new Sids; host tag present; host still stopped; zero-diff | readback JSON + post plan rc 0 | Readback 00:18Z: irpt-ycharts-generate and irpt-ycharts-runner policies each carry ReadCanonicalUserProfileByEmailIndexAndKey (Query email-index), ReadCanonicalUserProfileRow (GetItem opal-users-v2), DecryptCanonicalUsersTableViaDynamoOnly (kms:Decrypt key 64f25291 via dynamodb, tableName opal-users-v2); host i-0167fd745ad906a66 tags now include AutoShutdown=disabled and State is still stopped (nothing started); ycharts state serial 15; post-apply plan rc 0 No changes; YCHARTS_AUTHORITY_APPLY_20260924.json | CLOSED 20260924T001845Z |

## Log

- 20260924T001507Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260924T001845Z LEG A1 closed: Saved plan 1de760399ca1cd7f42e4b570c705f8e464500a1ba31a3da64a6a329d4c35006d applied via safe-apply from irpt-smoke-p-bac
- 20260924T001845Z LEG V1 closed: Readback 00:18Z: irpt-ycharts-generate and irpt-ycharts-runner policies each carry ReadCanonicalUserProfileByEmailIndexA
- 20260924T001845Z CLOSED -- all 2 legs proven
