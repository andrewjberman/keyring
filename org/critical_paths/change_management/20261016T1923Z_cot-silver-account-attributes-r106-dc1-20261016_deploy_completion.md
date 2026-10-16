# Deploy Completion Record
**Date opened:** 2026-10-16T19:23:11.303129+00:00
**Status:** OPEN
**Deploy:** ADVI_COTBKF TO-CB-dc-1: one added line in cot-pipeline ssm.tf so opal-cot-silver-run merges account_attributes (aws_ssm_document.cot_silver_run, in place; blast radius 1 resource; rollback: ssm update-document-default-version --document-version 4 then revert line and reconcile, or revert line and safe-apply)
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pair verified + world re-read (doc v4 hash 83b3fc89, manifest VersionId, 1 partition key) | read-back lines |  | OPEN |
| L2 | activation | safe-apply of saved plan (1 change, in place) | apply line + new doc version |  | OPEN |
| L3 | git | ssm.tf commit on box/dell1 | hash + push state |  | OPEN |
| L4 | verify | AC1 doc + AC2 state | criterion output lines |  | OPEN |

## Log

- 20261016T192311Z OPENED by 0.7.0_AE_CloudOps~FB1 with 4 leg(s)
