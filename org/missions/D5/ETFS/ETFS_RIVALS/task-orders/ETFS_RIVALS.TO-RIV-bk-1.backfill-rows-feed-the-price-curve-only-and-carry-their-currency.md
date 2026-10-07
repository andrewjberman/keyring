# ETFS_RIVALS task order -- `RIV-bk-1` -- ROUND 20 (REPAIR): BACKFILL ROWS FEED THE PRICE CURVE ONLY AND CARRY THEIR CURRENCY; THE TREND'S PARSEKEY JOIN READS ITS COLUMN

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-bk-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~10</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the backfill is ad hoc by Andrew's word and is run by the issuer, never scheduled)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (the mode reads and writes the table and the ledger it already reads and writes)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files and the backfill-preparation record
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding with a price curve, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. The gold table G4 `security_market` holds one parquet per date of Bloomberg closes. Round 15 built an ad hoc backfill of past dates into it (`enrichment_bloomberg` mode `market-range`), for the dialog's price curve only; it has never run. **This order, round 20, is one repair cell before it runs.** Nothing here deploys, merges or calls a vendor: every Bloomberg hook is stubbed, and no worker ever makes a Bloomberg request. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-bk-1` -- backfill rows feed the price curve only, carry their currency, and a range can be finished on a later day; the trend's parsekey join reads its column (rows Z-S60, Z-S61; CTO ruling 30897)
- Measured (backfill preparation, read-only, `deliverables/2.0.0_SA_COO~RV/backfill_prep/`): 863 securities x 252 trading
  days = 217,476 points against a 120,000-point daily allowance. Read in code: `gold_holding_contribution._daily` prices
  a holding-day from two consecutive G4 closes before the holding-implied return, and a newer G4 object makes the next
  publish rebuild that table, so backfilled closes would move every fund's served rankings; `_market_range` writes rows
  with `px_close` only (currency NULL), marked `as_of_source == "backfill"`, and no reader filters on that mark;
  `gold_buying_trend.handler_entry` reads G4 as `("security_id", "date", "security_name")`, so `parsekey_map(g4)` is
  always `{}` there (morning pass 2026-10-07: holding_contribution MERGED 13, buying_trend SPLIT 7).
- Interface:
  1. `gold_holding_contribution.drop_backfill(g4) -> DataFrame` returns the frame without rows whose `as_of_source` is
     exactly `"backfill"` (a frame with no such column is returned unchanged). `handler_entry`'s own G4 read loads
     `as_of_source` and drops those rows before anything else uses the frame: a day's table is identical with and
     without backfill-marked rows present in G4.
  2. `gold_canonical_shape`: when it picks the G4 partition for a report date (`_g4_for`), a partition whose rows are
     all backfill-marked is never picked (it falls back to the nearest earlier partition holding a non-backfill row),
     and a backfill-marked row never fills GICS.
  3. `enrichment_bloomberg` mode `market-range`: every backfill row carries `currency`. A security's currency is its
     STORED one (the `currency` of its newest non-backfill G4 row, read through the sink); for a security with no stored
     currency the mode makes ONE reference request for the single field `CRNCY` for exactly those securities, through
     the client hook the mode already uses, with `bbg_budget.check_points` before and `bbg_budget.record` after (points =
     securities asked); a security with no answer gets `None`. A dry run's plan gains `"currency_lookups"`. The plan's
     `points` and the budget check count only the dates NOT already held, so a range is finished on a later day inside
     that day's allowance; the ceiling and the reserve are untouched.
  4. `gold_buying_trend.handler_entry`'s own G4 read loads `security_parsekey`.
- Rulings at the cut (issuer): `price_series` and the chart object keep reading backfill rows (that is what they are
  for). Nothing under `integrations/` changes and no field other than `CRNCY` is added. The daily market pull already
  asks `CRNCY` per security, so a currently-held security takes its stored currency and costs no lookup. A reference
  request that fails leaves the run FAILED with nothing landed, like a failed historical batch. No stage marker is
  written. Input-census and trade-schedule readers are untouched (a backfill row's name, sector and parsekey are NULL
  and those readers skip blanks). A held date is neither counted NOR asked: each batch's historical request is sent
  once per contiguous run of un-held trading days, and the ledger records exactly what is asked (securities x the days
  of that run). The stored-currency read lists G4 from the range's first day to the run date and no further back. When
  no partition holding a non-backfill row exists at or before a report date, `_g4_for` answers as it does today when no
  partition exists at all. The round-15 checks `bf-1.AC1.py` and `bf-1.AC2.py` pin the mode as first built (no reference
  request; one request per batch over the whole range; a held date counted in the plan and the ledger): the cell may
  change in those two files ONLY the figures, request shapes and the "no reference request" clause that these rulings
  change, and nothing else.
- **Organic trigger:** the issuer's backfill run (never a worker's), split over the days the ledger's room allows, each
  after that day's 07:00 America/New_York vehicle run; the issuer's DELTA 0 proof on the served rankings (ruling term 1).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 2aba59986e or later)

- The check files' docstrings are the exact interface they read: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bk-1.AC1.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bk-1.AC2.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bk-1.AC3.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/_common.py` before you build. Where a docstring and the cell's "Rulings at the cut" differ, the RULING wins and the check accepts it.
- `enrichment_bloomberg.py`: `BACKFILL_SOURCE = "backfill"`; `_market_range(event, s, batch_id, produced_at, out)` plans, checks the budget, sends one historical `PX_LAST` request per batch and lands one object per date through `market_rows(data, d, MARKET_SOURCE_HIST, prov, BACKFILL_SOURCE)`; `_held_dates(s, days)` lists the dates that already hold a `market-*.parquet` object (those are skipped today, but still counted in the plan and the ledger). `bbg_budget.py`: `remaining(today)`, `check_points(points, today)`, `record(...)`.
- `gold_holding_contribution.py`: `handler_entry` reads G4 over a window through `_newest_by_date` and a column tuple; `_prices`, `_daily`, `g4_names`, `parsekey_map` consume the frame. `price_series.py` reuses `gold_holding_contribution` helpers and MUST keep seeing backfill rows: do not put the drop inside a helper `price_series` calls.
- `gold_canonical_shape.py`: `_g4_for` picks the greatest partition date at or before the report date and `apply_g4` fills GICS from it, skipping a blank sector.
- `gold_buying_trend.py` `handler_entry`: the G4 read's column tuple is the whole of change 4; `build` already calls `parsekey_map(g4)`.
- The round-15 checks `bf-1.AC1.py` and `bf-1.AC2.py` pin the mode as first built; they must end `PASS 0 failures` on your branch. By the ruling above you may change in those two files only what the rulings change: `bf-1.AC2.py` arm (a) asserts no reference request and one historical request per batch over the whole range, and its ledger arm sums the points with the held date counted. Quote every line you change, before and after, in your report; the issuer diffs both files at the merge.
- Existing package tests that pin the same figures are yours to re-pin; say which and why.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/` except the two check files named in your `<paths>`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-22, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~10/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r20bk1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing; read the file's existing row ids first and take an unused one), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/gold_holding_contribution.py
data/etfs/scripts/rivalfunds/gold_canonical_shape.py
data/etfs/scripts/rivalfunds/enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/gold_buying_trend.py
data/etfs/scripts/rivalfunds/bbg_budget.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bf-1.AC1.py
org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bf-1.AC2.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the rankings stage and the canonical-shape stage ignore backfill-marked G4 rows: a day's table is equal with and without them; control: the planted rows are in the fixture and would have been used (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bk-1.AC1.py`)
- **AC2** -- the backfill mode stamps every row's currency (stored, else one CRNCY reference request through the budget ledger), reports the lookups in its plan, and counts only un-held dates; control: the stub records the historical requests (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bk-1.AC2.py`)
- **AC3** -- the trend stage's own G4 read loads the parsekey column and one security under a CUSIP and a Bloomberg key becomes one key; control: the join's map holds the pair (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bk-1.AC3.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-bk-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bk-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-bk-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bk-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-bk-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bk-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~10/ETFS_RIVALS.TO-RIV-bk-1.backfill-rows-feed-the-price-curve-only-and-carry-their-currency.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-bk-1.backfill-rows-feed-the-price-curve-only-and-carry-their-currency`. Report once: each mechanical criterion's verdict line with the output above it; files written; where the backfill rows are dropped in each of the two stages and why `price_series` still sees them; how the reference request is built and which hook sends it; the final lines of `bf-1.AC1.py` and `bf-1.AC2.py` on your branch; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.18 @6e245cbebe (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.10 (round 20 appended). Source: rows ETFS_RIVALS-Z-S60 and ETFS_RIVALS-Z-S61 @fc82330f20 and the ruling of 1.0.0_SA_CTO~Z msg 30897 (the REC, shapes (a) (b) (c); term 1 DELTA 0 on served rankings, published with and without backfill-marked rows, every fund's holding_contribution table equal -- the issuer's proof at the drain, not a worker criterion; term 2 CRNCY one added reference field, a separate request only for formerly-held keys, every row through bbg_budget; term 3 split by the ledger's own room; term 4 no backfill request before that day's 07:00 America/New_York vehicle has completed). Chain `~10`, slot `~10`, position 1 of 1. Check files drafted by a helper under the issuer's brief and re-run by the issuer at the base before this issuance: see the issuance commit for each base verdict.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>20</round>
<slot>~10</slot>
<fabric>site-z</fabric>
