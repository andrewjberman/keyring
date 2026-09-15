# Deploy Completion Record
**Date opened:** 2026-09-15T02:29:15.576812+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260915T023659Z
**Deploy:** AMGT_RESAPP AMGT-ri-2: the chatter-axis producer consolidates into the harvest root and is repointed at the LIVE harvest tables
**Authored by:** 0.9.0_WK_AMGT_RESAPP~17
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | wk-amgt_resapp-10-2 branch commits (consolidation ea6cd450fa + AC12 builder 6cb6442158 + this ledger entry) | commit hash on the worker branch | worker branch wk-amgt_resapp-10-2 (LOCAL, never pushed by a worker): ea6cd450fa consolidation (R052/R082/R080 renames into infra/aws/terraform/harvest/, D amgt-resapp/main.tf, M s3.tf), 6cb6442158 AC12 builder + rows W17-S3/W17-S4, 245a9f568d this ledger entry and its sentinel | CLOSED 20260915T023628Z |
| L2 | activation | terraform apply of .scratch/ri2.tfplan into harvest/tfstate (6 imported producer resources; 0 add, 4 change, 0 destroy) | Apply complete! line with 0 destroyed | HALT_ACK=1 safe-apply -chdir=infra/aws/terraform/harvest apply .scratch/ri2.tfplan -> apply-rc=0, 'Apply complete! Resources: 0 added, 4 changed, 0 destroyed.' Destroy tokens 0, Creating tokens 0 across 67 lines. Halt gate resolved worker 0.9.0_WK_AMGT_RESAPP~17 and scanned issuer 2.0.0_SA_COO~W. Full output: deliverables/0.9.0_WK_AMGT_RESAPP~17/ri2.apply.txt | CLOSED 20260915T023628Z |
| L3 | verify | live amgt-resapp-chatter-axis function code hash + amgt-resapp-chatter-axis-lambda-policy Resource ARNs | get-function-configuration CodeSha256 equals the local zip sha256 b64 AND get-role-policy shows harvest tables with 0 opal-amgt- tokens | LIVE plane read after the apply: get-function-configuration amgt-resapp-chatter-axis -> CodeSha256 fj8wqp9jaZWfMaBrrAyUImGnt2c5Xeb7losUr+i65mM=, LastModified 2026-09-15T02:33:20.000+0000, CodeSize 24370. That hash EQUALS the local zip sha256 b64 and is NOT the pre-cell TtTSpotkwWuVuMFbPv0RWTv2zqqifa/xfHQtBtuo924= (13572 bytes, 2026-09-11). get-role-policy amgt-resapp-chatter-axis-lambda-policy Resource list -> harvest-articles 2, harvest-metrics 1, old-amgt 0 | CLOSED 20260915T023658Z |
| L4 | verify | QA invoke of amgt-resapp-chatter-axis and today's TRENDING_CHATTER partition in opal-harvest-security-metrics | StatusCode 200 with no FunctionError, rows_written greater than 0, and a non-zero COUNT for today against a zero COUNT for 2026-09-13 | QA invoke (ad-hoc QA is permitted; the 10:00Z scheduled fire remains the acceptance): StatusCode 200, FunctionError None, payload {"as_of_date": "2026-09-15", "tickers_considered": 34, "rows_ranked": 10, "rows_written": 10}. DynamoDB opal-harvest-security-metrics COUNT TRENDING_CHATTER#2026-09-15 = 10 against the discriminating control COUNT TRENDING_CHATTER#2026-09-13 = 0 (the day the pre-cell producer failed all 3 fires) | CLOSED 20260915T023658Z |

## Log

- 20260915T022915Z OPENED by 0.9.0_WK_AMGT_RESAPP~17 with 4 leg(s)
- 20260915T023628Z LEG L1 closed: worker branch wk-amgt_resapp-10-2 (LOCAL, never pushed by a worker): ea6cd450fa consolidation (R052/R082/R080 renames in
- 20260915T023628Z LEG L2 closed: HALT_ACK=1 safe-apply -chdir=infra/aws/terraform/harvest apply .scratch/ri2.tfplan -> apply-rc=0, 'Apply complete! Resou
- 20260915T023658Z LEG L3 closed: LIVE plane read after the apply: get-function-configuration amgt-resapp-chatter-axis -> CodeSha256 fj8wqp9jaZWfMaBrrAyUI
- 20260915T023658Z LEG L4 closed: QA invoke (ad-hoc QA is permitted; the 10:00Z scheduled fire remains the acceptance): StatusCode 200, FunctionError None
- 20260915T023659Z CLOSED -- all 4 legs proven
