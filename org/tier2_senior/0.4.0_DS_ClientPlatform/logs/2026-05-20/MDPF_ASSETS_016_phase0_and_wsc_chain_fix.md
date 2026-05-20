# MDPF_ASSETS.016 Phase 0 + WS-C Daily-Chain Fix

**Agent:** 0.4.0_DS_ClientPlatform (DS Base)
**Date:** 2026-05-20
**Branch:** CLOUD

## Current State

**MDPF_ASSETS.016** -- Phase 0 COMPLETE; Phase 1 feeder prep SHIPPED; the
82-date Phase 1 run + Phase 3-4 are HELD pending COO direction on a corrected
mechanism. Three findings show the TO's Phase 1-4 mechanism + formula spec are
stale (the TO was authored 2026-05-18; methodology drifted since). Full brief:
`docs/briefs/mdpf-assets-016-phase0-backfill-mechanism-findings-20260520.md`
(commit `b680ea294`). COO message sent 15:11Z.

**WS-C daily-chain fix** -- COMPLETE. The 2026-05-20 15:00Z mdpf chain failed at
the WS-C feeder; root-caused + fixed + S3-deployed this session.

## MDPF_ASSETS.016 findings

1. **PFDE/PFOE no historical NAV** (Phase 0 verdict). DIVZ + IDVZ have full
   coverage (82 dates each, 2026-01-17->05-17); PFDE + PFOE have ZERO history
   anywhere -- the Filepoint PFDE/PFOE integration started 2026-05-18. They are
   5.4% of Cohort 0 ($4.92M of $91.33M). Disposition: honest-null per AC5 (TO
   Phase 0 pre-authorized). Surfaced to COO 14:55Z.
2. **TO Phase 3 mechanism infeasible.** `mdpf/feeds/` has NO historical 1a/1b/1c
   partitions -- the historical platinum is `build_mdpf_process_backfill.py`
   output (builds platinum directly, never writes the feeds/ intermediate).
   Re-running the WS-A aggregator historically would write empty artifacts over
   good platinum. Corrected mechanism recommended: modify + re-run
   `build_mdpf_process_backfill.py` with an inline `agg.build_etf_decomposition`
   step, scoped to the window.
3. **TO opal_aggregate_aua formula is pre-reversal.** The deployed aggregator is
   post-reversal (opal_aggregate_aua = partner-only; etf_public_residual_total a
   separate audit field). The TO's "partner + etf_public_residual" is stale.
   Recommended: historical partitions get etf_decomposition +
   etf_public_residual_total (audit field), opal_aggregate_aua stays
   partner-only; Cohort-0-in-headline is an Andrew/CTO methodology call.

### Shipped (Phase 1 prep, mechanism-independent)

`build_mdpf_wsd2_etf_netassets_feeder.py` made date-aware (commit `57e2ca4d5`,
S3 etag MATCH). It always took `tail(1)` (latest) regardless of `--date` -- it
could not backfill. Now: `as_of_date` param selects the most-recent row
on-or-before the date (roll-forward); `net_assets` coalesces
`net_assets_reported -> net_assets` (historical reconstructed rows have a null
reported figure); a pre-2026-05-18 date missing only PFDE/PFOE is honest-null
WARN. Daily-forward behavior verified IDENTICAL (2026-05-18 dry-run ==
deployed partition).

## WS-C daily-chain fix

The 15:00Z mdpf chain failed at `build_mdpf_wsc_inflection_feeder.py`:
`RuntimeError: no Orion model-composition bronze found for 2026-05-20`. AE 0.7
flagged it (the .018/.019 seam). Root cause: the chain dispatches `--date today`
with no `--bronze-date`; `pull_orion_model_composition.py` (the MDPF_ASSETS.008
bronze producer) is a manual `--upload` puller, NOT wired into the daily chain
-- only the 2026-05-18 codify-run partition exists.

Fix: added `resolve_bronze_date()` to the WS-C feeder -- when the requested
bronze partition is absent, roll forward to the latest available partition
on-or-before the date (contract section-3.4 pattern). Model composition is
slow-changing structural data (target weights change on rebalance, not daily),
so a few-days-stale composition is sound; logs the staleness, WARN above 7
days. Commit `7d41d28cd`, S3-deployed to
`s3://opal-data-mdpf/code/scripts/gold/build_mdpf_wsc_inflection_feeder.py`
(etag `0f819282ffcacdd318ae31812ce6e508`, MATCH). Verified: `--date 2026-05-20`
dry-run rolls forward to 2026-05-18 (2 days stale), section-7 DUAL check PASS.

`.018`'s fail-loud held -- the chain aborted with no partial 49F-only emit, no
bad Cohort 0. Responded to AE 0.7 (don't ship the AE-side dispatch fix; the
feeder roll-forward is robust). Producer gap (the bronze puller needs a
cadence) flagged to AE + COO for a follow-on TO.

## Files Modified

| File | Change |
|------|--------|
| data/mdpf/scripts/gold/build_mdpf_wsd2_etf_netassets_feeder.py | Date-aware `as_of_date` selection + `net_assets` coalesce + honest-null tolerance (MDPF_ASSETS.016 Phase 1). |
| data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py | `resolve_bronze_date()` roll-forward (WS-C daily-chain fix). |

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| .016 Phase 0 + mechanism findings | docs/briefs/mdpf-assets-016-phase0-backfill-mechanism-findings-20260520.md | COO / CTO |

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-pipescript io` / `comp-blast` (MDPF scripts) | Off-graph per CTO 2026-05-20 directive (builder scan-path gap, comp-tooling-backlog). Used Read/Grep + direct S3 probes for all MDPF tracing. |
| `.tools/ds-commit-gate.sh` | exit 0 on every `.py` edit (build_mdpf_wsd2_etf_netassets_feeder.py, build_mdpf_wsc_inflection_feeder.py). |
| `.tools/safe-commit.sh` | All commits scoped via explicit pathspec. Caught a lane violation: `org/projects/MDPF_ASSETS.json` is ANY_EXEC_OR_AE -- DS cannot commit project JSONs; routed the .017/.019 closure entries to COO. |

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | (1) Confirm the corrected MDPF_ASSETS.016 Phase 3 mechanism + the opal_aggregate_aua formula + the Phase 4 timeseries target (message 15:11Z + brief). (2) Commit the .017/.019 closure entries to MDPF_ASSETS.json (DS lane-blocked; text in the 14:57Z message). (3) Scope a follow-on TO for the orion_model_composition bronze-producer cadence gap. |
| **AE 0.7.0** | Re-trigger the mdpf daily chain -- the runner pulls the fixed WS-C feeder from S3 at boot; WS-C will roll-forward to the 5/18 bronze and complete. |
| **DS Base (self)** | On COO mechanism confirm: execute MDPF_ASSETS.016 Phase 1 (82-date etf_net_assets + partner_held_etf backfill) + Phase 3 (build_mdpf_process_backfill.py etf_decomposition) + Phase 4 + Phase 5 RAVC2. |
