# Deploy Completion Record
**Date opened:** 2026-10-14T23:16:29.309932+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T232956Z
**Deploy:** NFRA_OPLGTW OG-ec-2: deploy the Eclipse converter fix (defaultTradingEngineId admitted) and drive the silver sweep once
**Authored by:** 0.7.0_AE_CloudOps~ZS
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | rel-nfra-oplgtw-ec2 (the one silver_build_commit eclipse pin row) merged into box/sitez | merge hash | merge bbe844c0cf on box/sitez (safe-merge, 1 path: infra/aws/terraform/opal-assets/silver.tf, eclipse pin b915719f25 -> 8929c5f16d); 4fd05be0d3 is an ancestor of HEAD; LOCAL, push is not this seat's act | CLOSED 20261014T231835Z |
| L2 | activation | artifact s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-silver-eclipse.zip uploaded as a NEW version; prior latest 9KbX3Ee84D5n9e2hNtWsRkg6pk40yYcW content-sha256 clrUz/ikqSMgd5Edtx7gJFceLH2LSjow7c6Vfqtw64g= recorded as the rollback | head-object size, version id and content-sha256 read back | build-and-upload write VERIFIED 2026-10-14T23:19:18Z: new version s1CCbTmGy2fCo3vOLK_JzugTURd6KWPq, 38093 bytes, content-sha256 GxWRZhTMvkSWAXuBQHuzjZcAwQ3mJg3C0da8/ZoD6zU= (head-object read back independently); C2 re-read before the upload read 9KbX3Ee84D5n9e2hNtWsRkg6pk40yYcW / clrUz/ikqSMgd5Edtx7gJFceLH2LSjow7c6Vfqtw64g=; rollback version 9KbX3Ee8... still present (list-object-versions, latest=s1CCbTmG..., none deleted) | CLOSED 20261014T232035Z |
| L3 | activation | module.silver_converter[eclipse] aws_lambda_function.this runs the repo package | CodeSha256 read back equal to GxWRZhTMvkSWAXuBQHuzjZcAwQ3mJg3C0da8/ZoD6zU=, State Active, LastUpdateStatus Successful, OPAL_BUILD_COMMIT 8929c5f16d | safe-apply targeted module.silver_converter[eclipse], rc 0, 2026-10-14T23:23-23:24Z; plan before apply 0 add/1 change/0 destroy (OPAL_BUILD_COMMIT, s3_object_version 9KbX3Ee8->s1CCbTmG, source_code_hash, last_modified); read back: CodeSha256 GxWRZhTMvkSWAXuBQHuzjZcAwQ3mJg3C0da8/ZoD6zU= equal to the package, CodeSize 38093, State Active, LastUpdateStatus Successful, OPAL_BUILD_COMMIT 8929c5f16d; targeted re-plan No changes | CLOSED 20261014T232624Z |
| L4 | verify | ONE applier-driven sweep invoke; the guard reads PASS with missing 0 alien 0 | sweep RequestId plus the guard line from backfill-status.json | ONE applier-driven sweep: aws lambda invoke {mode:sweep} at 2026-10-14T23:26:24Z, StatusCode 200, no FunctionError, RequestId b6f5f98f-4e6e-4457-92d5-0a1eeb4d1010 (1 START in the 23:20Z+ window), Duration 3443 ms; run_id 20261014T232630Z-4607ca2e converted 5, dlq_drained 0; backfill-status.json guard PASS 'expected 552 landed 552 matched 552 missing 0 alien 0' checked 2026-10-14T23:26:33Z; exactly 5 of 552 silver objects modified since 23:00Z, all fact_portfolios_simple date=2026-10-10..14; no second invoke | CLOSED 20261014T232956Z |

## Log

- 20261014T231629Z OPENED by 0.7.0_AE_CloudOps~ZS with 4 leg(s)
- 20261014T231835Z LEG L1 closed: merge bbe844c0cf on box/sitez (safe-merge, 1 path: infra/aws/terraform/opal-assets/silver.tf, eclipse pin b915719f25 -> 
- 20261014T232035Z LEG L2 closed: build-and-upload write VERIFIED 2026-10-14T23:19:18Z: new version s1CCbTmGy2fCo3vOLK_JzugTURd6KWPq, 38093 bytes, content
- 20261014T232624Z LEG L3 closed: safe-apply targeted module.silver_converter[eclipse], rc 0, 2026-10-14T23:23-23:24Z; plan before apply 0 add/1 change/0 
- 20261014T232956Z LEG L4 closed: ONE applier-driven sweep: aws lambda invoke {mode:sweep} at 2026-10-14T23:26:24Z, StatusCode 200, no FunctionError, Requ
- 20261014T232956Z CLOSED -- all 4 legs proven
