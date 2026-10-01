# Deploy Completion Record
**Date opened:** 2026-10-01T10:49:13.190531+00:00
**Status:** OPEN
**Deploy:** ETFS_RIVALS round-3 live join (RIV-d-4): etfs-rivalfunds in-place deploy + 2 read grants, BASG re-capture control, G4 import, replay G1/G2/G5/G6, page, read
**Authored by:** 0.9.0_WK_ETFS_RIVALS~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply infra/aws/terraform/etfs-rivalfunds (5 Lambdas source_code_hash in place + 2 stage role policies gain read grants on bbg landing and G4; no create/destroy) | apply output: Apply complete, 0 destroyed, plan in-place only |  | OPEN |
| L2 | s3-prefix | issuer-site bronze+silver, one landed BASG report date re-captured via the deployed fetch-holdings Lambda backfill (earlier silver object retained, silver marker OK) | S3 listing of silver + marker + request ids |  | OPEN |
| L3 | s3-prefix | rivalfunds/etfs/gold/security_market/ G4 import from newest characteristics.parquet (QA-class) plus live market pull if the Terminal reads signed in | S3 object counts + marker |  | OPEN |
| L4 | activation | replay G1, G2, G5, G6 for the window the home landings cover, then publish the page (NEW revisions only) | Lambda request ids + S3 object counts by prefix |  | OPEN |
| L5 | verify | d-4.AC1 AC2 AC3 PASS against the served bucket; d4_live.json written | AC RESULT lines |  | OPEN |

## Log

- 20261001T104913Z OPENED by 0.9.0_WK_ETFS_RIVALS~4 with 5 leg(s)
