# ETFS_RIVALS task order -- `RIV-eg-1` -- ROUND 10 (ENRICHMENT): THE G4 ENRICHMENT NEVER LANDS AN ALL-EMPTY OR ALL-ERROR REVISION (S25, FIRST)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-eg-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the issuer registers any stage at the merge)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 10** (the round-9 analysis): the G4 enrichment never lands an all-empty or all-error revision (S25, first), one key per security, a replay tool for the four code-defect classes of the G5 history (G3-pinned), and the IAM grant for round 9's two tables. Nothing in round 10 deploys, merges, flips a gate or calls Bloomberg from a worker (the AE seat's apply is under its own never-widen pair). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-eg-1` -- the G4 enrichment never lands an all-empty or all-error revision (row Z-S25; round-9 ruling 1, FIRST)
- Measured 2026-10-05: the 08:32 ET vehicle's enrichment ran against a no-data Terminal and landed
  `gold/security_market/date=2026-10-02/market-20261005T123318Z-c86a8d9e27fa.parquet` -- 601 rows, px_close / gics_sector /
  security_name all null -- as the NEWEST revision (status OK), shadowing the good 10-04 revision for every reader until a one-key
  restore at 12:46Z.
- Interface: `enrichment_bloomberg` mode `market` refuses to land a revision in which EVERY security is an error or carries none of
  px_close, gics_sector and security_name: nothing is written, the prior revision stays the newest, the result reads status
  "REFUSED" with `detail.reason` naming the count, and the refusal is recorded in the stage's state (a marker carrying status
  REFUSED). A revision with at least one usable security lands as today.
- **Organic trigger:** the vehicle's 07:00 ET enrichment step.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 33d9077d5f (the package equals the deployed pin b8b47bb8e7))

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round10/checks/eg-1.AC1.py` before you build.
- The check stubs `_blp_reference_data` and `_blp_historical_data` on the module; keep them module attributes.
- Keep round 7's nm-2 contract (LONG_COMP_NAME on the reference request only) and round 9's nm-3 names stage that runs after a
  landed G4 (`tests/test_r9nm3_*.py`): a REFUSED G4 runs no names stage.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order: no file there is written or read differently), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round10/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{8,9}/checks/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 9), the analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round8.md`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-10 chain owns. Tests go beside the code as `tests/test_r10eg1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/tests/test_r10eg1_*.py
data/etfs/scripts/rivalfunds/tests/test_e1_enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/tests/test_v2_enrichment_cli.py
data/etfs/scripts/rivalfunds/tests/test_r9nm3_*.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- an all-error or all-empty G4 revision is refused and the prior revision stays the newest; a revision with one usable security lands (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round10/checks/eg-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-eg-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round10/checks/eg-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-eg-1.g4-never-lands-empty.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-eg-1.g4-never-lands-empty`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round9.md @f68eb77491 section 4 (+ CTO~Z msg 29806: rp-2 option A; iam-1 to an AE seat with a simulate arm); decomposition round 10 v1.0. Chain `~1`, slot `~1`, position 1 of 1. Checks dry-run at base CLOUD 33d9077d5f (the package equals the deployed pin b8b47bb8e7): eg-1.AC1 FAIL (2; control OK) as expected. Bounds: no deploy before the issuer's never-widen pair; rp-2's served replay is an issuer act after the tool lands and BEFORE ok-1 deploys (ok-1 re-keys).

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>10</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<status>complete</status>
