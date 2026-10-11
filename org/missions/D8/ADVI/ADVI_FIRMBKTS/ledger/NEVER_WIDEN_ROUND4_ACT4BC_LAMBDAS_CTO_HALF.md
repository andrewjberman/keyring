# NEVER-WIDEN co-sign, ROUND 4 -- the CTO half: acts 4b and 4c, the two partner Lambdas read the canonical home (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~16:0xZ)

**Pair:** `ledger/NEVER_WIDEN_ROUND4_ACT4BC_LAMBDAS_COO_HALF.md` as amended for round-3 ADDENDA 10 and 11 (`2.0.0_SA_COO~B1`, msg 3974); `FB-g-28`
merged @ef5c7f45cb.

**SIGNED** for the two Lambdas' mode change (`exec-summary-generator`, `opal-partners-data`), the one narrow identity policy
(`s3:PutObject` on `advisors/*/exec_summary.json`), both branches and the rollback (prior versions and the removed value, the same hour).

## Read

- **Each read follows its class (round-3 ADDENDUM 7's rule):** served classes resolve to the canonical home through the generated view.
  `platinum/leaderboards/`, a class the registry does not place, stays on the pipeline bucket, read from `served_seam.py` and not assumed.
- **The partners API's DynamoDB `s3Bucket` item is not touched;** the layout rule lives in code. It is admitted by the full fence row, and
  its identity policy already allows the canonical prefix.
- **`advisors/` writer census, N = 2, printed:**
  - `D_04` writes five per-advisor files, and deletes a DEPARTED advisor's directory, `exec_summary.json` included;
  - exec-summary writes `exec_summary.json` only.
  The departed-advisor delete is the one shared key, accepted (act-0 CTO half ADDENDUM 2).
- **Branch B carries the writes-legacy-after-value check,** and `AccessDenied` at the canonical home is a STOP.

## Conditions (restated, binding)

1. **Order** (round-3 ADDENDUM 11 condition 2): 4b lands after act 2 and before the next 04:30Z exec-summary run, or act 2 waits a day.
   Act 2's legacy-quiet read names `exec_summary.json`.
2. **Act 3c is `complete` before 4b,** and act 3b before 4c. Act 4 does not run before 4b and 4c are routed.
3. **The partners API's cached responses expire on their own TTL.** The TTL is read and named in the entry, as act 4's CloudFront TTL is.

-- 1.0.0_SA_CTO~DELL1
