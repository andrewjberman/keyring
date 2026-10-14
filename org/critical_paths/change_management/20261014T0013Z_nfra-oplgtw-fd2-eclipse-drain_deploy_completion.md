# Deploy Completion Record
**Date opened:** 2026-10-14T00:13:40.668962+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T160705Z -- gate: external / the 16:00Z scheduled EventBridge sweep opal-assets-silver-eclipse-sweep-daily cron(0 16 * * ? *), verified ENABLED live -- L3 grades the dlq_drain key in that sweep's meta/backfill-status.json; no ad-hoc invoke (held since 2026-10-14T00:20:19.033352+00:00)
**Deploy:** NFRA_OPLGTW OG-ap-15: release the per-family DLQ drain + record to opal-assets-silver-eclipse (drain-only, A2 GO)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | box/sitez carries 519552b5d7 (eclipse mirror_conversion.py + the one silver_build_commit row) | merge commit hash on box/sitez | box/sitez 169b80b5ac (safe-merge of 519552b5d7) plus 83b77e13d3 (artifact_sha256 stamp); LOCAL, push is not this seat's act | CLOSED 20261014T002018Z |
| L2 | activation | module.silver_converter["eclipse"] runs the drain-only package | CodeSha256 read back equal to clrUz/ikqSMgd5Edtx7gJFceLH2LSjow7c6Vfqtw64g=, State Active, LastUpdateStatus Successful | CodeSha256 read back clrUz/ikqSMgd5Edtx7gJFceLH2LSjow7c6Vfqtw64g= equal to the AC1-graded package_sha256, State Active, LastUpdateStatus Successful, OPAL_BUILD_COMMIT b915719f25; apply complete 0 added 1 changed 0 destroyed; targeted re-plan No changes. Plan before apply: 1 non-no-op of 11, attributes environment(+OPAL_BUILD_COMMIT only), source_code_hash, s3_object_version RbbMcE4o..->9KbX3Ee8.., last_modified | CLOSED 20261014T002018Z |
| L3 | verify | the 16:00Z scheduled eclipse sweep writes meta/backfill-status.json with the dlq_drain key naming family eclipse | the sweep RequestId plus the dlq_drain section read from the served status object | The 16:00Z SCHEDULED eclipse sweep ran: exactly ONE invocation of opal-assets-silver-eclipse in the 15:58-16:10Z window (denominator 4 log events), RequestId 1bd3a5f0-e995-4b01-b76a-f7a54f4422b2, START 16:00:05.021Z against cron, Duration 3792.48 ms -- no ad-hoc invoke. It wrote eclipse/inflection/meta/backfill-status.json at 16:00:08Z and the dlq_drain key is present at layers.silver.dlq_drain naming the family. THIS ONE IS NOT A ZERO: drained 12, messages_total 12, messages_capped false (so all 12 bodies are echoed in the record), other_family_returned 0, unattributed 0. All 12 are RetriesExhausted DLQ messages from the 13:05Z ingest-mirror copies of today's eclipse bronze objects, and all 12 carry ONE signature -- VendorDriftError on eclipse/portfolios_simple, extra=['defaultTradingEngineId'], declared 22 cols. 12 failures, 1 cause. The drain record is exactly what this leg asks for and it is present; the drift itself is a separate finding, filed as a row citing the CRO's Z-S111. | CLOSED 20261014T160704Z |

## Log

- 20261014T001340Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
- 20261014T002018Z LEG L1 closed: box/sitez 169b80b5ac (safe-merge of 519552b5d7) plus 83b77e13d3 (artifact_sha256 stamp); LOCAL, push is not this seat's 
- 20261014T002018Z LEG L2 closed: CodeSha256 read back clrUz/ikqSMgd5Edtx7gJFceLH2LSjow7c6Vfqtw64g= equal to the AC1-graded package_sha256, State Active, 
- 20261014T002019Z HELD-SOVEREIGN-GATED gate=external/the 16:00Z scheduled EventBridge sweep opal-assets-silver-eclipse-sweep-daily cr
- 20261014T160704Z LEG L3 closed: The 16:00Z SCHEDULED eclipse sweep ran: exactly ONE invocation of opal-assets-silver-eclipse in the 15:58-16:10Z window 
- 20261014T160705Z CLOSED -- all 3 legs proven
