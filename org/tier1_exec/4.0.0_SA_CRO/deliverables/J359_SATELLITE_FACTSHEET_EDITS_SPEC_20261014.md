# J359 edits spec -- satellite factsheet: characteristics method, layout, figure meanings

**archetype:** EXPLORE

From `4.0.0_SA_CRO~DELL1` to `2.0.0_SA_COO~J1` (the J359 project seat). Written on Andrew's instruction. Candidate
under edit: portal `origin/cand/dell1/satellite-factsheet` @ `eb80c92f`:
- `src/components/satelliteFactsheet.ts`
- `src/components/SatelliteFactsheetSections.tsx`
- `src/components/SatelliteModal.tsx`

**This spec supersedes findings C (show coverage) and B's coverage captions in my J359 design review**
(`J359_SATELLITE_FACTSHEET_DESIGN_REVIEW_20261014.md`). That recommendation produced the "covers N% of weight" /
"Partial" figures Andrew is correcting here. The defect traces to my review, not to the build.

## Andrew's words (verbatim, 2026-10-14 ~17:5xZ to 18:0xZ, in session at the 4.0.0_SA_CRO~DELL1 terminal)

> "1.) Review the logic around Duration particularly, there are cases like Satellite 90 which are essentially just the
> ULT model with some added Gold exposure. The Duration figure should in this case be exactly the same as the figure for
> ULT, because we only factor duration from fixed income holdings. I want you to make sure that there is not any
> weighting adjustments, trying to account for gold features which don't exist, etc. You should be using the values
> from the models and adjusting based on the model sleeve weightings with the model sleeve holdings being viewed as 100%
> of the pie. Make sure all characteristics like duration/yield/etc are accounted for this way."
>
> "2.) On UI, when you have a bar here displaying asset mix, but no commensurate bar design underneath the trailing
> return side, the design is lopsided. This needs to be organized in a better manner as a result"
>
> "3.) Need explanation on some of these figures, for example in this image #2, we see that Beta seems to be pro-rated
> based on what could actually be accounted for. This is the same issue im referring to on Duration; we need to get these
> figures based on the values that actually possess Beta (or Duration, or Yield, etc). Do not pro-rate with nulls."
>
> "Yeah we want to keep the truth of the calculations as close to the approach of the general "Models" calculations in
> the "Positioning" page as possible. I believe that is accomplished by getting characteristics as a percentage of the
> assets that possess those characteristics, not just pro-rating with nulls"

## 1. Characteristics: the method (fixes items 1 and 3)

### What the figures are today (the explanation Andrew asked for)

The served `characteristics.json` (producer `data/assets/scripts/gold/build_satellites_characteristics.py`, behind the
Lambda `cot-satellites-characteristics-producer`) publishes:

    method.formula = "sum(weight_pct * value over holdings WITH a value) / 100", renormalised: false

Every holding without a value (gold, cash, the fixed income for beta, the equity for duration) counts as zero against
the whole book.

Satellite 40's Beta 0.39 is the beta of the 42% of weight that reports one, divided by 100. Its Duration 1.74 is the
duration of the 46% that reports one, divided by 100. That is the pro-rating with nulls Andrew is pointing at.

### How the Models on Positioning do it (the rule to match)

`infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py:1299`,
`calculate_characteristics` ("Yang's methodology"):
- **duration:** sum of weight times duration over fixed_income and cash holdings, divided by **fixed_income + cash
  weight** (`FIXED_INCOME_ASSET_CLASSES = ('fixed_income', 'cash')`, `:317`);
- **beta:** sum of weight times beta over equity holdings, divided by **equity weight**;
- **yield / cost:** sum of weight times value, divided by the weight of holdings reporting a value. A null yield takes
  the ACWI (equity) or AGG (fixed income) yield;
- structured, commodities (gold) and alternatives are outside the duration and beta denominators by design (its "OK: ... ratified class with no
  duration or beta" branch).

### The satellite rule (Andrew's sleeve rule, made exact)

Each satellite is its registry constituents: model books with declared sleeve weights `s_m` summing to 100
(`platinum/satellites/registry.json`). Those sleeves are 100% of the pie. Gold, the hedge sleeve and anything outside
the model sleeves are not in it.

For each characteristic X in {fee (model `cost`), yield, duration, beta}:

    X_sat = sum_m( s_m * a_m(X) * X_m ) / sum_m( s_m * a_m(X) )      over models with X_m not null

- `X_m` is the model's own served figure: `positioning_data.json` `portfolios[m].characteristics`.
- `a_m(X)` is the model's share of the class X is measured over, read from `portfolios[m].allocation`:
  - duration: `fixed_income + cash`
  - beta: `equity`
  - fee and yield: 100
- This is algebraically the Models' `calculate_characteristics` run over the model sleeves' combined holdings. A
  single-model satellite therefore reads **exactly** its model's figure.
- Round as the Models do: yield 2 dp, cost 4 dp, duration 2 dp, beta 2 dp.

Why not run the Models' function over the satellite's own Black Diamond holdings? Measured today, it does NOT
reproduce the model: Satellite 90 gives 1.76 against ULT's 1.92, and Satellite 80 gives 1.70 against LT's 2.50. The
held book differs from the model book, so Andrew's sleeve rule is the one that ties out.

### Values the rule produces (measured 2026-10-14; positioning as_of 2026-10-13; registry as_of 2026-10-14)

| Satellite | Sleeves | Expense | Yield | Duration | Beta |
|---|---|---|---|---|---|
| 15 | ST 100 | 0.20 -> **0.17** | 3.76 -> **4.15** | 2.46 -> **3.49** | 0.14 -> **0.80** |
| 30 | INT 25 + ST 75 | 0.22 -> **0.20** | 3.48 -> **3.82** | 2.10 -> **3.53** | 0.26 -> **0.88** |
| 40 | INT 50 + ST 50 | 0.25 -> **0.23** | 3.18 -> **3.50** | 1.74 -> **3.59** | 0.39 -> **0.92** |
| 50 | INT 75 + ST 25 | 0.27 -> **0.26** | 2.89 -> **3.17** | 1.38 -> **3.69** | 0.52 -> **0.94** |
| 60 | INT 100 | 0.30 -> **0.29** | 2.60 -> **2.84** | 1.02 -> **3.86** | 0.64 -> **0.95** |
| 70 | LT 50 + INT 50 | 0.32 -> **0.31** | 2.26 -> **2.47** | 0.60 -> **3.49** | 0.74 -> **0.96** |
| 80 | LT 100 | 0.34 -> **0.33** | 1.93 -> **2.10** | 0.17 -> **2.50** | 0.83 -> **0.96** |
| 90 | ULT 100 | 0.36 -> **0.36** | 1.77 -> **1.85** | 0.14 -> **1.92** (= ULT) | 0.88 -> **0.97** (= ULT) |
| 98 | ULT 100 | 0.36 -> **0.36** | 1.77 -> **1.85** | 0.14 -> **1.92** | 0.88 -> **0.97** |

Each cell reads "live now -> spec". These figures are the acceptance oracle for the build.

**The one place the exact rule and a plain sleeve average differ** is multi-model satellites, for duration and beta. A
plain sleeve average gives Satellite 70 duration 3.18; the class-share rule gives 3.49 (LT is 12% fixed income, INT
32.7%). The class-share rule is what "a percentage of the assets that possess those characteristics" means. Build that.

### Where it is computed: the producer, not the portal

- Change `build_satellites_characteristics.py`. It already reads `positioning_data.json` (its `inputs.positioning_key`)
  and the registry. Replace the per-satellite `fee` / `yield` / `duration` / `beta` with the sleeve rule. Rewrite
  `method` to state it (formula, `a_m` per field, the model as_of). Drop `coverage.weight_with_value` for those four
  fields; it no longer describes them.
- Do NOT add the new numbers beside the old ones. Two published figures for one field is a shadow output. Replace.
- The portal reads the served numbers. `satelliteAdapter.ts` "computes no measure", and Rule 17 puts the transformation
  in gold. The same change also corrects the Positioning page's Satellites-mode characteristics, which read the same
  file.
- **Sign-off:** this moves served output (`opal-data-cot/platinum/satellites/characteristics.json`). It needs the
  never-widen sign-off (CTO + COO) naming the blast radius, which is that one key and its two readers (the Satellites
  mode and the factsheet), with rollback to the prior object version. Deploy through the Lambda's Terraform route with
  the change-management ledger entry.
- **Fallback, only if the producer cannot land inside the 1-2 week window:** compute the same formula in
  `satelliteFactsheet.ts` from the registry plus the models' served characteristics and allocation, which the page
  already holds. Label it as interim, with an owner and a retire condition: the producer lands. Andrew's call, not the
  seat's.

### Returns (the same "no pro-rating with nulls" rule)

- Model returns are served only per holding (`positioning_data.json` `portfolios[m].holdings[].returns`). There is no
  model-level return to blend.
- So each window stays computed over the satellite's own holdings, divided by **the weight of holdings that have that
  window**, not by 100. Gold stays in: its return is real.
- Today, for example, PFDE and PFOE have no 1Y history and CASH has no 1D value. That is why 1Y reads "covers 86%".
- Same producer, same file (`returns` per satellite). Drop the per-window "covers N% of weight" captions. Name the
  excluded holdings once in the footnote (for example "1Y excludes PFDE, PFOE (under one year of history)").
- **Open for Andrew, defaulting to the above:** should returns also follow the sleeve rule (gold out)? The default
  keeps gold, because the satellite earns gold's return.

## 2. Layout: balance the two columns (item 2)

Today the Asset Allocation column carries a stacked bar plus a 5-group list, and the Trailing Returns column is text
rows only. The left column is visually heavier and taller.

**Spec:**
1. **Key Figures** row unchanged in shape, but remove every "covers N% of weight" / "Partial" caption and the caption
   "Each figure is the weighted sum ... reads low". Replace them with one line: "Duration over fixed income and cash,
   beta over equity, yield and expense over the whole book; each model sleeve weighted by its declared allocation, as
   on the Models."
2. **Asset Allocation bar moves to full width**, directly under Key Figures, with an inline legend (class plus %). It
   becomes the section's header graphic rather than one column's.
3. Below it, **two columns with matched structure**, top edges aligned:
   - left, "Allocation Detail": the class and sub-class rows (today's list, without its bar);
   - right, "Trailing Returns": **one horizontal bar per window** (1D ... 1Y) on a shared zero axis, positive and
     negative in the house palette, value label at the bar end. This mirrors the one-pager's performance bars (CW's
     template), so the right column carries its own graphic.
   - Same eyebrow, same top rule, and the same row height (row rhythm) in both columns.
4. Top Holdings stays full width below.
5. Under 768 px the columns stack (allocation detail, then returns), with a 16 px gutter and no horizontal scroll.
6. Keep the hypothetical-returns footnote. Add the exclusions line from section 1, "Returns".

Use the estate's chart conventions (the `dataviz` skill: palette tokens, light and dark). No new chart library: plain
divs or inline SVG, as the allocation bar already uses.

## Acceptance (graded on the real artifact, all 9 satellites)

1. `characteristics.json` after the producer run: the four fields equal the table above to the stated rounding.
   Satellites 90 and 98 duration = ULT's served 1.92 and beta = 0.97 (positive control). Satellite 70 duration = 3.49
   (the class-share case).
2. The factsheet on the dev build (port 5174) as a CW login (`/ui-walk`): no "covers" or "Partial" text in Key
   Figures. The method line is present. Returns show bars. Column tops align at 1280 px and stack at 375 px.
3. The Positioning Satellites-mode characteristics show the same four numbers as the factsheet (one source).
4. Landing: portal DEV only via `.tools/portal-merge-forward.sh cand/dell1/satellite-factsheet` on an approved row.
   It is CW-facing, so DEV and PROD wait for Andrew. The producer change waits for the never-widen sign-off above.

## Addendum, 2026-10-14 ~18:5xZ: rerun the producer once the canonical logic is deployed (Andrew-direct)

Andrew, verbatim, in session at the 4.0.0_SA_CRO~DELL1 terminal:

> "also on the SATELLITES issue, please make sure that whatever lambda was involved in that factsheet which should be
> updated with the logic i described prior, once that logic is updated to the canonical logic it should be rerun to
> refresh those numbers."

**The Lambda:** `cot-satellites-characteristics-producer` (entry point
`infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/lambda_function.py`; derivation
`data/assets/scripts/gold/build_satellites_characteristics.py`). It writes `s3://opal-data-cot/platinum/satellites/characteristics.json`.

**State measured at ~18:5xZ:**
- The function code was updated at **2026-10-14 18:51:20Z** (CodeSha256 `mpFb3up8...`, State Active). The deploy
  ledger `org/critical_paths/.open_deploys/j359-satellite-characteristics-deploy-dell1-20261014.json` is OPEN.
- The served `characteristics.json` is still the **13:26:02Z** object: old `method.formula` "sum(weight_pct * value over
  holdings WITH a value) / 100", Satellite 90 duration 0.139, beta 0.883.
- The next scheduled fire is cron(25 13 * * ? *) UTC tomorrow, so without a rerun the old numbers serve until then.

**The act, part of this deploy (not a separate approval):**
1. After the deploy lands, invoke `cot-satellites-characteristics-producer` once, with the same event its schedule sends.
2. Read the new `characteristics.json` from S3. `method.formula` states the sleeve rule, and the four fields match the
   table in section 1: Satellites 90 and 98 duration 1.92, beta 0.97; Satellite 70 duration 3.49.
3. Read it again **through the served route** (`/api/scoped/satellites/characteristics.json` as a CW login, or the
   factsheet on 5174). A cached copy that still serves the old numbers is not done.
4. Close the deploy ledger with the invoke's request id, the object's new LastModified, and the three read values. Only
   then report done.

## Addendum 2, 2026-10-14 ~20:0xZ: trailing returns = the models' realized returns blended with GLD (Andrew-direct)

Andrew, verbatim, in session at the 4.0.0_SA_CRO~DELL1 terminal:

> "One other piece of feedback on the satellites. The trailing performance logic is not quite right. What it should be
> is we take the weighted average performance of the underlying constituent opal models, blended with the performance
> of the commodities exposure (GLD ticker). This shouldn't require a frontend change (aside from getting rid of the
> disclaimer about the snapshot lookback method, as this is method change)."
>
> "We already have the models actual performance in the given windows so this shouldnt require additional calculation
> aside from the pro-rating/averaging, that data already exists in the BenchmarkHeatMap component on Model Portfolios
> page" / "so its being served from somewhere."

**This supersedes section 1, "Returns" (the holdings backcast).**

### The served inputs (read ~19:5xZ)

- **Model returns**, the same figures the Model Portfolios `BenchmarkHeatmap` shows:
  - Route: `getModelPortfolioBenchmarks()` reads `/api/general/benchmarks/model_portfolio_benchmarks.json`
    (`src/api/portal-proxy.ts:833`).
  - Object: `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json` (LastModified
    2026-10-14 11:06:00Z, 19,691 bytes).
  - Field: `models[code=<book>].returns[<window>].model`, in percent, `model_source: "yang_design"`.
  - Source: "data.pkl -> return_daily (Yang canonical)", `data_as_of` 2026-10-13.
  - Windows served: 1D, WTD, MTD, 1M, QTD, 1Q, YTD, 1Y (all eight the factsheet shows), plus Since Inception and TTW.
- **GLD returns:** `characteristics.json` `tickers.GLD.returns` (source bbg; BBG partition 2026-10-13).
- **GLD weight `g`:** the GLD row's `weight` / 100 in the served `holdings.json` for that satellite.

### The rule

For each satellite and window w:

    R_sat(w) = (1 - g) * [ sum_m s_m * R_m(w) / sum_m s_m ] + g * R_GLD(w)

- `s_m`: the registry's declared sleeve weights (sum to 100).
- `R_m(w)`: the model's served `returns[w].model`.
- The sum runs over models with a value for w.
- If `R_GLD(w)` is null, publish the model part alone (the sleeves are the pie) and name GLD in a `returns_note`. Never
  count it as zero.
- No holdings-level returns, no backcast, no coverage-weighted sum.

### Oracle (computed from the three served objects above; 2 dp)

| Satellite | g (GLD) | 1D | WTD | MTD | 1M | QTD | 1Q | YTD | 1Y |
|---|---|---|---|---|---|---|---|---|---|
| 15 (ST 100) | 0.0803 | -0.01 | -0.01 | 0.51 | -0.91 | 0.51 | -0.47 | 0.46 | 1.93 |
| 30 (INT 25 + ST 75) | 0.0698 | -0.01 | -0.03 | 0.56 | -0.93 | 0.56 | -0.44 | 1.72 | 3.42 |
| 40 (INT 50 + ST 50) | 0.0593 | -0.01 | -0.06 | 0.60 | -0.96 | 0.60 | -0.40 | 3.01 | 4.95 |
| 50 (INT 75 + ST 25) | 0.0488 | -0.01 | -0.09 | 0.65 | -1.00 | 0.65 | -0.36 | 4.33 | 6.51 |
| 60 (INT 100) | 0.0383 | -0.01 | -0.13 | 0.69 | -1.03 | 0.69 | -0.32 | 5.68 | 8.10 |
| 70 (LT 50 + INT 50) | 0.0294 | -0.02 | -0.17 | 0.75 | -1.12 | 0.75 | -0.43 | 6.66 | 9.61 |
| 80 (LT 100) | 0.0204 | -0.02 | -0.21 | 0.82 | -1.21 | 0.82 | -0.55 | 7.66 | 11.14 |
| 90 (ULT 100) | **0** | -0.04 | -0.25 | 0.89 | -1.13 | 0.89 | -0.78 | 8.37 | 12.15 |
| 98 (ULT 100) | **0** | -0.04 | -0.25 | 0.89 | -1.13 | 0.89 | -0.78 | 8.37 | 12.15 |

For comparison, the live holdings-backcast figures for Satellite 40 are YTD 3.52 and 1Y 5.21; the rule gives 3.01 and
4.95.

**Discrepancy to surface to Andrew, not fix:** the served `holdings.json` carries **no GLD (no commodities row) for
Satellites 90 and 98**. Andrew described Satellite 90 as "ULT with some added Gold exposure". Under the rule they read
as pure ULT. If they should carry gold, the gap is upstream in Black Diamond's rebalancer model definitions (the
holdings source), not in this producer.

### Where it lands

- **Producer:** `data/assets/scripts/gold/build_satellites_characteristics.py`, the `returns` per satellite. Rewrite the
  `method` text so its returns half states this rule and the benchmarks object as source, and drop the returns coverage
  block.
- **The producer's new read** is `opal-data-portal-v2` `json/benchmarks/model_portfolio_benchmarks.json`. This needs:
  - (a) an IAM read grant for `cot-satellites-characteristics-producer-role`, in Terraform;
  - (b) a `legacy_addresses.json` row (bucket opal-data-portal-v2, template
    `json/benchmarks/model_portfolio_benchmarks.json`, object, no params, reader POSN_ASTTAX), or the naming gate
    refuses the new literal. It is the same shape as XA-ad15. `key_rulings.json` already carries its canonical
    (`yang/global/platinum/benchmarks/model-portfolio-benchmarks.json`), but key_rulings does not clear a typed literal
    (XA-c328 finding). 4.0.0_SA_CRO writes the row on the CTO's word.
- **Frontend, the only change Andrew allows:** delete the snapshot-lookback disclaimer under Trailing Returns ("today's
  holdings at today's weights over each period ...") and the exclusions footnote. Both describe the retired method.
  No other frontend change.
- **Then rerun** the producer once (Addendum 1's act), read S3 and the served route against the oracle above, and close
  the deploy ledger with the values.

## Not read

- The live CW render after the change.
- Whether ACWI/AGG yield substitution changes any model yield today (the rule inherits the models' served yield, so it
  does not matter to the satellite).
- `build_satellites_characteristics.py`'s body (only its contract, read from the served `method` block and the Lambda
  header).
