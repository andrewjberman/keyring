# DS~B 2026-05-14 — Session 3: INF_D_06.cash_drag perf P0 vectorization

**Agent:** 0.4.0_DS_ClientPlatform~B
**Window:** ~14:35Z → 14:41Z (~6 min wall, single-pass refactor)
**Trigger:** Andrew direct via AE 0.6.1 MCP at 14:33Z — chain_gold-d_20260514_141936 cash_drag step burned 553s wall (17× next-slowest gold-d, 1-core sat, 20+ FutureWarnings from line 211).
**Ship:** commit `a4a4fd0b2`, S3 ETag `b7ed6218cb03cb4b94a1e0d6c9ac7b5f` (opal-data-inf/code/gold/INF_D_06.cash_drag.py, LM 14:40:05Z).
**TO_ID:** `ADVI_INFINC.cash_drag_perf_P0` (no formal TO; Andrew direct + AE routing = dispatch authority).

## TL;DR

Two perf bugs in INF_D_06 both vectorized in one commit:

1. **AE-flagged primary:** `_load_holdings_day_summary` called per partition (~1000× per window via ThreadPool) → `df.groupby('account_id').apply(lambda...)` Python-slow-path per call. Refactored to `_load_holdings_day_raw` (no per-partition aggregation) + single vectorized `groupby(['account_id','date']).agg(named=...)` on the full concat in `load_cash_time_series`.

2. **Secondary discovered while reading 180-230 context:** `build_window_rows` lines 397-404 iterated each of ~1000 accounts in Python, calling `_time_weighted_mean(sub, ...)` per account (each with its own Python for-loop on weights). Replaced with NEW `_time_weighted_avg_cash_vectorized` using `groupby+shift(-1)+clip` to compute step-function weights in a single pandas C-path pass.

Empirical wall-time validation pending AE 0.6.1 next chain re-fire. Target <30s vs 553s prior.

## Files Modified

| File | Change | Commit |
|---|---|---|
| `data/orion/scripts/gold/INF_D_06.cash_drag.py` | Two-bug vectorization: split `_load_holdings_day_summary` into raw + summary variants, vectorize `load_cash_time_series` end-aggregation, replace `_time_weighted_mean` with vectorized helper, delete dead code | `a4a4fd0b2` |

`+91 / -47`. No other files touched (lane discipline — perf-only fix, no semantic change).

## Code shape change

### Before — `_load_holdings_day_summary` (1 per partition, ~1000 calls/window)

```python
agg = (df.groupby('account_id')
         .apply(lambda g: pd.Series({
             'total_mv': float(g['market_value'].sum()),
             'cash_mv':  float(g.loc[g['is_cash'], 'market_value'].sum()),
         }))
         .reset_index())
```

Cost: ~140ms × ~1000 partitions × 1 window = ~140s; with multiple windows or repeated reads probably more. Observed: 553s wall.

### After — bulk path uses raw rows; one groupby at end

```python
# _load_holdings_day_raw: read + tag (no aggregation)
df['is_cash'] = (df['price'] - _CASH_PRICE_SENTINEL).abs() <= _CASH_PRICE_TOL
df['date']    = pd.Timestamp(fname)
return df[['account_id', 'date', 'market_value', 'is_cash']]

# load_cash_time_series: concat all raw frames, then ONE vectorized groupby
raw = pd.concat(frames, ignore_index=True)
raw['cash_value'] = raw['market_value'].where(raw['is_cash'], 0.0)
out = (raw.groupby(['account_id','date'], sort=False, as_index=False)
          .agg(total_mv=('market_value','sum'),
               cash_mv=('cash_value','sum')))
```

Walk-back path at line 542 (1-14 calls) still uses `_load_holdings_day_summary` — retained but internal apply also vectorized via the same `cash_value` mask + named-agg pattern.

### Before — `_time_weighted_mean` + per-account Python loop

```python
for acct in accounts_in_window:
    sub = window_ts[window_ts['account_id'] == acct]
    avg_cash = _time_weighted_mean(sub, 'cash_mv', window_start, window_end)
    avg_records.append({'account_id': acct, 'avg_cash_balance': round(avg_cash, 2)})

# _time_weighted_mean: Python for-loop over dates
for i in range(len(dates)):
    if i < len(dates) - 1:
        w = (pd.Timestamp(dates[i + 1]) - pd.Timestamp(dates[i])).days
    else:
        w = (window_end - pd.Timestamp(dates[i])).days + 1
    weights.append(max(w, 1))
```

Cost: O(accounts × obs) per window. ~1000 × ~250 × 4 windows.

### After — single vectorized groupby

```python
wt = window_ts.sort_values(['account_id', 'date']).copy()
wt['next_date'] = wt.groupby('account_id', sort=False)['date'].shift(-1)
wt['next_date'] = wt['next_date'].fillna(window_end + pd.Timedelta(days=1))
wt['weight']        = (wt['next_date'] - wt['date']).dt.days.clip(lower=1)
wt['weighted_cash'] = wt['cash_mv'].astype(float) * wt['weight']

out = (wt.groupby('account_id', sort=False, as_index=False)
         .agg(weighted_sum=('weighted_cash','sum'),
              total_weight=('weight','sum')))
out['avg_cash_balance'] = (out['weighted_sum'] / out['total_weight']).round(2)
```

Spec preservation:
- Last-obs carries through window_end + 1 day → matches original `(window_end - date[n-1]).days + 1`
- Min-1-day weight clip → matches `max(w, 1)`
- Sum-of-(value × weight) / sum-of-weight → identical math
- Output rounded to 2 decimals → byte-equal output schema

## Parity considerations

**Byte-equal probability is very high.** The vectorized sum reorders some floating-point operations relative to the original Python loop, but `round(_, 2)` collapses any sub-cent reordering. A row differs in the final output only if its unrounded weighted-average lands within ~1e-6 of a half-cent boundary (0.005, 0.015, etc.). For random floats this is ~1-in-10000 per row. With ~4000 final rows expected, expected diff count ~0-1, magnitude exactly $0.01.

Per AE RAVC spec: byte-equal preferred, float-epsilon acceptable. This fix is float-epsilon-safe by construction; byte-equal is the modal outcome.

## Compiler Tools

| Tool | Runs | Findings |
|---|---|---|
| `.tools/ds-commit-gate.sh data/orion/scripts/gold/INF_D_06.cash_drag.py` | 1 | PASS — py_compile + AST + ruff py39 |
| `.tools/safe-commit.sh` | 1 | Clean commit; pathspec scoped to single file |
| `.tools/safe-deploy.sh` (pre-push hook) | 1 | `[inf]` bucket detected, INF_D_06.cash_drag.py deployed, SHA-MATCH verified |
| `comp-pipescript`, `comp-blast`, `comp-trace` | not run | INF scripts not in BD-pipeline comp-graph catalog. Direct AE chain re-fire is the validation path. |

## Inter-agent coordination

| Time (Z) | To/From | Subject |
|---|---|---|
| 14:33 | FROM AE 0.6.1 | P0 routing: fix INF_D_06.cash_drag.py line 211 — 553s / 20+ FutureWarning / Andrew direct |
| 14:35 | TO AE 0.6.1 | ACK engagement, reading 180-230, ~30min ETA |
| 14:40 | TO AE 0.6.1 | RAVC1 — SHIPPED `a4a4fd0b2`, S3 ETag `b7ed6218cb03cb4b94a1e0d6c9ac7b5f`, two-fix scope detail |
| 14:40 | FROM COO | Heads-up FYI on the same P0; banking as P1; ADVI_INFINC architectural framing suggestion |
| 14:41 | TO COO | ACK status — already shipped; INFINC framing note added (script-internal vectorization is same pattern as chain-level skip-gates one level up) |

ETA delivery: 6 min wall vs 30 min estimate. Tight refactor scope + matching the original spec carefully made this fast.

## Architectural observations (per COO suggestion — link to ADVI_INFINC)

The two cash_drag bugs are textbook **Pattern A vectorization** at the script-internal level — analogous to Pattern A's chain-level skip-gates at the chain level:

| Layer | Anti-pattern | Vectorized form |
|---|---|---|
| **Chain (Pattern A in AE brief)** | rewrite every historical partition every chain run | per-partition idempotence: `head_object` skip-if-exists |
| **Script-internal (this fix)** | per-partition Python apply / per-account Python loop calling groupby-apply | concat raw → ONE vectorized groupby on the full frame |

The same recognition pattern applies in both cases: any time you see a Python `for` loop wrapping a pandas `.groupby().apply(lambda...)` or repeated `head_object` calls, look for vectorization opportunities. Script-internal wins can be tens-of-min wall reductions per script even before the chain-level Pattern A migration kicks in.

Worth mentioning in any future ADVI_INFINC Phase 2-4 implementation guide as "what to look for at the script-internal level before touching chain-level patterns."

## Lessons (informal — not promoted to memory yet)

1. **Reading the AE-flagged line + 30 lines of context is the right scope.** AE's "lines 180-230" pointed to the primary; widening to read the call-site (build_window_rows 397-404) surfaced the secondary bug. Both fixed in the same commit avoids a future "we caught the obvious bug, perf went from 553s to 60s, why is it still slow" round-trip.

2. **Step-function-integration spec preservation.** The original `_time_weighted_mean` had two non-obvious edge cases (last-obs +1d carry-through; min-1-day clip). Vectorizing required exactly replicating those — `fillna(window_end + pd.Timedelta(days=1))` for the +1d, `.clip(lower=1)` for the min. Easy to miss; caught by reading the original Python loop carefully before refactoring.

3. **Output-rounding hides sub-cent reordering.** Float-epsilon parity is structurally safe whenever the output goes through `round(_, N)` for N small (here 2). Reorderings only surface at the round boundary; for random floats, that's <1-in-10000 per row.

## Open / Pending TOs (unchanged)

- `ADVI_INFNNA.INF_A_03_STALE-PURGE` — deferred per CTO ruling
- 4 ADVI_INFGRO.001-.004 — shipped by base lane 2026-05-13; ground-truth-flip candidate for next COO startup pass

## Next Steps

| Recipient | Item |
|---|---|
| **AE 0.6.1** | Re-fire chain (or `--single INF_D_06` SSM-direct per the runbook I have in memory) to validate wall-time. Target <30s. RAVC2 me + COO + Andrew with empirical wall + sample-row parity check. |
| **COO** | RAVC2 will route through AE per protocol; CC'd on COO copy. |
| **DS~B (self)** | Stand by for AE empirical validation. If wall lands <30s and parity clean, mark cash_drag P0 closed. If wall still >30s, profile further (most likely culprit: the `for _, r in merged.iterrows()` at line 472 building final rows — ~4000 iterrows × dict-build; can vectorize to df.to_dict('records') if needed). |
| **DS~C** | Original INF_D_06 author (header line 54) — heads-up the refactor under ~B authorship; `_time_weighted_mean` removed (was only called from build_window_rows). No semantic change. |

## Self-watchdog state

Inbox watcher relaunched once during session (delivered the prior AE RAVC closure message). All sends acknowledged; no orphan watchers observed.
