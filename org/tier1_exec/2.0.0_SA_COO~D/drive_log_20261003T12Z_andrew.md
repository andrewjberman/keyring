# Drive log -- 2.0.0_SA_COO~D, 2026-10-03 12Z (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 11:4xZ-12:1xZ | DSGN_REBRND (FAST; IR lines still blocked: P-3/P-6 wait ~P's P-2 window, Case A waits ~Y) | round 3 E3, row W3-S4 | /positioning says a failed Models load: portal `b0b3c524` on origin DEV (ls-remote 12:11Z) | DRIVE FORWARD |
| 12:1xZ-12:4xZ | DSGN_REBRND (FAST; IR still blocked on ~P) | round 3 E3, row W3-S4 | /attribution says a failed read: portal `94c055e8` on origin DEV (ls-remote 12:47Z); the 5174 dev server restarted (stale date-fns bundle) | DRIVE FORWARD |

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

## W3-S4 on /attribution

- First render under the 401 crashed into the app-wide "Something went wrong": `Failed to fetch dynamically imported
  module .../Attribution/index.ts`. The netlog put it on `/.vite/deps/date-fns.js?v=0dfe6f92` -> 504 (Vite's outdated
  optimized dep), imported by `src/lib/periodResolution.ts`. The signed-in walker crashed the same way, so every
  session on that server was affected. A timestamp-only touch of the importer did not clear it.
- The 5174 server (PID 24388, `node scripts/dev-live.mjs --port 5174` under `bun run dev:live --port 5174`, up since
  2026-10-01 00:16) was stopped and started again with the same command, detached (bun PID 8616; logs in %TEMP%
  devlive_5174.{out,err}.log). After: the import carries `v=ca442387` and loads; the walker's /attribution draws.
- Measured from a build of DEV b0b3c524 (`--dist`, no dev server): the Style panel's skeleton never resolved, and the
  breakdown said "No holdings for this portfolio." Fix: StylePolicyComparison ERROR on a failed read; SelectionTab
  tracks the attribution read's own pending/failed state. Pin with a negative control; the build after shows both
  errors; the live walk is the positive control. The portal message's "22-row" is wrong: 18 security rows.

## Still open on W3-S4

- /advisor-intelligence, /portfolio-management, /ticket-center, /data-refresh (not re-measured). /attribution LANDED
  94c055e8.
- /market: a missing period change read as 0; RSIModal's own 50 defaults.
