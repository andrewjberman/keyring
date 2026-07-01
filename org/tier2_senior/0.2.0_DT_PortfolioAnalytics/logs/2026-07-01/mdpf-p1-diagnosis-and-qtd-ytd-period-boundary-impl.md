# MDPF P1 diagnosis + escalation, and QTD/YTD period-boundary implementation
**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT

**Agent:** 0.2.0_DT_PortfolioAnalytics
**Date:** 2026-07-01
**Window:** since my prior log (model_portfolio_timeseries served-verify, 44ac711cf) -> now. Two Andrew-direct asks.

## Summary

Andrew-direct 1: check MDPF (global/49F/inflection). Found + fully root-caused a P1 serving
incident (all MDPF served AUA frozen 6 days), escalated to COO/CVO/AE. Andrew-direct 2:
read the Yang QTD/YTD chat + implement my recs for the period-boundary bug class. Shipped a
shared app-wide period-resolution module + wired Attribution; discovered (and reported, not
yet fixed) a SEPARATE live Attribution regression from Andrew's cleaned-6/30 re-upload.

## Part 1 -- MDPF P1 (DIAGNOSE, escalated; not my repair lane)

SYMPTOM (comp-freshness FAIL x4): platinum/mdpf/aggregate_aua_timeseries.json + json/mdpf/{global,
49financial,inflection}/aggregate-aua-timeseries.json all frozen 2026-06-25 16:42Z (~145h, >48h fail).
Staleness alarm mdpf-daily-freshness-stale = ALARM since ~06-26 (detection fired, response didn't).

MECHANISM (grounded on runner status.json + s3://opal-data-mdpf/telemetry/mdpf-daily-runner/logs/):
- Event/gate layer HEALTHY: mdpf-daily-trigger fires daily on the INF sentinel (fresh 06-30), gate
  logic correct, EventBridge rule ENABLED. Gate PASSED + dispatched runner 06-26..06-29.
- Runner FAILS at Stage 2 WS-E (build_mdpf_wse_49f_non_model_aua.py) rc=1 EVERY day: reads
  bd/silver/allocations/{date}.parquet -> partner_custody_total (Schwab-only) = $0.00 (0 accounts)
  -> non_model_aua(49F) = $0 - model $1,381,488,891.17 - sma $23,326,571.45 = -$1.4B -> feeder's
  sanity gate hard-fails (correctly refuses to write) -> dispatch skips Stages 3/3.5/4/5 (aggregate+
  rollup+serve) -> no partition, served frozen for ALL firms (global/inflection collateral; WS-B 49F
  model $1.38B + WS-C inflection $202M compute fine -- only the 49F Schwab custody match = 0 accts).
- Compounding: bd/silver/fees frozen 06-25 (06-30 gate now also DEFERS). Root = Schwab bd/silver
  {rps,uln,rld} froze 06-24/06-25.

CVO (3.0.0) confirmed the Schwab-silver freeze is the shared upstream + is actively running
/49-schwab-conv to un-freeze (partial: 06-25 only; needs 06-26..06-30 + quartz-box cutover). Corrected
my over-link: CVO's /Advisors "no data" is a DISTINCT FE window-default bug (data present), not this.
Escalated full grounded diag to 2.0.0_SA_COO (repair-owner dispatch), cross-linked 3.0.0_SA_CVO,
FYI'd 0.5.0_AE_OpalETL (mdpf owner). Repair is DS/AE lane (BD-silver/WS-E), not my DT lane.

## Part 2 -- QTD/YTD period-boundary bug class (IMPLEMENT; Andrew-direct)

Read Yang<->Andrew chat: on the first day of a period (Jul 1 = Q3 start, data still t-1 @ 6/30), QTD/YTD
windows anchored to wall-clock "today" are EMPTY -> tabs blank. Yang: anchor to file end-date; Andrew:
auto-shift + footnote, flagged "dormant grenade" if a 1st-of-period-dated file is ever uploaded.

Recs implemented = 3 layers in ONE shared module portal/src/lib/periodResolution.ts (shape-agnostic,
serves both the ADVI windows-object model and the Attribution portfolios[pf][period] model):
- Layer 1 anchor: getPeriodToDateWindow(asOf, kind) -- windows from data as-of, not today.
- Layer 2 grenade-guard: getLastCompletedPeriodWindow -- deterministic fallback for a degenerate
  (1st-of-period-dated) window; defuses Andrew's grenade in code, not by human promise.
- Layer 3 never-blank: useEffectivePeriod/resolveEffectivePeriod -- auto-advance off a present-but-
  EMPTY selected window to the freshest POPULATED period, toggle stays honest. Generalizes DE 90322ba0.
Wired Attribution.tsx (default QTD -> auto-advance via allocation-summary availability; dedup'd query).
Covers the whole Attribution family (StylePolicyComparison + AssetAllocationSummary + SelectionTab all
inherit effectivePeriod via props -- verified). The two surfaces that actually BLANK are now both
covered: ADVI leaderboard (DE 90322ba0) + Attribution (this). Trailing-window + scalar-$0 toggles are
not vulnerable; ADVI drill-down consolidation handed to 0.4.0_DE_ClientPlatform (their lane).

DISCOVERED (separate live regression, reported to Andrew, HE owns the fix): served allocation_summary.json
= portfolios:{} (empty) since a 17:04 run clobbered a good 16:31 version. Root grounded via
yang-generate-holdings-attribution 17:03 CloudWatch: input "Model Portfolio Attribution 20260630.xlsx"
(Andrew's cleaned re-upload) has sheets [_QTD,_YTD,_1Y,_SI] but parser "Extracted 0 models" from each
(the cleaning moved the "<name> vs Benchmark" header layout the parser keys on). NOT the boundary bug;
pre-clean file parsed fine. Andrew: "I will address the attribution issue next." Fix options on record:
(A) re-upload working file, (B) I harden parse_period_sheet_horizontal, or stopgap restore 16:31 version.

## Deployment Sequence + Verification (actual output)

Portal DEV FE commit (not a Lambda deploy this window):
```
Files:      portal/src/lib/periodResolution.ts (new, 3-layer shared module)
            portal/src/pages/Attribution/Attribution.tsx (wired useEffectivePeriod)
Verify:     bun run typecheck (tsc -b --noEmit) -> exit 0
            bunx eslint <2 files>              -> exit 0 (only benign baseline-data notice)
Commit:     62cdb473 (portal DEV, author 0.2.0_DT_PortfolioAnalytics)
Push:       origin/DEV a58ff3a7..62cdb473 (pull --no-rebase merge; VALGATE D-1 PASS)
PROD:       NOT promoted (gated + DE QA); FE change is a no-op while allocation_summary is empty.
```
Served-artifact grounding: model_portfolio_timeseries.json verified earlier (44ac711cf); MDPF
freshness via comp-freshness; allocation_summary.json decompressed (gzip) -> portfolios EMPTY confirmed.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| comp-which | "MDPF freshness for global/49F/inflection" | PASS | routed to comp-freshness chain |
| pipescript | mdpf | PASS | full thread map: producers (trigger/runner/freshness-checker) -> served rollup + per-firm slices -> ModelPortfolios page; gave the exact served keys + gate-input chain |
| comp-freshness | artifact x4 (mdpf served) + chain inf + chain bd | PASS(tool) | FAIL(data) on 4 mdpf served artifacts (145h); INF sentinel + bd/silver/allocations PASS -> proved NOT an input-defer, pointed to runner-side |
| comp-freshness | artifact (INF sentinel, bd fees) | PASS | grounded gate inputs |

What worked: pipescript mdpf + comp-freshness artifact together isolated the failure to the runner
side (gate green, output frozen) in minutes -- the decisive narrowing. What failed: none. Gap:
comp-freshness `artifact` says "No cadence config entry - using default daily thresholds" for the
mdpf served keys (the known comptool_gap_mdpf_freshness gap -- served-only pipeline not in the script
map); default thresholds still gave the correct FAIL. FE typecheck/eslint via bun (no comp-tool covers TS).

## MCP traffic

~6 significant: escalation to 2.0.0_SA_COO (P1 MDPF, full diag) + cross-link 3.0.0_SA_CVO + FYI
0.5.0_AE_OpalETL; ACK to CVO (record correction, 2 distinct roots); handoff to 0.4.0_DE_ClientPlatform
(shared useEffectivePeriod + ADVI consolidation, queued for their bootup).

## Blockers

None (mine). MDPF repair is externally owned (DS/AE Schwab un-freeze via CVO/COO). Attribution-data
fix owned by Andrew. DE consolidation queued for DE bootup.

## Current State

- portal/src/lib/periodResolution.ts LIVE on DEV (62cdb473): resolveEffectivePeriod/useEffectivePeriod
  (Layer 3) + getPeriodToDateWindow/getLastCompletedPeriodWindow (Layer 1/2). Attribution.tsx wired.
  tsc/eslint clean. NOT on PROD (gated + DE QA). Blank-at-boundary bug covered app-wide (leaderboard +
  Attribution family).
- MDPF P1: served AUA frozen 06-25 for all firms; root = WS-E 49F custody=$0 from bd/silver/allocations
  (Schwab-silver freeze 06-24/25). Escalated; CVO un-freezing (partial). NOT self-healed yet.
- allocation_summary.json served EMPTY (portfolios:{}) since 17:04; root = cleaned-6/30 attribution
  Excel parses to 0 models. Andrew owns the fix.

## Next Steps

- [Andrew] fix the Attribution data (re-upload working attribution Excel OR request I harden the parser);
  then the effectivePeriod wiring also prevents future boundary-blanks.
- [0.4.0_DE_ClientPlatform] on bootup: adopt shared useEffectivePeriod (migrate AdvisorsTab dedup +
  optional scalar drill-down panels). Handoff in inbox.
- [2.0.0_SA_COO / 3.0.0_SA_CVO] drive MDPF un-freeze to COMPLETION (06-26..06-30 + quartz cutover) --
  I'm watching it doesn't stall half-done.
- [0.2.0_DT_PortfolioAnalytics] (optional, my pipeline) Layer-1 anchor in yang-generate-allocation-summary
  + yang-generate-holdings-attribution (compute QTD/YTD relative to data_as_of) -- deferred behind
  Andrew's Attribution-data fix.
