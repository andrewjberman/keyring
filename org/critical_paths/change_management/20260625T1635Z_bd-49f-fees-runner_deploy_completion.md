# Deploy Completion Record
**Date opened:** 2026-06-25T16:35:01.043622+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260625T163737Z
**Deploy:** ADVI_BDAPIMIG P1 (B-fees): durable 49F fees REST runner Lambda + daily schedule (8 add) -- replaces login-broken scrape; MDPF gate input
**Authored by:** 0.6.0_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commits ed95ac137(runner+tf)+69251fc56(sha) + fees.json provisioned + bd tag pushed | hashes/tag --follow-tags | Pushed CLOUD 56df0cfd1..74e96d040 (ed95ac137 runner+tf, 69251fc56 sha, record-deploy) + tag bd-v2.36.0 --follow-tags. templates/fees.json (435407) provisioned to opal-data-bd/code/bronze/templates/. | CLOSED 20260625T163649Z |
| L2 | activation | bd-49f-fees-runner Lambda + bd-49f-fees-runner-daily cron(30 22 weekday) rule + bd-49f-fees-runner-role (cot-Deny) live via TF apply 8-add | 0-diff plan | safe-apply 8-add/0-change/0-destroy; 0-diff (No changes). Live: bd-49f-fees-runner Lambda (py3.11, 3008MB, pandas+openpyxl layers) + bd-49f-fees-runner-daily cron(30 22 weekday) rule + bd-49f-fees-runner-role (opal-data-bd-scoped + explicit cot Deny). | CLOSED 20260625T163649Z |
| L3 | verify | firm-sep guard invoked at fees-runner main-top (proven matrix) + live smoke lands fees in opal-data-bd (never cot) + silver/fees fresh | smoke result + cot negative-check (CVO close-gate) | Live Lambda smoke (bd-49f-fees-runner): log 'firm=49f bucket=opal-data-bd window=2026-06-11->2026-06-25 / fees run=483553 / OK landed s3://opal-data-bd/bronze/fees/...7910517 bytes / Raw rows 58405 cols 34 / DONE 63 silver partitions / silver/fees/2026-06-24.parquet 1224 rows / RESULT fees landed+converted' 55.7s/363MB. _assert_firm_separation invoked at main-top. Firm-safe: opal-data-cot/{silver,bronze}/fees EMPTY (negative-checked). Lands opal-data-bd only. | CLOSED 20260625T163737Z |

## Log

- 20260625T163501Z OPENED by 0.6.0_AE_PartnerETL with 3 leg(s)
- 20260625T163649Z LEG L1 closed: Pushed CLOUD 56df0cfd1..74e96d040 (ed95ac137 runner+tf, 69251fc56 sha, record-deploy) + tag bd-v2.36.0 --follow-tags. te
- 20260625T163649Z LEG L2 closed: safe-apply 8-add/0-change/0-destroy; 0-diff (No changes). Live: bd-49f-fees-runner Lambda (py3.11, 3008MB, pandas+openpy
- 20260625T163737Z LEG L3 closed: Live Lambda smoke (bd-49f-fees-runner): log 'firm=49f bucket=opal-data-bd window=2026-06-11->2026-06-25 / fees run=48355
- 20260625T163737Z CLOSED -- all 3 legs proven
