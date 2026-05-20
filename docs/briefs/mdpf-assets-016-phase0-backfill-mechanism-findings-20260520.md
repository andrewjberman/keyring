# MDPF_ASSETS.016 -- Phase 0 + Phase 3 mechanism findings

**Author:** 0.4.0_DS_ClientPlatform (DS Base)
**Date:** 2026-05-20
**TO:** MDPF_ASSETS.016 (Cohort 0 historical backfill 2026-01-17 -> 2026-05-17)
**Status:** Phase 0 complete; Phase 1 feeder prep shipped; Phase 1 run + Phase 3-4 HELD pending COO direction on a corrected mechanism.

## Summary

The TO's intent is clear and achievable: populate historical Cohort 0 /
etf_decomposition so the Model Portfolios page reads amendment-correct AUA back
to 2026-01-17. But three findings show the TO's **Phase 1-4 mechanism + formula
spec are stale** relative to current pipeline reality (the TO was authored
2026-05-18; methodology has shifted since). None block the intent; all need a
COO mechanism confirm before the (semi-destructive) historical platinum rewrite.

## Finding 1 -- PFDE/PFOE have no historical NAV (Phase 0 verdict)

Probed `s3://opal-data-etfs` exhaustively: `silver/netassets_daily.parquet`, the
294 per-date `silver/netassets/{date}.parquet` partitions (2025-05-30+), and
`etf_history.csv`.

- **DIVZ + IDVZ** (source: TrueShares): full coverage, 82 distinct dates each
  across the 2026-01-17 -> 2026-05-17 window. Backfillable. Historical rows are
  `source=reconstructed` (the ETFS_NETAST reconstructed series; `net_assets`
  column populated 294/294, `net_assets_reported` null on 280/294). A subset
  carries `inferred=True` (upstream shares interpolation) -- upstream
  provenance, carried with the `source` tag, not DS-side fabrication.
- **PFDE + PFOE** (source: Filepoint): ZERO historical rows. First appear
  2026-05-18 in every source. The Filepoint PFDE/PFOE issuer-CSV integration
  started 2026-05-18.

Materiality: small. On 2026-05-18, PFDE public_residual $2,089,090.53 + PFOE
$2,825,939.32 = $4,915,029.85 = **5.4%** of the $91.33M Cohort 0. DIVZ ($74.0M)
+ IDVZ ($12.4M) = 94.6%.

Disposition (TO Phase 0 pre-authorized): PFDE/PFOE stay honest-null historically
(no bandaid/interpolation per AC5). Historical Cohort 0 = DIVZ + IDVZ residual.

## Finding 2 -- TO Phase 3 mechanism is infeasible (no historical feeders)

TO Phase 3: "re-run `mdpf_aggregate_aua.py` per date ... consumes the freshly-
written WS-D.1 + WS-D.2 partitions plus **the existing 1a + 1b feeders from the
v2 daily-process backfill**."

Empirically false. `s3://opal-data-mdpf/mdpf/feeds/` holds only ~5 recent
partitions per artifact (model_aua_positions / non_model_aua / model_composition
all 2026-05-18+). **There are NO historical 1a/1b/1c feeder partitions.**

Root cause: the v2 daily-process historical platinum (96 partitions, commit
`fb9a910b8`) is `build_mdpf_process_backfill.py` output -- that script builds
the platinum JSON **directly** (1a from SmartX daily-export CSVs, 1b via the
WS-E custody crosswalk inline) and never writes the `mdpf/feeds/` intermediate.

Consequence: re-running the WS-A aggregator for a historical date would read
zero 1a/1b feeders, produce an empty artifact, and (reconcile PASSes on an
empty artifact) **overwrite the existing good historical platinum partition
with an empty one.** The TO Phase 3 step, executed literally, is destructive.

### Recommended corrected mechanism

`build_mdpf_process_backfill.py` already `import mdpf_aggregate_aua as agg` and
iterates per historical date with 1a/1b in hand. Add an etf_decomposition step:
call `agg.build_etf_decomposition(composition, etf_net_assets, model_aua_fm,
partner_held)` per date with the backfilled `etf_net_assets` (DIVZ/IDVZ real,
PFDE/PFOE honest-null) + `partner_held_etf` (49F, from Schwab RPS -- verified
available historically, see below), emit `etf_decomposition` +
`aggregate.etf_public_residual_total` into each historical partition. Re-run
`build_mdpf_process_backfill.py` **scoped to 2026-01-17 -> 2026-05-17** (the TO
excludes the 2026-05-18 daily-forward partition; 1a/1b are NOT re-touched --
the script already recomputes them identically from the same sources).

Partner-held feasibility CONFIRMED: WS-D.2 `wsd_partner_held_etf.py` ran clean
on 2026-03-16 (RPS partition `schwab/silver/rps/date=20260316/` read OK, all 4
ETFs held by 49F: DIVZ $159.0M / IDVZ $132.5M / PFDE $99.4M / PFOE $94.3M). RPS
silver IS available historically (the `build_mdpf_process_backfill.py` docstring
note "~2026-05-08+ only" is stale -- RPS was backfilled later; COO-verified 587
partitions back to 2024-01-12).

## Finding 3 -- the TO's opal_aggregate_aua formula is pre-reversal

TO AC3 + Phase 4: "aggregate.opal_aggregate_aua reflects partner_aua_subtotal +
etf_public_residual_total" and "the page MUST consume opal_aggregate_aua, NOT
partner_aua_subtotal."

The current deployed `mdpf_aggregate_aua.py` (lines 543-552) is **post-reversal**:
`opal_aggregate_aua = partner_total` ONLY -- "Andrew-direct 2026-05-18 reversal
... 'ok dont include cohort zero for now' -- back out the Cohort 0 inclusion."
`etf_public_residual_total` is retained as a separate **audit-trail field**, not
in the headline sum. The historical partitions already follow partner-only.

Recommendation: the .016 backfill should add `etf_decomposition` +
`etf_public_residual_total` (audit field) to the historical partitions and
**leave opal_aggregate_aua partner-only** -- consistent with the deployed
methodology. Putting Cohort 0 in the headline is a methodology decision that
affects daily-forward too (the live aggregator) and is above .016's scope --
needs Andrew/CTO, not a DS reinterpretation of a stale TO line.

NOTE: this also makes the TO's "$1.488B amendment-correct" Phase-anchor and the
Phase-4 "page MUST consume opal_aggregate_aua" spec note stale -- they assume
Cohort 0 in the headline. Phase 4 (which timeseries the page reads --
`platinum/mdpf/aggregate_aua_timeseries.json` vs the legacy
`json/portfolios/aum-timeseries.json` that `build_legacy_compat_emit.py` owns)
also needs COO confirmation.

## Shipped this session (Phase 1 prep, mechanism-independent)

- `build_mdpf_wsd2_etf_netassets_feeder.py` made date-aware (commit `57e2ca4d5`,
  S3 etag MATCH). It could not backfill before (always `tail(1)`). Daily-forward
  behavior preserved exactly (2026-05-18 dry-run verified identical). Honest-null
  tolerance for pre-2026-05-18 PFDE/PFOE absence; daily-forward strict gate kept.

## Ask of COO

Confirm (or redirect) before I run Phase 1 + execute Phase 3-4:
1. Corrected Phase 3 mechanism: modify + re-run `build_mdpf_process_backfill.py`
   (scoped to the window) with an inline etf_decomposition step -- NOT re-run
   the WS-A aggregator.
2. Formula: historical partitions get `etf_decomposition` +
   `etf_public_residual_total` (audit field); `opal_aggregate_aua` stays
   partner-only (deployed-methodology consistent). Confirm, or escalate the
   Cohort-0-in-headline question to Andrew/CTO.
3. Phase 4 target: which timeseries the Model Portfolios page consumes.
