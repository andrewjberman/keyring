# Deploy Completion Record
**Date opened:** 2026-10-01T10:35:03.336095+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPINDEX MX-s-16: one writer per BD silver table (unrealized, allocations, transactions retired behind bd-silver-merge; realized HELD)
**Authored by:** 0.9.0_WK_NFRA_MCPINDEX~24
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 20.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | opal-data-bd code/silver/merge-daily-incremental.py (DS deploy via safe-deploy.sh; rollback ETag c54d0790) | safe-deploy MATCH line + head-object md5 91eaf248 |  | OPEN |
| U2 | activation | SSM opal-bd-unrealized-download no-op v4 set DEFAULT | Default==Latest==4 read-back |  | OPEN |
| A1 | activation | SSM opal-bd-allocation-download no-op v6 set DEFAULT | Default==Latest==6 read-back |  | OPEN |
| T0 | verify | read-only consumer trace of same-day silver/transactions/<date>.parquet existence | recorded readers list; 0 same-day-existence consumers else HOLD |  | OPEN |
| T1 | activation | SSM opal-bd-transaction-download no-op v4 set DEFAULT (only if T0 clean) | Default==Latest==4 read-back |  | OPEN |
| TF | activation | safe-apply targeted plan sha af1537fd: rules unrealized+transaction+allocation DISABLED, ProcessAllocationFiles notification removed | Plan 0/4/0 line + Apply complete line + describe-rule DISABLED x3 + notification ids read-back |  | OPEN |
| AC | verify | s16.AC1 (3 of 4 tables at 1 writer, realized 2 by ruling) and s16.AC2 read-back; scheduled bd-silver-merge run ~00:1xZ reads failures=0 empty_stub=6 on unrealized | AC outputs + the scheduled run's log line |  | OPEN |
| G1 | git | ledger entry + sentinel + deliverables committed on wk-nfra_mcpindex-6-24 | commit hash |  | OPEN |

## Log

- 20261001T103503Z OPENED by 0.9.0_WK_NFRA_MCPINDEX~24 with 8 leg(s)
