# SmartX `yaliu` HAR — endpoint findings + the daily-model-valuation lookback plan

**Author:** 1.0.0_SA_CTO · **Date:** 2026-07-14 (~03:4xZ) · **For:** Andrew, then §4a of the
consolidation PRD + the C5 SmartX TO.
**Source:** `smartx.smartxadvisory.com(yaliu).har` (494 entries; Yang's live session — **held in
scratchpad, NOT committed; it carries live bearer/session tokens**). Grounding is the HAR bytes, per
Rule 22. Cross-ref: `DATA_PLATFORM_D4_smartx_endpoint_sweep.md` (the `opal7`-account baseline).

---

## 1. THE HEADLINE: yaliu sees a materially larger surface than opal7

The `opal7` account D4 was swept on is a **manager-portal** login (`portal.managedaccounts.io/mngr`).
The `yaliu` account is the **full advisor app** (`smartx.smartxadvisory.com`, the Drupal/HCV
"dashboardv3" front end) — same three API hosts (`api.`, `performance.`, `identity.`) but **a wider
data grant and app-only endpoints D4 never touched.** Same OIDC/ROPC auth model (D4 §2 holds:
`identity.smartxadvisory.com/connect/token`, one JWT authenticates all hosts).

**Net-new data endpoints observed on yaliu (all 200, all JSON):**
| endpoint | grain | payload | why it matters |
|---|---|---|---|
| **`performance.smartxadvisory.com/models/summary?platform={id}`** | **897 models** | **5.23 MB** — per model: `statistics` (today/ytd/mtd/qtd + sharpe/sortino/std_dev/correlation/annualizedReturn{1,3,5}), `information` (name, `performanceStartDate`, `hcvPerformanceStartDate`, minimums, fee), `profile`, `feePercentage` | the model-universe stats surface — 897 vs the 11 the opal7 sweep saw. **`performanceStartDate`/`hcvPerformanceStartDate` per model = the lookback floor per model, stated by the vendor** |
| **`api/3.1/allocations/nonzerosleeve`** | **511 allocations (accounts)** | 394 KB — per allocation: `asOfTimestamp`, long/short position counts, opening/closing cash·dividend·interest·fee·**equity**, accountId, brokerageAcctNum, enterprise | **account-level daily equity with an `asOfTimestamp`** — the SMA-account valuation grain, not just model-level |
| **`api/3.1/users/access`** | entitlement | 708 KB — **906 modelAccess + 906 reportedModelAccess + 452 accountAccess**, each with `reportedModelId` + **`startTrackingDate`** | the yaliu grant enumerated: 906 models with a per-model tracking-start date, 452 accounts. This is the roster the pull iterates |
| `api/3.1/models/minimums` | 4,914 models | 641 KB | the full model catalog (minimums) — 4,914, the whole SmartX marketplace |
| `performance.smartxadvisory.com/models/sorted?sortBy=&order=&limit=&platform=` | ranked models | 32 KB | **parameterized** (sortBy/order/limit) — a queryable model list |
| `api/3.1/targets` · `api/3.1/accounts/counts` · `api/3.1/users` · `ng_api/v2/search_options` · `api/3.0/enterprise/{id}` · `api/3.0/commentary` | config/reference | small | target-weight groups, account counts, the model-search facet dictionary, enterprise branding |

**Everything non-SmartX in the HAR** (MSN news, giphy, intercom, fullstory, sentry, gstatic) is
browser/telemetry noise — excluded.

---

## 2. THE DAILY-VALUATION LOOKBACK QUESTION — what the HAR answers and what it does not

Andrew's ask: *historic daily position value of each model holding, back as far as possible; assess a
higher-granularity mechanism for daily model valuation + SMA fund lookback.*

**What is now in hand (yaliu-grant):**
- **Per-model lookback FLOOR is vendor-stated**: `performanceStartDate` / `hcvPerformanceStartDate` on
  every one of the 897 models. That is the "as far back as possible" answer, per model, without
  guessing — the pull reads it and backfills to it.
- **Account-level daily equity exists** (`nonzerosleeve.closingEquity` + `asOfTimestamp`) — 511
  allocations in one snapshot. This is the SMA-fund daily-value grain the opal7 path lacked.
- **The D4 daily flow-adjusted return series** (`models/{id}/performance?grouping=daily|weekly|monthly`)
  remains the model-return SoR — D4 measured it returns full history (daily→431 recs). The yaliu grant
  should widen WHICH models that works for (906 vs the opal7 roster).

**The one thing NOT yet proven, and it is the crux — a HAR is a snapshot, not a time machine:**
- **Per-holding daily HISTORY.** D4's hard finding on opal7: `reportedmodels/{rmid}/holdings` is
  **snapshot-only, `?date`/`?asOf` ignored, `holdings/historical` 404.** The yaliu HAR did NOT exercise
  a holdings screen with a date picker, so I **cannot yet claim** yaliu unlocks per-holding history.
  **This is the single most important thing the next capture must test** (§4). If yaliu's grant honors
  `?asOf` on holdings, that is the higher-granularity win; if not, per-holding daily value is
  **accrued** from the daily snapshot going forward (D4's standing answer) + reconstructed historically
  from `changerequesthistory` (the trade-event log) applied to a known holdings anchor.

**Honest verdict:** yaliu is a real granularity upgrade at the MODEL and ACCOUNT-EQUITY layers
(897 models, 511 daily-equity allocations, vendor-stated per-model floors, 906-model return access).
Whether it upgrades the PER-HOLDING history layer is **UNCONFIRMED and testable** — one more targeted
capture settles it.

---

## 3. THE BACKFILL + SILVER PLAN (into `opal-data-assets`, §4a/§4b)

**Bronze (raw JSON, byte-for-byte, channel-labeled):**
```
smartx/{platform}/bronze/models_summary/{YYYYMMDD}/summary.json        (perf host, 897 models + stats)
smartx/{platform}/bronze/model_performance/{model}/{YYYYMMDD}/...      (daily|weekly|monthly series, per model)
smartx/{model}/bronze/holdings/{YYYYMMDD}/...                          (reportedmodels/{rmid}/holdings snapshot)
smartx/{platform}/bronze/allocations_nonzerosleeve/{YYYYMMDD}/...      (account daily equity + asOf)
smartx/{platform}/bronze/access/{YYYYMMDD}/...                         (users/access roster — the pull's own iterator)
smartx/{platform}/bronze/{minimums,targets,counts,search_options}/{YYYYMMDD}/...   (reference)
```
- **Historic backfill, per model, to the vendor's stated floor**: for each model in `users/access`
  (906) read its `performanceStartDate`, pull `models/{id}/performance?grouping=daily` from that floor
  forward. This is the "as far back as possible" mechanism, bounded by the vendor's own attestation —
  no roll-forward, absent days ABSENT (§0.3 hyperrobust).
- **The GUI-era exports already in the estate** (`opal-data-smartx-v2/exports/`, 1,386 objects, span
  2025-12-23→2026-06-01, per-model allocation CSVs) mirror to `smartx/…/bronze/…` **channel-labeled
  gui-era** — the pre-REST history we already hold (§4b P-1).

**Silver (parquet, dedup + dtype only, every vendor column kept):**
- `models_summary` → one row per (model, run_date) with the flattened statistics block.
- `model_performance` → one row per (model, period) — dedup on period key (D4 bug 5: `performance`
  ignores date params, returns full history each call, so silver dedups).
- `holdings` → one row per (model, symbol, run_date); **vendor bugs preserved AS DELIVERED** (D4:
  `assetType` uniformly "equity" wrong, `industry`="Unknown") — classification is a GOLD join to Opal
  ETFClassifier, never a silver fix (Rule 17 + the completeness law).
- `allocations_nonzerosleeve` → one row per (allocation, asOf) — the account daily-equity fact table.

**Gold** (the emitter / future SmartX runner): daily model valuation + SMA lookback derive HERE from
the silver facts; the DDB cohort rows source from it. No summing below gold.

---

## 4. THE ONE CAPTURE THAT SETTLES THE GRANULARITY QUESTION (recommend before C5 locks the design)

A second short HAR on yaliu, specifically exercising **holdings with time controls** — the thing this
HAR did not touch:
1. Open a model's **holdings / composition** screen, then **change the as-of date** (or open a prior
   month) and let it fire — capture whether `reportedmodels/{rmid}/holdings?asOf=` returns different
   data or is ignored (D4's opal7 finding was: ignored).
2. Any **"performance since inception" or historical-holdings chart** — capture its backing call.
3. One **account/allocation drill with a date range** — confirm `nonzerosleeve` (or a sibling) accepts
   a date window vs snapshot-only.
If (1) honors `?asOf`, per-holding daily history is a direct pull and the design gets simpler + deeper.
If not, the design falls back to accrue-forward + `changerequesthistory` reconstruction — still an
upgrade over opal7, just not a free one.

---

## 2b. HAR #2 (`yaliu2`, 728 entries) — THE HISTORY QUESTION, ANSWERED (nuanced)

HAR #2 exercised the account-drill screens HAR #1 did not. **Verdict: yaliu is HIGHER FIDELITY than the
original design at the account / flow / valuation layers — and per-holding daily history is
RECONSTRUCTABLE from far richer inputs than opal7 gave, though still not a single direct time-series
pull.** New data endpoints:

| endpoint | what it carries | fidelity vs original |
|---|---|---|
| **`api/3.1/accounts/{id}/activity`** | **`ledger`: 572 dated events spanning 2025-03-04 → 2026-07-10** (16 months), each `{activityTimestamp, amount, activity, symbol, quantity}`. Activity types: Deposit · Withdrawal · Cash Dividend · Cash Dividend Accrual · Interest Received · Advisor/Management/Misc Fee · Cash Adjustment | **MAJOR UPGRADE.** 16 months of dated account-level CASH-FLOW history — the original SmartX design had NO account flow history. This is the NNA/flow reconstruction spine. **CAVEAT: these are CASH events, NOT buy/sell trades** — no position-quantity events here (trades live in `changerequesthistory`, D4) |
| **`api/3.1/accounts/{id}/holdings`** | 14 items: `{symbol, quantity, price, multiplier, marketValue, percentOfPortfolio}` | **UPGRADE.** Account-level holdings with a REAL price + marketValue + multiplier — vs the D4 `reportedmodels/holdings` whose `assetType` was uniformly-wrong "equity" and had no clean price. Still a SNAPSHOT (no date param seen) |
| **`api/4.1/cashmanagement/calendar?fromDate=&toDate=`** | `{transactions}`, **date-RANGE parameterized** (unix from/to) | a genuinely date-windowed endpoint — the first `?fromDate/toDate` we've seen honor a range; scheduled cash txns |
| **`enterprises/reports/model/{id}/allocations`** | per-model rollup: **3,182 account allocations, each `{accountId, accountNumber, aumValue}` + model `totalAum`** | the model→accounts AUM rollup — direct per-account AUM under a model |
| `api/3.1/allocations/statistics?accountId=&status=` | per-allocation `{value, cash, exposure{long/short/net/gross}, returns{today,mtd,qtd,ytd}}` | account-allocation valuation + return stat |
| `analytics.gtw.prod.smartx.us/mutual-funds`, `accounts/{id}/{statistics,exclusions}`, `targetweightgroups/{id}/details`, `cashmanagement/schedules/*` | mutual-fund reference, per-account stats/exclusions, target-weight detail | reference + config |

**HAR #3 (`yaliu3`) + the exported CSV — the fetch mechanism is CONFIRMED, and it is BETTER than
ranging:** the CSV (`WILLIAM_CHAN…activity_ledger`, 18 rows, 05/01–05/29/2026) is a **client-side
date-filter** — the browser fetches the FULL ledger once (`accounts/{id}/activity` with **NO date
params**, returning all 572 events / 16 months) and the CSV export slices to the UI-selected range
in-browser (the account's full ledger has 19 events in 2026-05; the CSV had 18 — a boundary edge, not
a different dataset). **So the pull is the simplest possible: ONE unparameterized GET per account
returns the complete account history — no ranging, no pagination, no from/to iteration.** (The
date-range params that DO exist are on `cashmanagement/calendar?fromDate=&toDate=` and
`calendar/detail?date=` — scheduled-cash surfaces, not the position/activity history.) This confirms
the 16-month account-flow ledger is trivially, completely pullable.

**The honest answer to "historic daily position value of each model holding, back as far as possible":**
- **Per-holding daily QUANTITY is not a single endpoint** — holdings stay snapshots (`?asOf` was NOT
  exercised on holdings even in HAR#2; the calendar range param is on cash txns, not holdings). So the
  D4 opal7 finding is not overturned for holdings specifically.
- **BUT the reconstruction is now well-fed and goes back ~16 months**: `holdings` snapshot (anchor,
  with real price/marketValue) + `changerequesthistory` (D4, the trade/rebalance events that move
  quantities) + `activity.ledger` (16mo dated cash/dividend/fee flows) + `models/{id}/performance`
  daily series (model return) → daily per-holding value reconstructed to 2025-03. That is materially
  higher fidelity than the original opal7-based design, which had a snapshot-only holdings view and no
  account flow history at all.
- **RECOMMENDED next probe to fully close it (cheap, one capture):** on a holdings/composition screen,
  explicitly change the AS-OF DATE and confirm whether `accounts/{id}/holdings?asOf=` or a sibling
  returns a prior-date snapshot. If yes, per-holding daily history is a direct pull and reconstruction
  is unnecessary. That is the last unknown.

**Bronze/silver additions (fold into §4a/§4b):** add `smartx/{account}/bronze/activity/{YYYYMMDD}/` (the
16-mo ledger — pulled once, then daily delta), `smartx/{account}/bronze/holdings/{YYYYMMDD}/` (daily
snapshot anchor), `smartx/{model}/bronze/model_allocations/{YYYYMMDD}/` (the 3,182-account rollup).
Silver: `activity` → account-flow fact (the NNA spine); `holdings` → account-position fact (daily
snapshot); reconstruction of daily per-holding value is a GOLD derivation, not silver.

## 4a. BASIS-LABEL DISCIPLINE ON ANY 49F/SMARTX AUM FIGURE (folded from COO's 2026-07-14 lift-era verify)
When the SmartX runner or the OPAL_RUNNERS 49F case doc quotes "~1.62b," it MUST carry its basis — the
same totalValue/managedValue precedent (a number without its basis is this project's defining defect).
The lift-era bd-49f verify found the record had paired the **BLENDED-PREFERRED total (~$1,621.6mm)**
with a feeder serving the **SCHWAB-RPS basis (~$1,390mm + ~$23mm SMA)** — **two different quantities on
partly different account universes, NOT a $230mm shortfall** (grounded `schwab_bd_cohort_framework.md:79`;
MEMORY.md now carries the labels). SmartX's `models/summary` stats and `nonzerosleeve` equity are their
OWN basis again — every emitted 49F/SmartX AUM row declares which one it is.

## 5. AUTH / OPERATIONAL NOTES
- Same OIDC/ROPC model as D4; one JWT spans `api.`/`performance.`/`identity.`. The `yaliu` credential
  is a **different, higher-grant principal** than the pipeline's `opal7` — using it recurrently is the
  SmartX vendor-egress lane Andrew already lifted (recurring, standing). **Which credential the
  production pull uses is an Andrew call** (yaliu is Yang's personal login; opal7 is Opal's service
  account — a dedicated higher-grant service credential may be worth requesting from SmartX rather than
  riding a person's login). Flagged, not assumed.
- The HAR file stays in scratchpad, uncommitted — it holds live tokens. Endpoint findings (this doc)
  carry no secrets and are safe on the record.
