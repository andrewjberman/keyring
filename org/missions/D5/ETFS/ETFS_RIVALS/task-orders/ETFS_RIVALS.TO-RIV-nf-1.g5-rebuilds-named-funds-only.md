# ETFS_RIVALS task order -- `RIV-nf-1` -- ROUND 9 (ENRICHMENT): THE TRADE SCHEDULE REBUILDS ONLY THE NAMED FUNDS AND CARRIES EVERY OTHER FUND'S ROWS (Z-S29, ruling B)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-nf-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the issuer registers any stage at the merge)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 9** (the round-8 analysis, 8 items): the IDVZ/PFOE backfill made purely additive (the trade schedule rebuilds only named funds), their daily join through a rivalfunds-owned gate file, an incremental security list, the AI-text name links, real names for past holdings, a measured Bloomberg capacity budget, and a read of the G5 history drift. Nothing in round 9 deploys, merges, flips a gate or calls Bloomberg from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-nf-1` -- the trade schedule rebuilds only the named funds (row Z-S29; CTO~Z ruling B)
- Measured: `gold_trade_schedule.run_stage` builds one G5 object (and its G6) per report date from every fund's windows; the D12
  Step B mirror dry run re-derived every fund's trades on 189 dates with current code (confidence 176 dates, action 99, est
  price 99, discretionary_shares 43, income_funded 10, row counts 3); `hold_funds` leaves a fund OUT of the new object
  (`:95-101`), so it cannot keep a fund's prior rows.
- Interface: the stage event key `rebuild_funds` (a list of tickers). With it, for each scope date the new G5 object is the
  newest prior G5 object's rows for every fund NOT named (values unchanged) plus freshly inferred rows for the named funds; G6
  likewise from the newest prior G6 object. A date with no prior object builds every fund. Without the key nothing changes.
  `sweep.run_gold_chain` passes the batch's `rebuild_funds` (read from the fetch-bloomberg marker of the batch) to the
  trade-schedule stage.
- **Organic trigger:** the import batch's S3 marker event (canonical-shape Lambda -> run_gold_chain).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD bfad7625d7 (the package equals the deployed pin b166e04416))

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/nf-1.AC1.py` before you build.
- The issuer adds ONE hookup at the merge (do not edit it): `collector_bloomberg` import mode copies `event["rebuild_funds"]`
  onto its fetch-bloomberg marker. Your side reads the marker key in `sweep.run_gold_chain` (use `markers.get_marker` for
  stage `fetch-bloomberg`, the batch and date of the event) and tolerates its absence.
- Keep the W5-S23 held-fund contract (`HELD_META`, `-v<NN>` objects, `held_of_bytes`) and the revision contract
  (`tests/test_v2_revision_contract.py`): readers take the newest object per date.
- Andrew's word is "purely additively": the proof after the deploy is a per-date census of every other fund's G5 rows (count
  and content) reading 0 deltas.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order: no file there is written or read differently), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{7,8}/checks/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 9), the analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round8.md`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-9 chain owns. Tests go beside the code as `tests/test_r9nf1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/sweep.py
data/etfs/scripts/rivalfunds/tests/test_r9nf1_*.py
data/etfs/scripts/rivalfunds/tests/test_g52_trade_schedule_v2.py
data/etfs/scripts/rivalfunds/tests/test_t5_own_prior_pairing.py
data/etfs/scripts/rivalfunds/tests/test_r3_repairs.py
data/etfs/scripts/rivalfunds/tests/test_d1_sweep.py
data/etfs/scripts/rivalfunds/tests/test_v2_revision_contract.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- with rebuild_funds ['TXUE'] the new G5 carries SCHY's prior rows unchanged and re-infers TXUE; G6 likewise; without the key every fund is re-inferred (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/nf-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-nf-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/nf-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-nf-1.g5-rebuilds-named-funds-only.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-nf-1.g5-rebuilds-named-funds-only`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round8.md @2097b5212b section 4; decomposition round 9 v1.0. Chain `~1`, slot `~1`, position 1 of 1. Checks dry-run at base CLOUD bfad7625d7 (the package equals the deployed pin b166e04416): nf-1.AC1 FAIL (2; control OK) as expected. Bounds: no deploy before the issuer's never-widen pair; D12 Step B and the D12 gate flip are issuer acts after nf-1 and gf-1 deploy.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>9</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<status>complete</status>
