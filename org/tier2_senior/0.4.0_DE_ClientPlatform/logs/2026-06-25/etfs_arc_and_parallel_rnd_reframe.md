# ETFS presentation arc (scope -> fact-check -> brand -> averaging) + parallel-R&D reframe

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, COORDINATE
**Serial:** 0.4.0_DE_ClientPlatform | **Date:** 2026-06-25 | **Window:** 16:33Z -> 20:40Z (since the D->A lineage log 9efb869d5)

## Summary
Two threads. (1) Closed the FE-migration scaffold + reconciled the DATA_ANALYTICS docs to Andrew's PARALLEL-R&D reset
(canonize-gold coexists with BD; no excise/cutover/lock). (2) Drove the whole HOT Andrew-direct ETFS presentation arc:
scope -> daily report (CTO-blessed, deployed by 0.5.0) -> the canonical-output+charts design -> month-end SHAPE renderer ->
a source-grounded FACT-CHECK that found a real pipeline bug (inf reading raw shared-Orion holdings) -> Opal-brand redesign ->
the full-calendar-month averaging-methodology fix. Plus the COT-staleness CVO finding + the ETFS_CANON Dynamo coming live.

## Current State (handoff surface)
- **ETFS month-end renderer** `data/etfs/scripts/presentation/render_month_end.py` (@ f774f1810 chain) -- self-contained HTML "deck", 5 slides (marquis / summary / charts / per-client-ETF / daily register), on Andrew's Desktop (`ETFS_month_end_2026-05.html` + `_2026-06.html`). Features folded this window: Opal-brand (Lato + Navy/Cool-Grey/Electric-Purple, real inlined `portal/public/logos/opal-logo-white.svg`, navy hero marquis), inline-SVG charts with **carry-forward** (no weekend/batch sawtooth), **lookback bounded** to ETFS program-start 05-01 (was over-reaching to 2019), `--inf-canonical-preview` (sources inf from `gold/canonical/holdings` pending backfill; prod default etfs-only/firm-sep), and the **full-calendar-month average**. Playwright-QA'd.
- **THE FACT-CHECK FINDING (Andrew-direct, source-verified):** the Inflection ETFS producer read RAW `opal-data-inf/gold/holdings` ($377.6M = full SHARED Orion accounts, ~50% non-Inflection) instead of `gold/canonical/holdings` ($202.3M = the portal's true book). True Opal-ETF = **$42.2M = 20.8%** (ties exact to `account_performance.total_aua` + `partner_analytics.views.aua.current.metrics.aua`), NOT the $83.3M/70% it showed. Reverse-engineered from PartnerAnalytics per Andrew's steer. Methodology banked: `data/etfs/ETFS_ARCHITECTURE_AND_MECHANISMS.md` (§2 canonical-holdings scoping + per-partner source-of-truth + total-book tie-out gate). 0.5.0 REPOINTED inf -> canonical + backfilled (served now $552.56M / inf $42.16M).
- **AVERAGING METHODOLOGY (Andrew-ruled):** "always full calendar month, because we bill monthly." Implemented in `render_month_end.py::_carry_forward_avg` -- denominator = every calendar day (MTD for in-progress); days before a partner's first holding = $0; carry-forward within held period; all partners. Validated against a per-day register: inf May avg **$7.49M** (current $12.13M > avg), COT Jun **$496K** (7 pre-onboard zeros). Banked `ETFS_ARCHITECTURE_AND_MECHANISMS.md` §2b. SUPERSEDES AVGCAP's PARTNER_CLOCKS in-window method -> flagged 0.5.0/DS to change `avgcap_monthly_average.py`.
- **ETFS daily report** `data/etfs/scripts/presentation/etf_ownership_dashboard.py` -- CTO-blessed served-path (producer-artifact `platinum/etf_ownership_dashboard.json` + lightweight push, ASTN pattern), CANONICAL_PARTNERS firm-sep allowlist, 0.5.0's date-key guard folded. 0.5.0 deployed it; CVO firm-sep-certed; live.
- **ETFS_CANON:** CTO design-gate GO (Dynamo+fan-in, full-month avg, internal-only). 0.5.0's `opal-etfs-ownership-daily` DynamoDB LIVE (356 canonical rows, my v0.1 schema + GSIs). Production monthly producer `etf_ownership_monthly.py` (DE, unbuilt) unblocked -- builds on shape-lock, queries Dynamo, full-month-avg + calendar-pad ($0 before first row, carry-forward after).
- **Parallel-R&D reframe:** all 6 DATA_ANALYTICS docs (unified contract / arch-gate brief / pre-scope / scaffold / convergence / D->A lineage) reconciled to "PARALLEL R&D, no excise/cutover/lock" (@ 139417849); BD + served $1.83B untouched. FE-migration scaffold @ eeff72f7d.
- **COT staleness:** validated (etfs/source/served all at 06-22, 2 days behind 49F/inf; 06-23 partial) -> written to CVO as a pipeline-wide (not ETFS) finding, COTETL-freeze hypothesis flagged for grounding.

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| `pipescript advi-inf` | PartnerAnalytics producer thread | PASS | traced the true-AUA source (partner_analytics -> account_performance) for the fact-check |
| `comp-glob` | `*etfs*` / brand assets | PASS | located ETFS scripts/PRDs + the brand pdf/logo package |
| `comp-platinum reverse` / `comp-pipescript io` | (carried from prior window) | PASS | underpins the canonical-holdings doc |
| `ds-commit-gate` | every `.py` edit (render_month_end, etf_ownership_dashboard) | PASS | py_compile + ruff py39 clean each commit |
| pandas/aws source-trace | gold/holdings vs gold/canonical/holdings vs account_performance | PASS (operational) | the decisive fact-check grounding (raw $377.6M vs canonical $202.3M; per-day register) -- operational data-plane reads, off-rail by design |

**What worked:** pipescript advi-inf pointed straight at PartnerAnalytics->account_performance, which cracked the $202.3M canonical-vs-$377.6M-raw discrepancy; the per-day register validated the averaging end-to-end. **What failed:** matplotlib absent -> pivoted to inline-SVG charts (no-dep, self-contained). **Gap:** comp-platinum reverse is BD-index-only (noted prior); the canonical-holdings scoping (raw-vs-canonical per shared-Orion accounts) is not a comp-tool yet -- a candidate (ETFS producers + any AUA% would benefit).

## Blockers
None. All remainders event-gated: 0.5.0/DS adopt full-month AVGCAP + build the production monthly producer interface; CVO grounds the COT-staleness mechanism; Andrew's next shape feedback on the Desktop renders.

## Next Steps
- **[0.5.0_AE_OpalETL / 0.4.0_DS]** change `avgcap_monthly_average.py` to full-calendar-month (drop PARTNER_CLOCKS); the canonical `monthly/*.json` + ETFS_CANON marquis depend on it.
- **[3.0.0_SA_CVO]** ground the COT pipeline-staleness mechanism (COTETL CurrentDay freeze hypothesis) + route the un-freeze.
- **[Andrew]** review the Desktop May/June renders (brand+logo+carry-forward+full-month-avg+canonical); direct next refinement or GO the production producer.
- **[0.4.0_DE]** on shape-lock: build `etf_ownership_monthly.py` (reads 0.5.0's Dynamo -> canonical monthly artifact, full-month avg) + the deck-gen branded deck. Port `_carry_forward_avg` + the brand CSS.
