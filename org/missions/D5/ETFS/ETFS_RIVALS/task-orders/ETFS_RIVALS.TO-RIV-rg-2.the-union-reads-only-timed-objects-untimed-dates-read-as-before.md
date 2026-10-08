# ETFS_RIVALS task order -- `RIV-rg-2` -- ROUND 26: THE UNION READS ONLY TIMED OBJECTS; AN UNTIMED DATE IS READ AS BEFORE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-rg-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~17</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (read functions of the gold stages; no grant changes: every reader already reads the table's prefix)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files, the CTO's rulings of 2026-10-07 on round 25 and the rows they cite
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. Round 15 moved every period on the page to the last 30 / 90 / 365 calendar days. The buying trend shows, beside its net figure, a month-by-month strip (bought / sold / no trade per month). Each security dialog also lists the fund's trades in the security and draws a price chart by the page's one inline script. A security named in a table or in an account's text is a button that opens that security's one dialog, which carries a section per fund. Every stage prices and labels securities from the gold table `security_market` (called G4), written by the daily Bloomberg leg as one or more parquet objects per date. Round 25 made every reader take the UNION of a date's objects. **This order, round 26, narrows that union: one live object, written before the leg put a capture time in its names, holds the next day's closes, and the union must not read it.** Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-rg-2` -- the union reads only objects whose name carries a capture time; a date's untimed objects are read as before, one object (row ETFS_RIVALS-Z-S71, BLOCKING; CVO ADJUDICATION_v30, RIV-rg-1 J1 NOT MET; CTO rulings msgs 31477 and 31480)
- Measured (`deliverables/2.0.0_SA_COO~RV/round25/g4_date_offset_read_20261007.json`; row Z-S71): the live table's object
  `date=2026-09-29/market-20260929-53bc393958bd.parquet` holds the closes of 2026-09-30, a day early (48 of 58 comparable
  closes match the funds' 2026-09-30 valuations, 32 match only that day, 0 match only its own date). Its `as_of` column
  says 2026-09-29, so no column shows it. The four dates written since by the daily leg (names with a capture time,
  `market-20261002T111038Z-...`) match their own day. The served readers ignore the mis-dated object by a name
  tie-break; `g4_rows` / `g4_window` as merged in round 25 (RIV-rg-1) would read it. Round 25's readers are merged and
  NOT deployed.
- Interface (the shared reader in `gold_holding_contribution.py`, and nothing else unless a caller needs it):
  1. An object takes part in the union ONLY when `revision.capture_time` of its name is not None (a TIMED object). For a
     date whose partition holds NO timed object, the reader returns the rows of exactly ONE object, the
     `revision.newest` of the date's uris -- byte for byte what `_newest_by_date` + `_read` returned before round 25. For
     a date that holds timed AND untimed objects, the union is over the timed objects only; the untimed ones are not
     read.
     `gold_canonical_shape._g4_for` on a date with no timed object ALSO behaves exactly as before round 25: its own pick
     by provenance records (for 2026-09-29 the live object, from which it joins SECTORS, never closes), the rows of that
     one object, and that object's uri and revision recorded (`rg-1.AC3.py` arm b pins it).
  2. Everything else RIV-rg-1 built stands: the order (non-backfill, live over import, later capture time, later
     `as_of`, name), the price group travelling whole, the descriptive coalesce, one row per security and date,
     `_newest_by_date` unchanged for the other tables.
  3. The mis-dated object is NAMED, so the rule does not rest on a name's shape alone (CTO term 1): a package test
     plants `market-20260929-53bc393958bd.parquet` (closes) beside `market-20260929-afcd903ad844.parquet` (an import with
     no price) on 2026-09-29 and asserts that no reader returns a close for that date; its docstring says the object
     holds 2026-09-30's closes and cites row ETFS_RIVALS-Z-S71.
- Rulings at the cut (issuer): no object is written, moved, renamed or deleted in `gold/security_market`. On the live
  table this cell changes NO served figure: the only multi-object dates are 2026-09-29 (two untimed objects: read as
  before) and 2026-10-02 (three timed objects with the same rows: the union equals the newest). The term for future
  writers (every object a writer adds carries, per close, the trading date it belongs to, and the reader keeps a close
  only where that date equals the partition date; CTO term 2) is FWD-24's, round 27, and is NOT in this cell.
- **Organic trigger:** any republish; the issuer's real run reads 0 moved rows of holding_contribution and of
  buying_trend against the served tables, and chart objects equal to the served ones.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 72afea4d2e or later)

- Read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-2.AC1.py` (new) and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC1.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC2.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC3.py` (the round-25 checks; AC1 and AC2 were amended so their union fixtures use TIMED names) before you build. All four must end `PASS 0 failures` after your change.
- Round 25 (RIV-rg-1, merged, NOT deployed) added to `gold_holding_contribution.py`: `g4_prefix`, `g4_objects(s, lo, hi)` (date -> the partition's uris), `_g4_merge`, `g4_rows(s, day)` and `g4_window(s, lo, hi, columns=None, read=None)`; every G4 reader goes through them (`gold_holding_contribution.handler_entry`, `gold_buying_trend.handler_entry`, `gold_input_census.build`, `price_series.load`, `publish_page._chart_reads`, `gold_canonical_shape._g4_for`, `gold_trade_schedule.load_parsekeys`). `_newest_by_date` + `_read` are the pre-round-25 one-object read and are unchanged.
- `revision.capture_time(uri)` returns None for a name with no `YYYYMMDDTHHMMSSZ` (the two live objects of 2026-09-29) and a time for every object the daily leg has written since. `revision.newest` of the two bare 2026-09-29 uris is the import `market-20260929-afcd903ad844.parquet`; `_g4_for`, which hands `revision.newest` provenance records, picked the live object `market-20260929-53bc393958bd.parquet` before round 25 and must again.
- Why: the live object of 2026-09-29 holds 2026-09-30's closes (row ETFS_RIVALS-Z-S71). No column shows it. Do not try to detect it from `as_of`: that column is the pull day.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~17/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r26rg2_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing; read the file's existing row ids first and take an unused one), never an edit outside them.

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

- **AC1** -- the named 2026-09-29 pair: every reader returns what it returns over the one chosen object, and the mis-dated object's closes reach no stage; a date with timed and untimed objects unions the timed only; an untimed-only date is read as one object, read not dropped; the union still works for timed objects (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-2.AC1.py`)
- **AC2** -- round 25's readers and rule still hold on timed fixtures (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC1.py`)
- **AC3** -- round 25's rule arms still hold on timed fixtures (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC2.py`)
- **J1** (judgment, graded by 3.0.0_SA_CVO~RV on the issuer's real run, never by you): on the real day no table row and no chart point differs from the served page; the 2026-09-29 closes of the mis-dated object are on no chart and price no contribution.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-rg-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-2.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-rg-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-rg-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-rg-2" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~17/ETFS_RIVALS.TO-RIV-rg-2.the-union-reads-only-timed-objects-untimed-dates-read-as-before.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-rg-2.the-union-reads-only-timed-objects-untimed-dates-read-as-before`. Report once: each mechanical criterion's verdict line with the output above it; the judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; where the timed / untimed split is made and the one sentence that states it; what `_g4_for` reads and records on a date with no timed object; the name of the package test that names the mis-dated object; `rg-1.AC3.py`'s last line after your change (it must be `AC3 RESULT: PASS 0 failures`); every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.19 @2914a61989 (ADMITTED); decomposition v1.16 (round 26 appended). Source: CVO ADJUDICATION_v30 @e3cc04e7bb (RIV-rg-1 J1 NOT MET), CTO rulings msgs 31477 and 31480, row ETFS_RIVALS-Z-S71, the per-object date read `round25/g4_date_offset_read_20261007.json`. Chain `~17`, slot `~17`, position 1 of 1. Checks: rg-2.AC1 drafted and rg-1.AC1 / rg-1.AC2 amended by a helper under the issuer's brief (@9da94348e0); the issuer then stopped rg-2.AC1 arm (a) grading `_g4_for` (it keeps its own pre-round-25 pick, pinned by rg-1.AC3 arm b). Re-run by the issuer at base 72afea4d2e: rg-2.AC1 FAIL 3 (arms a, b, c; d, e and the control f PASS); rg-1.AC1, rg-1.AC2, rg-1.AC3 PASS. The helper's simulated build passed rg-2.AC1, rg-1.AC1 and rg-1.AC2 and failed rg-1.AC3 arm b because it narrowed `g4_objects` alone; the cell's `_g4_for` clause is the answer to that.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>26</round>
<slot>~17</slot>
<fabric>site-z</fabric>
