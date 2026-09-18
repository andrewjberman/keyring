# Deploy Completion Record
**Date opened:** 2026-09-17T13:33:52.177045+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260917T144043Z
**Deploy:** OG-i-5: rename opal-gateway-access-state to the builder name gateway-access-state-table
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| create | activation | new table gateway-access-state-table + runtime/operator grant repoint (apply 1) | terraform apply1 plan JSON + describe-table | apply1 rc0 'Apply complete! Resources: 1 added, 2 changed, 0 destroyed.' 2026-09-17T13:44Z-ish; describe-table gateway-access-state-table ACTIVE SSE/PITR/PAY_PER_REQUEST/TTL expires_at confirmed (evidence/og_i5/new_table_describe.json, new_table_ttl.json, new_table_pitr.json); saved plan evidence/og_i5/apply1.plan.json (1 create + 2 update + 0 destroy) | CLOSED 20260917T144042Z |
| copy | verify | full consistent scan of old vs new table, item-by-item digest equal | scan digest JSON evidence (counts + sha256, no content) | 7 of 7 items copied old->new under attribute_not_exists(pk), 0 condition failures (og_i5_copy.py); post-cutover full consistent scan both tables equal counts (7=7) and per-item sha256 digest equal across all namespaces incl. operator_audit (evidence/og_i5/post_cutover_old_digest.json, post_cutover_new_digest.json); OGI5-AC5/AC6/AC13 PASS at commit 87d64458e6 | CLOSED 20260917T144042Z |
| retire | activation | old table opal-gateway-access-state destroy (apply 2) | terraform apply2 plan JSON + describe-table ResourceNotFound | apply2 rc0 'Apply complete! Resources: 0 added, 0 changed, 1 destroyed.' at 2026-09-17T14:36:49Z-14:36:56Z; describe-table opal-gateway-access-state -> ResourceNotFoundException; saved plan evidence/og_i5/apply2.plan.json (0 add, 0 change, 1 destroy: aws_dynamodb_table.access_state_old only) | CLOSED 20260917T144043Z |

## Log

- 20260917T133352Z OPENED by 0.9.0_WK_NFRA_OPLGTW~1 with 3 leg(s)
- 20260917T144042Z LEG create closed: apply1 rc0 'Apply complete! Resources: 1 added, 2 changed, 0 destroyed.' 2026-09-17T13:44Z-ish; describe-table gateway-a
- 20260917T144042Z LEG copy closed: 7 of 7 items copied old->new under attribute_not_exists(pk), 0 condition failures (og_i5_copy.py); post-cutover full con
- 20260917T144043Z LEG retire closed: apply2 rc0 'Apply complete! Resources: 0 added, 0 changed, 1 destroyed.' at 2026-09-17T14:36:49Z-14:36:56Z; describe-tab
- 20260917T144043Z CLOSED -- all 3 legs proven
