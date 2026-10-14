# Deploy Completion Record
**Date opened:** 2026-10-14T00:28:46.685430+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / the 12:15Z scheduled EventBridge sweep opal-assets-silver-schwab-sweep-daily cron(15 12 * * ? *), verified ENABLED live -- L3 grades the dlq_drain key in that sweep's meta/backfill-status.json; no ad-hoc invoke (held since 2026-10-14T00:35:52.233025+00:00)
**Deploy:** NFRA_OPLGTW OG-ap-15: release the OG-fd-2 drain record to opal-assets-silver-schwab (route full, drain moves ahead of the lanes)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | box/sitez carries 12ecbe2b8f (schwab_runtime.py) and the silver_build_commit schwab row moved a11240c01c -> 12ecbe2b8f | merge and pin commit hashes on box/sitez | box/sitez 6f5a641557 (safe-merge of 12ecbe2b8f), f2a1c6ed4c (pin move a11240c01c -> 12ecbe2b8f), 79200b5558 (artifact_sha256 stamp); LOCAL | CLOSED 20261014T003551Z |
| L2 | activation | module.silver_converter["schwab"] runs the re-vendored package | CodeSha256 read back equal to U6l7D4fUe125WC53/GblkfHQKtDbpzRorHLLsvlbFmc=, State Active, LastUpdateStatus Successful | CodeSha256 read back U6l7D4fUe125WC53/GblkfHQKtDbpzRorHLLsvlbFmc= equal to the AC1-graded package_sha256, State Active, LastUpdateStatus Successful, OPAL_BUILD_COMMIT 12ecbe2b8f; apply complete 0/1/0; re-plan No changes. Plan: 1 non-no-op of 11; OPAL_BUILD_COMMIT a11240c01c -> 12ecbe2b8f (a value change, schwab being the only pre-pinned family); s3_object_version yvgK0D.i..->ovDRfjMv.. | CLOSED 20261014T003551Z |
| L3 | verify | the 12:15Z scheduled schwab sweep writes meta/backfill-status.json with the dlq_drain key naming family schwab | the sweep RequestId plus the dlq_drain section read from the served status object |  | OPEN |

## Log

- 20261014T002846Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
- 20261014T003551Z LEG L1 closed: box/sitez 6f5a641557 (safe-merge of 12ecbe2b8f), f2a1c6ed4c (pin move a11240c01c -> 12ecbe2b8f), 79200b5558 (artifact_sh
- 20261014T003551Z LEG L2 closed: CodeSha256 read back U6l7D4fUe125WC53/GblkfHQKtDbpzRorHLLsvlbFmc= equal to the AC1-graded package_sha256, State Active, 
- 20261014T003552Z HELD-SOVEREIGN-GATED gate=external/the 12:15Z scheduled EventBridge sweep opal-assets-silver-schwab-sweep-daily cro
