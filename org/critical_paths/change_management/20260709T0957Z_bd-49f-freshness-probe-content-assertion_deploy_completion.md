# Deploy Completion Record
**Date opened:** 2026-07-09T09:57:57.804215+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260709T100014Z
**Deploy:** freshness-integrity reference impl: bd-49f-freshness-probe TradingDayLag bound to parquet row-count (was filename-anchored; greenlit a 5-day client-facing freeze). CTO/COO GO 094410Z
**Authored by:** 0.6.0_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | commit + push CLOUD (probe + IAM + tests) | hash pushed | f45e63189 pushed to CLOUD (b9ed8fd67..f45e63189) | CLOSED 20260709T095810Z |
| L2 | tf-lambda | build-and-upload + safe-apply: new lambda_function.py + s3:GetObject on opal-data-bd/silver/* | apply complete + 0-diff replan + comp-iam gaps clean | build-and-upload.sh bd-pipeline bd-49f-freshness-probe (SHA256 lIfp0ZeJDbBgFWFV3tgMmENxgmLdJG+FkKI9gmtu5Po=); safe-apply(HALTGT) 'Apply complete! Resources: 0 added, 2 changed, 0 destroyed' (lambda source_code_hash + aws_iam_role_policy.bd_49f_freshness_probe_policy); replan 'No changes. Your infrastructure matches the configuration.' comp-iam gaps: the 3 MISSING it reports belong to astn-wsjft-orchestrator + etfs-reports-orchestrator (pre-existing, other lanes, surfaced to COO); bd-49f-freshness-probe s3:GetObject is GRANTED and no longer flagged. | CLOSED 20260709T100014Z |
| L3 | verify | APPLIED truth: live CodeSha256 + live get-role-policy shows the GetObject statement | live primitives, not TF DESIRED | APPLIED truth read off LIVE primitives, not the TF DESIRED view (CLAUDE.md 22a): aws lambda get-function-configuration CodeSha256=lIfp0ZeJDbBgFWFV3tgMmENxgmLdJG+FkKI9gmtu5Po= (== plan source_code_hash), LastModified 2026-07-09T09:58:34Z; aws iam get-role-policy bd-49f-freshness-probe-role/bd-49f-freshness-probe-policy returns Sid=ReadBdSilverParquetFootersForContentAssertion Allow s3:GetObject on arn:aws:s3:::opal-data-bd/silver/* -- landed, not merely declared. | CLOSED 20260709T100014Z |
| L4 | verify | LIVE invoke: probe must read real row counts, skip the 07-09 degenerate stub, and NOT false-page any table | CW log + returned payload with silver_row_count | LIVE invoke in AWS with the real role. Payload: silver_row_count={transactions:204043, allocations:6870, realized:15992, unrealized:103490, fees:27787}; trading_day_lag={transactions:0, allocations:1, realized:0, unrealized:1, fees:2}; silver_newest_partition_degenerate={allocations:1, others 0}. CW log: 'silver/allocations 2026-07-09 -> 0 rows (DEGENERATE stub) -- skipped, not an as_of anchor' then 'silver/allocations -> 0.8h lag=1td rows=6870 NEWEST-PARTITION-DEGENERATE'. The probe now reads TRUE row counts from live parquet footers, skips the degenerate newest partition, anchors on the repaired 07-08, and NO table false-pages (all lag <= threshold 2). CERT BAR exercised on the REAL known-bad artifacts pre-deploy: stub->0 rows, repaired->6,870 rows, pre-repair inventory replay OLD lag=0 GREEN vs NEW lag=4 REDS. | CLOSED 20260709T100014Z |

## Log

- 20260709T095757Z OPENED by 0.6.0_AE_PartnerETL with 4 leg(s)
- 20260709T095810Z LEG L1 closed: f45e63189 pushed to CLOUD (b9ed8fd67..f45e63189)
- 20260709T100014Z LEG L2 closed: build-and-upload.sh bd-pipeline bd-49f-freshness-probe (SHA256 lIfp0ZeJDbBgFWFV3tgMmENxgmLdJG+FkKI9gmtu5Po=); safe-apply
- 20260709T100014Z LEG L3 closed: APPLIED truth read off LIVE primitives, not the TF DESIRED view (CLAUDE.md 22a): aws lambda get-function-configuration C
- 20260709T100014Z LEG L4 closed: LIVE invoke in AWS with the real role. Payload: silver_row_count={transactions:204043, allocations:6870, realized:15992,
- 20260709T100014Z CLOSED -- all 4 legs proven
