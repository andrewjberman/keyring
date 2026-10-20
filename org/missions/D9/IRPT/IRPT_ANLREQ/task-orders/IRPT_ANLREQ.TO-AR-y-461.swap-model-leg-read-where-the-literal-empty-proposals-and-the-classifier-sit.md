# TO IRPT_ANLREQ.TO-AR-y-461.swap-model-leg-read-where-the-literal-empty-proposals-and-the-classifier-sit -- READ ONLY: for the C-SWAP model leg (PRD v0.25), find in source where `swap_pass` receives its model proposals as a literal empty list, what classifier exists and how it is called, and the smallest change that wires them; no code is edited

<to_id>IRPT_ANLREQ.TO-AR-y-461.swap-model-leg-read-where-the-literal-empty-proposals-and-the-classifier-sit</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~326</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ120</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read of source; one record file) | **Decomp cell:** `AR-y-461` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-2 (the swap model leg, contract C-SWAP, PRD v0.25 ADDENDUM) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~326`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-326` (branch `wk-IRPT_ANLREQ-326`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~326 <0.9.0_WK_IRPT_ANLREQ~326@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W326-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields.
- **No AWS call, no network, no code edit, no push, no deploy.** Read with the Read and Grep tools; for a repo-wide name search use Grep with a `glob`, never a recursive shell grep. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first), with `to_id` exactly the order's id; run `python .tools/proof-of-spec-check.py <instance> "AR461-y-AC1,AR461-y-AC2,AR461-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID.

### THE CELL (`AR-y-461`, inlined)

*Context.* PRD v0.25 says the swap model leg of contract C-SWAP is wired by passing the classification and the model proposals that `swap_pass` currently receives as a literal `[]`: "the model widens the pool and never picks; a pick below 0.80 confidence is flagged; no new vendor". The C-SWAP contract (PRD `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`, the row beginning `C-SWAP:`) says: step (3) CLASSIFY only if neither Yahoo nor YCharts has prices, using SECCLASS's classifier on kimi-k2.6 with a web-search tool and the tool-call loop, output bound to the live (class, sub-class) vocabulary, below 0.80 confidence FLAGGED; step (4) REPLACE from the class-matched pool (registry rows plus model proposals that pass the class match and have Yahoo history), the longest Yahoo history winning, ties by ticker. The code is under `infra/aws/lambda/investor-reporting/ycharts/research/` (`swap_pass.py`, `swap_replacement.py`, `build_swap_pool.py`, `opal_producer.py`, tests in `tests/test_opal_producer_swap.py`) and the resident copy `infra/aws/lambda/investor-reporting/reports/resident_installed.py`.

*The read.* Write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~326/SWAP_LEG_READ.md` with exactly these four sections, each heading starting `## S1 `, `## S2 `, `## S3 `, `## S4 `, every claim carrying a `path:line` cite read in this worktree:
- **S1 where the proposals enter:** every place `swap_pass` / `swap_holdings` is called, and the literal `[]` (or equivalent) the model proposals take at each call; the function signatures; what shape a proposal must have to pass the class match and the Yahoo-history rule; how the resident reaches this code.
- **S2 what classifies today:** the classifier the contract names (SECCLASS, kimi-k2.6): its module path, entry function, inputs and outputs, how its output is bound to the live (class, sub-class) vocabulary, where its confidence and the 0.80 threshold live (or that they do not exist), and what it needs at run time (network, secrets, dependencies) compared with what the investor-reporting resident has. Say plainly if no such classifier exists in this tree.
- **S3 the tests that exist:** `tests/test_opal_producer_swap.py` and any other test of the swap pass: what they inject, and how a model proposal and a classification would be injected in a test with no network.
- **S4 the smallest change:** a list of files and functions that would have to change to wire the classification and proposals as the contract says, each with the reason, and the one question you could not answer from source.
End the file with one line `NOT-READ: <what you did not or could not read, or none>`.

---

## ACCEPTANCE

<criterion id="AR461-y-AC1" cell_refs="AR-y-461"><invocation>grep -c -E '^## S[1-4] ' org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~326/SWAP_LEG_READ.md</invocation><expect>^4$</expect></criterion>
<criterion id="AR461-y-AC2" cell_refs="AR-y-461"><invocation>grep -c -o -E '[A-Za-z0-9_./-]+\.py:[0-9]+' org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~326/SWAP_LEG_READ.md</invocation><expect>^([89]|[1-9][0-9]+)$</expect></criterion>
<criterion id="AR461-y-AC3" cell_refs="AR-y-461"><invocation>grep -c -E '^NOT-READ: .+' org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~326/SWAP_LEG_READ.md</invocation><expect>^1$</expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~326/IRPT_ANLREQ.TO-AR-y-461.swap-model-leg-read-where-the-literal-empty-proposals-and-the-classifier-sit.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-461.swap-model-leg-read-where-the-literal-empty-proposals-and-the-classifier-sit`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR461-y-AC1,AR461-y-AC2,AR461-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-461</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~326/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-461.swap-model-leg-read-where-the-literal-empty-proposals-and-the-classifier-sit.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of source and one record file in the worker deliverables; no code edit, no AWS call, no deploy.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the PRD v0.25 ADDENDUM and the C-SWAP row against this cell; the lens: a cite to a line that does not carry the claim (every cite must be re-read at the line), a classifier assumed to exist because the contract names it, a copy of the resident that differs from the source tree copy, an answer given for the wrong call site. NOT seen (blind): the deployed resident bytes on the host and the live classifier service; denominator: four sections.
</preflight>
