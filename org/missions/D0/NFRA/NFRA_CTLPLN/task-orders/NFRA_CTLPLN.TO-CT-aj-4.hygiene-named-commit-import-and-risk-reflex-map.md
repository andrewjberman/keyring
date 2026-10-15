# TO NFRA_CTLPLN.TO-CT-aj-4 -- workstream BATCH round 7 (cell CT-aj-4): ONE hygiene batch -- test_named_commit_deploy.py runs to its last line (W108-S2), and the risk reflex's map knows portal .tsx (W110-S1)

<to_id>NFRA_CTLPLN.TO-CT-aj-4</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~115</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>BATCH</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-aj-4` (`decompositions/NFRA_CTLPLN_DECOMP.round20.md`) | **outcome_ref:** hygiene |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Two small items, ONE cell. Read rows `NFRA_CTLPLN-W108-S2` and `NFRA_CTLPLN-W110-S1` first (Grep each id in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`).

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. **`W108-S2`.** `python .tools/tests/test_named_commit_deploy.py` prints PASS for cases 1-7, then raises `ModuleNotFoundError: No module named 'git_bash_resolver'` in case 8's fixture setup (its temporary repository has no `.tools/` on the import path). Fix the import path in the test (not in `.tools/git_bash_resolver.py`): put the real `.tools` directory on `sys.path` of the child process the test starts, or run the child with `PYTHONPATH` set to it. Done when the test prints its last line `NAMED-COMMIT-TEST cases=8/8 ok=True`. The test must write nothing into the real tree (check `git status --porcelain` before and after; at the cut a run left no file there).
2. **`W110-S1`.** The commit-time risk reflex is `comp-pulse diff` (`.tools/comp-pulse` calls `org/modules/graph/comp_pulse.py`); its danger map is stale for `portal/**/*.tsx` (DSGN_RBNDV2 row W8-S1: a portal `.tsx` commit passed with 0 of 3 files checked). Refresh ONLY the map entries so a staged `portal/**/*.tsx` path is classed (find the map in that file; add the `.tsx` portal paths to the class the portal's other source files already have). Add no new check and change no other behaviour. `.tools/tests/test_comp_pulse_battery.py` must pass no fewer arms than the 10 of 12 it passes at the cut.
3. A NEW test `.tools/tests/test_round20_hygiene.py` with `--map`: in a temporary repository, stage one `portal/src/x.tsx` and run `comp-pulse diff` (the real script) and require its output to class the path (print the line it uses) where the base map printed 0 files classed; and one `.py` path classed as before. Last line `HYGIENE-MAP tsx_classed=<n> py_classed=<m> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~115/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W115-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. 

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTaj4-AC1" cell_refs="CT-aj-4"><invocation>python .tools/tests/test_named_commit_deploy.py</invocation><expect>cases=8/8</expect></criterion>
`CTaj4-AC1` -- the named-commit deploy test runs through all 8 cases (base: it stops after case 7 with `ModuleNotFoundError`); report the whole last line.

<criterion id="CTaj4-AC2" cell_refs="CT-aj-4"><invocation>python .tools/tests/test_round20_hygiene.py --map</invocation><expect>ok=True</expect></criterion>
`CTaj4-AC2` -- a staged portal `.tsx` is classed by the risk reflex's map (base: the file does not exist); report the whole last line.

<criterion id="CTaj4-AC3" cell_refs="CT-aj-4"><invocation>python .tools/tests/test_comp_pulse_battery.py</invocation><expect>/12 PASS (denominator 12)</expect></criterion>
`CTaj4-AC3` -- the comp-pulse battery passes no fewer than 10 of 12 after the map change (base read 10/12 at the issuer's dry-run and 11/12 at the worker's: one arm, B1-PULSE-BUDGET-REACHED, is time-dependent; the denominator stays 12 and the count may be 10 to 12, never lower); report the whole last line.
</proof_of_spec>

<expected_criteria>CTaj4-AC1,CTaj4-AC2,CTaj4-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~115/NFRA_CTLPLN.TO-CT-aj-4.hygiene-named-commit-import-and-risk-reflex-map.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTaj4-AC1,CTaj4-AC2,CTaj4-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round20.md</decomp_doc>
<owned_cells>CT-aj-4</owned_cells>
</decomp_ref>

<paths>
.tools/tests/test_named_commit_deploy.py
org/modules/graph/comp_pulse.py
.tools/tests/test_round20_hygiene.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the named-commit test writing fixture ledgers into the real tree (the porcelain check before and after); the map edit adding a class that changes a verdict for non-`.tsx` paths (the `.py` arm and the battery); `comp_pulse.py` is a shared graph module: edit the map entries only; BLIND: the real grading of `.tsx` is DSGN_RBNDV2's merge-time portal checks.
risk: LOCAL -- test files and one map table in a read-only reflex.
lane: the <paths> block IS the grant (worker RULING 1). `org/modules/graph/comp_pulse.py` is a graph-module file; the CTO ordered the map refresh (msg 109393, round-19 analysis ruling 6).
</preflight>

Base checks, dry-run by the issuer before the cut: CTaj4-AC1 FAIL as expected (stops after case 7); CTaj4-AC2 FAIL as expected (the file does not exist); CTaj4-AC3 base `COMP-PULSE BATTERY: 10/12 PASS (denominator 12)` (a control; two arms fail at the cut).
Source: CTO round-19 analysis sections 2-3 (`ledger/ROUND_ANALYSIS.round19.md` @2009d89478), msg 109424; hygiene.
