# Deploy Completion Record
**Date opened:** 2026-09-17T13:33:52.177045+00:00
**Status:** OPEN
**Deploy:** OG-i-5: rename opal-gateway-access-state to the builder name gateway-access-state-table
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| create | activation | new table gateway-access-state-table + runtime/operator grant repoint (apply 1) | terraform apply1 plan JSON + describe-table |  | OPEN |
| copy | verify | full consistent scan of old vs new table, item-by-item digest equal | scan digest JSON evidence (counts + sha256, no content) |  | OPEN |
| retire | activation | old table opal-gateway-access-state destroy (apply 2) | terraform apply2 plan JSON + describe-table ResourceNotFound |  | OPEN |

## Log

- 20260917T133352Z OPENED by 0.9.0_WK_NFRA_OPLGTW~1 with 3 leg(s)
