# ETFS_RIVALS task order -- `RIV-dr-1` -- ROUND 11 (ENRICHMENT): THE G5 DRIFT RECORD NAMES ITS DATA-ARRIVAL CLASS'S CAUSE AS DATA ARRIVAL, NOT A CODE COMMIT (C-S38)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-dr-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~6</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the issuer registers any stage at the merge)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 11** (the round-10 analysis): the trade schedule writes a new revision when a same-input pass runs at a new code version (so the issuer's served replay of the four code-defect classes can land), and the G5 drift record names its data-arrival class's cause as data arrival. Nothing in round 11 deploys, merges, flips a gate or calls Bloomberg from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-dr-1` -- the G5 drift record names the data-arrival class's cause as data arrival (C-S38; analysis ruling 2)
- Measured: `deliverables/0.9.0_WK_ETFS_RIVALS~6/g5_drift.json` `classes[g3_latest_pull_supersession].cause` reads
  {"commit": "4fa3e25f5e", "cell": "RIV-g-4"}, as do its G5_DRIFT.md row and `tools/g5_drift.py` `CLASSES`; its 9,467 rows moved
  under UNCHANGED code because later G3 pulls landed (round-9 ruling 3 keeps their vintage).
- Interface: that `CLASSES` entry carries `"commit": None` and `"cause": "data arrival (later G3 pulls)"`; its record entry's
  `cause` reads {"commit": null, "cell": "RIV-g-4", "what": "data arrival (later G3 pulls)"}; `markdown()` prints that text in the
  cause-commit column for a null commit. The two record files are corrected IN PLACE (JSON edited, MD re-rendered by `markdown()`);
  no re-run, no S3 read, no data moves.
- **Organic trigger:** none (a record).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 134485f75b (deployed Lambda code = b8b47bb8e7 + the Z-S31 repair; eg-1 live on the vehicle))

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round11/checks/dr-1.AC1.py` before you build.
- Today `markdown(json)` equals G5_DRIFT.md byte for byte; keep that true after the edit (write the MD as `markdown()`'s output,
  LF, utf-8). Keep `tests/test_r9gd1_g5_drift.py` passing.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order: no file there is written or read differently), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round11/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{9,10}/checks/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 11), the analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round10.md`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~6/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-11 chain owns. Tests go beside the code as `tests/test_r11dr1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/tools/g5_drift.py
data/etfs/scripts/rivalfunds/tests/test_r11dr1_*.py
data/etfs/scripts/rivalfunds/tests/test_r9gd1_g5_drift.py
org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~6/g5_drift.json
org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~6/G5_DRIFT.md
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the drift record and the tool name the data-arrival class's cause as data arrival; the MD is the tool's rendering of the JSON; the other six causes and every row count unchanged (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round11/checks/dr-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-dr-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round11/checks/dr-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~6/ETFS_RIVALS.TO-RIV-dr-1.drift-record-data-arrival-cause.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-dr-1.drift-record-data-arrival-cause`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round10.md @134485f75b section 4 (items 1 and 4 are cells; 2, 3 and 5 are issuer acts); decomposition round 11 v1.0. Chain `~6`, slot `~6`, position 1 of 1. Checks dry-run at base CLOUD 134485f75b (deployed Lambda code = b8b47bb8e7 + the Z-S31 repair; eg-1 live on the vehicle): dr-1.AC1 FAIL (2; control (c) PASS) as expected. Bounds: no deploy before the issuer's never-widen pair; the served replay (item 2) runs gt-1's branch code BEFORE the ok-1 deploy (item 3).

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<direct_act>true</direct_act>
<status>pending</status>
<round>11</round>
<slot>~6</slot>
<fabric>site-z</fabric>
<status>complete</status>
