# ETFS_RIVALS task order -- `RIV-rp-1` -- ROUND 8 WORKSTREAM A (ENRICHMENT): THE CENSUS PRICE REPAIR: ONE KEY SPACE FOR THE HOLDING-IMPLIED PRICE, AND A MISS THAT NEVER CLAIMS A PRICE (Z-S18)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-rp-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~3</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L6 (2026-10-04 ~21:1xZ, --drift) -- WITHIN BUDGET, 6 of 6 carriers scanned (C1=29 C2=32 C3=12 C4=21 C5=334 C6=1); 1 gate armed, not on this project; the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 8, workstream A** (Andrew-direct 2026-10-04 "yes, build round 8 tonight"): the AI step can no longer cost the page its republish, the AI prose reads every security under the page's one name, the render remainder, the census price repair, and the Bloomberg leg sized for the benchmarks ACWI and IWM with its gate split in two. Nothing in round 8 deploys, merges or flips a gate from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-rp-1` -- the census price repair (row Z-S18 + the contradictory miss reason)
- Z-S18: `alias` comes from the wide g1w and `books` from the 14-day g1, so a CUSIP resolved only in an older report misses
  its holding-implied price (`rp-1.AC1`).
- A census price row that reads `missing` never claims the rankings price it (`gold_input_census.py` ~:183, 44 served rows)
  (`rp-1.AC2`).
- **Organic trigger:** the 07:00 ET marker publish.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 1c31a5f6ce (the package equals the deployed pin 75ad1e4d2e))

- Each check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rp-1.AC1.py` and `rp-1.AC2.py`
  before you build.
- Keep round 7's census contracts: cg-1 (the census reads the rankings' GICS classification) and cs-1 (census and header
  agree on freshness); their tests are `tests/test_r7cg1_census_reads_rankings_gics.py` and `test_r7cs1_census_header_agree.py`.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{5,6,7}/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.14 @4cc8e40575), the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 8 A), and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~3/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-8 chain owns. Tests go beside the code as `tests/test_r8rp1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/gold_input_census.py
data/etfs/scripts/rivalfunds/tests/test_r8rp1_*.py
data/etfs/scripts/rivalfunds/tests/test_a1ic_census.py
data/etfs/scripts/rivalfunds/tests/test_r6ic2_census_three_states.py
data/etfs/scripts/rivalfunds/tests/test_r7cg1_census_reads_rankings_gics.py
data/etfs/scripts/rivalfunds/tests/test_r7cs1_census_header_agree.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a CUSIP resolved only in an older report still gets its holding-implied census price (alias and books read one key space); a never-resolved line keeps covered_by_fallback / holding_implied (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rp-1.AC1.py`)
- **AC2** -- a census price row reading missing never claims the rankings price it; a holding-implied row keeps its reason (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rp-1.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-rp-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rp-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-rp-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rp-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~3/ETFS_RIVALS.TO-RIV-rp-1.census-price-repair.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-rp-1.census-price-repair`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-7 analysis @115645c4b4 section 3 (items 1, 2, 4) + Andrew-direct @0a4321b843 ("yes, build round 8 tonight"); decomposition round 8 workstream A v1.0. Chain `~3`, slot `~3`, position 1 of 1. Checks dry-run at base CLOUD 1c31a5f6ce (the package equals the deployed pin 75ad1e4d2e): rp-1.AC1 FAIL (1; control OK), rp-1.AC2 FAIL (1; control OK) as expected. Bounds: no merge before the 2026-10-05 07:00 ET vehicle pull; no deploy before the 13:30Z grades.

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>8</round>
<slot>~3</slot>
<fabric>site-z</fabric>
