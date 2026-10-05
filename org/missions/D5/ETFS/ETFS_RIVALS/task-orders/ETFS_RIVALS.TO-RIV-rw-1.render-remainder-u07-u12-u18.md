# ETFS_RIVALS task order -- `RIV-rw-1` -- ROUND 8 WORKSTREAM A (ENRICHMENT): THE RENDER REMAINDER: TREND CAPTION, COLLAPSED EMPTY WINDOWS, TWO-SENTENCE LEAD (RFW-U07, U12, U18)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-rw-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L6 (2026-10-04 ~21:1xZ, --drift) -- WITHIN BUDGET, 6 of 6 carriers scanned (C1=29 C2=32 C3=12 C4=21 C5=334 C6=1); 1 gate armed, not on this project; the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 8, workstream A** (Andrew-direct 2026-10-04 "yes, build round 8 tonight"): the AI step can no longer cost the page its republish, the AI prose reads every security under the page's one name, the render remainder, the census price repair, and the Bloomberg leg sized for the benchmarks ACWI and IWM with its gate split in two. Nothing in round 8 deploys, merges or flips a gate from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-rw-1` -- the render remainder (RFW-U07, U12, U18)
- U07: the trend caption reads the dates and trading days only; the unit moves off it (`rw-1.AC1`).
- U12: consecutive noted 0-trade windows collapse into one line, with the notes kept inside (`rw-1.AC2`).
- U18: an all-caps "CORP." ends a sentence, so the account's lead is two sentences (`rw-1.AC3`).
- **Organic trigger:** the 07:00 ET marker publish and the 09:00 ET sweep publish.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 1c31a5f6ce (the package equals the deployed pin 75ad1e4d2e))

- Each check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rw-1.AC1.py`, `rw-1.AC2.py` and
  `rw-1.AC3.py` before you build. Every control arm PASSES at base and must still PASS.
- This order follows an-1 on the same slot and the same file (`render.py`); build on your an-1 commit.
- Keep CRO~RV's layout (`tests/test_crorv_layout.py`) and the round-6/7 trend and audit-trail contracts
  (`test_r6ui3_trend_card.py`, `test_r6ui5_census_and_audit_trail.py`, `test_r7rd1_page_walk_remainder.py`).

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{5,6,7}/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.14 @4cc8e40575), the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 8 A), and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-8 chain owns. Tests go beside the code as `tests/test_r8rw1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/test_r8rw1_*.py
data/etfs/scripts/rivalfunds/tests/test_r6ui3_trend_card.py
data/etfs/scripts/rivalfunds/tests/test_r6ui5_census_and_audit_trail.py
data/etfs/scripts/rivalfunds/tests/test_r6ui4_ai_account_cards.py
data/etfs/scripts/rivalfunds/tests/test_r7rd1_page_walk_remainder.py
data/etfs/scripts/rivalfunds/tests/test_crorv_layout.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the trend caption carries the dates and trading days only, the unit off it; every Tilt/Bet pill keeps its title (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rw-1.AC1.py`)
- **AC2** -- consecutive noted 0-trade windows collapse into one line with their notes inside; a window with a trade keeps its heading and rows (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rw-1.AC2.py`)
- **AC3** -- an all-caps 'CORP.' ends a sentence so the account lead is two sentences; a mid-sentence 'Inc.' does not end one (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rw-1.AC3.py`)
- **J1** (JUDGMENT, graded by 3.0.0_SA_CVO~RV at L9 on the served page) -- the served page after the deploy reads the trend caption, the audit trail and the AI leads as the three acceptances say; positive control: the served 2026-10-02 page

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-rw-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rw-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-rw-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rw-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-rw-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/rw-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-rw-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-rw-1.render-remainder-u07-u12-u18.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-rw-1.render-remainder-u07-u12-u18`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-7 analysis @115645c4b4 section 3 (items 1, 2, 4) + Andrew-direct @0a4321b843 ("yes, build round 8 tonight"); decomposition round 8 workstream A v1.0. Chain `~2`, slot `~2`, position 2 of 2. Checks dry-run at base CLOUD 1c31a5f6ce (the package equals the deployed pin 75ad1e4d2e): rw-1.AC1 FAIL (2; control OK), rw-1.AC2 FAIL (2; control OK), rw-1.AC3 FAIL (1; control OK) as expected. Bounds: no merge before the 2026-10-05 07:00 ET vehicle pull; no deploy before the 13:30Z grades.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>8</round>
<slot>~2</slot>
<fabric>site-z</fabric>
