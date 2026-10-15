# TO IRPT_DASHBD.TO-DB-f-507 -- ONE TEST for the scalar case (row W506-S1): what the report model prints when a household scalar sits under an account-grain `avs` benchmark member; one test added to the round-117 test file; test only, no source file changes

<to_id>IRPT_DASHBD.TO-DB-f-507</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~507</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>118</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, B-49F round-120 analysis ruling 6 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_120_20261015.md` @5e358b0a8f: "W506-S1 (the scalar `by_row` case is unpinned) goes to `~F2`: one test") | **Rows:** IRPT_DASHBD-D2-W507-S<k> | **Decomp cell:** `DB-f-507` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R118_F.md`) | **outcome_ref:** FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-507` (branch `wk-IRPT_DASHBD-507`); run everything from its root unless a step says the portal. `C:/dev/wk-irpt-dashbd-507/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-507-portal`), cut from `cand/dell2/irpt-default-performance-report` @0d58fe2c43ffad9ca2ffeda422b42681c3494d1c. Do not amend or revert anything already committed there. Portal files commit in the portal repo with plain git and your author line (`0.9.0_WK_IRPT_DASHBD~507 <0.9.0_WK_IRPT_DASHBD~507@opal.agent>`); your folder, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~507/`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. Made-up ids and figures only. All portal paths below are under `portal/src/pages/InvestorReporting/`.

**Why.** Round 117's test file `__tests__/irpt-dashbd/avs-by-row.test.tsx` pins the report model's reading of the sixteen `avs.<window>.benchmark_<kind>` members as `{by_row: {account_id: figure}}` per account. Its worker found one case it could not pin as the order wrote it (row `IRPT_DASHBD-D2-W506-S1`): a plain HOUSEHOLD SCALAR under one of those account-grain members is not a `by_row` map, so `figureCell` (`dashboard/report/reportModel.ts`, about lines 483-500) takes it as the figure and every account's value summary prints that same figure. The contract forbids that input (an account-grain member holds `by_row`; a household scalar under it is a producer defect). The CTO asks for ONE test that pins what happens today, so a change in this behaviour is noticed and the case is no longer unpinned.

**The cell (`DB-f-507`).**
1. **Read first.** `__tests__/irpt-dashbd/avs-by-row.test.tsx` (the fixture builder, how a three-account `FilledReport` is made, how the cells are found), `dashboard/report/reportModel.ts` (`figureCell`, `isByRow`, `valueSummaryGrid`). Its row `W506-S1` is in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`. Run that test file once before any edit (base: 9 tests pass).
2. **ONE new test** in that same file (the only file you change), whose title contains the words `scalar`, `household` and `by_row`: build the round-117 three-account document, replace ONE member (any one of the sixteen) by a plain number (a household scalar, made up), render, and assert what the model does TODAY, found by running it: every account's value summary prints that one figure for that member (the three accounts print the same text). A comment above the test says, in plain words: the contract forbids a scalar under an account-grain member, so this pins the reader's present behaviour on an input the producer must never emit (row D2-S67), and a later reader guard that prints the absent words instead would change this test on purpose. Do NOT change any source file to make the test pass or fail; if what you find differs from "every account prints it", pin what you find and say so in your report.
3. **Gates, once, after your last portal commit:** from the portal worktree `bun run typecheck` and `bun run lint` (0 errors each) and `bun test src/pages/InvestorReporting`: the failing-test names after must be a subset of those before (20 failed at the candidate head). Do not use `test.todo` (this portal's typecheck refuses it).
4. **Record** `BUILD_R118.json` in your folder with exactly: `portal` {`branch` "wk-IRPT_DASHBD-507-portal", `base` "0d58fe2c43ffad9ca2ffeda422b42681c3494d1c", `head`, `files_changed`}, `pinned_behaviour` (one sentence of what the test asserts), `tests` {`avs_pass` (the file's total, 10 when all pass), `suite_before_fail`, `suite_after_fail`}, `typecheck_rc`, `lint_errors`, `pushed` false, `deployed` false.

<criterion id="DBF118-1-AC1" cell_refs="DB-f-507"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r118/p118_scalar.py" . DBF118-1-AC1</invocation><expect>DBF118-1-AC1 PASS</expect></criterion>
`DBF118-1-AC1` -- `avs-by-row.test.tsx` carries titles with the seven words `by_row`, `account`, `benchmark`, `absent`, `household`, `window` and `scalar`, and `bun test` on it passes with 0 failures and at least 10 tests. Base: FAIL (the word `scalar` is absent from the titles, and the file has 9 tests).
<criterion id="DBF118-1-AC2" cell_refs="DB-f-507"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r118/p118_scalar.py" . DBF118-1-AC2</invocation><expect>DBF118-1-AC2 PASS</expect></criterion>
`DBF118-1-AC2` -- bounds: the portal diff from the candidate head `0d58fe2c` to your head is that one test file and nothing else. Base: FAIL (no change).

<expected_criteria>DBF118-1-AC1,DBF118-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every source file (including `reportModel.ts`), every other test, the contract, the issuer's check.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. Never edit a source file.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W507-S<k>` (D2 is the device coordinate), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~507/
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/avs-by-row.test.tsx
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-507.one-test-a-household-scalar-under-an-avs-benchmark-member.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R118_F.md</decomp_doc> round 118, workstream ~F2 (F-SHIP), cell `DB-f-507`.
<owned_cells>DB-f-507</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF118-1-AC1, DBF118-1-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~507/IRPT_DASHBD.TO-DB-f-507.one-test-a-household-scalar-under-an-avs-benchmark-member.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF118-1-AC1,DBF118-1-AC2` BEFORE the flip (one comma-separated argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the portal head sha; what the test pins; the test counts and the typecheck and lint results; anything off-task (as row ids). Made-up values only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one test added on a local portal branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF118-1-AC1 and AC2 FAIL at base and the checker's pure helpers are exercised by its self-test (8 arms).
lane: the <paths> block IS the grant.
</preflight>
