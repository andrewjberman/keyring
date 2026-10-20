# TO IRPT_ANLREQ.TO-AR-y-425.c-filing-hint-keep-path-restored-on-top-of-the-form-cleanup -- C-FILING-HINT Keep path (AR-y-354) restored: Keep re-posts the SAME upload with the equal pair {TICKER_NOT_FOUND, X -> X}, so the door (AR-g-68) files the kept symbol as UNRESOLVED and it reaches C-SWAP; re-applied on top of your AR-y-416 and AR-y-419 commits

<to_id>IRPT_ANLREQ.TO-AR-y-425.c-filing-hint-keep-path-restored-on-top-of-the-form-cleanup</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~310</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ84</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-425` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-FILING-HINT, C-SWAP (an unknown holding such as BREIT can reach the swap from the form) | **depends_on:** AR-y-416 and AR-y-419 (YOUR own commits: you build on them); AR-g-68 (the door, built and complete, G2's lane; the portal Keep ships only in the same release as the door or after it); CTO msg 11106 (AR-y-354 was retired in error)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~310`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-310` (branch `wk-IRPT_ANLREQ-310`), with a portal worktree `C:/dev/wk-irpt-anlreq-310/portal` (branch `wk-IRPT_ANLREQ-310-portal`) provisioned by the issuer AT `origin/DEV` (4f9f2f633dc0). Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~310 <0.9.0_WK_IRPT_ANLREQ~310@opal.agent>" -F <msgfile> -- <paths>` (a commit can take up to 400 s: wait and check `git log` before retrying). The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: run `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~310" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~310@opal.agent" git -C C:/dev/wk-irpt-anlreq-310/portal commit --author "0.9.0_WK_IRPT_ANLREQ~310 <0.9.0_WK_IRPT_ANLREQ~310@opal.agent>" -F <msgfile>` (write no git config).
- Write every message file with the Write tool. APPEND rows only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, and COMMIT them. `surfaced_at` of any row = `date -u +%FT%TZ`; a row id has the form `IRPT_ANLREQ-D2-W310-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~300/` (the AR-y-410 instance; read it first; `git show HEAD:<path>` if absent), `to_id` exactly the order's id, a `controls.mutant` that FIRES and a `controls.determinism` really run. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`, and flip `<status>` to `complete` (commit alone) only on VALID. Scratch outside the product tree. Run the portal tests from `C:/dev/wk-irpt-anlreq-310/portal` with `bun test <path>` (node_modules is linked); the worktree is SPARSE: run ONLY the new test file and the folders the criteria name.

### THE CELL (`AR-y-425`, inlined)

*Context.* `AR-y-354` (worker 154, portal commit `f78ea50ef87d`, kept in the portal repository as the tag `archive/cand/dell2/anlreq-filing-hint-keep-equal-pair`; read it with `git -C <your portal worktree> show archive/cand/dell2/anlreq-filing-hint-keep-equal-pair`) is the C-FILING-HINT Keep path (PRD v0.15 item 3). Its message: Keep re-posts the SAME upload (same `upload_token`, same file) with the correction `{finding_code: 'TICKER_NOT_FOUND', from_value: <symbol>, to_value: <the same symbol>}` through the same filing path `Use` takes, so a NORMALIZED answer files the ticket and a NEEDS_CORRECTION answer shows the remaining hints; the door (AR-g-68, `intake/portfolio.py`) files the kept row as UNRESOLVED and it reaches C-SWAP. Five files: `analysisRequest.ts` (`keptHint`, `isKeptHint`, `withFilingChoice` where the last click for a symbol stands, `correctionsFor` building one correction per symbol, never a case-only pair, capped at `MAX_FILING_CORRECTIONS` 20, and the `keptLine` words), `TicketCenter.tsx` (one `chooseHint` accumulator for Use and Keep on the staff and partner routes; `keepHint = chooseHint(keptHint(h))`), `AnalysisRequestParts.tsx` (Keep offered only while the cap allows), the new `__tests__/filing-hint-keep.test.tsx` (seven cases a to g) and `__tests__/filing-hint.test.tsx` (case d re-pinned from "sends nothing" to the equal pair). It was retired by the issuer in error (it never touched the report-type field; the issuer misread its message) and the CTO has restored it (msg 11106). Your AR-y-416 and AR-y-419 changed `analysisRequest.ts`, `TicketCenter.tsx` and `AnalysisRequestParts.tsx` (the advisor-email, report-type and commentary removal, the firm read, the static models), so the old commit conflicts: you resolve it.

*The change.* Re-apply the whole of `f78ea50e`'s behaviour on top of your own portal commits (a cherry-pick with conflict resolution, or a manual re-application: your choice; the result must read as ONE new portal commit after your AR-y-419 commit). Keep BOTH sets of behaviour: nothing from AR-y-416 or AR-y-419 may return (no advisor email field, no report-type select, no Add-commentary box, the static models, `includeUnavailable` as it is now) and every behaviour listed above must hold. Keep the commit's words unchanged (`keptLine`: the symbol is kept as typed, not priced, and goes to the backend with the request; no raw code shown; the form never offers a swap). Adapt the two test files to the form as it is after your commits (the seven cases keep their intent; the existing `filing-hint.test.tsx` case d stays re-pinned to the equal pair); add no other test.

*Note for the record (not yours to act on).* The server refuses the equal pair with `CORRECTIONS_INVALID` until the door release AR-g-68 is applied, so this commit ships ONLY in the same release as that door change or after it (CTO msg 11106). Your commit changes nothing about that ordering.

*What to do.* (1) Baseline `cd portal && bun test src/pages/TicketCenter` (243 pass at your HEAD). (2) Re-apply; run the new test file (` 7 pass`, ` 0 fail`) and the folder (` 0 fail`); print both. `controls.mutant` = the new file run with `keptHint` returning an unequal pair (case a must FAIL). (3) Write `check_keep_bound.py` (below); commit the portal source in the portal worktree and the workspace files; then the proof instance and flip on VALID with all three PASS.

You also write `check_keep_bound.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/` (ruff clean, stdlib only): it takes your portal worktree's commit that carries AR-y-419 (find it with `git -C <portal> log --format=%H --grep=AR-y-419 -1`) and lists the files changed since it, and prints `KEEP-BOUND-OK files=<n>` only when every changed path is under `src/pages/TicketCenter/` and n is 3 to 6; otherwise `KEEP-BOUND-BAD <paths>` and a non-zero exit.

---

## ACCEPTANCE

<criterion id="AR425-y-AC1" cell_refs="AR-y-425"><invocation>cd portal && bun test src/pages/TicketCenter/__tests__/filing-hint-keep.test.tsx</invocation><expect> 7 pass</expect></criterion>
<criterion id="AR425-y-AC2" cell_refs="AR-y-425"><invocation>cd portal && bun test src/pages/TicketCenter</invocation><expect> 0 fail</expect></criterion>
<criterion id="AR425-y-AC3" cell_refs="AR-y-425"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/check_keep_bound.py</invocation><expect>^KEEP-BOUND-OK files=[3-6]$</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/IRPT_ANLREQ.TO-AR-y-425.c-filing-hint-keep-path-restored-on-top-of-the-form-cleanup.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-425.c-filing-hint-keep-path-restored-on-top-of-the-form-cleanup`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR425-y-AC1,AR425-y-AC2,AR425-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-425</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
portal/src/pages/TicketCenter/
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~310/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-425.c-filing-hint-keep-path-restored-on-top-of-the-form-cleanup.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one Ticket Center folder of the portal; a candidate branch, nothing landed or pushed; the commit ships only with or after the door release AR-g-68.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the archived commit f78ea50e, the CTO ruling (msg 11106) and PRD v0.15 item 3 against this cell; the lens: a conflict resolution that brings back a removed field (the folder run includes the AR-y-416 and AR-y-419 tests), a Keep that posts without a click (case c), a case-only pair (case e), a swap offered at the form (case g), the commit shipping before the door (a release-order condition noted on the face). NOT seen (blind): the live door; denominator: three criteria.
</preflight>
