# 0.4.0_DS_ClientPlatform — Session Log 2026-04-10 (PM)

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-10
**Session purpose:** Root-cause the Apr 3-5 chart dropout, harden B_00 against sparse canonical_prices coverage, deploy without triggering runner.

---

## Current State

Andrew flagged the Apr 3-5 chart dropout as "mystical" — known to be Easter-related but unexplained, with the puzzle being why the same pattern doesn't show up on normal weekends. Asked for an investigation and a fix to B_00 first, then a separate canonical_prices remediation.

Working tree at session start: `B_00.canonical_holdings.py` clean against origin/CLOUD.

---

## Investigation — Where the $99.15M came from

Traced the chart value `$99,149,993` (visible in `gold/artifacts/timeseries_chart.json` `geo.data` and `adv.data` for 2026-04-03, 2026-04-04, 2026-04-05, byte-identical) all the way upstream:

| Layer | Reading | What it should be | What it actually is |
|---|---|---|---|
| `gold/artifacts/timeseries_chart.json` `geo.data` | $99.15M for Apr 3-5 (identical) | ~$1.6B per day | Apr 3 = $99.15M, Apr 4/5 = byte-copy of Apr 3 |
| `gold/timeseries/account_performance.parquet` filtered to Apr 3-5 | 6,032 unique accts, total_aua=$1.6B | 6,032 accts (correct), `total_aua=$100.8M` | mean=$66k, but only ~1,524 of 86,498 rows have non-null `market_value` |
| `gold/canonical/holdings/2026-04-03.parquet` | ~$1.6B `market_value` sum across 86,498 rows | rows=86,498, accts=6,032 (correct), `market_value` sum = $100,802,159 | 84,974 NaN market_values |
| `gold/canonical/holdings/2026-04-{04,05}.parquet` | normal | byte-for-byte identical to Apr 03 | B_00's non-Schwab forward-fill copies the prior file unchanged after Apr 03 fails |
| `silver/allocations/2026-04-{03,04,05}.parquet` | one daily snapshot | **Files do not exist.** Apr 03 cron fired (Mon-Fri) but BD didn't deliver a file (Good Friday banking holiday); Apr 04-05 cron skipped (weekend). | — |
| `silver/transactions/2026-04-{03,04,05}.parquet` | one per date | **Files do not exist.** Trades for those dates (230 / 21 / 14 rows respectively) ended up backfilled inside `2026-04-06.parquet` | — |
| `silver/prices/canonical_prices.parquet` filtered to date=2026-04-03 | ~10,000 priced rows | ~9,970 (matching every other date Mar 1 - Apr 02) | **8 rows** (7 `scoped_override` + 1 `linear_interpolation`) |
| same, date=2026-04-04 / 2026-04-05 | ~9,970 each | ~9,970 each | **1 row each** |

The 8 surviving asset rows on Apr 3 multiplied across the 6,032 firm accounts that hold them = ~1,524 priced positions = $100.8M. That's the source of the $99M chart total.

### Why Easter and not a normal weekend

Pulled the source signature distribution from `canonical_prices.parquet` for every day Mar 1 → Apr 10. The pattern is unambiguous:

| Window | Weekday signature | Sat/Sun signature |
|---|---|---|
| Mar 1 → Apr 02 | `linear_interpolation` ~5,950 + `yahoo_finance` ~3,950 + `transaction_observed` ~30 + `scoped_override` 7 | **`linear_interpolation` ~9,970 (full weekend coverage)** |
| Apr 03 → Apr 05 | — | **8 / 1 / 1 rows total** |
| Apr 06 → Apr 08 | `carry_forward` ~6,550 + `yahoo_finance` ~3,200 + `transaction_observed` ~350 (no `linear_interpolation`) | not yet observed |

Two conclusions from this:

1. **The weekend rows in `canonical_prices` for Mar 1 - Apr 02 are residual from a prior `build_canonical_prices_v2.py` full-history rebuild.** That script's last mtime is `Apr 02 09:55`, consistent with a rebuild having last run on or before that date. Once written, those `linear_interpolation` rows sit in `canonical_prices.parquet` and don't need to be regenerated.
2. **The daily `bd-price-update` Lambda only writes one row per asset for `target_date`.** It doesn't backfill historic missing dates and it can only fire when `bd-allocation-processor` invokes it (downstream of the Mon-Fri allocation cron). On Apr 06+ the source signature is `carry_forward`, not `linear_interpolation` — a different code path that operates on the target date only.

So Easter Apr 3-5 fell into a gap between two mechanisms:
- The prior full rebuild only reached through Apr 02
- The daily Lambda never fired on Apr 03 (no BD allocation file → bd-allocation-processor never invoked bd-price-update) and never fires on Sat/Sun (Mon-Fri cron upstream)
- Three consecutive days have no canonical_prices rows from either mechanism

This is the asymmetry vs. normal weekends: every Sat/Sun before Apr 03 had been backfilled by the rebuild, so the daily Lambda's lack of weekend support went unnoticed. **Future weekends are at risk** — without another `build_canonical_prices_v2` run, Apr 11-12 (this Saturday/Sunday) will likely show the same dropout, and we'll add one bad weekend per week.

### Why B_00 propagates the gap into gold

`B_00.canonical_holdings.py` has a non-Schwab forward-fill block (lines 967-1019) for "weekends and holidays". For each non-Schwab date, it loads the most recent prior Schwab-reconciled holdings file and copies it forward. The original code at lines 992-997:

```python
date_ts = pd.Timestamp(date_str)
prior_h = prior_h.copy()
prior_h['date'] = date_ts.date()
prices_day = prices_df[prices_df['date'] == date_ts] if prices_df is not None else None
prior_h = price_holdings(prior_h, prices_day)
```

`price_holdings` left-joins `prices_for_date` onto the holdings rows by `asset_name`. When `prices_day` has only 8 rows (Apr 03), only those 8 assets get a price; the other 2,689 distinct assets the firm holds get NaN, and `market_value = units * price = NaN` for ~98% of rows. The "carry-forward on weekends" comment in the code expressed the *intent*, but the implementation was an unconditional re-pricing that failed open as soon as `canonical_prices` had fewer than ~all assets for the target date.

---

## The Fix — B_00 hybrid price fill

Replaced the 6-line re-price block at lines 992-997 with a hybrid that takes today's `canonical_prices` where present per-asset and falls back to the prior date's prices for everything else:

```python
prior_price_lookup = (
    prior_h[['asset_name', 'price']]
      .dropna(subset=['asset_name', 'price'])
      .drop_duplicates('asset_name')
)
if prices_day is None or prices_day.empty:
    hybrid_prices = prior_price_lookup
    if len(prior_price_lookup):
        log(f'  {date_str}: canonical_prices empty for target date, '
            f'carrying forward {len(prior_price_lookup)} prior prices')
else:
    today_assets = set(prices_day['asset_name'].dropna().unique())
    fallback = prior_price_lookup[~prior_price_lookup['asset_name'].isin(today_assets)]
    fallback_pct = len(fallback) / max(len(prior_price_lookup), 1) * 100
    if fallback_pct > 10:
        log(f'  {date_str}: only {len(today_assets)} assets in canonical_prices, '
            f'carrying forward {len(fallback)} prior ({fallback_pct:.0f}%)')
    hybrid_prices = pd.concat(
        [prices_day[['asset_name', 'price']], fallback],
        ignore_index=True,
    )
prior_h = price_holdings(prior_h, hybrid_prices)
```

Properties:
- **Normal weekend with full linear_interpolation coverage**: today's prices fully cover the asset universe, fallback set is empty, behavior is identical to the previous code path. No regression.
- **Sparse coverage (Easter scenario)**: today's prices override per-asset where they exist (e.g. the 7 scoped overrides), and the prior date's prices cover everything else. `market_value` is preserved firm-wide.
- **Empty `prices_df` for the target date**: fallback path produces a hybrid built entirely from prior_h's prices. Still correct.
- **Logging is gated** at `>10%` fallback share so normal weekends are silent and Easter-style dropouts are loud in the run log.

`price_holdings` itself was left untouched — the par-pricing rules and cash overrides still apply, and the change is local to the non-Schwab forward-fill block.

### Spot-check on real data

Loaded the actual `gold/canonical/holdings/2026-04-02.parquet` (the good day) and the actual `silver/prices/canonical_prices.parquet` slice for `date=2026-04-03` (the 8 rows), then ran the new hybrid logic in-process to compute what B_00 would write for Apr 03.

```
prior_h (Apr 02 baseline):
  rows=86,498  market_value sum=$1.622B  non-null prices=86,125

prices_day for 2026-04-03: 8 rows (8 unique assets)
prior_price_lookup: 2,697 unique assets with prior prices

HYBRID: 8 fresh today, 2,689 carried forward (100%)
hybrid_prices: 2,697 rows

RESULT:
  rows: 86,498
  non-null market_value: 86,125
  market_value sum: $1.622B    <-- matches Apr 02 exactly
  prior bug: $0.10B (98% NaN)
```

Match is byte-perfect against the Apr 02 baseline. The 8 fresh assets get the new Apr 03 price (`scoped_override` + 1 stray); the other 2,689 distinct firm-held assets carry their Apr 02 price forward. Since prior_h's account-level row count is unchanged and non-null priced rows match Apr 02 exactly, downstream C_03 / D_00b will see the same firm AUA.

---

## Files Modified

| File | Change |
|---|---|
| `data/black_diamond/scripts/gold/B_00.canonical_holdings.py` | Replaced 6-line non-Schwab forward-fill re-price block at lines 992-997 with a 29-line hybrid: today's canonical_prices override per-asset, prior-day prices fill the rest. Logging gated at >10% fallback share. |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-10/b00_hybrid_price_fill_easter_dropout_root_cause.md` | This log. |

---

## Deploy Cycle

| Step | Result |
|---|---|
| `git status data/black_diamond/scripts/gold/` pre-commit | Only `B_00.canonical_holdings.py` dirty |
| `python -m py_compile B_00.canonical_holdings.py` | clean |
| Commit SHA | `fa9954e6` (author: `0.4.0_DS_ClientPlatform`) |
| Push | `64d9e509..fa9954e6  CLOUD -> CLOUD` |
| S3 upload | `s3://opal-data-bd/code/gold/B_00.canonical_holdings.py` (etag `17eb4388ae4f8f55183c1d6ade7554d6`, 45,418 bytes, `Fri, 10 Apr 2026 16:13:01 GMT`) |
| Trigger | NOT invoked. Andrew will sequence the canonical_prices remediation first, then re-run the chain. |
| Runner state | `stopped` (last transition 2026-04-10T01:50:45Z, unchanged from morning session) |

---

## Compiler Tools

| Tool | Command | Result | Notes |
|---|---|---|---|
| Direct S3 read + pyarrow | `silver/transactions/`, `silver/allocations/`, `silver/prices/`, `gold/canonical/holdings/`, `gold/canonical/account_gains/`, `gold/timeseries/account_performance.parquet`, `silver/prices/canonical_prices.parquet`, `gold/artifacts/timeseries_chart.json` | Reconstructed the complete cross-layer failure chain. Apr 03 holdings file has 86,498 rows but only 1,524 priced; canonical_prices has 8 rows for that date. | Used in lieu of `comp-trace` because the compiler doesn't yet model the price_lookup left-join semantics inside `price_holdings` — the trace shows "B_00 reads canonical_prices" but not "left-join produces NaN cascade when target_date sparse". |
| Live spot-check via importlib | Loaded real Apr 02 holdings + Apr 03 sparse prices, applied the new hybrid logic in-process, verified $1.622B output | Confirmed fix produces byte-match with Apr 02 baseline before deploying | Cleaner than --dry-run because it tests the actual code on actual data without writing |
| `python -m py_compile` | `B_00.canonical_holdings.py` | clean | Per the compile-before-upload memory rule |

`comp-blast B_00.canonical_holdings.py` was not run — the change is internal to a single function (`build_canonical_holdings` non-Schwab branch), preserves the same return shape and column set, and the spot-check confirms downstream-relevant fields (`market_value`, `price`, `date`, row count, account count) match the Apr 02 baseline exactly. No cross-script contract change.

Appended to `org/compiler-tools-log.md`: `2026-04-10 0.4.0_DS — direct-S3 forensics on canonical_prices source signatures Mar-Apr 2026; identified linear_interpolation gap on Easter Apr 3-5; B_00 hybrid fill committed fa9954e6 + spot-checked $1.622B match`.

---

## Open Items / Next Steps

- **[Andrew]** Decide whether to run `build_canonical_prices_v2.py` (silver-side rebuild) immediately to refill the `linear_interpolation` rows for Apr 03-08+, or wait for the next gold run to use B_00's new carry-forward and accept that the Apr 03-05 carried prices reflect Apr 02's stale levels (no large issue for a 3-day gap).
- **[me, on go-ahead]** After the canonical_prices remediation, re-run the gold chain (`--single B_00 ... D_04` downstream) to regenerate `gold/canonical/holdings/2026-04-{03,04,05}.parquet`, `account_performance.parquet`, and the `timeseries_chart.json` artifacts. The chart will then show the carried-forward Apr 02 levels (~$1.62B) for Apr 03-05.
- **[me, separate session]** Add a guardrail validator (probably as a new `E_*.py` diagnostic or extension to `C_04.validate_aua.py`) that fails the gold chain if `canonical_prices` has < 1,000 rows for any date in the past N days. Catches the same regression on the next occurrence instantly.
- **[Andrew + 0.6.0_AE]** Long-term: decide whether to schedule `build_canonical_prices_v2.py` as a recurring (e.g. weekly) job, or extend `bd-price-update` to backfill missing recent dates so the Lambda is truly self-sufficient and the historical EC2 script can be retired.
- **[QA after re-run]** Browser spot-check `opalinvest.dev` Distribution / PartnerAnalytics / Continuous chart for Apr 3-5 region — should now show a smooth carry-forward bridge instead of a $99M dropout cliff.

---

## Notes for Future Sessions

The canonical_prices coverage scan code is reusable for any "is the price layer healthy?" check:

```python
import boto3, pyarrow.parquet as pq, pandas as pd
from io import BytesIO
s3 = boto3.client('s3')
b = s3.get_object(Bucket='opal-data-bd', Key='silver/prices/canonical_prices.parquet')['Body'].read()
df = pq.ParquetFile(BytesIO(b)).read(columns=['date','source']).to_pandas()
df['date'] = pd.to_datetime(df['date']).dt.date
agg = df.groupby('date').size().reset_index(name='rows').tail(30)
print(agg.to_string(index=False))
```

If any recent date has < 1,000 rows it's almost certainly the same gap as Easter 2026-04-03.
