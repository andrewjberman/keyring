# ADVI_INFNNA.P2.P0 — Continuous-GEO NNA flow-loss mechanism (DS investigation)

**Author:** 0.4.0_DS_ClientPlatform (DS) — Andrew-direct 3rd Inflection PRD
**Date:** 2026-06-02
**Type:** READ-ONLY investigation (parquet + producer archaeology + same-window diff). NO emit/data change.
**Gates:** W1 canonical-GEO emit spec (straight re-aggregation vs definitional-reconcile-first)
**Evidence base:** CVO analysis `7668bae52`; PRD `docs/architecture/ADVI_INFNNA_P2.md`

---

## VERDICT

**The continuous-GEO NNA undercount is mechanism (a): weekly-snapshot-SAMPLING loss — a pure stock/flow-sampling artifact, the SAME class as the F5 ADV bug. It is NOT a definitional difference.**

Therefore **W1 is a STRAIGHT re-aggregation** of `canonical_nna` by state/city, summing `net_nna` over **all** dates in each window (no weekly sampling), window-explicit per the F5 vocabulary. **No definitional reconciliation is required** before the canonical GEO emit.

---

## Line-level evidence

### Both producers read the SAME source with the SAME definition
- `INF_D_00d.cumulative_chart.py` (`nna_geo`/`nna_adv`) and `INF_D_00f.advisor_nna_canonical.py` (F5) **both** load `s3://opal-data-inf/gold/canonical/canonical_nna_*.parquet` (account×date) and use the **same** column `net_nna` (= `daily_inflow − daily_outflow`, external client flows). No fee-view, transaction-class, or population scoping divergence in the source — identical parquet, identical column.
- F5 canonical method (`INF_D_00f` docstring L23-26, `_agg_leaf` L290-292): `NNA(window) = sum over [window_start, window_end] of net_nna` — summed over **every** active date. `inflows = sum(daily_inflow)`, `outflows = sum(daily_outflow)`.
- `INF_D_00f` docstring L340-343 verbatim: *"Contrast INF_D_00d.build_nna_adv_view which weekly-SAMPLES."* The F5 author already identified the weekly-sample as the divergence — F5 was written to bypass it for ADV-L1, but GEO + all drill leaves still read `INF_D_00d`.

### The single transform difference = `_weekly_sample`
`INF_D_00d.build_nna_geo_view` (L450-459) computes **daily** per-(date,state) `net_nna`, then:
```python
sampled_dates = _weekly_sample(daily['date'])      # L458 — keep ~1 date per 7
daily = daily[daily['date'].isin(sampled_dates)]   # L459 — DROP the other ~6/7 days of flow
```
`net_nna` is a **daily FLOW** (not a stock). Sub-sampling to weekly dates and summing the kept single-day flows discards all flow on the ~6 non-sampled days per week. (`build_nna_adv_view` L506-507 is identical — hence `nna_geo` and `nna_adv` totals are byte-identical.)

### Empirical reproduction (read live S3 today, 2026-06-02)
Firm YTD net_nna over the canonical_nna source, two ways:

| Method | Firm YTD net_nna | vs canonical |
|---|---|---|
| **(i) FULL daily sum** (F5 canonical) | **$4,225,486.45** | = canonical firm YTD **to-the-cent** |
| **(ii) served `cumulative_chart.nna_geo` YTD** (weekly) | **$1,456,681.11** | **34.5%** (65.5% loss) |
| served `cumulative_chart.nna_adv` YTD (weekly) | $1,456,681.11 | byte-identical to nna_geo |

- (i) reproduces the canonical firm YTD ($4,225,486.45) exactly → confirms the canonical_nna full daily sum IS the canonical number, same definition.
- (ii) reproduces the PRD/CVO-reported served undercount ($1,456,681) exactly. The served weekly grid keeps **22 of 102** active YTD dates.
- FE strips `'Other'` (top-8-state display), so the on-screen top-state total is even lower ($1,211,999.57); the $1,456,681 includes the 'Other' bucket.
- Scripts: `.runtmp/infnna_p0_flowloss_probe.py` (full-vs-weekly), `.runtmp/infnna_p0_faithful_repro.py` (served-artifact YTD sum).

**Conclusion:** identical source + identical `net_nna` definition; the entire 65.5% gap is the `_weekly_sample` daily-flow drop. Mechanism (a), confirmed to-the-cent.

---

## W1 emit-spec determination (correct-by-construction)

1. **Straight re-aggregation — no definitional reconcile.** Canonical GEO State(L1)/City(L2) NNA = `groupby([state|city, window]).net_nna.sum()` over **all** dates (mirror `_agg_leaf`: also emit `inflows = sum(daily_inflow)`, `outflows = sum(daily_outflow)`). No `_weekly_sample`, no top-N truncation in the canonical emit (the canonical spine carries all states; FE may still top-N for display, but the canonical artifact must be complete so `sum(states) == firm` to-the-cent).
2. **State/city source.** `canonical_nna.parquet` columns are `[account_id, advisor_key, custodian, daily_inflow, daily_outflow, date, n_inflow_events, n_outflow_events, net_nna, rep_bucket]` — **it does NOT carry state/city.** W1 joins `account_id → state/city` via `accounts_v2` / `household_dim` (the **same** join `INF_D_00d` already uses, L437-446 / L327-335; and the F5 `account_id → household_id` dim join). The geo data exists and joins cleanly today — the lossy producer already renders states; W1 changes only the aggregation (full daily sum, not weekly).
3. **Per-client leaves (ADV→client L2).** Same pattern: `groupby([advisor_key, account_id|household_id, window]).net_nna.sum()` so `sum(clients under advisor) == advisor canonical NNA`. (Account→household via the F5 accounts dim.)
4. **Window-explicit (F5 lesson).** Emit over the unified F5 window vocab (QTD/YTD/MAX/1Y/3Y/q-strip) so no GEO surface renders a window-mismatched number.
5. **Shape (DS+CTO).** Prefer folding geo+client into the F5 artifact (`advisor_nna_canonical.json` → `nna_canonical.json`, dims {adv, geo, client}) for a single canonical source-of-truth, matching F5's intent; DS to assess emit cost vs a sibling artifact.

### Notes for downstream
- **W5(c) auto-resolves:** "continuous 8 states vs snapshot 14" is a top-N artifact of `INF_D_00d` (TOP_N_STATES=8, rest→'Other'); a complete canonical GEO emit from the full account×date source carries all states → coverage parity falls out of W1.
- **MAX-window 7.5% is window-confounded** (cumulative_chart 2024-06+ only vs canonical all-history incl pre-2024 Merge-In) — the fair number is the same-window YTD 34.5%, confirmed above. W1's window-explicit vocab eliminates this confound.
- **Mandatory served-verify** on the W1 emit (served artifact, not just partition) per `feedback_partition_verify_neq_serving_verify`.

---

## AC-P0 status: MET
- [x] Mechanism documented (weekly-snapshot-sampling, line-level: `INF_D_00d:458-459`) with empirical evidence reproducing both the canonical ($4,225,486.45) and served-undercount ($1,456,681.11) numbers to-the-cent.
- [x] `canonical_nna.parquet` state/city presence empirically confirmed: **absent from the parquet**; sourced via the existing `account_id→state/city` join (`accounts_v2`/`household_dim`).
- [x] W1 emit-spec determination: **straight re-aggregation** (no definitional reconcile), full daily sum, window-explicit.
