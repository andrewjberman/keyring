# Deploy Completion Record
**Date opened:** 2026-09-03T09:21:55.357351+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609.TO-OP-S-8 -- PITR + deletion protection on the partner identity tables (module partner-firm-table, 3 instantiations); opal-users-v2 limb HELD on row Z-S15; demo limb DEFERRED to round 2 per issuer 19600
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | module edit committed on SITEZ under 0.7.0_AE_CloudOps~S | commit hash |  | OPEN |
| L2 | activation | safe-apply of infra/aws/terraform/partner-firms (0 add, 3 change, 0 destroy, 0 replace) | apply output |  | OPEN |
| L3 | verify | PITR + DeletionProtectionEnabled read ENABLED/true on all 3 partner tables, TableId identical before/after (no replace) | pasted reads |  | OPEN |
| L4 | verify | partner-firms re-plan 0-diff after apply | plan output |  | OPEN |

## Log

- 20260903T092155Z OPENED by 0.7.0_AE_CloudOps~S with 4 leg(s)
