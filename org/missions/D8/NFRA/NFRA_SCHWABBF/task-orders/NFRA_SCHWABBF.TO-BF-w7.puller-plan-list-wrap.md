# TO NFRA_SCHWABBF.TO-BF-w7 -- the puller's plan filter no longer throws on the List[object] plan (one line, with a test arm that passes a real List)

<to_id>NFRA_SCHWABBF.TO-BF-w7</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~2</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>release-puller</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-w-7` (`decompositions/NFRA_SCHWABBF_DECOMP_R6.md`, AMENDMENT 3) |
**outcome_ref:** FWD-1, FWD-6 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-w-7`. In `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1`, the function `Select-PlanAsOf` (about line 304) begins `$all = @($planItems)`. The script calls it (about line 600) with `$plan`, which the script builds as `New-Object System.Collections.Generic.List[object]` (about line 534). In Windows PowerShell 5.1 that wrap THROWS `Argument types do not match` when the argument arrives untyped as a `List[object]` (reproduced by the issuer: `function G($p){ @($p).Count }; G $list` throws; `@($list | ForEach-Object { $_ })` returns 4). So every live run (daily pull and backfill) loses its plan and exits 9 or 5. The tests missed it because the harness (`data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py`, the `'filter'` case) builds `$plan` with `@(...)`, an array. This cell fixes the one line and makes the test pass a real `List[object]`. It edits one `.ps1` and one test file; it runs nothing against Schwab or AWS and does not upload or deploy.

**Build.**
1. In `sdd-daily-pull.ps1` change ONLY the first line of `Select-PlanAsOf`'s body to `$all = @($planItems | ForEach-Object { $_ })`. Then census EVERY other expression of the form `@($x)` in the script where `$x` may be a `System.Collections.Generic.List[...]` passed through an untyped parameter or variable (the Lists the script builds are `$short`, `$surp`, `$coll`, `$files`, `$plan`, `$undated`, `$failList`; read each use). For any other site with the same shape, apply the same pipe form and list it in your report; for a site that is not at risk (a typed parameter, or a plain array) change nothing and say so. No other line of the file changes.
2. In `test_sdd_daily_pull_key_form.py` add a case to the PowerShell harness input, `filter_list`: the same as `'filter'` but `$plan` is a REAL `New-Object System.Collections.Generic.List[object]` filled by `.Add(...)` with the same row objects, and add Python arms whose names contain `select_plan_list`: (a) a List of 4 rows with `day` empty keeps all 4 with `die_code` 0; (b) the same List with a day that matches 2 rows keeps exactly those 2 and `excluded` 2; (c) a List with no matching day returns `die_code` 9; (d) an EMPTY List with `day` empty returns `kept` empty and `die_code` 0. The existing arms stay unchanged.
3. Mutant control: run arm (a) once against the file as committed at HEAD BEFORE your edit (with `git stash` unavailable, use `git show HEAD:<path>` into a temp copy and point the harness at it, or run the arm before editing) and report that it FAILED there (the throw), then after the fix that it passes.

### ACCEPTANCE

<criterion id="BF6-w7-AC1" cell_refs="BF-w-7"><invocation>python -m pytest data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py -q -p no:cacheprovider --color=no -k select_plan_list</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF6-w7-AC1` -- the plan filter handles a real `List[object]` in Windows PowerShell 5.1: keeps all, keeps one day, die 9 on no match, empty in and out.

<criterion id="BF6-w7-AC2" cell_refs="BF-w-7"><invocation>python -m pytest data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py data/canonical/schwab/tests/test_sdd_daily_pull_state.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF6-w7-AC2` -- the control: the whole bronze-key test file (13 passed at the base) and the state-tier file (6 passed) still pass with the edited script.

<expected_criteria>BF6-w7-AC1,BF6-w7-AC2</expected_criteria>

Dry-run at the base: AC1 "deselected" (rc 5, no test named `select_plan_list`) -- FAIL as expected; AC2 `19 passed` -- PASS as expected (a control that must stay green).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **WORLD floor, nothing run or uploaded.** Do not run the puller, contact Schwab or AWS, or upload the script: `TO-BF-r5` (CloudOps) uploads it after this merges. TIME-CRITICAL: the 49F pull fires at 21:45Z tonight; do nothing the order does not ask for.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W2-S<k>`; read the investigation file for the highest `W2-S<k>` and use the next; the gate may renumber it). Append the row to `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` at the BYTE level (the file mixes CRLF and LF: do not use the Edit tool on it; insert before the closing `]`; the previous last row gains a trailing comma). Do not weaken the test to pass. The `.ps1` file must keep its own line endings and encoding; check `git diff --numstat` shows only the changed lines.

<paths>
infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1
data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md</decomp_doc> (round 6, AMENDMENT 3), cell `BF-w-7`.
<owned_cells>BF-w-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF6-w7-AC1, BF6-w7-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~2/NFRA_SCHWABBF.TO-BF-w7.puller-plan-list-wrap.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF6-w7-AC1,BF6-w7-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the changed line, every other `@($x)` site you examined with your verdict, the whole-file numstat of the `.ps1`, the mutant-control result (before and after), the two pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: RUN by reading -- the 49F pull fires 09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z; the cell changes script text only and nothing is uploaded until `TO-BF-r5`.
comp-iam: DECLARED-NOT-APPLICABLE -- script text; no grant (scanned the one `.ps1`, 1 file; BLIND: the live IAM plane).
comp-adversary: DECLARED-NOT-APPLICABLE as a lens run; finding inlined: the harness passed arrays where the script passes a List, so the test is the part that was wrong as much as the line.
lane: the <paths> block IS the grant.
</preflight>

Source: `2.0.0_SA_COO~SA` msg 110140 and 110141 (the Alongside first pull); CTO msg 110143 (HOLD R5, cut the fix now); the round-3 cell that introduced `Select-PlanAsOf` (commit `b62305e4421`); decomposition round 6.
