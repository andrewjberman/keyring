# TO IRPT_ANLREQ.TO-AR-y-252.proxy-placeholder-short -- the proxy input's placeholder is short; the full words stay on the hint line and the title

<to_id>IRPT_ANLREQ.TO-AR-y-252</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~85</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-252` (`decompositions/IRPT_ANLREQ_DECOMP_R22D_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~85`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-85` (branch `wk-IRPT_ANLREQ-85`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~85 <0.9.0_WK_IRPT_ANLREQ~85@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W85-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-252`, inlined) -- THE PROXY PLACEHOLDER. A small CANDIDATE on top of the AR-y-248 portal branch; nothing is landed, pushed or deployed.

*The AR-y-248 candidate (portal branch `wk-IRPT_ANLREQ-81-portal`, commit `1742505086408bc7120e3f36b9e3ced6dfc2fd02`, on dev tip `f6ef1d2548cf6f619f80662d3082d66ea0a3fcf4`) put the whole 163-character hint (`PROXY_HINT`) into the proxy input's `placeholder`; the input is `w-28`, so a person sees a clipped fragment (the worker's row W81-S3). The full words are already on the hint line under "Name a proxy" and on the input's `title`. Fix: the placeholder alone.*

1. **The branch.** In the portal repository (`C:/dev/ajb_workspace/portal`) make a worktree OUTSIDE the product tree on top of the candidate: `git -C C:/dev/ajb_workspace/portal worktree add C:/dev/wk-portal-85 -b wk-IRPT_ANLREQ-85-portal 1742505086408bc7120e3f36b9e3ced6dfc2fd02`. Record `dev_tip` (full sha of `origin/DEV`, read after a permitted `git fetch origin DEV`) and `base_candidate` (the sha above). Never push; commit the way the candidate was made (`git -C C:/dev/ajb_workspace/portal log wk-IRPT_ANLREQ-81-portal`); give the worktree a committer identity on the command line if it has none (row W81-S2). Read the portal's own `CLAUDE.md` and `DESIGN.md` first.
2. **The change.** In `src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx` set the proxy input's `placeholder` to the exported constant `PROXY_PLACEHOLDER = 'Type a ticker'` (new, next to `PROXY_HINT`); keep `title={PROXY_HINT}` and the hint line as they are. Nothing else changes.
3. **The test.** In the existing test file `src/pages/InvestorReporting/tabs/analysis/tests/prospect-suggested-swaps.test.tsx`, ONE new test: the proxy input's `placeholder` equals `PROXY_PLACEHOLDER`, is at most 20 characters, and the hint line still carries `PROXY_HINT` in full. `before_arm`: run it on the candidate WITHOUT your change (it must FAIL). With the change: the whole file and the tab folder pass; `bun run typecheck` rc=0.
4. **Commit** in the portal worktree; record the full sha.
5. **Write `r22/PORTAL_PROXY_PLACEHOLDER_CANDIDATE.json`:** `dev_tip`, `base_candidate`, `branch`, `commit`, `files_changed` (under `src/`), `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm` {`failed`, `output_tail`}, `what_a_person_sees` (the placeholder and the hint line), `design_clauses`, `claim`, `not_read`.
6. **In your report:** the commit, the counts, the words a person sees.

### ACCEPTANCE

<criterion id="AR252-y-AC1" cell_refs="AR-y-252"><invocation>python C:/dev/wk-irpt-anlreq-85/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y252-portal --root C:/dev/wk-irpt-anlreq-85</invocation><expect>Y252-PORTAL-OK</expect></criterion>
`AR252-y-AC1`: the record names a portal commit under `src/` only, built on the AR-y-248 candidate, with one added test that fails on the candidate without the change and passes with it.

<criterion id="AR252-y-AC2J" cell_refs="AR-y-252" judgment="true"/>
`AR252-y-AC2J` (judgment, graded at L9, never by you): only the placeholder changed, the full hint words are still on the hint line and the title, and nothing was landed or pushed.

<expected_criteria>AR252-y-AC1 AR252-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~85/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22D_Y.md</decomp_doc>
<owned_cells>AR-y-252</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~85/IRPT_ANLREQ.TO-AR-y-252.proxy-placeholder-short.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-252`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR252-y-AC1,AR252-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading Andrew's own-test report (rows D2-S77, D2-S78) against the cell; the lens: a test that passes without the change, or a change that fixes the page the worker imagined and not the one Andrew saw. The order requires the new test to FAIL on the DEV tip without the change, and the words a person sees to be stated as rendered. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the AR-y-248 worker's row `W81-S3` and this seat's read of its diff as workstream `YR` round 22. Base: `AR252-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
