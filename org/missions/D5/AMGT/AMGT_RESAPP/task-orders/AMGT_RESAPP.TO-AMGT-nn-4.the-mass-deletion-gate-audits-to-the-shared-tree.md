# AMGT_RESAPP task order -- `AMGT-nn-4` -- THE MASS-DELETION GATE'S AUDIT ROW LANDS IN THE SHARED TREE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-nn-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~352</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one shell script, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no cloud call.
comp-adversary: RUN at the cut -- measured in a throwaway repository: a verdict the gate writes from a LINKED worktree is gone after `git worktree remove` (main-tree rows 0); from the main worktree it lands; r89_audit_root.sh FAILs A1 and A2 at the base and PASSes A3.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-352`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-nn-4` (round 89, decomposition s.97)

CTO~DELL1 round-88 analysis item 5 (row AMGT_RESAPP-S4). `.tools/git-hooks/mass-deletion-check.sh` sets `ROOT="$(git rev-parse
--show-toplevel ...)"` (about line 111) and `_audit()` (about lines 160-165) appends its verdict row to `"$ROOT/$AUDIT_LOG"`
(`AUDIT_LOG="org/mass-deletion-audit.log"`). A row written from a linked worktree dies when that worktree is removed.
`.tools/safe-commit.sh` (read lines 160-190) already resolves its audit root through `git rev-parse --git-common-dir`; adopt that
resolution for the AUDIT PATH ONLY:

- add one variable, `AUDIT_ROOT`, resolved from `git rev-parse --path-format=absolute --git-common-dir` (the common dir's parent);
  when the resolution fails, or the parent is not a directory, or the parent holds NO `.git` entry (a SUBMODULE's common dir is
  `<super>/.git/modules/<name>`, whose parent is not a worktree), `AUDIT_ROOT` falls back to `ROOT`;
- `_audit()` writes to `"$AUDIT_ROOT/$AUDIT_LOG"` (its `mkdir -p` follows);
- change NOTHING else: the deletion count, the attribution test (`$ROOT/$TRAILER`), the mode logic, the exit codes, the printed
  text and every other use of `ROOT` stay exactly as they are.

ASCII only, Git Bash default utilities only (the file's own header rule). Stamp any surprise row's `surfaced_at` with `date -u
+%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W352-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit the one script named. Do not touch `.tools/safe-commit.sh` or any other hook.

## 3. SURFACES

<paths>
.tools/git-hooks/mass-deletion-check.sh
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~352/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-nn-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_audit_root.sh" --hook "$(pwd)/.tools/git-hooks/mass-deletion-check.sh"; echo "exit=$?"</invocation><expect>PASS A1 (a warn-mode verdict from a linked worktree leaves its row in the shared tree after the worktree is removed), PASS A2 (block mode: exit 1 and a BLOCKED row in the shared tree), PASS A3 (a deletion from the main worktree leaves its row in the main tree), PASS A4 (a submodule commit's row lands in a worktree, never under <super>/.git/modules); R89 AUDIT ROOT: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-nn-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash -n .tools/git-hooks/mass-deletion-check.sh &amp;&amp; bash .tools/git-hooks/mass-deletion-check.sh --mode; echo "exit=$?"</invocation><expect>the script parses (bash -n rc 0), `--mode` prints the gate's ramp state and threshold 25, and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~352 <0.9.0_WK_AMGT_RESAPP~352@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~352/AMGT_RESAPP.TO-AMGT-nn-4.the-mass-deletion-gate-audits-to-the-shared-tree.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the diff of the script, in full (it is a few lines);
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-88 analysis @6ad172c28d item 5 (AMGT_RESAPP-S4, REMEDIATION_v33). DIRECT-ACT: one cell, about ten lines, LOCAL; it runs no L2 and no L8-L10 and its close is the issuer's one real run (a gated deletion from a linked worktree after this lands). It lands through this issuance, never as a rider on a product cell (analysis section 2). A pre-existing neighbour is NOT in scope: `$ROOT/.git/MERGE_HEAD` (about line 107) tests a path that is a FILE in a linked worktree, so the merge-commit exemption never fires there. That is a separate defect; the worker files it as a row if its read confirms it, and does not fix it. Checks dry-run at the base: AC1 FAIL (A1, A2); AC2 PASS (a bound).

<status>pending</status>
<round>89</round>
<slot>0.9.0_WK_AMGT_RESAPP~352</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>pending -- AMENDMENT 1 (issuer, 2026-10-11T03:5xZ) on row AMGT_RESAPP-D1-W352-S1 (the worker's finding, measured by the issuer in a throwaway superproject): the first fix @46b12bd496 passes A1-A3 and writes a SUBMODULE commit's row under <super>/.git/modules. AUDIT_ROOT falls back to ROOT when the common dir's parent holds no .git entry; criterion AC1's expect gains A4 (the checker r89_audit_root.sh gained the arm; base PASS, @46b12bd496 FAIL). The portal's hooks dir carries no active commit-msg on dell1, so the arm is unreachable here today; the guard is for a box where it is installed. Graded by to-pipeline-gate on a modification.</status>
<status>complete -- issuer close 2026-10-11T04:2xZ (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-352 @63d9dc87b6 (fix a51ccfeed8 under AMENDMENT 1), proof instance VALID (worker run); issuer re-run in the worktree: AC1 R89 AUDIT ROOT YES (A1-A4 PASS), AC2 bash -n rc 0 and --mode threshold 25. Row D1-W352-S1 ruled: closed by the AUDIT_ROOT .git-entry guard.</status>
