# Deploy Completion Record
**Date opened:** 2026-10-14T00:28:46.685430+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-15: release the OG-fd-2 drain record to opal-assets-silver-schwab (route full, drain moves ahead of the lanes)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | box/sitez carries 12ecbe2b8f (schwab_runtime.py) and the silver_build_commit schwab row moved a11240c01c -> 12ecbe2b8f | merge and pin commit hashes on box/sitez |  | OPEN |
| L2 | activation | module.silver_converter["schwab"] runs the re-vendored package | CodeSha256 read back equal to U6l7D4fUe125WC53/GblkfHQKtDbpzRorHLLsvlbFmc=, State Active, LastUpdateStatus Successful |  | OPEN |
| L3 | verify | the 12:15Z scheduled schwab sweep writes meta/backfill-status.json with the dlq_drain key naming family schwab | the sweep RequestId plus the dlq_drain section read from the served status object |  | OPEN |

## Log

- 20261014T002846Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
