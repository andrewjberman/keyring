# Deploy Completion Record
**Date opened:** 2026-10-01T10:49:13.190531+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T112053Z
**Deploy:** ETFS_RIVALS round-3 live join (RIV-d-4): etfs-rivalfunds in-place deploy + 2 read grants, BASG re-capture control, G4 import, replay G1/G2/G5/G6, page, read
**Authored by:** 0.9.0_WK_ETFS_RIVALS~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply infra/aws/terraform/etfs-rivalfunds (5 Lambdas source_code_hash in place + 2 stage role policies gain read grants on bbg landing and G4; no create/destroy) | apply output: Apply complete, 0 destroyed, plan in-place only | safe-apply etfs-rivalfunds (HALT_ACK=1, saved plan, 2026-10-01T10:53Z): Apply complete! Resources: 0 added, 7 changed, 0 destroyed. Plan = 5 aws_lambda_function in place (source_code_hash) + 2 aws_iam_role_policy in place (daily, canonical-shape: GetHomeLanding, ListHomeLanding, G4 read); comp-tagauthz and tombstone gates clean; code pin e364f8971c; IAM simulation: canonical-shape + daily roles GetObject allowed on bbg/<D>/constituents/constituents_issuer_fill.parquet and G4, implicitDeny on bbg/<D>/characteristics.parquet and daily/x, Put/Delete implicitDeny; publish-page role unchanged (implicitDeny) | CLOSED 20261001T105642Z |
| L2 | s3-prefix | issuer-site bronze+silver, one landed BASG report date re-captured via the deployed fetch-holdings Lambda backfill (earlier silver object retained, silver marker OK) | S3 listing of silver + marker + request ids | backfill request 52dc7b59-e450-4c53-b9aa-9d0f661513ed (batch d4-control-basg-20260929, report date 2026-09-29): bronze basg-2026-09-29-20261001T105835Z-bfd36047cb41.txt; issuer-site/etfs/silver/holdings/date=2026-09-29/ now 2 objects (basg-20260930T110033Z-... retained + basg-20261001T105835Z-bfd36047cb41.parquet); build_silver marker state/build_silver/date=2026-10-01/d4-control-basg-20260929.json status OK written_new 1; G1 for the date written by the marker chain (holdings-20261001T105835Z-h330041300fa) and the replay | CLOSED 20261001T112052Z |
| L3 | s3-prefix | rivalfunds/etfs/gold/security_market/ G4 import from newest characteristics.parquet (QA-class) plus live market pull if the Terminal reads signed in | S3 object counts + marker | G4 import: security_market/date=2026-09-29/market-20260929-afcd903ad844.parquet (172 rows, 164 GICS sector, marker pull_enrichment/date=2026-09-29/d4-g4-import-market.json) before: 0 objects; live market pull (Terminal health ok 11:07:34Z): market-20260929-53bc393958bd.parquet (434 securities, 430 sector, 430 PX_LAST, marker d4-g4-market-market); prefix now 2 objects | CLOSED 20261001T112052Z |
| L4 | activation | replay G1, G2, G5, G6 for the window the home landings cover, then publish the page (NEW revisions only) | Lambda request ids + S3 object counts by prefix | canonical-shape Lambda request 7ffcd65f-e6a6-4210-9524-1041104fcc4a mode replay 2026-08-21..2026-09-29 batch d4-replay-r3: G1 23 new (17683 rows), G2 25 new, G5 23 new (895 rows), G6 23 new, all new revision objects; page published by the replay chain (date=2026-09-29) and by daily-lambda only publish-page requests ca245e04-3f89-4686-a197-3fb453431fd2 and 4721b79b-9853-4743-9f18-7be5031f8436 (date=2026-10-01, marker d4-publish-r3b, not_updated GQGU only); prefix counts in d4_live.json s3_prefixes | CLOSED 20261001T112052Z |
| L5 | verify | d-4.AC1 AC2 AC3 PASS against the served bucket; d4_live.json written | AC RESULT lines | d-4.AC1 RESULT: PASS 0 failures; d-4.AC2 RESULT: FAIL 1 failures (last clause grades the capture id inside G1 dataset_revision, which the home-inclusive revision scheme never carries; the G1 snapshot_id/silver_uri/bronze_uri DO name the re-capture; row ETFS_RIVALS-Z-W4-S3, issuer's check outside this order's paths); d-4.AC3 RESULT: PASS 0 failures; d4_live.json written. The deploy itself is whole: nothing stranded | CLOSED 20261001T112052Z |

## Log

- 20261001T104913Z OPENED by 0.9.0_WK_ETFS_RIVALS~4 with 5 leg(s)
- 20261001T105642Z LEG L1 closed: safe-apply etfs-rivalfunds (HALT_ACK=1, saved plan, 2026-10-01T10:53Z): Apply complete! Resources: 0 added, 7 changed, 0
- 20261001T112052Z LEG L2 closed: backfill request 52dc7b59-e450-4c53-b9aa-9d0f661513ed (batch d4-control-basg-20260929, report date 2026-09-29): bronze b
- 20261001T112052Z LEG L3 closed: G4 import: security_market/date=2026-09-29/market-20260929-afcd903ad844.parquet (172 rows, 164 GICS sector, marker pull_
- 20261001T112052Z LEG L4 closed: canonical-shape Lambda request 7ffcd65f-e6a6-4210-9524-1041104fcc4a mode replay 2026-08-21..2026-09-29 batch d4-replay-r
- 20261001T112052Z LEG L5 closed: d-4.AC1 RESULT: PASS 0 failures; d-4.AC2 RESULT: FAIL 1 failures (last clause grades the capture id inside G1 dataset_re
- 20261001T112053Z CLOSED -- all 5 legs proven
