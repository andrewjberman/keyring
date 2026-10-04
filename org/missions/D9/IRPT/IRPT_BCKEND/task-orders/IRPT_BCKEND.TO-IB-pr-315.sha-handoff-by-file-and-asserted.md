# TO IRPT_BCKEND.TO-IB-pr-315 -- build-and-upload.sh hands the artifact sha to its node step by file and asserts the written value (S278)

<to_id>IRPT_BCKEND.TO-IB-pr-315</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~118</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>48</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO ROUND ANALYSIS rounds 42-46 item E2 (msg 104972), on E1's LIVE list
(IB-pr-313 @db0adf0053), BLOCKING row S278 | **Decomp cell:** `IB-pr-315` (decomposition section 42) | **outcome_ref:** FWD-8 (every
served artifact's recorded sha) | **depends_on:** none. WORLD is the gate floor for infra/; nothing is deployed in this cell.

---

## WORKER FACE

**What is wrong.** `infra/aws/lambda/ci/build-and-upload.sh` computes an artifact's base64 sha256 and checks its shape in bash
(:555, `^[A-Za-z0-9+/]{43}=$`). It then hands it to a node step through an environment variable (:605-609
`SHA256="$SHA256" "$JSON_TOOL" "$TMPJS_UPDATE"`, read at :139-147 as `process.env.SHA256`), which writes it into
`infra/aws/lambda/ci/lambda-source-map.json` unchecked. Under Git Bash, MSYS path conversion can rewrite a value that starts with or
holds `/`, so the map can record a sha that is not the artifact's. Nothing asserts the written value.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-118`. Run everything from its root.

**What you build:**
1. **The node step reads the sha from a temp file**, written by bash with `printf '%s'`, instead of `process.env.SHA256`. Remove
   every `process.env.SHA256` read. Change nothing else in the script's flow.
2. **After the write, assert** that the map's `artifact_sha256` for that function equals the computed value and matches
   `^[A-Za-z0-9+/]{43}=$`. On a mismatch, exit non-zero with `ERROR:` and the function name.
3. **`infra/aws/lambda/ci/tests/test_sha_handoff.sh`**, offline: no AWS, no upload. Factor the hand-off into a function the test can
   source, or drive the node update directly against a temp copy of a tiny source map. It prints one `PASS ...` line per arm and
   exits non-zero on any failure. Arms:
   - a sha holding `/` and `+` (44 characters, ending `=`) is written verbatim;
   - a malformed written value is refused by the post-write assertion.

<criterion id="IB48-1-AC1" cell_refs="IB-pr-315"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r48/p48_e2_cells.py" . IB48-1-AC1</invocation><expect>IB48-1-AC1 PASS</expect></criterion>
`IB48-1-AC1` -- the hand-off test passes with at least 2 PASS lines. Base: FAIL.

<criterion id="IB48-1-AC2" cell_refs="IB-pr-315"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r48/p48_e2_cells.py" . IB48-1-AC2</invocation><expect>IB48-1-AC2 PASS</expect></criterion>
`IB48-1-AC2` -- `bash -n` passes and no `process.env.SHA256` remains. Base: FAIL.

<expected_criteria>IB48-1-AC1,IB48-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none. Do not run build-and-upload.sh against AWS.
- **Refusal clause.** A change to the script beyond the hand-off and the post-write assertion, or any upload, is a defect: stop
  and file a row.

<paths>
infra/aws/lambda/ci/build-and-upload.sh
infra/aws/lambda/ci/tests/test_sha_handoff.sh
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~118/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-315.sha-handoff-by-file-and-asserted.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 42 (round 48, workstream ~P), cell `IB-pr-315`.
<owned_cells>IB-pr-315</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB48-1-AC1, IB48-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~118/IRPT_BCKEND.TO-IB-pr-315.sha-handoff-by-file-and-asserted.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB48-1-AC1,IB48-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, and any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- infra/aws/lambda/ci/build-and-upload.sh, the estate's Lambda build-and-upload; the change is the sha hand-off and a post-write assertion; 0 served bytes move in the cell; every later build that records a sha reads through it.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB48-1-AC1 base FAIL (no test), IB48-1-AC2 base FAIL (process.env.SHA256 present), dry-run at base 123258bd51 2026-10-04 ~23:5xZ.
lane: the <paths> block IS the grant.
</preflight>
