# Deploy Completion Record
**Date opened:** 2026-06-25T15:47:36.157397+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260625T155339Z
**Deploy:** ADVI_BDAPIMIG P1-B: 49F scheduled REST-pull runner Lambda + daily schedule (8 add, additive) + shared script deployed to opal-data-bd/code/bronze/
**Authored by:** 0.6.0_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commits eb0ce40f6(guard)+f6ca77914(runner)+28420f49d(sha) + bd tag pushed | hashes/tag --follow-tags | Pushed CLOUD edbca164f..4f8f24714 (eb0ce40f6 guard, f6ca77914 runner, 28420f49d sha, record-deploy) + tag bd-v2.35.0 --follow-tags | CLOSED 20260625T155119Z |
| L2 | s3-prefix | shared cot_bronze_ingest.py (guarded) deployed to opal-data-bd/code/bronze/ | aws s3 ls confirms 27119b object 2026-06-25 | aws s3 ls s3://opal-data-bd/code/bronze/cot_bronze_ingest.py = 27119b @ 2026-06-25 (guarded single-source deployed to bd's OWN code prefix, Model-B firm-bound) | CLOSED 20260625T155119Z |
| L3 | activation | bd-49f-runner Lambda + bd-49f-runner-daily cron(0 2) rule live via TF apply 8-add | 0-diff plan + live get-function/describe-rule | safe-apply 8-add/0-change/0-destroy; 0-diff (No changes). Live: bd-49f-runner Lambda + bd-49f-runner-daily cron(0 2 UTC) rule + bd-49f-runner-role (opal-data-bd-scoped + explicit cot Deny) created. | CLOSED 20260625T155119Z |
| L4 | verify | firm-sep dry-run FAILS (49f+BD_S3_BUCKET-unset aborts, proven) + live single-table runner smoke lands forwardfill_v2 | guard matrix + live invoke result (CVO runs the close-gate dry-run personally) | Firm-sep guard matrix PROVEN (4 cases: 49f+unset=ABORT, 49f+cot=ABORT, 49f+bd=PASS, cot-default=no-abort). Live runner smoke (table=transactions): log 'firm=49f bucket=opal-data-bd / auth OK / [transactions] run=483531 polling / OK: ingested transactions (76171426 bytes) -> s3://opal-data-bd/forwardfill_v2/transactions/TRANSACTIONS_DAILY_2026-06-25.xlsx / RESULT landed=[transactions] failed=[] auth_dead=False'. 222s/201MB. End-to-end: script-pull+guard-pass+auth+query+poll+download+land all live-proven. CVO runs the script-level dry-run as her independent close-gate. | CLOSED 20260625T155339Z |

## Log

- 20260625T154736Z OPENED by 0.6.0_AE_PartnerETL with 4 leg(s)
- 20260625T155119Z LEG L1 closed: Pushed CLOUD edbca164f..4f8f24714 (eb0ce40f6 guard, f6ca77914 runner, 28420f49d sha, record-deploy) + tag bd-v2.35.0 --f
- 20260625T155119Z LEG L2 closed: aws s3 ls s3://opal-data-bd/code/bronze/cot_bronze_ingest.py = 27119b @ 2026-06-25 (guarded single-source deployed to bd
- 20260625T155119Z LEG L3 closed: safe-apply 8-add/0-change/0-destroy; 0-diff (No changes). Live: bd-49f-runner Lambda + bd-49f-runner-daily cron(0 2 UTC)
- 20260625T155339Z LEG L4 closed: Firm-sep guard matrix PROVEN (4 cases: 49f+unset=ABORT, 49f+cot=ABORT, 49f+bd=PASS, cot-default=no-abort). Live runner s
- 20260625T155339Z CLOSED -- all 4 legs proven
