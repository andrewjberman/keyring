# ETFS_RIVALS task order -- `RIV-rg-1` -- ROUND 25: A DATE'S MARKET ROWS ARE THE UNION OF ALL ITS OBJECTS, ONE ROW PER SECURITY BY A STATED RULE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-rg-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~15</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (read functions of the gold stages; no grant changes: every reader already reads the table's prefix)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files, the CTO's rulings of 2026-10-07 on round 25 and the rows they cite
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. Round 15 moved every period on the page to the last 30 / 90 / 365 calendar days. The buying trend shows, beside its net figure, a month-by-month strip (bought / sold / no trade per month). Each security dialog also lists the fund's trades in the security and draws a price chart by the page's one inline script. A security named in a table or in an account's text is a button that opens that security's one dialog, which carries a section per fund. Every stage prices and labels securities from the gold table `security_market` (called G4), written by the daily Bloomberg leg as one or more parquet objects per date. **This order, round 25, repairs how that table is READ: today every reader keeps one object per date, and on one live date the object kept is an import with no price, so that day's 430 market closes reach no stage.** Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-rg-1` -- a date's rows of gold security_market are the union of ALL its objects, one row per security and date by a stated rule (row ETFS_RIVALS-Z-S69, BLOCKING; PRD v0.19 C-OWED-GRAIN, G.4; CTO rulings msgs 31416, 31428)
- Measured (census `deliverables/2.0.0_SA_COO~RV/round25_prep/READER_CENSUS_SECURITY_MARKET_20261007.md` @33e8bbe318, and
  the live table): every reader of G4 rows takes ONE object per date, `revision.newest` of the date's uris. For
  2026-09-29 the partition holds a live pull `market-20260929-53bc393958bd.parquet` (434 securities, 430 with `px_close`,
  `source` `blp_client.reference_data`) and an import `market-20260929-afcd903ad844.parquet` (172 securities, 0 with
  `px_close`, 164 with a GICS sector, `source` `import:bbg/2026-09-29/characteristics.parquet`). Neither name carries a
  capture time and the readers hand `revision.newest` bare uris, so its "an import never outranks a live object" rule
  cannot apply and the NAME decides: the import wins and all 430 market closes of that day reach no stage (355
  fund-security chart entries of the served page then draw that day from the fund's own valuation). On 2026-10-02 three
  objects of 601 rows hold the same securities: the control.
- Interface (in `data/etfs/scripts/rivalfunds/`; no new module is required, one shared function is):
  1. ONE function, used by every reader below, returns a date's G4 rows as the union of ALL `.parquet` objects of that
     date's partition, ONE row per (`security_id`, `date`). Where several objects hold the same (`security_id`, `date`),
     the rows are ordered: (a) a row whose `as_of_source` is not `"backfill"` before a backfill row; (b) a row whose
     `source` does not start `import:` before an import row; (c) the later capture time in the object's name
     (`revision.capture_time`; a name with no time is oldest); (d) the later `as_of` of the row; (e) the object name,
     descending -- a last tie-break that decides only when (a) to (d) tie. From that order the merged row is built in
     TWO parts (CTO term, msg 31432). THE PRICE GROUP -- `px_close`, `total_return_index`, `currency`, `as_of`, `source`,
     `as_of_source` -- travels WHOLE from ONE row: the first row in the order whose `px_close` is not null (if none has
     a close, the first row in the order). A close is never combined with a currency, a price date or a price source
     from another object, even when its own currency is null. THE DESCRIPTIVE FIELDS -- every other column (the GICS
     columns, `security_bloomberg`, `security_parsekey`, a name) -- each take the first non-null value in the order. A
     column an older object lacks reads as null for its rows.
  2. Readers moved to it: `gold_holding_contribution._newest_by_date` + `_read` as used for G4 by
     `gold_holding_contribution.handler_entry`, `gold_buying_trend.handler_entry`, `gold_input_census.build`,
     `price_series.load` and `publish_page._chart_reads`; `gold_canonical_shape._g4_for` (still ONE date per report date,
     the greatest at or before it that holds a non-backfill row, but that date's rows are the union); and
     `gold_trade_schedule.load_parsekeys`. `_newest_by_date` keeps its one-object rule for every OTHER table (G1, G5 and
     the A1 tables are written whole per revision).
  3. For 2026-09-29 this keeps the live pull's close for every security it prices (430), the live pull's GICS where it
     has one and the import's where only the import has one. `drop_backfill` and every other row rule run AFTER the union.
  4. What a stage RECORDS as the date's G4 revision or location (for example the G4 revision inside a G1 revision in
     `gold_canonical_shape`, `location` in `gold_input_census`) stays the `revision.newest` object of the date, as today.
- Rulings at the cut (issuer): nothing is written to or deleted from `gold/security_market`; the writer
  (`enrichment_bloomberg.py`) is not in this cell. No change to `revision.py`'s ordering contract. The cost of opening
  every object of a date is accepted (8 objects over 5 dates today). `publish_page._a1_window` returning no window for
  buying_trend is NOT in this cell.
- Rulings on the check drafter's questions (issuer; the check files accept exactly these): the ONE shared function is
  `gold_holding_contribution.g4_rows(s, day)` -- `s` the sink, `day` a `YYYY-MM-DD` string -- returning a pandas
  DataFrame of that date's merged rows with every column any object of the date carries. It reads `source`, `as_of` and
  `as_of_source` to order the rows even when a caller's column filter leaves them out; a caller filters columns AFTER.
  A `px_close` of 0.0 is a close (not null). Backfill-marked rows are handled after the union exactly as today: the
  price series keeps a backfill-only row, `drop_backfill` drops it for the rankings, `_g4_for` leaves it out.
  `_newest_by_date(s, prefix, lo, hi)` keeps its signature and its one-object rule for G1, G5 and the A1 tables.
  Interface item 4 is narrowed: `_g4_for`'s recorded uri and revision stay the `revision.newest` object by its own
  provenance rule; what the input census records as a price's `location` and what the rankings manifest lists under
  `g4` may name the newest object or every object read -- say which in the report; neither is graded.
- **Organic trigger:** the next daily run and any republish; the issuer's real run prints, per fund, the rankings and
  the 30d / 90d / 365d tables before and after, each moved figure named, and the control on 2026-10-02 reads no change.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 7f7e680abf or later)

- The check files' docstrings are the exact interface they read and hold the fixtures: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC1.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC2.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC3.py` before you build. The census of every reader, with file and line, is `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round25_prep/READER_CENSUS_SECURITY_MARKET_20261007.md`: read it whole.
- Today: `gold_holding_contribution._newest_by_date(s, prefix, lo, hi)` returns ONE uri per date (`revision.newest` of the date's uris) and `_read(s, uris, columns)` concatenates one frame per date. G4 is read that way by `gold_holding_contribution.handler_entry`, `gold_buying_trend.handler_entry`, `gold_input_census.build`, `price_series.load` (prefix `_G4_PREFIX`, columns `_G4_COLUMNS`, which leave out `source` and `as_of_source`) and `publish_page._chart_reads`. `gold_canonical_shape._g4_for` picks one date and one object by provenance records; `gold_trade_schedule.load_parsekeys` picks one object per date. `revision.capture_time`, `revision.is_import` and `revision.newest` are the existing ordering contract: reuse them, do not change `revision.py`.
- Older live objects lack some columns (`as_of_source`, `security_parsekey`); an import's `source` starts `import:`; a backfill row's `as_of_source` is `backfill`. The writer (`enrichment_bloomberg.py`) is NOT yours.
- Existing package tests pin readers on single-object fixtures; they must stay green unchanged, or you say which line you re-pinned and why.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~15/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r25rg1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing; read the file's existing row ids first and take an unused one), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/gold_holding_contribution.py
data/etfs/scripts/rivalfunds/gold_buying_trend.py
data/etfs/scripts/rivalfunds/gold_input_census.py
data/etfs/scripts/rivalfunds/price_series.py
data/etfs/scripts/rivalfunds/publish_page.py
data/etfs/scripts/rivalfunds/gold_canonical_shape.py
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- every reader, through its real entry point on a local sink, reads the union of a two-object date (a live pull and an import): the live close, the import's sector where only the import has one, parsekeys from both; a planted top-up ADDS its security and removes none; control: three identical objects read as one (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC1.py`)
- **AC2** -- the rule on `g4_rows` and through the readers: non-backfill over backfill, live over import, later capture time, later `as_of`, name last; the price group travels whole from the row that has the close (a close is never given another object's currency); descriptive fields coalesce; an object lacking a column does not break the read; one row per security and date (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC2.py`)
- **AC3** -- every other table still reads one object per date; `_g4_for`'s recorded uri and revision are as today; seven neighbouring checks still PASS (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC3.py`)
- **J1** (judgment, graded by 3.0.0_SA_CVO~RV on the issuer's real run, never by you): on the real day the tables and charts of every fund read 2026-09-29 from its market closes; each figure that moves against the served page is named and explained by a close that was unused before; nothing moves on a date that had one object or identical objects.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-rg-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-rg-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-rg-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-rg-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~15/ETFS_RIVALS.TO-RIV-rg-1.a-dates-market-rows-are-the-union-of-all-its-objects.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-rg-1.a-dates-market-rows-are-the-union-of-all-its-objects`. Report once: each mechanical criterion's verdict line with the output above it; the judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; where `g4_rows` lives and each call site moved to it, by file and line; how the order (a) to (e) is computed and where the price group is taken; what the input census records as a price's `location` and what the rankings manifest lists under `g4` after your change; how many objects a 365-day read now opens against before (count them on the check's fixture, not on S3); every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.19 @2914a61989 (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.15 (round 25 appended). Source: row ETFS_RIVALS-Z-S69 (BLOCKING, ARMED) and Z-S70; CTO rulings msgs 31416, 31428, 31432; the reader census @33e8bbe318. Chain `~15`, slot `~15`, position 1 of 1. Check files drafted by a helper under the issuer's brief (@beff6be3e7), one clause of rg-1.AC3 arm b relaxed by the issuer (the census location and the manifest's g4 are printed, not graded), re-run by the issuer at base 7f7e680abf: rg-1.AC1 FAIL 8 (arms a to g; control h PASSES); rg-1.AC2 FAIL 8 (controls c and i PASS); rg-1.AC3 PASS (a guard). The helper's simulated conforming build passes all three and nine planted defects each fail the arms that grade them. The deploy of this cell moves served figures: its never-widen pair carries a before and after of every fund's tables (CTO ruling msg 31428).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>25</round>
<slot>~15</slot>
<fabric>site-z</fabric>
