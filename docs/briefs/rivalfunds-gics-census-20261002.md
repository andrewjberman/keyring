# /rivalfunds GICS census, 2026-10-02 -- what "Inputs that did not arrive" says about sectors, and the three fixes that matter

**Author:** `4.0.0_SA_CRO~RV`, on Andrew-direct ~15:4xZ ("Do it now"; the census starts from the page's "Inputs that did
not arrive" component). Record: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261002_154xZ_RIVALFUNDS_GICS_CENSUS_DO_IT_NOW.md`.
**Inputs, all read-only:**
- the component's table `input_census-20261002T150414Z-fcafb026ad5c` (page day 2026-10-02, 763 GICS rows over 13 funds);
- each fund's latest G1 report (the newest objects of the last 8 `canonical_shape` partitions);
- every G4 `security_market` object.

There was no vendor call. Script: `tmp/ui-walk/gics_census.py` (not committed). Per-row evidence:
`docs/briefs/rivalfunds-gics-census-rows-20261002.json`.

## 1. The component overstates the gap by a factor of six

It lists **763 of 763** securities as "GICS missing", because it checks only G4, which holds 638 rows across all dates. Each
row's own reason says *"the sector is read from the fund's G1 report where present"*. Joined to the funds' latest reports:

| class | lines | what it means |
|---|---|---|
| COVERED_OWN_FILE | 410 | the fund's own file carries GICS; not missing |
| COVERED_ELSEWHERE (another fund's G1) | 220 | the same security carries GICS in another fund's file; **joinable today** |
| IDENTITY_UNRESOLVED | 60 | named, with a CUSIP (21 also with ISIN and SEDOL), but the crosswalk does not resolve them, and no classified line in the estate shares a CUSIP, ISIN or name with them |
| LISTED_NO_SOURCE | 58 | resolved Bloomberg-channel equities (50 US-listed) with no name and no GICS anywhere in the estate |
| NOT_GICS_ELIGIBLE | 7 | money-market funds (IJGXX, DGCXX x3, CMQXX, GVMXX) and one future (MFSZ6) |
| NOT_IN_LATEST_REPORT | 8 | census rows from an older report (PFOE 7, IDVZ 1) |

**Truly without a sector source: 118 lines** (60 + 58), not 763. One IDVZ line (SALXX, a money-market fund) is misfiled as
IDENTITY_UNRESOLVED by this script's ticker test, so the eligible count is 117.

## 2. Weight left unclassified, per fund (fraction of the fund's latest report)

| fund | channel | covered elsewhere (fix 1) | identity unresolved (fix 2) | listed, no source (fix 3) | not eligible |
|---|---|---|---|---|---|
| IDVZ | home producer | 18.3% (7) | **78.1% (33)** | -- | -- |
| PFOE | home producer | 39.1% (10) | **26.9% (6)** | -- | -- |
| GQGU | issuer site | 20.8% (8) | **37.5% (20)** | -- | -- |
| BASG | issuer site | -- | 0.9% (1) | -- | -- |
| WCMG | Bloomberg | 36.9% (16) | -- | **58.4% (29)** | 0.2% |
| ETFT | Bloomberg | 32.3% (12) | -- | **42.1% (12)** | 11.7% (IJGXX) |
| TSEL | Bloomberg | 43.0% (9) | -- | 15.4% (8) | 3.9% |
| PCLG | Bloomberg | 33.4% (11) | -- | 13.1% (6) | 1.2% |
| INEQ | Bloomberg | **99.1% (99)** | -- | 0.9% (1) | -- |
| TXUE | Bloomberg | **89.5% (48)** | -- | -- | -- |
| BIDD, CGIC, SCHY | Bloomberg | -- | -- | 0.1-0.2% | 0.7-1.3% |

## 3. The three fixes, by leverage

**Fix 1 -- apply the cross-fund GICS fallback in the RANKINGS, not only in the trend.** This is the highest leverage and needs
no new data.
- CALL 9 put the fallback (a security takes the GICS another fund's file states for it) into `gold_buying_trend.py` only.
  The rankings producer reads the fund's own G1 sector, then G4 (`gold_holding_contribution.py:190` and `:209`).
- 220 lines are joinable. They take INEQ from about 0% classified to 99%, and TXUE to 89%, and cut the unclassified share
  of WCMG, ETFT, TSEL, PCLG, PFOE, GQGU and IDVZ by 18-43 points.
- A sample of 8 joins read correct: Commerzbank Financials, SAP Information Technology, Orange Communication Services, META
  Communication Services, BAT Consumer Staples, NN Financials, Yokogawa Information Technology, Mazda Consumer Discretionary.
- Better still, the join belongs in G1 itself, with `gics_source` = the other fund's file, so every consumer gains it.

**Fix 2 -- resolve the home-producer and GQGU lines by CUSIP and source their GICS.** This is the highest weight for the Opal
funds.
- 60 lines carry a CUSIP but read `resolution_status UNRESOLVED`. They are 78% of IDVZ, 38% of GQGU and 27% of PFOE.
- They are large, plainly classifiable names: Apple 7.5% and Dell 4.4% at GQGU; MercadoLibre 5.5%, Workday 5.1%,
  UnitedHealth 4.4% and Hermes 4.3% at PFOE; Petrobras 3.9%, Intesa 3.8%, Reckitt 3.7%, Enel 3.4% and BNP 3.3% at IDVZ.
- No classified line elsewhere shares their CUSIP or ISIN, so resolution alone does not classify them. They need a
  CUSIP-keyed GICS read in the scripted Bloomberg pull (G4).
- IDVZ's CUSIPs are largely the ADR lines (AMX, BBSEY, BP); the ADR's GICS is its ordinary share's.

**Fix 3 -- run the G4 enrichment at universe scale for the Bloomberg-channel funds.** This also fixes RFW-D05, the names.
- 58 resolved equities have neither a name nor GICS anywhere: 58% of WCMG, 42% of ETFT, 15% of TSEL and 13% of PCLG.
- Examples: WAT, AMS SM, VEEV, SYK, CHD, SGE LN, YUM, ADP, NFLX (ETFT); NBIS, 2269 HK, IBKR, TEVA IT, BAB LN, BKD, THC
  (WCMG); ORCL (PCLG); XYZ, CVNA (TSEL).
- G4's schema already carries `gics_sector` through `gics_sub_industry`, but G4 date=2026-10-01 holds 32 rows (RFW-D04). The
  pull Andrew worded under R-21 covers it; there is no agent-turn Bloomberg call.

**Also:**
- **The component's own state** (RFW-D14) should read the fund's G1 sector before calling a security missing. That turns 763
  "missing" into 118.
- **Money-market lines** (ETFT IJGXX 11.7%) are cash for sectors, as F2 already treats them for the rankings.

## 4. Correction to the walk brief

RFW-D06's acceptance in `docs/briefs/rivalfunds-ui-data-findings-20261002.json` set "Unclassified carries at most 10% of any
fund's absolute YTD contribution". That number was this seat's, and was not measured. The measured levers above replace it:
- after fix 1, the residual is IDVZ 78%, WCMG 58%, ETFT 42%, GQGU 38%, PFOE 27%, TSEL 15% and PCLG 13% (by weight of the
  latest report);
- after fixes 2 and 3, it is the not-eligible lines only.

## 5. What this census does not claim

- Cross-fund joins use any shared key (Bloomberg ticker, CUSIP, ISIN, SEDOL, security_id or raw identifier). Only 8 of the
  220 were checked by eye.
- The weights are the fund's reported weights in its latest report, not contribution shares.
- G1 history older than 8 partitions was not read for cross-fund GICS, so a longer read could cover a few more lines.
- Whether Bloomberg returns GICS for every one of the 118 lines is not known until the scripted pull runs.
