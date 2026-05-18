# Session Log — 0.4.2_RD_AdvisorIntelligence
# Business Intelligence panel — Trade Activity lens window wiring (Inflection)

**Date:** 2026-05-18
**Mode:** Andrew-direct investigation + fix
**Portal commit:** `<this commit>` (DEV)
**Related project:** ADVI_BIWNDW (Books-tab BI Window Coverage) — sibling to TO-1 `ADVI_BIWNDW.001`

---

## Symptom (Andrew)

On Inflection / ADVI, the Business Intelligence panel's **Trade Activity** lens
(scatter + table) did not adjust to the Window toggle (QTD / YTD / 1Y / Max).
Andrew believed it had worked before and asked whether we regressed.

## Verdict — not a regression; the window was never wired to the data

Traced FE state -> React Query -> endpoint -> S3 artifact.

`InflectionInsightsPanel.tsx` had `selectedWindow` in the activity query's
**queryKey** (so React Query refetched on toggle) but the **queryFn** called
`getInflectionActivityScan(firmOverride)` with no window — and the endpoint
had only ever accepted `firmOverride`, always pulling the single legacy file
`platinum/firm/activity_scan.json` (one rolling-12M `txn_count_12m` field).

Git history is unambiguous: `getInflectionActivityScan` was introduced in
`1511d0b1` (ADVI_INFLV2.007) and its signature never changed. Commit
`22de0b4c` (2026-05-12, "feat(ActivityScan): ... window toggle") added the
window *toggle UI* + the queryKey entry + the axis-label string, but the data
plumbing was never built. So the toggle was cosmetic since day one — worse, it
relabeled the axes "Transactions (QTD)" etc. while still showing 12-month data.

Cash Drag worked (and made this look like a regression by contrast) because
`getInflectionCashDrag` passes the window and DS publishes 4 per-window files.

## Key finding — the DS work was already done

`data/orion/scripts/gold/INF_D_05.activity_scan.py` **already emits 4 per-window
artifacts** — `activity_scan_{qtd,ytd,1y,max}.json` — plus the legacy
`activity_scan.json` kept "for FE backward-compat ... DE will retire in next FE
PR once window-keyed paths are wired" (script header lines 30-33). Verified all
4 files on S3 (`opal-data-inf/platinum/firm/`), fresh 2026-05-18 12:28Z, and the
data genuinely differs per window (HH 449: `txn_count` 231 QTD vs 1,661 1y).

So this needed **no DS work and no DS~D handoff** — purely the owed FE wiring PR.

## Fix (FE-only, this commit)

`src/api/endpoints/advisor-intelligence.ts`:
- `getInflectionActivityScan(firmOverride?, window='1y')` — interpolate the
  window into the path: `activity_scan_${window}.json` (same pattern as
  `getInflectionCashDrag`). Legacy `activity_scan.json` no longer requested.
- `InflectionActivityScanRow.txn_count_12m` -> `txn_count` (the per-window
  files use `txn_count`; the field is window-scoped now, not rolling-12M).

`_partners/inflection/InflectionInsightsPanel.tsx`:
- activity queryFn now passes `selectedWindow` -> `getInflectionActivityScan(firmOverride, selectedWindow)`.
- `txn_count_12m` -> `txn_count` at all 8 consumer sites (scoreActivityRows,
  regression input, scatter datum map, tooltip, table col type / sortKey / cell).
- `ActivityTooltip` now takes `windowLabel` — tooltip text was hardcoded
  "txns (12m)", now "txns ({windowLabel})".
- Cosmetic: XAxis `name` "Txns (12m)" -> "Transactions"; header comment updated.
- `warnOnInflectionActivityShape` sentinel: added a `txn_count` presence check
  — catches a stale legacy-file fallback (legacy file lacks `txn_count`).

`.frontend-dev/testing/inflection_advisor_intelligence.md`: Surface 5 Activity
Scan row updated — column list + per-window verified txn counts.

## Verification

Browser smoke (general-purpose agent + Python Playwright, dev server :5175,
michael@opalinvest.com -> Select Partner -> Inflection -> Books -> Business
Intelligence -> Trade Activity). **PASS**:

| Window | URL requested | HH 449 Txns |
|---|---|---|
| 1Y  | `activity_scan_1y.json?firm=inf`  | 1,661 |
| QTD | `activity_scan_qtd.json?firm=inf` | 231 |
| YTD | `activity_scan_ytd.json?firm=inf` | 690 |
| Max | `activity_scan_max.json?firm=inf` | 7,124 |

All 4 distinct per-window files requested (200 OK); HH 449 txn count differs
per window and matches the S3 ground truth; scatter point cloud visibly shifts
left at QTD. Evidence (workspace root): `advi_biwnd_*.png`, `advi_biwnd_result.json`,
`advi_bi_window_smoke.py`.

## Compiler Tools

| Tool | Target | Result |
|---|---|---|
| `bun run typecheck` (`tsc -b --noEmit`) | portal full | exit 0 — 0 errors |
| `bun run lint` (`eslint .`) | portal full | 10 warnings, 0 errors — held at baseline; +0 added (the 1 surfaced warning is in an unrelated file) |
| `comp-transform schema-check InflectionInsightsPanel` | InflectionInsightsPanel | "All rendered fields match their response types" — clean. (`getInflectionFirmConcentrations` type-not-in-types.ts note is pre-existing, unrelated.) |
| Browser smoke (Playwright, :5175) | window re-fetch verify | PASS — 4 distinct per-window files, HH 449 txn count differs per window |

## Files Modified

| File | Repo/Branch | Change |
|---|---|---|
| `portal/src/api/endpoints/advisor-intelligence.ts` | portal/DEV | `getInflectionActivityScan` window param + path interpolation; `InflectionActivityScanRow` field rename |
| `portal/src/pages/AdvisorIntelligence/_partners/inflection/InflectionInsightsPanel.tsx` | portal/DEV | queryFn passes window; `txn_count_12m`->`txn_count`; window-aware tooltip; sentinel check |
| `portal/.frontend-dev/testing/inflection_advisor_intelligence.md` | portal/DEV | Surface 5 Activity Scan row — window behavior + verified counts |
| `org/.../deliverables/page_inventory.xml` | workspace/CLOUD | new `<api_call>` entry — Inflection Activity Scan (per-window) |
| `org/.../logs/2026-05-18/...` | workspace/CLOUD | this log |

Note: the endpoint file (`src/api/endpoints/advisor-intelligence.ts`) is outside
the strict `pages/AdvisorIntelligence/` page dir but is page-exclusive (serves
only InflectionInsightsPanel per `comp-platinum reverse`) and the 2-line change
is mechanically required for the page fix. MCP heads-up sent to 0.4.0_DE_ClientPlatform.

## Next Steps

1. **[0.4.0_DT_ClientPlatform]** Push portal DEV + bundle — FE-only, no artifact
   dependency (the 4 per-window files are already live on S3).
2. **[0.4.0_DS_ClientPlatform / DS~D]** Optional cleanup: `INF_D_05.activity_scan.py`
   can drop the legacy `activity_scan.json` emit now that no FE path reads it
   (the script header flags this as the owed retirement). Non-blocking.
3. **[Andrew]** Visual confirm post-deploy.

## Status

Complete. 1 portal/DEV commit (3 files, awaiting DT push+bundle), workspace
commit (log + page_inventory.xml). Smoke PASS. No DS work needed — DS already
shipped the per-window artifacts. No blockers.
