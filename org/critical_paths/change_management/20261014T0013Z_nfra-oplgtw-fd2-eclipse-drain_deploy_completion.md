# Deploy Completion Record
**Date opened:** 2026-10-14T00:13:40.668962+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-15: release the per-family DLQ drain + record to opal-assets-silver-eclipse (drain-only, A2 GO)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | box/sitez carries 519552b5d7 (eclipse mirror_conversion.py + the one silver_build_commit row) | merge commit hash on box/sitez |  | OPEN |
| L2 | activation | module.silver_converter["eclipse"] runs the drain-only package | CodeSha256 read back equal to clrUz/ikqSMgd5Edtx7gJFceLH2LSjow7c6Vfqtw64g=, State Active, LastUpdateStatus Successful |  | OPEN |
| L3 | verify | the 16:00Z scheduled eclipse sweep writes meta/backfill-status.json with the dlq_drain key naming family eclipse | the sweep RequestId plus the dlq_drain section read from the served status object |  | OPEN |

## Log

- 20261014T001340Z OPENED by 0.7.0_AE_CloudOps~Z with 3 leg(s)
