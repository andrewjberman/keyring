# Deploy Completion Record -- bd silver allocations intraday-T-0-stub completeness reject

**Status:** CLOSED -- reject landed + ground-truth-verified (S3 ETag == local md5); no stranded leg.
**Date opened:** 2026-07-02T20:38Z (deploy-start)
**Date closed:** 2026-07-02T20:42Z
**Class:** deploy-completion (NEVER rule -- opened at deploy-start, closed at completion; no half-landed)
**Owner:** 0.4.0_DS_ClientPlatform~B
**Authority:** AE 0.6.0 wire-follow-on (203549Z: "land the alloc-reject backstop, PRIMARY"). ADVI_ETLFIX bd stub-guard.
**Commit:** 844a2cb45 (pushed). **RAVC:** 0.6.0_AE_PartnerETL + 2.0.0_SA_COO + 1.0.0_SA_CTO.

## What deployed

| Artifact | Target | ETag (== local md5) | Verified |
|---|---|---|---|
| merge-daily-incremental.py (alloc stub-reject) | s3://opal-data-bd/code/silver/ | c54d07908c69e2d9a9035050e0367f40 | HEAD-object OK 20:42Z (safe-deploy gate PASS) |

## What / why

GROUNDED LIVE: silver/allocations/2026-07-02.parquet landed at 45KB vs 07-01 = 1.2MB -- BD returns an
intraday T-0 allocations SNAPSHOT as an undersized partial stub. The allocations merge had ONLY a
col-count check (unlike unrealized's 0-row skip + holdings' nzf floor), so the stub landed + could
shadow the good T-1 snapshot (silent-partial). Added a row-count completeness floor: reject a snapshot
whose rows < ALLOC_MIN_ROW_FRACTION (0.5) of the most-recent OTHER-date partition
(`_latest_alloc_row_count` excludes the same date). Fail-OPEN on no-baseline/unreadable. Returns None ->
re-checked -> self-heals when BD lands a full snapshot. Rule-17-consistent (rejects an incomplete SOURCE
FILE, not a field-slim/row-filter). boto3-native.

## Verification

py_compile + ds-commit-gate clean. Tests: 25 bd green (+4 baseline exclude-same-date/none/empty +
threshold). ETag == local md5 (above). The existing 45KB 07-02 stub self-heals (etag reprocess on a full
07-02 land); served safe @07-01 empirically (AE: gold keyed on prices/run-date, not latest-alloc).

## Cross-lane (belt, AE)

AE adds runner T-1 targeting for the SNAPSHOT tables (defense-in-depth) as a fast-follow (my alloc-reject
is the sufficient primary, so it doesn't gate the coordinated apply).

**Status: CLOSED** -- artifact deployed + ETag-verified; no stranded leg.
