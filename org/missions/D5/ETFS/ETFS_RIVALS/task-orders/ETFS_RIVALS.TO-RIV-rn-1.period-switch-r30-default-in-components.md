# ETFS_RIVALS task order -- `RIV-rn-1` -- ROUND 8 WORKSTREAM B (ENRICHMENT): THE 30-TRADING-DAY DEFAULT, THE PERIOD SWITCH INSIDE BOTH COMPONENTS, AND HONEST WINDOW LABELS (smoke S3, S7, S8)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-rn-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L6 (2026-10-04 ~21:1xZ, --drift) -- WITHIN BUDGET, 6 of 6 carriers scanned (C1=29 C2=32 C3=12 C4=21 C5=334 C6=1); 1 gate armed, not on this project; the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 8, workstream B** (Andrew-direct 2026-10-04 signed-in smoke, on PRD v0.14 @4cc8e40575): the last 30 trading days become the default period, the period switch sits inside "What drove the return" and "Buying trend" and moves them together, every window states its real dates (a window clipped to a fund's first report never says "year to date"), and the grader attaches a figure's uncited fund-pack fact instead of calling it invented. Nothing in round 8 deploys, merges or flips a gate from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-rn-1` -- the 30-trading-day default, the switch inside both components, and honest window labels (S3, S7, S8)
- Measured: `render.PERIODS` = MTD/QTD/YTD with YTD first and selected (~:806-813); the switch lives only at the top; the
  trend card reads "year to date" for every fund (~:1057); IDVZ's clipped window reads "Year to date (2026)".
- AMENDED 2026-10-05 (PRD v0.15 @e99a733d4c; Andrew-direct @575e7d7250 "there is no need for MTD" and @a36e70f335: "Data
  available since X", dates under each pill, a short period greys): the switch is R30 | divider | QTD, YTD -- NO MTD.
- Interface: one `rf-period` radio group (R30 checked; radios R30, QTD, YTD only); the top switch reads R30, a
  `data-period-divider`, QTD, YTD, each top label holding a `data-period-dates` line with its first and last date;
  the rankings component and each trend card hold labels for the same four radios (any one moves all; no script); every rank
  and trend panel carries a `data-period-window` line (label, first and last date, trading days); R30 reads "Last 30
  trading days"; a clipped window reads "Data available since <date>"; a period under 5 trading days marks every one of its
  switch labels `data-period-short` and states its length ("QTD, 1 trading day").
- **Organic trigger:** the 07:00 ET marker publish and the 09:00 ET sweep publish.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base base CLOUD 7cc969288b (the package equals the deployed pin 75ad1e4d2e))

- AMENDMENT (2026-10-05, issuer): the first build of this order (f853bed481, 2ae50ff5ae) is on your branch; it rendered MTD
  and "Since first report". Re-cut it to the amended criteria: drop MTD from the switch (the producers still write MTD rows;
  render ignores them), "Data available since <date>", dates under each top pill, the short-period mark. Your earlier proof
  instance is superseded by the new run.
- Each check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rn-1.AC1.py`, `rn-1.AC2.py` and `rn-1.AC3.py`
  before you build.
- Andrew, verbatim (2026-10-04): "the last 30 trading days is the default ... then we have a dividing line between the year
  to date, quarter to date, month today ... that toggle can also exist in what drove the return, that toggle can also exist
  in buying trends, but when you click a toggle in any of those components, all the others move in tandem."
- The page has no script (CSP). The switch is CSS: the radios sit before the panels, `#rf-period-P:checked ~ ...` shows a
  panel, and any `<label for="rf-period-P">` anywhere checks the radio. Style the labels inside the components with the same
  `:checked` rules so the selected period reads selected everywhere. Keep the fund switch, the greyed empty-period state, the
  holding dialogs and DIALOG_SOFT_CAP.
- This worktree carries an-1 and rw-1 (render.py on branch wk-ETFS_RIVALS-2) plus the issuer's test amend ce381fd792; build
  on them and keep `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/an-1.AC1.py` and `rw-1.AC1..AC3.py` passing.
- The trend card renders one panel per period from buying_trend rows carrying `period` (rows with no `period` read as YTD);
  the rank panels read `period_clipped` / `period_nominal_start` from holding_contribution rows (absent reads as not clipped).
- Workstream B's interfaces are fixed by the checks so the four cells build in parallel: hc-1 adds `period_nominal_start` and `period_clipped` to holding_contribution rows; bt-1 adds a `period` column (R30, MTD, QTD, YTD) to buying_trend rows; rn-1 renders both; gc-1 reads buying_trend with `period == "YTD"` when the column exists. `R30` keeps its id and now means the last 30 NYSE trading days (`lib/trading_calendar.py`).

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{5,6,7}/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.14 @4cc8e40575), the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 8, its WORKSTREAM B section), and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-8 chain owns. Tests go beside the code as `tests/test_r8rn1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/test_r8rn1_*.py
data/etfs/scripts/rivalfunds/tests/test_crorv_layout.py
data/etfs/scripts/rivalfunds/tests/test_r6ui1_header_and_chrome.py
data/etfs/scripts/rivalfunds/tests/test_r6ui2_ranking_panels.py
data/etfs/scripts/rivalfunds/tests/test_r6ui3_trend_card.py
data/etfs/scripts/rivalfunds/tests/test_r6ui4_ai_account_cards.py
data/etfs/scripts/rivalfunds/tests/test_r6ui5_census_and_audit_trail.py
data/etfs/scripts/rivalfunds/tests/test_p2_page_grouped_by_fund.py
data/etfs/scripts/rivalfunds/tests/test_r7rd1_page_walk_remainder.py
data/etfs/scripts/rivalfunds/tests/test_r8rw1_render_remainder.py
data/etfs/scripts/rivalfunds/tests/test_r8an1_ai_prose_one_name.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- R30, QTD, YTD radios (no MTD) with R30 checked; the top switch reads R30, a divider, QTD, YTD, each pill with its dates; the rankings component and every trend card hold labels for R30, QTD, YTD; no script (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rn-1.AC1.py`)
- **AC2** -- every rank and trend panel states its period, first and last date and trading days; a clipped YTD reads 'Data available since <date>' and never 'Year to date'; R30 reads 'Last 30 trading days' (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rn-1.AC2.py`)
- **AC3** -- a period under 5 trading days (QTD on a 10-01 as-of) marks every one of its switch labels short and states its length; R30 and YTD are not marked (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rn-1.AC3.py`)
- **J1** (JUDGMENT, graded by 3.0.0_SA_CVO~RV at L9 on the served page) -- the served page after the deploy opens on the last 30 trading days, the switch inside both components moves them together, and no window is mislabelled; positive control: the served 2026-10-02 page (YTD default; IDVZ 'Year to date (2026), 2026-08-21 to 2026-10-01')

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-rn-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rn-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-rn-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rn-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-rn-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rn-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-rn-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-rn-1.period-switch-r30-default-in-components.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-rn-1.period-switch-r30-default-in-components`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Andrew-direct smoke @1c31a5f6ce (S2, S3, S7, S8) under "yes, build round 8 tonight" @0a4321b843, PRD v0.14 @4cc8e40575; decomposition round 8 WORKSTREAM B section; measured inputs WORKSTREAM_B_INPUTS.md @7cc969288b. Chain `~2`, slot `~2`, position 3 of 3. Checks dry-run at base base CLOUD 7cc969288b (the package equals the deployed pin 75ad1e4d2e): rn-1.AC1 FAIL (3; control OK), rn-1.AC2 FAIL (3; control OK) as expected. Bounds: no merge before the 2026-10-05 07:00 ET vehicle pull; no deploy before the 13:30Z grades.

**AMENDMENT 1 (2026-10-05 ~03:2xZ, issuer):** to PRD v0.15 @e99a733d4c (CTO~Z msg 29405 asked for it before the drain) and Andrew-direct @a36e70f335; criteria AC1/AC2 re-pointed, AC3 added (3 mechanical). Checks dry-run: CLOUD FAIL 3/3/1, the first rn-1 build FAIL 3/1/1, controls OK. Graded by: to-pipeline-gate on a modified order reads only GATE (viii) <placeholders> (NONE).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>8</round>
<workstream>B</workstream>
<slot>~2</slot>
<fabric>site-z</fabric>
