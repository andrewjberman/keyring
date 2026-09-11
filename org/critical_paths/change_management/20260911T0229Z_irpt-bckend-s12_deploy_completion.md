# Deploy Completion Record
**Date opened:** 2026-09-11T02:29:39.354494+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-s-12: apply the irpt-holdings-snapshot registered trigger slot (DISABLED) on the shared investor-reporting/directory root; land QA holdings snapshots in each firm bucket; attempt the rule-13 code deploy through the guard's explicit first-mint mechanism
**Authored by:** 0.9.0_WK_IRPT_BCKEND~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of holdings_snapshot.py, its tests and schedule.tf | commit hash on the worker branch |  | OPEN |
| L2 | activation | terraform apply of infra/aws/terraform/investor-reporting/directory (state key investor-reporting/directory/tfstate) | safe-apply Apply complete line with the resource count |  | OPEN |
| L3 | verify | post-apply live-state read via the IB-s-12 battery, plus head-object on each firm's QA latest.json | the battery output, every count beside its denominator |  | OPEN |
| L4 | verify | 0-diff plan on the applied root | terraform plan reading No changes |  | OPEN |

## Log

- 20260911T022939Z OPENED by 0.9.0_WK_IRPT_BCKEND~1 with 4 leg(s)
