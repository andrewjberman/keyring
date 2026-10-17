# TO IRPT_ANLREQ.TO-AR-y-384.two-test-file-lint-errors -- the two lint errors that stop the portal build on DEV (no-regex-spaces in filing-hint.test.tsx, no-control-regex in filing-decision-tree.test.tsx) are fixed in the test files only, with no change to what the tests assert; a test-only candidate, nothing landed

<to_id>IRPT_ANLREQ.TO-AR-y-384</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~284</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ45</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; portal test files for a client-facing page; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-384` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the PROD release of the dell2 portal set must build green) | **depends_on:** none (base `origin/DEV` @4d4dc68cae)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~284`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-284` (branch `wk-IRPT_ANLREQ-284`), with a portal worktree `C:/dev/wk-irpt-anlreq-284/portal` (branch `wk-IRPT_ANLREQ-284-portal`) provisioned by the issuer AT `origin/DEV` (4d4dc68cae). Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~284 <0.9.0_WK_IRPT_ANLREQ~284@opal.agent>" -F <msgfile> -- <paths>`. The PORTAL source is committed INSIDE the portal worktree, which has no committer identity: run `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~284" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~284@opal.agent" git -C C:/dev/wk-irpt-anlreq-284/portal commit --author "0.9.0_WK_IRPT_ANLREQ~284 <0.9.0_WK_IRPT_ANLREQ~284@opal.agent>" -F <msgfile>` (write no git config).
- Write every message file with the Write tool. Never rewrite `INVESTIGATION_v1.md` in text mode: APPEND rows only (check `git diff --stat` shows 0 deletions on it). `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W284-S<k>`. The workspace worktree shows ` M portal`: never commit it. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH of any branch, no deploy. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py`. Scratch outside the product tree. The worktree is SPARSE: you run ONLY the two test files named below, the folder `src/pages/TicketCenter`, and eslint on those two files.

### THE CELL (`AR-y-384`, inlined)

*Context. The portal's lint (`bun run lint` = `eslint .`) reports two errors on `origin/DEV` that stop a release build: `no-regex-spaces` in `src/pages/TicketCenter/__tests__/filing-hint.test.tsx` (a regular-expression literal that holds two or more consecutive spaces; read the file, the line is in the `SOURCES[2].match(/const chooseHint = ... \n  \}/)` area, about line 190) and `no-control-regex` in `src/pages/TicketCenter/__tests__/filing-decision-tree.test.tsx` (a regular-expression literal that holds a control character, about line 299). The CTO's message gave those two lines; the line numbers may differ from `origin/DEV`, so the eslint output is the oracle, not the number. Both are test files. Nothing about what the tests assert may change.*

1. **Read first (record in `r45/LINT_FINDING.json` in your deliverables folder):** run `eslint` on exactly the two files in the portal worktree (for example `bunx eslint src/pages/TicketCenter/__tests__/filing-hint.test.tsx src/pages/TicketCenter/__tests__/filing-decision-tree.test.tsx`; if the repository runs eslint another way, use that and record the command) and record each reported error: file, line, rule, the offending literal.
2. **The change.** For `no-regex-spaces`: write the run of spaces inside the literal as a counted space (` {2}`), which matches exactly the same text. For `no-control-regex`: replace the control character in the literal with the same character written so the rule does not flag it, while the pattern matches exactly the same text (for example move the control character out of the literal into a string built with `String.fromCharCode` or `new RegExp` from an escaped string, only if eslint accepts that; otherwise the minimal equivalent the rule allows). Do not add `eslint-disable` comments and do not change `eslint.config.*`. Touch only these two files.
3. **Proof of equivalence.** For each rewritten literal, a short check in your deliverables folder (`r45/equivalence_check.mjs`, run with bun) shows the old and the new literal give the SAME result on the same set of strings (at least 4 strings each: matching and not matching), printing `EQUIVALENT <n> strings` or `DIFFERENT <string>`.
4. **Run** both test files and the folder `src/pages/TicketCenter` with `bun test`; and `eslint` on the two files again (0 errors). Record counts.
5. **Commit** inside the portal worktree; record the full sha and `git -C ... diff --stat 4d4dc68cae <commit>` (exactly the two paths); create the LOCAL branch `cand/dell2/anlreq-test-lint-fixes` at it. Never push.
6. **Write `r45/LINT_FIXES_CANDIDATE.json`** in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~284/`: `base_sha`, `commit`, `files_changed`, `tests`, `eslint_before`, `eslint_after`, `claim`, `not_read` (the full-repository `eslint .`, which you do not run in the sparse worktree). Write the three checker scripts named in ACCEPTANCE.
7. **In your report:** the commit, the two errors before and after, and the equivalence output.

### ACCEPTANCE

<criterion id="AR384-y-AC1" cell_refs="AR-y-384"><invocation>python C:/dev/wk-irpt-anlreq-284/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~284/lint_check.py</invocation><expect>^LINT-OK </expect></criterion>
`AR384-y-AC1`: you write `lint_check.py`: it runs eslint on the two files at `cand/dell2/anlreq-test-lint-fixes` in `C:/dev/wk-irpt-anlreq-284/portal` and prints `LINT-OK 0 errors in 2 files` only when eslint reports 0 errors; otherwise `LINT-BAD <why>`, exit 1.

<criterion id="AR384-y-AC2" cell_refs="AR-y-384"><invocation>python C:/dev/wk-irpt-anlreq-284/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~284/tests_check.py</invocation><expect>^TESTS-OK </expect></criterion>
`AR384-y-AC2`: you write `tests_check.py`: it runs `bun test` on the two files and on the folder `src/pages/TicketCenter` in the portal worktree and prints `TESTS-OK <n> passed, 0 failed` only when the folder has 0 failed; otherwise `TESTS-BAD <why>`, exit 1. Its control: it also runs eslint on the same two files at `origin/DEV` (the base) and prints `BASE-HAS-ERRORS <n>` with n at least 2.

<criterion id="AR384-y-AC3" cell_refs="AR-y-384"><invocation>python C:/dev/wk-irpt-anlreq-284/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~284/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR384-y-AC3` (a third check, with a reason: only those two test files may move): you write `scope_check.py`: it prints `SCOPE-OK` only when `git -C C:/dev/wk-irpt-anlreq-284/portal diff --name-only 4d4dc68cae cand/dell2/anlreq-test-lint-fixes` lists exactly `src/pages/TicketCenter/__tests__/filing-hint.test.tsx` and `src/pages/TicketCenter/__tests__/filing-decision-tree.test.tsx`; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR384-y-AC4J" cell_refs="AR-y-384" judgment="true"/>
`AR384-y-AC4J` (judgment, graded at L9, never by you): the two rewritten literals match exactly what the old ones matched; no eslint-disable or config change was used; no assertion changed; nothing was pushed or landed; and the record says plainly what it did not read.

<expected_criteria>AR384-y-AC1 AR384-y-AC2 AR384-y-AC3 AR384-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~284/` and this order's file (status flip only), and INSIDE the portal worktree: the two test files named in the cell. A test or lint error OUTSIDE those: STOP, file a BLOCKING row.
- READ only: everything else. NO push of any branch.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-384</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~284/IRPT_ANLREQ.TO-AR-y-384.two-test-file-lint-errors.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-384`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR384-y-AC1,AR384-y-AC2,AR384-y-AC3,AR384-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a portal candidate branch of two test files; nothing is called, landed or pushed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the two test files' lint errors at origin/DEV against the cell; the lens: a literal rewritten so it matches something else, an eslint-disable comment, a config edit, an assertion loosened to pass, a third file touched. The cell requires equal matching shown on at least 4 strings per literal, no disable or config change, and exactly two files. NOT seen (blind): the full-repository `eslint .`; denominator: 2 literals, 3 checkers, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's message 10314 (the release must build green) with the two lint errors named there. Workstream `ZZ45` of round 43. Base (`origin/DEV` 4d4dc68cae): `r45/` and the candidate branch are absent, so `AR384-y-AC1`, `AC2` and `AC3` FAIL as expected.
- Candidate branch `cand/dell2/anlreq-test-lint-fixes`; test files only (class test-only: no approver). It is separate from `cand/dell2/anlreq-report-ref-revision-string` so the revision fix's approval row stays on the sha the CTO reads; both enter the one PROD release set.
