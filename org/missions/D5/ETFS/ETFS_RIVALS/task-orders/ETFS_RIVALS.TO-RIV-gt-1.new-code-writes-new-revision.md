# ETFS_RIVALS task order -- `RIV-gt-1` -- ROUND 11 (ENRICHMENT): A SAME-INPUT G5 PASS AT A NEW CODE VERSION WRITES A NEW REVISION; AT THE SAME VERSION IT STILL WRITES NOTHING (FIRST)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-gt-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the issuer registers any stage at the merge)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 11** (the round-10 analysis): the trade schedule writes a new revision when a same-input pass runs at a new code version (so the issuer's served replay of the four code-defect classes can land), and the G5 drift record names its data-arrival class's cause as data arrival. Nothing in round 11 deploys, merges, flips a gate or calls Bloomberg from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-gt-1` -- a same-input G5 pass at a new code version writes a new revision (rows Z-W3-S23 / Z-S42; analysis item 1, FIRST)
- Measured 2026-10-05 by RIV-rp-2's worker: `gold_trade_schedule._g5_target` returns the newest existing object whenever it records
  the same held funds, so a `rebuild_funds` replay at a date whose live G5 already sits at the newest G1 revision reads OK and
  writes nothing (written_new 0, object count unchanged; live 2026-01-02 G5 and G1 both at `20261005T054335Z-8b69497a75c4`).
- Interface: `gold_trade_schedule.GOLD_VERSION` (a module string). Every G5 object the stage writes carries it in its parquet schema
  metadata under `producer_version`; `_g5_target` reuses the newest existing object only when it records the same held funds AND the
  same `producer_version` as the running code (an object without the key reads as a different version); otherwise the next
  `-v<NN>` object, never an overwrite. Both arms are the criterion: new version -> a new revision; same version -> nothing.
- **Organic trigger:** the batch chain's G5 step, and the issuer's served replay of the four code classes (round-10 analysis item 2).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 134485f75b (deployed Lambda code = b8b47bb8e7 + the Z-S31 repair; eg-1 live on the vehicle))

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round11/checks/gt-1.AC1.py` before you build.
- YOUR BASE IS DELIBERATELY `0997603f5d` (round 10 after eg-1, BEFORE ok-1's re-keying), plus the issuance commit: the issuer's
  served replay runs this branch's code, and ok-1's key change must not ride it (the replay census isolates the four classes).
  Do NOT merge or rebase CLOUD into your branch; the issuer merges it.
- Keep nf-1's `rebuild_funds` carry, RIV-v-2's revision order and the held-funds metadata (`tests/test_r9nf1_*.py`,
  `tests/test_g52_trade_schedule_v2.py`, `tests/test_r5*`); G6 (flow_reconciliation) follows the G5 revision name as today.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order: no file there is written or read differently), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round11/checks/` and the earlier rounds' `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{9,10}/checks/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md` (round 11), the analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round10.md`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any environment gate flip outside a test, any file another round-11 chain owns. Tests go beside the code as `tests/test_r11gt1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/tests/test_r11gt1_*.py
data/etfs/scripts/rivalfunds/tests/test_g52_trade_schedule_v2.py
data/etfs/scripts/rivalfunds/tests/test_r9nf1_*.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a same-input pass at the same code version writes nothing; at a new version (and over a legacy object) it writes a new -v<NN> revision stamped with that version, the carried funds unchanged (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round11/checks/gt-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-gt-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round11/checks/gt-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-gt-1.new-code-writes-new-revision.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-gt-1.new-code-writes-new-revision`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round10.md @134485f75b section 4 (items 1 and 4 are cells; 2, 3 and 5 are issuer acts); decomposition round 11 v1.0. Chain `~1`, slot `~1`, position 1 of 1. Checks dry-run at base CLOUD 134485f75b (deployed Lambda code = b8b47bb8e7 + the Z-S31 repair; eg-1 live on the vehicle): gt-1.AC1 FAIL (2; control (a) PASS) as expected. Bounds: no deploy before the issuer's never-widen pair; the served replay (item 2) runs gt-1's branch code BEFORE the ok-1 deploy (item 3).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>11</round>
<slot>~1</slot>
<fabric>site-z</fabric>
