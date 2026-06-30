# Deploy-Completion Ledger — ADVI_BREAKS TO-4b cot: unrealized provision-fix

**Opened:** 2026-06-30T14:26Z by 0.4.0_DS_ClientPlatform
**Deploy:** provision a persisted BD DataMining templateId for cot `unrealized` (qt4 snapshot) + wire it into `code/bronze/templates/unrealized.json`, restoring the non-empty unrealized export (collapsed to 3743B/0-row stubs since the 06-22 AUAFIX-DATEMODE CurrentDay->Custom flip; unrealized is templateId=False, and qt4 snapshot under Custom via create-per-run returns empty). Mirrors the working snapshot siblings holdings(226355)/allocations(226334).
**Gates cleared:** CTO co-sign (134106Z, verify-before-wire condition) + COO GO (142331Z) + Andrew GO (standing authority, CTO-co-sign class).
**Scope:** cot BD template config (`s3://opal-data-cot/code/bronze/templates/unrealized.json`) — DS commit->QA-deploy (Rule 13). EC2 SSM runs (STEP-1/2) = 0.7.0_AE infra (DS lacks SSM:SendCommand to cot-exporter).
**Priority:** LOW (cot unrealized = CUSIP->asset_name bridge only, NOT the cot AUA driver [holdings is]; CTO-set). cot holdings freeze = SEPARATE BD-pricing-lag root (no code fix; gate/product call).

| Leg | Type | Step | Status |
|---|---|---|---|
| L1 | BD-write (AE SSM) | STEP-1: `cot_bronze_ingest.py --table unrealized --provision` on cot-exporter -> new persisted templateId | DONE: templateId=237784 (AE SSM 3b218b3b, on the CURRENT 9abd0181b measures-selected body) |
| L2 | verify (AE SSM) | STEP-2 GATE: Custom-mode unrealized pull w/ new id -> CONFIRM >0 data rows (vs current 3743B/0-row). 49F proved persisted-id qt4 can still empty -> load-bearing | OPEN |
| L3 | s3-config (DS) | STEP-3: wire templateId=237784 into unrealized.json — DONE: git 0e47446f2 (ds-gate PASS) + s3 cp to canonical; git==S3 parity confirmed. (Order: CTO-approved wire-then-verify collapse, no isolation-verify mode; no-regression.) | DONE |
| L2 | verify (AE SSM) | STEP-2 (now post-wire): AE clean `--table unrealized --date 2026-06-30` reads 237784 -> row-count. NON-EMPTY=FIXED / EMPTY=no-op | DISPATCHED to AE (237784 live in canonical) |
| L4 | verify | NEXT scheduled nightly: forwardfill_v2/unrealized non-empty -> silver/unrealized non-empty -> B_00 CUSIP bridge restored (NEVER#4: no ad-hoc gold run) | OPEN |

**Fork at L2:** if STEP-2 returns EMPTY, the provision alone is insufficient (same as 49F's 431167) -> pivot fix to the qt4 snapshot date-window semantics (start=end=asOfDate, not the 14d range) -> re-verify L2 -> then L3. ~B owns the parallel 49F 431167 repair.
**Also folding (cot-side TO-6 gap, ~B-flagged):** cot ingest has a holdings completeness guard but NO unrealized non-empty guard -> the empty landed silently since 06-22. Add an unrealized (+realized) empty-stub feed-contract reject/alarm (mirrors ~B's B_01 gate). Tracked separately if not in this deploy.

**Closure:** all legs closed + RAVC COO+CTO. Unclosed at session end = COO alarm.

## Log
- 20260630T1426Z OPENED at deploy-start. STEP-1/2 dispatched to 0.7.0_AE (SSM on cot-exporter); awaiting new templateId + STEP-2 row-count.
- 20260630T1513Z STEP-1 DONE: templateId=237784 provisioned. Context (~B, commit 9abd0181b 06-12): cot's unrealized body was measures-FIXED 06-12 (isSelected=true on 8 dims+6 meas, B_02 contract) -> worked under CurrentDay (10.7MB); the 06-13 "harvest+pin-back persisted id" was NEVER done (templateId stayed False); 237784 IS that intended pin-back. So cot = date-mode case (good body), NOT 49F's facts=0 case. Raises confidence 237784 carries measures under Custom.
- 20260630T1516Z STEP-2 MECHANISM: script has NO isolation test-pull (load_template reads templateId from canonical S3 template) -> verify-before-wire mechanically blocked. Mitigant: wiring 237784 is NO-REGRESSION (237784 empty == current empty-stub; non-empty == fixed; never worse than False). Recommended CTO collapse to wire-then-verify (DS-lane git+s3 wire, then AE clean pull); awaiting CTO OK. AE holding off canonical (151649Z).
- 20260630T1450Z FORK/STEER: AE+~B grounded 49F's 431167 root as facts=0 TEMPLATE BODY (needs enrichment, not date/id). But cot's body is facts=1 ([{'name':'Fact'}]+8 levels) and produced 10.7MB under CurrentDay (only 06-22 change = dateRangeType CurrentDay->Custom) -> cot is NOT confirmed 49F's facts=0 root. STEERED AE: run cot --provision on the CURRENT body + STEP-2 verify FIRST (decisive). If non-empty -> STEP-3 wire (co-signed scope). If empty -> cot needs a COT-SCHEMA-PRESERVING fix (match cot's historical unrealized columns for silver/B_00, NOT 49F's target set) -- candidate = revert cot unrealized to CurrentDay (no-refreeze, holdings/alloc-specific); this is a SCOPE EXPANSION beyond the co-signed provision -> requires fresh CTO co-sign (flagged 145024Z). Ledger stays OPEN through the fork.
