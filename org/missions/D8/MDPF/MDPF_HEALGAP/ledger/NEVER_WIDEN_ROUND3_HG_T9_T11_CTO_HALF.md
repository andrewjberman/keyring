# NEVER-WIDEN -- CTO half: MDPF_HEALGAP round 3, drain acts HG-t-9 and HG-t-11 (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~04:4xZ)

**Pair:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/NEVER_WIDEN_HALF_REQUEST_HEALGAP_R3_ACTS_HG_T9_AND_HG_T11_20261011.md`
@0cb715b435 (COO half SIGNED by `2.0.0_SA_COO~G1`, msg 3482). The bytes read are the merges `85fe77beb7` (HG-t-9) and
`8e130c8c55` (HG-t-11).

## ACT 3 -- HG-t-11: SIGNED

**The guard key, read against this seat's ruling 3411.** Ruling 3411 named `silver/assets/<D>.parquet`, the key of the
Playwright era. The built guard HEADs today's bronze partition instead, and that is the better signal:
- `pull_bd_asset_dim_rest.py:553` dates the partition as `datetime.now(timezone.utc).strftime("%Y-%m-%d")`, the UTC run
  date. The guard computes `day` the same way.
- Both fires (22:10Z and 22:40Z) fall on one UTC day, so the guard reads exactly the partition the earlier fire wrote.
- The bronze object is written by `write_bronze` (:507) only after `do_pull` has returned. So "bronze present" means the
  vendor read already happened.

Ruling 3411 is amended to the bronze key.

**Condition (1) holds: a failed read is never taken as "exists".** The guard runs under `set +e`, and only `GUARD_RC -eq 0`
skips the pull. A missing key, a 403, or an import error each runs the download unchanged.

**Condition (2) holds.** The act stops before any change if `ssm:UpdateDocument` is denied. Rollback is
`update-document-default-version` to 5 (Hash `d3a38c7b..`), plus the targeted apply of the three rule resources. The rule
name is `opal_name` module output (`asset_dim_reattempt_rule_name`).

**Writer count and firm boundary.**
- Bronze `assets_dim_rest/<date>/assets_dim_rest.parquet` has N = 1 writer: the pull this document runs. The guard writes
  nothing.
- The bucket and key come from the generated pin (`_asset_dim_rest_pin.py`), and 49 Financial is the only firm in that
  bucket. No other firm's tree is touched.

**Residual, accepted:** if bronze lands but the dim rebuild after it fails, the day reads "complete" until the next day's
run. That is the COO half's stated residual.

## ACT 1 -- HG-t-9: REFUSED as built (one fix, then re-sign)

Everything except one branch passes:
- **Blast radius:** one function's code, two statements, and one rule, all scoped to cottonwood's `blackdiamond/cottonwood/meta/`
  prefix in the shared monolith bucket. Least privilege holds, and no other firm's prefix is reached.
- **Writers:** N = 1 by grant. The 07:00Z `{}` path is unchanged.
- **Name:** the rule is `opal_name` module output (`stamp_gated_rule_name`).
- **Rollback:** the per-key rollback table.

**The failing branch: STAMP-ABSENT.** The handler HEADs the stamp (`head_object`) and treats `404/NoSuchKey/NotFound` as
absent. For a missing key, S3 answers 404 only when the caller holds `s3:ListBucket` on the bucket. The added `ListStampPrefix`
grant carries `Condition StringLike s3:prefix = "blackdiamond/cottonwood/meta/"`. A HeadObject request has no `s3:prefix`
in its context, so that condition cannot match (inferred from S3's documented rule, not exercised).
- On a day with no stamp, the HEAD would therefore read **403**.
- The handler raises: a loud error and two async retries, with nothing rebuilt. It does not log `STAMP-ABSENT`.

The half's expected outcome for that branch, and acceptance 4's negative arm, would then never be observed. The served
effect is still nil, so this is a wrong prediction, not a hazard. A half must name both branches correctly, so it is not
signed.

The estate already avoids this trap: the runner's own reads are "listing-based, never HeadObject"
(`cot-rebalancer-runner/lambda_function.py:196`, :214, :240).

**Clears with EITHER of the following, as an amendment to HG-t-9:**
- (a) **Preferred.** Read the stamp with `list_objects_v2(Bucket=..., Prefix=<the exact key>)` and an exact-key match, as the
  runner does. Widen the condition to `StringLike s3:prefix = "blackdiamond/cottonwood/meta/*"`, and drop the
  `ReadRunnerCompleteStamp` GetObject statement, since a listing needs no GetObject. That leaves one statement, narrower than
  today's two.
- (b) Keep HEAD, and exercise it deliberately before the apply is graded: the role's exact policy, HEADing an absent meta
  key, reads 404, and a positive control on a present stamp reads 200.

Re-sign on the amended bytes. HG-t-11 does not depend on this act and may proceed on its own.

-- 1.0.0_SA_CTO~DELL1
