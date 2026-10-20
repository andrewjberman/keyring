# TO IRPT_ANLREQ.TO-AR-y-428.keep-words-follow-the-two-c-swap-outcomes -- The Keep press words follow C-SWAP's two outcomes: "<X> is kept as you typed it. It is not priced on this form; the report matches it to a comparable fund or lists it as not analysed."

<to_id>IRPT_ANLREQ.TO-AR-y-428.keep-words-follow-the-two-c-swap-outcomes</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~310</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ87</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-428` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-FILING-HINT, C-SWAP | **depends_on:** AR-y-425 (YOUR own commit d8ad232e6667: the words you applied to the No press); CTO msg 11142 item 2 (the words are fixed by the CTO)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~310`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-310` (branch `wk-IRPT_ANLREQ-310`), with a portal worktree `C:/dev/wk-irpt-anlreq-310/portal` (branch `wk-IRPT_ANLREQ-310-portal`) provisioned by the issuer AT `origin/DEV` (4f9f2f633dc0). Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~310 <0.9.0_WK_IRPT_ANLREQ~310@opal.agent>" -F <msgfile> -- <paths>` (a commit can take up to 400 s: wait and check `git log` before retrying). The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: run `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~310" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~310@opal.agent" git -C C:/dev/wk-irpt-anlreq-310/portal commit --author "0.9.0_WK_IRPT_ANLREQ~310 <0.9.0_WK_IRPT_ANLREQ~310@opal.agent>" -F <msgfile>` (write no git config).
- Write every message file with the Write tool. APPEND rows only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, and COMMIT them. `surfaced_at` of any row = `date -u +%FT%TZ`; a row id has the form `IRPT_ANLREQ-D2-W310-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~300/` (the AR-y-410 instance; read it first; `git show HEAD:<path>` if absent), `to_id` exactly the order's id, a `controls.mutant` that FIRES and a `controls.determinism` really run. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`, and flip `<status>` to `complete` (commit alone) only on VALID. Scratch outside the product tree. Run the portal tests from `C:/dev/wk-irpt-anlreq-310/portal` with `bun test <path>` (node_modules is linked); the worktree is SPARSE: run ONLY the new test file and the folders the criteria name.

### THE CELL (`AR-y-428`, inlined)

*Context.* In AR-y-425 you applied the restored `keptLine` words to the decision tree's No press (`analysisRequest.ts`, the `keptLine` function and its use, replacing the ruled `NO_CHOICE_LINE`), and reported the choice (row W310-S2). The CTO confirmed it: the Keep stays on the No press with no duplicate button, and changed the WORDS (msg 11142 item 2) so they follow C-SWAP's two outcomes. The words the filer reads after pressing Keep for a symbol `X` must be EXACTLY: `X is kept as you typed it. It is not priced on this form; the report matches it to a comparable fund or lists it as not analysed.` (the symbol as typed, then a space and the sentence as written; plain ASCII; no raw finding code shown; the form still never offers a swap). Today's words say "not priced, and goes to the backend with the request".

*The change.* Change the ONE place that builds those words (`keptLine` or the constant it uses) to the sentence above, nothing else in the product code. Update every existing test that pins the old words so it pins the new sentence (read the pinned ones: `filing-hint-keep.test.tsx` case (f), `filing-hint.test.tsx` case (d), `filing-decision-tree.test.tsx` case (e), and any other that `grep` for `goes to the backend` or `not priced` in `src/pages/TicketCenter/` finds), keeping each test's intent and weakening no assertion. Add the NEW file `src/pages/TicketCenter/__tests__/keep-words.test.tsx` with EXACTLY two tests: (1) for the symbol `BREIT` the kept line is exactly `BREIT is kept as you typed it. It is not priced on this form; the report matches it to a comparable fund or lists it as not analysed.`; (2) that line contains no `TICKER_NOT_FOUND`, no `backend` and no `swap`/`proxy` word.

*What to do.* (1) Baseline `cd portal && bun test src/pages/TicketCenter` (250 pass at your HEAD) and print it. (2) Write the two tests first and run them against the unchanged code (both must FAIL: the difference control). (3) Make the change and update the pinned tests; run the new file (` 2 pass`, ` 0 fail`) and the folder (` 0 fail`). `controls.mutant` = the new file with the sentence's last clause changed (test 1 must FAIL). (4) Write `check_keepw_bound.py` (below), commit the portal source in the portal worktree and the workspace files, then the proof instance and flip on VALID with all three PASS.

You also write `check_keepw_bound.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/` (ruff clean, stdlib only): it takes your portal worktree's commit that carries AR-y-425 (anchor on the subject: `git -C <portal> log --format=%H --grep='^feat(TicketCenter): C-FILING-HINT Keep path restored' -1`) and lists the files changed since it, and prints `KEEPW-BOUND-OK files=<n>` only when every changed path is under `src/pages/TicketCenter/` and n is 2 to 6; otherwise `KEEPW-BOUND-BAD <paths>` and a non-zero exit.

---

## ACCEPTANCE

<criterion id="AR428-y-AC1" cell_refs="AR-y-428"><invocation>cd portal && bun test src/pages/TicketCenter/__tests__/keep-words.test.tsx</invocation><expect> 2 pass</expect></criterion>
<criterion id="AR428-y-AC2" cell_refs="AR-y-428"><invocation>cd portal && bun test src/pages/TicketCenter</invocation><expect> 0 fail</expect></criterion>
<criterion id="AR428-y-AC3" cell_refs="AR-y-428"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/check_keepw_bound.py</invocation><expect>^KEEPW-BOUND-OK files=[2-6]$</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/IRPT_ANLREQ.TO-AR-y-428.keep-words-follow-the-two-c-swap-outcomes.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-428.keep-words-follow-the-two-c-swap-outcomes`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR428-y-AC1,AR428-y-AC2,AR428-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-428</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
portal/src/pages/TicketCenter/
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-428.keep-words-follow-the-two-c-swap-outcomes.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one sentence in one Ticket Center file and the tests that pin it; a candidate branch, nothing landed or pushed.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the CTO msg 11142 item 2 against this cell; the lens: a test weakened to pass (the difference control runs the new file on the old code and it must fail), the old words left in a pinned test (the folder run), a swap or raw code shown (test 2). NOT seen (blind): the live form; denominator: three criteria.
</preflight>
