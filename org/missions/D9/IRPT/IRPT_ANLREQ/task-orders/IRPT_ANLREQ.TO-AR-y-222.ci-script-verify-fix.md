# TO IRPT_ANLREQ.TO-AR-y-222.ci-script-verify-fix -- the ci script's verify step fixed, shown on two offline arms

<to_id>IRPT_ANLREQ.TO-AR-y-222</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~68</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-222` (`decompositions/IRPT_ANLREQ_DECOMP_R21_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~68`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-68` (branch `wk-IRPT_ANLREQ-68`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~68 <0.9.0_WK_IRPT_ANLREQ~68@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W68-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call EXCEPT one read-only `aws s3api head-object` on an existing artifact key (step 1); no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-222`, inlined) -- THE CI SCRIPT'S VERIFY STEP. ONE FILE. NO REAL UPLOAD.

*On this box `infra/aws/lambda/ci/build-and-upload.sh` (without `BUILD_ONLY`) prints `ERROR: UPLOAD NOT VERIFIED` and exits 1 after a GOOD upload, and does not update the source map: its own `aws s3api head-object --query` verify call dies with `'int' object has no attribute 'items'`, and the script reads that error text as the head-object result (row `IRPT_ANLREQ-D2-S71`, from the applier of release 20).* The CTO (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_21_20261013.md` section 2 item 3): this project fixes it; one cell owns the script; if the owned-paths gate refuses the path, that refusal names the owner and it goes in as a surprise row, not as a message.

**NEVER run `build-and-upload.sh` against the real `aws` without `BUILD_ONLY=1`: without it the script UPLOADS to the artifact bucket (row `D2-S69`). Every arm of this cell runs with a STUB `aws` and a STUB `powershell.exe` first on PATH (or against an extracted function), so nothing can be written to S3 or to the repository's source map.**

**Read first:** the script (the block from the `powershell.exe -NoProfile -Command "aws s3 cp ..."` upload through `write_sha_to_map`, lines 698 to 745 at the trunk head; `BUILD_ONLY` at 691), the row `D2-S71` in `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`, and the applier's record `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r20/` (the units' logs show the failing line).

1. **Reproduce the defect read-only.** Run, with the real CLI, ONE read-only call on an existing artifact key: `aws s3api head-object --bucket opal-313476888478-lambda-artifacts --key investor-reporting/irpt-narrative.zip --region us-east-1 --query '[ContentLength, Metadata."content-sha256"]' --output text` (the script's own call) and the same call without `--query`. Record the output of each in `repro` (`command`, `cli_error_text` = the error the old call hits, or the exact output if it does not fail in your shell; also say which `aws` the script's shell resolves: `type -a aws`). Find the CAUSE (the CLI's response member that is an integer where the query expects a mapping, or the shell's `aws`), and say it.
2. **Fix the script's verify step only** (no other part of the script changes): the verify reads what it needs in a form that does not hit the error (for example two `--query` calls, or `--output json` parsed in the script), and keeps its fail-closed meaning: it requires `ContentLength` equal to the local zip's size and the `content-sha256` metadata equal to this build's SHA256. A landed upload verifies, prints the VERIFIED line, updates the source map and the function lands in BUILT; a head-object that FAILS (non-zero exit, or output that is not the two values) makes the script exit non-zero (the existing FAILED path) with the CLI's error text printed to stderr, and the map is not updated.
3. **Two offline arms, in a test file you add** (`infra/aws/lambda/ci/tests/test_build_and_upload_verify.py` or `.sh`; a new directory is fine): (a) `landed_upload_verifies`: stub `aws` returns the size and the content-sha256 of a built zip; the script (or the verify function you extracted) exits 0 and the temp copy of the source map carries the new `artifact_sha256`; (b) `head_object_fails`: stub `aws` fails (exit 1 with a CLI-style error text); exit is non-zero, the error text appears on stderr, the map copy is unchanged. Run the script end to end in a throwaway worktree OUTSIDE the product tree with the stubs, or extract the verify block into a function and test it directly; say which, and why the arm exercises the script's own code. A third arm for the `BUILD_ONLY` path is welcome (it still uploads nothing). Run `bash -n` on the script.
4. **The live scratch-key arm is NOT yours.** Design it in `scratch_arm_design`: the exact command lines an applier will run to upload to a SCRATCH key (a key under a prefix that is not any function's key, for example `investor-reporting/_ar222_scratch/`), what the applier reads back, and how the scratch object is left (no delete: versioned bucket, the object stays as evidence).
5. **Write `r21/CI_VERIFY_FIX.json`:** `repro`, `fix` (words and the changed line numbers), `arms` (objects with `arm` named EXACTLY `landed_upload_verifies` and `head_object_fails`, `exit_code`, `map_updated`, `cli_error_printed` for the second), `shell_syntax_ok`, `tests` {`passed`, `failed`}, `scratch_arm_design`, `claim`, `not_read`.
6. **In your report:** the cause in one sentence, the fix in one, the arms and their exit codes.

### ACCEPTANCE

<criterion id="AR222-y-AC1" cell_refs="AR-y-222"><invocation>python C:/dev/wk-irpt-anlreq-68/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y222-verify --root C:/dev/wk-irpt-anlreq-68</invocation><expect>Y222-VERIFY-OK</expect></criterion>
`AR222-y-AC1`: the record names the cause of the old verify error, a landed upload verifies with exit 0 and an updated map on a stub, a failing head-object exits non-zero with the CLI's error printed and the map untouched, `bash -n` passes, and the added tests pass.

<criterion id="AR222-y-AC2J" cell_refs="AR-y-222" judgment="true"/>
`AR222-y-AC2J` (judgment, graded at L9, never by you): the fix changes only the verify step and keeps it fail-closed, the arms exercise the script's own code, nothing was written to S3 or to the repository's source map, and the scratch-key arm is designed and not run.

<expected_criteria>AR222-y-AC1 AR222-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~68/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/ci/build-and-upload.sh
infra/aws/lambda/ci/tests/
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R21_Y.md</decomp_doc>
<owned_cells>AR-y-222</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~68/IRPT_ANLREQ.TO-AR-y-222.ci-script-verify-fix.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-222`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading the script: it is the release path for every Lambda artifact of the estate; the cell changes the verify step only and runs every arm against stubs; nothing is uploaded and no source map is written.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading rows D2-S69 and D2-S71 against the cell; the lens: an arm that runs the real aws and uploads, a verify that stops failing closed, or a fix that hides the CLI's error. The order forbids the real aws without BUILD_ONLY, requires the stubs first on PATH, and requires the failing arm to print the CLI's error and exit non-zero. NOT seen: the script on a machine whose aws differs from this box's.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-21 analysis item 2 as round 21 workstream `Y`. Base: `AR222-y-AC1` FAIL as expected (no record).
- If the owned-paths gate refuses `infra/aws/lambda/ci/`, file the surprise row it asks for.
