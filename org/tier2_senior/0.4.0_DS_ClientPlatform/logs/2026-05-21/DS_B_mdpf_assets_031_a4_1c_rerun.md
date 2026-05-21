# DS~B Session Log -- MDPF_ASSETS.031 A4 (1c re-derive + 297-partition re-run)

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-21
**Branch:** CLOUD
**TO:** MDPF_ASSETS.031 amendment A4 -- the .032-outcome-(a) 1c correction

## Summary

Re-derived `.031`'s 1c (SMA) from `0` to flat **$19,673,469.29** across all
297 partitions per CTO~B's `.032` ruling, recomputed `1b`, re-ran the 297
partitions + the rollup, applied to S3, verified all-pass. The `$0 -> $19.67M`
1c component-seam that triggered CTO~B's HOLD is closed. Headline invariant.

## Sequence

1. `.029` quick-check (read-only) -- stored ratio-1c vs an independent
   SMA-source estimate, 6 samples. Worst gap $1.50M (upper-bracket estimate)
   -- within the ~$2-3M tolerance. `.029` STANDS, no re-open. CTO~B accepted.
2. Re-derived 1c: flat $19,673,469.29 (the `.031/.029` seam anchor). Basis:
   the SMA per-date value is unrecoverable (95/189 allocations closed, no
   close-dates, no historical values, survivorship-biased openedDate curve)
   -- flat is the honest fallback CTO~B named; a taper would be manufactured
   precision. Premise correction surfaced + acknowledged by CTO~B.
3. Re-ran the 297 `.031` partitions to scratch -- 0 negative 1b, 0
   identity-break, 0 AC1-fail.
4. Verified scratch -- 7/7 checks pass incl. headline invariance (0 drift).
5. Applied -- 297 partitions to S3; rollup rebuilt + uploaded.
6. Verified S3 state -- all-pass: 1c flat 297/297, seam $0.00, AC1 297/297,
   identity 0 breaks, 0 negative 1b.

## Files / artifacts

| Artifact | Detail |
|----------|--------|
| docs/briefs/mdpf-assets-031-a4-1c-rerun-ravc2-20260521.md | the RAVC2 deliverable |
| s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{2024-11-01..2025-12-22}.json | 297 re-uploaded partitions |
| s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua_timeseries.json | rollup rebuilt (395 dates, generated_at 2026-05-21T14:57:58Z) |
| .runtmp/mdpf031/build_031_sweep.py | sweep (scratch; C1_FLAT edit) -- ad-hoc, .runtmp gitignored |
| .runtmp/mdpf031/c1_redrive_probe.py, verify_031_redrive.py, verify_031_s3_final.py | probe + verification (scratch) |

## Compiler Tools

| Tool | Result |
|------|--------|
| comp-pipescript io | N/A -- the re-run touches no gold/silver script; it re-materializes data partitions via the .runtmp sweep + the committed rollup builder |
| build_aggregate_aua_timeseries.py | run unmodified (--upload) -- re-aggregates the corrected S3 partitions; the PORTAL-consumed rollup |
| (verification) | verify_031_s3_final.py -- live-S3 rollup + 297 partitions, all checks pass |

Note: the `.031` backfill is a one-time historical data materialization via
`.runtmp` scratch scripts (the `.runtmp` dir is gitignored) -- consistent with
how `.029`/`.031` were originally built. No `data/*/scripts/` producer was
changed, so Rule 13/14/15 gates do not apply to this re-run; the committed
`build_aggregate_aua_timeseries.py` was run, not modified.

## Current State

`.031` A4 re-run COMPLETE + verified on S3. RAVC2 routed to COO~B CC CTO~B.
On COO~B independent S3 re-validation + CTO~B output-validation accept,
`.031` re-closes -> MDPF_ASSETS 3-step-closes.

## Next

| Recipient | Item |
|-----------|------|
| COO~B 2.0.0 | RAVC2 -- independent S3 re-validation (1c non-zero per-partition; seam level-continuous; AC1 297/297) |
| CTO~B 1.0.0 | CC -- output-validate the re-run |
