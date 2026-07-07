# MKOV_RETFIX TO-1 -- IndexPerformanceModal: served-TR source + annualize + data-date anchor + trailing-period cap

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

**Serial:** 0.1.0_DE_MarketIntelligence
**Date:** 2026-07-07 (window: session start ~1620Z -> ~1728Z; prior log 2026-06-16)
**TO:** MKOV_RETFIX.TO-1 (COO 2.0.0_SA_COO; Andrew-direct P0, advisory-board-visible; PRD docs/architecture/MKOV_RETFIX_PRD.md SS6 TO-1)

## Summary

Wayne Wicker (advisory board) fact-checked the Market Overview 3Y index returns vs Bloomberg; all four read "low." Root cause (per DS 0.2.0 brief + PRD): `IndexPerformanceModal.tsx` computed its return stat from a PRICE diff (`(last.price-first.price)/first.price`) off the price series = price return, ex-dividend -> 1.4-2.8pt low vs total return; plus cumulative-not-annualized for 3Y and a today-anchored window (the "2.97y not 3.0y" drift). Fixed the modal to read the already-served TOTAL-return `period_returns`, annualize multi-year, anchor to the data date, and (req 4, added mid-session as Andrew's GO condition) cap trailing periods that lack full history. Shipped to PROD.

## Work done

Frontend-only, scope = `portal/src/components/market-performance/IndexPerformanceModal.tsx` (Pod 1 / MarketIntelligence). Built on portal DEV, two commits:

**7a58a54d -- items 1-3** (`portal/src/components/market-performance/IndexPerformanceModal.tsx`):
- Return stat now reads served `period_returns[key]` (total return) instead of diffing price. Sourced via `getAllReturns()` (summary/all-returns.json -- the fresh, Bloomberg-validated artifact the heatmap uses), NOT `details/{ticker}.json` (found STALE, see Findings).
- Toggle->served-key map (matches generator PERIOD_CALENDAR_DAYS): 30D->1M, 90D->1Q, 1Y->1Y, 3Y->3Y.
- Multi-year annualized: `(1+cum)^(365.25/calendarDays)-1`; label "3Y Return (annualized)". 1Y and shorter shown as period return.
- Chart window anchored to latest DATA date (`historicalPrices[last].date - days`) not `new Date()`. Chart price LINE UNCHANGED (req 5 non-negotiable -- protects RSI/regime).

**df9323de -- req 4 (trailing-period cap)** (same file):
- The generator's `calculate_period_return` (lambda_function.py:123-124) returns None ONLY when zero obs fall in the window -- it does NOT null-out insufficient history -- so a ticker with < the requested period silently gets a truncated "3Y" that would be mis-annualized with the full 1095d exponent.
- Modal now verifies the ticker's own `historical_prices` span >= 95% of the requested period; if materially short, caps to "N/A -- X.Xy history" instead of presenting/annualizing a truncated window. Never extrapolates.

## Verification (RAVC, PROD-confirmed)

**Before/after (3Y annualized), grounded on served all-returns.json (as_of 2026-06-30) + each ticker's timeseries:**
| Index | BEFORE (cum price-diff) | AFTER (served TR ann) | Bloomberg |
|---|---|---|---|
| S&P 500 | 70.07% | 20.60% | 20.4 |
| Russell 2000 | 59.58% | 18.64% | 18.3 |
| MSCI EAFE | 49.08% | 17.17% | 16.3 (gross-vs-net, out of scope PRD SS1.6) |
| Bloomberg Agg | 14.09% | 4.16% | 4.1 |

AFTER == served heatmap card to the bp (fix makes modal agree with card). 1Y (price-diff->served TR): S&P 20.38->22.29, R2K 36.59->40.91, EAFE 17.77->20.94, Agg 4.52->3.79.

**req-4 cap verified latent** -- no current ticker <95% of its period: equities span 1532-1595d, BTC/ETH 1094d (all >= 95% of 1095d 3Y). So zero visible change today; pure guard for future short-history tickers.

**PROD deploy (DT 0.1.0_DT promoted; I independently verified, not self-report):**
- origin/PROD = f3ce600c (`git show origin/PROD:...IndexPerformanceModal.tsx` = my code); tag portal-v2.1.132 peels to f3ce600c; CI run 28884926281 = SUCCESS via `gh run view`; CLOUD submodule bumped df9323de (e2004a5a4).
- SERVED live: PROD d2n2nzpeqf34ge.cloudfront.net route chunk `index-2uAKXBJz.js` contains my exact minified logic (`.partialYears.toFixed(1)}y history` + `ys*.95)return{value:null,annualized:S.annualize`). Deployed bundle IS my code, not merely CI-green.
- EXERCISED (visual authed render): deferred to 0.2.0_DS (I lack portal auth); numbers handed over.

## Compiler Tools

| Tool + command | Result | Note |
|---|---|---|
| `comp-transform schema-check IndexPerformanceModal` | NOT-FOUND ("Component not found") | Expected per PRD SS5.2 (known COMPONENT-graph coverage gap for market-performance). Compensated via direct served-artifact + generator source read. |
| `comp-cache collisions` | PASS -- no NEW key | Change adds no React Query key (raw getAllReturns/getTickerTimeSeries via useState). Only pre-existing advisor-intelligence/firm-leaderboard collisions, unrelated. |
| `git -C portal log` / `gh run view 28884926281` | promote + CI verified | Independent PROD confirmation. |

- **What worked:** grounding the fix on the SERVED all-returns.json (not the TS types) caught that the transform drops 3Y/5Y and that details/ is stale; grounding on the generator source answered COO's "does reading period_returns implicitly cap?" definitively (no).
- **What failed / gap:** comp-transform/comp-blast dead-end on IndexPerformanceModal (COMPONENT node set doesn't cover market-performance) -- flagged for graph-coverage backlog (also noted in PRD SS5.3).
- Rail: raw `curl` to the live PROD CDN bundle used with inline `# rail-checked:` markers (served-state verification -- no comp-tool inspects a deployed CDN bundle).

## Findings (routed, non-blocking)

- **(A) details/{ticker}.json tier is STALE** -- Jan-2026 vintage (latest_date 2026-01-09, generated 2026-01-13); its period_returns disagree with the fresh summary (S&P 3Y 0.866 vs 0.7536). PRD IO-contract listed summary/details as interchangeable -- they are NOT. Sourced from summary. Routed to COO + DS (the details generator likely isn't scheduled).
- **(B) residual-bps (S&P +0.2, R2K +0.34, Agg +0.06 vs Bloomberg)** = the pre-existing pipeline-vs-Bloomberg methodology gap owned by DS's TO-2 -- NOT introduced by my fix (my AFTER == served card exactly).

## MCP traffic

~14 messages handled. Significant: COO GO (deploy) -> my RAVC -> DT-spawn/stand-down cross -> DT LIVE+HOLDING -> DS/COO added req-4 (Andrew GO condition) -> Andrew-direct promote GO -> DT pre-flight CAUGHT uncommitted req-4 and HELD (correct) -> I committed df9323de -> DT promoted f3ce600c -> PROD-confirmed RAVC to COO + eyeball handoff to DS. Andrew-direct: batching + he instantiates DT at deploy time.

## Current State

- **PROD LIVE:** portal-v2.1.132 = f3ce600c (whole-head: df9323de[mine] + f07b0b25[AE advisor-intel docs] + 4d646417[ClientPlatform NNA]). CLOUD submodule = df9323de.
- **Modal behavior now:** return stat = served total-return period_returns; 3Y labeled "(annualized)" ~20.6% (S&P); 30D->1M, 90D->1Q, 1Y->1Y; window anchored to data date; chart price line unchanged; short-history tickers cap to "N/A -- X.Xy history" (latent, none today).
- **Portal main tree:** on DEV (df9323de), clean. Workspace root anchored.

## Next Steps

- [0.2.0_DS_PortfolioAnalytics] Post-push served-parity VISUAL eyeball on live PROD modal (expected numbers sent); + disposition finding (A) stale details tier; + TO-2 residual-bps reconciliation.
- [2.0.0_SA_COO] Close TO-1 on DS's visual-eyeball confirmation (code+data+deploy already RAVC-verified PROD-live).
- [0.1.0_DE_MarketIntelligence] Event-driven; Andrew signaled "a couple more changes coming" for this P0 -- stack any on DEV, hold batch promote-ready for Andrew's DT instantiation.
