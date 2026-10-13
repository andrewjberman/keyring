# TO IRPT_ANLREQ.TO-AR-y-229.ci-script-stderr-not-the-value -- the verify step reads each head-object value from stdout alone

<to_id>IRPT_ANLREQ.TO-AR-y-229</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~73</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>15</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-229` (`decompositions/IRPT_ANLREQ_DECOMP_R21F_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~73`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-73` (branch `wk-IRPT_ANLREQ-73`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~73 <0.9.0_WK_IRPT_ANLREQ~73@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W73-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).
- **NEVER run `build-and-upload.sh` without `BUILD_ONLY=1` against the real `aws`.** Your test runs the script end to end ONLY with the stub `aws` and stub `powershell.exe` first on PATH (as the existing test does).

### THE CELL (`AR-y-229`, inlined) -- THE VERIFY STEP MUST NOT READ STDERR AS THE VALUE. Offline arms only.

*The first fix (AR-y-222, @9ffca59db9) replaced a list-valued `--query` by two scalar reads, and kept `2>&1` on both (`infra/aws/lambda/ci/build-and-upload.sh` lines 728-733). On a real run by the applier the object landed and read back equal, but the script exited 1 `UPLOAD NOT VERIFIED`: each value came back prefixed by a `.tools/aws` shim WARN line written on stderr, and the compare read `WARN...<value>` against `<value>`. The fix is: stdout alone is the value; stderr is kept apart and shown only when the read fails or the compare does not match.*

**Read first:** the script lines 712-745 at HEAD (the verify block and the two `HEAD_*` reads), the test `infra/aws/lambda/ci/tests/test_build_and_upload_verify.sh` (the stub `aws` writes nothing on stderr on success: that is why it could not show this), the applier's record `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r21/SCRATCH_RUN.txt` (its stderr text is the WARN line and the exit; read it, quote it in your record, copy no secret) and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~68/r21/CI_VERIFY_FIX.json` (the first fix and its arms).

1. **Change only the two reads and the failure message.** Capture stdout of each `aws s3api head-object --query ...` as the value, with stderr redirected to a temp file (`mktemp`, removed at the end of the iteration; if `mktemp` fails the function is FAILED loud, not skipped). The compare stays fail-closed: a non-zero rc, a size mismatch or a sha mismatch fails. On a failure the message prints the value AND the contents of the stderr file (so the CLI's text is shown). On success the stderr file's content is NOT part of any compared value. Do not touch any other line of the script. Print `git diff --stat` and `bash -n` of the result.
2. **Add the new arm to the test** `infra/aws/lambda/ci/tests/test_build_and_upload_verify.sh`: `stderr_warning_ignored` -- the stub `aws` answers both head-object reads correctly on stdout AND writes a `WARN: shim ...` line on stderr on each call; the script must exit 0, print `write VERIFIED`, and update the temp map copy; the real `lambda-source-map.json` is checked byte-identical after the arm. Print `PASS stderr_warning_ignored`. Keep the existing arms (`landed_upload_verifies`, `head_object_fails` -- its CLI error must still be PRINTED on the failure path -- and the mutant arm) and the final `ALL PASS`.
3. **Prove the arm bites.** Run the new arm against the script at HEAD (the unfixed `2>&1`): it must FAIL there (that run is your mutant: the `controls.mutant` of the proof). Run it against your fix: it must pass. Record both outputs.
4. **Run the whole test** `bash infra/aws/lambda/ci/tests/test_build_and_upload_verify.sh` (exit 0, `ALL PASS`) and the sibling tests `test_build_only.sh`, `test_sha_handoff.sh` and `test_build_artifact_key.sh` (they must stay as they are at HEAD: say each result).
5. **Write `r21/CI_STDERR_FIX.json`:** `repro` (the applier's stderr text and the exit), `fix` (`lines_changed`, `diff_stat`), `arms` (list: `arm`, `exit_code`, `evidence`), `unfixed_script_result_on_new_arm`, `tests` (`passed`, `failed`, `sibling_results`), `shell_syntax_ok`, `claim`, `not_read` (state that the live CLI and the shim were not run by you).
6. **In your report:** the diff in one line, the new arm's result on the unfixed and the fixed script, the sibling results.

### ACCEPTANCE

<criterion id="AR229-y-AC1" cell_refs="AR-y-229"><invocation>python C:/dev/wk-irpt-anlreq-73/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y229-stderr --root C:/dev/wk-irpt-anlreq-73</invocation><expect>Y229-STDERR-OK</expect></criterion>
`AR229-y-AC1`: no head-object value of the verify block merges stderr into stdout, the test prints PASS for `landed_upload_verifies`, `head_object_fails`, `stderr_warning_ignored` and the mutant arm, and exits 0 with ALL PASS.

<criterion id="AR229-y-AC2J" cell_refs="AR-y-229" judgment="true"/>
`AR229-y-AC2J` (judgment, graded at L9, never by you): only the two reads and the failure message changed, the new arm FAILS on the unfixed script and passes on the fix, the CLI's error text is still printed on the failure path, and nothing was run against the real `aws`.

<expected_criteria>AR229-y-AC1 AR229-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~73/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/ci/build-and-upload.sh
infra/aws/lambda/ci/tests/test_build_and_upload_verify.sh
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R21F_Y.md</decomp_doc>
<owned_cells>AR-y-229</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~73/IRPT_ANLREQ.TO-AR-y-229.ci-script-stderr-not-the-value.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-229`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR229-y-AC1,AR229-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one shell script and its test, edited in a worktree; the test runs with stub aws and stub powershell.exe; nothing is uploaded, deployed, applied or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the applier's report (msg 7019: the first fix passed every offline arm and failed on the first real run) against the cell; the lens: a stub that is cleaner than the real CLI, so an arm cannot show the defect. The order requires the new arm to write a WARN line on stderr on success, to FAIL on the unfixed script, and the CLI's error to stay printed on the failure path. NOT seen: the real shim and CLI (the applier's live arm re-runs after the drain).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the applier's report (msg 7019, `TO-SCRATCH-R21`, commit `ec4b724fdd`) as workstream `YR` round 15. Base: `AR229-y-AC1` FAIL as expected (the script still merges stderr).
- The live re-run (one more real upload to a scratch key) is a new applier order after the drain.
