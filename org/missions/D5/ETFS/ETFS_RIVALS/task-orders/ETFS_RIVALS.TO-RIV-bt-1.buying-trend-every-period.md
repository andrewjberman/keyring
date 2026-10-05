# ETFS_RIVALS task order -- `RIV-bt-1` -- ROUND 8 WORKSTREAM B (ENRICHMENT): THE BUYING TREND CARRIES EVERY PERIOD: LAST 30 TRADING DAYS, MONTH, QUARTER, YEAR (smoke S8; v0.14 FWD-15)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-bt-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~7</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L6 (2026-10-04 ~21:1xZ, --drift) -- WITHIN BUDGET, 6 of 6 carriers scanned (C1=29 C2=32 C3=12 C4=21 C5=334 C6=1); 1 gate armed, not on this project; the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 8, workstream B** (Andrew-direct 2026-10-04 signed-in smoke, on PRD v0.14 @4cc8e40575): the last 30 trading days become the default period, the period switch sits inside "What drove the return" and "Buying trend" and moves them together, every window states its real dates (a window clipped to a fund's first report never says "year to date"), and the grader attaches a figure's uncited fund-pack fact instead of calling it invented. Nothing in round 8 deploys, merges or flips a gate from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-bt-1` -- the buying trend carries every period (S8; v0.14 FWD-15)
- Measured: `build` writes the year to date only (`gold_buying_trend.py:157`, `:210`).
- Interface: rows carry `period` in {R30, MTD, QTD, YTD}, each with its own window_start / window_end / n_trading_days;
  YTD rows are today's rows.
- **Organic trigger:** the 07:00 ET marker publish.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base base CLOUD 7cc969288b (the package equals the deployed pin 75ad1e4d2e))

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/bt-1.AC1.py` before you build.
- Ranks, lean (into / away), reading (bet / tilt) and the by-month mark are computed per period over that period's windows;
  a period with no trade for the fund writes no line rows for it.
- The handler's G5 read window must reach back to the earliest period start (YTD, 01-01) as today; R30 lies inside it.
- Keep every existing contract: the Unclassified rule (sx-1), the name pick (nm-2 / nt-1), the refused windows (G6 REFUSED).
- Workstream B's interfaces are fixed by the checks so the four cells build in parallel: hc-1 adds `period_nominal_start` and `period_clipped` to holding_contribution rows; bt-1 adds a `period` column (R30, MTD, QTD, YTD) to buying_trend rows; rn-1 renders both; gc-1 reads buying_trend with `period == "YTD"` when the column exists. `R30` keeps its id and now means the last 30 NYSE trading days (`lib/trading_calendar.py`).

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{5,6,7}/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.14 @4cc8e40575), the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 8, its WORKSTREAM B section), and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~7/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-8 chain owns. Tests go beside the code as `tests/test_r8bt1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/gold_buying_trend.py
data/etfs/scripts/rivalfunds/tests/test_r8bt1_*.py
data/etfs/scripts/rivalfunds/tests/test_a1tb_trend.py
data/etfs/scripts/rivalfunds/tests/test_r6sx1_unclassified_never_ranked.py
data/etfs/scripts/rivalfunds/tests/test_r7nm2_security_name.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- buying_trend rows carry a period column with R30, MTD, QTD, YTD; each period's lines are its own trades' securities with its own window_start; YTD is unchanged (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/bt-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-bt-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/bt-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~7/ETFS_RIVALS.TO-RIV-bt-1.buying-trend-every-period.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-bt-1.buying-trend-every-period`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Andrew-direct smoke @1c31a5f6ce (S2, S3, S7, S8) under "yes, build round 8 tonight" @0a4321b843, PRD v0.14 @4cc8e40575; decomposition round 8 WORKSTREAM B section; measured inputs WORKSTREAM_B_INPUTS.md @7cc969288b. Chain `~7`, slot `~7`, position 1 of 1. Checks dry-run at base base CLOUD 7cc969288b (the package equals the deployed pin 75ad1e4d2e): bt-1.AC1 FAIL (2; control OK) as expected. Bounds: no merge before the 2026-10-05 07:00 ET vehicle pull; no deploy before the 13:30Z grades.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>8</round>
<workstream>B</workstream>
<slot>~7</slot>
<fabric>site-z</fabric>
