# TO IRPT_ANLREQ.TO-AR-y-385.prod-based-recut-of-the-dell2-portal-set -- ONE branch cut from origin/PROD that cherry-picks only this box's own commits of the approved dell2 candidates, in dependency order, with a file-by-file payload check that the Trade Request form, the meeting-outcome visibility and commentary-always do not ride; a candidate that cannot apply without an excluded commit is left out and named; a candidate branch, nothing landed

<to_id>IRPT_ANLREQ.TO-AR-y-385</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~285</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ46</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; client-facing portal pages; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-385` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (Andrew's end-to-end read of the Analysis Request on PROD) | **depends_on:** none (base `origin/PROD` @fa21a303d8)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~285`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-285` (branch `wk-IRPT_ANLREQ-285`), with a portal worktree `C:/dev/wk-irpt-anlreq-285/portal` (branch `wk-IRPT_ANLREQ-285-portal`) provisioned by the issuer AT `origin/PROD` (fa21a303d87271a1e2d60c514d13501d71f9f020). Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~285 <0.9.0_WK_IRPT_ANLREQ~285@opal.agent>" -F <msgfile> -- <paths>`. The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: set it per command with `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~285" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~285@opal.agent"` and `--author "0.9.0_WK_IRPT_ANLREQ~285 <0.9.0_WK_IRPT_ANLREQ~285@opal.agent>"` on every `git cherry-pick` and `git commit` (write no git config).
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md` in text mode: APPEND rows only (check `git diff --stat` shows 0 deletions on it). `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W285-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree. The portal worktree has `node_modules` linked: you run `bun run typecheck`, `bun test` on the folders named below and `eslint` on the changed files.

### THE CELL (`AR-y-385`, inlined)

*Context. Andrew's word (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261017_054xZ_PROMOTE_DELL2_PORTAL_SET_TO_PROD_SEE_ANLREQ_END_TO_END.md` @9063a44a4c) approves the dell2 portal set for PROD and EXCLUDES the Trade Request form, `cand/dell2/anlreq-commentary-always-requested` (reverted from PROD on 10-15) and `tckt-meeting-outcome-visibility`. The chosen-set builder (`.tools/portal-release-build.sh --features ...`) cannot assemble the set: three of the branches are cut from DEV and carry its overlap of 53 to 57 commits, which include the Trade Request form (`c05e3dda`), the commentary-always merge (`7f6c698d`), the outcome-visibility commit (`8e4f0885`) and the original meeting-and-trade commit (`12c164a0`), and `cand/dell2/tckt-meeting-form-prod-recut` conflicts in the merge. The CTO's ruling (msg 10330): ONE branch cut from `origin/PROD` fa21a303, cherry-picking only this box's own commits in dependency order; a candidate that cannot apply without an excluded commit is LEFT OUT and NAMED; an excluded commit is never pulled in.*

1. **Read first (record in `r46/CANDIDATE_COMMITS.json`, your deliverables folder):** for each candidate below, its approved head and its OWN commits, computed in the portal worktree. For the six PROD-cut branches the own commits are `git rev-list --reverse --no-merges origin/PROD..<branch>`. For the three DEV-cut branches the own commits are `git rev-list --reverse --no-merges <P>..<branch>` where `<P>` is the first parent of the merge commit on `origin/DEV` whose subject is `Merge <branch> into DEV (approved feature)` (find it with `git log --merges --format=%H --grep="Merge <branch> into DEV" origin/DEV -1`). Print the counts: expected approximately 3, 2, 3, 1, 1, 2 (PROD-cut) and 1, 5, 1 (DEV-cut); a count that differs by more than one: STOP and file a BLOCKING row. Record the four EXCLUDED commits' patch ids (`git show <sha> | git patch-id --stable`): `c05e3dda`, `7f6c698d` (a merge: record its second parent's commits instead), `8e4f0885`, `12c164a0`, and `406345bce1` (the commentary-always commit).
2. **The order of application (dependency order; each is a branch under `cand/dell2/`):** (1) `anlreq-filing-notice`; (2) `anlreq-ticket-commentary-pdf-reader`; (3) `asof-date-only-no-invented-clock`; (4) `irpt-fwd10-partial-history-sentence`; (5) `irpt-series-mirror-contract-031`; (6) `tckt-meeting-form-prod-recut` (the meeting-form content only: its two own commits); (7) `anlreq-advisor-login-email` (its ONE own commit `9355392a93`); (8) `ticket-hop-failure-read-dev` (its own commits, in order); (9) `anlreq-report-ref-revision-string` (its ONE own commit `b8f783791b`). Create the LOCAL branch `cand/dell2/anlreq-prod-recut` at `origin/PROD` and apply each commit with `git cherry-pick -x <sha>` (the `-x` trailer is the record). On a conflict: resolve it ONLY when the resolution adds no behaviour beyond the commit's own diff and pulls in no excluded commit (the conflict hunks name the reason in your record); if a commit cannot apply without an excluded commit or without a behaviour of a candidate you have left out, `git cherry-pick --abort`, LEAVE OUT that whole candidate (also its later commits), name it with the reason in `r46/LEFT_OUT.json`, and go on; never skip a single commit of a candidate that stays in.
3. **The two lint fixes.** Branch `cand/dell2/anlreq-test-lint-fixes` (a separate worker is writing it) holds two test-file rewrites for `filing-hint.test.tsx` and `filing-decision-tree.test.tsx`. Run `eslint` on every file the recut changed or added. A lint error that the recut carries in a file is fixed IN THE RECUT only if it is one of those two files and the fix is the same rewrite; any other error: record it, do not fix it, STOP and file a BLOCKING row (nothing is disabled, no config changes).
4. **The payload check (the heart of the cell).** Write `r46/payload_check.py`. It prints, for the recut against `origin/PROD`: the commit list (`git log --reverse --format='%h %an %s' origin/PROD..cand/dell2/anlreq-prod-recut`), the file list (`git diff --name-status origin/PROD cand/dell2/anlreq-prod-recut`), and then ONE line per excluded item, file by file: `ABSENT TradeRequestParts.tsx`, `ABSENT trade-request tests` (no path under `src/` matching `trade` case-insensitively except files that were already on PROD), `ABSENT meeting-outcome-visibility` (no path matching `meeting-outcome-visibility` and no `MeetingOutcome`-named new file beyond what 8b35's two commits add), `ABSENT commentary-always` (the recut's diff does not make `commentary_requested` a constant `true` on the wire: show the two lines of `analysisRequest.ts` and `contracts/wire/AnalysisSubmissionRequest.ts` that mention `commentary_requested` at the recut and at PROD), and `ABSENT patch-id <sha>` for each of the four excluded patch ids against every commit in the recut. A present item prints `PRESENT <what> <path or sha>` and the script exits 1. It ends with `PAYLOAD-OK <n> commits <m> files` only when every line is ABSENT.
5. **The gates.** In the portal worktree on the recut: `bun run typecheck` (0 errors), `bun test src/pages/TicketCenter src/pages/InvestorReporting` (0 failed; print the counts), `eslint` on every changed file (0 errors). Do NOT run the vite build (the DT seat does at promote). Record each rc and count in `r46/GATES.json`.
6. **Record the head.** Print the full sha of `cand/dell2/anlreq-prod-recut`, `git diff --stat origin/PROD <head>`, the applied candidates (with their cherry-pick shas) and the left-out ones. Never push.
7. **Write `r46/PROD_RECUT_CANDIDATE.json`** in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~285/`: `base_sha`, `head`, `applied` (candidate, own commits, cherry-pick shas), `left_out`, `files_changed`, `tests`, `claim`, `not_read` (the vite build, the rendered pages, the live service). Write the three checker scripts named in ACCEPTANCE.
8. **In your report:** the head, the applied and left-out candidates, the payload check output, the gates.

### ACCEPTANCE

<criterion id="AR385-y-AC1" cell_refs="AR-y-385"><invocation>python C:/dev/wk-irpt-anlreq-285/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~285/r46/payload_check.py</invocation><expect>PAYLOAD-OK </expect></criterion>
`AR385-y-AC1`: the payload check of step 4; it exits 0 and prints `PAYLOAD-OK <n> commits <m> files` only when every excluded item reads ABSENT.

<criterion id="AR385-y-AC2" cell_refs="AR-y-385"><invocation>python C:/dev/wk-irpt-anlreq-285/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~285/gates_check.py</invocation><expect>^GATES-OK </expect></criterion>
`AR385-y-AC2`: you write `gates_check.py`: it runs the step-5 gates on `cand/dell2/anlreq-prod-recut` in `C:/dev/wk-irpt-anlreq-285/portal` and prints `GATES-OK typecheck 0 tests <n> passed 0 failed eslint 0 errors` only when all three hold; otherwise `GATES-BAD <why>`, exit 1. Its control: it also prints `CONTROL-FIRES` after it shows that the payload check of AC1 exits 1 when run against `cand/dell2/anlreq-report-ref-revision-string` (a DEV-cut branch that carries the Trade Request form) in place of the recut.

<criterion id="AR385-y-AC3" cell_refs="AR-y-385"><invocation>python C:/dev/wk-irpt-anlreq-285/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~285/applied_check.py</invocation><expect>^APPLIED-OK </expect></criterion>
`AR385-y-AC3` (a third check, with a reason: the set must be exactly what the CTO named, with every omission named): you write `applied_check.py`: it prints `APPLIED-OK <a> applied <l> left out` only when every one of the nine candidates is in exactly one of `applied` or `left_out` of `r46/PROD_RECUT_CANDIDATE.json`, every applied candidate's own commits all appear as `(cherry picked from commit <sha>)` lines in `git log origin/PROD..cand/dell2/anlreq-prod-recut`, and every left-out candidate carries a reason; otherwise `APPLIED-BAD <why>`, exit 1.

<criterion id="AR385-y-AC4J" cell_refs="AR-y-385" judgment="true"/>
`AR385-y-AC4J` (judgment, graded at L9, never by you): the recut carries only the approved candidates' own commits; no excluded commit, file or behaviour rides; every conflict resolution added no behaviour beyond the commit's own diff; every left-out candidate is named with its reason; nothing was pushed or landed; and the record says plainly what it did not read.

<expected_criteria>AR385-y-AC1 AR385-y-AC2 AR385-y-AC3 AR385-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~285/` and this order's file (status flip only), and INSIDE the portal worktree: the LOCAL branch `cand/dell2/anlreq-prod-recut` and the files its cherry-picks change (and the two test-file lint rewrites of step 3 where they apply). No edit of any file by hand beyond a conflict resolution, a cherry-pick, or step 3's rewrite.
- READ only: every other branch; the excluded commits' content (read to compute patch ids). NO push of any branch.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-385</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~285/IRPT_ANLREQ.TO-AR-y-385.prod-based-recut-of-the-dell2-portal-set.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-385`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR385-y-AC1,AR385-y-AC2,AR385-y-AC3,AR385-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a portal candidate branch cut from PROD; nothing is called, landed or pushed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed by the issuer; the cherry-picks carry the candidates' own diffs. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by running `.tools/portal-release-build.sh --features` on the eight approved branches (READY, but the release carried `TradeRequestParts.tsx`, `7f6c698d` and `8e4f0885`: `git merge-base --is-ancestor` exit 0 for each) and a first cherry-pick trial (the revision fix applies alone; login-email and hop-failure conflict without the earlier candidates) against the cell; the lens: a conflict resolved by taking an excluded commit's hunk, a candidate's later commits applied after an earlier one was skipped, a payload check that looks only at file names, a patch id compared against the wrong commit, a PRESENT line swallowed. The cell requires dependency order, an abort-and-leave-out rule, a payload check on paths, content and patch ids with a control that fires. NOT seen (blind): the vite build, the rendered pages and the live service; denominator: 9 candidates, 4 excluded items, 3 checkers, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (msg 10330, "APPROVED: ONE PROD-based recut branch as the release, approved by sha against Andrew's word 9063a44a4c"). Workstream `ZZ46` of round 43. Base (`origin/PROD` fa21a303d8): `r46/` and the candidate branch are absent, so `AR385-y-AC1`, `AC2` and `AC3` FAIL as expected.
- Next: the issuer opens ONE approval row on the recut head (class client-facing); the CTO approves it by sha if the payload check passes; then `0.4.0_DT_ClientPlatform~DELL2` promotes it through `/prod-deploy`; then one Retry on `TCK-20261017-5af976ff` and its read-back. The two lint fixes stay on `cand/dell2/anlreq-test-lint-fixes` (worker 284) unless step 3 needs them.
