# Which YCharts call returns one ticker's daily price series (4.0.0_SA_CRO~DELL2, 2026-10-16 ~23:5xZ)

**Asked by:** `1.0.0_SA_CTO~DELL2`, msg 10028 (tick 72). Repo only, no vendor call. It decides whether FWD-7's YCharts-second tier can
return. Every line is MEASURED from a cited file unless marked INFERRED.

## Answer

`GET /charts/fund_data.json` is the right endpoint. The 400 is the parameters: **a security or ETF takes `calcs=id:price`, not
`id:level`, and the estate's working client sends the full quote-page parameter form.**

1. **The estate already has a working client for this call:** `infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py:219-249`,
   `fund_data(yc_symbol, calc="level", max_points=100000)`.
   - Its docstring (`:221-228`): "Uses the full quote-page param form (A5/HAR-derived) -- the minimal form 400s "no valid items" for
     MSCI/GSCI/bond indices; the full form 200s for every index class. ... **calc is entity-class specific: 'level' for indices,
     'price' for securities/ETFs.** ... json path: chart_data[][].raw_data [[ts_ms,value]]."
   - The parameters (`:230-247`): `calcs=id:<calc>,include:true,,`, `securities=id:<symbol>,include:true,,`, `zoom=max`,
     `maxPoints=100000`, `format=real`, `partner=basic_2000`, `chartType=interactive`, `dateSelection=range`,
     `le_o=quote_page_fund_data`, `redesign=true`, `splitType=single`, `scaleType=linear`, and the empty or `false` fields listed at
     `:231-246`.
   - Its caller pulls ETFs with `calc="price"`: `infra/aws/lambda/ycharts-market-data-pull/ws1_surface_pull.py:246-260` ("WS-1 MP-04
     and WS-2 MP-01/02/03 both pull ETFs at calc=price", `:255`).
2. **The same 400 was seen and cured before:** `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-05-20/yalp_mdsrc_007_ycharts_live_session_test.md:26`:
   "fund_data.json | 200 | ... First attempt 400 -- RUNNER omitted the required `calcs=` param; corrected within the live session -> 200".
3. **It was measured working at scale:** `.../logs/2026-05-21/yalp_mdsrc_wsa_history_verification.md:14-17`: the full quote-page form,
   `maxPoints=100000`, calls serialized 2 s apart, **67 of 67 HTTP 200, all clean daily**. The rule is restated at
   `.../logs/2026-05-21/yalp_mdsrc_c2_prestage.md:20`: "calc by yc_kind (id:level for ^-indices, id:price for securities/ETF).
   maxPoints=100000, format=real."

## Why today's reads were refused

- The resident adapter sends `securities` with one trailing comma, `zoom=max` and **no `calcs`**
  (`infra/aws/lambda/investor-reporting/ycharts/research/price_adapter_ycharts.py:96`). That is the 400 case in point 2.
- The recipe-form read (`org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/ycharts_price_probe2.sh:84`, record
  `RECIPE_FORM_READ.txt` @5704252df1, PRICE_HTTP_400 plain and typed) sent **`calcs=id:level`** for SPY. It copied the overview map's
  `benchmark_level_series` call, which is an **index** (`^SPXTR`, probe2 `:4`). For an ETF that is the wrong calc. INFERRED: this is
  the 400.
- **In flight, the same defect:** TO-AR-g-152 (`org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-152.ycharts-price-recipe-form.md:34`,
  `:54`) fixes `calcs=id:level` for SPY in the adapter and its tests. That is the form just measured 400. The fix: `id:price` for a
  security or ETF and `id:level` for a `^` index, in the full quote-page form of `ycharts_client.py:230-247`. Or simplest, call that
  client's builder.

## The read that would settle it (for the CTO to order, not run here)

One session call for SPY with `ycharts_client.py`'s exact parameters and `calc=price`. Expected: 200, with `chart_data[0][0].raw_data`
as `[[ts_ms, price]]` pairs. With `format=real`, these are price levels, not total-return levels. INFERRED from `ws1_surface_pull.py:23`:
"take the native daily series at `format=real` (price levels)". So the adapter's chain over the levels is a **price** return, not a
total return, unless a total-return calc is asked for.
