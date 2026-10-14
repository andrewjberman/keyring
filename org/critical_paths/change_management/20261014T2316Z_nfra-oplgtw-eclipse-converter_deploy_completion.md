# Deploy Completion Record
**Date opened:** 2026-10-14T23:16:29.309932+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ec-2: deploy the Eclipse converter fix (defaultTradingEngineId admitted) and drive the silver sweep once
**Authored by:** 0.7.0_AE_CloudOps~ZS
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | rel-nfra-oplgtw-ec2 (the one silver_build_commit eclipse pin row) merged into box/sitez | merge hash |  | OPEN |
| L2 | activation | artifact s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-silver-eclipse.zip uploaded as a NEW version; prior latest 9KbX3Ee84D5n9e2hNtWsRkg6pk40yYcW content-sha256 clrUz/ikqSMgd5Edtx7gJFceLH2LSjow7c6Vfqtw64g= recorded as the rollback | head-object size, version id and content-sha256 read back |  | OPEN |
| L3 | activation | module.silver_converter[eclipse] aws_lambda_function.this runs the repo package | CodeSha256 read back equal to GxWRZhTMvkSWAXuBQHuzjZcAwQ3mJg3C0da8/ZoD6zU=, State Active, LastUpdateStatus Successful, OPAL_BUILD_COMMIT 8929c5f16d |  | OPEN |
| L4 | verify | ONE applier-driven sweep invoke; the guard reads PASS with missing 0 alien 0 | sweep RequestId plus the guard line from backfill-status.json |  | OPEN |

## Log

- 20261014T231629Z OPENED by 0.7.0_AE_CloudOps~ZS with 4 leg(s)
