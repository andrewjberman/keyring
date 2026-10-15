# Deploy Completion Record
**Date opened:** 2026-10-15T13:07:38.993226+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-l-5 act 3 (plan M04 steps 1-2): move inf-portal-publisher's trigger from the opal-data-inf S3 notification (gold/meta/ + pipeline-complete.json) to the Scheduler floor. ONE scoped Terraform apply in infra/aws/terraform/inf-pipeline/ (-target the floor schedule, the catch-up schedule, the bucket notification): the daily floor advi-inf-publish-daily DISABLED -> ENABLED with target Input {}; the catch-up advi-inf-publish-catchup-daily created cron(30 16 * * ? *) UTC, same target, Input {}, same DLQ, retry 1 / 3600 s, window OFF, ENABLED (name via the opal_name module); the gold/meta/ entry removed from the bucket notification, the silver entry (silver/_silver_complete/ + .json -> inf-silver-aggregator) unchanged. Plan: 1 to add, 2 to change, 0 to destroy (the notification renders as a list-order diff of two blocks; end state is the silver entry alone, its auto-generated Id may change) or STOP. Pair: COO half a6e2df30dc + addendum 1 b72692a2bf, CTO half 1709a6e779 + ADDENDUM 1 52d04a8269 (conditional on FB-m-2 arm (a) MET and that day's publish: both hold, FB-m-2 closed a93a84d45d, served data_as_of 2026-10-15). Prior state: PRIOR_STATE_ACT3.json. Rollback: floor and catch-up DISABLED, gold/meta/ entry restored (Terraform revert + scoped safe-apply); if the day's publish is missed or half-written, ONE manual invoke after gold is read complete with prior VersionIds recorded first. First-day reads 2026-10-16 (13:30Z publishes the named set, 16:30Z halts with 0 writes, no marker-triggered invocation), by 18:00Z. Not in this act: M04 steps 3-6, any hand exercise, any code change.
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 30.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pair addenda at HEAD and unchanged; FB-m-2 closed with arm (a) MET; served data_as_of equals the day's holdings date; prior state saved (notification whole, floor definition) | the commits, the dates, PRIOR_STATE_ACT3.json |  | OPEN |
| L2 | git | the Terraform change committed (floor ENABLED with Input {}, catch-up schedule, gold/meta/ entry removed) | commit hash |  | OPEN |
| L3 | activation | scoped safe-apply: plan matches 1/2/0; apply; floor ENABLED Input {}; catch-up ENABLED cron(30 16 * * ? *); notification holds the silver entry alone (ARN, events, filters equal to before) | plan summary, apply line, the reads |  | OPEN |
| L4 | verify | first-day reads 2026-10-16 by 18:00Z: 13:30Z fire publishes the named set (advisor files written equal the count recorded before), 16:30Z fire halts with 0 writes, no marker-triggered invocation, advisor publisher no error, then MOVE_RECORD.json | the logs, VersionIds and counts |  | OPEN |

## Log

- 20261015T130738Z OPENED by 0.7.0_AE_CloudOps~FB1 with 4 leg(s)
