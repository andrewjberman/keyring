# MDPF_REVAMP -- first green end-to-end + D1=serve-real phase (DS)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE
**Serial:** 0.4.0_DS_ClientPlatform | **Date:** 2026-07-20 | **Window:** ~21:25Z (prior log c0ab21caa) -> ~22:52Z

## Summary
Two milestones this window. (1) Landed the FIRST decision-independent GREEN END-TO-END: TO-3
account_distribution (all 3 firms) -> gold/mdpf_revamp staging (my --upload, listing-verified) ->
AE's opal-assets-mdpf-portal-publisher (v0.30.0, 22a-fenced) copied byte-identical to portal/* ->
DT served-vs-published parity = 3/3 shape-clean (one global display-convention finding caught + fixed
in a fast loop). (2) Andrew ruled D1 = SERVE REAL/COMPLETE; drove the serve-real phase: 49F serve-real
history + the never-widen named-delta LEDGER (md+JSON, per-quarter segmented + latest-tie, DT-verified)
+ grounded/resolved all 3 CTO flags -- TWO grounding catches kept wrong data off the served page.

## Work done
- **TO-3 end-to-end (first green):** wired --upload (ceab29600, ListObjectsV2 landing verify); populated
  gold/mdpf_revamp/{49financial,inflection,global}/account_distribution.json (verified ETags); AE published
  byte-identical (source ETag==portal ETag). GLOBAL parity finding (per-firm relabeled display used vs the
  served GLOBAL un-relabeled convention + extra firm scoping) -> FIXED 99fdd755a via a per-SCOPE+ARTIFACT
  display lookup folded into the crosswalk (account_dist_display; served-derived) + leaner global top-level;
  DT re-parity = 3/3 clean (residual F2 date-drift only).
- **D1=SERVE-REAL phase (Andrew ruled via CTO 220141Z):**
  - Named-delta LEDGER (never-widen evidence): human md (2b57be0b0) + machine JSON (43f989647 -> 70a1d077c
    per-quarter segmented -> e3b9772f9 latest-tie). Data-derived: 49F D-1 convergence 2026-04-09; per-quarter
    windows 2025Q1 [21,42]% -> post-conv [-1.43,2.08]%; D-2 custody +$20.34M/0.5%. DT harness verified it
    catches mid-range (2025Q3 +30%->UNEXPLAINED) AND small latest bugs.
  - TO-1 49F serve-real history (aa90d97dc): model_aua[]/by_model.model_value[] = REAL aum_daily day-col
    series (model_aua[0] $436.84M real vs backfill $353.80M); core D4 zero-pad, SMA 38-day depth; internal
    invariant model_aua[i]==Sigma-core PASS. Custody latest = full-envelope fact_rps_s2 net_mv_plus_cash
    $1,665.34M (D-2, +$20.34M).
  - FLAG-1 (D-3) GROUNDED = NOT REAL (51c87173f): roster.value==aum_daily.closing_equity (4/5 core EXACT,
    LTC -$1.87M pure date-drift); monolith already ties served -- the "+$4.1M enumeration gap" was roster
    day-to-day volatility, not under-enumeration. CTO accepted + corrected Andrew's D-3.
  - FLAG-2 (account_count history) GROUNDED = REAL daily-snapshots (9ab28a43a/ca698c55f): all-integer
    irregular step-changes (INT 269 distinct/311 changes; LTC 388/391), NOT interpolated -> None would be a
    REGRESSION -> PRESERVE (CTO-approved 225137Z; import served-real + roster-daily forward; wire at cutover
    with a seam-continuity check; folded into cutover co-sign).
  - FLAG-3 (band) DONE = per-quarter segmented ledger + latest-tie (above).

## MCP traffic
~30+ messages, all base CTO (gate) + 0.2.0_DT_PortfolioAnalytics (parity harness) + 0.7.0_AE_CloudOps
(publisher). Significant: Andrew D1=SERVE-REAL ruling (via CTO); CTO GO on AE publisher apply; AE published
3/9 keys byte-identical; DT parity 3/3 (global finding -> fixed -> clean); CTO rulings on the 3 flags +
FLAG-2 PRESERVE approval; FLAG-1 grounding accepted (corrected a number CTO gave Andrew).

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| safe-commit (surface-check + risk-reflex) | 10 commits | PASS | no critical surface; reflex clean each |
| commit-gate | every .py edit | PASS | py_compile + ds-precommit + ruff |
| comp-system gate | 3 doc commits | OVERRIDE | audited system-current-override (ledger deliverables, no infra/pipeline state change) |
Grounding (FLAG-1/2 provenance, custody-basis, inflection ties) via boto3 silver/served data-plane reads
(off-rail per Rule 21 data-plane carve-out) -- no rich comp-tool fits parquet/served-JSON provenance reads.
The two data-plane groundings each caught a wrong number before it reached the page. Gap: none new.

## Files Modified
See commit messages: **ceab29600** (--upload wiring), **99fdd755a** (global display fix), **2b57be0b0/43f989647/
51c87173f/70a1d077c/e3b9772f9/9ab28a43a/ca698c55f** (named-delta ledger md+JSON evolution + FLAG resolutions),
**aa90d97dc/1d2b676a5** (TO-1 49F serve-real history + FLAG-2). Files: data/mdpf/scripts/gold/dim_mdpf_*.py +
mdpf_revamp_model_crosswalk.py + the two ledger deliverables.

## Blockers
None. Every decision resolved: D1=serve-real ruled; all 3 flags grounded + dispositioned (D-3 out, count
preserve, band segmented). account_count preserve-import + seam-check are CUTOVER-time (co-sign), not blockers.

## Current State
- **TO-1** `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` (`--firm all`): 49F serve-real
  history LANDED (aa90d97dc @9ab28a43a) -- real aum_daily model series, full-envelope custody latest,
  core D4 zero-pad, SMA 38-day depth, account_count=latest+placeholder-None (PRESERVE at cutover).
  inflection/global still latest-only skeleton (history TBD).
- **TO-3** `dim_mdpf_account_distribution.py`: all 3 firms parity-final + LIVE (published byte-identical to
  portal/model-portfolios/{49financial,inflection}/ + portal/portfolios/global/account_distribution.json,
  3/9 cutover keys). `--upload` gold/mdpf_revamp/{firm}/ wired.
- **Ledger** `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/MDPF_REVAMP_named_delta_ledger.json` (+ .md,
  ca698c55f): complete tight instrument -- 7 per-quarter history_windows + post_convergence + custody +
  model_latest_tie; DT consumer verified.
- **AE:** publisher opal-assets-mdpf-portal-publisher v0.30.0 live (role opal-assets-mdpf-portal-publisher-role,
  22a-fenced writes portal/* only). **DT:** harness mdpf_parity_check.py (@edd69fefe) reads my ledger format.

## Next Steps
- **[me / 0.4.0_DS_ClientPlatform]** PURE BUILD (no open Qs): 49F custody daily-history (schwab fact_rps_s2
  back to 2024-05-24, 538 partitions); inflection/global serve-real history; TO-4 (non_model_assets 455-day),
  TO-2 (aum-metrics/timeseries), TO-5 (vintage from DDB). Then stage all 3 firms' aggregate_aua_timeseries.
- **[me + 0.7.0_AE_CloudOps + 0.2.0_DT_PortfolioAnalytics]** stage aggregate history -> AE publish -> DT widened
  history parity (per-quarter ledger) -> N=3 same-cycle.
- **[1.0.0_SA_CTO + Andrew]** cutover co-sign package (incl. account_count PRESERVE + seam-verify); D-1/D-2 are
  the only named deltas.
- Reachable, event-driven (Monitor b2f21yxyb). No crons.
