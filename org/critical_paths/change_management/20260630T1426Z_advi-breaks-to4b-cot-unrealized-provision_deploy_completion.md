# Deploy-Completion Ledger — ADVI_BREAKS TO-4b cot: unrealized provision-fix

**Opened:** 2026-06-30T14:26Z by 0.4.0_DS_ClientPlatform
**Deploy:** provision a persisted BD DataMining templateId for cot `unrealized` (qt4 snapshot) + wire it into `code/bronze/templates/unrealized.json`, restoring the non-empty unrealized export (collapsed to 3743B/0-row stubs since the 06-22 AUAFIX-DATEMODE CurrentDay->Custom flip; unrealized is templateId=False, and qt4 snapshot under Custom via create-per-run returns empty). Mirrors the working snapshot siblings holdings(226355)/allocations(226334).
**Gates cleared:** CTO co-sign (134106Z, verify-before-wire condition) + COO GO (142331Z) + Andrew GO (standing authority, CTO-co-sign class).
**Scope:** cot BD template config (`s3://opal-data-cot/code/bronze/templates/unrealized.json`) — DS commit->QA-deploy (Rule 13). EC2 SSM runs (STEP-1/2) = 0.7.0_AE infra (DS lacks SSM:SendCommand to cot-exporter).
**Priority:** LOW (cot unrealized = CUSIP->asset_name bridge only, NOT the cot AUA driver [holdings is]; CTO-set). cot holdings freeze = SEPARATE BD-pricing-lag root (no code fix; gate/product call).

| Leg | Type | Step | Status |
|---|---|---|---|
| L1 | BD-write (AE SSM) | STEP-1: `cot_bronze_ingest.py --table unrealized --provision` on cot-exporter -> new persisted templateId | OPEN |
| L2 | verify (AE SSM) | STEP-2 GATE: Custom-mode unrealized pull w/ new id -> CONFIRM >0 data rows (vs current 3743B/0-row). 49F proved persisted-id qt4 can still empty -> load-bearing | OPEN |
| L3 | s3-config (DS) | STEP-3: wire new templateId into code/bronze/templates/unrealized.json (ds-commit-gate + s3 cp) — GATED on L2 non-empty; RAVC CTO before serving | OPEN |
| L4 | verify | NEXT scheduled nightly: forwardfill_v2/unrealized non-empty -> silver/unrealized non-empty -> B_00 CUSIP bridge restored (NEVER#4: no ad-hoc gold run) | OPEN |

**Fork at L2:** if STEP-2 returns EMPTY, the provision alone is insufficient (same as 49F's 431167) -> pivot fix to the qt4 snapshot date-window semantics (start=end=asOfDate, not the 14d range) -> re-verify L2 -> then L3. ~B owns the parallel 49F 431167 repair.
**Also folding (cot-side TO-6 gap, ~B-flagged):** cot ingest has a holdings completeness guard but NO unrealized non-empty guard -> the empty landed silently since 06-22. Add an unrealized (+realized) empty-stub feed-contract reject/alarm (mirrors ~B's B_01 gate). Tracked separately if not in this deploy.

**Closure:** all legs closed + RAVC COO+CTO. Unclosed at session end = COO alarm.

## Log
- 20260630T1426Z OPENED at deploy-start. STEP-1/2 dispatched to 0.7.0_AE (SSM on cot-exporter); awaiting new templateId + STEP-2 row-count.
