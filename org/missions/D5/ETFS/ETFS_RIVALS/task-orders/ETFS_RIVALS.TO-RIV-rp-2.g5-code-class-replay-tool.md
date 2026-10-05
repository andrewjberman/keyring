# ETFS_RIVALS task order -- `RIV-rp-2` -- ROUND 10 (ENRICHMENT): THE G5 CODE-CLASS REPLAY TOOL: A G3-PINNED DRY RUN OF THE 4 NON-G3 CLASSES WITH A CENSUS IN WHICH NOTHING ELSE MOVES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-rp-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~3</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the issuer registers any stage at the merge)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 10** (the round-9 analysis): the G4 enrichment never lands an all-empty or all-error revision (S25, first), one key per security, a replay tool for the four code-defect classes of the G5 history (G3-pinned), and the IAM grant for round 9's two tables. Nothing in round 10 deploys, merges, flips a gate or calls Bloomberg from a worker (the AE seat's apply is under its own never-widen pair). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-rp-2` -- the G5 code-class replay tool (round-9 ruling 4, re-ruled option A by CTO~Z msg 29806)
- Measured by RIV-gd-1 (deliverables/0.9.0_WK_ETFS_RIVALS~6/g5_drift.json): key_resolution_out_of_confidence 1,040 rows (RIV-h-6),
  full_exit_priced 266 (RIV-x-1), own_prior_pairing 7 (RIV-t-5), implausible_window_refused 10 (RIV-h-5) -- 1,323 rows; the two
  RIV-e-2 classes (20 rows) and the data-arrival class (9,467 rows) keep their vintage.
- Interface: `data/etfs/scripts/rivalfunds/tools/g5_code_replay.py` with `plan` and `dry` (G3 pinned to the live object's recorded
  revisions; `rebuild_funds` per date), writing `deliverables/0.9.0_WK_ETFS_RIVALS~3/g5_replay_dry.json` (classes, dates, rows_moved,
  rows_moved_by_class, rows_moved_outside_classes, columns_moved_outside_classes, g3_label_columns_moved). No S3 write.
- **Organic trigger:** none; the served replay is the issuer's act under its own pair, with this tool.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 33d9077d5f (the package equals the deployed pin b8b47bb8e7))

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round10/checks/rp-2.AC1.py` before you build.
- Reuse RIV-gd-1's tool (`data/etfs/scripts/rivalfunds/tools/g5_drift.py`): its G3 pinning, its replay-from-2025-12-01 start (row
  Z-W6-S2) and its comparison; read `deliverables/0.9.0_WK_ETFS_RIVALS~6/G5_DRIFT.md` first.
- Read S3 READ-ONLY with the package's readers; build into a LOCAL sink only; the trade schedule's `rebuild_funds` (RIV-nf-1) carries
  every unplanned fund's rows unchanged.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order: no file there is written or read differently), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round10/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{8,9}/checks/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 9), the analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round8.md`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~3/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-10 chain owns. Tests go beside the code as `tests/test_r10rp2_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/tools/g5_code_replay.py
data/etfs/scripts/rivalfunds/tests/test_r10rp2_*.py
org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~3/g5_replay_dry.json
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the dry-run report names exactly the 4 code classes, each moving gd-1's row count; nothing outside them moves and no G3 label column moves (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round10/checks/rp-2.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-rp-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round10/checks/rp-2.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~3/ETFS_RIVALS.TO-RIV-rp-2.g5-code-class-replay-tool.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-rp-2.g5-code-class-replay-tool`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round9.md @f68eb77491 section 4 (+ CTO~Z msg 29806: rp-2 option A; iam-1 to an AE seat with a simulate arm); decomposition round 10 v1.0. Chain `~3`, slot `~3`, position 1 of 1. Checks dry-run at base CLOUD 33d9077d5f (the package equals the deployed pin b8b47bb8e7): rp-2.AC1 FAIL (3) as expected (no report). Bounds: no deploy before the issuer's never-widen pair; rp-2's served replay is an issuer act after the tool lands and BEFORE ok-1 deploys (ok-1 re-keys).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>10</round>
<slot>~3</slot>
<fabric>site-z</fabric>
