# TO IRPT_ANLREQ.TO-AR-y-279.commentary-requested-only-when-true -- the form sends commentary_requested only when it is true, and a test names the order with IB-pr-456

<to_id>IRPT_ANLREQ.TO-AR-y-279</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~100</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-279` (`decompositions/IRPT_ANLREQ_DECOMP_R23B_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~100`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-100` (branch `wk-IRPT_ANLREQ-100`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~100 <0.9.0_WK_IRPT_ANLREQ~100@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W100-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-279`, inlined) -- AR-y-264 AMENDED BY THE CTO'S HOLD. A small CANDIDATE on top of the AR-y-264 portal branch; nothing is landed, pushed or deployed.

*The CTO (msg 7201) HELD the AR-y-264 candidate (`wk-IRPT_ANLREQ-89-portal`, commit `972c7dabc320ac4ee2e5a4e18459ff61a3bdba51`): it sends `commentary_requested` on EVERY submission, `false` included. Until IRPT_BCKEND's IB-pr-456 (the acceptance release that carries the member) is live, the live acceptance refuses that member as `UNKNOWN_OR_SERVER_OWNED_FIELD`, so every analysis filing would fail. The CTO's words: 'It lands only after P2 reports IB-pr-456 live; add a test that names that order. Optional hardening: send the member only when true.' This cell does the hardening and the test; the landing order stays the CTO's.*

1. **The branch.** In the portal repository (`C:/dev/ajb_workspace/portal`) make a worktree OUTSIDE the product tree on top of the held candidate: `git -C C:/dev/ajb_workspace/portal worktree add C:/dev/wk-portal-100 -b wk-IRPT_ANLREQ-100-portal 972c7dabc320ac4ee2e5a4e18459ff61a3bdba51`. Record `base_candidate` (that sha) and `dev_tip` (full sha of `origin/DEV` after a permitted `git fetch origin DEV`). Never push; commit the way the candidate was made (`git -C C:/dev/ajb_workspace/portal log wk-IRPT_ANLREQ-89-portal`); give the worktree a committer identity on the command line if it has none. Read the held candidate's record first: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~89/r22/PORTAL_FORM_COMMENTARY_CANDIDATE.json` (the trace: `analysisBody` and `submissionBody` in `src/pages/TicketCenter/analysisRequest.ts` set the member; `contracts/submission-request.ts` is the closed reader).
2. **The change.** The submission body carries `commentary_requested: true` ONLY when the box is checked; when it is unchecked the member is ABSENT from the body (not `false`). The ticket answer keeps `add_commentary` as it is. Touch `src/` only.
3. **The tests.** In the existing test file for the candidate (or beside it): (a) checked: the submission body has `commentary_requested === true`; (b) unchecked: the submission body has NO `commentary_requested` key at all (`'commentary_requested' in body` is false) and the answers still carry `add_commentary: false`; (c) a test whose NAME states the order: `commentary_requested is sent only when true, so a filing without commentary is accepted before IB-pr-456 is live; a filing WITH commentary needs IB-pr-456 live first` and asserts (a) and (b) together; (d) the ticket POST body is unchanged by the checkbox except for `add_commentary`. `before_arm`: run the new tests on the held candidate WITHOUT your change: (b) FAILS. With the change all pass; the whole TicketCenter folder (counts); `bun run typecheck` rc=0; known `dsgn-irptv1` failures with counts both ways. Edit an existing assertion ONLY where it pinned `commentary_requested: false` on an unchecked box (list each).
4. **Commit** in the portal worktree; record the full sha.
5. **Write `r23/PORTAL_COMMENTARY_ONLY_WHEN_TRUE_CANDIDATE.json`:** `dev_tip`, `base_candidate`, `branch`, `commit`, `files_changed` (under `src/`), `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm` {`failed`, `output_tail`}, `what_a_person_sees` (an unchecked filing: the body words; a checked filing), `design_clauses`, `claim`, `not_read` (the live acceptance, IB-pr-456's release state).
6. **In your report:** the commit, the counts, the two body shapes.

### ACCEPTANCE

<criterion id="AR279-y-AC1" cell_refs="AR-y-279"><invocation>python C:/dev/wk-irpt-anlreq-100/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y279-portal --root C:/dev/wk-irpt-anlreq-100</invocation><expect>Y279-PORTAL-OK</expect></criterion>
`AR279-y-AC1`: the record names a portal commit under `src/` only, built on the held AR-y-264 candidate, with added tests that fail on the held candidate without the change (the unchecked body has no member) and pass with it, including the test whose name states the IB-pr-456 order.

<criterion id="AR279-y-AC2J" cell_refs="AR-y-279" judgment="true"/>
`AR279-y-AC2J` (judgment, graded at L9, never by you): an unchecked box leaves `commentary_requested` out of the body entirely, a checked box sends true, the test names the IB-pr-456 order, the answers still carry `add_commentary`, and nothing was landed or pushed.

<expected_criteria>AR279-y-AC1 AR279-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~100/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23B_Y.md</decomp_doc>
<owned_cells>AR-y-279</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~100/IRPT_ANLREQ.TO-AR-y-279.commentary-requested-only-when-true.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-279`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR279-y-AC1,AR279-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's hold (msg 7201) and the held candidate's trace against the cell; the lens: a body that still carries the member when unchecked, a test that passes on the held candidate unchanged, a landing order left unstated. The order requires the new test to FAIL on the DEV tip without the change, and the words a person sees to be stated as rendered. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's hold of the AR-y-264 candidate (msg 7201: it sends commentary_requested on every submission; the live acceptance refuses the member until IB-pr-456 is live). Workstream `Y` round 24. The landing order (only after `~P2` reports IB-pr-456 live) is the CTO's. Base: `AR279-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
