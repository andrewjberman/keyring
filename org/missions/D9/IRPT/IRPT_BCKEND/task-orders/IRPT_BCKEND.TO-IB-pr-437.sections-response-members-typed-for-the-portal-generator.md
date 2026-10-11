# TO IRPT_BCKEND.TO-IB-pr-437 -- the sections response schema's members are typed, so the portal's wire generator renders the file

<to_id>IRPT_BCKEND.TO-IB-pr-437</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~295</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>135</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `2.0.0_SA_COO~D2` msg 5188 (a defect of this workstream's own IB-pr-432, drained @8aa28be2a8); the issuer rules a repair inside its own decomposition | **Decomp cell:** `IB-pr-437` (decomposition section 127) | **outcome_ref:** FWD-4

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-295/` (bash `/c/dev/wk-irpt-bckend-295`). Work only there. Its `portal/` folder is a NESTED worktree of
the portal repository at commit `b92696c1ed61` (the portal's DEV head, provisioned for you with linked `node_modules`). No AWS
call, no deploy, no network install, no push of anything.

**The defect.** IB-pr-432 changed `docs/contracts/investor-reporting/v1/responses/analysis-report.response.schema.json` so that
`data` is an `anyOf` of two closed forms (the vendor form and the Opal form). To keep a test's slice working it also listed the
member names under `data.properties` as DESCRIPTION-ONLY schemas (no `$ref`, `type`, `const` or `enum`). The portal's wire
generator refuses an untyped member on purpose. Measured by `2.0.0_SA_COO~D2` at portal `b92696c1`: the generator command
`portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-all.ts` throws

`UNRENDERABLE SCHEMA at responses/analysis-report.response.schema.json#/properties/data/properties/request_ref: no $ref, const, enum or type this generator can render`

and three portal tests are red: IVE98 (the wire folder is generator output), F14-AC13 (every declared route parses) and F57-AC2
(`unprojected_grant` on every route). The same class was fixed once before in this project (commit 35c17fdd07, IB-pr-411: three
members typed). Nothing served is affected.

**Build:**
1. Read how the generator reads a response schema (the `fe-s-13` folder beside `gen-all.ts`, and what it accepts: `$ref`, `const`,
   `enum`, `type`, and whether it renders `anyOf` at `data`). Read commit 35c17fdd07 for the earlier fix's form.
2. Change ONLY that one response schema so every member under `data.properties` (and under each form's `properties`) is typed in a
   way the generator renders AND the two closed forms keep meaning what they mean: the vendor form unchanged; the Opal form by
   `$ref` into the v2 report schema; `additionalProperties: false` on each form. The member-level type at `data.properties` must be
   TRUE of both forms (for example `request_ref` is an object in both; `sections` is an array in both) and must not narrow either.
   Do not retype a v1 or v2 shape; do not copy the v2 schema.
3. Run the portal's generator IN YOUR WORKTREE's `portal/` against your changed schema. Find, from `gen-all.ts` and the tests,
   how it locates the workspace's contract folder (it must read YOUR worktree's `docs/contracts/...`, not the main checkout's;
   prove which file it read: for example run it once on the base schema first and see the UNRENDERABLE error naming
   `request_ref` -- that is your CONTROL, exit code non-zero -- then on your change). Resolve `bun` through the profile (`bun`
   on PATH, or `~/.bun/bin/bun`); do not install anything.
4. The generator REWRITES the portal's wire folder. Those are portal files and belong to `2.0.0_SA_COO~D2`'s lane: do NOT commit
   anything inside `portal/`. List the files it rewrote (`git -C portal status --short`), save the diff as
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~295/IB135-1_portal_wire_regenerated.diff` (it is generated
   contract code, no client data), and run the three named tests in the portal with the regenerated output in place; record each
   one's result line. If a test still fails for a reason that is not this schema, say which line and file a row; do not edit a
   portal test.
5. If the generator cannot render `anyOf` at `data` at all (it throws on the two-form structure itself, whatever the member
   types), STOP: record the exact error and file a row. Do not flatten the two forms into one open form to make it pass: the
   contract's two closed forms are ratified (PRD ADDENDUM v0.28 item 29) and the choice between changing the generator and
   changing the contract's structure is not yours.
6. **Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~295/IB135-1_generator_record.json`:
   `{schema_change_summary, generator:{command, portal_ref, exit_code, ran_on_the_changed_schema, how_the_contract_folder_is_found},
   control_base_schema_exit_code, control_base_schema_error, portal_tests:{"IVE98":{passed, result_line}, "F14-AC13":{...},
   "F57-AC2":{...}}, wire_files_rewritten_by_generator:[...], portal_files_committed_by_this_cell:0, other_untyped_members_found:[...]}`.
   `other_untyped_members_found`: run the generator's same rule over EVERY v1 response schema (the generator does this itself;
   report any other file it refuses) -- a census, so `2.0.0_SA_COO~D2` is not sent back a second time.

<criterion id="IB135-1-AC1" cell_refs="IB-pr-437"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r135/p135_cells.py" . IB135-1-AC1</invocation><expect>IB135-1-AC1 PASS</expect></criterion>
<criterion id="IB135-1-AC2" cell_refs="IB-pr-437"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r135/p135_cells.py" . IB135-1-AC2</invocation><expect>IB135-1-AC2 PASS</expect></criterion>
<criterion id="IB135-1-AC3" cell_refs="IB-pr-437"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r135/p135_cells.py" . IB135-1-AC3</invocation><expect>IB135-1-AC3 PASS</expect></criterion>

<expected_criteria>IB135-1-AC1, IB135-1-AC2, IB135-1-AC3</expected_criteria>

AC1 also re-runs IB-pr-432's four arms (`checks/r130/p130_cells.py . IB130-1-AC1`): the Opal answer and the vendor answer still
validate, the Opal answer with `extraction_validation` and the Opal answer without `computation_validation` are still refused.
AC3 runs `python -m pytest _contracts ops/tests/test_owned_report.py` from `infra/aws/lambda/investor-reporting/`: at base
`2 failed, 235 passed`, the two failures being `analysis-request-original` in `test_seam_paired.py`; after, the same two and no
fewer passed. You may not edit a test.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else: ONE schema file, your deliverables folder, the channel, the order. Nothing in
  `portal/`, no test, no handler, no other schema.
- **Refusal clause:** step 5 above; and if a criterion cannot be met as written, stop, file a row and report. Never weaken a check
  or a test; do not edit `p135_cells.py` or `p130_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W295-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's existing line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~295" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~295@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~295 <0.9.0_WK_IRPT_BCKEND~295@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push. Before the commit, restore the portal worktree to its ref (`git -C portal checkout -- .` after the diff is saved) so no portal change rides anywhere.

<paths>
docs/contracts/investor-reporting/v1/responses/analysis-report.response.schema.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~295/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-437.sections-response-members-typed-for-the-portal-generator.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 127 (round 135, workstream ~P), cell `IB-pr-437`.
<owned_cells>IB-pr-437</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB135-1-AC1, IB135-1-AC2, IB135-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~295/IRPT_BCKEND.TO-IB-pr-437.sections-response-members-typed-for-the-portal-generator.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the schema change in three lines; the control (the generator on the base schema) and the run
on your change, with exit codes; how the generator finds the contract folder; the three tests' result lines; the wire files the
generator rewrote; any other response schema the generator refuses; each criterion's last line; the proof checker's result;
commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; one contract schema file; no handler, route, function or deployed byte. The consumer is named and is the reason for the cell: the portal's wire generator (2.0.0_SA_COO~D2 msg 5188), run by the worker in a provisioned portal worktree as the cell's seam probe against its real neighbour.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p135_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~15:1xZ: AC1 FAIL (the members under data.properties are untyped), AC2 FAIL (no record), AC3 PASS (a bound: 2 failed, 235 passed); commit-gate clean. NOT measured by the issuer: the generator's error (it is 2.0.0_SA_COO~D2's reading), and whether the generator renders anyOf at data; the second is a named stop on the face.
lane: the <paths> block IS the grant. Class WORLD by the L6 floor is not implied by these paths (no infra path); declared WORLD by the issuer's choice because the contract file's consumer is a served page's generator. fanout data: portal_ref: b92696c1ed61 (the nested repository's DEV head at the cut, read by the issuer with ls of origin/DEV after a fetch). ISSUER DEFECT recorded: IB-pr-432's face did not name the portal generator as a reader and its check did not grade member typing; the earlier fix of the same class (35c17fdd07) was not read at that cut.
</preflight>
