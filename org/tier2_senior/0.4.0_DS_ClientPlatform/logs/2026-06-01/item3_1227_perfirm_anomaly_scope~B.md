# Item-3: 12/27/2025 per-firm anomaly — SCOPE/ROOT-CAUSE (DS~B, 2026-06-01)
Scope-first per COO (no fix executed). Andrew per-firm visual review (4bb7a0ecc). DS-CP data-side lead. RAVC2 COO+CTO. CVO sole verify-writer.

## Symptom (Andrew)
12/27/2025: INF total -> $0 (full single-date dropout, every cohort $0); 49F model breakdown collapses (UltraShort ~$1.118B, all other models $0, Non-Model ~$223M); GLOBAL unaffected.

## ROOT CAUSE: spurious WEEKEND partition (12/27/2025 = Saturday)
12/27/2025 is a **SATURDAY**. Empirical:
- It is the **ONLY Saturday partition** in the platinum series. Surrounding partitions: 12/26 (Fri) ✓, **12/27 (Sat) — spurious**, 12/29 (Mon) ✓.
- It is the **ONLY INF null-model date in the entire 402-date series** (INF model=sma=non_model=None at 12/27; weekday-dist of INF nulls = {Sat:1}).
- Year-end also has a GAP: **12/30 (Tue) + 12/31 (Wed) business-day partitions are MISSING** (series jumps 12/29 -> 2026-01-05).

So the year-end 2025 backfill date-selection both INCLUDED a spurious Saturday (12/27) AND DROPPED business days (12/30, 12/31). The spurious 12/27 weekend partition carries degenerate data:
- 49F: by_model collapsed to **1 entry** (Ultra Short-Term $1,107,162,810; model_aua TOTAL ~right but the 5-model breakdown is gone — 12/26 correctly has by_model_n=5: LTC $469M/INT $251M/LTA $188M/ST $80M/UST $76M). So the per-firm donut/stack shows one model.
- INF: fully null (no weekend INF data).
- GLOBAL: the headline opal_aggregate_aua still computed a plausible total ($1,335,896,131) -> "looks unaffected" (it's the per-firm DECOMPOSITION + INF slice that broke, not the global total).

=> This is a DATE-SELECTION / EMIT bug (a weekend leaked into the emitted partitions; year-end business days dropped), NOT a methodology issue. Confined to the 12/27/2025 partition + the 12/30-12/31 gap.

## FIX OPTIONS (scope only — NOT executed)
1. Remove the spurious 12/27/2025 (Sat) partition + (if recoverable) backfill the missing 12/30 + 12/31 business days, then re-run the rollup so the FE series drops the spurious 12/27 point + fills the gap.
2. COORDINATION NOTE: this likely FOLDS INTO the Andrew full-history Schwab re-derive (CTO PRD pending) — if that re-derive re-emits the entire 49F series with correct BUSINESS-DAY selection (weekday + holiday-aware), it would naturally drop the spurious 12/27 Saturday + emit the correct 12/30/12/31. Recommend the CTO PRD's date-selection explicitly exclude weekends + use a trading-calendar so this class can't recur. So Item-3 may not need a standalone fix if the re-derive subsumes it — flag for CTO to fold the business-day-selection requirement into the PRD.

## Recommendation
Confirm with CTO whether to (a) fix Item-3 standalone now (delete 12/27 + backfill 12/30-31 + rollup) or (b) fold it into the full-history Schwab re-derive's business-day-selection. Given the re-derive re-emits the whole series anyway, (b) is likely cleaner (one coherent re-emit with correct date selection) — but if Andrew wants the visible 12/27 glitch gone before the PRD lands, (a) is a quick targeted fix. No fix executed pending the call.
