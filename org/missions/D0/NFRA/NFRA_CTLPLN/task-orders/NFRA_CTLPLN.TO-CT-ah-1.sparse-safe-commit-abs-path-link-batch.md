# TO NFRA_CTLPLN.TO-CT-ah-1 -- workstream BATCH round 5 (cell CT-ah-1): safe-commit green inside a wk-provision.sh worktree; worktree_gc resolves the path before its in-use match; the preserve step keeps a link as a link (CTO round-17 rulings 1-3; rows W103-S1, S9126, W103-S2)

<to_id>NFRA_CTLPLN.TO-CT-ah-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~105</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>BATCH</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ah-1` (`decompositions/NFRA_CTLPLN_DECOMP.round18.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Three small items from round 17, in ONE cell. Read rows `NFRA_CTLPLN-W103-S1`, `NFRA_CTLPLN-W103-S2` and `NFRA_CTLPLN-S9126` first (Grep each id in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`). YOUR WORKTREE WAS CUT BY THE NEW `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT (the first real use of that recipe): it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. Because it is the first real use, item 1 below is also your own situation: if a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

1. **The sparse base set under `safe-commit.sh` (CTO ruling 1).** `.tools/wk-provision.sh provision` cuts a sparse checkout whose base set must always hold what `.tools/safe-commit.sh` needs: `.tools/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`. Round 17 added them (read `cmd_provision`). Prove it: a test that cuts a REAL sparse worktree of this repository with `.tools/wk-provision.sh provision` (under a temporary folder, NOT under `C:/Users/AndrewBerman/Desktop/ajb_wk/`), makes ONE throwaway commit there of a new `.txt` file under the project folder's `deliverables/` through `.tools/safe-commit.sh --author "0.9.0_WK_NFRA_CTLPLN~105 <0.9.0_WK_NFRA_CTLPLN~105@opal.agent>" -F <msgfile> -- <path>` (message file written by Python; the commit lands on the throwaway branch only), requires `safe-commit.sh` to exit 0 and the branch tip to move, then removes the worktree and its branch in a `finally`. A `.txt` file is not one of the graded extensions, so the naming gate's live limb does not run; check the gate's printed input to be sure, and if any AWS call would happen, STOP and file a BLOCKING row. If `safe-commit.sh` fails for a missing folder, add that folder to the base set in `wk-provision.sh` (it is in your `<paths>`) and say so.
2. **`S9126`.** In `.tools/worktree_gc.py`, `--only <path>` and `--check-removable <path>` must resolve the path (absolute, relative, with or without a trailing slash, either slash direction) to one canonical form BEFORE the in-use match, and the in-use scan must leave out the tool's own process and its parent shell's command line. A worktree not named by any OTHER process must no longer read `SKIP IN USE` because the tool was started with its absolute path. A worktree genuinely named by another process still reads `SKIP IN USE`.
3. **`W103-S2` (CTO ruling 3).** In the preserve step (`preserve_dirt`), a directory junction or symlink in a worktree is preserved AS THE LINK, never followed: the link is recorded in the temporary index as a link entry (`git hash-object -w --stdin` of the target path, then `git update-index --add --cacheinfo 120000,<sha>,<path>`) and its target's files are not added. State this in a code comment. A directory junction can be created on this box without privilege (`cmd /c mklink /J`), so TEST IT FOR REAL. A symlink cannot be created here (WinError 1314): the symlink arm is SKIPPED with that reason printed and counted as skipped, not failed.

### BUILD

4. A NEW test `.tools/tests/test_round18_batch.py` (standard library; temporary repositories for the arms; no AWS, no network). Arms: (a) `--check-removable` and `--go --only` given an ABSOLUTE path, a relative path and a trailing-slash path to the same clean merged tree read the same verdict and none reads `SKIP IN USE` (reuse the fixtures of `.tools/tests/test_worktree_gc_preserve.py`); (b) a worktree whose path is named in a running process's command line (start a harmless `python -c "import time; time.sleep(60)" <path>` and kill it in a `finally`) still reads `SKIP IN USE`; (c) a dirty merged tree holding a directory junction to a folder outside the worktree: after `--go --only` the preserve commit holds the junction as a mode-120000 entry (`git ls-tree` shows `120000`), does NOT hold the target's files, and the target folder's files still exist after the removal; (d) the symlink arm SKIPPED with the reason `WinError 1314` where creation fails (and run for real where it succeeds); (e) the sparse-provision arm of item 1 behind the flag `--real` (it needs C: above 12 GB free: check `df -h /c` and skip it with a printed reason if not). Final lines: `ROUND18-BATCH arms=<k>/<n> skipped=<s> ok=<True|False>` (default run, arm e not run) and, with `--real`, `SAFE-COMMIT-SPARSE exit=<rc> tip_moved=<True|False> folders=<n> green=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. Every worktree_gc experiment runs in a temporary repository; never run `worktree_gc.py --go` without `--only`, and never against a real worktree of another seat. The one real worktree this cell creates (arm e) is removed in a `finally` with its branch. No aws, no network, no push. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~104/NFRA_CTLPLN.TO-CT-ag-2.sparse-worker-checkout-by-default.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W105-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTah1-AC1" cell_refs="CT-ah-1"><invocation>python .tools/tests/test_round18_batch.py</invocation><expect>ok=True</expect></criterion>
`CTah1-AC1` -- every non-skipped arm passes: the absolute-path verdict, the in-use control, the junction kept as a link (base: the file does not exist); report the whole last line with its denominator and the skipped count.

<criterion id="CTah1-AC2" cell_refs="CT-ah-1"><invocation>python .tools/tests/test_round18_batch.py --real</invocation><expect>green=True</expect></criterion>
`CTah1-AC2` -- `safe-commit.sh` runs green inside a real worktree cut by `wk-provision.sh` (base: the file does not exist); report the whole `SAFE-COMMIT-SPARSE` line and any folder you had to add to the base set.

<criterion id="CTah1-AC3" cell_refs="CT-ah-1"><invocation>python .tools/tests/test_worktree_gc_preserve.py</invocation><expect>ok=True</expect></criterion>
`CTah1-AC3` -- the round-17 preserve suite still passes after items 2 and 3 (base: `WORKTREE-GC-PRESERVE arms=9/9 ok=True`, a control; the count may grow); report the whole last line.
</proof_of_spec>

<expected_criteria>CTah1-AC1,CTah1-AC2,CTah1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTah1-AC1,CTah1-AC2,CTah1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round18.md</decomp_doc>
<owned_cells>CT-ah-1</owned_cells>
</decomp_ref>

<paths>
.tools/worktree_gc.py
.tools/wk-provision.sh
.tools/tests/test_round18_batch.py
.tools/tests/test_worktree_gc_preserve.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the throwaway commit is a `.txt` file so the naming gate's live limb does not run.
comp-adversary: RUN -- a real worktree of another seat touched by a worktree_gc experiment (temporary repositories only; `--only` always); the in-use scan blinded so a genuinely used worktree is removed (arm b); the preserve step following a junction into a large folder or deleting its target on removal (arm c checks the target survives); a throwaway commit merged or pushed (it stays on a branch the `finally` deletes); the `--real` arm leaving a worktree behind or filling the disk (C: check first, the `finally`); BLIND: `safe-commit.sh` reaching a folder outside the sparse set only on a commit path the throwaway `.txt` commit does not take (a `.py`, a `.tf`, a task order), which this arm does not exercise; the worker reports which commit kinds it did not try.
risk: LOCAL -- temporary repositories and one real sparse worktree under a temporary folder, removed.
lane: the <paths> block IS the grant (worker RULING 1). `.tools/worktree_gc.py` is `0.0.0_AB_MSTR`'s tool and `.tools/wk-provision.sh` is on the issuer's cutting path; the CTO ordered each change (round-17 analysis rulings 1-3).
</preflight>

Base checks, dry-run by the issuer before the cut: CTah1-AC1 and CTah1-AC2 base: FAIL as expected (the test file does not exist); CTah1-AC3 base: `WORKTREE-GC-PRESERVE arms=9/9 ok=True` (a control).
Source: CTO round-17 analysis rulings 1-3 and section 3 item 1 (`ledger/ROUND_ANALYSIS.round17.md` @8b52525b29); msg 109386; rows W103-S1, W103-S2, S9126.
