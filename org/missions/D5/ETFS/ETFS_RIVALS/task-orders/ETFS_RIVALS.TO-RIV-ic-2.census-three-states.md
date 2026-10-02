# ETFS_RIVALS task order -- `RIV-ic-2` -- ROUND 6 (ENRICHMENT): THE CENSUS READS THREE STATES (RFW-D14, RFW-U11 data half)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-ic-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~4</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-02 ~15:2xZ, --drift) -- carrier C1: 31 sentinels scanned, 12 gates armed, none names rivalfunds/, etfs-rivalfunds or this cell's files; C2-C5 not scanned inside the 90 s budget (blind there); the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 6** makes the A1 tables follow their inputs, puts the AI accounts into the scheduled path, adds the plausibility guard, fixes dividend currency and exit pricing, gives the census three states and the page real names, and carries the 33-item page walk (PRD v0.12). Nothing in round 6 deploys from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-ic-2` -- the census reads three states (RFW-D14, RFW-U11 data half)
- `gold_input_census` status gains "covered_by_fallback" with a new column `fallback`: "holding_implied" for a price,
  "other_fund" for a GICS sector taken from another fund's file (CALL 9).
- "missing" is only for an input no fallback covers; `fallback` is NULL where none applies.
- "arrived" stays arrived. The page can count per state.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD bdbd7a257b (rv-fast; package unchanged since 722f0db291, the deployed pin))

- Today the enum is arrived | missing | stale; the served census lists 765 securities 'missing, no G4 row ...' though the rankings price them (RFW-D14).
- `fallback` is NULL where none applies.
- AMENDMENT A1 (issuer, 2026-10-02 ~16:4xZ; CRO~RV GICS census @308f982bb8, section 3 "Also": the census should read the fund's own G1 sector before calling a security missing, which turns 763 "missing" into 118): a GICS input whose sector is present in the fund's OWN G1 file reads `arrived` (fallback NULL) even with no G4 row. Your build already passes limbs (b) and (c) of AC4; limb (a) is the change. Keep AC1-AC3 passing.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/` and round 5's `.../round5/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.12), the walk brief `docs/briefs/rivalfunds-ui-data-walk-20261002.md` and its register `docs/briefs/rivalfunds-ui-data-findings-20261002.json`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~4/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-6 chain owns, and none of the merge hookups the decomposition names (the issuer adds them). Tests go beside the code as `tests/test_r6ic2_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file, never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/gold_input_census.py
data/etfs/scripts/rivalfunds/tests/test_r6ic2_*.py
data/etfs/scripts/rivalfunds/tests/test_a1ic_census.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a price with no G4 row, covered by the holding-implied price, reads covered_by_fallback / holding_implied (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ic-2.AC1.py`)
- **AC2** -- a GICS sector from another fund's file reads covered_by_fallback / other_fund; absent everywhere reads missing (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ic-2.AC2.py`)
- **AC3** -- control: an arrived input stays arrived (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ic-2.AC3.py`)
- **AC4** -- (a fourth criterion; reason: the CRO census amendment A1 above) a GICS sector in the fund's own G1 file with no G4 row reads arrived; control: no own sector, no G4, no other file stays missing; another fund's file reads covered_by_fallback / other_fund (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ic-2.AC4.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-ic-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ic-2.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-ic-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ic-2.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-ic-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ic-2.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC4" cell_refs="RIV-ic-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/ic-2.AC4.py</invocation><expect>AC4 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~4/ETFS_RIVALS.TO-RIV-ic-2.census-three-states.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-ic-2.census-three-states`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-5 analysis @56c99763bb (msg 28485) section 4 + PRD v0.12 @afc2bed44f
(RFW register, msg 28535); decomposition round 6 v1.0; Andrew-direct "/canonical-drive with max parallelization on
subagents" (cooRV record 141xZ). Chain `~4`, slot `~4`, position 1 of 1. Checks dry-run at base CLOUD bdbd7a257b (rv-fast; package unchanged since 722f0db291, the deployed pin):
ic-2.AC1 FAIL as expected; ic-2.AC2 FAIL as expected; ic-2.AC3 PASS (control) as expected.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<slot>~4</slot>
<fabric>site-z</fabric>
