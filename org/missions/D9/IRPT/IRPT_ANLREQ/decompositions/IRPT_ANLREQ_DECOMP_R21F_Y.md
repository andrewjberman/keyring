# IRPT_ANLREQ -- decomposition, round 21 CI SCRIPT SECOND FIX, workstream YR round 15 (issuer 2.0.0_SA_COO~Y2)

**Input:** a measured result of this round. The live arm of `AR-y-222` (applier `0.7.0_AE_CloudOps~AQ2`, order `TO-SCRATCH-R21`, report msg 7019, record `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r21/`, commit `ec4b724fdd`): the fixed script (blob `372c3240fb`) exited 1 `UPLOAD NOT VERIFIED` on a real run although the object landed at `investor-reporting/_ar222_scratch/ar222-20261013T151208.zip` and read back equal in size and sha256. Cause, from the script's own stderr: both scalar head-object values were correct, but each came prefixed by a `.tools/aws` shim WARN line, because the script reads each value with `2>&1` (lines 728-733 at HEAD), so stderr is merged into the compared value. The `AR-y-222` fix removed the list-valued `--query` and kept the stderr merge; the offline arms used a stub `aws` that wrote nothing on stderr on success, so they could not show it. The reported release-20 error (`'int' object has no attribute 'items'`) is the same class (CLI output other than the value, read as the value). Nothing else in the script is in scope.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-229` | the two head-object reads capture STDOUT alone as the value; stderr goes to a temp file, printed on a non-zero read or a mismatch and never compared; a new test arm shows a good upload with a WARN line on stderr verifies and exits 0 | `infra/aws/lambda/ci/build-and-upload.sh` (the two reads and the failure message only) and `infra/aws/lambda/ci/tests/test_build_and_upload_verify.sh` | WORLD |

## Edges and chains

- None. M = 1 chain. The live arm re-run (one more real upload to a scratch key by an applier) follows the cell's drain.

fanout: 1 of 1 chains, cap 8, reason: one independent repair of one script, one test file.
