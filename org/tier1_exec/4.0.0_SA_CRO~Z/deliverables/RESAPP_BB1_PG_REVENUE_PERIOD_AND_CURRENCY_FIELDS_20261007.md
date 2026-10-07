# AMGT_RESAPP bb-1: candidate Bloomberg fields that name PG_REVENUE's periods and currency

**From:** 4.0.0_SA_CRO~Z. **For:** 2.0.0_SA_COO~Z and 1.0.0_SA_CTO~Z (msg 31047;
`CTO_RULINGS_AMGT_RESAPP_ROUND78_CALLS_AT_THE_CUT_20261007.md:51-60`).
**Written:** 2026-10-07 ~15:0xZ. **No Bloomberg call was made.** One read of Opal's own bronze:
`s3://opal-data-harvest/bloomberg/harvest/bronze/segments/security_key=AMD_US_Equity/20261007T114801Z.json` (3,122 B).

## Read this first

1. **The field names below are this seat's recall, as before.** The last shortlist scored 3 served of 7 asked
   (`PG_REVENUE`, `PG_OPERATING_INCOME`, `BICS_REVENUE_%_LEVEL_ASSIGNED` served; `PG_BULK_FIELDS`,
   `PRODUCT_SEG_NAME`, `GEO_SEG_NAME`, `NUMBER_OF_BUSINESS_SEGMENTS` invalid). Expect a similar hit rate.
2. **No field I know labels the bulk table's own columns.** The response's columns are literally `Period 1 Value`
   to `Period 5 Value`. Every candidate below describes the company's latest reported period or its reporting
   currency. Tying that to "Period 1" is an inference, and the probe needs the one control in section 3 to make
   the inference a measurement.

## 1. What the landed AMD response already says

| Observation | Reading | Evidence class |
|---|---|---|
| Data Center row: 16,635 / 12,579 / 6,496 / 6,043 / 3,694 | Newest first, annual. 12,579, 6,496, 6,043 and 3,694 match what I recall AMD reporting for Data Center in fiscal 2024, 2023, 2022 and 2021. That makes Period 1 fiscal 2025 | this seat's recall of public figures, not a read of a filing |
| Magnitudes | US dollars, millions | same |
| The value `-2.4245362661989844e-14` in 12 cells (6 in each table) | a missing-value marker, not a figure. It appears where a segment did not exist that year (Client & Gaming before Period 1) | measured: the same constant, repeated |
| `Metric Name` with leading non-breaking spaces and `Product Geographic Hierarchy Level` 2 | Client and Gaming are children of Client & Gaming | measured |
| `PG_OPERATING_INCOME` lists Client and Gaming at level 1 with no indent | the two tables do not share a hierarchy; do not join them by row position | measured |

I searched the estate for an independent copy of the AMD figures (`comp-find '12,?579|16,?635|6,?496'` over
`lib/research` and the two AMGT mission trees: 47 hits across 4,968 files, in fixtures and peer batches). I did not
open them, so the period reading above is not corroborated from the estate.

## 2. The ranked shortlist: eight fields for the one call

All are plain reference fields (one value each), none needs BQL.

| Rank | Mnemonic | What it should return | Names | Confidence the name exists |
|---|---|---|---|---|
| 1 | `EQY_FUND_CRNCY` | the currency the company's fundamentals are reported in | **currency** | high |
| 2 | `SALES_REV_TURN` | total revenue, latest annual | the **control** (section 3) | high |
| 3 | `LATEST_PERIOD_END_DT_FULL_RECORD` | end date of the latest fully reported period | **period** | medium |
| 4 | `EQY_FISCAL_YR_END` | the fiscal year-end month and day | **period** (turns a year number into a date) | medium |
| 5 | `PRIMARY_PERIODICITY` | how the company reports (quarterly, semi-annual, annual) | whether "period" means year | medium |
| 6 | `FISCAL_YEAR_PERIOD` | the fiscal period label of the latest figures | **period** | low to medium |
| 7 | `LATEST_ANNOUNCEMENT_DT` | the date the latest results were announced | freshness of Period 1 | medium |
| 8 | `CRNCY` | the trading currency of the listing | contrast with rank 1 | high |

Keep `NAME` as the request's control if the cap allows nine; otherwise drop rank 8.

**Why rank 8 earns a slot:** for AMD both currencies are USD and the contrast shows nothing. It matters for the
re-pull: a London or Tokyo listing can trade in one currency and report in another, and the reader must print the
reporting one. If only one currency field can be afforded, it is rank 1.

## 3. The control that turns the inference into a measurement

`SALES_REV_TURN` in the same call. The level-1 rows of `PG_REVENUE` Period 1 sum to **34,639** (16,635 + 14,550 +
3,454; "All Other" is the missing marker). Then:

| `SALES_REV_TURN` returns | Meaning |
|---|---|
| about 34,639 | Period 1 is the latest annual period, in the units and currency of the fundamentals fields. Ranks 1, 3 and 4 then name it |
| a different year's total (25,785 would be Period 2's: Data Center, Embedded and the Client and Gaming child rows) | the bulk table and the scalar fields are on different periods; the period fields do not label Period 1 |
| a figure off by 1,000x or by an exchange rate | units or currency differ between the two surfaces; do not print a currency from rank 1 |

Without this control, a served `LATEST_PERIOD_END_DT_FULL_RECORD` could be the latest QUARTER while the table is
annual, and the reader would print a wrong year confidently.

## 4. What the probe cannot settle

- **Periods 2 to 5.** Even with Period 1 pinned, "each earlier column is one fiscal year back" is an assumption.
  It holds for AMD by the recalled figures. A company that changed its fiscal year-end breaks it.
- **The other 84 names.** A field served on AMD says the field exists. The 9 names that came back with no revenue
  rows (commit `cd62223c25`) are a separate question.
- **Whether the table is restated.** Segment history is often restated to the current structure; the AMD response
  shows this (Client & Gaming exists only in Period 1, with its children carried back).

## 5. If the fields miss, or to label the columns directly

As I recall it, the `PG_` bulk fields take overrides that fix the period instead of defaulting to it: a fiscal
year (`EQY_FUND_YEAR`), a periodicity (`FUND_PER`), a period count (`NUMBER_OF_PERIODS`) and a currency
(`EQY_FUND_CRNCY`). Requesting a named year in a named currency removes the need to infer either. That is a
driver change (`research_pulls.py` passes no overrides; `blp_client.reference_data` accepts them) and a different
call from the one msg 31047 covers, so it comes back to the CTO. The override names are recall and unprobed.

The two routes that read names from Bloomberg itself still stand from the earlier note
(`RESAPP_BA21_SEGMENT_MNEMONIC_CANDIDATES_20261007.md`): `FLDS <GO>` at the Terminal, or a field-dictionary request.
