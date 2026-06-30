# Deploy-Completion Ledger — ADVI_BREAKS TO-3 49F: B_01 non-empty-unrealized gate

**Opened:** 2026-06-30T14:24Z by 0.4.0_DS_ClientPlatform~B
**Deploy:** B_01.holdings_lots.py `_resolve_unrealized_key` — skip 0-row/degenerate unrealized partitions, fall back to last NON-EMPTY within the existing 2-day window (restores 49F served frozen since 06-26T05:00).
**Gates cleared:** CTO apply-co-sign (135551Z) + COO GO (142324Z) + Andrew GO (135xxx direct).
**Scope:** single gold script, `code/gold/` S3 prefix. DS commit->QA-deploy (Rule 13).

| Leg | Type | Step | Status |
|---|---|---|---|
| L1 | git | CLOUD commit B_01 source (ds-commit-gate PASS) under DS~B author | OPEN |
| L2 | s3-prefix | upload B_01.holdings_lots.py -> s3://opal-data-bd/code/gold/ | OPEN |
| L3 | verify | NEXT scheduled gold run: 49F served platinum/firm/header_metrics.json data_as_of UN-FREEZES (NEVER#4: no ad-hoc run) | OPEN |

**Closure:** all 3 legs closed + RAVC COO+CTO+CVO. Unclosed at session end = COO alarm.

## Log
- 20260630T1424Z OPENED at deploy-start.
