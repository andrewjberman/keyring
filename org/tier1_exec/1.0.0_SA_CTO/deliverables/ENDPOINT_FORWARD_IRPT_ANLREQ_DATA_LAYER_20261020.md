# /endpoint --forward -- IRPT_ANLREQ report data layer (yfinance first, Bloomberg without limit): FWD-13 to FWD-15

**Seat:** 1.0.0_SA_CTO~DELL2. **Date:** 2026-10-20 ~22:4xZ. **State:** DRAFT, put to Andrew at the dell2 terminal. These outcomes
land as IRPT_ANLREQ PRD v0.29 on his confirmation of the DONE WHEN lines.

- **Brief:** `docs/briefs/irpt-anlreq-report-data-layer-yfinance-bloomberg-brief-20261020.md` @04395db240 (166 lines,
  `4.0.0_SA_CRO~TCKT`).
- **Authority:** `org/tier1_exec/4.0.0_SA_CRO~TCKT/deliverables/ANDREW_DIRECT_20261020_22xxZ_REPORT_FROM_DATA_WE_HAVE_BLOOMBERG_DRAW.md`
  @c464f10d32.
- **Numbering:** v0.28 holds FWD-1 to FWD-12, so the next unused number is 13.

```
  FWD-13  Every concentration chart in the YCharts packet is drawn from real data, for every holding the client owns
          DONE WHEN  EXERCISED -- an Overview filed for a real client holdings file that holds funds and stocks
                     outside Opal's own ETFs shows filled charts and breakdowns for region and country, sector,
                     asset class, credit quality, maturity, bond sector, market cap, style, fundamentals, top
                     holdings, and the return and risk series, each computed for the client's actual holdings
          ACCEPT     a person opening the report finds the charts and breakdowns the YCharts packet carries, filled;
                     no holding reads "not covered" when yfinance or Bloomberg knows it; how the pages look matters
                     less than that the charts and concentrations are there
          SOURCE     Andrew 2026-10-20 ("the premise is simply to recreate the y chart format, hwoever we have to
                     do it"; "as long as it has a bunch of charts and concentrations"); brief D1

  FWD-14  Each holding's details come from yfinance first and Bloomberg second, and the report says which
          DONE WHEN  EXERCISED -- for FWD-13's request, every value records its source per holding (yfinance or
                     Bloomberg); Bloomberg is asked only for what yfinance cannot supply, through its request
                     queue; prices still come only from the existing price chain
          ACCEPT     anyone checking a number can see where it came from; Bloomberg fills only what yfinance could
                     not; a holding neither source knows is named in words on the page
          SOURCE     Andrew 2026-10-20 ("if we cannot get that from yfinance, then we need to get it from bloomberg";
                     "there are no limits on bloomberg when it comes to this, it has to get done"); brief D2

  FWD-15  The fund style box and the full fund look-through are filled
          DONE WHEN  EXERCISED -- FWD-13's report shows the 3x3 style box for each fund held and the top-25
                     look-through holdings, from Bloomberg's query service once Opal holds that entitlement
          ACCEPT     the style box and top-holdings pages carry real values for the client's funds, not a gap
          SOURCE     brief D3; Andrew 2026-10-20 ("no limits on bloomberg")
```

**FWD-9 (unchanged text):**
- Andrew's Overview verdict is given on a packet built under FWD-13 to FWD-15 (brief D4).
- Run 7d's sample showed the gap this closes.

**Act only Andrew can do:**
- The Bloomberg BQL entitlement for FWD-15 is a purchase (READ_HERE s.4: "a purchase, not a build").
- `4.0.0_SA_CRO~TCKT` is asking him for it. FWD-13 and FWD-14 do not wait on it.

**NOT READ:** IRPT_ANLREQ task orders and decompositions; the gap-map research beyond the brief's citations; the client YCharts
sample (a client document).
