# Deploy Completion Record
**Date opened:** 2026-10-01T10:35:03.336095+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T002841Z -- gate: external / scheduled bd-silver-merge run ~00:1xZ 2026-10-02 (S3 sentinel bronze/2026-10-02/_BRONZE_COMPLETE.json -> BronzeCompleteSilverMerge): must read failures=0 empty_stub=6 on unrealized; acceptance AC leg (held since 2026-10-01T10:56:43.866228+00:00)
**Deploy:** NFRA_MCPINDEX MX-s-16: one writer per BD silver table (unrealized, allocations, transactions retired behind bd-silver-merge; realized HELD)
**Authored by:** 0.9.0_WK_NFRA_MCPINDEX~24
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 20.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | opal-data-bd code/silver/merge-daily-incremental.py (DS deploy via safe-deploy.sh; rollback ETag c54d0790) | safe-deploy MATCH line + head-object md5 91eaf248 | safe-deploy.sh rc=0 'VERIFY OK comp-pipescript deployed ...merge-daily-incremental.py' ; comp-pipescript Summary 1 MATCH, 0 STALE; head-object ETag 91eaf2486fc56ece76db2f0d862096f7 59820 B VersionId ZrPu_8iVGmN5ItxGuc6KxfVP_Z.U1.Qh 2026-10-01T10:36:31Z (prior c54d0790 VersionId gDNvsypwihDy3Rd6KfZ0CosUiD.MM3ma retained) | CLOSED 20261001T103719Z |
| U2 | activation | SSM opal-bd-unrealized-download no-op v4 set DEFAULT | Default==Latest==4 read-back | update-document opal-bd-unrealized-download -> v4 (Latest 4); update-document-default-version -> 4; describe-document read-back Default=4 Latest=4 Status=Active (10:37-10:38Z) | CLOSED 20261001T103851Z |
| A1 | activation | SSM opal-bd-allocation-download no-op v6 set DEFAULT | Default==Latest==6 read-back | update-document opal-bd-allocation-download -> v6 (Latest 6); update-document-default-version -> 6; describe-document read-back Default=6 Latest=6 Status=Active (10:38Z) | CLOSED 20261001T103851Z |
| T0 | verify | read-only consumer trace of same-day silver/transactions/<date>.parquet existence | recorded readers list; 0 same-day-existence consumers else HOLD | Read-only trace done 10:40-10:50Z: readers of silver/transactions listed (build_schwab_bd_account_xref, bd_price_update, A_00/A_01/A_03/A_04, B_01, B_03, C_01 nna_flows, gold_dispatch.sh check_freshness, gold_freshness_config.yaml bd_silver_transactions ERROR 48h). HIT: comp-freshness gate on newest LastModified blocks gold dispatch (FAIL) without the document's gap-day write: 8 of 8 Tue slots (4 of 4 weeks) read 51.7-94.7h vs 1.1-6.1h. Row NFRA_MCPINDEX-Z-W24-S8 BLOCKING/ARMED. Outcome: HOLD transactions. | CLOSED 20261001T104757Z |
| T1 | activation | SSM opal-bd-transaction-download no-op v4 set DEFAULT (only if T0 clean) | Default==Latest==4 read-back | NOT APPLIED -- HELD by the consumer trace (row Z-W24-S8): opal-bd-transaction-download stays v3 DEFAULT (Default==Latest==3 read-back), bd-transaction-pipeline-trigger stays ENABLED; no act on this key, nothing to roll back | CLOSED 20261001T104758Z |
| TF | activation | safe-apply targeted plan sha af1537fd: rules unrealized+transaction+allocation DISABLED, ProcessAllocationFiles notification removed | Plan 0/4/0 line + Apply complete line + describe-rule DISABLED x3 + notification ids read-back | re-plan 'Plan: 0 to add, 3 to change, 0 to destroy.' (transactions held; 2 rules + notification; saved binary sha256 3e97fe2c2481f54dc9be080bd602286a219776b03b092ff0f021fc39d78a45a7); safe-apply rc=0 'Apply complete! Resources: 0 added, 3 changed, 0 destroyed.'; read-back: bd-unrealized-pipeline-trigger DISABLED, bd-allocation-pipeline-trigger DISABLED, bd-transaction/realized ENABLED; notifications now GoldLayerPricesTrigger + BronzeCompleteSilverMerge (2), EventBridgeConfiguration {} unchanged; bd-allocation-processor Lambda LastModified 2026-04-06 (untouched) | CLOSED 20261001T105432Z |
| AC | verify | s16.AC1 (3 of 4 tables at 1 writer, realized 2 by ruling) and s16.AC2 read-back; scheduled bd-silver-merge run ~00:1xZ reads failures=0 empty_stub=6 on unrealized | AC outputs + the scheduled run's log line | Read 2026-10-02T00:24Z by 2.0.0_SA_COO~MI. The SCHEDULED bd-silver-merge run (invoked 2026-10-02T00:11:36Z, sentinel run_date=2026-10-02, merge --all) logged: transactions 'failures=0 rows_added=246777'; allocations 'new=0 reprocess=0 skip=131'; realized 'failures=0 rows_added=9,172'; unrealized 'SUMMARY: 6 processed \| new=6 \| failures=0 \| rows_added=0 \| empty_stub=6' (was failures=6 on 09-30 and 10-01: Z-S72 disarmed by the deployed fix 91eaf248). s16.AC2: graded tables with a clean newest run 3 of 3, RESULT: PASS. s16.AC1 scoped to the A2-retired tables (A3): unrealized 1 writer, allocations 1 writer, graded 2 of 2, RESULT: PASS; transactions and realized at 2 writers each by the A2 HOLD (unscoped control reads 2 of 4, FAIL, as ruled). Tonight's document slots: unrealized/allocation did not fire (rules DISABLED), transaction 21:53Z and realized 21:46Z fired Success (held). | CLOSED 20261002T002841Z |
| G1 | git | ledger entry + sentinel + deliverables committed on wk-nfra_mcpindex-6-24 | commit hash | branch wk-nfra_mcpindex-6-24 LOCAL (nothing pushed): b1301bd64e (ledger open) and f4f3e2a629 (PHASE B work, plan render, read-back, row S8) | CLOSED 20261001T105643Z |

## Log

- 20261001T103503Z OPENED by 0.9.0_WK_NFRA_MCPINDEX~24 with 8 leg(s)
- 20261001T103719Z LEG U1 closed: safe-deploy.sh rc=0 'VERIFY OK comp-pipescript deployed ...merge-daily-incremental.py' ; comp-pipescript Summary 1 MATCH
- 20261001T103851Z LEG U2 closed: update-document opal-bd-unrealized-download -> v4 (Latest 4); update-document-default-version -> 4; describe-document re
- 20261001T103851Z LEG A1 closed: update-document opal-bd-allocation-download -> v6 (Latest 6); update-document-default-version -> 6; describe-document re
- 20261001T104757Z LEG T0 closed: Read-only trace done 10:40-10:50Z: readers of silver/transactions listed (build_schwab_bd_account_xref, bd_price_update,
- 20261001T104758Z LEG T1 closed: NOT APPLIED -- HELD by the consumer trace (row Z-W24-S8): opal-bd-transaction-download stays v3 DEFAULT (Default==Latest
- 20261001T105432Z LEG TF closed: re-plan 'Plan: 0 to add, 3 to change, 0 to destroy.' (transactions held; 2 rules + notification; saved binary sha256 3e9
- 20261001T105643Z LEG G1 closed: branch wk-nfra_mcpindex-6-24 LOCAL (nothing pushed): b1301bd64e (ledger open) and f4f3e2a629 (PHASE B work, plan render,
- 20261001T105643Z HELD-SOVEREIGN-GATED gate=external/scheduled bd-silver-merge run ~00:1xZ 2026-10-02 (S3 sentinel bronze/2026-10-02/
- 20261002T002841Z LEG AC closed: Read 2026-10-02T00:24Z by 2.0.0_SA_COO~MI. The SCHEDULED bd-silver-merge run (invoked 2026-10-02T00:11:36Z, sentinel run
- 20261002T002841Z CLOSED -- all 8 legs proven
