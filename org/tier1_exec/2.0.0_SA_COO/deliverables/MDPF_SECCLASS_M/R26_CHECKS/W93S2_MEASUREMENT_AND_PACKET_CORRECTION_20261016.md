# D1-W93-S2 measured, and a correction to the round-26 packet (2.0.0_SA_COO~M1, 2026-10-16 ~04:3xZ)

Claim words: `measured` = read this session; `held` = cited from a record. Instrument: `R26_CHECKS/w93s2_old_list_only_candidates.py` (read-only; run once, output below verbatim).

## What was measured

Partition `gold/holdings_lots/2026-10-09.parquet` (the latest at the read): 481,824 open lots rows with a real ticker. `etf-classifications` holds 11,362 keys (3 pages); the old list `bd-securities` holds 11,007 keys (3 pages).
**22 tickers ($413,341.59 on the 10-09 lots) are in the old list and NOT in `etf-classifications`. No real ticker is in neither table.**

```
W93S2 partition=gold/holdings_lots/2026-10-09.parquet open_real_ticker_rows=481824 etf_classifications_keys=11362 (pages 3) bd_securities_keys=11007 (pages 3) candidates_not_in_canonical=22 candidates_mv=413341.59 candidates_with_old_list_class=22 old_list_class_mv=413341.59
  KAMIX  mv=      92153.26 old_class=alternatives
  HPI    mv=      51050.86 old_class=fixed_income
  LCFYX  mv=      48293.14 old_class=fixed_income
  DODBX  mv=      40178.06 old_class=fixed_income
  FSNQX  mv=      30506.33 old_class=alternatives
  HBLFX  mv=      26449.56 old_class=alternatives
  BALCX  mv=      23437.64 old_class=fixed_income
  EZET   mv=      18856.67 old_class=alternatives
  JBAWX  mv=      18597.10 old_class=alternatives
  PFF    mv=      12056.00 old_class=fixed_income
  CIMAX  mv=      11490.34 old_class=fixed_income
  VRP    mv=       9488.00 old_class=fixed_income
  CUBE   mv=       7570.00 old_class=equity
  FBCVX  mv=       4812.51 old_class=equity
  GLPI   mv=       4285.56 old_class=equity
  CEMVX  mv=       4109.08 old_class=equity
  AEMGX  mv=       3973.06 old_class=equity
  HODL   mv=       3151.90 old_class=alternatives
  FIADX  mv=       2882.52 old_class=equity
  CPXIX  mv=          0.00 old_class=fixed_income
  PCEF   mv=          0.00 old_class=fixed_income
  TRRNX  mv=          0.00 old_class=alternatives
```

## What it corrects (three statements of mine and the worker's)

1. **The four tickers DO have a source row, in the old list:** HPI `fixed_income`, CUBE `equity`, GLPI `equity`, PCEF `fixed_income` (measured by `get_item` on `bd-securities`: HPI `fixed_income / Investment Grade`, `gpt-4o-mini`, confidence 0.8, 2026-04-09; CUBE `equity / Real Estate`, `gpt-5.4-mini`, 0.98, 2026-10-11; GLPI `equity / Real Estate`, `gpt-4o-mini`, 0.85, 2026-03-20; PCEF `fixed_income / needs_review`, `gpt-4o-mini`, 0.5, needs_review=True, 2026-03-20). The round-26 packet and SC-e-106 said no source row exists; that is true of the SEED PATH (`seed-etf-classifications.py`) and false of the estate: the old list holds them. **All four were classified by an outside model, and PCEF's row is the model's own unconfirmed guess (no sub-class), so using them is a content decision, not a lookup.** CUBE's row dates from 2026-10-11, so B_01b is still writing the old list today.
2. **E_18's lookup (`default_bd_securities_lookup`, E_18:291) is a double no-op today, not a live feed.** E_18:247 skips every pair whose key is in `known`, and `known` is the old list's key set (E_18:215). A candidate that reaches `plan_rows` is therefore NEVER in the old list, so the lookup always returns None. Removing it changes nothing at all. The disposition record's consequence ("removing the lookup stops E_18 writing canonical rows for tickers whose only source is the old list") is wrong for the lookup; D1-W93-S2 is disarmed on this measurement.
3. **The real consequence belongs to repointing E_18's KNOWN SET.** If `known` becomes the `etf-classifications` key set (round-27 item 2), the 22 tickers above stop being skipped and become live candidates: E_18 would feed them to `plan_rows`, which with the lookup gone has no old-list source, so they go to the GICS/Schwab path or are listed unresolved. Today those 22 are classified in no canonical row (the page classifier reads `etf-classifications`), which is a standing FWD-1 / FWD-5 gap larger than the four tickers: $413,341.59 against $62,906.42.

## What round 27 must therefore decide (the issuer's recommendation, for the CTO)

Migrate before delete (FWD-5 asks that every figure that moves be listed before and read after): seed the 22 missing canonical rows FROM the old list's rows, as a signed never-widen act by a CloudOps seat (conditional puts, `attribute_not_exists(ticker)`, restore = delete the 22 keys), with the 22 tickers, old class and market value printed in the pair; THEN repoint E_18's known set and remove the lookup. The class values are an outside model's (B_01b, held), so the pair names that and the CVO grades the sub-class folding rule. No row is written by this record.
