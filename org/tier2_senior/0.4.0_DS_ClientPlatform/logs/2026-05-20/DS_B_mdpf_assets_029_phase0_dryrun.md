# DS~B Session Log -- MDPF_ASSETS.029 Phase 0 (v0.9 historical-backfill dry-run)

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-20
**Branch:** CLOUD
**TO:** MDPF_ASSETS.029 -- v0.9 historical-backfill, Phase 0 only (non-mutating dry-run)
**PRD:** docs/architecture/MDPF_ASSETS.md v0.9 (8951ce8f0)

## Summary

Phase 0 of .029 -- a NON-MUTATING dry-run + mechanism validation for the v0.9
historical backfill of the platinum aggregate_aua series. CTO~B amendment
folded: traced BACKWARD from the Model Portfolios "Daily AUA Analysis" chart,
enumerated every artifact it consumes, resolved the aggregate_aua_timeseries
vs aum-timeseries.json identity question.

## Findings (full detail in the brief)

- `aggregate_aua_timeseries.json` != `aum-timeseries.json` -- three distinct
  artifacts, two buckets, two producers. The .029 named target
  (aggregate_aua_timeseries) has NO portal consumer (whole-tree grep empty).
- The "Daily AUA Analysis" chart reads `aum-timeseries.json` (model layers)
  + `non_model_assets.json` (1b overlay) -- BOTH produced by
  build_legacy_compat_emit.py = the .030 script.
- .029 -> .030 is a real data dependency: build_legacy_compat_emit.py reads
  the aggregate_aua/{date}.json partitions .029 re-materializes.
- Mechanism validated: scratch re-mat of 2026-05-20 via
  `mdpf_aggregate_aua.py --date 2026-05-20 --source s3 --out <scratch> --dry-run`
  reproduced the live v0.9 partition BIT-IDENTICALLY (headline
  $1,748,030,393.45 to the cent).
- 98 partitions live (2025-12-23..2026-05-20); 97 are pre-v0.9, 2026-05-20
  already v0.9 (.028). v0.8->v0.9 boundary skew = -$100.8M at the cutover.
- Cost flag: older-date re-mat needs a per-date WS-B+WS-E feeder-chain re-run
  (EC2 gold-runner) -- Phase-1 work, not a ~1h Phase 0.

## Non-mutating verification (AC0)

- All re-materializations -> `.runtmp/mdpf029_scratch/` (local scratch).
- No S3 object written/overwritten/deleted. Aggregator run with `--dry-run`
  + `--out <local>`.
- No code committed. Only the brief + this log committed (TO permits the
  brief commit; "no commit" applies to pipeline CODE).

## Deliverable

docs/briefs/mdpf-assets-029-phase0-v09-historical-backfill-dryrun-20260520.md
-- routed to 1.0.0_SA_CTO~B (direct) + 2.0.0_SA_COO~B (separate CC send).

## Compiler Tools

| Tool | Result |
|------|--------|
| portal-tree grep `aggregate_aua_timeseries` | empty -- confirms no portal consumer |
| aggregator `--dry-run`/`--out` | built-in non-mutating mode -- used for the scratch re-mat |
| comp-* | data/mdpf off-graph (known gap); chart-backward trace done by direct read of ModelPortfolios.tsx + portal-proxy.ts |

## Current State

MDPF_ASSETS.029 Phase 0 COMPLETE. HARD STOP -- Phase 1 (the historical
partition rewrite) is Andrew-gated, does NOT execute on this GO. CTO~B
reviews the brief + carries a go/no-go-to-rewrite recommendation to Andrew.

## Next Steps

| Recipient | Item |
|-----------|------|
| **CTO~B 1.0.0** | Phase-0 brief (direct) -- review + Andrew go/no-go relay. |
| **COO~B 2.0.0** | Phase-0 brief (separate CC send) -- the brief confirms .030's scope_pending: .030 must grow to include the historical non_model_assets.json backfill. |
