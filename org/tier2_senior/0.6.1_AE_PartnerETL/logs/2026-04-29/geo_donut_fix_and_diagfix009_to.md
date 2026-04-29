# Session Log — 0.6.1_AE_PartnerETL — Geo Donut Fix + DIAGFIX.009 TO — 2026-04-29

**Agent:** 0.6.1_AE_PartnerETL (base lane)
**Date:** 2026-04-29
**Session scope:** Geo donut $89.6M -> $182.6M fix in INF_D_04; DIAGFIX.009 TO drafted for upstream holdings pricing strategy
**Continuation of:** diagfix_rerun_wave_and_catalog.md (same day)

---

## Context

Andrew flagged the geo radial in the portal showing $89M AUA — half of actual firm AUA ($182.6M). Initial hypothesis: accounts with null state_code being excluded from geo total.

Investigation revealed a deeper architectural issue: the geo view in `_build_geo_view()` was sourcing per-account AUA from `holdings.market_value` (which carries the nav_price=0 reconstruction bug from INF_B_00). Same root cause as the firm-level $89.6M issue we fixed earlier today via D_04 + aum_snapshot pattern, but this branch of the code never got the fix.

Andrew's strategic direction:
> "we've been through this ad nauseam with 49financial, the issue is not snapshot numbers
> its constructing lookback. if in a client page they have time series that accounts for
> nav value on a daily basis, then awesome lets grab it right from the source. if they
> do not have that, then the simple mechanism for valuation is what we do for 49financial
> whereby there are type A B and C assets"

Two parallel tracks:
1. **Immediate**: fix the geo donut to use aum_snapshot (same as views.aua); null state -> Other
2. **Strategic**: file a TO for DS to investigate Orion daily EndingMV endpoint, with BD A/B/C pricing pattern as the fallback if daily data not available

---

## Track 1: Geo Donut Fix

### Diagnosis

Read `_build_geo_view()` in INF_D_04.client_portal_summary.py:
- Function signature: `_build_geo_view(holdings, household_dim, ...)` — only got holdings + household_dim
- Lines 1564-1568: `acct_aua = holdings.groupby('account_id')['market_value'].sum()` — per-account AUA from holdings
- Lines 1593-1595: `merged = merged[merged['state_code'].notna()]` + empty-string filter — null states dropped, not bucketed

Confirmed via inspection of partner_analytics_quarterly.json: `views.geo.donut.total = 89,590,439` (exactly the holdings sum), while `views.aua.donut.total = 182,552,381` (the aum_snapshot sum already wired correctly).

So both Andrew's hypothesis (null exclusion) AND the deeper holdings problem were active. The fix had to address both.

### Fix (commit e39ebd025)

Two changes to `_build_geo_view()`:

1. **Add `aum_snapshot` + `accounts_dim` params**, same pattern `_build_aua_view()` already uses (lines 1727-1741). When aum_snapshot available with `managed_value` + `household_id`, use it as AUA source.

2. **Null/empty state_code -> 'Other'** instead of row drop. Mask: `state_code.isna() | state_code.str.strip() == ''` -> assign 'Other'. Applied in both the aum_snapshot path and the holdings-fallback path.

Household -> state mapping has two paths in the new code:
- Path 1: `household_dim` has `household_id` column directly -> dedupe + use
- Path 2: route through `accounts_dim` (`account_id -> household_id`) joined to `household_dim` (`account_id -> state_code`) -> groupby household_id, take first state

Call site (line 1868) updated to pass `aum_snapshot=aum_snapshot, accounts_dim=accounts_dim` — both already in scope.

Pre-commit gate: clean (py_compile + ds-precommit-check.py + ruff).

### Deploy + verify

| Step | Result |
|---|---|
| Upload to s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py | 94,470 bytes |
| EC2 i-0ed5afded2ebd4ed4 start (was stopped post-prior wave) | running, watchdog disabled |
| SSM run: INF_D_04 + INF_09 sync | 60s, exit 0 |
| `geo.donut.total` post-run | **$182,552,381** (matches firm AUA) |
| Households | 274 |
| Households with null state -> 'Other' | 0 (all had state data this run) |
| CF invalidation `I87P8RW9ERQIRHLBA3GZ6CNVGE` | InProgress |

### Geo segments (post-fix)

| State | AUA | % | Clients |
|---|---|---|---|
| WA | $164,160,869 | 89.9% | 237 |
| CA | $3,570,091 | 2.0% | 5 |
| IN | $3,142,351 | 1.7% | 1 |
| MT | $2,906,210 | 1.6% | 2 |
| MN | $2,309,204 | 1.3% | 3 |
| TX | $1,760,732 | 1.0% | 2 |
| ID | $1,155,793 | 0.6% | 3 |
| AZ | $1,004,628 | 0.6% | 5 |
| OTHER | $2,542,504 | 1.4% | 16 |

Sum = $182,552,382 (rounding to $1).

### Pre-existing failures flagged

INF_09 exited 0 but reported 2 upstream failures:
- `INF_D_00c.portal_leaderboard.py failed`
- `INF_D_02.advisor_client_detail.py failed`

These are pre-existing issues — partner_analytics_quarterly.json wrote correctly. Flagged in RAVC to COO for separate routing; not in scope of geo fix.

---

## Track 2: DIAGFIX.009 TO — Holdings Pricing Strategy

### Background

Andrew explained why the holdings reconstruction is architecturally wrong:
- TRN feed = transaction events, not a price feed
- "Last seen wins" + non-trade events with nav_price=0 = corrupted prices for affected positions
- Even the guard fix (`if nav > 0`) deployed today only stops future corruption; the price used remains the price at the LAST TRADE, which can be stale by days/weeks
- That's why holdings = $190.5M (overcorrection) vs aum_snapshot = $182.6M (true)

aum_snapshot from Orion AUM API is fine for **aggregate AUA totals**. But for **position-level daily market values** (timeseries lookback, concentration_risk, composition), we need a real price source.

### TO scope (commit 394c34606)

**File:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INFLEC.DIAGFIX.009.ds-holdings-pricing-strategy.md`

**Phase 1 (1-2h, investigation only)**
Probe the Orion Envision API we already have working:
- `pull_inflection_positions.py` already pulls `Activity.Value(activityOptionId=1)` (Ending Market Value) over a Rolling 3-Year date range
- `PATH_DISCOVERY.md` confirms `DateRange.StartDate` / `DateRange.EndDate` paths work

Questions to answer:
1. Granularity — daily per (account, asset, date) or single period-end value?
2. Coverage — gaps?
3. Ticker linkage — reliable join back to ticker/CUSIP?
4. Historical depth — full 3 years?

Probe deliverable: extend `pull_inflection_positions.py` for a 30-day window, write to `bronze/orion-api/probe/positions_mv_30d.csv`, count distinct dates per (account, ticker).

**Phase 2 (strategy decision)**

If Phase 1 returns daily EndingMV:
- Path A: design `silver/positions_mv/snapshot_date={date}/data.parquet`, replace TRN reconstruction in INF_B_00 with direct EndingMV pulls
- Estimate: 1-2 sprint days

If Phase 1 returns period-end only:
- Path B: adapt BD pipeline's A/B/C pricing pattern
  - Type A (liquid, public ticker — ETFs/MFs/equities) -> Yahoo Finance daily EOD close
  - Type B (illiquid/alternatives) -> Orion period-end + linear interpolation
  - Type C (cash/MM) -> face value
- Reference: `data/black_diamond/scripts/gold/build_canonical_prices_v2.py` (T1->T4 SOURCE_RANK system) + `bd_price_update.py`
- Bucket assignment uses Orion-native `product_category` + `asset_class` from `silver/api_dims/assets_v2/` (INF_I_D03 already uses this — no separate ETFClassifier or DDB)
- Estimate: 3-5 sprint days

### Constraints written into TO

- Do NOT modify INF_B_00 or B-chain until Phase 1 findings are in
- Guard fix (`if nav > 0`) deployed today is stable; do not break it
- aum_snapshot remains authoritative for all aggregate AUA views (do not regress)
- Phase 1 is investigation only; no silver writes until COO approves the path

DS notified via MCP at 22:25Z.

---

## Files Changed

| File | Change | Commit |
|---|---|---|
| data/orion/scripts/gold/INF_D_04.client_portal_summary.py | _build_geo_view aum_snapshot source + null state -> Other | e39ebd025 |
| org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INFLEC.DIAGFIX.009.ds-holdings-pricing-strategy.md | New TO | 394c34606 |

---

## Compiler Tools

| Tool | Why ran / skipped |
|---|---|
| `comp-pipescript io INF_D_04` | N/A — INF not in comp catalog (gap flagged DIAGFIX.001) |
| `comp-iam` | N/A — no new boto3 calls; geo fix is pure pandas in-memory |
| `comp-validate` | N/A — no validation config for INF partner_analytics |
| `comp-blast` | N/A — single function modification, callers already audited |

---

## RAVCs / Messages Sent

- 22:25Z — TO MCP to 0.4.0_DS_ClientPlatform: DIAGFIX.009 holdings pricing strategy
- 22:31Z — RAVC to 2.0.0_SA_COO: geo donut fix shipped + DIAGFIX.009 filed

---

## Open Items Carried Forward

- DIAGFIX.009 Phase 1 probe — DS owns
- INF_D_00c + INF_D_02 pre-existing failures — separate routing needed
- concentration_risk gap (DIAGFIX.001 carried forward) — partially resolved by DIAGFIX.009 outcomes (correct prices -> correct concentration)
- INFSHIP.A2 Orion asset API HAR capture — Andrew initiation required
- daria_zalewska/ stale S3 dir — needs Andrew authorization
- ORIAPI Phase 1 closure gate — TWO clean cron cycles (2026-04-30 + 2026-05-01)

---

## EC2 State at Session End

`i-0ed5afded2ebd4ed4` — running, watchdog timer disabled (will not auto-stop). Safe for AE/COO to stop manually when nothing else queued, or leave for next dispatch.

---

## Key Architectural Note for Future Sessions

Two distinct AUA sources in this codebase, do not confuse:

1. **aum_snapshot.managed_value** (silver/aum_snapshot/{date}.parquet) — Orion AUM API reconciled value per household. **Use this for all aggregate dollar amounts** (donut totals, leaderboard, geo segmentation, partner_analytics totals). $182.6M canonical.

2. **holdings.market_value** (gold/canonical/holdings_{date}.parquet) — INF_B_00 reconstruction from TRN feed. **Has known nav_price corruption bug** even after the guard fix. **Do not use for aggregate totals.** Currently fine for relative composition (% of portfolio per ticker) but not for absolute dollars. DIAGFIX.009 will replace this.

Any new gold script that aggregates AUA must source from aum_snapshot, not holdings, until DIAGFIX.009 lands a real position-level price layer.
