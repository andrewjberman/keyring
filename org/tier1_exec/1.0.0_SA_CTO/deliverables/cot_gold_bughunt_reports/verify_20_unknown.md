# VERIFY #20 -- target: unknown

- is_real: **True**
- confidence: **confirmed**
- corrected_severity: high

## Reasoning
CONFIRMED. I traced a concrete triggering path end-to-end.

CALL SITE (generate_header_metrics, lines 2545-2548): build_cla_view is invoked with the RAW `ts, start_ts` calendar boundaries -- NOT the fallback-resolved `cp_start_date` that line 2518 (`cp_start_date = _cp_date_fallback.get(start_ts, start_ts)`) computes for the NNA views one call earlier. So the carefully-built nearest-prior-trading-day fallback is deliberately applied to cp_day (2460) and the NNA cp_start (2518-2519) but never threaded into CLA.

INSIDE build_cla_view (line 1689): `cp_start = client_perf[client_perf['date'] == start_ts]` filters on the raw boundary. `client_perf` here is `client_perf_filtered`, which (2408-2409) is `client_perf[date.isin(all_cp_dates)]`; `.isin` only KEEPS existing rows -- it never injects a row for a boundary date that isn't in the data. So when start_ts is a non-trading day, cp_start is empty even though the fallback row is present in the frame.

WRONG OUTPUT (1698-1705): `merged = cp_end.merge(cp_start, how='left')` then `merged['inflows_start'/'outflows_start'/'nna_start'].fillna(0)` -> `period_inflows = cum_inflows - 0`, `period_outflows = cum_outflows - 0`, `period_nna = nna - 0` = the entire cumulative-since-inception, not the one-period delta. No crash (the merge yields the columns all-NaN). These inflated values are aggregated into `nmnc/nmec.inflows/outflows/nna` (1765-1767, 1825-1834) and firm `totals` (1842-1844), placed in `views['cla']`, and served to `platinum/firm/partner_analytics_monthly.json` plus quarterly/annual (write_s3 line 2643; all three granularities run by default, main() line 2690).

NO SAFETY NET FOR THE FIRE CASE: the early return `if cp_end.empty` (1691) only protects periods whose END boundary is itself a non-trading day. The vulnerable configuration is end present + start absent. This occurs for (a) the current period, whose end = ref_date is always a real trading day (2369) while start = prior period-end can be a weekend; and (b) any trailing period landing on a trading day while its prior boundary is a weekend. Concretely RIGHT NOW (ref_date ~2026-07-06, monthly): the m1 period has end=2026-06-30 (Tuesday, present -> cp_end non-empty) and start=m2=2026-05-31 (Sunday, absent -> cp_start empty) -> that period's CLA inflows/outflows/nna are inflated to inception-to-06-30 cumulative. The flag's headline (current period, monthly) fires in any month whose prior month-end is a weekend (e.g. June 2026, start=2026-05-31 Sun). Period boundaries come from pure pd.Timestamp calendar arithmetic (get_periods 205-219, 295) with no snap-to-trading-day, and the author's own comment at 2393-2406 ("Period boundaries ... may not exist in the data if they fall on weekends/holidays") documents exactly this absence.

SECONDARY claim (NNA fallback donut, build_nna_geo_view 1361-1378 / build_nna_adv_view analog): also real but narrower -- those lines re-filter geo_ts/adv_ts on raw start_ts and only execute when `use_canonical` is False (canonical_nna absent/empty). The NNA DISTRIBUTION path is safe because it consumes the pre-resolved cp_start passed in. The flag correctly scopes this to "when canonical is absent."

SEVERITY: high, not critical. It is a silent, one-directional overstatement of a client-facing growth artifact (no crash, no chain abort), and for cot's short history the inflation is currently ~2-4x rather than the forward-looking "~100x" the flag cites (that upper bound only materializes as history lengthens). Confirmed real, materially wrong served number, fires on real data today.
