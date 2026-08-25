# ANDREW-DIRECT 2026-08-24 ~23:44Z -- ORDER ON ECONOMY CODE; "I REALLY DONT CARE IF ITS OFFICIAL GICS"

**Seat:** `1.0.0_SA_CTO~Z` (site Z) · answers the item-5 card put at 23:38Z ·
**recorded + broadcast same turn** (5899-5903, 5/5 DELIVERED).

## HIS WORD, VERBATIM AND COMPLETE

> *"If you have access to economy code for these securities we can order based on that instead of
> GICS, i really dont care if its official gics or some general economy/sector thing, whatever we
> can get."*

## THE CARD IT ANSWERS

His two earlier phrases named **different sequences** and I refused to pick between his own words:

| his phrase | the order it names |
|---|---|
| *"canonical Sector/GICS ordering"* | `SECTOR_INDICES` -- 10,15,20,25,30,35,40,45,50,55,60 (Energy first) |
| *"how the frontend handles it in Portfolio Management (Yang was very adamant)"* | `ECONOMY_ORDER` -- 25,45,40,10,15,20,50,35,30,55,60,65,90,95 (Consumer Discretionary first) |

**He has now resolved it toward the second and explicitly released the canonicality requirement.**

## ⭐ MEASURED: WE ALREADY HAVE IT, AT ZERO ADDITIONAL COST

`ECONOMY_ORDER`'s own comment (`PortfolioManagement/constants.ts:103`) reads
*"Canonical sector/economy ordering (GICS codes)"*, and our served `sub_asset_class` values are GICS
sector **names**, already pulled in `GICS_SECTOR_NAME`. Name -> code is a fixed 11-row map.

```
Consumer Discretionary  25 -> 0     Communication Services  50 -> 6
Information Technology  45 -> 1     Health Care             35 -> 7
Financials              40 -> 2     Consumer Staples        30 -> 8
Energy                  10 -> 3     Utilities               55 -> 9
Materials               15 -> 4     ---- MAPPED: 10 of 10 sectors ----
Industrials             20 -> 5     Cash & Cash Equivalents / None: UNMAPPED
```

**No new Bloomberg field, no new request, no second data source.** His *"whatever we can get"* is
satisfied by what the pipeline already pulls.

## THE ORDERING CONTRACT, RULED

1. **`GICS_SECTOR_NAME` -> GICS code -> `ECONOMY_ORDER.indexOf(code)`.** Matches PM's actual behaviour
   (`TradeTab.tsx:255-262, :286-287`), so Models and ETFs show one order -- which is what his
   pointing at PM was for.
2. **The mapping is a DECLARED CONSTANT, not a runtime inference.** 11 rows, in code, testable.
   ⚠ **Keyed on the spelling OUR DATA USES** (`Health Care`, `Information Technology`) -- which is
   `SECTOR_INDICES`' spelling and **NOT** `SECTORS`' (`Healthcare`/`Technology`). That is the
   collision flagged earlier, arriving at the one place it can actually fire.
3. **`Cash & Cash Equivalents` and unmapped values APPEND AFTER the ten, DECLARED, not given a fake
   code.** `ECONOMY_ORDER` carries trailing `65, 90, 95` which are not GICS sectors -- reuse them if
   they have known meanings in PM (rung 2), otherwise append and say so.
   ⛔ **Do not invent a code for Cash to make the sort uniform: an identifier that means nothing is
   worse than a declared exception.**
4. **The `None` row (TPG) sorts LAST and stays VISIBLY unlabelled.** It is a real defect with an
   owner; hiding it inside a sort order is the safe-and-invisible conversion this round keeps
   refusing.

## CONSEQUENCE

**Item 6 is unblocked.** Light-to-dark can be assigned now that an order exists. The composition rule
stands unchanged: **technique and colour families from the Models ramp (`SUB_ASSET_CLASS_COLORS`),
ORDER from (1).** Two inputs, not a port -- the key sets do not overlap, so it is a new table built
to the same construction rule.
