# TO IRPT_ANLREQ.TO-AR-y-151 -- the portal's vendored wire type declares commentary_requested (generated; sent by nothing)

<to_id>IRPT_ANLREQ.TO-AR-y-151</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>15</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (generated type files on a portal candidate branch; nothing is pushed, deployed or called live)
**Decomp cell:** `AR-y-151` (`decompositions/IRPT_ANLREQ_DECOMP_R15_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none
**DIRECT ACT:** one cell, small, LOCAL; its close is the issuer's one real run of the suite on the candidate's head.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`.
- **Workspace worktree:** `C:/dev/wk-irpt-anlreq-51` (branch `wk-IRPT_ANLREQ-51`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~51 <0.9.0_WK_IRPT_ANLREQ~51@opal.agent>" -F <msgfile> -- <paths>`.
- **Portal worktree:** `C:/dev/wk-irpt-anlreq-51/portal`, branch `wk-IRPT_ANLREQ-51-portal-r15`, cut from portal DEV `1221f7644c`
  (confirm with `git rev-parse --abbrev-ref HEAD` before you edit). Commit there with
  `git -c user.name=0.9.0_WK_IRPT_ANLREQ~51 -c user.email=0.9.0_WK_IRPT_ANLREQ~51@opal.agent commit -F <msgfile> -- <files>`. Never push.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W51-S<k>`. The workspace worktree shows ` M portal`: never commit it. Never run `bun install` (the issuer has
  installed this worktree's dependencies from the frozen lockfile; `git status` in the portal is clean of tracked changes).

### THE CELL (`AR-y-151`, inlined)

*The portal's generated wire type for the analysis submission request declares the optional `commentary_requested`. Nothing sends it.*

Why. The workspace contract the portal vendors, `docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json` (in the
WORKSPACE worktree above the portal), gained an optional boolean member `commentary_requested`. The portal's generated copy,
`src/pages/InvestorReporting/contracts/wire/AnalysisSubmissionRequest.ts`, was not regenerated. Two tests compare the two and fail
on every portal head (`iv-e-26` wire-regen and `iv-e-98` generators-drift, under
`src/pages/InvestorReporting/__tests__/`). At this base the Investor Reporting suite reads 1189 pass, 2 fail.

1. Read the generator before you run it: `src/pages/InvestorReporting/__tests__/fe-s-13/gen-all.ts` (and `gen-wire.ts` beside it):
   what it reads (the workspace contract documents, by which path) and which files it writes.
2. Run it exactly: `bun run src/pages/InvestorReporting/__tests__/fe-s-13/gen-all.ts` from the portal worktree.
3. `git status --short` and `git diff --stat`: list EVERY file it changed. Commit EXACTLY what the generator wrote and nothing
   else. NEVER hand-edit a generated file, the generator or a test. If it changes any file OUTSIDE
   `src/pages/InvestorReporting/contracts/wire/`, do not commit that file: list it, say why the generator touched it, and file a
   row (a generated file elsewhere may belong to another lane's open work).
4. If the diff holds anything other than the one new optional member on the one type (another member appearing, a member
   disappearing, a reordering, another type changing), STOP before committing, list every other change, and file a row: the
   contract has moved further than this order knows.
5. **Nothing sends the member.** Do not add it to any request builder, form, fixture or hand-written type. After your commit,
   outside `contracts/wire/` and the tests, the string `commentary_requested` appears in NO file under `src` (the check counts it).
6. In your report: the generator's inputs and outputs; the exact diff of the wire file (the added lines); `bun run typecheck`;
   the eslint error-count line for the changed files (`bun x eslint <files>`); `git diff --stat origin/DEV HEAD`.

### ACCEPTANCE

<criterion id="AR151-y-AC1" cell_refs="AR-y-151"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r15/ar15_checks.py y151-wire --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y151-WIRE-OK</expect></criterion>
`AR151-y-AC1`: the wire type declares the member, no file outside the generated wire folder and the tests names it, and the whole
Investor Reporting suite passes with 0 failing and 0 errors.

<criterion id="AR151-y-AC2" cell_refs="AR-y-151"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r15/ar15_checks.py y151-keep --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y151-KEEP-OK</expect></criterion>
`AR151-y-AC2`: the difference control -- the TicketCenter test folder passes (67 at the base).

<expected_criteria>AR151-y-AC1 AR151-y-AC2</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's
  file (status flip only). In the portal: ONLY files the generator writes under `src/pages/InvestorReporting/contracts/wire/`.
- READ only: everything else. No live call, no push, no deploy. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R15_Y.md</decomp_doc>
<owned_cells>AR-y-151</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR151-y-AC1 AR151-y-AC2. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-151.wire-type-commentary-requested.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-151`. Artifact rows use a `kind` the schema admits. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR151-y-AC1,AR151-y-AC2`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 1 row (DSGN_IRPTV1-D2-W65-S1: the one command and the one file it rewrites) and 1 base run of the Investor Reporting suite in this worktree (1189 pass, 2 fail, 0 error); NOT seen: the generator's full output set (the worker lists every file it changes before committing). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or called; a type gains an optional member that 0 callers send. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers. comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission change
comp-adversary: RUN -- by reading 1 ruling (CTO msg 6019: declared and sent by nothing) against the face; the lens: the member reaching a request builder and being SENT before the service admits it, which refuses every filing. The check counts files outside the wire folder and the tests that name the member and requires 0. NOT seen: whether the generator also rewrites a file another lane has open.
lane: the generated wire folder, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on CTO msg 6019 as round 15's single cell, DIRECT ACT. `AR151-y-AC1` base: FAIL as expected (the member absent; the suite
  reads 2 failing). `AR151-y-AC2` base: PASS as expected (67 pass).
- The issuer installed this worktree's portal dependencies from the frozen lockfile before the cut (9 packages, no tracked file
  changed): the suite here errored on a module the worktree lacked, which is why earlier whole-suite runs in this worktree read
  failures DEV does not have.
- After the drain: the issuer runs the whole portal suite on the candidate's head and sends it to the CTO with typecheck and eslint.
- Seating: slot ~51 is reused; its earlier orders are terminal.
