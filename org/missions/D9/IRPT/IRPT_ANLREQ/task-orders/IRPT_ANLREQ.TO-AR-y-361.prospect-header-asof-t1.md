# TO IRPT_ANLREQ.TO-AR-y-361.prospect-header-asof-t1 -- C-PRICES (PRD v0.16): the prospect composer hands the header card the as-of "T-1 close" and not null, so the card states the as-of instead of "not supplied"; one line of source and one test, on the AR-y-360 candidate

<to_id>IRPT_ANLREQ.TO-AR-y-361</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~158</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZZ22</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (a client-facing portal page; the worker lands and pushes NOTHING)
**Decomp cell:** `AR-y-361` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-7 (C-PRICES) | **depends_on:** `AR-y-360` (merged `7ac19bb2fc`; candidate `cand/dell2/anlreq-no-price-date-t1` @ `c22f4508`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~158`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-158` (branch `wk-IRPT_ANLREQ-158`), with a portal worktree `C:/dev/wk-irpt-anlreq-158/portal` (branch `wk-IRPT_ANLREQ-158-portal`) provisioned by the issuer AT the candidate commit `c22f4508`. Commit the WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~158 <0.9.0_WK_IRPT_ANLREQ~158@opal.agent>" -F <msgfile> -- <paths>`; the PORTAL source is committed INSIDE the portal worktree (`git -C C:/dev/wk-irpt-anlreq-158/portal ...`).
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W158-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal`: never commit it to the WORKSPACE repository. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH of any branch, no deploy, no upload. No non-ASCII in what you add. Run the proof-of-spec check with THIS worktree's own `.tools/proof-of-spec-check.py` from inside it. Scratch outside the product tree. Your worktree is SPARSE: the folder runs of other cells fail on absent paths at the base too; you run ONLY the new test file and the one file named below.

### THE CELL (`AR-y-361`, inlined)

*Context. AR-y-360 removed the price-date input from `portal/src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx`; its `onProspectReviewed({ ..., asOf: null, total: null })` call (about line 213 to 217) now always hands the header card a null as-of, and `src/pages/InvestorReporting/header/IdentityCard.tsx` (about line 505) renders a prospect's `asOf ?? 'not supplied'` as a literal string. PRD v0.16 C-PRICES says every price is the T-1 close, STATED as the as-of: the card must say so, not 'not supplied'. The Ticket Center, `prospect.ts` and `IdentityCard.tsx` stay untouched.*

1. In `ProspectComposer.tsx` change the `asOf` handed to `onProspectReviewed` from `null` to the constant string `'T-1 close'` (a named module constant `PROSPECT_AS_OF = 'T-1 close'`, no other wording); nothing else in the file changes.
2. In the EXISTING test file `src/pages/InvestorReporting/tabs/analysis/tests/prospect-no-price-date.test.tsx` add ONE case (g), named `the header card is handed the as-of "T-1 close" and not null`, asserting the value handed to `onProspectReviewed` (through the existing fakes) has `asOf` equal to `'T-1 close'`. Re-pin any test of the new file or of `src/pages/InvestorReporting/__tests__/dsgn-irptv1/s55.component-wiring.test.tsx` that pins `asOf: null`, case by case, never deleted. `before_arm`: case (g) FAILS on the AR-y-360 candidate without the source change.
3. Commit in the portal worktree, record the full sha and `git diff --stat c22f4508 <commit>` (exactly the paths you touched), create the LOCAL branch `cand/dell2/anlreq-no-price-date-t1-asof` at your commit (never push).
4. Write `r41/ASOF_CANDIDATE.json` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~158/`: `base_candidate_sha`, `commit`, `files_changed`, `tests` {`passed`, `failed`}, `before_arm`, `repinned`, `what_a_person_sees` (in words: the card's as-of line reads `T-1 close` for a prospect), `not_read` (the rendered page).
5. Write the three checker scripts named in ACCEPTANCE into your deliverable folder.
6. In your report: the commit, the counts, the before-arm failure, every re-pinned case.

### ACCEPTANCE

<criterion id="AR361-y-AC1" cell_refs="AR-y-361"><invocation>python C:/dev/wk-irpt-anlreq-158/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~158/asof_check.py</invocation><expect>^ASOF-TESTS-OK </expect></criterion>
`AR361-y-AC1`: you write `asof_check.py`: it runs `bun test src/pages/InvestorReporting/tabs/analysis/tests/prospect-no-price-date.test.tsx` and `bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/s55.component-wiring.test.tsx` in `C:/dev/wk-irpt-anlreq-158/portal` and prints `ASOF-TESTS-OK <n> passed, 0 failed` only when both files report 0 fail and the first file runs 7 cases (a) to (g); otherwise `ASOF-TESTS-BAD <why>`, exit 1.

<criterion id="AR361-y-AC2" cell_refs="AR-y-361"><invocation>python C:/dev/wk-irpt-anlreq-158/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~158/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR361-y-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `ProspectComposer.tsx` to a scratch folder OUTSIDE the product tree with the as-of put back to `null`, runs the new test file against the copy, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR361-y-AC3" cell_refs="AR-y-361"><invocation>python C:/dev/wk-irpt-anlreq-158/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~158/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR361-y-AC3` (a third check, with a reason: a client-facing page, the scope is what the approver reads): you write `scope_check.py`: it prints `SCOPE-OK` only when `git -C C:/dev/wk-irpt-anlreq-158/portal diff --name-only c22f4508 cand/dell2/anlreq-no-price-date-t1-asof` lists only `src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx` and test files under `src/pages/InvestorReporting/tabs/analysis/tests/` or `src/pages/InvestorReporting/__tests__/dsgn-irptv1/`, and `git diff c22f4508 cand/dell2/anlreq-no-price-date-t1-asof -- src/api src/pages/TicketCenter src/pages/InvestorReporting/header src/pages/InvestorReporting/tabs/analysis/prospect.ts` is empty; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR361-y-AC4J" cell_refs="AR-y-361" judgment="true"/>
`AR361-y-AC4J` (judgment, graded at L9, never by you): the as-of handed to the header is exactly `T-1 close`, nothing else of the composer changed, the header card and Ticket Center are untouched, and nothing was pushed or landed.

<expected_criteria>AR361-y-AC1 AR361-y-AC2 AR361-y-AC3 AR361-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~158/` and this order's file (status flip only), and INSIDE the portal worktree: `src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx`, `src/pages/InvestorReporting/tabs/analysis/tests/prospect-no-price-date.test.tsx` and `src/pages/InvestorReporting/__tests__/dsgn-irptv1/s55.component-wiring.test.tsx` (re-pin only). A test OUTSIDE the grant that fails because of your change: STOP, file a BLOCKING row.
- READ only: everything else. NO push of any branch.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-361</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~158/IRPT_ANLREQ.TO-AR-y-361.prospect-header-asof-t1.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-361`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR361-y-AC1,AR361-y-AC2,AR361-y-AC3,AR361-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading W157-S5 and IdentityCard.tsx line 505 against the cell; the lens: another string than the T-1 wording, the header card edited instead of the composer, a null left on some branch of the composer, a re-pinned test weakened into a pass. The cell requires the exact constant, one new case, the card untouched, and a mutant that fails. NOT seen (blind): the rendered card; denominator: 7 test cases, 1 source file, 3 criteria files, 4 criteria.
</preflight>

---

## RECORD FACE

- Cut on the issuer's read of W157-S5 (a null as-of renders 'not supplied' on a prospect card, against C-PRICES). Workstream `ZZ22` of round 40. Base: `AR361-y-AC1`, `AC2` and `AC3` FAIL as expected (no checker files).
- Stacks on the AR-y-360 candidate; the two candidates ship together or not at all, only after r32 and on Andrew's word.
