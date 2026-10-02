# ETFS_RIVALS task order -- `RIV-cu-1` -- ROUND 7 (ENRICHMENT): THE SWEEP CONTINUES EVERY OPEN G1 CURSOR (W4-S9, continuation half)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-cu-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-02 ~21:3xZ, --drift) -- carrier C1 PARTIAL inside the 90 s budget (446 of 65,153 files scanned, 0 gates armed); C2-C6 not scanned (blind there); the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 7** makes the 09:00 ET sweep run the AI step itself (round 6 left no scheduled path to it), makes every run carry its trigger, has the census read the rankings' classification and agree with the header, gives one deterministic name per security, asks Bloomberg for the CUSIP lines' names, and carries the page-walk remainder (PRD v0.13). Nothing in round 7 deploys from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-cu-1` -- the sweep continues every open G1 cursor (W4-S9, continuation half; found at I-1's measurement)
- Round 5 bounded a long G1 batch: `_budget_s` 600 s returns PARTIAL with a cursor and NO G1 marker, and `run_gold_chain`
  re-runs G1 once inside one invocation.
- The issuer's I-1 measurement (C:/tmp/r7i1/, batch d5-gqgu-03: 60 dates, PARTIAL, PARTIAL, OK) found that NOTHING continues an
  open cursor across invocations. The silver trigger fires only on a new marker, and the 09:00 ET sweep walks only its own
  page day, so a PARTIAL batch stays incomplete until a seat re-invokes it.
- The sweep continues every OPEN G1 cursor (a cursor object without its G1 marker), within a bounded lookback the cell
  states and within its budget. A cursor older than the lookback is reported in the sweep's detail, never silently dropped.
  With no open cursor, the sweep behaves exactly as today.
- **Organic trigger:** the 09:00 ET sweep schedule. A PARTIAL batch completes on the next scheduled sweep.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 50761d39e9 (the package equals the deployed pin eb6e9f04ff))

- Measured by the issuer's I-1 overlay (C:/tmp/r7i1/, batch d5-gqgu-03, 60 dates: PARTIAL, PARTIAL, OK): nothing continues an open cursor across invocations -- the silver trigger fires only on a NEW marker, the 09:00 ET sweep walks only its own day, and no EventBridge rule watches build_canonical_shape markers (generated.auto.tfvars.json `rules`).
- Interface (the check reads it): an OPEN cursor = a `markers.cursor_uri(G1, D, B)` object with no `homes.marker_uri` beside it (a cursor WITH its marker is closed -- the real G1 leaves the cursor in place when it finishes); find cursors by listing `homes.address("rivalfunds","etfs","state","build_canonical_shape","date=")`; lookback `sweep.CURSOR_LOOKBACK_DAYS = 10` NYSE trading days before the sweep's day via `prev_trading_day` (the sweep's own day is excluded -- its own DAG continues it); continuation = `run_gold_chain({"date": D, "mode": "daily", "batch_id": B, "sink": ...}, <runners>)` so G1 resumes from its cursor, then G2 and the gated G5 run (nothing else for that day; no publish -- the G5 marker's own rule publishes it); G1's event carries budget_s <= 450 when 600 s remain (never start a window that cannot finish: the W4-S9 timeout); report in `result["detail"]["open_cursors"]`, one entry per open cursor `{date, batch_id, action: continued|beyond_lookback|out_of_time, status}`.
- This slot's previous orders (sa-1, pv-1) changed sweep.handler_entry for the AI step; build on them and keep their checks passing (round7/checks/sa-1.AC*.py, pv-1.AC1.py).
- Organic trigger: the 09:00 ET sweep schedule; a PARTIAL batch completes on the next scheduled sweep.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/` and rounds 5-6's `.../round5/checks/`, `.../round6/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.13), the round-6 analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round6.md`, the walk brief `docs/briefs/rivalfunds-ui-data-walk-20261002.md` and its register `docs/briefs/rivalfunds-ui-data-findings-20261002.json`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-7 chain owns, and none of the merge hookups the decomposition names (the issuer adds them). Tests go beside the code as `tests/test_r7cu1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file, never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/sweep.py
data/etfs/scripts/rivalfunds/tests/test_r7cu1_*.py
data/etfs/scripts/rivalfunds/tests/test_d1_sweep.py
data/etfs/scripts/rivalfunds/tests/test_r5b1_g1_windowed.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the sweep continues an open G1 cursor within 10 trading days (G1 from the cursor, then G2 and G5; marker written; a second sweep runs nothing), reports every open cursor (continued / beyond_lookback / out_of_time), caps G1's budget_s at 450 with 600 s left; control: no open cursor -> exactly today's sweep (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/cu-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-cu-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/cu-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-cu-1.sweep-continues-open-cursors.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-cu-1.sweep-continues-open-cursors`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-6 analysis @94f682c868 (CTO~Z msg 28735) section 3 + the RFW register
graded against rv-publish-1002r6; decomposition round 7 v1.0; Andrew-direct max parallelization (cooRV record 141xZ). Chain `~1`, slot `~1`, position 3 of 3 (sa-1 -> pv-1 -> cu-1). Checks dry-run at base CLOUD 50761d39e9 (the package equals the deployed pin eb6e9f04ff):
cu-1.AC1 FAIL (8; controls b1-b3 and c1 PASS) as expected; PASSES under the check writer's in-memory fix (scratchpad cu1_positive_arm.py); five mutant fixes each fail their limb.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>7</round>
<slot>~1</slot>
<fabric>site-z</fabric>
