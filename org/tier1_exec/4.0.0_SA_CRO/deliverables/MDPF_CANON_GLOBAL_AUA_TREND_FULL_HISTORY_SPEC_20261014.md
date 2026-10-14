# /portfolios Global AUA Trend: the break-out over full history (2024-11-01 to date)

**archetype:** EXPLORE

From `4.0.0_SA_CRO~DELL1` to `1.0.0_SA_CTO~DELL1`, on msg 5830. Andrew's record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_201xZ_PORTFOLIOS_SMOKE_TREND_FULL_HISTORY_COTTONWOOD_SPEC.md`
@caf5dc7d73. All reads were made on 2026-10-14 at ~20:2xZ against the served objects named below. Read-only.

## RULED 2026-10-14 ~20:4xZ: Variant 1 (Andrew-direct)

> "Call 3, only opal staff see global, that is correct. therefore your assessment is correct with rec a, that is the
> easiest stitch."

Record: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_204xZ_MDPF_GLOBAL_TREND_VARIANT_1_AND_SATELLITE_GLD_RETURNS.md`.
Build Variant 1. Variant 2 below is retired.

## Verdict: DOABLE from served data, with no new pull

With the rule below, the Trend groups **partition the Global total exactly on every one of the 487 dates that carry a
total (max |sum - total| = $0.00)**, from 2024-11-01. No group goes negative. Andrew's lead is right, to the cent: Client
Supervised is 49 Financial's former "Other AUA", less the two ETF SMA carve-outs.

**One decision is his and is not mine to take.** Before 2026-05-15, Global contains ONE firm (49 Financial). Breaking
those dates out by model shows 49 Financial's own book under the Global label. That is exactly what the CTO's fe9b
ruling (A) folded away (`CTO_RULING_DELL1_FE9B_MDPF_CANON_X2_GLOBAL_FOLD_A_20261012.md`: X2 was granted as "aggregate
counts only"). The same applies from 2026-05-15 to 07-19 for the Custom line, which is Inflection's blends alone.
Variant 1 below needs Andrew's word that Global may show single-firm lines on those dates. Variant 2 needs nothing and
still gives a full history, with a coarser split before 05-15.

## Why the chart looks as it does today (measured)

Served object: `s3://opal-data-assets/portal/gold/mdpf/global/aggregate-aua-timeseries/2026-10-13.json` (producer
`mdpf-gold-lambda (mdpf_gold_consolidator)`, 487 dated rows of 496 carry a total).

1. `model_aua`, `non_model_aua` and `opal_aggregate_aua` run from **2024-11-01** ($436.8M, $358.5M and $795.4M).
2. `by_model` per-model values start on **2026-05-15** only, because of the fold (`meta.by_model_fold`: "Per-model
   lines are shown on a date only where at least 2 firms hold the model; per-model detail begins 2026-05-15, the first
   date Global combined 2 firms"; code `data/mdpf/scripts/gold/mdpf_gold_consolidator.py:2089`
   `apply_global_min_firms_fold`, min_firms 2).
3. So before 05-15 the candidate (`cand/dell1/mdpf-canon-aua-trend-groups-repair` @fd5433a3) draws only `non_model_aua`
   as grey "Other AUA" (about $250M to $360M). It omits the $437M to $1.35B of model AUA it cannot break out, and the
   total appears to jump about 5x at 05-15. **The jump is a drawing artefact, not data.** The real total moves from
   $1,642.6M (05-14) to $1,719.0M (05-15).
4. The Client chips come from category-views, served only from 2026-08-27 (22 objects), and the candidate draws them only
   on the object's own as-of date (`trendGrouping.ts` `clientChipAt`).

## The identities (measured on every dated row)

- Global `non_model_aua` = 49 Financial `non_model_aua`, every date. Inflection's non-model (`inflection_non_model_aua`,
  $152M to $204M before 05-15 and $60M now) is outside the Global total.
- Global `model_aua` = 49F `model_aua` + Inflection `model_aua` + Cottonwood `model_aua`, every date. Before 05-15,
  Inflection and Cottonwood are 0, so Global = 49F.
- **Client - Opal Supervised = `non_model_aua` - `opal_div_sma` - `opal_growth_sma`.** It is exact to the cent on the
  three same-vintage category-views dates (2026-08-27, 09-25, 10-13; 10-13: 313,383,701.40 - 17,143,856.33 -
  3,975,550.24 = 292,264,294.83). On the other 19 it differs by $0 to $0.30M (at most 0.11%, on 10-05). The cause is the
  aggregate restating history after each category-views object was cut, not a different definition.
- **Client - Opal Unsupervised = 0** on all 22 category-views dates (to the cent).
- **ETF Strategies = `opal_div_sma` + `opal_growth_sma` + `sma_additive_aua`** (PFDE, $0.41M from 2026-10-08 in the
  chips; `sma_additive_aua` from 2026-08-26). Exact on all 22 dates.
- **ALT Strategies = `tax_additive_aua`** (Tax-Managed SMA, from 2026-09-30; the Muni SMA member serves null). Exact on
  all 22 dates.

## The rule, per group

All sources are in `opal-data-assets/portal/gold/mdpf/`. "G" = `global/aggregate-aua-timeseries`; "F" =
`49financial/aggregate-aua-timeseries`.

| Group | Dates | Source | Claim |
|---|---|---|---|
| UST, ST, INT, LT, ULT (each its own line) | 2024-11-01 .. 2026-05-14 | F `by_model.<model>.model_value` (49F is the whole of Global on these dates: G `model_aua` = F `model_aua`, diff 0.00 on every row). UST's first value is 2025-01-16; before that it draws nothing, never back-filled. | measured; **Variant 1 only** |
| same | 2026-05-15 .. as-of | G `by_model.<model>.model_value` | measured |
| Custom Models | 2024-11-01 .. 2026-05-14 | none: G `model_aua` - sum of the five = 0.00 on every row | measured zero, drawn as nothing |
| Custom Models | 2026-05-15 .. as-of | **G `model_aua` - sum of the five primary lines**, a difference of served fields. It runs $26.1M (05-19) to $69.2M (10-13) and is never negative. It replaces `other_models`, which the fold suppresses wherever its pool is held by one firm (05-15 .. 07-19: Inflection's blends alone). | measured (residual); 05-15 .. 07-19 is single-firm: **Variant 1 only** |
| Client Supervised | 2024-11-01 .. as-of | G `non_model_aua` - G `opal_div_sma` - G `opal_growth_sma` (carve-outs 0 before 2026-05-18) | measured (difference) |
| Client Unsupervised | 2026-08-27 .. as-of | category-views: 0 | measured 0; draw nothing. Before 08-27 there is no served split; held 0. |
| ETF Strategies | 2026-05-18 .. as-of | G `opal_div_sma` + `opal_growth_sma` + `sma_additive_aua` | measured |
| ETF Strategies | before 2026-05-18 | not separable from served data: the carve-outs begin 05-18, and before that the same assets sit inside 49F non-model, so inside Client Supervised | held: nothing drawn. A visible transfer of about $24.9M from Client Supervised to ETF happens on 05-18; footnote it. |
| ALT Strategies | 2026-09-30 .. as-of | G `tax_additive_aua` | measured; nothing before (the additive channel begins that day) |
| Other AUA | all dates | `non_model_aua` - carve-outs - Client = 0 by the identity above | **retire the group**: on this page it IS Client Supervised |
| Total (the stack top) | all dates | G `opal_aggregate_aua` | measured; the groups sum to it exactly |

**Roll-forward (Andrew: "if we are missing totals on any given day, just roll forward last known values"):**
- 9 dated rows carry no total: 2026-05-30, 05-31, 06-06, 06-07, 06-13, 06-14, 06-19, 06-20, 06-21. Every partner reads
  `absent` there.
- On such a row, each group takes its last known value, with point class `carried` (claim: held). The same applies to
  any single group's null on a row that has a total.
- Roll FORWARD only: never before a group's first value. UST before 2025-01-16, ETF before 05-18 and ALT before 09-30 are
  not gaps.
- Cottonwood's 2026-05-28 .. 07-19 values are served as `interpolated_estimate`; keep that class and its marking.
- The served `point_class` vocabulary already has `carried`, so the producer can emit it.

**Two real composition steps stay** (footnote them; they are not drawing errors):
- 2026-05-15: Inflection's models enter Global (+$93.6M), because Inflection's earlier assets were never in the Global
  total.
- 2026-05-28: Cottonwood enters, interpolated until 07-20.

## Variant 2 (no single-firm line; no new sign-off)

- Before 2026-05-15, draw **one "Models" band** (G `model_aua`) and Client Supervised; per-model lines begin 05-15.
- 05-15 .. 07-19: Custom is suppressed as now. The stack then falls $26M to $39M short of the total on those rows; draw
  the total line and footnote "models held at one firm are in the total and not broken out".
- Everything else as above.

## Oracle: period-end values, $M (Variant 1; the last dated row on or before the period end)

| period end | UST | ST | INT | LT | ULT | Custom | Client Sup. | ETF | ALT | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| 2024-12-31 | 0.0 | 64.3 | 182.4 | 118.6 | 146.6 | 0.0 | 362.6 | 0.0 | 0.0 | 874.6 |
| 2025-03-31 | 72.7 | 68.4 | 201.5 | 192.8 | 152.8 | 0.0 | 288.9 | 0.0 | 0.0 | 977.0 |
| 2025-06-30 | 59.9 | 69.9 | 225.6 | 279.4 | 182.8 | 0.0 | 251.5 | 0.0 | 0.0 | 1069.1 |
| 2025-09-30 | 51.6 | 76.6 | 246.2 | 361.4 | 189.0 | 0.0 | 259.3 | 0.0 | 0.0 | 1184.0 |
| 2025-12-31 | 55.6 | 80.1 | 257.1 | 506.0 | 191.0 | 0.0 | 291.0 | 0.0 | 0.0 | 1380.8 |
| 2026-03-31 | 58.7 | 93.4 | 262.3 | 600.0 | 189.1 | 0.0 | 274.4 | 0.0 | 0.0 | 1477.9 |
| 2026-06-30 | 48.4 | 111.3 | 365.1 | 755.8 | 204.1 | 34.3 | 228.6 | 23.1 | 0.0 | 1770.6 |
| 2026-09-30 | 68.4 | 131.9 | 451.6 | 872.9 | 205.6 | 66.9 | 266.6 | 21.2 | 24.8 | 2109.9 |
| 2026-10-13 | 70.0 | 138.3 | 456.7 | 888.5 | 211.3 | 69.2 | 292.3 | 21.5 | 29.2 | 2177.1 |

Model keys: UST `opal_ultra_short_term`, ST `opal_short_term`, INT `opal_intermediate`, LT `opal_long_term_conservative`,
ULT `opal_long_term_aggressive` (the served display names). Each row's groups sum to its Total.

## Where it lands

1. **Producer** (`mdpf_gold_consolidator`), Variant 1 only:
   - emit the Global `by_model` primary values for dates before 2026-05-15 from the 49F series (firms ['49financial'],
     claim measured);
   - emit `custom_models_aua` as `model_aua` - the five, or let the portal take the difference;
   - emit `carried` rows for the 9 no-total dates.
   - This is a served change, so it goes under a never-widen pair. Every Global leaf is read before and after; the
     headline sums must be byte-equal.
2. **Portal** (`src/lib/trendGrouping.ts`, `ModelPortfolios.tsx`; both variants):
   - Client Supervised per date from the G difference, replacing `clientChipAt` (chips only on the as-of);
   - ETF and ALT from the G series;
   - retire Other AUA;
   - Custom by difference (if not emitted);
   - carried points drawn with their class;
   - drop the "Per-model detail begins ..." sentence (Variant 1) or keep it (Variant 2).
   - FIELD-READ LAW holds: every group is a sum or difference of served fields, and the total is read, never recomposed.
3. **PRD:** the MDPF_CANON addendum records Andrew's roll-forward rule, which supersedes FWD-9 clause (2) exception (ii)
   per his record, and the variant he picks.

## Not read

- The Cottonwood Trend (the next ask).
- Whether any partner login can open the Global view. If none can, Variant 1's single-firm lines are seen only by Opal
  staff; that is a fact for Andrew's decision, not a substitute for it.
- The PROD old layout's own series.
