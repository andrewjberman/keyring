# Deploy Completion Record
**Date opened:** 2026-10-01T17:19:46.989378+00:00
**Status:** OPEN
**Deploy:** ETFS_RIVALS round-4 live join (RIV-d-5): etfs-rivalfunds in-place deploy (5 Lambda source_code_hash), 305 GQGU archive days as issuer bronze + silver, per-source identity floors, G1/G5/G6 replay, page, read
**Authored by:** 0.9.0_WK_ETFS_RIVALS~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply infra/aws/terraform/etfs-rivalfunds (5 Lambdas source_code_hash in place; no create/destroy/policy change) | apply output: Apply complete, 0 added 0 destroyed, plan = 5 aws_lambda_function in place |  | OPEN |
| L2 | s3-prefix | issuer-site bronze + silver for GQGU (305 archived days landed with land_bronze fund=GQGU, silver by marker, 0 gqgu objects before) | S3 listing counts + silver marker |  | OPEN |
| L3 | git | guardrails_config.json min_resolved_fraction per-source floors (issuer, bloomberg, home_producer), one commit | commit hash |  | OPEN |
| L4 | activation | replay G1 G2 G5 G6 over the served-delta window then publish the page (NEW revisions only) | Lambda request ids + S3 object counts by prefix |  | OPEN |
| L5 | verify | d-5.AC1 AC2 AC3 against the served bucket; d5_live.json written | AC RESULT lines |  | OPEN |

## Log

- 20261001T171946Z OPENED by 0.9.0_WK_ETFS_RIVALS~4 with 5 leg(s)
