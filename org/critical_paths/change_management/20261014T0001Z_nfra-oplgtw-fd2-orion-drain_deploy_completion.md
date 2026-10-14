# Deploy Completion Record
**Date opened:** 2026-10-14T00:01:27.017008+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / the 16:00Z scheduled EventBridge sweep opal-assets-silver-orion-sweep-daily cron(0 16 * * ? *), verified ENABLED live -- L3 grades the dlq_drain key in that sweep's meta/backfill-status.json and no ad-hoc invoke is permitted (held since 2026-10-14T00:12:34.511743+00:00)
**Deploy:** NFRA_OPLGTW OG-ap-15: release the per-family DLQ drain + record to opal-assets-silver-orion (drain-only, A2 GO)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | box/sitez carries dfec92946c (orion mirror_conversion.py + the one silver_build_commit row) | merge commit hash on box/sitez | box/sitez 01668227a0 (safe-merge of dfec92946c: orion mirror_conversion.py +85/-9 and the one silver_build_commit row) plus 7a05ab2021 (artifact_sha256 stamp); LOCAL, push is not this seat's act | CLOSED 20261014T001234Z |
| L2 | activation | module.silver_converter["orion"] runs the drain-only package | CodeSha256 read back equal to n7kVWHvtYBXn8xaNRsO0y5e7tVAH63i5LSYNJ9+dAo4=, State Active, LastUpdateStatus Successful | get-function-configuration read back CodeSha256 n7kVWHvtYBXn8xaNRsO0y5e7tVAH63i5LSYNJ9+dAo4= equal to the AC1-graded package_sha256, State Active, LastUpdateStatus Successful, OPAL_BUILD_COMMIT fdf2b07a9e, LastModified 2026-10-14T00:11:15Z; targeted re-plan reads No changes (0-diff). Plan before apply: 1 non-no-op of 11 resources, attributes moved environment(+OPAL_BUILD_COMMIT), source_code_hash, s3_object_version Jojh09IV..->W4zggPZI.., last_modified | CLOSED 20261014T001234Z |
| L3 | verify | the 16:00Z scheduled orion sweep writes meta/backfill-status.json with the dlq_drain key naming family orion | the sweep RequestId plus the dlq_drain section read from the served status object |  | OPEN |

## Log

- 20261014T000127Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
- 20261014T001234Z LEG L1 closed: box/sitez 01668227a0 (safe-merge of dfec92946c: orion mirror_conversion.py +85/-9 and the one silver_build_commit row) p
- 20261014T001234Z LEG L2 closed: get-function-configuration read back CodeSha256 n7kVWHvtYBXn8xaNRsO0y5e7tVAH63i5LSYNJ9+dAo4= equal to the AC1-graded pac
- 20261014T001234Z HELD-SOVEREIGN-GATED gate=external/the 16:00Z scheduled EventBridge sweep opal-assets-silver-orion-sweep-daily cron
