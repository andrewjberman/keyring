# AMGT_RESAPP task order -- `AMGT-oo-3` -- THE MASS-DELETION GATE EXEMPTS A MERGE IN A LINKED WORKTREE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-oo-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~361</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-oo-3.the-mass-deletion-gate-exempts-a-merge-in-a-linked-worktree</to_id>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one shell script, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no cloud call.
comp-adversary: RUN at the cut -- measured in a throwaway repository: a merge with staged deletions in a LINKED worktree is gated (hook exit 1, a BLOCKED row) while the same merge in the main worktree is exempt (exit 0); r90_merge_head.sh FAILs B1 at the base and PASSes B2 and B3, and PASSes all three against a candidate one-line change in a temporary copy.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** the spawn names it (branch `wk-AMGT_RESAPP-361`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd` into that path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-oo-3` (round 90, decomposition s.98)

CTO~DELL1 round-89 analysis item 4. `.tools/git-hooks/mass-deletion-check.sh` exempts a merge commit's deletions (they come from the
merged branch, not from the committer) with this test, at about line 130:

    if [ -f "$ROOT/.git/MERGE_HEAD" ] || [ -f "$ROOT/.git/CHERRY_PICK_HEAD" ]; then
      exit 0
    fi

In a LINKED worktree `$ROOT/.git` is a FILE, and the merge state lives in that worktree's own git directory
(`<common>/worktrees/<name>/MERGE_HEAD`), so the test never fires there: a legitimate merge that brings a deletion is gated like a
hand-made mass deletion. Resolve the two paths with git's own resolver and test those:

- `git rev-parse --git-path MERGE_HEAD` and `git rev-parse --git-path CHERRY_PICK_HEAD` (each prints the path for the worktree it runs
  in; a failed resolution must not exempt anything: an empty or failing resolution tests false);
- the exemption's effect (`exit 0`), its position in the script and its comment's meaning stay as they are; extend the comment by one
  line naming the linked-worktree case;
- change NOTHING else: the audit root block above it (`AUDIT_ROOT`), the deletion count, the attribution test, the mode logic, the exit
  codes and the printed text stay exactly as they are.

ASCII only, Git Bash default utilities only (the file's own header rule). Stamp any surprise row's `surfaced_at` with `date -u
+%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W361-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install` of any kind. Nothing is fetched from the internet.
3. Standing: no S3 delete, no push of shared branches.
4. You edit the one script named. Do not touch `.tools/safe-commit.sh` or any other hook.

## 3. SURFACES

<paths>
.tools/git-hooks/mass-deletion-check.sh
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~361/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-oo-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round90_prep/checks/r90_merge_head.sh" --hook "$(pwd)/.tools/git-hooks/mass-deletion-check.sh"; echo "exit=$?"</invocation><expect>PASS B1 (a merge in a linked worktree that brings deletions is exempt: exit 0, no BLOCKED row), PASS B2 (control: a non-merge mass deletion in the linked worktree is still BLOCKED, exit 1 and a new row), PASS B3 (control: a merge in the main worktree stays exempt); R90 MERGE HEAD: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-oo-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash -n .tools/git-hooks/mass-deletion-check.sh &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round89_prep/checks/r89_audit_root.sh" --hook "$(pwd)/.tools/git-hooks/mass-deletion-check.sh"; echo "exit=$?"</invocation><expect>the script parses (bash -n rc 0) and the round-89 audit-root check still reads R89 AUDIT ROOT: YES (A1-A4 PASS), so the audit path this edit sits beside is unchanged; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~361 <0.9.0_WK_AMGT_RESAPP~361@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~361/AMGT_RESAPP.TO-AMGT-oo-3.the-mass-deletion-gate-exempts-a-merge-in-a-linked-worktree.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the diff of the script, in full (it is a few lines);
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-89 analysis @34a0c14300 item 4 (named in nn-4's record face, packet section 5 item 4). DIRECT-ACT: one cell, about three lines, LOCAL; it runs no L2 and no L8-L10 and its close is the issuer's one real run (a merge that brings a deletion, committed from a linked worktree after this lands). It lands through this issuance, never as a rider on a product cell. Checks dry-run at the base: AC1 FAIL (B1; B2 and B3 PASS); AC2 PASS (a bound). CHERRY_PICK_HEAD sits in the same expression and has the same defect; it is one change, not a second cell. Worker slot `~361` continues the `~35x` numbering of round 89.

<status>pending</status>
<round>90</round>
<slot>0.9.0_WK_AMGT_RESAPP~361</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete -- issuer close 2026-10-11T05:5xZ (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-361 @fc55fbc4a9 merged @69d5fea1a9, proof instance VALID (worker run and issuer re-run); issuer re-run in the worktree: AC1 R90 MERGE HEAD YES (B1-B3 PASS; base NO 2 of 3), AC2 bash -n rc 0 and R89 AUDIT ROOT YES (A1-A4). Rows: none. CHERRY_PICK_HEAD moved with MERGE_HEAD in the same expression.</status>
