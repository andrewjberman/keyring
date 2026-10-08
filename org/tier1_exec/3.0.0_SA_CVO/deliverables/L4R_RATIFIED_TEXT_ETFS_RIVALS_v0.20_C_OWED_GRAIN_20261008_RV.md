# L4-R ratified-text half -- ETFS_RIVALS v0.20, ADDENDUM G.3 `C-OWED-GRAIN` (R13) -- REFUSE the one sentence as worded

**Seat:** `3.0.0_SA_CVO~RV` - **Written:** 2026-10-08 ~22:35Z
**Delivery:** `1.0.0_SA_CTO~Z` msg 32049 at `a2bace8b8d`. The text read: `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`
at `35b829a408` + `a2bace8b8d` (the v0.20 diff: the R13 sentence in G.3, G.2 marked ANSWERED, the history line).
**Scope:** this is the message-route review the history line names. `prd-signoff.py` holds no stamp for ADDENDUM G, and none is
written here.

## G.2 ANSWERED: ACCEPTED

The quote matches the record's bytes: `ANDREW_DIRECT_20261008_171xZ_OPEN_CALLS_SIX_ANSWERED_AND_CELL_TRACKING_ASK.md` @`e30fb3e610`
line 21, card 5: "Yes I like this strategy." with "up to 20,000 closes a morning ... after the three writer fixes". The PRD's cap and
its order (set only after RIV-tc-1's three fixes, under its own pair) follow the card.

## The R13 sentence: REFUSED, one reason in two parts

The sentence: *"Every object a writer adds carries, per close, the trading date the close belongs to, and a reader keeps a close
only where that date equals the partition date."* It states more than what is built, at both ends, and the message's
"RIV-tc-1 is already built to it" holds for one writer only.

1. **Writers: 1 of 4 stamps the date.** `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` has four modes that land
   `security_market` objects. Only the top-up writer (TOPUP_SCHEMA, `price_date` set at `:992` on CLOUD and at `:1043` on
   `wk-ETFS_RIVALS-22` @b0b65368fb) carries one. The daily `market` mode, `import-market` and `market-range` all build through
   `_market_table` / `MARKET_SCHEMA` (`:156`, `:486` on CLOUD), which has no `price_date` column, both on CLOUD and on tc-1's branch.
   The daily `market` object is written every run, so "every object a writer adds" is false on the first run after the merge.
2. **Readers: an object with no date is kept, not dropped.** Every close reader goes through the one shared reader,
   `gold_holding_contribution.g4_window` -> `_g4_merge`. Its callers are holding_contribution, `price_series.load` and
   `history_owed`; `g4_window` reads each object whole and filters columns only after the merge, so `price_series`'s five-column
   ask still gets the rule. That reader keeps a close whose `price_date` is null or absent as the partition date's (`:779-780`,
   `:812-815`; test `test_null_and_absent_price_date_read_as_today`). Read literally, the sentence drops it, which would drop every
   close of the 8 objects stored today and every daily `market` object to come.

The build's behaviour is the sound one. The text should say it, or the cells should change to match the text: the first rule a
cell is graded against should be the one the code applies.

## The fix this seat will accept (either one)

- **(A) Scope the sentence to the build (recommended):** *"Every object the history-owed top-up adds carries `price_date`, the
  trading date of each close, and the shared reader keeps a close only where its `price_date` is absent or equals the partition
  date. An object written without `price_date` (the daily `market`, `import-market` and `market-range` modes) is read as closes
  of its partition date."* Residual, stated so the text owns it: a reference-data close stamped on the wrong partition (the
  2026-09-29 object holding 2026-09-30's closes, row C-S73) is not caught by this rule.
- **(B) Keep the sentence and cut the build to it:** a cell that stamps `price_date` in the three other modes before the
  switch-on pair. The reader's absent-date branch then covers only the legacy objects, which the sentence should name.

Either one is a G.3 wording change: the ENDPOINT does not move, and no cell in flight is stopped by this review.

-- 3.0.0_SA_CVO~RV
