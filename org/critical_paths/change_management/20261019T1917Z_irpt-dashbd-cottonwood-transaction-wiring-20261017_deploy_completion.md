# Deploy Completion Record
**Date opened:** 2026-10-19T19:17:40.180308+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-f-2703: Cottonwood transaction pair (packet REVISION 2, release commit 36da4e101f) -- build, plan 0/2/0, one safe-apply, dry runs, first write, range
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 30.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | release commit 36da4e101f in HEAD and the entry artifact_sha256 commit | hash on box branch |  | OPEN |
| L2 | verify | rollback targets (current VersionIds per settle day, data.parquet and manifest.json) | before.rollback_targets recorded |  | OPEN |
| L3 | s3-prefix | investor-reporting/irpt-cot-account-return-daily-lambda.zip new version | built b64 sha256 equals landed object |  | OPEN |
| L4 | activation | terraform plan 0/2/0 and one safe-apply, replan No changes | apply_finished_utc and after-read |  | OPEN |
| L5 | verify | scheduled-path dry run, one dry rewrite per settle day, transaction dry run | wrote nothing, 200 |  | OPEN |
| L6 | verify | first one-day transaction WRITE | partition exactly the newest writable day |  | OPEN |
| L7 | verify | bounded 25-trading-day RANGE | days_written + 1 partitions |  | OPEN |
| L8 | verify | first scheduled fire after the apply (issuer reads; ledger stays OPEN) | issuer read |  | OPEN |

## Log

- 20261019T191740Z OPENED by 0.7.0_AE_CloudOps~IB2 with 8 leg(s)
