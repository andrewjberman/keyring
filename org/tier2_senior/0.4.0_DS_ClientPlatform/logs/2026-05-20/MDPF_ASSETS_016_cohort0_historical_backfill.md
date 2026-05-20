# MDPF_ASSETS.016 -- Cohort 0 Historical Backfill (2026-01-17 -> 2026-05-17)

**Agent:** 0.4.0_DS_ClientPlatform (DS Base)
**Date:** 2026-05-20
**Branch:** CLOUD
**TO:** MDPF_ASSETS.016 (re-issued 2026-05-20 with the CTO~B amendment block)

## Current State

COMPLETE -- 81 historical platinum partitions (2026-01-19 -> 2026-05-15) now
carry a populated `etf_decomposition` + `etf_public_residual_total` (Cohort 0
audit field); the platinum timeseries is regenerated. All 8 ACs met. RAVC2 to
COO.

## Execution (corrected mechanism per the CTO~B amendment)

The TO was executed against the `<amendment id="2026-05-20-cto-disposition">`
block, which governs over the stale body (the original Phase-3 "re-run the
aggregator standalone" was infeasible + destructive -- see the Phase-0 brief
`docs/briefs/mdpf-assets-016-phase0-backfill-mechanism-findings-20260520.md`).

| Phase | Result |
|-------|--------|
| Phase 0 | Filepoint NAV-depth probe -- DIVZ/IDVZ full coverage, PFDE/PFOE no history before 2026-05-18 (honest-null, 5.4% of Cohort 0). Verdict in the Phase-0 brief b680ea294. |
| Phase 1 | WS-D.1 `etf_net_assets` backfilled for all 81 dates (`build_mdpf_wsd2_etf_netassets_feeder.py --date D --upload`). DIVZ/IDVZ real, PFDE/PFOE honest-null. |
| Phase 2 | WS-D.2 `partner_held_etf/49financial` backfilled for all 81 dates (`wsd_partner_held_etf.py`). RPS has all 4 ETFs historically. |
| Phase 3 | `build_mdpf_process_backfill.py` extended with an inline `agg.build_etf_decomposition()` step + the AC8 guard + `--start-date/--end-date` window scoping; re-run scoped 2026-01-17->2026-05-17. WRITTEN 81/81, **0 AC8 rejects**. |
| Phase 4 | `aggregate_aua_timeseries.json` regenerated (98 dates) with the `cohort0_historical_backfill` meta marker naming this TO. |
| Phase 5 | 3-date spot-check + this RAVC2. |

### CRLF bug caught + corrected mid-execution

The first Phase-1/2 run wrote all 162 feeder partitions to malformed keys
(`{date}\r.parquet`) -- the date list was written by Python text-mode `open()`
which emitted CRLF, and bash `read` left a trailing `\r`. The parquet *content*
was correct; only the S3 keys were wrong. Caught at the Phase-3 dry-run (empty
`etf_decomposition`). Fixed: rewrote the date file LF-only, re-ran Phase 1+2 to
the correct keys (81/81 each). The 162 `\r`-keyed junk objects under
`s3://opal-data-mdpf/mdpf/feeds/{etf_net_assets,partner_held_etf/49financial}/`
remain -- harmless (no reader resolves a `\r` key) but litter; flagged to COO
for a cleanup decision (S3 deletion is a human-confirm operation).

## Phase 5 spot-check

| Date | opal_aggregate_aua | etf_public_residual_total (Cohort 0) | DIVZ / IDVZ residual |
|------|-------------------|--------------------------------------|----------------------|
| 2026-01-20 | $1,396,901,692.73 | $83,244,070.53 | $73.82M / $9.42M |
| 2026-03-16 | $1,463,566,180.36 | $87,966,524.19 | $74.84M / $13.13M |
| 2026-05-15 | $1,648,847,956.91 | $90,788,304.28 | $76.29M / $14.49M |

`opal_aggregate_aua` is UNCHANGED from the pre-backfill value on every date --
correct: the historical series is 49F-only (no Inflection partner; 2a=0), so
the headline (1a+1b+1c+2a) == the 49F partner total. The .016 backfill ADDED
the Cohort 0 audit data (`etf_decomposition` + `etf_public_residual_total`); it
did not move the headline. PFDE/PFOE `public_residual` is honest-null on every
historical date. ANCHOR 2026-05-15 49F total $1,648,847,956.91 matches the
process-backfill reference.

2026-05-18 daily-forward partition: spot-checked, NOT touched by .016
(opal_aggregate_aua $1,848,563,071.88 unchanged) -- out of backfill scope.

## Acceptance Criteria

| AC | Result |
|----|--------|
| AC1 | PASS -- Phase 0 verdict landed (brief b680ea294); PFDE/PFOE honest-null path declared. |
| AC2 | PASS -- 81 `etf_net_assets` + 81 `partner_held_etf/49financial` partitions present at the correct keys (CRLF bug corrected). DIVZ/IDVZ real; PFDE/PFOE honest-null (no synthesized values). |
| AC3 | PASS -- every backfilled partition carries `etf_decomposition[]` (4 entries; DIVZ/IDVZ real, PFDE/PFOE honest-null). identity reconciliation is `NOT_APPLICABLE_HISTORICAL` per the build_mdpf_process_backfill design (the §7 identity gates the daily-forward, not the partial historical series) -- consistent with the pre-existing partitions; .016 did not change that. |
| AC4 | PASS -- timeseries regenerated; `meta.cohort0_historical_backfill` names MDPF_ASSETS_016. opal_aggregate_aua array carries the values; pre-2026-01-19 stays partner-only honestly. |
| AC5 | PASS -- NO bandaid / interpolation / carry-forward. PFDE/PFOE honest-null; the 3 schema-broken BD partitions (2026-01-26/01-28/02-05) keep their pre-existing honest-null 1b. |
| AC6 | PASS -- page-wire spec note: `docs/briefs/mdpf-assets-wsa-page-wire-note-20260520.md` + this log. The page consumes `opal_aggregate_aua` (the 1a+1b+1c+2a headline), NOT partner_aua_subtotal / cohort_2b_audit / etf_public_residual_total. |
| AC7 | PASS -- this session log with the Compiler Tools section; ds-commit-gate exit 0 on every .py edit; Rule 15; no emoji. RAVC2 to COO with the 3-date spot-check. |
| AC8 | PASS -- empty-overwrite guard in `build_mdpf_process_backfill.py`: each rewritten partition's partner_total checked non-zero + within +/-5% of the pre-existing partition's. Phase-3 real run: WRITTEN 81/81, **0 rejects** -- the recompute is faithful to the pre-existing series. |

## Files Modified

| File | Change |
|------|--------|
| data/mdpf/scripts/gold/build_mdpf_wsd2_etf_netassets_feeder.py | Date-aware backfill (`as_of_date` selection + `net_assets` coalesce + PFDE/PFOE honest-null tolerance). Commit `57e2ca4d5`. |
| data/mdpf/scripts/backfill/build_mdpf_process_backfill.py | Inline `etf_decomposition` step + audit fields + AC8 empty-overwrite guard + `--start-date/--end-date` window scoping. Commit `9089736c2`. |
| data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py | `meta.cohort0_historical_backfill` marker. Commit `69b9a8228`. |

## S3 artifacts written

- 81 `s3://opal-data-mdpf/mdpf/feeds/etf_net_assets/{date}.parquet` (2026-01-19..2026-05-15).
- 81 `s3://opal-data-mdpf/mdpf/feeds/partner_held_etf/49financial/{date}.parquet`.
- 81 `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{date}.json` rewritten with `etf_decomposition`.
- `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua_timeseries.json` regenerated (98 dates).
- Code S3-synced to `s3://opal-data-mdpf/code/scripts/{gold,backfill}/` (etag MATCH on all 3 scripts).

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-pipescript io` / `comp-blast` | N/A -- `data/mdpf/scripts/` off the comp graph (CTO 2026-05-20: builder scan-path gap). Direct file-read + S3 probes for all tracing. |
| `.tools/ds-commit-gate.sh` | exit 0 on every `.py` edit (3 scripts). |
| `.tools/safe-commit.sh` | All commits scoped via explicit pathspec. |

## Known follow-ups (for COO)

1. **2026-05-18/19/20 tail-headline gap**: those daily-forward partitions carry the pre-.024 headline (partner_total incl 2b). .016 scopes ≤2026-05-17; .024 is forward-only. Neither covers them. They converge via a re-materialization or as the daily chain rolls forward. Surfaced.
2. **162 `\r`-keyed junk feeder objects** from the CRLF bug -- need a cleanup decision (S3 deletion = human-confirm).

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 -- MDPF_ASSETS.016 complete, AC1-AC8 met. Two follow-ups above (tail gap + `\r` junk cleanup). On accept, MDPF_ASSETS.json phase-narrative update (DS lane-blocked on project JSONs). |
