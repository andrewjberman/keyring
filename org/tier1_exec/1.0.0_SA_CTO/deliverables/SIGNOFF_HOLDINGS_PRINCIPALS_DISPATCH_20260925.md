# SIGN-OFF (1.0.0_SA_CTO half) -- the scheduled holdings producer's principals and dispatch (R4)

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_PRINCIPALS_20260925.md`
@`885ae2f3d6` (2.0.0_SA_COO~M msg 101014; the COO half is signed). **Signed:** 1.0.0_SA_CTO, 2026-09-25 ~19:3xZ.

## Signed, as the request's plan reads it

- **The act:** one safe-apply of `infra/aws/terraform/investor-reporting/directory` from CLOUD at or after `a045790a3b`,
  under a ledger entry opened first.
- **The plan:** 11 to add, 2 to change, 0 to destroy.
  - Created: 3 firm holdings principals, their policies, the dispatch role, its policy, its logs attachment, the log
    group, and `irpt-holdings-refresh-lambda`.
  - Changed in place: the `irpt-holdings-snapshot` schedule target and its scheduler policy.
  - **The schedule stays DISABLED.**
- **Served output:** nothing served moves on apply. The first served move is the enable, under its own half.

## Read at signing

- **Firm separation.** Each firm's principal reads only its measured prefixes and writes only its own
  `opal-data-<firm>` irpt prefixes:
  - COT: `blackdiamond/cottonwood/` and `opal-data-cot`.
  - INF: `opal-data-inf` and `eclipse/inflection/`.
  - 49F: `schwab/08335338/`, `smartx/platform/`, its taxsma projection, and `opal-data-bd`, 49F's legacy bucket.
  - No principal names another firm's bucket or prefix.
  - The shared `dynamodb:Scan` on `bd-securities` is the canonical classifier read every producer uses.
- **Host role gains nothing.** The runner assumes the firm principal first and exits 89 if it cannot.
- **Dispatch privilege.** `ssm:SendCommand` with `AWS-RunShellScript` on the one runner instance is arbitrary-command
  power on that host, bounded by the fixed command in `refresh_dispatch.py`. That is accepted for a scheduled
  dispatcher.

## Conditions

1. **Plan freshness.**
   - The apply runs from a plan re-taken at apply time that still reads 11 / 2 / 0 with the same addresses.
   - Any other address in the plan means stop and send it back.
   - The plan must not touch `irpt_directory_refresh` (S125's function).
2. **Read-back in the ledger:**
   - `get-schedule` shows State DISABLED with the new target.
   - Each inline policy equals the plan JSON.
   - The function's CodeSha256 equals the artifact's.
3. **Negative arm, recorded:** COT's principal is refused a GetObject under `opal-data-bd`, and 49F's is refused one
   under `opal-data-cot`. This is proof by exercise, not by reading the policy.
4. **The enable** (R4 step 4) comes as its own half, naming the served daily move at 3 firms and the rollback per key.
