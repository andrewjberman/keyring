# ETFS_RIVALS task order -- `RIV-gd-1` -- ROUND 9 (ENRICHMENT): CLASSIFY THE G5 HISTORY DRIFT: WHICH CODE CHANGE MOVES WHICH COLUMNS ON WHICH DATES (a read, no replay)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-gd-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~6</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the issuer registers any stage at the merge)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 9** (the round-8 analysis, 8 items): the IDVZ/PFOE backfill made purely additive (the trade schedule rebuilds only named funds), their daily join through a rivalfunds-owned gate file, an incremental security list, the AI-text name links, real names for past holdings, a measured Bloomberg capacity budget, and a read of the G5 history drift. Nothing in round 9 deploys, merges, flips a gate or calls Bloomberg from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-gd-1` -- the G5 history-drift classification (round-8 analysis item 7, row Z-S29)
- Measured by the D12 Step B mirror dry run: a G5 built by current code differs from the live G5 on most of 189 dates for the
  funds other than IDVZ/PFOE (confidence 176 dates, action 99, est price 99, discretionary_shares 43, income_funded 10, row count
  3; est_price_source and key_resolution new on 183).
- Interface: `data/etfs/scripts/rivalfunds/tools/g5_drift.py` (live S3 READ-ONLY; G5 rebuilt into a LOCAL sink) writes
  `deliverables/0.9.0_WK_ETFS_RIVALS~6/g5_drift.json` (dates, rows_compared, rows_differing, classes [{name, columns, n_dates,
  n_rows, cause {commit, cell}, reader_visible}], unclassified_rows) and a one-page G5_DRIFT.md. No S3 write, no replay.
- **Organic trigger:** none; a one-off read for the CTO's ruling on the history.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD bfad7625d7 (the package equals the deployed pin b166e04416))

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/gd-1.AC1.py` before you build.
- Read S3 with the package's own readers (`sinks.get_sink("s3")`, `revision.newest`); copy what you need into a LOCAL sink and
  build there with `gold_trade_schedule.handler_entry` (mode replay or daily per date) -- never with an S3 sink.
- A class is one cause: find it with `git log -S`/`git log -L` on `gold_trade_schedule.py` and name the commit and the cell
  (e.g. RIV-r6x1, RIV-r5h6). `reader_visible` says whether the page shows the column.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order: no file there is written or read differently), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{7,8}/checks/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 9), the analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round8.md`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~6/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-9 chain owns. Tests go beside the code as `tests/test_r9gd1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/tools/g5_drift.py
data/etfs/scripts/rivalfunds/tests/test_r9gd1_*.py
org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~6/g5_drift.json
org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~6/G5_DRIFT.md
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the drift report covers 189 dates with 0 unclassified rows; every class names a real cause commit and a cell and the classes cover every differing row; each measured drifting column sits in a class (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/gd-1.AC1.py`)
- **J1** (JUDGMENT, graded by 3.0.0_SA_CVO~RV at L9) -- the classes are right: each class's cause commit is the change that moves those columns, and reader_visible is true exactly for the columns the page shows

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-gd-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/gd-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-gd-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~6/ETFS_RIVALS.TO-RIV-gd-1.g5-history-drift-classification.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-gd-1.g5-history-drift-classification`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round8.md @2097b5212b section 4; decomposition round 9 v1.0. Chain `~6`, slot `~6`, position 1 of 1. Checks dry-run at base CLOUD bfad7625d7 (the package equals the deployed pin b166e04416): gd-1.AC1 FAIL (3) as expected (no report). Bounds: no deploy before the issuer's never-widen pair; D12 Step B and the D12 gate flip are issuer acts after nf-1 and gf-1 deploy.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>9</round>
<slot>~6</slot>
<fabric>site-z</fabric>
<status>complete</status>
