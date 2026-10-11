# TO IRPT_BCKEND.TO-IB-pr-430 -- the four closed v1 response schemas that omit `unprojected_grant` declare it, as the other 17 do; and two thin producer fixtures are re-made by their handlers

<to_id>IRPT_BCKEND.TO-IB-pr-430</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~289</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>128</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msgs 4858 and 4865 (rulings on this seat's msg 4856 and on `2.0.0_SA_COO~D2` msg 4863; row IRPT_BCKEND-D2-W287-S1) | **Decomp cell:** `IB-pr-430` (decomposition section 121) | **outcome_ref:** FWD-2

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-289/` (bash `/c/dev/wk-irpt-bckend-289`). Work only there. No AWS call, no deploy, no handler edit.

**The defect.** `infra/aws/lambda/investor-reporting/_authz/served.py:403` `response_envelope` adds the top-level member
`unprojected_grant` to EVERY served answer, by an earlier CTO ruling (non-optional, present at zero). Of the 21 response schemas in
`docs/contracts/investor-reporting/v1/responses/`, 17 declare it: one identical declaration, listed in `required` (measured by the
issuer). Four are closed (`additionalProperties: false`) and omit it, so on those routes the handler's own answer fails its own
contract:

`analysis-request-pdf`, `comparison-catalogue`, `custody-report-persist`, `custody-report-read`
(each file is `<name>.response.schema.json`).

The CTO ruled: the contract is the side out of step; the four gain the member. The portal's envelope parser already requires it, so no
reader breaks.

**Build:**
1. In each of the four schema files, add `unprojected_grant` to `properties` with the SAME declaration the other 17 carry (copy it
   from one of them byte for byte as JSON; do not retype it) and add it to `required`. Keep `additionalProperties: false`. Change
   nothing else in those files: not `data`, not `status`, not the `x-` annotations, not key order beyond the insertion.
2. **What the change makes false, and only that.** Find every fixture and test under
   `infra/aws/lambda/investor-reporting/_contracts/` that holds a whole RESPONSE ENVELOPE for one of the four routes (for example
   `fixtures/custody-report-read.response.valid.json` and its `persist` sibling) and that the new `required` member now fails. Add the
   member to the VALID fixtures in the form the handler emits at zero (read `response_envelope` for it; do not invent a shape). A
   fixture that is meant to be invalid stays invalid for its own reason. Do not edit a test's assertion to make it pass; if a test
   asserts the member is ABSENT, stop and file a row.
3. **Run** `python -m pytest _contracts -q -p no:cacheprovider -rf` from `infra/aws/lambda/investor-reporting/`. At base it reads
   `2 failed, 203 passed`; both failures are `analysis-request-original` (owned by IRPT_ANLREQ) and are not yours. After your change
   the same two and no other may fail.
4. **Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~289/IB128-1_schema_member_record.json`:
   `{declaration_copied_from, files_changed:[...], routes:[{operation, with_member_validates, without_member_refused,
   foreign_member_refused, invocation}], packaged_in_functions:[...], suite_before, suite_after}`. For each of the four routes,
   validate three envelopes against the changed schema with `jsonschema` and a `referencing` registry over the v1 schema files (reuse
   `validate_against_response_contract` from `_contracts/tests/test_seam_paired.py` if you can import it): (a) the route's valid
   envelope WITH the member validates; (b) the same envelope with the member removed is refused; (c) the valid envelope with one
   foreign top-level member added is refused. `invocation` is the command that printed those three results. Put the small script
   in your deliverables folder.
6. **Two thin fixtures, re-made by their handlers (CTO msg 4865).** The portal's readers enforce two identities the schema cannot
   state, the handlers keep both, and the fixtures break both (read by `2.0.0_SA_COO~D2` and confirmed by the issuer on the files):
   - `_contracts/fixtures/DirectoryPage.valid.json`: the page's `directory_revision` is 64 hex; its entry's
     `revision.directory_revision` is a different, 18-character value. Every entry must carry the page's own revision.
   - `_contracts/fixtures/AnalysisUploadResult.valid.json`: state NORMALIZED with `portfolio: {}`. The handler builds
     `portfolio.source.upload_id` equal to `upload_id` (`intake/uploads.py`, about lines 333 and 502).
   **Make each fixture's `instance` by the handler's own code path, not by hand:** run the function that builds the answer (the
   existing tests already do: `directory/tests/test_bootstrap_browse.py`; `intake/tests/test_deferred_resolution.py` and the builder
   in `intake/uploads.py` / `intake/upload_entry.py`), take its `data`, and write that as the fixture's `instance`, keeping the
   wrapper's `_fixture`, `_source` and `_expect` members and updating `_source` to say how it was made. Synthetic test values only:
   the tests' fakes are synthetic; if any value looks like a real client's, stop and file a row. The re-made instance must still
   validate against its type schema and against its route's response schema's `data` member, and the matching `.invalid` fixture
   must still be refused. In the record add `fixtures_made_by_handler: [{fixture, built_by:"<file>:<function>", invocation,
   validates_type_schema, validates_response_data}]`. If a handler path cannot produce a NORMALIZED upload answer or a page with
   entries in process, stop and file a row; do not hand-edit the fixture to pass.
5. **`packaged_in_functions`:** say which Lambda functions, if any, package one of the four schema files (search
   `infra/aws/lambda/ci/lambda-source-map.json` for the four file names). Do NOT edit the source map. If a function packages one,
   name it and its pin: the deployed copy then moves only at that function's next release, and the record says so.

**AMENDMENT 1 (issuer, 2026-10-11, on row IRPT_BCKEND-D2-W289-S2).** The commit-time naming gate refuses the re-made
`AnalysisUploadResult.valid.json` because the source test's principal belongs to a firm whose id is a registry spelling, and the
handler copies it into `portfolio.owner.firm_id`. The gate is right and is not overridden. Ruling, inside this cell:
- Re-capture the upload answer by the SAME handler path (`served.Entry.handle` to `intake/uploads.py:_normalized_response`), driven
  from a capture script in your deliverables folder that builds the same in-memory fakes the source test builds, with ONE
  difference: the acting principal's firm id is the synthetic id `F-49F`, which five sibling fixtures in the same folder already
  carry. Import the test module's helpers and fakes; do not edit any file under a `tests/` folder.
- The fixture's `instance` is that run's `data`, written as captured. No value is edited after capture. `_source` says the path,
  the script, and that the principal's firm id differs from the source test's.
- The record's `fixtures_made_by_handler` row for this fixture adds `differs_from_source_test: "principal firm id"`.
- If the handler path refuses a firm id that is not in the firm registry, or the answer cannot reach NORMALIZED with it, STOP and
  file a row saying exactly which line refuses; do not try another spelling and do not hand-edit.
- Everything else you built stands as it is (the four schemas, `DirectoryPage.valid.json`, the validation script, the record).
  Re-run all four criteria and the proof checker after the re-capture, then commit and flip.
Gate limb that graded this modification: GATE (viii) (placeholders). No criterion, check or path changes.

**AMENDMENT 2 (issuer, 2026-10-11, on row IRPT_BCKEND-D2-W289-S3).** `_scope/prospect.py:34` refuses a firm that is not an
enabled client firm of the registry `firm_ids()` reads, so AMENDMENT 1's capture cannot run against the real registry. Ruling:
- The capture may point the handler's own configuration seam, the environment variable `IRPT_FIRM_REGISTRY`, at a SYNTHETIC
  registry file kept in your deliverables folder, in which the one enabled client firm is `F-49F`. Build it as the smallest file
  the code path accepts (read how `_ids/ids.py` loads it; copy the real file's STRUCTURE, never a real firm's row or name).
  That is the second and last permitted difference from the source test. No source file, no test file and no real registry
  file is edited.
- The record's row adds `differs_from_source_test: "principal firm id; synthetic firm registry by IRPT_FIRM_REGISTRY"` and the
  synthetic registry's path. `_source` in the fixture says the same.
- STOP, with a row, if: a second module on the path reads firms from somewhere the variable does not reach; the answer does
  not reach NORMALIZED; any real firm spelling still appears in the captured `data`; or the naming gate refuses any file of
  the commit. Do not widen the method further.
- Then AMENDMENT 1's remaining steps: checks on the instance, the four criteria, the proof, the commit, the flip.
Gate limb that graded this modification: GATE (viii) (placeholders). No criterion, check or path changes.

<criterion id="IB128-1-AC1" cell_refs="IB-pr-430"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r128/p128_cells.py" . IB128-1-AC1</invocation><expect>IB128-1-AC1 PASS</expect></criterion>
<criterion id="IB128-1-AC2" cell_refs="IB-pr-430"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r128/p128_cells.py" . IB128-1-AC2</invocation><expect>IB128-1-AC2 PASS</expect></criterion>
<criterion id="IB128-1-AC3" cell_refs="IB-pr-430"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r128/p128_cells.py" . IB128-1-AC3</invocation><expect>IB128-1-AC3 PASS</expect></criterion>
<criterion id="IB128-1-AC4" cell_refs="IB-pr-430"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r128/p128_cells.py" . IB128-1-AC4</invocation><expect>IB128-1-AC4 PASS</expect></criterion>

A FOURTH criterion, with its reason: the CTO added the two fixtures to this cell after it was drafted (msg 4865), and they are a second built behaviour, not a control of the first.

<expected_criteria>IB128-1-AC1, IB128-1-AC2, IB128-1-AC3, IB128-1-AC4</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No handler, no `_authz/`, no portal, no source map, no other schema file.
- **Refusal clause:** if adding the member makes a test fail that asserts something OTHER than a missing member, or if the 17 turn
  out not to share one declaration, stop, file a row and report. If a criterion cannot be met as written, stop, file a row and
  report. Never weaken a check or a test; do not edit `p128_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W289-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; check the id is free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~289" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~289@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~289 <0.9.0_WK_IRPT_BCKEND~289@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
docs/contracts/investor-reporting/v1/responses/analysis-request-pdf.response.schema.json
docs/contracts/investor-reporting/v1/responses/comparison-catalogue.response.schema.json
docs/contracts/investor-reporting/v1/responses/custody-report-persist.response.schema.json
docs/contracts/investor-reporting/v1/responses/custody-report-read.response.schema.json
infra/aws/lambda/investor-reporting/_contracts/fixtures/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~289/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-430.four-response-schemas-declare-unprojected-grant.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 121 (round 128, workstream ~P), cell `IB-pr-430`.
<owned_cells>IB-pr-430</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB128-1-AC1, IB128-1-AC2, IB128-1-AC3, IB128-1-AC4. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~289/IRPT_BCKEND.TO-IB-pr-430.four-response-schemas-declare-unprojected-grant.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the four files' diff in one line each; for each re-made fixture, the handler path and invocation that made it and its two validation results; the fixtures you changed and why; the suite's last line
before and after; the three validation results per route; which functions package any of the four files; each criterion's last line;
the proof checker's result; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; four contract schema files and their valid fixtures; no handler, route, function or deployed byte changes in this cell. The consumer is named by the CTO (msg 4858): the portal's envelope parser already requires the member (row DSGN_IRPTV1-D2-W49-S7).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p128_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~12:0xZ: AC1 FAIL (17 of 21 declare it), AC2 PASS (a bound: 2 failed, 203 passed, both base failures), AC3 FAIL (no record), AC4 FAIL (the entry's revision is not the page's); commit-gate clean. The declaration's single form across the 17 and its required listing were measured by the issuer before the cut.
lane: the <paths> block IS the grant; the v1 response contracts of IRPT_BCKEND's routes. The ratified-text signer 3.0.0_SA_CVO is told at issuance.
</preflight>
