# Deploy Completion Record
**Date opened:** 2026-10-14T00:37:40.296123+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / the 23:30Z scheduled EventBridge sweep opal-assets-silver-etf-sweep-daily cron(30 23 * * ? *), verified ENABLED live -- L3 grades the dlq_drain key across etf's 3 trees; no ad-hoc invoke (held since 2026-10-14T00:47:15.639312+00:00)
**Deploy:** NFRA_OPLGTW OG-ap-15: release the per-family DLQ drain + record to opal-assets-silver-etf (route full, 19 drift lines, SIGNED on condition E1)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | box/sitez carries 58ee124eb7 (etf_conversion.py, mirror_conversion.py, silver_registry.py) and the silver_build_commit etf row | merge and pin commit hashes on box/sitez | box/sitez 43b0ee8858 (safe-merge of 58ee124eb7; all three package blobs verified equal to the build commit's), 96833f3b95 (pin add etf=58ee124eb7), b936003323 (artifact_sha256 stamp); LOCAL | CLOSED 20261014T004715Z |
| L2 | activation | module.silver_converter["etf"] runs the re-vendored package | CodeSha256 read back equal to zNCf2GLiRNSpUYsdQUUPvwuAHtDZBlPevai0YqdzRh4=, State Active, LastUpdateStatus Successful | E1 RE-READ immediately pre-apply: deployed etf package 9 of 9 members byte-EQUAL to the package dir at base_sha, 0 differing, 0 zip-only, zip sha256 hosvkcI2.. equal to get-function-configuration -- so the 19 ruled drift lines were measured against what was actually running. Then CodeSha256 read back zNCf2GLiRNSpUYsdQUUPvwuAHtDZBlPevai0YqdzRh4= equal to the AC1-graded package_sha256, State Active, LastUpdateStatus Successful, OPAL_BUILD_COMMIT 58ee124eb7; apply 0/1/0; re-plan No changes. Plan: 1 non-no-op of 11, env +OPAL_BUILD_COMMIT only, s3_object_version OUjv4oZ4..->8EbcKsc6.. | CLOSED 20261014T004715Z |
| L3 | verify | the 23:30Z scheduled etf sweep writes meta/backfill-status.json with the dlq_drain key naming family etf, across its 3 trees | the sweep RequestId plus the dlq_drain section read from the served status object |  | OPEN |

## Log

- 20261014T003740Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
- 20261014T004715Z LEG L1 closed: box/sitez 43b0ee8858 (safe-merge of 58ee124eb7; all three package blobs verified equal to the build commit's), 96833f3b9
- 20261014T004715Z LEG L2 closed: E1 RE-READ immediately pre-apply: deployed etf package 9 of 9 members byte-EQUAL to the package dir at base_sha, 0 diffe
- 20261014T004715Z HELD-SOVEREIGN-GATED gate=external/the 23:30Z scheduled EventBridge sweep opal-assets-silver-etf-sweep-daily cron(3
