# Deploy Completion Record
**Date opened:** 2026-09-10T23:52:05.890031+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-s-5: apply the FirmDestinationPolicy IAM half on the investor-reporting core root (3 firm role stubs + 1 quarantine role stub, per-firm S3 prefix conditions, the generated policy document)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of roles.tf, iam_firm_conditions.tf, outputs.tf and the ingestion gate | commit hash on the worker branch |  | OPEN |
| L2 | activation | terraform apply of infra/aws/terraform/investor-reporting/core (state key investor-reporting/core/tfstate) | safe-apply Apply complete line with the resource count |  | OPEN |
| L3 | verify | post-apply live-state read of the roles, policies and the generated policy document via the IB-s-5 battery | the battery output, every count beside its denominator |  | OPEN |
| L4 | verify | 0-diff plan on the applied root | terraform plan reading No changes |  | OPEN |

## Log

- 20260910T235205Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 4 leg(s)
