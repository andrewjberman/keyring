# Positioning Summary — Freeze the allocation-bars container as a pane (Andrew-direct)
**archetype:** IMPLEMENT

**Portal DEV commit:** `3b516623`
**Workspace CLOUD commit:** (this log)

## Ask (Andrew-direct, ad-hoc)
On the Positioning page, freeze the initial content container of the "Positioning Summary"
panel — the stacked allocation bars for the 5 models — as a **pane**, so that when the user
clicks **Expand Details** and explores the detail charts (Asset Class, Management Style,
Characteristics, Asset Sub-Categories), the bars container **stays in place**.

Clarified the freeze mechanism with Andrew (two viable readings). Andrew chose **Option 1 —
freeze-pane inside the panel**: bars + portfolio name-headers pinned at the top of the panel;
the detail matrix scrolls in a bounded region beneath (Excel-style frozen panes), fully
self-contained in the panel (vs. Option 2, sticky-to-viewport / page-level scroll).

## Change
`portal/src/pages/Positioning/panels/PositioningSummary.tsx` only.

The allocation-bars grid + the portfolio name-header row already sit **above** the detail
matrix in document flow. So the freeze needs no `position: sticky` / flex-column hacks — I
wrapped **only the matrix grid** in a bounded, vertically-scrollable box:

```
<div className="overflow-y-auto overflow-x-hidden" style={{ maxHeight: 'clamp(300px, 48vh, 600px)' }}>
  <div className="grid w-full" style={{ gridTemplateColumns: PORTFOLIO_GRID_TEMPLATE, width:'100%' }}>
    {renderContent()}
  </div>
</div>
```

The bars + name-headers, being outside that scroll box, stay put while the matrix scrolls.

**Why the columns stay aligned:** the scroll box shares `PORTFOLIO_GRID_TEMPLATE`
(`300px repeat(5, minmax(min-content,1fr))`) with the frozen bars/headers, and both regions
live inside the single outer `overflow-x-auto` wrapper — so any horizontal scroll (narrow
screens) moves both together. `overflow-x-hidden` on the scroll box prevents it from spawning
its own independent horizontal scrollbar, which would desync it from the frozen header.

**Scrollbar affordance:** left the box WITHOUT `scrollbar-none`, so it inherits the global
auto-hide / hover-reveal (`--primary`) scrollbar — consistent with the rest of the app and
signals the matrix is scrollable.

**maxHeight** `clamp(300px, 48vh, 600px)` is viewport-responsive (works on laptops and the
large-screen scaling path); trivially tunable if Andrew wants a taller/shorter window.

Collapsed view (bars + Expand button only) is **unchanged**.

## Verify
- `tsc -b --noEmit` (portal): **PASS** (exit 0).
- `eslint src/pages/Positioning/panels/PositioningSummary.tsx`: **PASS** (exit 0; only a benign
  baseline-browser-mapping staleness notice).
- **Live pixel-eyeball: BLOCKED for me** — local dev server (:5175) redirects `/positioning`
  to `/login`; portal is auth-gated and I have no login creds (standing env limit, see
  2026-06-26 logs). Pure-layout change, low risk; the freeze-pane behavior wants a visual
  confirm on the authed page → operator/Andrew, or DT via authed browser at promote time.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| (none applicable) | — | Pure CSS/layout wrapper on an existing panel — no data props, no new cohort/metric/mode, no deletion. `comp-transform schema-check` (the DE minimum for data-prop changes) is N/A; these recharts/grid presentational comps are also not in the comp-transform registry (GAP already logged 2026-06-26). Mechanical gates = tsc + eslint (both PASS). |

## Files Modified
| File | Change | Committed |
|------|--------|-----------|
| portal/src/pages/Positioning/panels/PositioningSummary.tsx | Wrap detail matrix in bounded overflow-y-auto box (freeze bars/headers as a pane) + docstring | Yes — DEV `3b516623` |

## Current State
Committed to portal **DEV `3b516623`**, mechanically verified. Not yet pushed/promoted (DE
cannot push — DT is the QA/deploy gate). Not a structural change → `pod_inventory.xml` untouched.

## Next Steps
- [0.2.0_DT_PortfolioAnalytics] Push DEV + (on Andrew's GO) promote DEV→PROD via `/prod-deploy`;
  the change is FE-only, no backend/Lambda touch.
- [Andrew/operator] Pixel-eyeball the freeze pane on the authed Positioning page: click
  **Expand Details**, confirm the bars + model-name headers stay pinned while the detail
  matrix scrolls beneath. Confirm the maxHeight window feels right (tunable).

## Blockers
None. Pixel-eyeball residual is a credential/auth-wall limit (handed to operator/DT), not a
correctness gap — functional change is mechanically verified.
