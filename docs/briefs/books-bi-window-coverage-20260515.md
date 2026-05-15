# Brief — Books-tab "Business Intelligence" window coverage (49Financial + Inflection)

**Author:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-15
**Source:** Andrew direct, 2026-05-15
**For:** 2.0.0_SA_COO (decomposition into TOs)
**Status:** Analysis complete — ready for decomposition

---

## 1. Problem statement (Andrew)

In the **/Books tab** (both 49Financial and Inflection), the windowed metrics — **NNA, GRO
(AUA growth %), New Clients, Rank** — shown in the advisor summary table are meant to
re-compute when the user changes the window in the **"Business Intelligence"** panel.

- **49Financial:** QTD and YTD work. **1Y, 3Y, and Max all silently fall back to QTD.**
  Need full coverage for all windows.
- **Inflection:** the window selection does **not drive these metrics at all** — needs wiring.

---

## 2. How it works today (architecture)

| Piece | Detail |
|-------|--------|
| Books tab component | `BooksTab`, exported from `portal/src/pages/AdvisorIntelligence/_shared/tabs/ClientsTab.tsx` (shared by both partners) |
| Window state | `feePeriod` in BooksTab — type `FeeEfficiencyWindow` = `qtd \| ytd \| trailing_1y \| trailing_3y \| max`, default `trailing_1y` |
| "Business Intelligence" panel (49F) | `FeeEfficiencyPanel` — panel title literally "Business Intelligence"; window toggle `PERIOD_OPTIONS` offers QTD/YTD/1Y/3Y/Max; calls `onPeriodChange` → sets BooksTab `feePeriod` |
| "Business Intelligence" panel (Inflection) | `InflectionInsightsPanel` (passed to BooksTab as `revenueOpsSlot`) — also titled "Business Intelligence"; has its OWN internal `selectedWindow` state (`qtd \| ytd \| 1y \| max`) |
| Windowed metric table | `AdvisorSummaryTable` (in ClientsTab.tsx) renders the NNA / GRO / New Clients / Rank rows. Rank = list position. |
| Data binding | `periodAdvisors` (ClientsTab.tsx L343-369) maps `feePeriod` → a leaderboard window key → `employeeLbData.windows[key]` → feeds `AdvisorSummaryTable` |
| Data source | `employeeLbData` = `platinum/firm/leaderboard.json`, fetched by `getPlatinumFirmDashboard()` → `getFirmLeaderboard()` (advisor-intelligence.ts). Firm-routed S3: `opal-data-bd` (49F) / `opal-data-inf` (Inflection). |

---

## 3. Root-cause analysis

### 3a. DATA — `leaderboard.json` only carries 3 windows

Empirically verified (pulled both files from S3, 2026-05-15):

| File | `available_windows` | `windows` keys |
|------|---------------------|----------------|
| `s3://opal-data-bd/platinum/firm/leaderboard.json` (49F, gen 05-15T05:11Z) | `[QTD, YTD, MAX]` | QTD, YTD, MAX |
| `s3://opal-data-inf/platinum/firm/leaderboard.json` (Inflection, gen 05-15T16:44Z) | `[QTD, YTD, MAX]` | QTD, YTD, MAX |

**No 1Y window. No 3Y window.** Producers:
- 49F: `data/orion/scripts/gold/D_00c.portal_leaderboard.py`
- Inflection: `data/orion/scripts/gold/INF_D_00c.portal_leaderboard.py`

Both hardcode the window set: `_window_date_range()` handles only `QTD`/`YTD`/`MAX`; the build
loop is `for window in ('QTD','YTD','MAX')`; `available_windows` is a literal `['QTD','YTD','MAX']`.
(A legacy `data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py` has a richer
`WINDOWS = {'3M':90,'6M':180,'1Y':365,'2Y':730,'3Y':1095}` dict but still only builds
QTD/YTD/MAX, and is not the live producer — the orion-tier scripts are.)

### 3b. FRONTEND — `PERIOD_TO_LB_WINDOW` map (ClientsTab.tsx L345-347)

```js
const PERIOD_TO_LB_WINDOW = { qtd:'QTD', ytd:'YTD', trailing_1y:'1Y', trailing_3y:'3Y', max:'3Y' }
const lbKey = PERIOD_TO_LB_WINDOW[feePeriod] ?? '1Y'
const win = employeeLbData.windows[lbKey] ?? employeeLbData.windows[available_windows[0]]
```

Two distinct defects:
1. **`max → '3Y'` is a bug.** It should be `'MAX'`. The MAX window data **exists** in
   `leaderboard.json` — so the Max window is broken purely by a frontend typo, fixable
   with **zero backend work**.
2. **`trailing_1y → '1Y'` and `trailing_3y → '3Y'`** point at window keys the data does not
   contain → `employeeLbData.windows['1Y']` is `undefined` → the `?? windows[available_windows[0]]`
   fallback resolves to **QTD**. This is why 1Y/3Y show QTD numbers.

The silent fallback is what makes the bug invisible — the table shows QTD data under a "3Y"
label rather than erroring or disabling the option.

### 3c. FRONTEND — Inflection never lifts the window to `feePeriod`

Inflection's `layout.tabs.books.revenueOpsPanel = 'inflection_insights'` →
`hideFeeEfficiency = true` (ClientsTab L787) → `CanonicalBookView` (L113-119) renders the
`revenueOpsSlot` (`InflectionInsightsPanel`) **instead of** `FeeEfficiencyPanel`.

`FeeEfficiencyPanel` is the only thing wired to `onFeePeriodChange`. Since Inflection never
renders it, **`feePeriod` is frozen at its default `trailing_1y`**. `InflectionInsightsPanel`
has its own internal `selectedWindow` state that drives only its activity-scan / cash-drag
charts — it never calls back to BooksTab. Result: `periodAdvisors` always resolves
`trailing_1y → '1Y' → undefined → QTD fallback`; the `AdvisorSummaryTable` is permanently
static. "Not connected at all" — confirmed.

---

## 4. Frontend implementation

| ID | Change | Files | Effort |
|----|--------|-------|--------|
| **FE-1** | Fix `PERIOD_TO_LB_WINDOW` `max:'3Y'` → `max:'MAX'`. Restores the **Max** window for **both** firms immediately — data already exists. | `ClientsTab.tsx` L346 | ~15 min |
| **FE-2** | Wire Inflection's window selector to `feePeriod`. Add `onPeriodChange?: (w) => void` to `InflectionInsightsPanelProps`; inject it from BooksTab via the existing `cloneElement` mechanism (ClientsTab L573-578 already injects `onHouseholdClick` the same way); map `InflectionInsightsPanel`'s `Window` (`qtd/ytd/1y/max`) → `FeeEfficiencyWindow` (`qtd/ytd/trailing_1y/max`). | `InflectionInsightsPanel.tsx`, `ClientsTab.tsx` | ~1-2 h |
| **FE-3** | No further FE change needed once 1Y/3Y land in the data — `trailing_1y→'1Y'` / `trailing_3y→'3Y'` are already correct; they resolve as soon as the keys exist. | — | — |
| **FE-4** | Replace the silent QTD fallback with an explicit state. When `windows[lbKey]` is missing, disable that toggle option (or show "window unavailable") rather than render QTD data under a wrong label. This is what hid the bug. | `ClientsTab.tsx`, `FeeEfficiencyPanel.tsx` | ~30 min |
| **FE-5** | Reconcile window sets — 49F BI offers QTD/YTD/1Y/3Y/Max (5); Inflection's `InflectionInsightsPanel` offers QTD/YTD/1Y/Max (4, no 3Y). Product call: unify or accept the asymmetry. | layout-driven | — (see Q1) |

---

## 5. Backend implementation

| ID | Change | Files | Notes |
|----|--------|-------|-------|
| **BE-1** | Add `1Y` (data_as_of − 365d) and `3Y` (data_as_of − 1095d) branches to `_window_date_range()`. | `D_00c.portal_leaderboard.py` + `INF_D_00c.portal_leaderboard.py` (both `data/orion/scripts/gold/`) | Symmetric change, both firms |
| **BE-2** | Extend the build loop to `('QTD','YTD','MAX','1Y','3Y')` and the `available_windows` literal. | same | |
| **BE-3** | No per-aggregation change needed — NNA / new-clients / GRO / GRO-decomposition aggregators already take `(window_start, window_end)` and are window-agnostic. | — | Low-risk: the windowing is parameterized; only the date-range resolver is hardcoded |
| **BE-4** | Coverage pre-check: 1Y needs ≥1y silver history; 3Y needs ≥3y (holdings partitions back 3y for GRO `_aua_at_start`, transaction history for NNA/new-clients). The MAX window already aggregates inception-to-date successfully (Inflection MAX = 293 new clients / $135M NNA), so deep history exists — but a DS coverage check at the 3Y horizon is the pre-req. Same class as the INFGRO.006 MAX-coverage proof. | DS | Gating |
| **BE-5** | Known limitation: GRO (`aua_growth_pct`) is structurally null for MAX (no reliable inception-to-date AUA start). For 1Y/3Y it depends on a holdings partition near the window start; absent → null GRO for that window (FE already renders em-dash gracefully). | — | Document, not fix |
| **BE-6** | Payload size — +2 windows ≈ +60-70% on `leaderboard.json`. `D_04`/dashboard already has a split-mode threshold; confirm size stays under it. | — | Low risk |

---

## 6. Sequencing & effort

1. **FE-1** (`max:'MAX'`) — standalone, ships now, restores the **Max** window for **both**
   firms with zero backend dependency. Highest value-per-effort.
2. **FE-2** (Inflection lift) — ships now, makes Inflection's QTD/YTD/Max responsive.
3. **BE-1..4** (1Y/3Y emit) — gold-script change, both firms, needs a DS owner + a chain
   run. After this, 1Y/3Y light up with no further FE work (FE-3).
4. **FE-4** (defensive) + **FE-5** (reconciliation) — fast-follow.

**Coordination note:** BE-1..4 touch `INF_D_00c.portal_leaderboard.py` and require a gold
chain re-run. There is already an open INFGRO defect in the same file — `firm_return_pct_twr`
window aggregation (DE 0.4 finding 2026-05-15, session log `b1fd04b30`, routed to CTO).
**Recommend folding the 1Y/3Y window addition into the same INF_D_00c fix + chain run** to
avoid two separate chain cycles. COO to coordinate with the INFGRO gold owner (DS~C/base).

---

## 7. Open product questions (COO / CTO)

- **Q1 — window set.** Should Inflection's BI panel gain a 3Y option (it currently has none)?
  Unify both firms on QTD/YTD/1Y/3Y/Max, or accept Inflection = QTD/YTD/1Y/Max?
- **Q2 — MAX-window GRO.** `aua_growth_pct` is structurally null for MAX. Acceptable as an
  em-dash, or should the GRO column hide when Max is selected?
- **Q3 — priority split.** FE-1 (Max fix) and FE-2 (Inflection wiring) are cheap and
  high-value and have no backend dependency — can they ship ahead of the BE 1Y/3Y work?

---

## Compiler tools (this analysis)

- `comp-routes trace getFirmLeaderboard` — confirmed CF behavior + S3 key `platinum/firm/leaderboard.json`, firm-routed origin.
- `comp-cache collisions` — `firm-leaderboard` cache key is shared across `index` / `AdvisorsTab` / `ClientsTab`, all typed `PlatinumLeaderboardResponse` — intentional dedup, no collision.

Implementation TOs must run: `comp-transform schema-check` on `BooksTab` / `FeeEfficiencyPanel` /
`InflectionInsightsPanel`; `comp-pipescript io` on `D_00c` + `INF_D_00c` (COLUMN GAPS check for
the new window aggregations).
