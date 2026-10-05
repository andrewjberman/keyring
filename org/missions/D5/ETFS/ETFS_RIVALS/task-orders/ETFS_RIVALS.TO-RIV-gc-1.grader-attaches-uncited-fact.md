# ETFS_RIVALS task order -- `RIV-gc-1` -- ROUND 8 WORKSTREAM A (ENRICHMENT): THE GRADER ATTACHES AN UNCITED FUND-PACK FACT, AND THE AI'S LAST 30 DAYS ARE TRADING DAYS (smoke S2, S7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-gc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~5</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L6 (2026-10-04 ~21:1xZ, --drift) -- WITHIN BUDGET, 6 of 6 carriers scanned (C1=29 C2=32 C3=12 C4=21 C5=334 C6=1); 1 gate armed, not on this project; the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 8, workstream B** (Andrew-direct 2026-10-04 signed-in smoke, on PRD v0.14 @4cc8e40575): the last 30 trading days become the default period, the period switch sits inside "What drove the return" and "Buying trend" and moves them together, every window states its real dates (a window clipped to a fund's first report never says "year to date"), and the grader attaches a figure's uncited fund-pack fact instead of calling it invented. Nothing in round 8 deploys, merges or flips a gate from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-gc-1` -- the grader attaches an uncited fund-pack fact, and the AI's last 30 days are trading days (S2, S7)
- Measured: IDVZ "The last 30 days" FAILED on "$1.6 million, $1.3 million"; both are real fact-pack trades (T7 1,564,110.98;
  T9 1,292,762.88) the model left out of `cited`; with them cited the grade PASSES. "$1.3 million" also matches T8.
- Interface: `ai_accounts.attach_uncited(body, facts, cited) -> (rows, notes)` (one uncited match -> its row attached with
  `auto_cited`; two or more -> no attach, one note naming the ids); `run_chain` calls it before `grounding_check` and an
  ambiguous note joins the FAIL reason. `fact_pack` keeps trades in the last 30 NYSE trading days, and reads the trend rows
  with `period == "YTD"` when the column exists.
- **Organic trigger:** the 09:00 ET sweep's AI step.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base base CLOUD 7cc969288b (the package equals the deployed pin 75ad1e4d2e))

- Each check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/gc-1.AC1.py` and `gc-1.AC2.py`
  before you build.
- The grader: `ai_accounts.py:396` builds the cited set from the model's `cited` list plus matching market readings
  (`used_readings`, :357-360); `:274-277` compare each figure only against those; `:201-207` is the number matcher
  (`_matches`), correct for this case (1.564 rounds to 1.6). Reuse `_figures` and `_matches`; do not loosen the matcher.
- `regrade_rows` (:446-470) re-grades stored rows from their stored citations; give it the same attach step so a re-grade
  of the 2026-10-02 run can flip IDVZ without a new model call (no re-grade is RUN in this order).
- `R30_DAYS` = 30 calendar days today (:45, :133, :495, :579); the fact pack's trade window becomes the last 30 trading days.
  The two loaders' `lo` bounds (:495, :579) must still read far enough back for that window (30 trading days is about 42
  calendar days).
- Workstream B's interfaces are fixed by the checks so the four cells build in parallel: hc-1 adds `period_nominal_start` and `period_clipped` to holding_contribution rows; bt-1 adds a `period` column (R30, MTD, QTD, YTD) to buying_trend rows; rn-1 renders both; gc-1 reads buying_trend with `period == "YTD"` when the column exists. `R30` keeps its id and now means the last 30 NYSE trading days (`lib/trading_calendar.py`).

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{5,6,7}/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.14 @4cc8e40575), the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 8, its WORKSTREAM B section), and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~5/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-8 chain owns. Tests go beside the code as `tests/test_r8gc1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/ai_accounts.py
data/etfs/scripts/rivalfunds/tests/test_r8gc1_*.py
data/etfs/scripts/rivalfunds/tests/test_a1ai2_grounding_hookup.py
data/etfs/scripts/rivalfunds/tests/test_grounding_iso_timestamp.py
data/etfs/scripts/rivalfunds/tests/test_grounding_ticker_form.py
data/etfs/scripts/rivalfunds/tests/test_grounding_unknown_identifier.py
data/etfs/scripts/rivalfunds/tests/test_r6ap1_ai_stage.py
data/etfs/scripts/rivalfunds/tests/test_r6r6_quoted_name.py
data/etfs/scripts/rivalfunds/tests/test_regrade_call11.py
data/etfs/scripts/rivalfunds/tests/test_f5_reading_labels.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a stated figure in exactly one uncited fund-pack fact attaches that fact (auto_cited) and grounding passes; an ambiguous figure attaches nothing and its note names both facts; a figure in no fact still FAILS (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/gc-1.AC1.py`)
- **AC2** -- the fact pack's trades are the last 30 NYSE trading days: a trade 36 calendar days back (inside 30 trading days) is a fact; one more than 30 trading days back is not (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/gc-1.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-gc-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/gc-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-gc-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/gc-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~5/ETFS_RIVALS.TO-RIV-gc-1.grader-attaches-uncited-fact.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-gc-1.grader-attaches-uncited-fact`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Andrew-direct smoke @1c31a5f6ce (S2, S3, S7, S8) under "yes, build round 8 tonight" @0a4321b843, PRD v0.14 @4cc8e40575; decomposition round 8 WORKSTREAM B section; measured inputs WORKSTREAM_B_INPUTS.md @7cc969288b. Chain `~5`, slot `~5`, position 1 of 1. Checks dry-run at base base CLOUD 7cc969288b (the package equals the deployed pin 75ad1e4d2e): gc-1.AC1 FAIL (2; control OK), gc-1.AC2 FAIL (1; controls OK) as expected. Bounds: no merge before the 2026-10-05 07:00 ET vehicle pull; no deploy before the 13:30Z grades.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>8</round>
<workstream>B</workstream>
<slot>~5</slot>
<fabric>site-z</fabric>
