# TO IRPT_BCKEND.TO-IB-pr-329 -- one S3 key per function: the builder uploads to the key the source map and Terraform read (row S343)

<to_id>IRPT_BCKEND.TO-IB-pr-329</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~132</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>61</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** `1.0.0_SA_CTO~DELL2` round analysis rounds 47-60,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_47_60_20261007.md` @e363a194ed section 5, item E-P1 |
**Risk:** declared at the L6 floor its `<paths>` imply (an `infra/` path floors at WORLD, spine v3.19); the analysis's own class for E-P1 is in its section 5 | **Decomp cell:** `IB-pr-329` (decomposition section 54) | **outcome_ref:** row S343 (release tooling); no FWD moves directly | **depends_on:** none.

---

## WORKER FACE

**The defect (row IRPT_BCKEND-S343, measured at HEAD).** `infra/aws/lambda/ci/build-and-upload.sh:354` sets
`S3_KEY="$PIPELINE/$FN_NAME.zip"`. For the three functions whose deployed name differs from their artifact key, the build uploads to the
wrong key: `irpt-49f-reporting-read-lambda`, `irpt-49f-reporting-gold-lambda` and `irpt-49f-reporting-publish-lambda` each carry
`artifact_s3_key` `investor-reporting/irpt-reporting-{read,gold,publish}-lambda.zip` in `infra/aws/lambda/ci/lambda-source-map.json`, and their
Terraform roots read those keys. Releases r57 and r58 each needed a manual server-side copy-object before apply. Line 152 also writes
the builder's key back into the map's `artifact_s3_key` after an upload.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-132`; run everything from its root):

1. **`build-and-upload.sh` only.** When the function's map row carries a non-empty `artifact_s3_key`, `S3_KEY` is that value; otherwise
   it stays `$PIPELINE/$FN_NAME.zip`. Read the field with the script's existing JSON tool the way it reads `name`/`source_dir`/`files`.
   The `BUILD_ONLY:` line (about :612) gains ` key=$S3_KEY` at its end; keep the rest of that line byte-identical (`test_build_only.sh`
   reads it). Touch nothing else in the script, and do not edit `lambda-source-map.json`.
2. **`infra/aws/lambda/ci/tests/test_build_artifact_key.sh`** (new). Model it on `infra/aws/lambda/ci/tests/test_build_only.sh`: a tiny fixture pipeline built under
   `BUILD_ONLY=1` with a stub `aws` first on PATH and `BAU_SOURCE_MAP_OVERRIDE` pointing at a fixture map whose row carries an
   `artifact_s3_key` different from the function name. Assert the `BUILD_ONLY:` line ends with `key=<that key>`, and that a second row
   with no `artifact_s3_key` prints `key=<pipeline>/<name>.zip`. The test runs the builder at `${BAU_BUILDER:-<repo>/infra/aws/lambda/ci/build-and-upload.sh}`
   so the check can point it at the base builder, where it must FAIL. Exit 0 on pass, non-zero on fail.
3. Run `bash infra/aws/lambda/ci/tests/test_build_only.sh` once and report its last line (it must still pass).
4. Commit. No upload, no AWS call.

<criterion id="IB61-1-AC1" cell_refs="IB-pr-329"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-1-AC1</invocation><expect>IB61-1-AC1 PASS</expect></criterion>
`IB61-1-AC1` -- the new test passes against your builder and FAILS against the base builder (BAU_BUILDER). Base: FAIL (no test).

<criterion id="IB61-1-AC2" cell_refs="IB-pr-329"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-1-AC2</invocation><expect>IB61-1-AC2 PASS</expect></criterion>
`IB61-1-AC2` -- BUILD_ONLY=1 of each of the three reporting functions prints key= equal to its map artifact_s3_key. Base: FAIL (no key printed; dry-run at 6e462d3499).

<criterion id="IB61-G-132" cell_refs="IB-pr-329"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-G-132</invocation><expect>IB61-G-132 PASS</expect></criterion>
`IB61-G-132` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB61-1-AC1,IB61-1-AC2,IB61-G-132</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** An edit to `lambda-source-map.json`, to any Terraform file, or an upload is a defect: stop and file a row.

<paths>
infra/aws/lambda/ci/build-and-upload.sh
infra/aws/lambda/ci/tests/test_build_artifact_key.sh
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~132/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-329.one-s3-key-per-function.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 54 (round 61, workstream ~P), cell `IB-pr-329`.
<owned_cells>IB-pr-329</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB61-1-AC1, IB61-1-AC2, IB61-G-132. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~132/IRPT_BCKEND.TO-IB-pr-329.one-s3-key-per-function.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB61-1-AC1,IB61-1-AC2,IB61-G-132` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, any suite's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- nothing is deployed by this order; any release is the issuer's after the drain.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS permission is added.
comp-routes: DECLARED-NOT-APPLICABLE -- no route or CloudFront behaviour changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- every criterion dry-run at base 6e462d3499 2026-10-07 ~09:0xZ: build checks FAIL, guards PASS (p61_cells.py).
lane: the <paths> block IS the grant.
</preflight>
