# MDPF_REVAMP gold dim_* projections -- decision-independent latest-parity set (DS)

**archetype:** IMPLEMENT
**secondary_archetypes:** EXPLORE, COORDINATE
**Serial:** 0.4.0_DS_ClientPlatform | **Date:** 2026-07-20 | **Window:** session start (~20:12Z) -> 21:25Z

## Summary
CTO dispatched me (20260720T201254Z) the MDPF_REVAMP gold `dim_*` projection build: author the gold
projection CODE that inverts monolith silver `fact_*` -> new gold `dim_*` -> the served Model-Portfolios
artifact shapes, build-alongside, parity vs the LOCKED baseline (84d22bb4d). Base COO/CVO offline -> all
routed to base CTO direct (gate + code-review). Delivered the ENTIRE decision-independent latest-parity
set: TO-0 crosswalk + TO-1 aggregate (all 3 firms latest) + TO-3 distribution (all 3 firms). Everything
that does NOT wait on the D1/D2 product ruling is built, parity-checked, committed, pushed. Holding at the
pre-D1 checkpoint (hard external gate = Andrew's D1/D2).

## Work done
- **Grounded** end-to-end (spec v1.1 6edc1b89a S9-first, baseline 84d22bb4d, audit brief, 5 silver tables,
  5 legacy producers, live served artifacts). Key findings: F1 history is INTRA-PARTITION (fact_model_aum_daily
  `day` col, 1223 days); the served HISTORY is a rederived/interpolated backfill diverging +10-40% from the
  measured aum_daily series in 2024-25 (converging to tie now) -> the D1 question; F2 delta = daily drift;
  corrected my own F8 error (SMA arrays are 391-None+38-tail, not all-null).
- **TO-0** `mdpf_revamp_model_crosswalk.py`: model_id-only crosswalk (F5), rmid live-bridge, raise-on-unknown,
  8th dormant model + KNOWN_EXCLUDED_ECLIPSE_IDS; self-test PASS.
- **TO-1** `dim_mdpf_aggregate_aua_timeseries.py`: A5/A6 spine, 3-firm dispatch. LATEST parity: 49F model
  5-core $1,395.40M (F2 -$1.9M drift); INFLECTION model $137,170,028.82 + custody(orion fact_assets.currentValue)
  $201,648,128.16 + non_model $64,478,099.34 ALL tie served TO THE CENT; GLOBAL firm-sum model $1,532.57M
  (F2-only, SOLID). History arrays D1-HELD; 49F custody(fact_rps) D2-HELD.
- **TO-3** `dim_mdpf_account_distribution.py`: A3/A7 distribution, 3-firm dispatch, byte-parity stats. 49F
  near-exact (excl_unfunded 34 EXACT, std within $0.71); INFLECTION EXACT (534=534, all stats); GLOBAL union
  near-exact (7550 vs 7553). CTO candidate-new-Opal safeguard caught eclipse_id 30 (90/10 blend), correctly
  excluded for parity.
- **Custody value-basis (D2-i, resolved):** 49F served $1,644.99M ties NO monolith candidate (fact_rps
  positions-only $1,631.66M / net_mv_plus_cash $1,665.34M bracket it -> legacy partial-cash artifact, folds to
  D1). Inflection ties EXACTLY (orion fact_assets.currentValue).

## MCP traffic
~18 messages, all with base CTO (gate) + 0.2.0_DT_PortfolioAnalytics (portal-side coordinate). Significant:
CTO ruled D3(add 8th, new module)/D4(zero-pad), HELD D1/D2 -> escalated to Andrew with my Option-A rec;
approved the inflection filter-vs-raise asymmetry + the safeguard; accepted every TO parity. DT: staging
split CONFIRMED (I produce gold/mdpf_revamp/{firm}/, DT owns portal/* publish + serving); parity harness
built+exercised (2e87dbc22); TO-3 staging-upload sequenced INTO AE's publisher-apply (no solo pre-write).

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-which/comp-grep | (not run) | -- | targeted Read/Glob on known files + Explore agent for the producer/schema map |
| safe-commit.sh (surface-check + risk-reflex) | 5 commits | PASS | no critical surface; reflex clean each |
| commit-gate.sh | every .py edit | PASS | py_compile + ds-precommit + ruff, all clean |
Native tools (Read/Glob/Explore agent) + boto3 data-plane reads (silver/served inspection, off-rail per
Rule 21 data-plane carve-out) carried the grounding; no rich comp-tool fit the "read a specific parquet
schema / served JSON shape" need. Gap: none new.

## Files Modified
See commit messages: **f4a409182** (TO-0 + TO-1 49F skeleton + grounding notes), **a511dabbb** (TO-3 49F),
**2b8963881** (TO-3 inflection + safeguard + KNOWN_EXCLUDED), **4f0aedd55** (TO-1 inflection+global),
**3602420fd** (TO-3 global). All under data/mdpf/scripts/gold/ + the grounding-notes deliverable.

## Blockers
None assumption-blocked. HARD EXTERNAL GATE: Andrew's D1 (serve-real measured history vs replicate the
interpolated backfill) + D2 (49F custody completeness) -- CTO is bringing him the completed checkpoint + the
call. All history work (TO-1 history, TO-2, TO-4, TO-5) + 49F custody-basis wait on his ruling.

## Current State
- **Crosswalk** `data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py`: canonical model_id->model_key +
  eclipse_id/orion_id; `resolve_model_id`/`resolve_rmid`/`resolve_eclipse_id` (raise-on-unknown);
  `build_rmid_bridge`; KNOWN_EXCLUDED_ECLIPSE_IDS={30}; `_self_test()` (run as __main__).
- **TO-1** `dim_mdpf_aggregate_aua_timeseries.py` (`--firm 49financial|inflection|global|all`, `--dry-run`/
  `--out-dir`): reads opal-data-assets smartx/platform/silver (fact_model_aum_daily day-col F1 +
  fact_model_allocation_roster basis + schwab/08242234 fact_rps custody) + eclipse/inflection/silver
  fact_portfolios_full + orion/inflection/silver fact_assets. Emits the served F4 shape; LATEST solid,
  history D1-HELD (single-point skeleton), 49F custody D2-HELD.
- **TO-3** `dim_mdpf_account_distribution.py` (`--firm 49financial|inflection|global`): allocation-grain
  (49F) / portfolio-grain (inflection) distribution, byte-parity stats (>=$1K floor, np.percentile, log
  histogram). PARITY-FINAL all 3 firms.
- **Staging target (DT-confirmed):** gold/mdpf_revamp/{global,49financial,inflection}/{aggregate_aua_timeseries,
  account_distribution}.json (underscore names); DT publishes -> portal/model-portfolios|portfolios/*. NOT
  yet uploaded (sequenced into AE's CTO-gated publisher-apply).
- Grounding notes: org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/MDPF_REVAMP_grounding_notes_20260720.md.

## Next Steps
- **[Andrew, via 1.0.0_SA_CTO]** rule D1 (measured-history serve-real vs replicate-backfill) + D2 (49F custody
  completeness). Unblocks all history + 49F custody.
- **[me / 0.4.0_DS_ClientPlatform]** on D1/D2: complete TO-1 history arrays (all 3 firms) + 49F custody-basis;
  build TO-2 (aum-metrics/timeseries), TO-4 (non_model_assets), TO-5 (vintage from DDB) -- all history/backfill.
- **[1.0.0_SA_CTO + 0.7.0_AE_CloudOps + 0.2.0_DT_PortfolioAnalytics]** AE publisher write-IAM + Lambda apply
  (CTO-gated) -> I --upload TO-3 both firms to gold/mdpf_revamp/* -> publisher exercised -> DT served-vs-published
  parity (inflection EXACT first). The decision-independent first green end-to-end.
- Reachable, event-driven (Monitor b2f21yxyb). No crons.
