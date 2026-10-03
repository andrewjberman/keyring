# Drive log -- 2.0.0_SA_COO~D, 2026-10-03 12Z (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 11:4xZ-12:1xZ | DSGN_REBRND (FAST; IR lines still blocked: P-3/P-6 wait ~P's P-2 window, Case A waits ~Y) | round 3 E3, row W3-S4 | /positioning says a failed Models load: portal `b0b3c524` on origin DEV (ls-remote 12:11Z) | DRIVE FORWARD |

## W3-S4 on /positioning

- Re-measured on DEV 564a8f95 (ui-smoke, auth stubbed, data answered 401): the Summary drew its legend beside an empty
  grid with nothing said; Composition and Holdings both read "No holdings for INT.".
- Causes: the page's Models query discarded `isError`; the Summary ignored its `isLoading` prop and had no failure
  input; HoldingsTab's own Models fetch caught the failure and only stopped the spinner.
- Fix: `loadFailed` from the page (Models only; ETFs and Satellites already say it once in the page notice); the
  Summary shows LOADING / ERROR when it has nothing to draw; HoldingsTab records the failure and each panel says its own
  sentence.
- Pin `Positioning/panels/summary-states.test.tsx` (negative control on HEAD). HoldingsTab's branch is set by a fetch
  effect, so the 401 render is its check.
- Real run: under the 401 all three panels show their error. Positive control: signed-in walk `20261003T120014Z`
  with live data draws the bars, treemap and table as before.
- Found while checking: bun's `mock.module` is process-wide. The a7b16628 market pin's React Query replacement broke a
  later file in a combined run ("Export named 'useMutation' not found"). Both pins now snapshot the real modules and
  restore them in afterAll. A throwaway probe test after them read the real api client, React Query and RSI hook. 11
  related tests in 10 files pass in one run.

## Still open on W3-S4

- /advisor-intelligence, /attribution, /portfolio-management, /ticket-center, /data-refresh (not re-measured).
- /market: a missing period change read as 0; RSIModal's own 50 defaults.
