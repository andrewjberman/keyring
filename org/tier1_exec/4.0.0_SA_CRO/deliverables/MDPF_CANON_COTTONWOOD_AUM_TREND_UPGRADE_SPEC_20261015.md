# /portfolios Cottonwood AUM Trend: the upgrade (fill, roll forward, honest window)

**archetype:** EXPLORE

From `4.0.0_SA_CRO~DELL1` to `1.0.0_SA_CTO~DELL1`, on msg 6039. Andrew's ask (10-14 record
`ANDREW_DIRECT_20261014_201xZ_PORTFOLIOS_SMOKE_TREND_FULL_HISTORY_COTTONWOOD_SPEC.md` @caf5dc7d73): "This one could benefit
from some surgery look how uneven this is ... how to upgrade this, potentially employing the same tricks ... to
find/fill/roll-forward the asset taxonomy groups as needed." Companion to the Global spec
(`MDPF_CANON_GLOBAL_AUA_TREND_FULL_HISTORY_SPEC_20261014.md` @686f769e63, now on PROD c3b21a40).

Everything was read on 2026-10-15 at ~14:5xZ. Read-only.

## Verdict: DOABLE from MDPF's own served Cottonwood object, with no new pull

From 2026-06-09, the first measured total, the groups partition the Cottonwood total **exactly on all 89 dated rows
(max |sum - total| = $0.00, no negative group)**: 50 measured, 27 interpolated (model leg) and 12 carried.

A Cottonwood firm total before Black Diamond coverage is **not served anywhere**, so a true rolling 1-year chart cannot
be filled for Oct 2025 - May 2026. The honest fix is to start Cottonwood's window at its first measured total.

**Muni: SETTLED 2026-10-15** -- Andrew: "Muni is in Custom Models, yes" (below).

## What makes it look uneven today (each measured)

Served object: `s3://opal-data-assets/portal/gold/mdpf/cottonwood/aggregate-aua-timeseries/2026-10-14.json`.

1. **The empty months (Oct 2025 - Apr 2026).** The view draws a rolling 1-year window, but Cottonwood's served
   coverage begins in 2026 (`channel_participation.coverage.cottonwood.first` = 2026-05-28; the total from 2026-06-09).
   - Cottonwood's money arrived on Black Diamond in May - June 2026. The served ADVI firm series
     (`s3://opal-data-cot/platinum/firm/timeseries_chart.json` `adv`, daily from 2026-04-22) reads $0.17M (04-22),
     $4.95M (05-15), $220.8M (05-29), $373.2M (06-09) and $436.7M (06-30).
   - Before the transfer, the only served Cottonwood custody is the **Commonwealth slice**
     (`commonwealth/cottonwood/silver/account_day_value/date=2026-06-23`, 54 MB). It holds $121M - $138M over about
     720 - 750 accounts (Oct 2025 - mid May 2026), then drains to $0.3M by 2026-06-22.
   - That is about a quarter of the firm. Drawing it as Cottonwood's AUM would show a 4x "growth" that is only a
     custody move. **Do not fill the empty months with it.**
2. **The "Interpolated model mix (estimate)" from 05-28 to 07-19.**
   - The model leg before 07-20 is the sanctioned labeled backfill (`meta.composed_backfill`, Andrew-direct
     2026-07-28: "SANCTIONED for cottonwood's pre-measured history only"; 44 dates).
   - It ramps from $0.45M to $122.4M (07-14). That ramp is consistent with real onboarding: accounts assigned to models
     over June - July.
   - Measured model assignment starts only at 2026-07-21 (`blackdiamond/cottonwood/silver/fact_model_assignment`, 76
     partitions). Carrying it backward onto June holdings would claim about $120M in models in June against an
     estimate of about $5M, so **keep the band; do not back-fill assignments.**
   - The band looks empty because the total is drawn only where `non_model_aua` is measured (07-20 on), while the total
     itself is measured from 06-09 (`partner_custody_total`, `meta.total_source`: Black Diamond `fact_holdings`
     Market Value).
3. **The missing Aug 31 bar.** 2026-08-31 is one of 12 dates whose **model leg** is absent
   (`channel_participation.exceptions`: 07-28, 07-29, 07-30, 08-04, 08-12, 08-31, 09-01 .. 09-04, 09-08, 09-09).
   **All 12 have a measured total.** The month-end bar has no model leg to stack, so it draws nothing.
4. **The Jan 30 shaded column is not data.** The Trend bar chart's tooltip draws a hover band:
   `cursor={{ fill: 'rgba(255,255,255,0.05)' }}` (portal PROD `src/pages/ModelPortfolios.tsx:2145`). The screenshot
   caught the pointer over an empty month. *Claim: inferred.* The code is measured; that the pointer sat there is not.
   Moving the mouse settles it. It disappears with fix 1.

## The rule, per group (Cottonwood view)

| Group | Dates | Source | Claim |
|---|---|---|---|
| Window start | 2026-06-09 | the first date with a measured total (`partner_custody_total`) | measured |
| UST, ST, INT, LT, ULT | 06-09 .. 07-19 | `by_model.<model>.model_value` (the sanctioned backfill) | interpolated (keep the existing marking) |
| same | 07-20 .. as-of | `by_model.<model>.model_value` | measured |
| Custom Models | as above | `model_aua` - the five primary lines | same class as its leg |
| Other AUM | 06-09 .. as-of | **`partner_custody_total` - `model_aua`**, on every row with a total. Today it is drawn only from 07-20 (`non_model_aua`); this fills 06-09 .. 07-19 as interpolated, because one leg is. | measured, interpolated or carried, following the model leg |
| Model leg on the 12 absent dates | 07-28 .. 09-09 | the last measured model leg, rolled forward (Andrew's Global rule) | carried; the total stays measured |
| Total (stack top) | 06-09 .. as-of | `partner_custody_total` | measured; the groups sum to it exactly |

### Oracle: month-end values, $M (the last dated row on or before the period end)

| period end (class) | UST | ST | INT | LT | ULT | Custom | Other AUM | Total |
|---|---|---|---|---|---|---|---|---|
| 2026-06-30 (interpolated) | 0.0 | 0.0 | 4.2 | 1.0 | 0.0 | 0.0 | 431.4 | 436.7 |
| 2026-07-31 (measured) | 1.4 | 16.3 | 74.9 | 31.3 | 1.1 | 6.2 | 338.8 | 470.1 |
| 2026-08-31 (**carried**, from 08-28) | 18.5 | 18.4 | 80.3 | 59.5 | 1.1 | 15.0 | 283.7 | 476.5 |
| 2026-09-30 (measured) | 18.2 | 21.2 | 81.4 | 56.7 | 1.0 | 24.0 | 338.8 | 541.3 |
| 2026-10-14 (measured) | 18.2 | 22.0 | 82.0 | 56.6 | 1.4 | 24.8 | 348.6 | 553.7 |

Cross-check: the 06-30 and 09-30 totals equal the ADVI firm series ($436.65M and $541.26M).

## Optional extension (Andrew's call; not in the base)

Begin the window at **2026-04-22**, drawing the total from the ADVI firm series before 06-09 (measured, total only; the
model leg is the backfill). This adds the transfer ramp (Apr $0.17M, May $220.8M).

Costs:
- a cross-product read (MDPF reading ADVI platinum), with a registry row;
- a footnote, because the ramp is custody arriving, not growth.

**Recommendation: base only.** The ramp says nothing about performance and would reintroduce a jump.

## The call for Andrew: Muni at Cottonwood

The Cottonwood object routes **Opal Muni Income (about $64M; 1 account, auto-classified)** to **Other AUM**:
- `meta.income_non_model_residual`: "Opal - Income routes NON-MODEL (standing G8 ruling)";
- the dollars equal `custom_residual_detail` Opal_Muni_Income, $64,119,753.85 on 2026-10-07.

Andrew's word on 10-14 was "muni is just a custom model". If that holds for Cottonwood, about $64M moves from Other
AUM to Custom Models, and from Global non-model to Global Custom. That is a served change under the G8 ruling, so it
needs his word, not mine.

**REC:** yes, to match the Global rule; recut G8 for Muni only.

**RULED (a), 2026-10-15:** "Muni is in Custom Models, yes", Cottonwood included. Opal Muni Income moves Other ->
Custom at Cottonwood and Global. Only Muni is named; the 09-21 rule stands for other auto-classified models. It enters
MDPF_CANON through the CTO's Cottonwood addendum. Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_152xZ_MUNI_IS_CUSTOM_MODELS_EVERYWHERE.md`.

## Where it lands

- **Portal:** the Cottonwood Trend reads `partner_custody_total` for the total. It draws Other AUM as total - model on
  every total-bearing row, starts the window at the first measured total, and keeps the interpolated marking.
- **Producer** (or portal): emit `carried` model legs on the 12 dates.
- **Muni:** ruled (a); Other -> Custom at Cottonwood and Global, through the CTO's Cottonwood addendum.

## Not read

- The Cottonwood Trend's PROD render after these changes.
- The full G8 ruling text.
- Black Diamond per-account history before 2026-06-09.
