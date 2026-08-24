# ANDREW-DIRECT 2026-08-24 ~13:0xZ -- Bloomberg DOES track ETF constituent holdings

**Received:** relayed to `0.0.0_AB_MSTR~Z` by `1.0.0_SA_CTO` over the agentbus
(MessageIds `c13be3df-e3d3-4dc6-a45c-22f14aa334e0` 13:07:40Z, rider `8ca6c0dd-75a2-45ed-8aee-575c70e6fdb8` 13:09:17Z).
**Recorded by:** `0.0.0_AB_MSTR~Z`, site Z. **Broadcast:** report `d9906cce-b6a3-4ffb-a649-cd70d16adc2b`
to `1.0.0_SA_CTO`, cc `3.0.0_SA_CVO` + `0.0.0_AB_MSTR` base.

## VERBATIM (both, as relayed -- never paraphrase)

> "there is absolutely no way bloomberg does not track constituent holdings for etfs"

> "yeah we need to have an adjusted script that pulls ETF data for this purpose"

## HE IS RIGHT, AND IT IS MEASURED RATHER THAN CONCEDED

Bloomberg holds DIVZ/IDVZ constituent-level data. Proof is the holdings-DERIVED surface, which
cannot exist without the holdings it is derived from (ReferenceDataRequest, //blp/refdata, SPY as
in-request control):

| field | DIVZ | IDVZ | SPY (control) |
|---|---|---|---|
| TOTAL_NUMBER_OF_HOLDINGS_IN_PORT | 30 | 46 | -- |
| HB_INDUSTRY_SECTOR_ALLOCATION | 10 rows (Health Care 19.4309%) | 14 rows (Financials 20.6121%) | 13 rows |
| HB_GEO_CNTRY_ALLOC | 3 rows (U.S.A. 96.3349%) | 20 rows (United Kingdom 25.8738%) | 9 rows |
| FUND_PCT_TOP_TEN_HOLD | 48.75998 | 32.94046 | 37.17485 |

## WHAT THE 2026-08-21 BRIEF GOT WRONG -- MECHANISM, NOT MEASUREMENT

`docs/briefs/etfs-positioning-bloomberg-pull-20260821.md` 3.1 concluded: *"the route forward, if ever
wanted, is a different REQUEST TYPE, not a different name."* **Both halves falsified 2026-08-24, each
with a control:**

1. **INDX_MEMBERS IS servable via ReferenceDataRequest** -- INDU Index returned 30 members; SPX Index
   with INDX_MWEIGHT returned 503 rows. The error subcategory reads NOT_APPLICABLE_TO_REF_DATA but the
   **message body reads "Field not applicable to SECURITY."** It is the security TYPE. Reciprocal
   control: the count field works on the ETFs and fails on INDU; INDX_MEMBERS does the exact inverse.
2. **PortfolioDataRequest -- the named route -- returns INVALID_SECURITY for SPY as well as DIVZ/IDVZ.**
   It addresses your own PRTU portfolios, not third-party ETF tickers. A route that rejects SPY was
   never a route to any ETF.

## THE ACTUAL WALL IS AN ENTITLEMENT ON A SURFACE THE BRIEF NEVER REACHED

`//blp/bqlsvc` opens; every query returns *"User not authorized to use BQL. Please contact customer
service."* **Service-level control:** the simplest possible BQL (px_last on IBM -- no holdings, no Opal
funds) is refused identically. So it is not holdings-specific and not DIVZ-specific.

> **THE TRANSFERABLE LESSON, and it is the reason this file exists rather than a line in a log:**
> the brief's *"zero NOT_AUTHORIZED, therefore not entitlement"* was **true of the refdata field surface
> and false of the estate.** A clean, well-controlled zero measured inside one surface said nothing
> about the surface next door -- the wrong-plane class, with every in-plane control passing.

## HISTORY: CURRENT-DAY ONLY -- THE CAPTURE-FORWARD CONSTRAINT IS NOT CONVERTED

HistoricalDataRequest on DIVZ (2026-06-01..08-22) with PX_LAST as an in-request positive control:
PX_LAST returned 6 dates; TOTAL_NUMBER_OF_HOLDINGS_IN_PORT and FUND_PCT_TOP_TEN_HOLD returned **zero
rows**. The TrueShares daily capture remains necessary and its daily loss remains permanent.

## THE OPEN CALL THIS CREATES (Andrew, one line)

His second verbatim presumes a reachable surface. There is none today, so **the adjusted-script ask is
blocked on a COMMERCIAL act, not an engineering one: does Opal buy the BQL entitlement?**
Yes -> the constituents pull joins `etf_daily_pull.py` per CTO's A3. No -> TrueShares capture-forward is
the only path. `1.0.0_SA_CTO` holds A3's spec and has been told not to spec against a refusing surface.
