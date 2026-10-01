# Deploy Completion Record
**Date opened:** 2026-10-01T00:43:58.436130+00:00
**Status:** OPEN
**Deploy:** ETFS_RIVALS round-2 live join (RIV-d-3): etfs-rivalfunds in-place deploy, G0, G3 + Bloomberg capture import, vehicle leg enabled, fire, read
**Authored by:** 0.9.0_WK_ETFS_RIVALS~5
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply infra/aws/terraform/etfs-rivalfunds (5 Lambdas source_code_hash in place, 5 role policies widened, 2 new marker rules + targets + permissions; no destroy) | apply output: Apply complete, 0 destroyed, plan in-place or create-only |  | OPEN |
| L2 | activation | G0 map_version 1 (home funds home_producer) + G3 import of dividends.json (G3 BEFORE any G5, row W3-S13) + key-4 served delta re-run WITH the imported G3 (CTO condition) before G5 writes | G0 object + G3 marker + key4_with_g3.json read |  | OPEN |
| L3 | s3-prefix | opal-data-etfs bloomberg/etfs/bronze/holdings/ 937 imported captures (501 IDVZ-group + 436 PFOE-group), raw + sidecar each, 9 date-ordered batches | S3 object counts by prefix + fetch_bloomberg markers |  | OPEN |
| L4 | activation | marker-driven build-bloomberg-silver, G1, G2 (+ replay), G5, G6 and the grouped page via rivalfunds Lambdas | Lambda request ids + S3 object counts by prefix |  | OPEN |
| L5 | git | scheduled_daily_pull.cmd the ONE enabling line inside :rivalfunds_bbg_leg; b-1.AC3 still PASS | commit hash + b-1.AC3 PASS |  | OPEN |
| L6 | verify | d-3.AC1 AC2 AC3 PASS against the served bucket; Terminal state recorded (never a sign-in attempt) | AC RESULT lines |  | OPEN |

## Log

- 20261001T004358Z OPENED by 0.9.0_WK_ETFS_RIVALS~5 with 6 leg(s)
