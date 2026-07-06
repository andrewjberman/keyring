# Session — INF DI-1 unrealized-gain re-point (SERVED+CERTIFIED) + DI-7 tax-status restore (DEPLOYED) — lane B

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, DEPLOY, COORDINATE

**Serial:** 0.4.0_DS_ClientPlatform~B (lane B, spun up by Andrew this session to OWN the INF unrealized issue)
**Window:** session launch ~2205Z -> ~2355Z 2026-07-06
**Commits:** d3038c1d0, 885450aae (DI-1); 121d22bfd (DI-7)

## Summary

Two critical-live, HNW-facing INF tax-panel regressions fixed end-to-end, both pipeline-only (ZERO local ETL, the Andrew-STOP held all session).

### DI-1 — client-tax unrealized-gain re-point (CLOSED, CVO-CERTIFIED)
Served INF client-tax unrealized gain was ~13.6x OVERSTATED: $180,511,834.67 (derived) vs $13,285,579 (Orion-native).
- ROOT: INF_C_05 + INF_C_03 DERIVED gain from INF_B_03 account_gains = market_value.fillna(0) - cost_basis.fillna(0) -> booked full MV as phantom gain for the ~68% no-cost-basis accounts + ignored Orion adjusted-cost/amortization.
- FIX (CTO arch-gate PASS, source-not-derive): re-pointed C_05 + C_03 OFF account_gains ONTO the Orion tax_unrealized silver dim, passing the NATIVE total/st/lt_gain_loss FIELDS through VERBATIM (never MV-cost -- CVO's load-bearing guard; MV-cost would re-create the phantom).
  - C_05 (point-in-time): latest tax_unrealized snapshot -> field passthrough -> CANONICAL household rollup (CVO ruling, platform-consistent) + explicit 'unmapped/other' bucket for the 53 accounts that don't map to a canonical household_id (WARN + count + $, NOT silent-drop) + ST/LT coverage guard + ST+LT=Total invariant + data_as_of=snapshot_date (vintage-honest) + household_id float-coercion guard ('463' not '463.0').
  - C_03 (grain-aware, Andrew-direct): per (date, account_id) join to tax_unrealized/snapshot_date={date}/ native total_gain_loss; honest-null on no-snapshot dates.
  - B_03 DEMOTE-not-delete: untouched (stays intact for non-tax consumer C_00.canonical_performance per orion_pipeline_deps.yaml); only C_03/C_05 stopped reading it.
- DEPLOY: code -> code/gold (ETag-MATCH) -> 0.6.1 fired a fresh targeted CHAIN_GOLD_C runner-run -> client_tax_liability.json re-served 23:26:01Z.
- VERIFIED (4-way: me + AE + COO + CVO cert): served firm total $13,285,579 EXACT (LT $12,825,108 + ST $460,465), 890 accts / 290 canonical hh + 53-acct/$0 unmapped bucket, top-5 households all exact (463/449/338/407/201), source=orion_tax_unrealized. CVO CERTIFIED PASS.
- RESIDUAL (non-regression, flagged): D_02 book capital_gains_ttm (consumes C_03) refreshes on next full nightly (targeted run was C-only); account_performance already corrected.

### DI-7 — tax-status classification restore (DEPLOYED, awaiting nightly)
clients_tab.json tax block served 100% taxable / 0 deferred / 0 free since 06-30 ($202,542,849.81 all-taxable; ~48% is actually IRA/Roth).
- ROOT: ADVI_INFREF LEG-1 (cf4a05a9c, 06-30) repointed INF_D_00.load_accounts_dim onto accounts_v2 (no free-text reg type) -> add_tax_status_column defaulted every row 'taxable', fallback_rate=1.0 -> silent (fallback_rate dropped pre-emit).
- FIX (CTO arch-gate: a1 + sentinel-degrade):
  - a1 SOURCE: load_accounts_dim LEFT-JOINs free-text reg_type from frozen silver/accounts_dim/latest.parquet by account_id (ADDITIVE; new _join_reg_type_from_silver; reg_type registration-STATIC so 04-29 freeze correct for tax CLASS). ~96% coverage (~3.8% honest new-onboard fallback). a2 (join A_00 tax_status) REJECTED -- A_00 derives it from the same accounts_v2.account_type bug one hop up.
  - SENTINEL-DEGRADE guard: build_firm_tax_block on fallback_rate==1.0 collapse SUPPRESSES buckets (null) + data_quality=FAIL_COLLAPSED (fail-CLOSED, no hard-raise -> AUA/NNA chain continues). WARN band 5-100% still serves. fallback_rate + data_quality CARRIED into emit + forwarded through D_04 slim.
- DEPLOY: code -> code/gold (ETag-MATCH both). D-stage run rides the next full INF nightly (two birds: DI-7 + the DI-1 capital_gains_ttm residual) -- vehicle timing with 0.6.1.
- FOLLOW-ON (durable, not gated): fix A_00 reg_type source (silver-free-text -> accounts_v2.account_type) so the D_00 silver-rejoin isn't permanent (NFRA_GLDINV-adjacent).

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| comp-blast | account_gains | PASS | INF consumers = C_03+C_05 (re-pointed) + C_00 non-tax (kept) -> demote-not-delete grounded |
| comp-blast | build_firm_tax_block / load_accounts_dim | PASS | DI-7 blast contained: build_firm_tax_block -> clients_tab -> D_04 -> ClientsTab panel |
| comp-pipescript io | INF_C_05, INF_C_03 | PASS | C_03 source-swap confirmed (tax_unrealized in, account_gains gone); consumers C_01b/C_07/D_00/D_02/D_04/D_09 |
| comp-pipescript io | INF_D_00, INF_D_04 | PASS | D_00 now reads silver/accounts_dim (a1 join confirmed); D_04 -> ClientsTab |
| comp-pipescript deployed | INF_C_05/C_03 | WARN | defaulted to bd bucket; grounded INF deploy path directly (opal-data-inf/code/gold) instead |
| comp-freshness | (attempted) | FAIL | needs registered chain/script id; used direct s3 head-object for artifact freshness (rail-checked) |
| ds-commit-gate | all 4 .py | PASS | clean all files (py_compile + AST + ruff) |

**What worked:** comp-pipescript io confirmed both re-point source-swaps at the graph level (esp. D_00's new silver/accounts_dim read). comp-blast grounded both demote/change blast radii.
**What failed:** comp-pipescript deployed defaults to the bd bucket (didn't cover the inf tree) -> grounded the INF deploy path manually. comp-freshness needs a registered id, not an ad-hoc key.
**Gap found:** comp-pipescript deployed has no inf-tree coverage for INF_-prefixed gold scripts; comp-freshness can't take an ad-hoc s3 key. (Both worked around; flag for compiler R&D.)

## Files Modified

See commit messages: d3038c1d0 (C_05+C_03 re-point), 885450aae (C_05 household_id float-guard), 121d22bfd (D_00 a1+sentinel + D_04 slim passthrough).

## Deployment Sequence + Verification

- DI-1: `aws s3 cp INF_C_05, INF_C_03 -> s3://opal-data-inf/code/gold/` ETag-MATCH (a20fd586, 2f6c409b) -> 0.6.1 CHAIN_GOLD_C runner-run -> served client_tax_liability.json 23:26:01Z -> verified $13,285,579 EXACT (4-way). CVO CERTIFIED.
- DI-7: `aws s3 cp INF_D_00, INF_D_04 -> code/gold/` ETag-MATCH (ec590e95, b7c72ceb) -> rides next full INF nightly (D-stage). Verifier pre-staged (scratchpad verify_di7_served.sh).

## Blockers

None (mine). DI-7 final verify is gated on the next full INF nightly (D-stage runner-run) -- a real external cadence gate (0.6.1 lane), NOT a block; vehicle timing being confirmed with 0.6.1.

## Current State

- DI-1 CLOSED, CVO-certified. Served client_tax_liability.json = $13,285,579 (Orion-native), source=orion_tax_unrealized, data_as_of 2026-07-06. C_05+C_03 deployed to opal-data-inf/code/gold + committed (d3038c1d0, 885450aae). B_03 untouched.
- DI-7 code DEPLOYED (opal-data-inf/code/gold/INF_D_00.portal_aggregates.py + INF_D_04.client_portal_summary.py, ETag-MATCH, commit 121d22bfd), NOT yet served -- rides the next full INF nightly (D-stage). Before-state: clients_tab.json tax = $202,542,849.81 taxable/100%/0/0. Target: ~52/48 split, fallback_rate ~3.8%, data_quality='OK'.
- Andrew guard honored throughout: 100% Orion/INF (opal-data-inf, silver tax_unrealized + silver/accounts_dim), NO Black Diamond conflation.

## Next Steps

1. **[0.6.1_AE_PartnerETL]** INF nightly ETA + DI-7 vehicle call (ride nightly vs ad-hoc D-stage). Ping on the D-stage re-serve.
2. **[0.4.0_DS_ClientPlatform~B]** on DI-7 re-serve: run verify_di7_served.sh -> ping CVO for census-exact exercise-gate -> close DI-7. Also verify DI-1 D_02 capital_gains_ttm self-heal on the same nightly.
3. **[3.0.0_SA_CVO]** C_03-limb content-verify (native vs derived) to fully close DI-1 both limbs; DI-7 census-exact cert on re-serve.
4. **[0.4.0_DS_ClientPlatform~B / CTO]** durable follow-on: fix INF_A_00 reg_type source (accounts_v2.account_type -> silver free-text) so the D_00 silver-rejoin isn't permanent. Not gated tonight.
