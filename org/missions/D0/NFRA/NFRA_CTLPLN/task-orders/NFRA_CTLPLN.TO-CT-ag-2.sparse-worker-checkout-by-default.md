# TO NFRA_CTLPLN.TO-CT-ag-2 -- workstream PROVISION round 1 (cell CT-ag-2): a worker worktree is a SPARSE checkout by default; a full one needs a stated reason (CTO round-16 ruling 3, msg 109364)

<to_id>NFRA_CTLPLN.TO-CT-ag-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~104</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run on branch wk-NFRA_CTLPLN-104 @e04d14f563 (merged 4f05cf168c): WK-SPARSE-PROVISION arms=7/7 ok=True, wk-provision.sh --self-test RESULT: 0 arm(s) failed of 8, and SPARSE-REAL tracked_bytes_sparse=68134267 tracked_bytes_full=3636649180 ratio=0.02 du_sparse=105M green=True (a real sparse worktree of this repository ran the CT-af-2 cell's test, ROUND-CLOSE-DECOMP-ROUND arms=6/6, green); proof instance VALID; the diff touches only the order's paths. Reading: wk-provision.sh provision is a SPARSE cone checkout by default (base folders: .tools, lib, the project folder, org/modules/graph, org/devices, infra/logic/registry, org/standards, plus the --order paths); --full requires a reason; the portal step is unchanged (du_sparse includes the nested portal worktree, a full 2163-file checkout). The worker did not run safe-commit.sh inside a sparse worktree of its own (its worktree was full by the order); the ruled folder set comes from worker ~103, whose safe-commit ran in a hand-cut sparse worktree. BLOCKING row W104-S2 ruled by the issuer: the dispatch SKILL.md edit was refused by the file's byte-budget gate (33778 against 25600; HEAD 33198 is already over), so the worker restored the file; the issuer rewrote the recipe paragraph (old lines 218-227) shorter, net -48 bytes, commit 43f9022522, nothing else in the file changed. Row W104-S1 (the order's fixture layout D0/X/Y/CODE cannot satisfy the project-folder rule D*/*/CODE; the fixture uses D0/NFRA/PROJX) accepted.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>PROVISION</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ag-2` (`decompositions/NFRA_CTLPLN_DECOMP.round17.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

A full worker worktree of this repository costs 3.6 to 3.7 GB (about 84,000 tracked files); the laptop fell to 6 GB free twice in one morning. The CTO's ruling (`ledger/ROUND_ANALYSIS.round16.md` ruling 3, and msg 109364): a worker worktree is cut as a SPARSE checkout of the order's `<paths>` plus `.tools/` and `lib/`, with a full checkout only when stated with a reason. The cut is `.tools/wk-provision.sh provision <CODE> <n> --path <abs-path>` (read the file: usage at :25-44, `cmd_provision` at about :268-327, and the worktree-add line at about :312, `git worktree add -b "$branch" "$path" HEAD`). `.claude/skills/dispatch/SKILL.md` lines 216-227 describe that recipe to the issuer. The project's own tree folder holds the order, the decomposition, the surprise channel and the deliverables; a worker needs it to read its order and to write its proof instance.

### BUILD

1. In `cmd_provision`, replace the full checkout with a sparse one: `git worktree add --no-checkout -b "$branch" "$path" HEAD`, then in that worktree `git sparse-checkout init --cone` and `git sparse-checkout set <folders>`, then check out HEAD. The folders are: `.tools`, `lib`, the project's tree folder (found as the one directory `org/missions/D*/*/<CODE>` that exists at HEAD), and, with the new option `--order <task order file>`, every directory the order's `<paths>` block names (a file path contributes its parent folder; a folder path contributes itself; skip a path that does not exist at HEAD and print it). Cone mode also checks out the files at the repository root.
2. New options: `--order <file>` (repeatable), `--sparse-add <folder>` (repeatable; extra folders), and `--full "<reason>"` (a full checkout, the reason is required and is recorded: print it and write it to the audit line below). `--full` with an empty reason is refused (exit 2, before anything is created). With neither `--order` nor `--full`, the base set (`.tools`, `lib`, the project folder) still applies.
3. Print the result in one line: `PROVISIONED <path> branch=<branch> mode=sparse folders=<n> files=<n> bytes=<n>` (or `mode=full reason=<...>`), where files and bytes are the checked-out tracked files (count and byte total read from `git ls-files` and file sizes, not from the disk's cluster size). The portal and nested-worktree steps that follow are unchanged and still run.
4. Do not change `portal`, `remove`, `--self-test` arms 1-8 or the node_modules handling. Existing callers keep working: their worktree is now sparse, which is the intent.
5. Edit `.claude/skills/dispatch/SKILL.md` lines 216-227 ONLY: say the worktree is sparse by default, show the `--order` form, say a full checkout needs `--full "<reason>"`, and keep the `HEAD` derivation warning and the portal sentences. Change nothing else in that file.
6. A NEW test `.tools/tests/test_wk_sparse_provision.py` (standard library, `subprocess`; temporary repositories for the arms; no AWS, no network). Arms, on a temporary repository that mimics the layout (`.tools/`, `lib/`, `org/missions/D0/X/Y/CODE/task-orders/`, `infra/`, `docs/`, and a root file): (a) default provision leaves `.tools`, `lib` and the project folder checked out and `infra/` and `docs/` NOT present; (b) with `--order` naming a path under `infra/aws/x/`, that folder is present and `docs/` is not; (c) `--full "reason"` checks out everything and prints `mode=full reason=reason`; (d) `--full ""` is refused with exit 2 and creates nothing; (e) an `--order` path that does not exist at HEAD is printed as skipped and does not fail; (f) a commit made in the sparse worktree with plain `git commit` of a file under the project folder lands and the branch tip moves; (g) `remove <path>` still removes a sparse worktree and its branch state. The test also takes a flag `--real`: it provisions a REAL sparse worktree of THIS repository for the already-merged order `org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/NFRA_CTLPLN.TO-CT-af-2.round-close-check-decomp-round-scope.md` (`--order` that file), runs that cell's test `python .tools/tests/test_round_close_decomp_round.py` inside it and requires its last line to read `ok=True`, then prints `SPARSE-REAL tracked_bytes_sparse=<n> tracked_bytes_full=<n> ratio=<x.xx> du_sparse=<human> green=<True|False>` (tracked_bytes_full from `git ls-tree -r -l HEAD`; `du_sparse` from `du -sh` of the worktree), and removes the worktree and its branch in a `finally`. If the cell's test fails in the sparse worktree because a file or folder is missing, add that folder to the BASE set (and say so in your report): the base set is what the next worker needs. Final lines `WK-SPARSE-PROVISION arms=<k>/<n> ok=<True|False>` (default run) and the `SPARSE-REAL` line (with `--real`).

### RULES FOR THIS CELL

Write surface = the `<paths>`. The only real worktree this cell creates is the one `--real` makes under a temporary folder (not under `C:/Users/AndrewBerman/Desktop/ajb_wk/`), and it removes it. Disk: C: must stay above 12 GB free; check `df -h /c` before `--real` and skip it with a printed reason if below. No aws, no network, no push. `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only, no associative arrays). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~102/NFRA_CTLPLN.TO-CT-af-3.placement-refusal-unstages-all.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W104-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTag2-AC1" cell_refs="CT-ag-2"><invocation>python .tools/tests/test_wk_sparse_provision.py</invocation><expect>ok=True</expect></criterion>
`CTag2-AC1` -- every arm passes (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTag2-AC2" cell_refs="CT-ag-2"><invocation>bash .tools/wk-provision.sh --self-test</invocation><expect>RESULT: 0 arm\(s\) failed</expect></criterion>
`CTag2-AC2` -- the provisioner's own self-test still passes (base: `RESULT: 0 arm(s) failed of 8`, a control, about 30 seconds); report the whole last line.

<criterion id="CTag2-AC3" cell_refs="CT-ag-2"><invocation>python .tools/tests/test_wk_sparse_provision.py --real</invocation><expect>green=True</expect></criterion>
`CTag2-AC3` -- a real sparse worktree of this repository runs the `CT-af-2` cell's test green; report the whole `SPARSE-REAL` line (sizes against a full checkout) and the folders in the base set.
</proof_of_spec>

<expected_criteria>CTag2-AC1,CTag2-AC2,CTag2-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~104/NFRA_CTLPLN.TO-CT-ag-2.sparse-worker-checkout-by-default.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTag2-AC1,CTag2-AC2,CTag2-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round17.md</decomp_doc>
<owned_cells>CT-ag-2</owned_cells>
</decomp_ref>

<paths>
.tools/wk-provision.sh
.tools/tests/test_wk_sparse_provision.py
.claude/skills/dispatch/SKILL.md
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a sparse worktree missing a file the worker's gates need, so a commit or a criterion fails there (the `--real` arm runs a real cell's test and the worker adds to the base set); a `--full` without a reason (arm d); a portal cell broken by the sparse default (self-test arms 1-8 stay green, AC2); the skill edit touching more than the recipe paragraph (the issuer reads the diff); a leftover real worktree or branch after `--real` (the `finally`); BLIND: the commit gates (`safe-commit.sh`, the surprise-row gate, the to-pipeline gate) reading files outside the sparse set (the arm commits with plain `git commit` only; the worker reports whether `safe-commit.sh` runs in a sparse worktree of this repository, by one real `.tools/safe-commit.sh` run on a trivial file under the project folder in the `--real` worktree before removing it, and which folders it asked for).
risk: LOCAL -- temporary repositories and one real worktree created under a temporary folder and removed; `.claude/skills/dispatch/SKILL.md` is a recipe paragraph.
lane: the <paths> block IS the grant (worker RULING 1). `.tools/wk-provision.sh` is on the issuer's cutting path; the CTO ordered the change (msg 109364, round-16 ruling 3).
</preflight>

Base checks, dry-run by the issuer before the cut: CTag2-AC1 and CTag2-AC3 base: FAIL as expected (the test file does not exist); CTag2-AC2 base: `RESULT: 0 arm(s) failed of 8` (a control).
Source: CTO round-16 analysis ruling 3 and section 3 item 2 (`ledger/ROUND_ANALYSIS.round16.md` @f62974941f); msgs 109364 and 109362 (disk).
