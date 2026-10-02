# ETFS_RIVALS task order -- `RIV-l-1` -- ROUND 5 (ENRICHMENT): THE v0.8 BLOOMBERG LEG, BUILT AND INERT (IDVZ, PFOE, ACWI, IWM PENDING)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-l-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~23:xxZ, --drift) -- no armed gate names rivalfunds/, issuer-site/etfs/, bloomberg/etfs/ or this cell's files; the notifier moratorium binds.
comp-iam: RUN at L5 -- no IAM change in this cell.
comp-adversary: RUN at L5 and DECLARED on this cell: the vehicle runs the CLOUD tree, so the cell must be INERT with the gate unset; the check's first clause proves the leg requests exactly today's funds.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg run by the vehicle from the CLOUD working tree). **Round 5** bounds G1, fixes three trade-inference method defects (CTO hop-9 rulings), makes the issuer floor per fund, and builds the v0.8 Bloomberg leg inert. Nothing in round 5 deploys. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-l-1` -- the v0.8 Bloomberg leg, built and inert (PRD v0.8; item 7; after m-2 on `~2`)

`peer_groups.json` gains pending entries:
- ACWI (group IDVZ) and IWM (group PFOE): `role` index_control, `source_policy` bloomberg_primary, `"leg": "pending"`.
- IDVZ and PFOE: `"pending_source_policy": "bloomberg_primary"`.
- SCHY: `"pending_role": "rival"`.

Behaviour of the gate:
- **Unset:** every reader (`universe.funds`, `policy`, `entries`, `collector_bloomberg.funds_for_day`) behaves EXACTLY as today.
- **`RIVALFUNDS_LEG_ENABLE=1`:** pending entries and pending fields take effect:
  - the four join the leg;
  - one index_control per group, ACWI and IWM;
  - SCHY reads rival.
- `collector_bloomberg.request_plan(report_date)` returns the offline request plan: `funds`, `names`, and the request shape
  (sheets and rounds as `excel_fetch` would split them).
- No G1, silver or page change in this cell.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base 9e201639c3)

- `collector_bloomberg.funds_for_day(s, report_date, event)` (~257-268): `universe_funds("bloomberg_primary")` plus each
  `issuer_first` fund with no OK issuer bronze for the date (not GQGU: `NO_BLOOMBERG_ROUTE`). `excel_fetch` (~272-349): Excel BQL,
  up to 20 sheets per round, 45 s wait, 2000-row cap.
- `universe.py`: `load` (~25-69, one home per group), `_default()` with a stamp cache (~72-77), `funds(group_id, source_policy)`,
  `policy(fund_id)`, `entries()`; roles `home|rival|index_control`, policies
  `bloomberg_primary|issuer_first|home_producer|home_producer_pending` (~18-19).
- `peer_groups.json` (map_version 1, 13 entries): SCHY is today's `index_control` (IDVZ group); the PFOE group has none; IDVZ and
  PFOE are `home_producer`.
- PRD v0.8 (`org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` ~505-560): ACWI (IDVZ group) and IWM (PFOE group) are the
  index controls, bloomberg_primary; SCHY stays a member as a rival; IDVZ and PFOE join the leg. They join ONLY after the issuer
  measures the request cost and runs the ACWI/IWM G9 preview -- so this cell is INERT until `RIVALFUNDS_LEG_ENABLE=1`.
- The vehicle runs this file from the CLOUD tree: with the gate unset, nothing it requests may change.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{3,4,5}/checks/`, the CTO rulings `org/missions/D5/ETFS/ETFS_RIVALS/ledger/CTO_RULING_20261001_HOP9_METHOD_DEFECTS.md` and `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round4.md`, the device-local captures under `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-5 cell owns. Tests go beside the code as `tests/test_r5l1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed).

<paths>
data/etfs/scripts/rivalfunds/collector_bloomberg.py
data/etfs/scripts/rivalfunds/universe.py
data/etfs/scripts/rivalfunds/peer_groups.json
data/etfs/scripts/rivalfunds/tests/test_r5l1_*.py
data/etfs/scripts/rivalfunds/tests/test_g01_universe.py
data/etfs/scripts/rivalfunds/tests/test_b1_bloomberg_channel.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- gate unset: exactly today's funds and policies; the map carries ACWI/IWM as pending index controls; gate set: the four join, one control per group, SCHY rival, request_plan covers them (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/l-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-l-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/l-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-l-1.v08-bloomberg-leg-inert.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-l-1.v08-bloomberg-leg-inert`. Report once: each criterion's verdict line with the output above it; files written; any test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-4 analysis @6dcb0074e4 (msg 28075), decomposition round 5 v1.0. Checks dry-run
at base 9e201639c3: l-1.AC1 FAIL -- each FAIL as expected, each control PASS.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>5</round>
<slot>~2</slot>
<fabric>site-z</fabric>
