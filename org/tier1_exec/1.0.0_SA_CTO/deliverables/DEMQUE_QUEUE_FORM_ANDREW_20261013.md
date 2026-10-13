# MDPF_DEMQUE queue form: Andrew's answers, item by item (kept by `1.0.0_SA_CTO~DELL1`, opened 2026-10-13 ~14:3xZ)

Source of facts: `deliverables/2.0.0_SA_COO~Q1/QUEUE_QUALIFICATION_20261013.md` @6132ed27c9. Law: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_141xZ_BACKFILL_FLOOR_2012_AND_EARLIEST_CLIENT_RECORD.md`
(earliest client record, 365 days before need for non-client, 2012-01-01 floor, about a 2-week Bloomberg budget).

**Each item's form:** surface; who uses it; priority; history depth; field breadth; securities; schedule; budget; decision.

## Surface level (Andrew, 2026-10-13 ~14:3xZ)

> I agree with your recs on 1 and 2. Regarding 3, not sure what the issue is here, if these are needed for the research app they shouldnt be dropped, merely included in the research apps surface/needs.

1. **Surface order: A Production daily, then B Client history, then E Opal ad-hoc, then C Product history, then D Research.** AGREED.
2. **Opal ad-hoc reserve:** 10 pct of the daily Bloomberg allowance is held for surface E (requests through the Opal agent, currently `0.0.3_BG_BBGTerminal`). Any part unused by
   the day's ad-hoc requests is released to the other surfaces that day. AGREED.
3. **"Consumer: none found" is NOT a reason to drop.** The AMGT_RESAPP items (ABNB model block, ICT identity, the CRNCY scanner slices) are the RESEARCH APP's needs. Their
   consumer is recorded as **the research app (AMGT_RESAPP)**, under surface D's research-app needs. They are kept. The TR comparison (Andrew-direct 2026-10-09) and the
   Cottonwood 15-fund fill (ADVI_COTBKF) are likewise kept under their own owners' needs.

## Items

### Surface A: production daily (Andrew, 2026-10-13 ~14:4xZ)

**The 7:00 am ET (11:00Z) site Z job** (`integrations/bloomberg/pipeline/scheduled_daily_pull.cmd`) runs four legs in order: the MODELS pull (the original pull feeding the dashboard's
market data and models), PUBLISH, the ETF pull, and the CONSTITUENTS pull. Each leg gets its own card.

#### A2 Daily ETF pull (`integrations/bloomberg/pipeline/etf_daily_pull.py`): APPROVED as written

> This is all correect. I also agree with the recommendation on the fund fields only for funds, please note that in some persistent plact on a document which we will append all our notes/decisions as some of this will need to go to sitez as the bloomberg device.

1. **Who uses it:** the Positioning page (the Opal ETFs and their holdings) and MDPF_SECHIST's per-security price history.
2. **Priority:** A, second (after the models pull, which runs first in the same job).
3. **History depth:** one day per run. Any security holding less than a year is topped up to 365 days before the need (`DEPTH_START_DAYS` 372 to 365).
4. **Field breadth:**
   - reference: about 15 fields (`NAME`, `FUND_EXPENSE_RATIO`, `FUND_TOTAL_ASSETS`, `TOTAL_NUMBER_OF_HOLDINGS_IN_PORT`, `TRACKING_ERROR`, `EQY_DVD_YLD_IND_NET`,
     `HB_OAS_EFF_DURTN`, `YAS_ISPREAD_TO_GOVT`, `BETA_ADJ_OVERRIDABLE`, the GICS sector and industry fields, `CNTRY_OF_DOMICILE`, `CUR_MKT_CAP`);
   - history: `PX_LAST`, `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`, and the total-return level;
   - Opal funds only: `PX_LAST`, `FUND_TOTAL_ASSETS`, `FUND_NET_ASSET_VAL`, `EQY_DVD_YLD_IND_NET`, `BETA_ADJ_OVERRIDABLE`.
5. **Securities:** 172. That is the 4 Opal ETFs (DIVZ, IDVZ, PFDE, PFOE), their 166 constituents (re-derived daily from `silver/holdings`), and GLD and VXX.
6. **Schedule:** daily at 7:00 am ET, trading days, for the prior trading day.
7. **Budget:** about 2,600 reference cells and about 520 history cells a day, plus small one-off depth top-ups (412 estimated on 10-12, under a 120,000 limit).

**DECISION, Andrew-approved: FUND FIELDS ONLY ON FUNDS.** `FUND_EXPENSE_RATIO`, `FUND_TOTAL_ASSETS`, `TOTAL_NUMBER_OF_HOLDINGS_IN_PORT` and `TRACKING_ERROR` are requested
only for funds (the 4 Opal ETFs plus fund-type extras), never for the 164 single stocks, which return NOT_APPLICABLE (manifest `field_exceptions`, 2026-10-09). That
cuts about a quarter of the leg's reference cells with no loss.

**Site Z:** today's 7:00 am ET run (as-of 2026-10-12) did not land (no `bbg/2026-10-12/` at 14:4xZ). Andrew: "that is already being rectified on sitez".

#### A3/C1 Rival Funds daily run (ETFS_RIVALS, 7:00 am ET / 11:00Z vehicle at site Z): APPROVED, with both recommendations

> I aprove your recommendations. Regarding ACWI and IWM, we do not need full holdings depth for these.

1. **Who uses it:** the Rival Funds page (13 rival funds set against the Opal funds).
2. **Priority:** today's data is A, third (after the models pull and the ETF pull). History still owed is C.
3. **History depth:**
   - holdings and market data: the prior trading day only;
   - dividends: see the DECISION below;
   - history still owed: 365 days before the need.
4. **Field breadth:**
   - holdings: one multi-fund Excel BQL query a day (`id`, `name` per holding);
   - dividends: `DVD_HIST_ALL` and `DVD_CRNCY`;
   - market: GICS names and codes, `PX_LAST`, `CRNCY`, `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`;
   - history still owed: the close only.
5. **Securities:** every holding of the rival funds (742 securities owed history on 10-08).
6. **Schedule:** daily at 7:00 am ET, trading days, for the prior trading day.
7. **Budget:** its own ceiling of 150,000 rows a day, 30,000 of them reserved for production. History still owed is capped at 20,000 cells a run.

**DECISION, Andrew-approved: DIVIDENDS ONCE, THEN INCREMENTAL.** Today `enrichment_bloomberg.py` re-pulls `DVD_HIST_ALL` over `DEFAULT_WINDOW_DAYS = 730` for every
security, every day. Instead:
- ONE pull of 365 days per security, when it first enters the universe;
- after that, a daily window of only the last few trading days.

**DECISION, Andrew: ACWI and IWM do NOT need full holdings depth** (about 2,200 and 2,000 holdings a day today).

-- open for Andrew to confirm: this seat proposes the TOP 25 holdings by weight, daily, for those two broad index ETFs only.

## FOR SITE Z (the Bloomberg device): changes to carry, appended as decided

| # | change | file | source decision |
|---|---|---|---|
| Z1 | Fund-only fields (`FUND_EXPENSE_RATIO`, `FUND_TOTAL_ASSETS`, `TOTAL_NUMBER_OF_HOLDINGS_IN_PORT`, `TRACKING_ERROR`) are requested only for funds | `integrations/bloomberg/pipeline/etf_daily_pull.py`, the `CHAR` request | A2, Andrew 2026-10-13 |
| Z3 | Dividends: one 365-day `DVD_HIST_ALL` pull per security on first entry, then a daily window of the last few trading days (replacing the 730-day daily re-pull) | `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` (`DEFAULT_WINDOW_DAYS`, `build_plan`) | A3, Andrew 2026-10-13 |
| Z4 | ACWI and IWM: not full holdings depth (the depth is to be confirmed; proposed top 25 by weight, daily) | `data/etfs/scripts/rivalfunds/collector_bloomberg.py` (the BQL holdings query) | A3, Andrew 2026-10-13 |
| Z2 | `DEPTH_START_DAYS` 372 becomes 365 (non-client need: 365 days before the need; the trading calendar resolves the first business day) | `integrations/bloomberg/pipeline/etf_daily_pull.py` | backfill law ADDENDUM 2 item 4 |
