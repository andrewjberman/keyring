# ETFS_RIVALS task order -- `RIV-gf-1` -- ROUND 9 (ENRICHMENT): A RIVALFUNDS-OWNED GATE FILE FOR THE BLOOMBERG LEG GATES (the IDVZ/PFOE daily join)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-gf-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the issuer registers any stage at the merge)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 9** (the round-8 analysis, 8 items): the IDVZ/PFOE backfill made purely additive (the trade schedule rebuilds only named funds), their daily join through a rivalfunds-owned gate file, an incremental security list, the AI-text name links, real names for past holdings, a measured Bloomberg capacity budget, and a read of the G5 history drift. Nothing in round 9 deploys, merges, flips a gate or calls Bloomberg from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-gf-1` -- a rivalfunds-owned gate file (CTO~Z ruling; Andrew-direct @33ff3bdac0)
- Measured: `universe.d12_enabled()` reads only the process environment (`universe.py:36-37`); the vehicle sets no D12 variable
  and its file `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` may not be edited.
- Interface: `data/etfs/scripts/rivalfunds/leg_gates.json` {"RIVALFUNDS_LEG_ENABLE", "RIVALFUNDS_LEG_D12", "RIVALFUNDS_LEG_D13":
  "0"|"1"}; a gate reads ON when the environment says "1" OR the file says "1" (one direction); `universe.GATES_FILE` names the
  file; the committed file ships every gate "0". The map cache stamp includes the file's gate state.
- **Organic trigger:** every process that reads the map (the vehicle's leg, every Lambda).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD bfad7625d7 (the package equals the deployed pin b166e04416))

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/gf-1.AC1.py` before you build.
- Flipping D12 is a later one-line issuer commit under its own never-widen pair, never part of this order.
- Keep round 5's leg-inert contract (`tests/test_r5l1_leg_inert.py`) and round 8's split gates (`tests/test_r8lg1_*.py`).
- The Lambda package already stages the whole `rivalfunds/` directory, so the file ships with the code.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order: no file there is written or read differently), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{7,8}/checks/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 9), the analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round8.md`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-9 chain owns. Tests go beside the code as `tests/test_r9gf1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/universe.py
data/etfs/scripts/rivalfunds/leg_gates.json
data/etfs/scripts/rivalfunds/tests/test_r9gf1_*.py
data/etfs/scripts/rivalfunds/tests/test_r5l1_leg_inert.py
data/etfs/scripts/rivalfunds/tests/test_g01_universe.py
data/etfs/scripts/rivalfunds/tests/test_r8lg1_*.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a file D12 '1' alone turns D12 on; the environment '1' turns it on whatever the file says; both off is off; the committed file ships every gate '0' (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/gf-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-gf-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/gf-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-gf-1.leg-gate-file.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-gf-1.leg-gate-file`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round8.md @2097b5212b section 4; decomposition round 9 v1.0. Chain `~2`, slot `~2`, position 1 of 1. Checks dry-run at base CLOUD bfad7625d7 (the package equals the deployed pin b166e04416): gf-1.AC1 FAIL (2; controls OK) as expected. Bounds: no deploy before the issuer's never-widen pair; D12 Step B and the D12 gate flip are issuer acts after nf-1 and gf-1 deploy.

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>9</round>
<slot>~2</slot>
<fabric>site-z</fabric>
