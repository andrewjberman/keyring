# ETFS_RIVALS task order -- `RIV-lg-1` -- ROUND 8 WORKSTREAM A (ENRICHMENT): THE BLOOMBERG LEG CARRIES INDEX-CONTROL-SIZED HOLDINGS AND SWITCHES D12 AND D13 APART (Z-S20)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-lg-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~4</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L6 (2026-10-04 ~21:1xZ, --drift) -- WITHIN BUDGET, 6 of 6 carriers scanned (C1=29 C2=32 C3=12 C4=21 C5=334 C6=1); 1 gate armed, not on this project; the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 8, workstream A** (Andrew-direct 2026-10-04 "yes, build round 8 tonight"): the AI step can no longer cost the page its republish, the AI prose reads every security under the page's one name, the render remainder, the census price repair, and the Bloomberg leg sized for the benchmarks ACWI and IWM with its gate split in two. Nothing in round 8 deploys, merges or flips a gate from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-lg-1` -- the Bloomberg leg carries index-control-sized holdings and switches D12 and D13 apart (row Z-S20)
- Measured 2026-10-03 for 2026-10-01: IDVZ 45 / PFOE 24 / ACWI 2,198 / IWM 1,979 rows. `excel_fetch` runs one query per
  date with max_rows=2000 and raises RuntimeError on overflow, which `_handler_entry` does not catch: the leg crashes. The
  gate `RIVALFUNDS_LEG_ENABLE` switches every pending key at once.
- Interface: an `index_control` fund is queried on its own per date under a cap >= 2,500 and < 50,000; the range read never
  truncates silently; an overflow is a per-name partial (PARTIAL, the fund named, the others land); `universe` reads
  `RIVALFUNDS_LEG_D12` (the HOME entries' `pending_source_policy`: IDVZ, PFOE) and `RIVALFUNDS_LEG_D13` (the `"leg":
  "pending"` entries ACWI and IWM); `RIVALFUNDS_LEG_ENABLE=1` turns both on.
- AMENDED 2026-10-05 (Andrew-direct: "SCHY is NOT the benchmark for IDVZ. The benchmark for IDVZ is ACWI ... the benchmark
  for PFOE is IWM"): SCHY is a rival in `peer_groups.json` itself (role rival, its pending_role removed), under every gate
  state; ACWI and IWM are the benchmarks once D13 flips.
- **Organic trigger:** the vehicle's 07:00 ET leg. Nothing here flips a gate: each flip and its backfill is an issuer act.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 1c31a5f6ce (the package equals the deployed pin 75ad1e4d2e))

- Each check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/lg-1.AC1.py` and `lg-1.AC2.py`
  before you build. AC1 drives `_handler_entry(event, fetch=None)` through `excel_fetch` with a FAKE pywin32 (it replaces
  `pythoncom`, `pywintypes`, `win32com.client` in `sys.modules`); each fake sheet answers the BQL in its A1 formula, so a
  control on its own sheet (or its own query round) is what makes (b) pass. One date may need more than one sheet now.
- `universe._default()` caches on a stamp that includes `leg_enabled()`; the stamp must include every gate, or a flip
  in-process reads the stale map (AC2 flips gates in one process).
- The vehicle's leg exit codes (module docstring: 0 landed, 1 unreachable, 2 partial, 3 nothing written) stay as they are;
  an overflow on one name is exit 2, never a traceback.
- Andrew's smoke (2026-10-04): "S-C-H-Y is not the benchmark. The benchmark is ACWI ... P-F-O-E, the benchmark is I-W-M."
  That is the D13 gate's effect once the issuer flips it; this order only builds the switch.
- Keep round 5's leg-inert contract for the pending ENTRIES (`tests/test_r5l1_leg_inert.py`: all gates unset admits no
  ACWI/IWM) and the b-1 channel tests; the SCHY role assertions in `test_r5l1_leg_inert.py` and `test_g01_universe.py` move
  to rival by this amendment.
- AMENDMENT (2026-10-05, issuer): your first build (f8124d0969, 2c885a91f3) is on your branch and passes AC1; re-cut only
  what AC2 now asks (SCHY rival in the map) and re-run both checks.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{5,6,7}/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.14 @4cc8e40575), the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 8 A), and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~4/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-8 chain owns. Tests go beside the code as `tests/test_r8lg1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/collector_bloomberg.py
data/etfs/scripts/rivalfunds/universe.py
data/etfs/scripts/rivalfunds/peer_groups.json
data/etfs/scripts/rivalfunds/tests/test_r8lg1_*.py
data/etfs/scripts/rivalfunds/tests/test_b1_bloomberg_channel.py
data/etfs/scripts/rivalfunds/tests/test_r5l1_leg_inert.py
data/etfs/scripts/rivalfunds/tests/test_g01_universe.py
data/etfs/scripts/rivalfunds/tests/test_r5m2_dedup_memo.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a 2,300-row control beside two rivals lands whole, queried on its own; a 50,000-row overflow is a per-name PARTIAL with the fund named and the others landed; two rivals alone still land OK (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/lg-1.AC1.py`)
- **AC2** -- RIVALFUNDS_LEG_D12 and RIVALFUNDS_LEG_D13 switch the home funds' source and the benchmarks independently; SCHY reads rival in every state; RIVALFUNDS_LEG_ENABLE=1 turns both on (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/lg-1.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-lg-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/lg-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-lg-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/lg-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~4/ETFS_RIVALS.TO-RIV-lg-1.bloomberg-leg-control-sized-gate-split.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-lg-1.bloomberg-leg-control-sized-gate-split`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-7 analysis @115645c4b4 section 3 (items 1, 2, 4) + Andrew-direct @0a4321b843 ("yes, build round 8 tonight"); decomposition round 8 workstream A v1.0. Chain `~4`, slot `~4`, position 1 of 1. Checks dry-run at base CLOUD 1c31a5f6ce (the package equals the deployed pin 75ad1e4d2e): lg-1.AC1 FAIL (3; control OK), lg-1.AC2 FAIL (2; control OK) as expected. Bounds: no merge before the 2026-10-05 07:00 ET vehicle pull; no deploy before the 13:30Z grades.

**AMENDMENT 1 (2026-10-05 ~03:5xZ, issuer):** Andrew-direct benchmarks (record cooRV_ANDREW_DIRECT_20261005_03xxZ_RIVALFUNDS_BENCHMARKS_...); AC2 re-pointed (SCHY rival in every state); paths += peer_groups.json. Dry-run: CLOUD FAIL 3, the first lg-1 build FAIL 2 ((b),(c)). Graded by: to-pipeline-gate on a modified order reads only GATE (viii) <placeholders> (NONE).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>8</round>
<slot>~4</slot>
<fabric>site-z</fabric>
