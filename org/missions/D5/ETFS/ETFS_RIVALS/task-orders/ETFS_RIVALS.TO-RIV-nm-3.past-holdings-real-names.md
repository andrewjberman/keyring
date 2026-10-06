# ETFS_RIVALS task order -- `RIV-nm-3` -- ROUND 9 (ENRICHMENT): A SECURITY NAMED BY ITS TICKER FORM GETS ITS REAL NAME, ASKED OF BLOOMBERG ONCE (C-S36)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-nm-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~5</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the issuer registers any stage at the merge)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 9** (the round-8 analysis, 8 items): the IDVZ/PFOE backfill made purely additive (the trade schedule rebuilds only named funds), their daily join through a rivalfunds-owned gate file, an incremental security list, the AI-text name links, real names for past holdings, a measured Bloomberg capacity budget, and a read of the G5 history drift. Nothing in round 9 deploys, merges, flips a gate or calls Bloomberg from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-nm-3` -- real names for past holdings (CVO C-S36)
- Measured on the 10-05 render context: 135 keys carry a ticker-form name ('ATD CN Equity'); 0 of them sit in any fund's latest
  holdings; 128 were never in any G4 date and 7 sit in G4 with no name -- the G4 enrichment asks only for current holdings.
- Interface: `rivalfunds.security_names.handler_entry({"date", "sink"}, fetch=None)` reads the page day's newest
  holding_contribution, takes the keys with a blank or ticker-form name, drops the keys the newest `gold/security_names` object
  already names, asks `fetch(keys) -> {key: name}` for the rest (production: one LONG_COMP_NAME reference request, asked through
  `bbg_budget` first) and writes a new object with the prior names plus the new; `gold_holding_contribution` takes a key's name
  from it when G4 has none, before any G1 name. `enrichment_bloomberg --mode daily` runs it for the page day after its G4 lands.
- **Organic trigger:** the vehicle's 07:00 ET enrichment step (no vehicle file changes).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD bfad7625d7 (the package equals the deployed pin b166e04416))

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/nm-3.AC1.py` before you build.
- Build on your cb-1 commit (same slot): the production fetch asks `bbg_budget` with an estimate of 1 row per key and records the
  rows it gets; refused -> nothing asked, the stage reads SKIPPED with the reason.
- The production fetch reuses `enrichment_bloomberg`'s reference-request path (the one nm-2 added LONG_COMP_NAME to); never call it
  in a test.
- Keep nt-1's name pick (`tests/test_r7nt1_name_pick.py`) and round 8's hc-1 contracts (`tests/test_r8hc1_*.py`).

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order: no file there is written or read differently), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{7,8}/checks/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 9), the analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round8.md`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~5/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-9 chain owns. Tests go beside the code as `tests/test_r9nm3_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/security_names.py
data/etfs/scripts/rivalfunds/gold_holding_contribution.py
data/etfs/scripts/rivalfunds/enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/tests/test_r9nm3_*.py
data/etfs/scripts/rivalfunds/tests/test_r7nt1_name_pick.py
data/etfs/scripts/rivalfunds/tests/test_r8hc1_*.py
data/etfs/scripts/rivalfunds/tests/test_a1rk_contribution.py
data/etfs/scripts/rivalfunds/tests/test_e1_enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/tests/test_v2_enrichment_cli.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the names stage asks for exactly the ticker-named key, holding_contribution then names it, a second run asks for nothing, and a key with a G4 name is never asked (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/nm-3.AC1.py`)
- **J1** (JUDGMENT, graded by 3.0.0_SA_CVO~RV at L9) -- on the served page after the deploy and one vehicle run, holdings named by a '<id> XX Equity' form read 0, or each remaining one is named with its reason; positive control: the served 10-05 page (22 reader-visible ticker forms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-nm-3"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/checks/nm-3.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-nm-3" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~5/ETFS_RIVALS.TO-RIV-nm-3.past-holdings-real-names.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-nm-3.past-holdings-real-names`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round8.md @2097b5212b section 4; decomposition round 9 v1.0. Chain `~5`, slot `~5`, position 2 of 2. Checks dry-run at base CLOUD bfad7625d7 (the package equals the deployed pin b166e04416): nm-3.AC1 FAIL (3; control OK) as expected. Bounds: no deploy before the issuer's never-widen pair; D12 Step B and the D12 gate flip are issuer acts after nf-1 and gf-1 deploy.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>9</round>
<slot>~5</slot>
<fabric>site-z</fabric>
<status>complete</status>
