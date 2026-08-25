# BRIEFING for `0.2.0_DT_PortfolioAnalytics` -- AGG view removal + toggle-persistence pattern

**From:** `1.0.0_SA_CTO~X`
**Date:** 2026-08-24
**Commits:** portal `d53049a0` (branch DEV) + workspace `c59ccf4667` (branch CLOUD, gitlink bump)
**Push state:** BOTH **LOCAL**. Integrator-only push (LD-0367) -- neither is on a remote yet.
**Asked of you (Andrew-direct):** cursory lint-check / review, then the DEV -> PROD promote if it looks good.

---

## 1. WHAT ANDREW ASKED FOR, AND WHY

He asked where the "Agg" view's weights on Positioning came from, with a specific worry, verbatim:

> "what my concern is here is that the 'Agg' view is somehow tied to Opal's aggregate models somehow as
> opposed to the Advisor's aggregate Opal Model exposure, which would be a problem."

**He was right.** Then, verbatim:

> "I think the easier solution here is simply just pulling 'Agg' toggle view from those three pages
> ('Positioning' 'Attribution' and 'Factor Tilts') nobody cares about this view and its more trouble than
> its worth."

> "Also we want to get that subtle local/client-side browser cache mechanism with the toggles set up in
> Positioning (and define this mechanism as a pattern because we may want to implement it elsewhere in the
> Portal on key toggles)."

Full investigation record with every citation:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260824_PULL_AGG_VIEW_THREE_PAGES_AND_TOGGLE_PERSISTENCE_PATTERN.md`

## 2. THE FINDING IN ONE PARAGRAPH

The AGG rollup weighted each model by `model_aum / total_aum`, sourced from
`json/portfolios/aum-metrics.json` `by_model[].aum`
(`yang-generate-positioning/lambda_function.py:1193-1218` @`69b867c4eb`). That artifact is Opal's entire
book **pooled across three partner firms** -- `total.aum` $1,951,676,164.42 / 7,854 accounts, and its own
`meta.fee_basis_components` splits it exactly three ways (49financial $1.689B / inflection $138.0M /
cottonwood $124.4M). A token census over the whole file returns `advisor`=0, `rep_code`=0, `household`=0,
`tenant`=0: **there is no advisor dimension in the weighting at all.** Measured on the served
`positioning_data.json`, the implied weights were UST 3.20 / ST 7.89 / INT 27.14 / **LT 49.15** / ULT 12.62
pct -- so an advisor whose book was entirely Short-Term saw an "Aggregate" that was 49% Long-Term
Conservative. It was never a display bug; it was a correct answer to a question nobody on those pages was
asking.

## 3. WHAT CHANGED, FILE BY FILE

15 files, +413 / -746. It is mostly deletion.

**New -- the pattern (this is the piece worth your attention):**
- `src/hooks/usePersistentToggle.ts` -- sessionStorage-backed toggle state. Heavily commented on purpose:
  it is meant to be the ONE mechanism if we do this elsewhere.
- `src/hooks/useFilterTracking.ts` -- `useSelectTracking` gains an optional `persist` arg so any existing
  tracked toggle opts in with one argument. Existing call sites are unchanged in behaviour.

**Positioning:**
- `shared/bookSet.ts` -- `aggregate` capability removed from `BookSetCapabilities`; adds
  `SUMMARY_VIEW_MODES` / `HOLDINGS_VIEW_MODES` (the allowed sets the persistence validates against).
  Carries the long WHY comment -- if anyone ever wants an aggregate back, that comment is the thing to read.
- `tabs/HoldingsTab.tsx` -- the bulk of the deletion: AGG selector entry, the AGG-only MODEL BREAKDOWN
  column group (4 JSX blocks + colgroup + header), `aggregateWeighting`, the `aumByModel` state and its
  fetch, and two dead AGG builders. Adds the first-render landing rule (see s.5) and book persistence.
- `Positioning.tsx`, `panels/PositioningSummary.tsx` -- toggles wired to the pattern.
- `README.md` -- correction header (see s.6).

**Attribution:**
- `constants/holdings-shared.tsx` -- AGG dropped from the shared `PORTFOLIOS` list. This is what removes it
  from all three consumers (`SelectionTab`, `AssetAllocationSummary`, `StylePolicyComparison`).
- `tabs/SelectionTab.tsx` -- two live client-side AGG builders + the AUM fetch removed; a now-redundant
  `.filter(p => p.id !== 'AGG')` collapsed.

**FactorTilts:**
- `constants.ts` -- `computeAggregateMetrics` removed entirely; AGG dropped from `AVAILABLE_PORTFOLIOS`;
  the AGG branch in the radar builder removed.
- `FactorTilts.tsx` -- the AUM fetch that fed it removed (the `Promise.all` collapses to a single fetch);
  default scope **AGG -> INT**; a defensive filter drops an AGG row if a producer ever emits one.
- `types.ts` -- `'AGG'` off `PortfolioId`; `priceWeighted*` fields removed.
- `panels/SummaryMetricsTable.tsx` -- AGG scope filter, the AGG-only "Show All Models" toggle, and the
  price-weighted arm removed.
- `panels/FactorTiltOverviewPanel.tsx` -- AGG branch + the AGG-only methodology footnote removed.
- `index.ts` -- one barrel export line.

## 4. WHAT I DELIBERATELY DID **NOT** TOUCH -- please sanity-check me on these

1. **The producer's served `current_holdings.AGG`.** Andrew said pull the toggle VIEW. Removing served
   output is a separate act under NEVER#3. The key is still served and still correct; nothing in the portal
   reads it now.
2. **The `AGG` ETF ticker** -- iShares Core U.S. Aggregate Bond. Same three letters, completely different
   thing, and it is live throughout benchmark composition (`lambda_function.py:157/170/596/1009`,
   `BenchmarkHeatmap.tsx`, `Attribution/constants/etf-categories.ts:36`). **A string-matched removal here
   breaks benchmarks.** I made the view-vs-ticker call per call site rather than by grep. If you review one
   thing, review this.
3. **The `FactorKey` names `'Agg vs Short'` and `'HY vs Agg'`** -- Bloomberg Aggregate factor names, not the
   view. Untouched, and visible working in the Factor Tilts screenshot.
4. **AGG on pages Andrew did not name** -- `TradeSubmission/tabs/HistoryTab.tsx`, `ModelPortfolios.tsx`,
   market-performance, Macroeconomics. Out of scope.

## 5. THE REGRESSION I INTRODUCED AND CAUGHT -- worth knowing before you review

Removing AGG removed an **accidental** behaviour. The initial state was
`useState(caps.aggregate ? 'AGG' : '')`, which handed Models mode a selected book on mount purely as a side
effect of AGG existing. With AGG gone it initialised to `''`, and in Models mode the edge that would pick a
default never fires (`bookStatus` is ETF-only, so its key never changes). **The page mounted with no book
selected and rendered "No holdings data available" over perfectly good data.**

**`tsc -b` and `eslint` both passed clean on that.** It was caught only by rendering the page and reading
the screenshot -- which is exactly what `portal/CLAUDE.md`'s verification law exists for. It is now an
explicit first-render landing rule in `HoldingsTab.tsx` with a comment saying why, rather than an emergent
property of a default value.

## 6. VERIFICATION ALREADY RUN (re-run whatever you want; do not take my word)

- **`bun run typecheck`** (= `tsc -b --noEmit`) clean. **I ran the mutant control first** -- injected a
  deliberate type error, confirmed it FAILED (TS2322), then removed it -- so the clean pass discriminates.
  Per portal CLAUDE.md, a bare `tsc --noEmit` here compiles an empty file set and proves nothing.
- **`bun run lint`** -- 0 errors. 3 warnings remain repo-wide: one pre-existing memoization warning and two
  in `AdvisorIntelligence/_shared/perfrp/PerfrpControls.tsx`, **a file this change never touched** (another
  seat is working in the tree). All 14 touched files lint individually clean.
- **`bun run build`** succeeds.
- **All three pages rendered headless and READ**, against fixtures built from the **live served artifacts**
  (I pulled `positioning_data.json`, `factor-tilts/tier1-snapshot.json`, `holdings_attribution_data.json`
  and `allocation_summary.json` from S3 -- note they are gzip-encoded on the wire). Confirmed: no Aggregate
  in any selector, Positioning holdings render with weights summing to 100.00, no MODEL BREAKDOWN column
  group, Factor Tilts defaults to Intermediate-Term with the Agg-named FACTORS intact, Attribution renders
  full attribution with totals. Colour law checked on each -- content is inside dark Panels, canvas text is
  dark.
- **Persistence exercised in a real browser, both directions:** select LT -> reload -> LT restored; then a
  negative control with storage hand-set to `"NOT_A_BOOK"` -> discarded, falls back to UST, bad key cleared.
  (My first probe reported a false FAIL because it read `className` when active state is an inline `style` --
  the probe was wrong, not the feature. Flagging it so you do not repeat it if you write your own.)

## 7. PROMOTE

Normal `/prod-deploy` (DT lane). Portal main tree is on DEV and stayed there throughout. Two notes:

- Both commits are **LOCAL**. The portal DEV push and the PROD push are integrator-only per LD-0367 --
  route them to MSTR rather than pushing from your seat, unless your standing posture says otherwise.
- The workspace gitlink bump `c59ccf4667` is already made (`9580e18b8f -> d53049a0d0`), so you should not
  need to mint another pointer commit unless portal DEV moves again before your promote.

## 8. TWO THINGS SURFACED, NOT CHASED (not blocking; routing is not mine to decide)

1. **`safe-commit.sh` has a broken post-commit verify helper.** Both of my commits printed a python
   `SyntaxError: unterminated string literal` AFTER the `[msg-verify]` line. The commits and the
   msg-verify itself succeeded, so it is cosmetic today -- but it is a verification step that is not
   running, and it fails in a way that reads like noise.
2. **The AGG denominator was silently truncating.** `aum-metrics.json` carries **7** models; the producer's
   name->code map covers **5**. `Opal Blend 5050 Int Ltc` ($32.1M / 155 accounts) and `Opal Blend 5050 St
   Int` ($7.3M / 24 accounts) mapped to nothing and dropped out of both numerator and denominator, while
   the survivors still normalised to exactly 1.0 -- invisible on screen. Moot for these three pages now,
   but **the same map and the same artifact feed other consumers**, so it is worth someone's eyes.
