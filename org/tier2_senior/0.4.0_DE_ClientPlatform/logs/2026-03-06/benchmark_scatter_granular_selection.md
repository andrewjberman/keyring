# Benchmark Scatter Granular Selection — 0.4.0_DE_ClientPlatform

**Date:** 2026-03-06
**Portal DEV commits:** `60f1ee0` -> `0ac188c` -> `5cc598f` -> `b3f3bec` -> `adc5e4c` -> `fcaa484` -> `a1fb029` -> `a493db4` -> `312ca3d`
**Workspace CLOUD commit:** `pending`

## Objective

Add a general/granular state toggle to the Return vs Volatility scatter chart on the
ModelPortfolios Benchmark tab. Clicking a legend item enters granular state: only that
model's circle and paired benchmark diamond are visible, the chart auto-zooms around
them, and persistent tooltip cards appear on both points without hover. Clicking again
returns to general state. Clicking a different model while in granular state switches
context directly.

---

## Work Completed

### 1. Core State + Legend Interaction (`60f1ee0`)

Added `selectedModel: string | null` state. `null` = general, code string = granular.
- `filteredData` filters `scatterData` to the selected model's 2 points in granular state
- Axis domains recalculate from `filteredData` automatically — chart auto-zooms with no
  extra logic
- Model legend `<div>` items converted to `<button>` elements: toggle on same code,
  switch on different code, `opacity-30` on unselected items, white ring + bold label
  on selected item, 200ms transitions throughout

### 2. Persistent Tooltips — Iteration History

Six iterations to arrive at the correct implementation. Documented in full for future reference.

#### Attempt 1 — SVG text labels via `makeShapeRenderer` factory (`0ac188c`, `5cc598f`)
Approach: extend shape renderer to also draw SVG `<rect>` + `<text>` elements as
persistent labels when `showLabel=true`.
Issues: SVG text has no CSS wrapping control, size/content was too abbreviated, and
grid-aware placement (above/below based on return rank + axis padding) was overly
complex for what was essentially a cosmetic layer.
Reverted.

#### Attempt 2 — HTML cards below the chart (`b3f3bec`)
Approach: remove SVG labels entirely; render `<CustomTooltip active={true} ...>`
as a flex row of HTML divs below the `ResponsiveContainer`.
Issue: user wanted tooltips inside the chart adjacent to their data points, not
in a separate section below.
Reverted.

#### Attempt 3 — `Customized` component with `foreignObject` (`adc5e4c`)
Approach: use Recharts' `Customized` component (receives chart internals as props)
to render `<foreignObject>` tooltip cards at pixel positions computed from `xAxisMap`
and `yAxisMap` scales.
Issue: Recharts 3.x deprecated `Customized`. The `xAxisMap`/`yAxisMap` internal
state it relied on no longer exists in v3 — early-return guard always fired, nothing
rendered.

#### Attempt 4 — Recharts 3.x public hooks (`fcaa484`)
Approach: replace `Customized` with a `GranularTooltips` component (direct chart
child) using `useXAxisDomain(0)`, `useYAxisDomain(0)`, `usePlotArea()` — all public
v3 exports. Construct linear scales manually from domain + plot area to compute exact
pixel positions. Render `<foreignObject>` + `<CustomTooltip>`.
Issues: (a) `TH=128` too small — tooltip HTML was ~136px for long model names,
foreignObject clips at declared height. (b) bottom clamp used `plotBottom` (plot area
edge) not `chartHeight` (full SVG height), over-restricting vertical range.

#### Attempt 5 — Fix bottom clip (`a1fb029`)
Added `useChartHeight()` hook; clamp `ty` against `svgHeight - 8` rather than
`plotBottom`. Bumped `TH=160`. Resolved bottom cutoff.

#### Attempt 6 — No-wrap + Z-order (`a493db4`, `312ca3d`)
Two final issues:
1. Text wrapping: long model names wrapped at 220px foreignObject width. Fix: set
   `style={{ whiteSpace: 'nowrap' }}` on wrapper div (inherited by all CustomTooltip
   text); bumped `TW=300`, dropped `TH=130` (single-line content is shorter).
2. Z-order: Recharts 3.x renders custom children through its own pipeline, so
   CartesianGrid could appear after the `<g>` in SVG document order (last = topmost
   in SVG). Fix: `useLayoutEffect` with `svg.appendChild(g)` after each render —
   fires synchronously before browser paint, moves `<g>` to last child of the SVG
   unconditionally. Guard `svg.lastElementChild !== g` makes it a no-op when
   already in position.

### 3. Final Architecture of `GranularTooltips`

```tsx
function GranularTooltips({ points }) {
  const gRef = useRef<SVGGElement>(null)
  useLayoutEffect(() => {
    const g = gRef.current
    if (!g) return
    const svg = g.closest('svg')
    if (svg && svg.lastElementChild !== g) svg.appendChild(g)
  })
  const xDomain = useXAxisDomain(0)   // public Recharts 3.x hook
  const yDomain = useYAxisDomain(0)   // public Recharts 3.x hook
  const plotArea = usePlotArea()      // public Recharts 3.x hook
  const chartHeight = useChartHeight() // public Recharts 3.x hook
  // manual linear scales mirroring XAxis/YAxis
  // model → right of point, benchmark → left, fallback on overflow
  // vertical clamp to [plotTop, svgHeight - 8]
  // <foreignObject> per point, whiteSpace: nowrap, overflow="visible"
  // <CustomTooltip active={true} payload={[{payload: point}]} />
}
```

Hover tooltip (`<Tooltip content={<CustomTooltip />} />`) suppressed in granular
state to avoid double-display.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| `useLayoutEffect` for SVG reorder | Fires before paint; no user-visible flicker. `useEffect` would be too late. |
| Public hooks only (`useXAxisDomain`, `usePlotArea`, etc.) | `useXAxis`/`useYAxis` are internal-only in Recharts 3.x, not exported from index |
| Manual linear scale construction | Scale is linear with known domain+range; matches Recharts exactly without private API access |
| `whiteSpace: 'nowrap'` on wrapper div | `white-space` is inherited CSS — cascades to all CustomTooltip text without modifying shared component |
| model → right, benchmark → left | Opposite sides guarantees no overlap; both points share same model code so same X range |
| Hover tooltip suppressed in granular state | Both pinned and hover would show simultaneously; pinned already shows full info |
| BenchmarkHeatmap unaffected | Scoped to scatter chart only per Andrew |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/components/ReturnVolatilityScatter.tsx` | Full granular feature + GranularTooltips | Yes — `312ca3d` (DEV) |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `DEV` (portal), `CLOUD` (workspace)

`ReturnVolatilityScatter.tsx` is complete through `312ca3d`. Portal DEV pushed to
`origin/DEV`. CLOUD submodule pointer updated and pushed. Feature is live on remote.

---

## Next Steps

None — feature complete and pushed.

**Do NOT:**
- Touch `BenchmarkHeatmap.tsx` — heatmap granular filtering is explicitly out of scope.
- Modify `ModelPortfolios.tsx` — feature is self-contained in `ReturnVolatilityScatter.tsx`.
