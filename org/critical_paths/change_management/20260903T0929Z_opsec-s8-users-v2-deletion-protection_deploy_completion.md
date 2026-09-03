# Deploy Completion Record
**Date opened:** 2026-09-03T09:29:56.440870+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609.TO-OP-S-8 -- deletion_protection_enabled on opal-users-v2 at its REAL carrier shared-infra/dynamo.tf, SCOPED -target apply (shared-infra carries unrelated pre-existing drift that must not ride)
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | shared-infra/dynamo.tf edit committed under 0.7.0_AE_CloudOps~S | commit hash |  | OPEN |
| L2 | activation | safe-apply -target=aws_dynamodb_table.opal_users_v2 (1 change, 0 add, 0 destroy, 0 replace) | apply output |  | OPEN |
| L3 | verify | DeletionProtectionEnabled true + PITR still ENABLED + SSE unchanged + TableId identical before/after | pasted reads |  | OPEN |
| L4 | verify | UNSCOPED re-plan: opal_users_v2 shows 0-diff and the pre-existing global_graph drift is STILL THERE untouched (the scoped-check trap: a -target apply must not be verified by a -target re-plan) | unscoped plan output |  | OPEN |

## Log

- 20260903T092956Z OPENED by 0.7.0_AE_CloudOps~S with 4 leg(s)
