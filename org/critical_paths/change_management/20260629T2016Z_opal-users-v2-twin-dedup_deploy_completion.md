# Deploy Completion Record
**Date opened:** 2026-06-29T20:16:31.991944+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260629T201926Z
**Deploy:** opal_users_v2 (AUTH DDB) double-management de-dup: drop the portal-auth TWIN, keep shared-infra canonical. GROUNDED: shared-infra config has point_in_time_recovery=enabled (matches LIVE PITR=ENABLED, deliberate import CDRS_TFIMPT.006); portal-auth twin LACKS the PITR block (a portal-auth apply would DISABLE PITR -- actively harmful). NEVER-WIDEN: live table is NEVER touched -- only state-rm from portal-auth + remove the config block; portal-auth/iam.tf hardcoded-ARN grants stay. CVO dispatch a47d169ef.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | terraform state rm from portal-auth (live table untouched) + portal-auth plan shows NO destroy of opal-users-v2 | state rm output + plan | terraform state rm aws_dynamodb_table.opal_users_v2 in portal-auth -> 'Successfully removed 1 resource instance(s)'; confirmed gone from portal-auth state list. portal-auth plan post-block-removal: 'No changes. Your infrastructure matches the configuration' -> NO destroy/create of opal-users-v2. Live table untouched. | CLOSED 20260629T201857Z |
| L2 | git | CLOUD commit removing the portal-auth resource block | hash pushed | commit 1f6fa344d pushed CLOUD (portal-auth/dynamodb.tf: 9 ins/52 del, twin block removed). | CLOSED 20260629T201925Z |
| L3 | verify | shared-infra plan 0-diff on opal_users_v2 (canonical owner consistent, PITR on) + portal-auth 0-diff | both plans | shared-infra plan -target opal_users_v2: 'No changes. Your infrastructure matches the configuration' (canonical owner consistent, live PITR=ENABLED preserved). portal-auth plan: 'No changes' (twin fully removed, live table untouched). | CLOSED 20260629T201926Z |

## Log

- 20260629T201631Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
- 20260629T201857Z LEG L1 closed: terraform state rm aws_dynamodb_table.opal_users_v2 in portal-auth -> 'Successfully removed 1 resource instance(s)'; con
- 20260629T201925Z LEG L2 closed: commit 1f6fa344d pushed CLOUD (portal-auth/dynamodb.tf: 9 ins/52 del, twin block removed).
- 20260629T201926Z LEG L3 closed: shared-infra plan -target opal_users_v2: 'No changes. Your infrastructure matches the configuration' (canonical owner co
- 20260629T201926Z CLOSED -- all 3 legs proven
