# ETFS_RIVALS task order -- `RIV-dt-1` -- ROUND 8 WORKSTREAM A (ENRICHMENT): THE DEADLINE-AWARE VENDOR TIMEOUT: THE AI STEP NEVER COSTS THE PAGE ITS REPUBLISH (W1-S46)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-dt-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L6 (2026-10-04 ~21:1xZ, --drift) -- WITHIN BUDGET, 6 of 6 carriers scanned (C1=29 C2=32 C3=12 C4=21 C5=334 C6=1); 1 gate armed, not on this project; the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 8, workstream A** (Andrew-direct 2026-10-04 "yes, build round 8 tonight"): the AI step can no longer cost the page its republish, the AI prose reads every security under the page's one name, the render remainder, the census price repair, and the Bloomberg leg sized for the benchmarks ACWI and IWM with its gate split in two. Nothing in round 8 deploys, merges or flips a gate from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-dt-1` -- the deadline-aware vendor timeout (W1-S46; CTO round-7 ruling 1)
- The worst case today: a vendor call starting near the AI deadline runs `ai_client.TIMEOUT_S` = 120 s, which leaves 30 s
  of the 150 s margin for a republish that takes ~68 s at p95 (publish-page Lambda, 14 days, n=29: p95 68.1 s, max 81.2 s;
  the act-3 publish with refresh_a1 took 117.5 s; the CVO measured ~88 s).
- Interface: `chat(timeout=)`; a deadline client hands each call min(TIMEOUT_S, the time left); `sweep.REPUBLISH_RESERVE_S`
  >= 88 s is subtracted from the remaining time. A planted slow vendor at the deadline still republishes: the account is
  recorded FAILED and the page publishes without it.
- **Organic trigger:** the 09:00 ET sweep.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 1c31a5f6ce (the package equals the deployed pin 75ad1e4d2e))

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/dt-1.AC1.py` before you build.
- The CTO's ruling: each vendor call's timeout is the lesser of its own timeout and (remaining budget minus a republish
  reserve measured from the republish's p95 plus a margin). The sweep must never lose the page to the AI step: the page is the
  product, the AI account an enrichment.
- Keep round 7's contracts: sa-1 (the sweep runs the AI step with a deadline, then republishes), pv-1 (`run_path` from the
  trigger), cu-1 (open cursors continue). Their tests are `tests/test_r7sa1_sweep_ai_step.py`, `test_r7pv1_run_path_trigger.py`,
  `test_r7cu1_sweep_cursors.py`.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{5,6,7}/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.14 @4cc8e40575), the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 8 A), and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-8 chain owns. Tests go beside the code as `tests/test_r8dt1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/ai_client.py
data/etfs/scripts/rivalfunds/ai_stage.py
data/etfs/scripts/rivalfunds/sweep.py
data/etfs/scripts/rivalfunds/tests/test_r8dt1_*.py
data/etfs/scripts/rivalfunds/tests/test_r6ap1_ai_stage.py
data/etfs/scripts/rivalfunds/tests/test_r7sa1_sweep_ai_step.py
data/etfs/scripts/rivalfunds/tests/test_r7pv1_run_path_trigger.py
data/etfs/scripts/rivalfunds/tests/test_d1_sweep.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a planted slow vendor at the deadline is handed a timeout that leaves the republish reserve; the page still republishes with the account FAILED; far from the deadline no call gets less than the vendor's own timeout (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/dt-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-dt-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/checks/dt-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-dt-1.deadline-aware-vendor-timeout.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-dt-1.deadline-aware-vendor-timeout`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-7 analysis @115645c4b4 section 3 (items 1, 2, 4) + Andrew-direct @0a4321b843 ("yes, build round 8 tonight"); decomposition round 8 workstream A v1.0. Chain `~1`, slot `~1`, position 1 of 1. Checks dry-run at base CLOUD 1c31a5f6ce (the package equals the deployed pin 75ad1e4d2e): dt-1.AC1 FAIL (4; control OK) as expected. Bounds: no merge before the 2026-10-05 07:00 ET vehicle pull; no deploy before the 13:30Z grades.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>8</round>
<slot>~1</slot>
<fabric>site-z</fabric>
