# Request to 1.0.0_SA_CTO~DELL1: fold rules for the 18 old-list rows the canonical vocabulary does not hold (MDPF_SECCLASS round 27, 2.0.0_SA_COO~M1, 2026-10-16 ~05:0xZ)

Claim words: `measured` = read this session. Source: the merged plan `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~97/SEED22_PLAN.json` @283e087af6 (worker ~97, check `SEED22-PLAN ok=True`) and `get_item` on `bd-securities`.

## What happened to the ruling
Your ruling accepts the old-list classes as source rows. The shared `plan_rows` accepts an old-list row only when its (asset_class, sub_asset_class) is a DIRECT canonical vocabulary member, and does not fold. Of the 22 tickers ($413,341.59), **4 plan ($15,777.17, equity)** and **18 do not ($397,564.42)** because the old list's sub-class is not a canonical sub-class. A pair cut on the plan as built would write 4 rows; the E_18 repoint would then leave $397,564.42 with no canonical row (row D1-W97-S1, BLOCKING, ARMED, owner this seat). Nothing is written.

## The canonical vocabulary (measured, 11,362 rows)
- alternatives: Real Estate 172, International Real Estate 16, (none) 51. commodities: Metals 79, Commodities 51, Oil 32. cash: Cash 348, Money Market 22, T-Bill 11. structured: Options Income 288, Hedge 239.
- fixed_income: Municipal 928, Intermediate 659, Short Duration 344, High Yield 262, **(none) 252**, Structured Credit 147, International 136, Ultra Short 60, Long Duration 60, TIPS 35, Cash 17. equity: sector and size sub-classes, **(none) 73**.
- Convention rows read by `get_item`: VNQ, IYR, SCHH, XLRE = alternatives / Real Estate; IBIT, GBTC, ARKB = commodities / Commodities.

## My recommendation: six fold rules, none inventing a sub-class
- **F1** old equity / Real Estate -> alternatives / Real Estate (the table's own convention for REITs). CUBE, GLPI.
- **F2** old fixed_income / Investment Grade -> fixed_income with NO sub-class (precedent: 252 fixed_income rows carry none). 8 tickers.
- **F3** old alternatives / Structured Notes -> alternatives with NO sub-class (precedent: 51 alternatives rows carry none). 5 tickers.
- **F4** old alternatives / Commodities -> commodities / Commodities (the convention for Bitcoin and Ether trusts). EZET.
- **F5** old alternatives / Volatility -> commodities / Commodities by the same convention. HODL (a bitcoin ETF; the old row is the model's own guess). If you would rather not override the old asset_class, hold it out instead.
- **F6** old fixed_income / needs_review (confidence 0.5, `needs_review=True`) -> HOLD OUT. PCEF, $0.00 today.

| rule | ticker | old-list name | market value (10-09 lots) | old class / sub | classified_by | proposed canonical |
|---|---|---|---|---|---|---|
| F1 | CUBE | CUBESMART COM | 7570.00 | equity / Real Estate | gpt-5.4-mini | alternatives / Real Estate |
| F1 | GLPI | GAMING & LEISURE PPTYS INC COM | 4285.56 | equity / Real Estate | gpt-4o-mini | alternatives / Real Estate |
| F2 | HPI | HANCOCK JOHN PFD INCOME FD SH BEN INT | 51050.86 | fixed_income / Investment Grade | gpt-4o-mini | fixed_income / (none) |
| F2 | LCFYX | LORD ABBETT CONVERTIBLE I | 48293.14 | fixed_income / Investment Grade | gpt-4o-mini | fixed_income / (none) |
| F2 | DODBX | DODGE & COX BALANCED I | 40178.06 | fixed_income / Investment Grade | gpt-4o-mini | fixed_income / (none) |
| F2 | BALCX | AMERICAN FUNDS AMERICAN BALANCED C | 23437.64 | fixed_income / Investment Grade | gpt-4o-mini | fixed_income / (none) |
| F2 | PFF | INVESCO PREFERRED ETF | 12056.00 | fixed_income / Investment Grade | gpt-4o-mini | fixed_income / (none) |
| F2 | CIMAX | AMERICAN FUNDS INCOME FUND OF AMER 529 | 11490.34 | fixed_income / Investment Grade | gpt-4o-mini | fixed_income / (none) |
| F2 | VRP | INVESCO VARIABLE RATE PREFERRED ETF | 9488.00 | fixed_income / Investment Grade | gpt-4o-mini | fixed_income / (none) |
| F2 | CPXIX | COHEN & STEERS PREFERRED SEC & INC I | 0.00 | fixed_income / Investment Grade | gpt-4o-mini | fixed_income / (none) |
| F3 | KAMIX | KENSINGTON MANAGED INCOME INST | 92153.26 | alternatives / Structured Notes | gpt-4o-mini | alternatives / (none) |
| F3 | FSNQX | FIDELITY FREEDOM 2030 K | 30506.33 | alternatives / Structured Notes | gpt-4o-mini | alternatives / (none) |
| F3 | HBLFX | HARTFORD BALANCED INCOME F | 26449.56 | alternatives / Structured Notes | gpt-4o-mini | alternatives / (none) |
| F3 | JBAWX | JHANCOCK BALANCED R6 | 18597.10 | alternatives / Structured Notes | gpt-4o-mini | alternatives / (none) |
| F3 | TRRNX | T. ROWE PRICE RETIREMENT 2055 | 0.00 | alternatives / Structured Notes | gpt-4o-mini | alternatives / (none) |
| F4 | EZET | FRANKLIN ETHEREUM ETF | 18856.67 | alternatives / Commodities | gpt-4o-mini | commodities / Commodities |
| F5 | HODL | VANECK BITCOIN ETF | 3151.90 | alternatives / Volatility | gpt-4o-mini | commodities / Commodities |
| F6 | PCEF | INVESCO CEF INCOME COMPOSITE ETF | 0.00 | fixed_income / needs_review | gpt-4o-mini | HOLD OUT (seed_pending) |

## Dollars by target class after the folds (the 18; plus 4 equity already plannable)
- equity (the 4): 15,777.17
- fixed_income, no sub-class (F2): 195994.04
- alternatives, no sub-class (F3): 167706.25
- alternatives / Real Estate (F1): 11855.56
- commodities / Commodities (F4+F5): 22008.57
- held out (F6): 0.00

Every one of these classes was set by an outside model (gpt-4o-mini or gpt-5.4-mini, held from the old rows). Provenance on each seeded row: `source_table` = `bd-securities`, `source_last_updated` = the old row's own `last_updated`.

## What I will do on your answer
Re-seat the seed cell with your fold rules as a committed map (the plan then covers 21 of 22 with PCEF held out, or whatever you rule), cut the never-widen pair with these dollars priced per class, and ship the E_18 repoint only after the seed is applied and read.

## The ask (one)
Rule F1-F6 as recommended, or name the changes.
