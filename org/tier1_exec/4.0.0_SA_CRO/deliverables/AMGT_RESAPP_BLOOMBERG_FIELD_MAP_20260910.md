# AMGT_RESAPP -- Bloomberg field map for Adam's one-pager model

**Author:** `4.0.0_SA_CRO~Z` | **Date:** 2026-09-10 | **Status:** MEASURED, batch 1 (one security).
**Authority:** Andrew-direct egress grant 2026-09-10, VERBATIM: *"you have egress to do whatever you
need to do just try to be ginger about data pulls, one security at a time, ideally one endpoint at
a time and if they have date picker dont go too historical."* Honoured: **one security throughout
(`SAP GY Equity`), one endpoint per call, 5 calls total, deepest history 5 annual points.**

**Instrument:** `mcp__bloomberg__bloomberg_{health,reference_data,historical_data}` against local
DAPI `127.0.0.1:8194`, service `//blp/refdata`. `bloomberg_health` -> `ok: true` before any pull;
**no sign-in attempted, attempt budget unspent.**
**Reference artifact:** `SAP FactSet Based ONE PAGER 2026 07 01_v1.xlsx`, sheet `Model NEW VERSION`,
read with `openpyxl data_only=True` -- i.e. **values as last saved (2026-07-01), not live formulas.**

---

## 1. THE HEADLINE -- read this before the tables

**Raw reported line items reconcile. Vendor-NORMALIZED line items do not, and they are the rows
analysts quote most.**

| FY | Item | FactSet (workbook) | Bloomberg | Delta |
|---|---|---|---|---|
| 2022 | Revenue | 29,520 | 29,520 | **0** |
| 2023 | Revenue | 31,207 | 31,208 | **+1** |
| 2022 | FCF | 4,770 | 4,769 | **-1** |
| 2023 | FCF | 5,547 | 5,548 | **+1** |
| 2022 | EBITDA | 8,216 | `EBITDA` 7,658 | **-6.8%** |
| 2023 | EBITDA | 7,957 | `EBITDA` 7,160 | **-10.0%** |
| 2022 | EBITDA | 8,216 | `EBITDA_ADJUSTED` 8,126 | **-1.1%** |
| 2023 | EBITDA | 7,957 | `EBITDA_ADJUSTED` 7,875 | **-1.0%** |
| 2022 | EPS recurring | 2.27 | `IS_COMP_EPS_ADJUSTED` 4.08 / `IS_EPS` 1.95 | **no match** |
| 2023 | EPS recurring | 2.65 | `IS_COMP_EPS_ADJUSTED` 5.01 / `IS_EPS` 5.26 | **no match** |

**THE CONTROL THAT MAKES THIS A DEFINITION FINDING AND NOT A VINTAGE FINDING:** FY2022 and FY2023
are closed years. If the divergence were restatement or stale-cache, **Revenue would move too.**
Revenue matches to +/-1 across both years. So the gap is normalization, not vintage.

**Both sides are internally consistent**, which is what rules out arithmetic error: the workbook's
2022 EBITDA margin 0.28 = 8,216 / 29,520; Bloomberg's `EBITDA` gives 7,658 / 29,520 = 0.259. Two
coherent answers to two different questions.

**EPS is the unresolved one.** Eight mnemonics tested: `IS_EPS`, `IS_DILUTED_EPS`,
`IS_COMP_EPS_ADJUSTED`, `TRAIL_12M_EPS`, `TRAIL_12M_DILUTED_EPS`, `IS_BASIC_EPS_CONT_OPS`,
`IS_DILUTED_EPS_CONT_OPS`, `IS_ADJUSTED_EPS`. **None reproduces FactSet's "EPS recurring."**
The 2023 shape is the tell: SAP's reported EPS carries a large one-off, FactSet's recurring strips
it (2.65) and every Bloomberg variant retains some of it (5.01 / 5.26). **FactSet's recurring-EPS
normalization looks proprietary.** -> sovereign call, see §5.

---

## 2. HEADER BLOCK -- 15 of 16 mapped

| Workbook item | Bloomberg mnemonic | Served | Unit / note |
|---|---|---|---|
| Name | `NAME` | YES | "SAP SE" -- exact match |
| Currency | `CRNCY` | YES | `EUR` vs workbook "Euro" -- format only |
| Location | `CNTRY_OF_DOMICILE` | YES | `DE` vs "Germany" -- format only |
| Sector | `GICS_SECTOR_NAME` | YES | **"Information Technology" vs FactSet "Technology Services" -- DIFFERENT TAXONOMY, not a format difference** |
| Share Price | `PX_LAST` | YES | 178.12 |
| Market Cap | `CUR_MKT_CAP` | YES | **ABSOLUTE** (218,821,173,803.84) |
| Net Debt | `NET_DEBT` | YES | **MILLIONS** (-2,213) |
| Enterprise Value | `CURR_ENTP_VAL` | YES | **MILLIONS** (218,208.17) |
| ADTV | `VOLUME_AVG_30D` | YES | **ABSOLUTE shares** (2,515,312) |
| Outstanding Shares | `EQY_SH_OUT_REAL` | YES | **ABSOLUTE** (1,228,504,232) |
| Float | `EQY_FREE_FLOAT_PCT` | YES | 79.16% -- **workbook's "Float 0.90" is a PERCENT, but `EQY_FLOAT` is float SHARES (972.526mm). Two different quantities sharing one label.** Value also differs from workbook; unreconciled. |
| Beta | `EQY_BETA` | YES | 1.019 vs workbook 1.09 -- different calc window, expected |
| Div Yield | `EQY_DVD_YLD_IND` | YES | **PERCENT** (1.4035) vs workbook **DECIMAL** (0.02) |
| Fiscal Yr | `FISCAL_YEAR_END` | **NO** | `BAD_FLD / INVALID_FIELD` -- needs an alternative |
| Short Interest | `SHORT_INT_RATIO`, `SI_PERCENT_EQUITY_FLOAT` | **NULL, no error** | **Corroborated: the workbook's own header reads `Short Interest / Total | N/A`.** Valid fields, no data for this name. |
| Date of Pricing | -- | n/a | pull timestamp, not a field |

## 3. FINANCIAL SUMMARY -- 17 of 19 mapped

| Workbook line | Bloomberg mnemonic | Unit / sign note |
|---|---|---|
| Revenue | `SALES_REV_TURN` | millions -- **reconciles to +/-1** |
| Operating Income | `IS_OPER_INC` | millions |
| Operating Margin | `OPER_MARGIN` | **PERCENT** (26.13) vs workbook **DECIMAL** (0.23) |
| EBITDA | **`EBITDA_ADJUSTED`** | millions -- **use this, NOT `EBITDA`** (§1) |
| EBITDA Margin | `EBITDA_MARGIN` | **PERCENT**; recompute if using `EBITDA_ADJUSTED` |
| EPS recurring | **UNRESOLVED** | §1, §5 |
| BVPS | `BOOK_VAL_PER_SH` | per share |
| Avg Diluted Shares | `IS_SH_FOR_DILUTED_EPS` | **MILLIONS** (1,175) -- contrast `EQY_SH_OUT_REAL`, absolute |
| Cap Ex | `CAPITAL_EXPEND` | **SIGN INVERTED** -- BBG -739, workbook +785 |
| FCF | `CF_FREE_CASH_FLOW` | millions -- **reconciles to +/-1** |
| DPS | `IS_DIV_PER_SHR` | per share |
| ROA | `RETURN_ON_ASSET` | **PERCENT** (10.83) vs workbook **DECIMAL** (0.05) |
| ROE | `RETURN_COM_EQY` | **PERCENT** (18.18) vs workbook **DECIMAL** (0.09) |
| P/E | `PE_RATIO` | ratio |
| EV/EBITDA | `CURRENT_EV_TO_T12M_EBITDA` | ratio |
| P/B | `PX_TO_BOOK_RATIO` | ratio |
| Dividend Yield | `EQY_DVD_YLD_IND` | PERCENT |
| FCF Yield / FCF Margin | -- | derive from mapped components |

**Invalid (`BAD_FLD/INVALID_FIELD`), do not retry as written:** `FISCAL_YEAR_END`,
`IS_DILUTED_EPS_CONT_OPS`, `IS_ADJUSTED_EPS`, `DILUTED_EPS_BEFORE_XO`, `IS_ADJ_EBITDA`,
`EBITDA_BEFORE_XO`, `IS_STATUTORY_EBITDA`, `IS_SHARE_BASED_COMPENSATION`, `ARDR_EBITDA`.

---

## 4. TWO SHAPE TRAPS FOR WHOEVER BUILDS THIS

**(a) Bloomberg's units are inconsistent ACROSS ITS OWN FIELD FAMILIES.** `CUR_MKT_CAP` is
absolute while `NET_DEBT` and `CURR_ENTP_VAL` are millions; `EQY_SH_OUT_REAL` is absolute while
`IS_SH_FOR_DILUTED_EPS` is millions; every margin/return/yield is a percent while the workbook
holds decimals; `CAPITAL_EXPEND`'s sign is inverted. **The mapping table must carry a UNIT column
and a SIGN column, not just a mnemonic.** A mnemonic-only map will silently produce a model that is
off by 100x in some cells and 1e6 in others.

**(b) Price and fundamentals land on DIFFERENT DATES in the same historical response.** Measured:

```
{"date":"2022-12-30","PX_LAST":96.39}                                  <- last TRADING day
{"date":"2022-12-31","SALES_REV_TURN":29520,"EBITDA":7658,...}         <- FISCAL year end
{"date":"2024-12-31","PX_LAST":236.3,"SALES_REV_TURN":34176,...}       <- merged, 12-31 traded
```

**A consumer joining on `date` gets rows with a price and no fundamentals, and rows with
fundamentals and no price -- in some years but not others.** Join on fiscal year, never on the
date string.

**(c) Corrected scope note, stated because the wrong read was available.** `READ_HERE.md` warns
that derived fields return ZERO rows on a `HistoricalDataRequest` while `PX_LAST` returns a full
series. **That was measured on the ETF derived-field surface and it does NOT hold here** --
equity fundamentals returned a clean annual series with `PX_LAST` riding along as the positive
control. This is READ_HERE's own lesson running in the other direction: a result measured inside
one surface says nothing about the surface next door, and that cuts both ways.

---

## 5. WHAT THIS RAISES

**A NEW SOVEREIGN CALL -- normalization.** A Bloomberg-fed rebuild of Adam's model will show
**different EBITDA and EPS than the packs already circulating**, in the rows analysts quote most.
Three ways out:

- **(a)** Adopt Bloomberg's definitions, use `EBITDA_ADJUSTED`, and **state the basis on the page**.
  Cheapest; the ~1% EBITDA gap is defensible; EPS stays visibly different.
- **(b)** Reconstruct FactSet's recurring EPS from components. Costly, fragile, and it re-implements
  a proprietary normalization we cannot verify against.
- **(c)** Keep FactSet as the model's source and use Bloomberg only for price/market/peer blocks.
  Preserves continuity with every existing pack, but keeps a desktop Excel add-in in the pipeline --
  which is the thing this project exists to remove.

**REC: (a), with the basis stated beside the number** -- and show Adam the SAP delta table in §1
before it is decided, because he is the one who has to defend the number.

## 6. PAYLOAD VOLUME -- the quota precondition, MEASURED

**Andrew-direct 2026-09-10, VERBATIM:** *"test on one security at a time initially to assess the
actual payload volume so in case it turns out really heavy we dont get in trouble with bloomberg on
quota."* Measured on exactly that basis: **one security, one call.**

**THE MEASUREMENT.** `SAP GY Equity`, 18 fields, YEARLY, 2016-01-01 -> 2025-12-31:

| | Measured |
|---|---|
| Calls | **1** |
| Rows returned | **14** (for 10 fiscal years -- see below) |
| Data points returned | **180** = 18 fields x 10 years, **complete, zero gaps** |
| Response size | **~3.4 KB** of JSON |

**PROJECTION TO THE 89-NAME UNIVERSE** (arithmetic, flagged as arithmetic):

| Leg | Data points | Notes |
|---|---|---|
| 10y history, 89 names | **16,020** | 89 x 180 |
| Header block, 89 names | **1,424** | 89 x 16, reference not historical |
| **Subtotal** | **~17,400** | **~300 KB JSON for a FULL rebuild** |
| Peer/`CSC` block | **up to ~10,700** | 89 x ~12 peers x ~10 fields, **before dedup** |

**READ: VOLUME IS NOT THE RISK. UNIQUE SECURITY COUNT IS.**
A full 89-name rebuild is ~300 KB and well under 20k data points -- small by any measure. But the
peer block touches **up to ~1,000 additional unique securities** if peers are pulled per-name
without deduplication, and Bloomberg desktop entitlements are commonly bound by *unique securities
touched* rather than by payload. **Dedupe the peer set across the 89 before pulling it** -- the
telecom peers on the SAP sheet will recur across every telecom name in the coverage list.

**THE LIMIT ITSELF IS UNMEASURED AND I AM NOT GUESSING IT.** Nothing in this session establishes
this terminal's daily or monthly entitlement. The consumption arithmetic above is sound; the
headroom is unknown. **That number has to come from the terminal's own entitlement or Andrew's
Bloomberg representative, and it should be obtained before the first multi-security run.**

**CADENCE IS THE MULTIPLIER, not the one-off.** 89 names refreshed daily is 89 unique securities
per day and unremarkable. The same 89 with an undeduped peer block refreshed daily is a different
order of exposure. The refresh policy is therefore a quota decision, not only a product one.

**TRAP (b) CONFIRMED AT SCALE, WITH A DENOMINATOR:** the price/fundamentals date split occurred in
**4 of 10 years** (2016, 2017, 2022, 2023 split into two rows; 2018-2021, 2024-2025 merged) --
**14 rows for 10 fiscal years.** It is the common case, not an edge case, and any consumer keying
on the date string will silently drop 40% of this name's price history.

**INSTRUCTION RIDING ON THIS, per the same ruling** (*"make sure that its stored somewhere so we
dont need to do it twice"*): every response above must land in `opal-data-research` on first pull
and be served from there afterwards. **The cache is a correctness requirement, not an
optimisation** -- it is what makes the quota arithmetic a one-time cost rather than a recurring one.

## 7. NOT MEASURED (so it is not mistaken for coverage)

- **One security only.** `SAP GY Equity`. Nothing establishes these mnemonics behave the same on a
  US name, an ADR, or a financial. **The unit conventions in §4(a) are the most likely to vary.**
- No test of `FISCAL_YEAR_END` alternatives.
- `EQY_FREE_FLOAT_PCT` 79.16% vs workbook 0.90 left unreconciled.
- CapIQ's `IQ_*` line items were not mapped -- only FactSet's, via the workbook's cached values.
- The peer/`CSC` block was not touched.
