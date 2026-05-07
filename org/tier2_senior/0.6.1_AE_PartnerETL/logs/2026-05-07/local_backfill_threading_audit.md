# Session Log: Local Backfill Threading Audit + 24h Hold Decision

**Agent:** 0.6.1_AE_PartnerETL
**Date:** 2026-05-07
**Session window:** ~19:05Z – 19:25Z
**Branch:** CLOUD

---

## Summary

Per Andrew direction, audited the four locally-running Python backfill processes (billing, tax+perf, assets_v2, positions_daily) for threading adequacy and live progress. Confirmed all four are running on Andrew's local machine (paths in logs: `C:\Users\AndrewBerman\Desktop\ajb_workspace\...`). Threading varies by stream — billing/tax adequate, assets_v2 + positions_daily strictly single-threaded. All four advancing; no intervention. Decision: leave Andrew's device running for next ~24h to let streams complete naturally.

---

## 1. Process Inventory

Four Python processes confirmed running via `ps -ef | grep python`:

| PID | Stream | Command |
|---|---|---|
| 109299 | tax + performance | `python .runtmp/local_wavec1_backfill.py --from 2020-03-11 --to 2026-05-05 --workers 16` |
| 109316 | billing | `python .runtmp/local_full_backfill.py --from 2020-03-11 --to 2026-05-05 --workers 8 --dims billing` |
| 109331 | assets_v2 | `python data/orion/manual_api/pull_inflection_assets_v2.py --upload-bronze --start 2020-03-11 --end 2026-05-05` |
| 109343 | positions_daily | `python data/orion/manual_api/pull_inflection_positions_daily.py --upload-bronze --start 2020-03-11 --end 2026-05-05` |

All started ~13:51Z (5h+ runtime at audit time).

---

## 2. Threading Audit

| Process | Workers | Threading model | Adequate? |
|---|---|---|---|
| billing (`local_full_backfill.py`) | `--workers 8` | `ThreadPoolExecutor` over (dim, date) pairs; each worker spawns subprocess of `orion_billing_dim.py` | OK |
| tax + performance (`local_wavec1_backfill.py`) | `--workers 16` | `ThreadPoolExecutor` over dates; each worker runs tax → perf **sequentially** within date | OK on workers; tax/perf serialized within each date (could halve time by parallelizing) |
| assets_v2 (`pull_inflection_assets_v2.py`) | none | Plain `for date in dates: for cid in client_ids:` — strictly sequential, AdaptiveRateLimiter throttles | **NOT MULTITHREADED** |
| positions_daily (`pull_inflection_positions_daily.py`) | none | Same as assets_v2 — sequential dates × sequential 310 clients | **NOT MULTITHREADED** |

---

## 3. Live Performance from Logs

Captured at ~19:10Z:

| Stream | Latest record | Rate | ETA |
|---|---|---|---|
| billing | 720/2,241 (32%) | 0.17–0.20/s | ~150 min (2.5h) |
| tax+perf | 614/2,247 (27%) | 0.14–0.15/s | ~190 min (3.2h) |
| assets_v2 | date 2,177/2,247 (97%) | ~415s/date | ~8h (70 dates left) |
| positions_daily | date 2,180/2,247 (97%) | ~395s/date | ~7.4h (67 dates left) |

S3 partition counts (live):
- `bronze/orion-api/{date}/billing.csv`: 768
- `bronze/orion-api/{date}/tax_unrealized.csv`: 729
- `bronze/orion-api/{date}/tax_realized.csv`: 715
- `bronze/assets/{date}.parquet`: ~2,175 (silver/api_dims/assets_v2 not auto-built)
- `bronze/positions/{date}.parquet`: ~2,178 (silver/api_dims/positions_mv has 2,173)

---

## 4. Bugs / Concerns

### 4.1 — `local_wavec1_backfill.py:42-54` skip-check filename mismatch

`date_complete()` checks for `performance.csv`, but `pull_inflection_performance_dim.py` writes `performance_dim.csv`. As coded, the resume check never short-circuits a completed date. If this process restarts, it would wastefully re-pull every previously-done date. Right now the streams are running fresh through, so the bug is invisible; if a restart is needed, the script needs a one-line fix:

```python
# WRONG (current)
keys = [
    f"{PREFIX}/{date_iso}/tax_unrealized.csv",
    f"{PREFIX}/{date_iso}/tax_realized.csv",
    f"{PREFIX}/{date_iso}/performance.csv",
]
# RIGHT
keys = [
    f"{PREFIX}/{date_iso}/tax_unrealized.csv",
    f"{PREFIX}/{date_iso}/tax_realized.csv",
    f"{PREFIX}/{date_iso}/performance_dim.csv",
]
```

**Impact during this run:** none (no restart yet). **Impact on restart:** ~3h wasted re-pulling dates already done.

### 4.2 — billing subprocess timeouts ~1%

7 of 720 billing dates failed with elapsed ≈ 304–305s, indicating the Envision ExcelReport endpoint occasionally hangs near the script's 300s subprocess timeout. Visible in log: `2021-10-13 fail elapsed=305.1s`, `2021-12-13 fail elapsed=303.6s`, `2022-01-18 fail elapsed=304.4s`, etc. Failures are isolated dates, not systemic. Plan: collect the failed-date list when the run ends; retry those targeted dates in a follow-up dispatch.

### 4.3 — assets_v2 + positions_daily are single-threaded

The most significant inefficiency, but at 97% done it is now an "ETA pain" not a structural fix. For future runs: each script should wrap its inner client loop in a `ThreadPoolExecutor` over `client_ids` — the Orion REST endpoint empirically tolerates 30–50 RPS per the [project_inflec_orion_rest_rate_ceiling.md](memory/project_inflec_orion_rest_rate_ceiling.md) memory.

---

## 5. Decision: 24h Hold

Per Andrew 2026-05-07 ~19:25Z: leave device running for ~24h. All four streams complete on their own:
- billing + tax+perf finish in ~3–3.2h (well before 24h).
- assets_v2 + positions_daily finish in ~7–8h (also well within 24h).

**No intervention.** Interrupting now to thread assets_v2/positions_daily would discard 97% progress.

**Watch items overnight:**
1. inf-api-txn first T-1 cron fire 2026-05-08T13:00Z (~17.5h from now). RAVC11 to COO after empirical confirmation.
2. Stream-end cleanup: when each stream ends (especially billing/tax+perf in ~3h), capture the failed-date list for follow-up retry (Wave C-style targeted dispatch).
3. Silver chain for billing/tax bronze dates is NOT auto-firing — DS~A monitors armed for that handoff.

---

## 6. Cross-Domain Notes

- **DS~A**: monitors armed for billing/tax bronze stream completion; will fire silver builders.
- **AE 0.7**: parallel work on GOLD-EVENT-TRIGGER Lambda; not affected by these streams.
- **DS~B**: implementing INFETL.003 inf-portal-publisher; downstream of full bronze→silver→gold completion.
- **DS~C**: INFETL.004 impl complete, blocked on AE 0.7 owned-paths gate.

---

## 7. Open Items (Carry to Next Session)

1. **inf-api-txn cron fire 2026-05-08T13:00Z** — RAVC11 with empirical (snap_date, row count, bronze/silver paths).
2. **Stream-end retry sweep** — once billing + tax+perf finish, harvest fail-date lists from `.runtmp/logs/full_backfill_*.log`, build a focused Wave C-style retry script.
3. **`local_wavec1_backfill.py` skip-check fix** — one-line rename `performance.csv` → `performance_dim.csv` if a restart is ever needed.
4. **assets_v2 / positions_daily threading enhancement** — defer until next backfill is contemplated; not retrofit during this run.
5. **LAMBDA-DIMS sub-TOs from AE 0.7** — standing by for code-author work.
