# 0.4.0_DS_ClientPlatform — /work work_1715Z (MDLP_DISTFIX I3 BUILT + DEPLOYED)

**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, VALIDATE

## MDLP_DISTFIX I3 — shared >=$1K floored-percentile helper (commit 50f6a32ba)

Andrew-pre-directed fix for the Inflection Segment Analytics P10 dust ($8.42 / min=$0.00): percentiles
computed on raw `vals>0` while the histogram floored $1K -> sub-$1K dust on P10. DE root-cause:
producer = orion INF_D_04._build_geo_view (raw `aua_series.quantile()`, bypasses the stats helper).

### Shipped
- **Canonical `lib/floored_percentiles.py`** — `floored_distribution_stats(values, num_bins, floor=1000)`
  + `floored_percentiles` + `floor_series`. Floors accounts >=$1K for the distribution AND all
  percentiles + histogram (one floored basis). Byte-identical in bd/gold/lib + orion/gold/lib.
- **Structural byte-identical SYNC-GUARD** in `.tools/ds-precommit-check.py` (`check_dual_pipeline_sync`,
  CTO placement ruling) — separate runtimes means two physical copies; the guard FAILS the gate on any
  divergence (tested: pass-on-identical, exit-1-on-diverge). Generalizes to any bd<->orion shared gold helper.
- **4 refactors:** bd D_01.calculate_distribution_stats; bd D_04._calculate_distribution_stats (retires the
  "inlined from D_01, update in lockstep" drift-copy); orion INF_D_04._calc_distribution_stats_adv; orion
  INF_D_04._build_geo_view (THE BYPASS — by_segment + total size-stats floored via the helper; count=household
  + sum=full-state kept as aggregate totals so donut/segment totals stay true).
- Gold tier (Rule 17). Gate CLEAN (py_compile + undefined-name + sync-guard + ruff, 5 files). Functional
  smoke: min/p10 >=1000, sub-$1K excluded.
- Fixed-forward pre-existing D_01 gate debt: Rule-15 future-import + ruff (removed unused os/numpy, split
  import, noqa'd 2 pre-existing dead vars). All flagged in commit; none touch I3 logic.

### Deployed (safe-deploy pre-push hook, Rule 13 — both pipelines)
- bd: D_01 + D_04 MATCH on s3://opal-data-bd/code/gold/ + lib/floored_percentiles.py.
- orion: INF_D_04 + lib/floored_percentiles.py on s3://opal-data-inf/code/gold/ — both byte-verified S3==local.

### Close (next-day, C1 — NO ad-hoc run)
Tonight's SCHEDULED nightlies (bd ~04:00 UTC, inf ~13:00 UTC) pick up the code. Tomorrow: served-verify
the orion `partner_analytics_monthly.json` views.geo.*.distribution.percentiles (P10 -> >=$1K, P25-P90
~unchanged) + bd partner_analytics + visual smoke the live Inflection Segment Analytics panel. RAVC2-close then.

## Other workstreams (this session)
- R2 (NFRA_COSTRED): DONE — applied + verified (4-rule Option B); tail = storage-trend read next CloudWatch cycle.
- GLDINC §5: review accepted into PRD v0.2 (§5a = my restatement-detection primitive); §4a carve-out granted;
  reconcile-correctness co-owner; engages on P0 reconcile-gate def. v0.2 Andrew-approved.
- MDLP I1+I2 (collapsed re-source): gated behind I3 (now built) — next, surface MDPF feed-contract +
  partner-set scope to base-DE before build.

## Compiler Tools
| Tool | Run | Result | Notes |
|---|---|---|---|
| comp-pipescript io | D_01, D_04 | clean, no COLUMN GAPS | helper change is percentile-basis logic, doesn't alter columns read/written |
| comp-pipescript deployed | D_01, D_04 | MATCH | confirms bd S3 = committed code post-safe-deploy |
| ds-commit-gate | helper x2 + D_01 + D_04 + INF_D_04 | exit 0 (incl. new sync-guard) | py_compile + undefined-name + sync-guard + ruff |
| (S3 byte-verify) | orion INF_D_04 + helper on opal-data-inf | S3==local IDENTICAL | comp-pipescript deployed is bd-keyed; orion verified by direct byte-diff |

work-cycle:0013
