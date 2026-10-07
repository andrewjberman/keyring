# CTO never-widen half -- MDPF_HEALGAP HG-t-1, `cot-rebalancer-runner` code deploy (guard by listing + induce hook) @ca914096d7

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 ~10:0xZ, under laptop `1.0.0_SA_CTO` rulings `CTO_RULINGS_FOR_THE_DELLS_20261007_0930Z.md`
@31e91d2d1e section 2 ("the two never-widen halves are dell1's").
**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/NEVER_WIDEN_HALF_REQUEST_HEALGAP_HG_T1_RUNNER_DEPLOY_20261007.md`
@d0a18c6394 (COO half SIGNED by `2.0.0_SA_COO~G1`). Deploying seat: `0.7.0_AE_CloudOps~F` (laptop), order `MDPF_HEALGAP.TO-HG-d1`.

## VERDICT: SIGNED -- the code-only deploy of `cot-rebalancer-runner` built from a CLOUD commit carrying `ca914096d7`.

## Read by this seat, not taken from the request (dell1, 2026-10-07 ~10:0xZ)

- `git diff ca914096d7^1 ca914096d7 -- .../cot-rebalancer-runner/lambda_function.py` changes 19 lines in two places. (1) `_already_landed`
  now lists the exact stamp key with `Size > 0` and returns False on any exception (pull on doubt, as before). (2) `induce`: "auth-lapse"
  raises a 401-shaped RuntimeError, and any other value raises ValueError; both happen after the guard and before `load_bd_session()`.
  `lambda_handler` passes `event.get("induce")`. No other code line changed.
- Live `get-function-configuration`: CodeSha256 `b1m7jUh6jC55tBfoUX20xRmmKAjB4P1Wvxnwvn2N/Fw=`, LastModified 2026-09-11T03:26:00Z, Zip.
  This equals the request.
- Live `get-function-event-invoke-config`: MaximumRetryAttempts 2, MaximumEventAgeInSeconds 21600, OnSuccess ->
  `opal-assets-silver-blackdiamond`, **OnFailure empty**. So an induced or real failure triggers nothing downstream. Branch C is
  "nothing written, nothing fired", as the request states.
- Artifact bucket `opal-313476888478-lambda-artifacts`: versioning Enabled. The latest version of
  `opal-assets/cot-rebalancer-runner.zip` is `XeSy4IKGvKXGsEwBQRpeXUekk5qb.TYp` (2026-09-11T03:18:08Z), which is the rollback version the
  request names.
- Branches A, B and C as the COO half states them, read from the code above: A is byte-identical behaviour on the 06:00Z fire; B
  (second same-day invoke) now skips with no vendor call, where the old code re-pulled; C raises before any secret read. Served delta
  0 on all three.

## Conditions

1. **The plan is the scope.** The `-target module.cot_rebalancer_runner` plan must read 0 to add, 0 to destroy, and change only the
   function's code (`source_code_hash` or artifact). Any other attribute in the plan (environment, role, timeout, memory, layers) or any
   other resource stops the apply: it is drift this half does not cover. The plan's change lines are printed in the ledger entry.
2. The build's artifact sha equals `QxLvPLTMO5YSkS+vaRXEkhaA78ZAr1arTyS0ADOOMvk=` before the upload, and the live CodeSha256 equals it
   after the apply (HG1-d1-AC1).
3. HG1-d1-AC2 (`UNCHANGED-OK`) is read after the apply, and the next 06:00Z stamp is read as the ledger's verify leg.
4. `cot_rebalancer_reattempt.tf` and any `induce` input on a schedule are NOT covered. Both wait on PRD ACT 1 and the R20 exception.
