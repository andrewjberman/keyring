# ETFS_RIVALS task order -- `RIV-ok-1` -- ROUND 10 (ENRICHMENT): ONE KEY PER SECURITY: A CUSIP-ONLY ROW TAKES THE BLOOMBERG KEY ANOTHER ROW CARRIES FOR THAT CUSIP (round-9 ruling 7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-ok-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the issuer registers any stage at the merge)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 10** (the round-9 analysis): the G4 enrichment never lands an all-empty or all-error revision (S25, first), one key per security, a replay tool for the four code-defect classes of the G5 history (G3-pinned), and the IAM grant for round 9's two tables. Nothing in round 10 deploys, merges, flips a gate or calls Bloomberg from a worker (the AE seat's apply is under its own never-widen pair). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-ok-1` -- one key per security (round-9 ruling 7, COO P3)
- Measured on the served 10-05 page: Nebius Group is two securities -- `N97284108` (GQGU reports it by CUSIP only) and
  `NBIS_US_Equity` (WCMG reports the Bloomberg id, the same CUSIP on the row) -- two dialogs, two ranking rows; Broadcom and Intuit
  carry the same class in the page's name map. `gold_holding_contribution._books` keys a row by `security_id`, else by an alias of
  its `raw_identifier`; the alias never joins on the CUSIP / ISIN columns.
- Interface: a row whose key is a CUSIP or ISIN takes the Bloomberg-id key that another row in the same input window carries for that
  same CUSIP / ISIN (`security_cusip` / `security_isin`); a CUSIP with no Bloomberg counterpart keeps its CUSIP key. The same rule
  keys the trade schedule's positions.
- **Organic trigger:** the 07:00 ET marker publish (A1) and the batch chain (G5).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 33d9077d5f (the package equals the deployed pin b8b47bb8e7))

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round10/checks/ok-1.AC1.py` before you build.
- Keep nt-1's name pick, hc-1's contracts and nm-3's stored names (`tests/test_r7nt1_name_pick.py`, `tests/test_r8hc1_*.py`,
  `tests/test_r9nm3_*.py`) and the G5 key-resolution column (`tests/test_r5h6_key_resolution_column.py`).
- Sequencing (record): the issuer's G5 code-class replay (rp-2) runs at the code BEFORE this cell deploys; do not depend on it.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order: no file there is written or read differently), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round10/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{8,9}/checks/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 10), the analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round9.md`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-10 chain owns. Tests go beside the code as `tests/test_r10ok1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/gold_holding_contribution.py
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/tests/test_r10ok1_*.py
data/etfs/scripts/rivalfunds/tests/test_a1rk_contribution.py
data/etfs/scripts/rivalfunds/tests/test_r7nt1_name_pick.py
data/etfs/scripts/rivalfunds/tests/test_r8hc1_*.py
data/etfs/scripts/rivalfunds/tests/test_r9nm3_*.py
data/etfs/scripts/rivalfunds/tests/test_r5h6_key_resolution_column.py
data/etfs/scripts/rivalfunds/tests/test_g52_trade_schedule_v2.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a CUSIP-only Nebius row and a Bloomberg-keyed Nebius row share the one bucket NBIS_US_Equity; a CUSIP with no Bloomberg counterpart keeps its CUSIP (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round10/checks/ok-1.AC1.py`)
- **J1** (JUDGMENT, graded by 3.0.0_SA_CVO~RV at L9) -- on the served page after the deploy, Nebius, Broadcom and Intuit each open ONE dialog and rank under one row per fund; positive control: the served 10-05 page (Nebius: two dialogs, N97284108 and NBIS_US_Equity)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-ok-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round10/checks/ok-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-ok-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-ok-1.one-key-per-security.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-ok-1.one-key-per-security`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round9.md @f68eb77491 section 4 (+ CTO~Z msg 29806: rp-2 option A; iam-1 to an AE seat with a simulate arm); decomposition round 10 v1.0. Chain `~2`, slot `~2`, position 1 of 1. Checks dry-run at base CLOUD 33d9077d5f (the package equals the deployed pin b8b47bb8e7): ok-1.AC1 FAIL (1; control OK) as expected. Bounds: no deploy before the issuer's never-widen pair; rp-2's served replay is an issuer act after the tool lands and BEFORE ok-1 deploys (ok-1 re-keys).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>10</round>
<slot>~2</slot>
<fabric>site-z</fabric>
