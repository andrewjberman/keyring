# ETFS_RIVALS task order -- `RIV-b-2` -- ROUND 5 (ENRICHMENT): A MARKER-DRIVEN G1 RUN IS WINDOWED AND CONTINUED FROM A CURSOR (W4-S9, FIRST)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-b-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~23:xxZ, --drift) -- no armed gate names rivalfunds/, issuer-site/etfs/, bloomberg/etfs/ or this cell's files; the notifier moratorium binds.
comp-iam: RUN at L5 -- no IAM change in this cell.
comp-adversary: RUN at L5 and DECLARED on this cell: any batch size must complete and no report date may be built twice; the check plants a 50-date marker batch with a tiny budget and counts objects per date.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg run by the vehicle from the CLOUD working tree). **Round 5** bounds G1, fixes three trade-inference method defects (CTO hop-9 rulings), makes the issuer floor per fund, and builds the v0.8 Bloomberg leg inert. Nothing in round 5 deploys. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-b-2` -- a marker-driven G1 run is windowed and continued from a cursor (W4-S9; ruling 1; FIRST)

`gold_canonical_shape.handler_entry` takes a time budget: the event's `budget_s`, else the environment `RIVALFUNDS_G1_BUDGET_S`,
default 600 s.
- It stops STARTING report dates once the budget is spent.
- It returns status `PARTIAL` with a cursor in `detail`, and writes NO output marker.
- The same event re-invoked continues from the cursor: dates already built are not rebuilt.
- When every date is built it returns OK and writes the marker as today.
- `sweep.run_gold_chain` treats `PARTIAL` as not done and re-invokes while its own budget allows.
- Without a budget the behaviour is unchanged.
- No infra file changes.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base 9e201639c3)

- Trigger: EventBridge on `state/build_silver/` and `state/build_bloomberg_silver/` -> `rivalfunds-build-canonical-shape-lambda`
  (900 s timeout); its handler `return sweep.run_gold_chain(sweep.trigger_event(event))` DROPS the Lambda context (do not edit
  infra: the bound lives in the package). `sweep.trigger_event` (`sweep.py` ~197-220) makes `{"date", "mode": "daily",
  "batch_id", "sink": "s3"}`; `sweep.run_gold_chain` (~333-355) runs G1, G2, gated G5 with no budget.
- `gold_canonical_shape.handler_entry` (~739-875) takes its dates from `_report_dates` (~308-331: daily/backfill = the union of
  `date=` from BOTH silver markers' outputs for the batch id) and builds them in ONE loop (~787-859); the marker is written only after
  all dates (~872). A date already gold is skipped ("this revision is already gold") but only AFTER its rows are rebuilt (~12 s per
  date on S3): measured batches of 60 dates took 696.7 s, 858.1 s, then timed out (REMEDIATION_v4.Z.md).
- No cursor exists anywhere in the package. `sweep.MARGIN_MS` / `_budget` (~73, ~463) only guard the start of a sweep batch.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{3,4,5}/checks/`, the CTO rulings `org/missions/D5/ETFS/ETFS_RIVALS/ledger/CTO_RULING_20261001_HOP9_METHOD_DEFECTS.md` and `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round4.md`, the device-local captures under `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-5 cell owns. Tests go beside the code as `tests/test_r5b1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed).

<paths>
data/etfs/scripts/rivalfunds/gold_canonical_shape.py
data/etfs/scripts/rivalfunds/sweep.py
data/etfs/scripts/rivalfunds/markers.py
data/etfs/scripts/rivalfunds/tests/test_r5b1_*.py
data/etfs/scripts/rivalfunds/tests/test_g1_canonical_shape.py
data/etfs/scripts/rivalfunds/tests/test_g12_canonical_multi_source.py
data/etfs/scripts/rivalfunds/tests/test_d1_sweep.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a 50-date marker batch with `budget_s` 0.001 returns PARTIAL with no marker, then completes across several invocations with exactly one G1 object per date; without a budget it completes in one (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/b-2.AC1.py`)

**Time bound (fabric ruling 9):** `b-2.AC1` read a whole window or a 50-date fixture: run it under `timeout 600`, not 120. rc 124 is a timeout, never a FAIL; report it as such.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-b-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/b-2.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-b-2.g1-windowed-continued.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-b-2.g1-windowed-continued`. Report once: each criterion's verdict line with the output above it; files written; any test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-4 analysis @6dcb0074e4 (msg 28075), decomposition round 5 v1.0. Checks dry-run
at base 9e201639c3: b-2.AC1 FAIL -- each FAIL as expected, each control PASS.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>5</round>
<slot>~1</slot>
<fabric>site-z</fabric>
