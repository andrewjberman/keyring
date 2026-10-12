# TO IRPT_BCKEND.TO-IB-pr-481 -- BUILD ONLY: the two `PerformanceReport.schema.json` copies return to their bytes at c16bf9d7bb^ (the frozen v1 contract does not move)

<to_id>IRPT_BCKEND.TO-IB-pr-481</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~336</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>167</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6517 (PRD ADDENDUM v0.51 @54c4366a1c, section 1 and section 2 item 1; row IRPT_BCKEND-D2-W334-S2) | **Decomp cell:** `IB-pr-481` (decomposition section 159) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-336/` (bash `/c/dev/wk-irpt-bckend-336`). Work only there; `git rev-parse HEAD` before your first commit is `base_commit` (state it).

**HARD BOUNDS.** BUILD ONLY. No AWS call, nothing deployed. You edit only the two schema files named below.

**Why.** IB-pr-479 (merged at `c16bf9d7bb`) declared `start_value` and `end_value` in both copies of `PerformanceReport.schema.json`, as PRD v0.50 ordered. The docs copy, `docs/contracts/investor-reporting/v1/PerformanceReport.schema.json`, is IMMUTABLE since IB-rt-1 ("v1 IS FROZEN AT THIS FLIP",
`infra/aws/lambda/investor-reporting/PATH_MANIFEST.json` line 5730, per the CTO's addendum), and `infra/aws/lambda/ci/lambda-source-map.json` pins its sha256. The CTO's PRD ADDENDUM v0.51 (line 1342 of `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`; read section 1) WITHDRAWS v0.50's schema order: a published frozen contract does not move, even additively.
`value_facts` is an open object in v1, so an instance carrying the two members already validates. Both copies return to their bytes at the parent of that merge.

**Build (one thing).** Restore both files to exactly their content at `c16bf9d7bb^` (use `git show c16bf9d7bb^:<path>`; write the bytes, LF, no re-serialising by a JSON library):
- `docs/contracts/investor-reporting/v1/PerformanceReport.schema.json` -> sha256 `c4e2fdb122f0da2821fff846591d047463d9669117179ed7411a6e4ab3041f0f`
- `infra/aws/lambda/investor-reporting/_contracts/PerformanceReport.schema.json` -> sha256 `195c345fc2d13077f0a117bf257fc55fed31359d5998e05d78467896eef1cb81`
Print each hash after the restore. Then read `infra/aws/lambda/ci/lambda-source-map.json` for the pin of the docs copy and show, in the record, that the restored docs copy hashes to that pin (cite the line). Edit NO other file: the fixtures, the tests and the source map stay as they are.

**Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~336/IB167-1_revert_record.json`: `{base_commit, docs_copy_sha256, contracts_copy_sha256, docs_copy_equals_source_map_pin: true, source_map_pin_cite: "infra/aws/lambda/ci/lambda-source-map.json:<line>", files_changed:[the two paths], contracts_suite:{before, after}, note_on_round_166_check: "IB166-4-AC2 demands the two members and now FAILs by the CTO's order; it is superseded by this order"}`.

<criterion id="IB167-1-AC1" cell_refs="IB-pr-481"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-1-AC1</invocation><expect>IB167-1-AC1 PASS</expect></criterion>
<criterion id="IB167-1-AC2" cell_refs="IB-pr-481"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-1-AC2</invocation><expect>IB167-1-AC2 PASS</expect></criterion>
<criterion id="IB167-1-AC3" cell_refs="IB-pr-481"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-1-AC3</invocation><expect>IB167-1-AC3 PASS</expect></criterion>

<expected_criteria>IB167-1-AC1, IB167-1-AC2, IB167-1-AC3</expected_criteria>

What the checks grade: AC1 both schema files at `HEAD` (and in the working tree) hash to the frozen values above; AC2 the regression guard (it PASSes at base BY DESIGN): the `_contracts` suite reads `203 passed, 2 failed`, the two failures being `test_every_declared_route_has_a_response_contract_whose_refs_resolve` and
`test_control_a_known_good_document_conforms_and_a_known_bad_one_does_not[analysis-request-original]`, not yours; AC3 the record's form, the pin cite resolves, and nothing but the two schema files (and your deliverables, rows and order) changed.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else.
- **Refusal clause:** a hash that does not match after the restore, or a `_contracts` failure beyond the two known: file a row and report. Never weaken a check; do not edit `p167_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W336-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~336" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~336@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~336 <0.9.0_WK_IRPT_BCKEND~336@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
docs/contracts/investor-reporting/v1/PerformanceReport.schema.json
infra/aws/lambda/investor-reporting/_contracts/PerformanceReport.schema.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~336/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-481.frozen-v1-schema-copies-restored.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 159 (round 167, workstream ~P), cell `IB-pr-481`.
<owned_cells>IB-pr-481</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB167-1-AC1, IB167-1-AC2, IB167-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~336/IRPT_BCKEND.TO-IB-pr-481.frozen-v1-schema-copies-restored.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; the two hashes after the restore; the source-map pin line; the `_contracts` suite's last line before and after; each criterion's last line; the proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell restores two contract files to their earlier bytes in the repo; nothing is built, deployed or invoked.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p167_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~20:3xZ: IB167-1 AC1 FAIL (the docs copy hashes 69982a18..., not the frozen c4e2fdb1...), AC2 PASS (the regression guard: _contracts 203 passed, 2 failed, the two known), AC3 FAIL (no record); commit-gate clean. The issuer measured at c16bf9d7bb^: the docs copy's bytes hash c4e2fdb122f0..., the _contracts copy's 195c345fc2d1..., equal to the CTO's values (git show, sha256sum).
lane: the <paths> block IS the grant. Class WORLD by the L6 floor (an infra path); nothing is deployed.
</preflight>
