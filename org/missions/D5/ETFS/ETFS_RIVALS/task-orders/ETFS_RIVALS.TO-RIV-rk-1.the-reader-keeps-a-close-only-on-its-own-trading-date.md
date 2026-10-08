# ETFS_RIVALS task order -- `RIV-rk-1` -- ROUND 27: THE READER KEEPS A CLOSE ONLY ON ITS OWN TRADING DATE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-rk-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~20</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (read functions of the gold stages; no grant changes)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files, the CTO's rulings of 2026-10-07 on round 25 and the rows they cite
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. Round 15 moved every period on the page to the last 30 / 90 / 365 calendar days. The buying trend shows, beside its net figure, a month-by-month strip (bought / sold / no trade per month). Each security dialog also lists the fund's trades in the security and draws a price chart by the page's one inline script. A security named in a table or in an account's text is a button that opens that security's one dialog, which carries a section per fund. The page's price charts and rankings read closes from the gold table `security_market`, which today holds five trading days. PRD outcome FWD-24: every security a tracked fund held in the last 365 days has its year of closes, kept by the daily Bloomberg leg, which prints what is owed, asks inside the budget and carries the rest. **This order, round 27, is one of three cells of that outcome; the standing request to the vendor stays OFF in everything you build and test.** Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-rk-1` -- the reader keeps a close only where its own trading date equals the partition date; an untimed date that gains a timed object keeps its sectors; a backfill close does not cost a security its sector (CTO ruling R13; CTO half @e081a672d4 note; worker row Z-W15-S2)
- Measured: `gold_holding_contribution.g4_objects` / `_g4_merge` (rounds 25, 26). No stored object carries a per-close
  date today, so nothing tells the reader that a close belongs to another day (row Z-S71). On a date with untimed
  objects only (2026-09-29) the reader returns one object, an import with sectors; the first timed top-up landed there
  would make the union "timed only" and drop those sectors. And a security whose live row has no close while a backfill
  row has one merges to a backfill-marked row, which `drop_backfill` then removes whole, sector and parsekey included.
- Interface (`gold_holding_contribution.py`; `gold_canonical_shape.py` only if `_g4_for` needs it):
  1. THE PRICE DATE. Where a row carries a non-null `price_date`, its price group (`px_close`, `total_return_index`,
     `currency`, `as_of`, `source`, `as_of_source`, `price_date`) takes part in the merge only when `price_date` equals
     the partition date; otherwise that row offers no price group (its descriptive fields still coalesce). A row with no
     `price_date` column, or a null one, is treated as today (every stored object).
  2. THE UNTIMED DATE THAT GAINS A TIMED OBJECT. On a date holding timed AND untimed objects, the ONE untimed object
     the pre-round-25 read picks (`revision.newest` of the date's untimed uris) contributes its DESCRIPTIVE fields to
     the merge, last in the order, and NEVER a price group. Other untimed objects are still not read.
  3. THE BACKFILL CLOSE. `drop_backfill` no longer removes a merged row whose price group came from a backfill row when
     any of its descriptive fields came from a non-backfill row: it returns the row with the price group nulled
     (so the rankings price it as they do today, from the fund's valuation) and the descriptive fields kept. A row
     whose every contributing object is a backfill object is still dropped. The price series (`price_series.load`)
     still receives the backfill close.
  4. Everything rounds 25 and 26 built stands; on the live table NOTHING read today changes (no stored object carries
     `price_date`; no date mixes timed and untimed objects; no backfill row exists).
- Rulings at the cut (issuer): the column is named `price_date` in both this cell and RIV-tw-1. No object is written,
  moved or deleted.
- Rulings on the check drafter's questions (issuer): `price_date` may arrive as an ISO string or a date; both compare
  to the partition date. In item 2 a security present ONLY in the picked untimed object, with no non-null descriptive
  field there, yields NO row (so `rg-2.AC1.py` arm c stands unchanged). Descriptive fields are every column outside
  the price group. Item 3 also binds `gold_canonical_shape._g4_for`: a merged row whose price group came from a
  backfill row while a descriptive field came from a non-backfill row stays in its sector join (today it filters the
  merged frame on `as_of_source`); `rk-1.AC1.py` does not grade that, so the cell's package test does. Item 4 is the
  issuer's own measurement of the live table on 2026-10-07 and 2026-10-08: 8 objects over 5 dates, the two untimed on
  2026-09-29 alone, no `price_date` column anywhere, `as_of_source` absent or `pull` on every row.
- **Organic trigger:** any republish; the issuer's real run reads 0 moved rows and identical charts.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 66cab2698e or later)

- Read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rk-1.AC1.py` before you build, and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-2.AC1.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC1.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC2.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rg-1.AC3.py`, which must all still end `PASS 0 failures` (rk-1.AC1 arm f runs them).
- `gold_holding_contribution.py` after rounds 25 and 26: `g4_objects(s, lo, hi)` returns, per date, the uris read (timed objects only; an untimed-only date: the one `revision.newest` uri); `_g4_merge` orders a (security, date)'s rows (non-backfill, live over import, later capture time, later `as_of`, name) and builds one row, the price group whole from the first row with a close, the other columns first non-null; `g4_rows` / `g4_window` call them; `drop_backfill(df)` removes rows whose `as_of_source` is `backfill` and is applied by the rankings stage after the read; `price_series.load` does not apply it. `gold_canonical_shape._g4_for` filters the merged frame on `as_of_source` for its sector join and, on a date with no timed object, keeps its own pre-round-25 read.
- A scheduled job outside this product loads `gold_holding_contribution` and calls `_newest_by_date`, `_blank`, `target_uri`, `parquet_bytes` and `_content_sha`: do not change their signature or behaviour.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~20/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r27rk1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing; read the file's existing row ids first and take an unused one), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/gold_holding_contribution.py
data/etfs/scripts/rivalfunds/gold_canonical_shape.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a close whose `price_date` is another day is not read and its sector still is; rows without a `price_date` read as today; an untimed date that gains a timed object keeps the picked untimed object's sectors and takes no close from an untimed object; a backfill close leaves the live row's sector and parsekey in the rankings read; eight neighbouring checks still PASS (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rk-1.AC1.py`)
- **J1** (judgment, graded by 3.0.0_SA_CVO~RV on the issuer's real read, never by you): on the real day no table row and no chart point differs from the served page.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-rk-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rk-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-rk-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~20/ETFS_RIVALS.TO-RIV-rk-1.the-reader-keeps-a-close-only-on-its-own-trading-date.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-rk-1.the-reader-keeps-a-close-only-on-its-own-trading-date`. Report once: each mechanical criterion's verdict line with the output above it; the judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; where each of the three rules lives, one sentence each; how `drop_backfill` knows a descriptive field came from a non-backfill row; what `_g4_for` does with such a row and the name of the package test that pins it; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.19 @2914a61989 (ADMITTED); decomposition v1.17 (round 27 appended). Source: PRD ADDENDUM G (FWD-24), ROUND_ANALYSIS.round22 ADDENDUM 4 and CTO ruling R13. Also the CTO half @e081a672d4's note for round 27 and worker row Z-W15-S2. Chain `~20`, slot `~20`, position 1 of 1. Check drafted by a helper under the issuer's brief (@80327807d9), re-run by the issuer at base 66cab2698e: rk-1.AC1 FAIL 3 (arms a, c, d; arms b, e, g and the eight regression arms PASS). The helper's simulated build passes; four planted defects fail the arms that grade them. The helper found the cell as first written contradicted rg-2.AC1 arm c; the ruling in the cell (no row for a security the picked untimed object holds with no descriptive field) resolves it.

**AMENDMENT 1 (issuer, 2026-10-08, before any worker was spawned; no criterion, path or ruling changes):** this order's cell id, RIV-rk-1, is also the id of an older, closed order (`ETFS_RIVALS.TO-RIV-rk-1.holding-contribution`). The two are told apart by file name and round (this one: round 27, check `rk-1.AC1.py` under `round15/checks/`, tests `test_r27rk1_*.py`). A rename to an unused id was tried and the issuance gate refuses it as a second issuance in the round (row ETFS_RIVALS-Z-S74), so the id stands. No gate limb graded this note.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>27</round>
<slot>~20</slot>
<fabric>site-z</fabric>
