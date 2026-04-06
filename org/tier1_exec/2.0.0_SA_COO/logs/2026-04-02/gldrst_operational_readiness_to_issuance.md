# ADVI_GLDRST Operational Readiness TO Issuance -- 2.0.0_SA_COO

**Date:** 2026-04-02
**Session:** 10

---

## Task: Issue 5 new GLDRST task orders (.015-.019)

CTO delivered PRD `docs/architecture/GLDRST_P3_OPERATIONAL_READINESS.md` with
COO handoff briefing. 4 operational work streams identified during the 04-01/04-02
gold rebuild cycle. Andrew directed all items integrated into GLDRST.

### PRD Verification (before writing TOs)

| PRD Claim | Verification | Result |
|-----------|-------------|--------|
| lib/config.py exists at gold/lib/config.py | `ls` check | CONFIRMED |
| 7 non-gold scripts import from lib.config | `grep` across data/black_diamond/scripts | CONFIRMED (5 silver, 2 classification) |
| Script 05 exists | `ls` check | CONFIRMED |
| synthetic_positions_index.parquet written by script 02 | `grep` for string | CONFIRMED at line 1402 of 02_build_positions_cube.py |
| bd-gold-layer-runner infra dir exists | `ls` check | CONFIRMED (6 files including run-gold-layer.sh, setup-instance.sh) |

### TOs Issued

| TO | Agent | Description | Status | GO Sent |
|----|-------|-------------|--------|---------|
| .015 | 0.7.0_AE_CloudOps | Watchdog shutdown service + SSM nohup wrapper | staged -> GO | YES (AE not registered, filesystem + broker delivery) |
| .016 | 0.4.0_DS_ClientPlatform | Fix 7 cross-instance lib.config imports | staged -> pending | YES (channel push, DS flipped to pending) |
| .017 | 0.4.0_DS_ClientPlatform | NNA/market growth rearchitecture (script 05) | staged | NO -- hold until gold rebuild confirms success |
| .018 | 0.4.0_DE_ClientPlatform | Portal NNA/growth decomposition wiring | staged | NO -- depends on .017 |
| .019 | 0.7.0_AE_CloudOps | Schwab RPS automated daily ingestion | staged | NO -- BLOCKED on Andrew (vendor interface) |

### Documents Updated

1. **COO prompt.md dashboard** -- GLDRST row updated with .015-.019 scope, activation status
2. **COO prompt.md Pod 4 table** -- DS, DE rows updated with new TO assignments
3. **COO prompt.md Shared Services table** -- AE CloudOps row updated with .015/.019
4. **ADHC_HISTRY.json** -- blocking field: NNA rearch now tracked under GLDRST.017

### Org Scan Findings (startup reconciliation)

- 7 live agents: CTO, COO, DE/DS/DT Pod 4, AE PartnerETL, DS TradingOps
- AE CloudOps NOT REGISTERED (offline) -- .015 GO delivered to filesystem + broker
- ADVI_ANONYM: All 11 TOs complete. Follow-on JWT removal and partner table migration TOs not yet issued (low priority, no blockers)
- ADHC_HISTRY: All 8 TOs complete. Gold rebuild in progress (PID 39671). NNA rearch moved to GLDRST.017.
- DEBT_1STRUN: 20/27 scans complete. 7 remaining. No change.
- ADHC_TMSTEL: P0, blocked on Azure AD. No change.
- No stale TOs found requiring correction.

---

## Current State

**Status:** COMPLETE (TO issuance session)
**Active branch:** CLOUD

5 GLDRST operational readiness TOs issued. .015 and .016 activated (GO sent).
.017 held for gold rebuild confirmation. .018 held for .017. .019 BLOCKED on Andrew.

## Next Steps

1. **Verify gold rebuild output** -- when PID 39671 completes, confirm holdings_lots ~$1.58B, asset mix corrected, instance self-stopped. Then activate .017.
2. **After .017 delivers** -- activate .018 (DE portal wiring).
3. **Andrew provides Schwab delivery mechanism** -- unblock .019.
4. **GLDRST P3-P6 activation** -- 12 original TOs (.003-.014) still awaiting explicit Andrew GO for the S3 restructure itself.
5. **ADVI_ANONYM follow-on** -- issue DT TO for JWT tier removal when prioritized.
