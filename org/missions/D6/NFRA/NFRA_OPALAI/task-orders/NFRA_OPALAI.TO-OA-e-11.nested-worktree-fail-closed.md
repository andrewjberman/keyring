# NFRA_OPALAI task order -- `OA-e-11` -- ROUND 2, E11: a nested linked worktree outside the parent fails CLOSED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-e-11</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~17</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- the three fixture arms are the adversary read of the one gate this changes.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-e-11` (round 2, decomposition section R2.1; row NFRA_OPALAI-Z-S17, ruling R-2)

The workspace grades every commit by lane: `.tools/git-hooks/owned-paths-check.sh` resolves the staged paths against
the parent repo's `.owned-paths.yaml`. For a commit made INSIDE the nested repo `opal_ai` (a git submodule), it first
finds the superproject so it can grade against the parent's lane file. `install-owned-paths.sh --submodule opal_ai`
installs a small wrapper (the `WRAPPER=` text, `:78-95`) into the submodule's shared hooks dir
(`.git/modules/opal_ai/hooks/pre-commit`); every linked worktree of the submodule runs that one wrapper.

**The defect, measured on a scratch fixture at the cut.** Both the wrapper and the hook find the superproject by
taking the FIRST entry of `git worktree list --porcelain` when `--show-superproject-working-tree` is empty
(`owned-paths-check.sh:51-62`, the wrapper's `_MAIN_WT` lines). For a submodule, that first entry is its GITDIR
(`<super>/.git/modules/opal_ai`), which has no superproject. So in a linked worktree of `opal_ai` placed OUTSIDE every
parent worktree:
- the wrapper finds no superproject;
- it looks for `.tools/git-hooks/owned-paths-check.sh` under the nested toplevel, where it does not exist;
- it prints `WARN ... skipping lane check` and exits 0.
An out-of-lane commit LANDS. The same commit in the main nested checkout is refused, because there
`--show-superproject-working-tree` answers directly.

**The remedy (R-2):**
- resolve the superproject from the COMMITTING worktree's own situation, never from the first `git worktree list`
  entry;
- when NO superproject resolves for a commit in a repo that is a submodule (its common gitdir sits under some
  `.git/modules/`), REFUSE loud: a non-zero exit and a message naming the reason. Never skip the lane check;
- apply the same resolution in BOTH places: the hook, and the wrapper text in `install-owned-paths.sh` (the wrapper is
  what a nested worktree actually runs).

The parent repository's own verdicts must not move: an in-lane parent commit still lands, and an out-of-lane one is
still refused. A commit in the main nested checkout is still graded against the parent lane file (in-lane lands,
out-of-lane refused).

Add a regression test, `.tools/tests/test_nested_worktree_failclosed.sh`. It builds its own scratch superproject and
submodule under `mktemp -d` (local file protocol, `-c protocol.file.allow=always`, no network), installs the hook, and
runs the three arms below. It prints one line per arm and ends with a summary line `RESULT: N passed, M failed`, exiting
0 only when M is 0. It must never write the real `org/git-author-override-audit.log`: set `OWNED_PATHS_AUDIT_LOG` to a
scratch file.

## 2. BOUNDS

1. Change only the superproject RESOLUTION and the fail-closed branch. The lane logic, the merge exemption, the override
   hatch and the validator are unchanged. Do not touch `.tools/owned-paths-validate.py` or `.owned-paths.yaml`.
2. Do not install anything into the REAL `opal_ai` hooks dir or the real `.git/hooks`. The issuer installs at the drain.
3. Standing: no push, no install, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal
   with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
.tools/git-hooks/owned-paths-check.sh
.tools/git-hooks/install-owned-paths.sh
.tools/tests/test_nested_worktree_failclosed.sh
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~17/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read (never write): `.tools/owned-paths-validate.py`, `.owned-paths.yaml`.
Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_OPALAI-Z-W17-S<k>` (next free k for W17).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the commit)

The checks build their OWN scratch fixture from the COMMITTED bytes at your HEAD (`git show HEAD:<path>` for the lane
file, the validator and both hook scripts). In the fixture, `opal_ai/**` is lane `ANY_EXEC_OR_AE`:
`0.4.0_DS_ClientPlatform` is out of it and `1.0.0_SA_CTO` is in it.

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-e-11"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e11.AC1.sh; echo "exit=$?"</invocation><expect>arm1 outside-worktree out-of-lane: refused; arm2 main-nested out-of-lane: refused; arm3 main-nested in-lane: landed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-e-11"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e11.AC2.sh; echo "exit=$?"</invocation><expect>test at HEAD=present; rc=0; failing lines=0; summary names 0 failed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-e-11"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e11.AC3.sh; echo "exit=$?"</invocation><expect>parent out-of-lane: refused; parent in-lane: landed -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~17/NFRA_OPALAI.TO-OA-e-11.nested-worktree-fail-closed.proof_of_spec.json`.
Report once: the resolution you used and why it cannot land on the gitdir, the refusal message text, the commit hash,
and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** R-2 (row Z-S17; the hook is fabric gate code whose owner is `1.0.0_SA_CTO~O`, cut as a worker cell
under this order's `<paths>` per the analysis). Chain I, alone.

**AT THE DRAIN (issuer):** a hook fix applies to a worktree's BASE, not to live worktrees. After the merge, re-run
`bash .tools/git-hooks/install-owned-paths.sh --submodule opal_ai` in the main tree ONLY if the installed wrapper text
must change: the installer is a no-op when a wrapper already names `owned-paths-check.sh`, so a changed wrapper needs
the old one replaced deliberately. That is the issuer's act, recorded in the drain commit. Row Z-S17 closes at the
round-2 L8 on AC1's arm 1.

SPAWN ONLY WHEN: at the cut (no precondition). Slot `~17`, no nested worktree needed.

Dry-run at base (main tree, CLOUD `c8df03c408`; the fixture builds from HEAD's committed hook bytes):
- e11.AC1 base: FAIL as expected (`arm1 outside-worktree out-of-lane: landed; arm2 main-nested out-of-lane: refused
  rc=1; arm3 main-nested in-lane: landed` -- the fail-open reproduced on arm 1 only; arms 2 and 3 are the controls).
- e11.AC2 base: FAIL as expected (`test at HEAD=absent`).
- e11.AC3 base: PASS as expected (bound: `parent out-of-lane: refused rc=1; parent in-lane: landed`).

<status>pending</status>
<round>2</round>
<slot>~17</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
