# TO IRPT_ANLREQ.TO-AR-y-389.prod-into-dev-reconcile-merge -- a branch cut from origin/DEV that merges origin/PROD into it, with the conflicts in src/api/endpoints/tickets.ts and src/pages/TicketCenter/TicketCenter.tsx resolved so each change appears once as on both sides, the Trade Request code neither added nor moved, typecheck 0 errors, eslint 0 errors and the TicketCenter tests no worse than DEV's, and a file-by-file resolution note; a candidate branch, nothing pushed by the worker

<to_id>IRPT_ANLREQ.TO-AR-y-389</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~289</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ50</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; client-facing portal pages; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-389` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (DEV and PROD must carry the same history so the next promote is clean) | **depends_on:** none (base `origin/DEV` @539b1ee70ba1)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~289`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-289` (branch `wk-IRPT_ANLREQ-289`), with a portal worktree `C:/dev/wk-irpt-anlreq-289/portal` (branch `wk-IRPT_ANLREQ-289-portal`) provisioned by the issuer AT `origin/DEV` (539b1ee70ba1). Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~289 <0.9.0_WK_IRPT_ANLREQ~289@opal.agent>" -F <msgfile> -- <paths>`. The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: set it per command with `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~289" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~289@opal.agent"` and `--author "0.9.0_WK_IRPT_ANLREQ~289 <0.9.0_WK_IRPT_ANLREQ~289@opal.agent>"` on every `git merge` and `git commit` (write no git config).
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md`: APPEND rows only (0 deletions). `surfaced_at` of any row = `date -u +%FT%TZ`; a row id has the form `IRPT_ANLREQ-D2-W289-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add. No live call, NO PUSH of any branch, no deploy. Never use `git reset --hard`, `git rebase` or a force option. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree. The portal worktree has `node_modules` linked: you run `bun run typecheck`, `bun test` on the folders named below and `eslint` on the changed files.

### THE CELL (`AR-y-389`, inlined)

*Context. `origin/PROD` (15bc21b304d4) holds 23 commits that `origin/DEV` (539b1ee70ba1) lacks, and `origin/DEV` holds 102 that PROD lacks. The 23 are two PROD-based recuts of work that was already on DEV: the release `4cf06588736b` (branch `cand/dell2/anlreq-prod-recut-v2`, 20 cherry-picked commits) and `15bc21b304d4` (the meeting outcome-line contrast fix `2a64d2115f`), plus the earlier PROD history. A trial `git merge-tree --write-tree --name-only origin/DEV origin/PROD` conflicts in exactly two files, `src/api/endpoints/tickets.ts` and `src/pages/TicketCenter/TicketCenter.tsx` (and auto-merges `src/pages/InvestorReporting/dashboard/DashboardPerformance.tsx`). The CTO's ruling (msg 10552): cut a branch from origin/DEV, merge origin/PROD into it, resolve the two conflicts so each change appears ONCE, as on both sides; keep the Trade Request code out of PROD's side and do not add it; typecheck, eslint at 0 errors and the TicketCenter tests; push as `cand/dell2/prod-into-dev-reconcile` (the issuer pushes, not you) with a file-by-file resolution note.*

1. **Cut and merge.** In the portal worktree create the LOCAL branch `cand/dell2/prod-into-dev-reconcile` at `origin/DEV` (run `git fetch origin` first and print `git rev-parse origin/DEV` and `git rev-parse origin/PROD`; they must read `539b1ee70ba1...` and `15bc21b304d4...`; if either moved, print the new values and go on, naming them in your record). Run `git merge --no-ff origin/PROD` with the committer env above. Print `git merge-tree --write-tree --name-only origin/DEV origin/PROD` BEFORE the merge and the list of files `git diff --name-only --diff-filter=U` shows after it: the expected conflicted files are the two named above; any OTHER conflicted file: STOP and file a BLOCKING row naming it.
2. **Resolve the two files by provenance, hunk by hunk.** For each conflicted hunk print (in `r48/RESOLUTION_NOTE.md`, your deliverables folder) the DEV side, the PROD side and the rule that decides it: the PROD side is a cherry-pick of a DEV change, so BOTH sides hold the SAME change in different surroundings; the resolved file holds that change ONCE (never doubled, never dropped), in DEV's surroundings, plus any change that exists on only one side. Prove it: for each file, `git diff origin/DEV <branch> -- <file>` (what the merge adds to DEV's file) must contain only hunks that are PROD-only (a change DEV lacks); list each such hunk and name the PROD commit that carries it (`git log -S"<a distinctive line>" origin/PROD -- <file>`). An empty diff is a legal and likely answer for a file whose PROD changes are all already on DEV. A doubled declaration, import, JSX block or function that the typecheck does not catch must be looked for by reading the resolved hunks, not only by running tools.
3. **The Trade Request code.** `git diff --name-only origin/DEV <branch>` must contain NO path matching `trade` (case-insensitive) and the resolved `TicketCenter.tsx` must hold the same Trade Request lines as `origin/DEV`'s (compare the `trade`/`Trade` lines of `git show origin/DEV:src/pages/TicketCenter/TicketCenter.tsx` and of the resolved file: equal sets). Do not remove, move or add Trade Request code.
4. **Gates (in the portal worktree on the branch).** `bun run typecheck` (0 errors), `eslint` on every file `git diff --name-only origin/DEV <branch>` lists (0 errors), and `bun test src/pages/TicketCenter src/pages/InvestorReporting` run the same way at `origin/DEV` in a detached worktree of the same repository and on the branch: the failing test lines at the branch must EQUAL (as a multiset) those at `origin/DEV`; a test file that errors (fails to load) on the branch but not at `origin/DEV` is named with its cause. Record counts in `r48/GATES.json`. The worktree is sparse, so some tests fail in BOTH trees; only a difference counts.
5. **Ancestry proofs.** Print `git merge-base --is-ancestor origin/PROD <branch>` (exit 0), `git merge-base --is-ancestor origin/DEV <branch>` (exit 0), and `git rev-list --count origin/DEV..<branch>` (the merge commit plus nothing else: expected 24, i.e. the 23 PROD commits plus the merge; print the number and explain a different one). Record the full head sha. Never push.
6. **Write** `r48/RECONCILE_CANDIDATE.json` (base_sha, prod_sha, head, conflicted_files, per-file hunks resolved with provenance, tests, claim, not_read: the rendered pages, the vite build, anything on a server) and the three checkers named in ACCEPTANCE.
7. **In your report:** the head, the conflicted files and what each resolution did, the gates and any difference.

### ACCEPTANCE

<criterion id="AR389-y-AC1" cell_refs="AR-y-389"><invocation>python C:/dev/wk-irpt-anlreq-289/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~289/r48/ancestry_check.py</invocation><expect>^ANCESTRY-OK </expect></criterion>
`AR389-y-AC1`: you write `ancestry_check.py`: it prints `ANCESTRY-OK head <sha12> contains origin/PROD and origin/DEV, <n> commits over DEV, no conflict markers` only when both ancestry checks exit 0 and `git grep -n -E '^(<<<<<<<|=======|>>>>>>>)' <branch> -- src` finds nothing; otherwise `ANCESTRY-BAD <why>`, exit 1.

<criterion id="AR389-y-AC2" cell_refs="AR-y-389"><invocation>python C:/dev/wk-irpt-anlreq-289/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~289/r48/gates_check.py</invocation><expect>^GATES-OK </expect></criterion>
`AR389-y-AC2`: you write `gates_check.py`: it prints `GATES-OK typecheck 0 eslint 0 errors failing-lines-equal-DEV <k> new-load-errors <e> explained trade-lines-equal <t>` only when typecheck and eslint hold, the failing test lines equal `origin/DEV`'s, every new load error is explained in `r48/GATES.json`, no path matching `trade` differs from DEV and the Trade Request lines of `TicketCenter.tsx` equal DEV's, AND (AMENDMENT 1, CTO msg 10556) the diff of `origin/PROD` against the branch head names NO file outside the DEV-only set (`git diff --name-only origin/PROD <branch>` is a subset of `git diff --name-only origin/PROD origin/DEV`) and no Trade Request hunk crosses into PROD content (the set of `trade`/`Trade` lines of `git diff origin/PROD <branch>` equals the set of the same lines of `git diff origin/PROD origin/DEV`; it prints both counts); otherwise `GATES-BAD <why>`, exit 1.

<criterion id="AR389-y-AC3" cell_refs="AR-y-389"><invocation>python C:/dev/wk-irpt-anlreq-289/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~289/r48/once_check.py</invocation><expect>^ONCE-OK </expect></criterion>
`AR389-y-AC3` (a third check, with a reason: the CTO's rule is "each change appears once", which a typecheck can pass while a block is doubled): you write `once_check.py`: for `src/api/endpoints/tickets.ts` and `src/pages/TicketCenter/TicketCenter.tsx` it extracts every top-level `export` declaration name and every import specifier and prints `ONCE-OK <n> exports <m> imports, none repeated, every export of origin/DEV and of origin/PROD present` only when no name repeats and the union of the exports of `origin/DEV:<file>` and `origin/PROD:<file>` is a subset of the resolved file's exports; its control: it prints `CONTROL-FIRES` after it shows it rejects a copy of the resolved file in which one export is duplicated.

<criterion id="AR389-y-AC4J" cell_refs="AR-y-389" judgment="true"/>
`AR389-y-AC4J` (judgment, graded at L9, never by you): each of the resolved hunks holds its change exactly once in DEV's surroundings; no Trade Request line was added, moved or removed; the `git diff origin/DEV <branch>` hunks are PROD-only and each names its PROD commit; nothing was pushed; and the record says plainly what it did not read.

<expected_criteria>AR389-y-AC1 AR389-y-AC2 AR389-y-AC3 AR389-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~289/` and this order's file (status flip only), and INSIDE the portal worktree: the LOCAL branch `cand/dell2/prod-into-dev-reconcile` and the merge commit with its resolutions in `src/api/endpoints/tickets.ts` and `src/pages/TicketCenter/TicketCenter.tsx`. A resolution anywhere else, or a hand edit beyond a conflict resolution: STOP, file a BLOCKING row.
- READ only: every other branch and file. NO push of any branch.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-389</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~289/IRPT_ANLREQ.TO-AR-y-389.prod-into-dev-reconcile-merge.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-389`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR389-y-AC1,AR389-y-AC2,AR389-y-AC3,AR389-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a portal candidate branch (a merge of PROD into DEV in a worktree); nothing is called, landed or pushed by the worker.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by a trial `git merge-tree --write-tree --name-only origin/DEV origin/PROD` (exactly two conflicted files; 23 PROD-only and 102 DEV-only commits) and the earlier recut work (a DEV-cut branch carries excluded content; the sparse worktree fails tests in both trees) against the cell; the lens: a conflict resolved by taking one side whole (dropping the other side's change), a change doubled that the typecheck passes, a Trade Request line moved or removed, a hand edit beyond the conflicts, a test difference hidden by a failing baseline. The cell requires hunk-by-hunk provenance, an export-uniqueness check with a control, the Trade Request lines equal to DEV's, and failing test lines equal to DEV's. NOT seen (blind): the rendered pages and the vite build; denominator: 2 conflicted files, 3 checkers, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (msg 10552, `1.0.0_SA_CTO~DELL2`, deadline 18:00Z today for the head sha, via `0.0.0_AB_MSTR~DELL2` to dell1 and the laptop). Workstream `ZZ50` of round 43. Base: `r48/` and the branch are absent, so AC1, AC2 and AC3 FAIL as expected.
- After the worker: the issuer re-runs the three checks, has `2.0.0_SA_COO~V2` review the meeting form and outcome-line hunks (CTO msg 10552), pushes `cand/dell2/prod-into-dev-reconcile` from the worker's portal worktree and sends the head sha. The merge into DEV is the laptop's and the integrator's act, not this worker's.
