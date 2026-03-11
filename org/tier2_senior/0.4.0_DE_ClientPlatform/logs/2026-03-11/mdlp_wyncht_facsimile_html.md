# MDLP_WYNCHT.001: Benchmark Tab Facsimile HTML — 0.4.0_DE_ClientPlatform

**Date:** 2026-03-11
**Portal DEV commits:** none (tools/ only — no portal changes)
**Workspace CLOUD commits:** `a6fd5c12` → `89965ce9` → `02879be8` → `a6d7ab98` → `c335a9f6`

## Objective

Build a standalone offline HTML facsimile of the Model Portfolios benchmark tab
(Return vs Volatility scatter + Benchmark Heatmap) with all data hardcoded from
`model_portfolio_return_vol_20260227.csv`. Screenshot-ready for documentation and audit.
Task order revised mid-session from dynamic JSON-loading to static hardcoded clone.

---

## Work Completed

### 1. Task Order Scope Revision

COO revised MDLP_WYNCHT.001 to eliminate the DS dependency (no JSON extraction script
needed). New scope: hardcode all values directly from CSV, no file picker, no dynamic
data loading. DS task order `MDLP_WYNCHT.001.extract-benchmark-data` is superseded.

### 2. Data Transcription

Transcribed all 270 data points (5 models × 9 periods × 6 values) from CSV into the
HTML JS data object. Validated with Python against source CSV — all values match.

### 3. Scatter Chart — Chart.js with Custom Plugins

| Feature | Implementation |
|---------|---------------|
| Period toggle (9 buttons, default YTD) | Rebuilds chart on click |
| Model circles | `pointRadius:8`, per-model color from `modelPortfolioColors.ts` |
| Benchmark diamonds | Canvas plugin (`afterDatasetsDraw`) — Chart.js renders nothing, plugin draws manually |
| LTC/LTA split diamond | One shared benchmark point; plugin draws left-half blue (LTC) / right-half red (LTA) when `solidColor=null`; solid single-color when in granular state |
| Hover tooltip | Manual `mousemove` canvas listener with pixel-distance hit detection — bypasses Chart.js hit detection entirely (unreliable for `pointRadius:0` datasets) |
| Granular click | Manual `click` canvas listener, same pixel-distance function; `animation:false` so scales are valid synchronously for pinned card positioning |
| Pinned cards (granular) | Absolutely-positioned HTML divs inside `#scatter-container`; model card prefers right, benchmark prefers left; overlap resolver pushes cards apart vertically |
| Y=0 reference line | Canvas plugin (`afterDraw`) |
| X-axis headroom | `max = maxVol × 1.28` — prevents LTC/LTA from being cramped in corner |

### 4. Benchmark Heatmap

CSS Grid (200px + 100px + 9×1fr). 3 rows per model (Model / Benchmark / Spread).
Model name column spans 3 rows with left border in model color. Spread cells use
`rgba(emerald/red/yellow, 0.5)` overlay matching `BenchmarkHeatmap.tsx` exactly.

### 5. Index/ETF + Gross/Net Toggles

Net cost proration matches `BenchmarkHeatmap.tsx` exactly:
- `net = gross - (trading_days / 252) * 0.36`
- Fixed: 1D=1, 1M=21, 1Q=63, 1Y=252, SI=252
- To-date (WTD/MTD/QTD/YTD): weekday count from period start to `2026-02-27`
- Net applies to Model and Spread rows only; benchmarks always gross
- Scatter chart also applies net to model points (not benchmark points)

### 6. Theme — Exact Portal Vars

| Element | Value |
|---------|-------|
| Page background | `hsl(222,24%,81%)` — Opal brand silver (`--palette-silver`) |
| Panel header | `hsl(221,44%,14%)` — `--semantic-background-muted` |
| Panel body | `hsl(221,44%,21%)` — `--semantic-background-surface` |
| Tooltip bg | `hsl(221,44%,11%)` — `--semantic-background-tooltip` |
| Panel titles | `color:#fff; text-transform:uppercase; tracking-wide` — exact `PanelHeader.tsx` |
| Tooltip structure | Exact `CustomTooltip` from `ReturnVolatilityScatter.tsx`: name bold white, type white/60, return emerald-400/red-400, vol amber-400 |
| Tooltip sizing | `width:max-content; max-width:260px; word-break:break-word` — grows to content, benchmark names never overflow |

### 7. PanelFooter Timestamp

Format matches `PanelFooter.tsx`: `"February 27th, 2026, 5:00p ET | Source: Bloomberg."`
Right-aligned, `text-xs text-white/40`, on all three panels.

### 8. S3 Hosting

Bucket: `opal-313476888478-wyncht` (one-off, public-read)
URL: `https://opal-313476888478-wyncht.s3.amazonaws.com/facsimile.html`

Re-upload command:
```bash
export AWS_EC2_METADATA_DISABLED=true && aws s3 cp tools/wyncht/facsimile.html s3://opal-313476888478-wyncht/facsimile.html --content-type "text/html"
```

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Manual canvas event listeners instead of Chart.js `onHover`/`onClick` | Chart.js hit detection unreliable for `pointRadius:0` datasets even with `pointHitRadius`. Manual pixel-distance calculation is 100% reliable. |
| `animation:false` | Synchronous chart render — scales valid immediately after `new Chart()`, required for pinned card positioning. |
| Split diamond via canvas plugin | Recharts `renderCustomShape` polygon approach ported to Chart.js `afterDatasetsDraw`. Clean separation: Chart.js renders nothing for benchmark dataset, plugin owns all visual rendering. |
| `width:max-content; max-width:260px` on tooltips | Tooltip grows to fit longest line (benchmark names), caps before becoming unwieldy. Removed hardcoded 190px width that was clipping text. |
| `CARD_W=260` in positioning math | Conservative bound for `left/right` placement decision — card will be ≤260px wide. |
| One shared LTC/LTA benchmark point | LTC and LTA have identical benchmark values in all periods (confirmed from CSV). One point avoids visual double-counting. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `tools/wyncht/facsimile.html` | Created — complete standalone facsimile | Yes — CLOUD `c335a9f6` |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/MDLP_WYNCHT.001.facsimile-html.md` | status → complete | No — local only |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

`tools/wyncht/facsimile.html` delivered and live at S3 URL above. All 9 acceptance
criteria met. Scatter chart, heatmap, all toggles, granular drilldown, hover tooltips,
pinned cards, PanelFooter timestamps all match portal visual language. Data validated
against `model_portfolio_return_vol_20260227.csv` (270 values, 0 mismatches).

---

## Next Steps

1. **[Andrew] Screenshot** — Open S3 URL in Chrome, capture benchmark tab for documentation.
2. **[0.4.0_DT_ClientPlatform] Commit org changes to CLOUD** — this session log + task order status update.

**Do NOT:**
- Run `pip install` or any Python tooling — data is hardcoded, no extraction script needed
- Modify `portal/` — facsimile is entirely in `tools/wyncht/`
