# Deploy Completion Record
**Date opened:** 2026-10-01T21:51:55.887030+00:00
**Status:** OPEN
**Deploy:** ETFS_RIVALS RIV-d-5 addendum 1: five Lambdas in place to the q-1 G2 fix (rows Z-W4-S12/S13), G2 holdings_coverage replay, page republish
**Authored by:** 0.9.0_WK_ETFS_RIVALS~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | safe-apply infra/aws/terraform/etfs-rivalfunds (5 Lambdas source_code_hash in place; no create/destroy/policy) | apply output: Apply complete 0 added 5 changed 0 destroyed |  | OPEN |
| A2 | activation | G2 holdings_coverage replay over 2025-07-14..2026-09-30 (GQGU +307 rows, others byte-equal) | Lambda request ids + per-fund G2 rows |  | OPEN |
| A3 | activation | republish page 2026-10-01 (new object) | publish marker + request id |  | OPEN |
| A4 | verify | d-5.AC1 AC2 AC3 re-run; d5_live.json addendum1 | AC RESULT lines |  | OPEN |

## Log

- 20261001T215155Z OPENED by 0.9.0_WK_ETFS_RIVALS~4 with 4 leg(s)
