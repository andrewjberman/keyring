# TO IRPT_BCKEND.TO-IB-pr-504 -- the frozen export envelope carries `facts.covered_account_ids` and the `fe-s-18` generator reproduces it (row D2-W353-S5)

<to_id>IRPT_BCKEND.TO-IB-pr-504</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~355</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>173</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO ROUND-173 ANALYSIS (msg 6798) section 1 (row D2-W353-S5) and section 2 item 1 | **Decomp cell:** `IB-pr-504` (decomposition section 165) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-504` (inlined):** the committed frozen map `portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json` holds an export envelope under the key `/api/scoped/investor-reporting/export/` whose `data.facts` lacks `covered_account_ids`, while the v1 contract `docs/contracts/investor-reporting/v1/ExportReceipt.schema.json` lists it in `/properties/facts` `required`, the wire fixture `fixtures/smoke/fe-s-13-wire.json` carries it (`["ACCT-1"]`, synthetic) and the portal's `ExportReceipt` type declares it required. The CTO ruled: **the FIXTURE moves**. The committed envelope gains the member (synthetic ids only), is validated against the v1 schema in the same cell, and the generator then reproduces the committed bytes. Round 172's repair of `fe-s-18/gen-fixtures.ts` deliberately DROPS the member (`exportEnvelope()` deletes `facts.covered_account_ids`) because the committed bytes then omitted it; that drop is now the defect. You work in the PORTAL repo (your worktree's `portal/` directory, `node_modules` linked, `bun` on PATH). This is a candidate for portal DEV. Your worktree's portal repo starts at a commit that does NOT yet carry round 172's generator repair (it is on the branch `wk-IRPT_BCKEND-353-portal` at `e1cd356e2f`): FIRST run `git -C portal merge --ff-only e1cd356e2f` (it is in the same object store; if it is not a fast-forward, STOP and file a row), then work on top of it.

**Do:**
1. In `fe-s-18/gen-fixtures.ts` make `exportEnvelope()` KEEP the wire's `facts.covered_account_ids` (stop deleting it); change nothing else in the generator unless a run shows another difference.
2. Regenerate: run `bun run src/pages/InvestorReporting/__tests__/fe-s-18/gen-fixtures.ts` from `portal/` so that `fixtures/smoke/fe-s-18-frozen.json` gains exactly that member (the only expected change in the output; the diff of the frozen map against its base must be that one added list). If the run changes any other line of any output, STOP and file a row.
3. Validate the frozen envelope's `data` against `docs/contracts/investor-reporting/v1/ExportReceipt.schema.json` (Draft 2020-12 `jsonschema`) in your own run and print the result; the ids must be the wire fixture's synthetic list, none invented.
4. Keep each file's EXISTING line endings (compare with `git diff --ignore-cr-at-eol`); do not mass-convert; do not edit a fixture by hand (the generator writes it).
5. Find any portal test that asserts the member is ABSENT from the frozen export envelope or counts its facts; if one fails because of this change, STOP and file a row naming it (do not edit it: it is outside the grant).
6. Commit the portal change BEFORE you run the criterion that runs the generator (it checks for a clean tree).

**Criteria (run each under `timeout 120` from your WORKSPACE root, the parent of `portal/`, record the output and exit code verbatim):**

<criterion id="IB173-2-AC1" cell_refs="IB-pr-504"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r173/p173_cells.py" . IB173-2-AC1</invocation><expect>IB173-2-AC1 PASS</expect></criterion>
<criterion id="IB173-2-AC2" cell_refs="IB-pr-504"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r173/p173_cells.py" . IB173-2-AC2</invocation><expect>IB173-2-AC2 PASS</expect></criterion>
<criterion id="IB173-2-AC3" cell_refs="IB-pr-504"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r173/p173_cells.py" . IB173-2-AC3</invocation><expect>IB173-2-AC3 PASS</expect></criterion>

<expected_criteria>IB173-2-AC1, IB173-2-AC2, IB173-2-AC3</expected_criteria>

What the checks grade: AC1 the check RUNS the `fe-s-18` generator and then `git diff --ignore-cr-at-eol --stat` over the smoke, fe-s-16 and fe-s-32 fixture folders must be EMPTY; AC2 the six portal tests that consume the fe-s-18 maps pass (28 or more pass, none fail); AC3 the frozen export envelope's `data` validates against the v1 `ExportReceipt` schema and its `covered_account_ids` equal the wire fixture's list. Do not edit the checks. Run `bun test src/pages/InvestorReporting` ONCE at the end and report its counts against your base run (the base is 1213 pass, 27 skip, 4 fail; the four are pre-existing).

## BOUNDS

- **Grant:** the `paths` block and nothing else. Portal repo: only `src/pages/InvestorReporting/__tests__/fe-s-18/gen-fixtures.ts` and `src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json`. No other fixture, no test, no product code, no `package.json` or lockfile; run no `bun install`; push nothing.
- **Refusal clause:** STOP, file a row, change nothing more, if the regeneration changes any line of any output other than the one added list, if the v1 schema rejects the envelope for any reason other than the missing member, or if a portal test fails because of the change.
- **Commit** in BOTH repos per your definition: the workspace commit (order flip, proof, rows) with `.tools/safe-commit.sh`, and the portal commit with plain `git -C portal commit` (same author and committer values, message file from the Write tool outside the worktree); ASCII only; never stage the workspace's `portal` gitlink.
- **Row ids** are `IRPT_BCKEND-D2-W355-S<k>` (the next free `k`). Report once, under 150 words.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-18/gen-fixtures.ts
portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~355/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-504.frozen-export-envelope-carries-covered-account-ids.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 165 (round 173, workstream ~P), cell `IB-pr-504`.
<owned_cells>IB-pr-504</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB173-2-AC1, IB173-2-AC2, IB173-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~355/IRPT_BCKEND.TO-IB-pr-504.frozen-export-envelope-carries-covered-account-ids.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one fixture and its test-folder generator of one portal page; no product file, no served artifact; the candidate lands on portal DEV through the CTO review lane (PROD rides the held promote `dell1-e7f2`).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p173_cells.py dry-run at base on dell2 2026-10-13 ~05:1xZ: IB173-2 AC3 FAIL ("'covered_account_ids' is a required property"); AC2 reads PASS at the base (a regression guard); AC1 (running the generator) fails at the portal DEV base (the generator throws) and is dry-run in a throwaway worktree. Positive control: the same AC3 reads PASS on the frozen map with the member added (temporary edit, restored).
lane: the paths block IS the grant; worker slot ~355 of IRPT_BCKEND, a portal worktree pair. Class LOCAL.
</preflight>
