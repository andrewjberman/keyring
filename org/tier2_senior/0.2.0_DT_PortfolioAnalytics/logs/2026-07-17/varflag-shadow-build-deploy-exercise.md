# Session Log -- 0.2.0_DT_PortfolioAnalytics -- 2026-07-17 ~1704-1815Z
**Archetype:** TO execution (greenfield guard build + deploy + runtime exercise)
**Project:** MDPF_VARFLAG (TO_VARFLAG_SHADOW_01 @f70328bda)

## Built + deployed (yang-pipeline-v1.5.0)
- yang-varflag-check: log-only shadow variance gate on the 3 Model-Portfolios artifacts,
  post-InvalidateCloudFront SFN state (Catch-all both layers -- publication untouched by
  construction). Stdlib+boto3 ONLY (no layers -- the openpyxl class cannot recur).
- Ratified stack implemented verbatim, CVO constants cited by commit in varflag_config.json:
  V1 25pct slow cells (1pp floor, spreads annotate); peers P1 50pct 1Y/SI + P2 envelope
  (monotonic + 2x headroom) + bounds; V2 fast-cell bounds; V3 structural + WTD-vol allowlist;
  timeseries at derived-stats grain (90 cells from 14,450 leaves). Binding P1s: accepted-baseline
  from execution metadata (DDB + outputs-manifest, BE01 UUID seam-join reused), FM-6 loud-on-miss,
  Jan-YTD suppression. New scoped IAM role (not the shared yang role).

## Acceptance -- all exercised
- Replays on real S3 versions: corrupt-0716 vs healthy-0712 = 6/6 ST slow cells (551-1151pct),
  served + derived grains agree to the decimal; healthy-vs-healthy = 0.
- 49-vintage calibration REPRODUCED: 1.85 FP/upload over 46 healthy transitions (budget <=2);
  vol separation healthy<=70pct vs corrupt>=679pct; honest tail named (stale re-upload file-order
  transitions, excluded by the accepted-baseline rule live).
- Deployed-runtime invokes on the real 53a06944 execution: first run flagged the correction vs
  the corrupt baseline (the instrument demanding the disposition annotation) -> annotated
  exec-ed7efa408fe5 varflagDisposition=rejected (additive; basis = Andrew's own rollback) ->
  terminal 0 flags / 600 cells, per-artifact baselines benchmarks/ts<-07-10, peers<-06-30.
- Two real defects surfaced BY the runtime exercise and cured same-session: exec-hex vs
  pipeline-UUID made the self-baseline exclusion inert post-hoc; newest-manifest-only baselining
  burned a standing weekly FM6 flag for monthly peers. Per-artifact walk-back + manifest-path
  UUID guard; redeployed; 0-diff.

## Open
- Shadow evidence clock: >=3 real uploads before P2 (COO decomposes). CVO instrument-verification
  handoff sent (incl. the pstdev-vs-stdev deviation note + the 6-flags-vs-13-cells census diff).
- Carried: 07-18 03:05Z bd49f first unattended fire read; F4 first real-email row.

## Compiler tools
comp-grep/comp-glob (SFN definition + TF discovery). Constants NOT re-derived (TO law) -- cited
from CVO's committed analyses; calibration replay recomputed only to REPRODUCE, per acceptance.
