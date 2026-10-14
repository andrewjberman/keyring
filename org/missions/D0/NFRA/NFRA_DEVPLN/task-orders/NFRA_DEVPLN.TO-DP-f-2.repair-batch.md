# TO NFRA_DEVPLN.TO-DP-f-2 -- round 5 ENRICHMENT DP-f-2: the repair batch (one test seam variable, not two; exit checks on the merge-forward self-test's fixture writes)

<to_id>NFRA_DEVPLN.TO-DP-f-2</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~2</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>ENRICHMENT</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-f-2` (`decompositions/NFRA_DEVPLN_DECOMP.round5.md`) | **outcome_ref:** FWD-2, FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Two small repairs from round 4, batched. Your worktree has the portal repo at `portal/` (read only for you; do not fetch it).

### BUILD

1. ONE test seam variable, not two (row W1-S14). `approval_read` in `.tools/open-calls.py` reads a foreign box's list from the freshest of three sources: the cluster copy, `origin/box/<box>` (git) and the working tree. Its test needed a controlled stand-in for each: `OPAL_CLOUD_READ_LOCAL=<dir>` (a directory holding `box=<box>/open_calls.json`, standing for the cluster copy) and a second variable `OPAL_GIT_READ_ROOT` (a repository root to read the git copy from). Remove `OPAL_GIT_READ_ROOT` entirely. The single variable `OPAL_CLOUD_READ_LOCAL=<dir>` now also stands in for the GIT source: a file `git=<box>/open_calls.json` in the same directory is read as the `origin/box/<box>` copy when the variable is set, exactly as `box=<box>/open_calls.json` stands for the cluster copy; production reads (variable unset) are unchanged. Update the module header comment that names the variables.
2. Update `.tools/tests/test_open_calls_cloudread.py` to use only that one variable, and ADD exactly one case: a foreign box whose `git=` copy is newer than its stale `box=` cluster copy and its stale working-tree copy reads the git rows. The test keeps its 7 existing cases (their last line goes from `cases=7/7` to `cases=8/8`).
3. Exit checks on fixture writes (row W2-S11). In `.tools/portal-merge-forward.sh`, every command that builds a self-test fixture (a file write, `git init`, `git commit`, `git branch`, `git push`, `git clone`, `git merge` used to BUILD a fixture, not the call under test) goes through one helper `fx` that runs its arguments and, on a non-zero exit, prints `SELFTEST ERROR: fixture step failed: <the command>` and exits the self-test non-zero BEFORE any case is graded. A fixture step that is EXPECTED to fail (a deliberate conflict, a deliberately rejected push) stays a plain command, with a comment saying so. All 29 cases stay and still pass; the selftest's last line stays `ok=True`.

### RULES FOR THIS CELL

Nothing you run pushes, or changes the real portal's DEV, PROD or main tree: tests use `mktemp -d` repositories and a temporary state root (`OPAL_STATE_ROOT`). No S3 call in any test. Git Bash default utilities only; quote every expansion. No non-ASCII in anything you add. Ruff clean on the Python files you touch. The existing five open-calls suites stay green (run them). Do not put `MSYS_NO_PATHCONV=1` on a command that takes an absolute path.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W2-S<k>`, next unused k after the highest `W2-S` in the file, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPf2-AC1" cell_refs="DP-f-2"><invocation>python .tools/tests/test_open_calls_cloudread.py</invocation><expect>cases=8/8 ok=True</expect></criterion>
`DPf2-AC1` -- the cloud-read test with its one variable and its one new case (it reads 7/7 at the base).

<criterion id="DPf2-AC2" cell_refs="DP-f-2"><invocation>grep -c "OPAL_GIT_READ_ROOT" .tools/open-calls.py</invocation><expect>^0$</expect></criterion>
`DPf2-AC2` -- the second variable is gone from the tool (it counts 1 or more at the base).

<criterion id="DPf2-AC3" cell_refs="DP-f-2"><invocation>grep -c "SELFTEST ERROR: fixture step failed" .tools/portal-merge-forward.sh</invocation><expect>^[1-9]</expect></criterion>
`DPf2-AC3` -- the fixture helper exists and prints its error line (it counts 0 at the base).

<criterion id="DPf2-AC4" cell_refs="DP-f-2"><invocation>bash .tools/portal-merge-forward.sh --selftest</invocation><expect>ok=True</expect></criterion>
`DPf2-AC4` -- a fourth criterion, with its reason: this order edits a script whose 29 self-test cases must all stay green through the `fx` helper.
</proof_of_spec>

<expected_criteria>DPf2-AC1,DPf2-AC2,DPf2-AC3,DPf2-AC4</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~2/NFRA_DEVPLN.TO-DP-f-2.repair-batch.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPf2-AC1,DPf2-AC2,DPf2-AC3,DPf2-AC4`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round5.md</decomp_doc>
<owned_cells>DP-f-2</owned_cells>
</decomp_ref>

<paths>
.tools/open-calls.py
.tools/tests/test_open_calls_cloudread.py
.tools/portal-merge-forward.sh
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-f-2.repair-batch.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE the cell touches no IAM.
comp-adversary: RUN over the cell's own invocations; BLIND to the filesystem around the cited paths. Findings inlined: collapsing two test seams into one must leave the production read path byte-for-byte unchanged (variable unset); the `fx` helper must not swallow an EXPECTED failure.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `ledger/ROUND_ANALYSIS.round4.md` @e8db882826 section 3 item 3 (rows W1-S14 and W2-S11; W1-S13 is read and recorded only, no cell). Portal worktree: this order needs `--portal-ref` at the spawn.
