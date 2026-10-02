# Deploy Completion Record
**Date opened:** 2026-10-02T07:34:13.141110+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T074224Z
**Deploy:** ETFS_RIVALS FAST lease: round 5 + amendment A1 to the five etfs-rivalfunds Lambdas (pin CLOUD 7aa0186d45, plan 0/7/0), republish page 2026-10-01
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | safe-apply infra/aws/terraform/etfs-rivalfunds saved plan /c/tmp/rv_apply.tfplan (5 Lambdas source_code_hash in place + 2 role policies additive; no create/destroy) | apply output: Apply complete 0 added 7 changed 0 destroyed | safe-apply etfs-rivalfunds (HALT_ACK=1, saved plan /c/tmp/rv_apply.tfplan from /c/tmp/rv-apply at 7aa0186d45, 07:36:47Z): Apply complete! Resources: 0 added, 7 changed, 0 destroyed; comp-tagauthz PASSED; tombstone CLEAN (0 creates) | CLOSED 20261002T073859Z |
| A2 | verify | five CodeSha256 after apply differ from the base and two role policies carry GetMarketReadings | get-function + get-role-policy output | CodeSha256 after (all Active/Successful, LastModified 07:36:21-45Z): daily PJr6l0z/.. fetch-holdings XNCVRKjn.. canonical-shape /xRX2KTZ.. silver ziEjx8Wm.. publish-page Rx7MAw7q.. (base was C/lTSdk7.. sLwaf78F.. DSDRr5th.. bDpv4Qks.. rphyMKON..); rivalfunds-publish-page-policy and etfs-rivalfunds-daily-policy Sids now include GetMarketReadings + ListMarketReadings | CLOSED 20261002T073859Z |
| A3 | activation | republish page 2026-10-01: daily-lambda only publish-page, batch fast-a1-publish-1001 | request id + publish marker + manifest page_version publish_page/3 + a1_produced statuses | daily-lambda only publish-page, date 2026-10-01, batch fast-a1-publish-1001, request 2acebec1-2215-4fe8-8cf2-4a0f8fbcfdab (72.4 s, 499 MB of 1024), status PARTIAL by GQGU freshness as before; marker state/publish_page/date=2026-10-01/fast-a1-publish-1001.json; manifest page_version publish_page/3, runtime etfs-rivalfunds-daily-lambda, a1_produced holding_contribution OK 3939 rows, buying_trend OK 311, input_census OK 1568 (market readings 23 arrived); prior page kept as revision 20261002T074018Z | CLOSED 20261002T074223Z |
| A4 | verify | served page read: headline count, 39 ranking panels, 13 trends, 12 AI blocks (none for SCHY), no script, under 2 MiB; screenshot | S3 index.html readback counts + screenshot path | S3 index.html read back 07:40Z: headline '12 of 13 funds current' (GQGU lagging), 39 ranking panels, 13 trends, 12 AI blocks (no SCHY), analysis_grounding PASS (TSEL activity shown as grounding FAIL), 198 trace panels (equal to served), audit block closed, no <script, 1,603,171 bytes (cap 2,097,152); screenshot rf_served_1001_a1_top.png of the served bytes (gateway is SSO-gated) | CLOSED 20261002T074223Z |

## Log

- 20261002T073413Z OPENED by 2.0.0_SA_COO~RV with 4 leg(s)
- 20261002T073859Z LEG A1 closed: safe-apply etfs-rivalfunds (HALT_ACK=1, saved plan /c/tmp/rv_apply.tfplan from /c/tmp/rv-apply at 7aa0186d45, 07:36:47Z)
- 20261002T073859Z LEG A2 closed: CodeSha256 after (all Active/Successful, LastModified 07:36:21-45Z): daily PJr6l0z/.. fetch-holdings XNCVRKjn.. canonica
- 20261002T074223Z LEG A3 closed: daily-lambda only publish-page, date 2026-10-01, batch fast-a1-publish-1001, request 2acebec1-2215-4fe8-8cf2-4a0f8fbcfda
- 20261002T074223Z LEG A4 closed: S3 index.html read back 07:40Z: headline '12 of 13 funds current' (GQGU lagging), 39 ranking panels, 13 trends, 12 AI bl
- 20261002T074224Z CLOSED -- all 4 legs proven
