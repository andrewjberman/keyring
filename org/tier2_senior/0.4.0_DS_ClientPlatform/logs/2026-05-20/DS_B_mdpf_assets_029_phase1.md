# DS~B Session Log -- MDPF_ASSETS.029 Phase 1 (v0.9 historical backfill)

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-20
**Branch:** CLOUD
**TO:** MDPF_ASSETS.029 Phase 1 -- v0.9 historical backfill of the 97-partition
aggregate_aua series (Andrew-gated; GO ab6d2a87c)

## Summary

Re-materialized the 97 historical `platinum/mdpf/aggregate_aua/{date}.json`
partitions (2025-12-23..2026-05-19) onto the PRD v0.9 basis, rebuilt the
rollup. The full historical series is now v0.9, continuous, with the
−$100.77M v0.8→v0.9 methodology cliff removed.

## Staged execution (CTO~B staging)

- **Checkpoint 1 -- opening probe.** Found the literal TO mechanism ("re-run
  WS-E + WS-B per date") non-executable -- WS-B's SmartX `enterprises/
  allocations` endpoint is current-state-only. Andrew corrected the mechanism
  mid-probe: read the existing daily artifacts (1a from aum-timeseries.json,
  Schwab-whole from schwab/silver/rps, 1c ratio-estimated). Brief:
  docs/briefs/mdpf-assets-029-phase1-opening-probe-20260520.md.
- **Checkpoint 2 -- scratch batch + calibration.** 3-date scratch validated
  the mechanism. Surfaced the 1a-series anomaly + measured the RPS-vs-crosswalk
  delta (drifts $16.6M→$56.2M). Briefs: ...checkpoint2-scratch-batch... +
  ...checkpoint2-calibration...
- **Seam resolution.** Flagged that CTO~B's HYBRID reintroduced silver/
  allocations against Andrew's verbatim directive -> CTO~B walked the HYBRID
  back -> Andrew ruled **Option B** (RPS + calibration lift). CTO~B ratified
  the calibration form: **linear delta-$ fit** (not a flat K -- the gap drifts).
- **RULING #1 -- 1a smoothing.** 05-15/18/19 interpolated; 01-14 (inflow) +
  04-02 (market) corroborated real via by_model decomposition. Brief:
  ...ruling1-1a-smoothing-rps-prep...
- **Checkpoint 3 -- the 97-sweep (this log).**

## Mechanism

calibrated_Schwab(d) = RPS_whole(d) + delta_$(d);
delta_$(d) = 14,796,793 + 343,246 × days_since(2026-01-16);
1c(d) = 0.0184769 × 1a(d); 1b(d) = calibrated_Schwab − 1a − 1c.
Construction: v0.8 partition as template, 49F block patched to v0.9,
methodology_version=v0_9, calibration + 1a-adjustment markers in meta,
Inflection partner preserved verbatim, aggregate recomputed.

## Verification

| check | result |
|-------|--------|
| S3 partitions all v0.9 | 98/98 methodology_version=v0_9 |
| 49F identity 1a+1c+1b==partner_custody_total | 0 breaks / 98 |
| negative 1b | 0 / 98 |
| headline series | continuous $1,328.26M..$1,748.03M |
| boundary 05-19→05-20 | +$4.70M (the −$100.77M v0.8 cliff GONE) |
| rollup aggregate_aua_timeseries.json | rebuilt 98 dates, uploaded |

## Files / artifacts

| Artifact | Detail |
|----------|--------|
| 97 × aggregate_aua/{date}.json | re-materialized v0.9, S3 opal-data-portal-v2 |
| aggregate_aua_timeseries.json | rollup rebuilt + uploaded |
| local backup | .runtmp/mdpf029_scratch/backup_partitions/ (98 prior objects) |
| backfill tooling | .runtmp/mdpf029_scratch/ (one-off; mechanism documented in the briefs + per-partition meta) |

## Non-destructive (AC / Andrew "be ginger")

Versioned bucket; local pre-write backup of all 98 prior objects; overwrite-
in-place; no object deleted. Rollback = restore prior version / local backup.

## Compiler Tools

| Tool | Result |
|------|--------|
| comp-pipescript / comp-validate | data/mdpf off-graph (known gap); verification done by direct S3 read -- 98/98 v0.9, identity + boundary checks all pass |

## Current State

MDPF_ASSETS.029 Phase 1 COMPLETE. RAVC2 to COO~B CC CTO~B. Brief:
docs/briefs/mdpf-assets-029-phase1-checkpoint3-97sweep-complete-20260520.md.

## Next Steps

| Recipient | Item |
|-----------|------|
| COO~B 2.0.0 | RAVC2 -- .029 Phase 1 complete. Unblocks .030 (legacy-emit v0.9). |
| CTO~B 1.0.0 | CC on RAVC2; carries the 2024-depth extension decision to Andrew (separate). |
| (queued) | ADHC_VALGATE.003 (C-4) -- parked behind .029, now resumable. |
