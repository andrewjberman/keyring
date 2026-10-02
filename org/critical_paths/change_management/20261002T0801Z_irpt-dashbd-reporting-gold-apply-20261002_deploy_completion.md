# Deploy Completion Record
**Date opened:** 2026-10-02T08:01:06.452501+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T114705Z
**Deploy:** IRPT_DASHBD DB-b-7: apply the reporting-gold root (the adapter on its own clock, 07:41 ET Mon-Fri; 7 new resources)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | re-plan of reporting-gold at CLOUD ce942dd8d1 | 7 to add, 0 to change, 0 to destroy; schedule cron(41 7 ? * MON-FRI *) America/New_York | terraform plan -lock=false at CLOUD ce942dd8d1 (08:0xZ): Plan: 7 to add, 0 to change, 0 to destroy; schedule_expression cron(41 7 ? * MON-FRI *), timezone America/New_York, state ENABLED; role writes only irpt/49financial/gold/account_return_daily/*; the build map packages MEASURED_THRESHOLDS_R1.json and the pinned code table | CLOSED 20261002T080434Z |
| D1 | activation | safe-apply of infra/aws/terraform/investor-reporting/reporting-gold | apply complete, 7 added | HALT_ACK=1 .tools/safe-apply.sh apply of the saved plan, 08:03:28Z: Apply complete! Resources: 7 added, 0 changed, 0 destroyed (halt gate: the same 40 routine historic messages, no STOP/HALT) | CLOSED 20261002T080434Z |
| V1 | verify | post-apply readback | CodeSha256 7eCQtWhs..., schedule ENABLED at the cron, role write only account_return_daily, re-plan No changes | get-function-configuration irpt-49f-reporting-gold-lambda: CodeSha256 7eCQtWhsWpReBrPzPULoVMLuS/pvymKg2XS9BAP37HQ= (= the source map), Active, timeout 900, memory 2048, role irpt-49f-reporting-gold-role; get-schedule irpt-49f-reporting-gold-daily: ENABLED, cron(41 7 ? * MON-FRI *), America/New_York, target the function; re-plan: No changes | CLOSED 20261002T080434Z |
| A1 | verify | first scheduled fire, no seat starting it | 07:41 ET fire lands partitions after 2026-09-28 through T-1; function log rows per day | first scheduled fire 2026-10-02 11:41Z (07:41 ET, schedule irpt-49f-reporting-gold-daily; no seat invoked): RequestId 356abf98-4c68-48dc-adf0-7de8acaafdea, 20.2 s, log 'newest landed date=2026-09-28; computing 3 day(s) 2026-09-29..2026-10-01 for 6 account(s)', each day rows=6 LANDED; s3api list-objects-v2 at the opal_naming address s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=2026-09-29\|30\|10-01: data.parquet + manifest.json each LastModified 2026-10-02T11:42:08Z; frontier = T-1 of Fri 2026-10-02 = 2026-10-01 | CLOSED 20261002T114705Z |

## Log

- 20261002T080106Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20261002T080434Z LEG P1 closed: terraform plan -lock=false at CLOUD ce942dd8d1 (08:0xZ): Plan: 7 to add, 0 to change, 0 to destroy; schedule_expression 
- 20261002T080434Z LEG D1 closed: HALT_ACK=1 .tools/safe-apply.sh apply of the saved plan, 08:03:28Z: Apply complete! Resources: 7 added, 0 changed, 0 des
- 20261002T080434Z LEG V1 closed: get-function-configuration irpt-49f-reporting-gold-lambda: CodeSha256 7eCQtWhsWpReBrPzPULoVMLuS/pvymKg2XS9BAP37HQ= (= th
- 20261002T114705Z LEG A1 closed: first scheduled fire 2026-10-02 11:41Z (07:41 ET, schedule irpt-49f-reporting-gold-daily; no seat invoked): RequestId 35
- 20261002T114705Z CLOSED -- all 4 legs proven
