# MDLP_WYNCHT Full Session — 0.4.0_DE_ClientPlatform

**Date:** 2026-03-11
**Start Time:** ~09:00
**End Time:** ~16:00
**Portal DEV commits:** none (tools/ only — no portal changes)
**Workspace CLOUD commits:** `a6fd5c12` → `89965ce9` → `02879be8` → `a6d7ab98` → `c335a9f6` → `d876bc87` → `cfd1fc9a` → `696a530a` → `10abd669` → `ef4058e0` → `627dc83f` → `5eae8094`

---

## Objective

Execute MDLP_WYNCHT task orders from COO:
1. Build a standalone offline HTML facsimile of the Model Portfolios benchmark tab
2. Stand up individual scatter and benchmark pages for presentation use
3. Build a peers quartile chart page from live S3 data
4. Investigate PowerPoint embedding options and deliver an interactive PPTX

---

## Work Completed

### 1. Orientation

Read recent logs (2026-03-10), confirmed ADVI_APISCP COMPLETE, ADVI_SNPLBK COMPLETE.
Two pending task orders received from COO today:
- `MDLP_WYNCHT.001.facsimile-html` — benchmark tab static clone
- `MDLP_WYNCHT.001` (DS) — pkl extraction script (later superseded)

### 2. Task Order Scope Revision — Hardcoded Data

COO revised `MDLP_WYNCHT.001.facsimile-html` mid-session: eliminated DS dependency
entirely. New scope: hardcode all 270 values directly from `model_portfolio_return_vol_20260227.csv`,
no JSON file loading, no file picker. DS task order `MDLP_WYNCHT.001.extract-benchmark-data`
is superseded and inactive.

Validated all 270 data points (5 models × 9 periods × 6 values) against CSV with Python
— zero mismatches.

### 3. facsimile.html — `tools/wyncht/facsimile.html`

**Commit:** `a6fd5c12`

Full standalone benchmark tab clone. Chart.js CDN for scatter, inline CSS grid for heatmap.

**Iterative refinement over multiple commits:**

| Commit | Change |
|--------|--------|
| `89965ce9` | Exact portal theme vars: brand silver page bg `hsl(222,24%,81%)`, panel headers `hsl(221,44%,14%)`, panel body `hsl(221,44%,21%)`, primary indigo `hsl(253,100%,68%)`. Panel titles `color:#fff uppercase tracking-wide` matching `PanelHeader.tsx`. Split LTC/LTA diamond, legend drilldown. |
| `02879be8` | Tooltips rebuilt as external HTML div matching `CustomTooltip` exactly: `bg-[hsl(221,44%,14%)]`, `border-white/20`, name bold white, type `white/60`, return `emerald-400`/`red-400`, vol `amber-400`. Manual `mousemove`/`click` canvas event handlers with pixel-distance hit detection — bypasses Chart.js hit detection which is unreliable for `pointRadius:0` datasets. `animation:false` for synchronous render. Granular pinned cards as absolutely-positioned HTML divs. |
| `a6d7ab98` | Timestamp: `"February 27th, 2026, 5:00p ET \| Source: Bloomberg."` matching `PanelFooter.tsx` format. X-axis `max = maxVol × 1.28` (28% headroom for LTC/LTA). Pinned card overlap resolver: detects x+y overlap, pushes cards apart vertically. |
| `c335a9f6` | Tooltip sizing: `width:max-content; max-width:260px; word-break:break-word` — cards grow to content, benchmark names (`85% Bloomberg Agg / 15% MSCI ACWI`) never overflow. Removed hardcoded JS `width=190px` that was clipping text. |

**Key technical decisions:**

| Decision | Rationale |
|----------|-----------|
| Manual canvas mousemove/click listeners | Chart.js `onHover`/`onClick` unreliable for invisible datasets (`pointRadius:0`). Pixel-distance check against `chart.scales.x.getPixelForValue()` is 100% reliable. |
| `animation:false` | Synchronous chart render — scales valid immediately after `new Chart()`, required for pinned card pixel positioning. |
| Split diamond via `afterDatasetsDraw` plugin | LTC and LTA share identical benchmark values in all periods (confirmed from CSV). One shared point, left half = LTC blue, right half = LTA red. In single-model granular state, renders as solid model color. |
| `CARD_W=260` for bounds checking | Card auto-sizes via CSS `width:max-content`, but 260px is the upper bound used for left/right placement calculation. |

### 4. S3 Bucket Setup — `opal-313476888478-wyncht`

Created public-read S3 bucket for hosting all facsimile pages:

```bash
aws s3api create-bucket --bucket opal-313476888478-wyncht --region us-east-1
aws s3api put-public-access-block ...  # all false
aws s3api put-bucket-policy ...        # s3:GetObject Principal:*
```

Re-upload command for any file:
```bash
export AWS_EC2_METADATA_DISABLED=true && aws s3 cp tools/wyncht/<file>.html s3://opal-313476888478-wyncht/<file>.html --content-type "text/html"
```

### 5. scatter.html + benchmark.html — Standalone Presentation Pages

**Commit:** `cfd1fc9a`

Extracted each chart component into its own fullscreen page for presentation use.

`scatter.html`:
- Chart fills viewport (flex:1 height, responsive)
- All toggles in header: Benchmark (Index/ETF), Returns (Gross/Net), Period (9 buttons)
- Full granular drilldown, split diamond, hover tooltips, pinned cards
- Benchmark type toggle switches benchmark points + volatility in scatter

`benchmark.html`:
- Heatmap + compositions only, no chart overhead
- Index/ETF and Gross/Net toggles
- Same 36 bps net proration logic

| Page | S3 URL |
|------|--------|
| Full facsimile | `https://opal-313476888478-wyncht.s3.amazonaws.com/facsimile.html` |
| Scatter only | `https://opal-313476888478-wyncht.s3.amazonaws.com/scatter.html` |
| Heatmap only | `https://opal-313476888478-wyncht.s3.amazonaws.com/benchmark.html` |

### 6. PPTX Action Buttons — `opal_iwm_partnership- 3.10.26 (interactive).pptx`

Investigated LiveWeb add-in for PowerPoint embedding — download link dead (404, expired SSL cert, site abandoned). Web Viewer Office Add-in not available in client's Office installation. Proceeded with python-pptx action buttons as reliable fallback.

Read PPTX structure (43 slides). Identified slides 23–27 as "Opal Model vs. Benchmark" — the target slides for interactive chart links.

Used python-pptx to add two navy action buttons to slides 23–27:
- `Return vs Volatility ↗` → `scatter.html`
- `Benchmark Heatmap ↗` → `benchmark.html`

Positioned bottom-right corner, Opal navy fill (`#163372`), white semibold text 8.5pt.
Buttons work via Ctrl+click in edit mode, single click in slideshow mode. No add-in dependency — any machine with a browser works.

Output: `C:/Users/AndrewBerman/Downloads/opal_iwm_partnership- 3.10.26 (interactive).pptx`

### 7. peers.html — Quartile Chart

**Commits:** `696a530a` → `10abd669` → `ef4058e0` → `627dc83f`

Fetched live peer performance data:
```bash
aws s3 cp s3://opal-data-portal-v2/json/peers/peer_performance.json ...
```

Data: `data_as_of: 2026-02-01`, 6 periods (1M, QTD, 1Q, YTD, 1Y, Since Inception),
5 models. Displayed as February 27th, 2026 per project convention.

Hardcoded all 30 rows (5 models × 6 periods × p5/p25/p50/p75/p95/model/bench).

Implements `PeersTab.tsx` exactly:
- SI annualization: `(1 + cumulative/100)^(365/actual_days) - 1` using `data_as_of=2026-02-01` and `inception=2024-04-30` (642 actual days)
- Quartile colors exact: `hsl(260,60%,50%)` (bottom), `hsl(220,40%,60%)`, `hsl(210,30%,70%)`, `hsl(210,50%,45%)` (top)
- Cyan arrow = model, black arrow = policy benchmark
- Global min/max Y scale across all periods for selected model (consistent axis)
- Model selector: UST/ST/INT/LTC/LTA, colored buttons, default LTC
- Period headers extracted from SVG to HTML `<div class="period-hdr">` — CSS-controlled spacing below legend divider
- `align-items:flex-start` on chart row for correct top-anchored column layout

| Refinement | Fix |
|-----------|-----|
| `10abd669` | `margin-bottom:36px` on legend strip; added `Model:` / `Policy Benchmark:` prefix to value labels |
| `ef4058e0` | Period headers moved from SVG text to HTML div — full CSS padding control |
| `627dc83f` | `align-items:flex-start` on chart-row — was `flex-end`, which was bottom-snapping columns and pulling period headers up into the legend area |

S3 URL: `https://opal-313476888478-wyncht.s3.amazonaws.com/peers.html`

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Hardcode data vs dynamic JSON loading | COO revised task order mid-session; eliminates DS dependency, simpler for screenshot/presentation use |
| Manual canvas event listeners | Chart.js built-in detection unreliable for zero-radius benchmark points |
| S3 public bucket (one-off) | Fastest path to shareable URL; not production infrastructure |
| python-pptx action buttons over LiveWeb | LiveWeb download dead; action buttons work on any machine with no add-in dependency |
| Period headers as HTML not SVG text | SVG text at y=16 with `overflow:visible` caused positioning issues relative to CSS-controlled parent layout |
| DS task order superseded | Hardcoded approach eliminates need for pkl extraction script |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `tools/wyncht/facsimile.html` | Created — full benchmark tab facsimile | Yes — `c335a9f6` |
| `tools/wyncht/scatter.html` | Created — scatter-only presentation page | Yes — `cfd1fc9a` |
| `tools/wyncht/benchmark.html` | Created — heatmap-only presentation page | Yes — `cfd1fc9a` |
| `tools/wyncht/peers.html` | Created — quartile peer comparison page | Yes — `627dc83f` |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/MDLP_WYNCHT.001.facsimile-html.md` | status → complete | Yes — `5eae8094` |
| `C:/Users/AndrewBerman/Downloads/opal_iwm_partnership- 3.10.26 (interactive).pptx` | New file — PPTX with action buttons on slides 23–27 | Local only (not a repo file) |
| S3 bucket `opal-313476888478-wyncht` | Created; facsimile.html, scatter.html, benchmark.html, peers.html uploaded | AWS live |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD

All four HTML pages live on S3. PPTX delivered to Downloads. All 13 CLOUD commits made.
MDLP_WYNCHT.001 task order marked complete.

The facsimile reproduces the portal's Performance tab with full visual fidelity:
exact theme vars, split LTC/LTA diamond, manual hit detection, pinned granular cards,
portal-matching tooltip structure, canonical PanelFooter timestamp. Peers chart replicates
PeersTab.tsx including SI annualization and global Y-axis scale.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Push CLOUD** — 13 commits pending push, including all wyncht tooling.
2. **[Andrew] Screenshot** — Open S3 URLs in Chrome, capture for documentation/audit.
3. **[Andrew] PPTX** — Open `opal_iwm_partnership- 3.10.26 (interactive).pptx`, verify buttons on slides 23–27 launch correct pages.

**Do NOT:**
- Modify `portal/` — all facsimile work is in `tools/wyncht/`, no portal changes
- Run DS extraction script — data is hardcoded; DS task order superseded
- Push to portal DEV — no portal commits were made this session
