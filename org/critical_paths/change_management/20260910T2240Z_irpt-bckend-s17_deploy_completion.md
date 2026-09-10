# Deploy Completion Record
**Date opened:** 2026-09-10T22:40:29.777518+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-s-17: apply the investor-reporting core root (KMS, opal-data-ycharts, 4 DynamoDB tables, 3 queues + 3 DLQs, the declared layout)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of the core root sources and the key grammar | commit hash on the worker branch |  | OPEN |
| L2 | activation | terraform apply of infra/aws/terraform/investor-reporting/core (state key investor-reporting/core/tfstate) | safe-apply Apply complete line with the resource count |  | OPEN |
| L3 | verify | post-apply live-state read of the bucket, the four tables and the six queues | the IB-s-17 battery output, every count beside its denominator |  | OPEN |
| L4 | verify | 0-diff plan on the applied root | terraform plan reading No changes |  | OPEN |

## Log

- 20260910T224029Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 4 leg(s)
