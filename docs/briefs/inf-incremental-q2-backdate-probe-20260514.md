# INF Incremental Pipeline Q2 — Empirical Orion Backdate Distribution

**Author:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-14
**Probe scope:** ADVI_INFINC.Q2 — validate 90-day trailing window for incremental Pattern E (PULL_TXN / PULL_PERF)
**Reference design brief:** `docs/briefs/inf-incremental-pipeline-design-20260514.md` §2.5, §6.2 (commit `2920719f8`)
**Audience:** 2.0.0_SA_COO, 0.6.1_AE_PartnerETL

---

## TL;DR

**90-day trailing window is empirically safe with 25 days of margin.** Across 200,811 Inflection transactions over the 7-month window 2025-09-08 → 2026-05-13 (~179 silver partitions), the maximum observed Orion `created_date - trans_date` lag is **65 days**. Zero transactions in the empirical record exceed 90 days. The recommendation in design brief §6.2 holds: **90d trailing window + weekly Sunday full-pull** is the right belt-and-suspenders configuration.

---

## Method

**Signal source:** `silver/transactions/{date}.parquet` (old-schema partitions, pre ADVI_DWSPLT.002 2026-05-13 ship), each containing the rows newly written by the old daily-delta silver writer for that pull-date.

**Lag computation:** `lag_days = (created_date - trans_date).dt.days`, where:

- `created_date` — Orion-side timestamp for when Orion booked the row (datetime64[ns], `0` nulls observed in 7-month sample).
- `trans_date` — the calendar date of the actual transaction (date, ~9% null on cash/admin rows; those rows excluded from lag analysis since "trans date" doesn't apply).

`created_date` is the canonical empirical signal for "when did Orion become aware of this transaction" and is the correct measure for incremental-pull window design. `snapshot_date` (when WE pulled) is a different and not-relevant signal — we control that cadence.

**Scope:** Last 180 partitions of `silver/transactions/`. One partition (`2026-05-14`) skipped — that's the new-schema bronze-passthrough post DWSPLT.002 which doesn't retain `created_date` (the column was dropped in the new puller's `CONFIRMED_FIELDS` set). 179 of 180 partitions analyzed.

**Validation against alternate signal:** Bronze delta computation (compare `bronze/transactions/2026-05-12.parquet` ids vs `2026-05-14.parquet` ids → "new in 2 days" → lag = pull_date - transDate) gave 41,949 rows with 100% lag ≤ 1 day, 0% > 90d. Consistent with silver result; weaker sample (2-day window) but no contradiction.

---

## Results

**Sample:** n = 200,811 (`trans_date` + `created_date` both non-null)
**Time range:** trans_date 2025-09-08 → 2026-05-08; created_date 2025-09-09 → 2026-05-14

### Distribution

| Lag bucket | Count | % | Cumulative % |
|---|---:|---:|---:|
| NEGATIVE (future-dated trans_date) | 16 | 0.0080% | 0.0080% |
| 0d (same-day book) | 1,669 | 0.8311% | 0.8391% |
| 1-7d (overnight Orion batch) | 199,066 | 99.1310% | 99.9701% |
| 8-30d | 2 | 0.0010% | 99.9711% |
| 31-60d | 1 | 0.0005% | 99.9716% |
| 61-90d | 57 | 0.0284% | 100.0000% |
| **91-180d** | **0** | **0.0000%** | **100.0000%** |
| **181-365d** | **0** | **0.0000%** | **100.0000%** |
| **>365d** | **0** | **0.0000%** | **100.0000%** |

### Percentiles

| Percentile | Lag (days) |
|---|---:|
| P50 | 1 |
| P75 | 1 |
| P90 | 2 |
| P95 | 2 |
| P99 | 4 |
| P99.5 | 4 |
| P99.9 | 4 |
| P99.99 | 63 |
| max | **65** |

### Long-tail characterization (31-90d, n=58)

Dominated by **`Cancel Account` events** (57 of 58 rows) — Orion booking bulk account-closure reversal entries with original trans_date but ~2 month later created_date:

- 41 rows at 63d lag (trans_date 2025-10-15, created 2025-12-17 — one client account closure)
- 16 rows at 65d lag (trans_date 2025-12-01, created 2026-02-04 — one client account closure)
- 1 Tax Credit at 56d lag

These are not steady-state backdate corrections — they are deferred account-closure reversal events that Orion books in batches once an Inflection-side workflow completes. They are the largest legitimate-correction lag in the empirical record.

### Negative-lag (future-dated trans_date) characterization (n=16)

- 11 Management Fee (scheduled quarterly billings booked at start-of-quarter for end-of-quarter trans_date)
- 2 Buy Exchange / 2 Sell Exchange (T+1/T+2 settlement-date trades)
- 1 Fee Credit

These are NOT a 90d window concern — a trans-date-windowed query catches them whenever their trans_date arrives, regardless of how early Orion books them.

---

## Recommendation

**Lock 90d as the trailing window for PULL_TXN / PULL_PERF Pattern E.**

Empirical max lag is 65 days; 90d provides 25 days of margin against future variance.

**Keep the weekly Sunday full-pull from design brief §6.2** as the belt-and-suspenders mitigation. Empirically zero transactions in 7 months crossed 90d, but:

1. Sample size for 91-180d bucket is exactly 0 — we cannot statistically distinguish "never happens" from "happens at <0.0005% rate." A weekly catch-up at <2 minutes is cheap insurance.
2. New Inflection workflows (e.g., year-end tax reclassification, multi-quarter fee true-ups) could plausibly produce >90d lag without prior empirical signal — these would be silently dropped under a pure 90d-windowed pull.
3. The Sunday full-pull (~16 min) restores full snapshot integrity once weekly, bounding the worst-case data-age to 7 days regardless of edge cases.

**Window-size sensitivity:** Even a 30-day window would capture 99.97% of empirical events; 90d is generous. Net cost of 90d vs 30d is the same incremental-pull design (just a wider date filter); no operational reason to tighten below 90d for marginal API cost savings.

---

## Excluded scope

- Performance pull (`PULL_PERF`) — analyzed only transactions silver here. AE may want a parallel probe on `silver/performance` partitions if they have an analogous `created_date` field; ping me and I'll run the same shape.
- Schema-divergent partitions: 1 partition skipped (`2026-05-14` new bronze-passthrough silver without `created_date`). Post DWSPLT.002, AE may want to re-add `created_date` to the bronze schema so this probe can be re-run on future data; flagging as ADHC_INFINC candidate.
- Total silver retention is 1,514 partitions back to 2020-05-26 — analyzed last 180 for current Orion behavior. If multi-year drift analysis is desired, expand the window; cost is ~1 GB load.

---

## Reproducibility

Probe is one-shot inline-Python invoking the AWS SDK; no committed probe script. Method written into this brief for re-run if needed:

```python
# Load last 180 silver/transactions partitions; filter old-schema (with created_date);
# compute lag = (created_date - trans_date).dt.days; histogram + percentile.
# ~30s wall time end-to-end.
```

Compiler-tools context updated: `SERIAL=0.4.0_DS_ClientPlatform~B; TO_ID=ADVI_INFINC.Q2_probe`.
