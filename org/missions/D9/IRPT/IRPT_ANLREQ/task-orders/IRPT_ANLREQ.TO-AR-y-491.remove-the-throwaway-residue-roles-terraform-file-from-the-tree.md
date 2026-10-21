# TO IRPT_ANLREQ.TO-AR-y-491.remove-the-throwaway-residue-roles-terraform-file-from-the-tree -- DELETE ONE FILE and prove it: remove `infra/aws/terraform/investor-reporting/ycharts/irpt_residue_delete_r35.tf` from the tree (the throwaway delete roles it declared were destroyed by IB2 at 08:10Z; left in the tree it makes every whole-root plan show six pending adds)

<to_id>IRPT_ANLREQ.TO-AR-y-491.remove-the-throwaway-residue-roles-terraform-file-from-the-tree</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~364</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ150</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-491` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** the clean close of round 43 | **depends_on:** the residue delete pass (cell AR-y-490, IB2 msg 11943: 29 of 29 versions deleted, the six roles and policies destroyed), CTO msg 11937 ("the close commit removes irpt_residue_delete_r35.tf, and a whole-root plan then reads No changes")

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~364`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-364` (branch `wk-IRPT_ANLREQ-364`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~364 <0.9.0_WK_IRPT_ANLREQ~364@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W364-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** Terraform is not installed: do not try to run it. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first; `controls` holds `mutant` and `determinism` only), with `to_id` exactly the order's id; run `python .tools/proof-of-spec-check.py <instance> "AR491-y-AC1,AR491-y-AC2"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID and only after every other edit you intend is committed. The instance's check-script reference is pinned to a commit that EXISTS (commit the script first, then pin it).

### THE CELL (`AR-y-491`, inlined)

*The change (the only edit).* `git rm infra/aws/terraform/investor-reporting/ycharts/irpt_residue_delete_r35.tf` and commit that deletion ALONE, as ONE commit first, message citing AR-y-491 (a deletion of a tracked file passes `safe-commit.sh` with the path named). No other file under `infra/` changes. The file's content was the signed blob `8897a25273c8547c2ba0d6f9fdd3ce76849fdddf` of the pair `RESIDUE_DELETE_PAIR_7E7J.md`; it is recoverable from git history.

*The check.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~364/`: `check_tf_removed.py` (stdlib only, ruff clean, offline). It prints `RESIDUE-TF-REMOVED tracked=0 infra_changes=1 deletion=yes content_blob_in_history=8897a25273` only if: `git ls-files -- infra/aws/terraform/investor-reporting/ycharts/irpt_residue_delete_r35.tf` prints nothing; `git diff --name-status 4c7935fe2c8 HEAD -- infra/` prints exactly one line, a `D` for that path; and `git rev-parse 4c7935fe2c8:infra/aws/terraform/investor-reporting/ycharts/irpt_residue_delete_r35.tf` prints `8897a25273c8547c2ba0d6f9fdd3ce76849fdddf` (the removed content is the signed blob). Else `RESIDUE-TF-REMOVED-BAD <why>` (rc 1). `--selftest` feeds the three predicates mutated in memory (the file still tracked; a second infra path in the diff; a different content blob) and prints `CONTROL-FIRES` only when ALL THREE read BAD. Commit order: the deletion first; then the script; then the instance.

---

## ACCEPTANCE

<criterion id="AR491-y-AC1" cell_refs="AR-y-491"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~364/check_tf_removed.py</invocation><expect>^RESIDUE-TF-REMOVED tracked=0 infra_changes=1 deletion=yes content_blob_in_history=8897a25273$</expect></criterion>
<criterion id="AR491-y-AC2" cell_refs="AR-y-491"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~364/check_tf_removed.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~364/IRPT_ANLREQ.TO-AR-y-491.remove-the-throwaway-residue-roles-terraform-file-from-the-tree.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-491.remove-the-throwaway-residue-roles-terraform-file-from-the-tree`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR491-y-AC1,AR491-y-AC2"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-491</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/terraform/investor-reporting/ycharts/irpt_residue_delete_r35.tf
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~364/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-491.remove-the-throwaway-residue-roles-terraform-file-from-the-tree.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one Terraform file removed from the tree; nothing is planned, applied or run against AWS; the six resources it declared no longer exist in AWS (destroyed 08:10Z) or in state.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the pair, IB2's destroy report and the CTO's condition against this cell; the lens: a second infra file removed or edited, the wrong content removed, the file kept, the deletion committed with a status flip that removes the grant before the proof. NOT seen (blind): the whole-root plan (IB2 reads it at the close leg); denominator: two criteria.
</preflight>

## AMENDMENT 1 (2.0.0_SA_COO~Y2, 2026-10-21) -- the issuer's error, acknowledged
The check's base commit was wrong: `1e6073761ca` is 51 commits behind the head the worktree was cut from, and seven other infra paths changed in between, so the one-line expectation could not hold (your row W364-S1 is right). The base is now `4c7935fe2c8`, the commit your worktree was cut from (the order's renumbering commit); the criteria and expectations are unchanged. Edit only your check script's base constant and its text, re-run AC1 and AC2, re-validate the instance, and flip the status to complete in the same commit only on VALID. Gate limb that graded the amendment: none stated.
