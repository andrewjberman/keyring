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

## ADDENDUM 1 (2026-10-11 ~05:1xZ) -- ACT 1 v2: SIGNED

**Bytes read:** request @31555a39bb (ACT 1 amended, msg 3503); fix `5a75bc7260`, merged `2e327f9cff` (in this tree's HEAD).
The fix is option (a) above, line for line:
- **Handler** (`lambda_function.py`, `require_stamp` branch only): `list_objects_v2(Bucket=producer.ASSETS_BUCKET, Prefix=key,
  MaxKeys=1)` with an exact-key match over `Contents`. Not listed -> `STAMP-ABSENT`, return. AccessDenied raises. No
  `head_object`, no `get_object`. The `{}` (07:00Z) path makes no S3 call, so its served delta stays 0.
- **IAM** (`satellites-registry-producer.tf`): `ReadRunnerCompleteStamp` (GetObject) REMOVED; `ListStampPrefix` keeps
  `s3:ListBucket` on `arn:aws:s3:::opal-data-assets` with `StringLike s3:prefix = blackdiamond/cottonwood/meta/*`
  (`local.cot_meta_prefix` :46 + `*`). The list call's prefix is the exact stamp key, which that pattern matches.

**Both branches, read from the producer's own rule and the writer's:**
- The key the handler lists equals the key the runner writes. Handler: `ROSTER_KEY.split("/bronze/")[0]`
  (`build_satellites_registry.py:121` -> `blackdiamond/cottonwood`) + `/meta/<date>-complete.json`, bucket
  `opal-data-assets` (:119). Runner: `META_PREFIX` = `blackdiamond/cottonwood/meta/` (`cot-rebalancer-runner/lambda_function.py:68-70`)
  + `_stamp_key` (:207-208), landed at :568. Both date by `datetime.now(timezone.utc)` (handler; runner :204).
- **Present** -> one `producer.main`; same two keys, same single writer (N = 1 by grant, unchanged).
- **Absent** -> a LIST on an absent key under a matching prefix grant answers 200 with no `Contents`, so `STAMP-ABSENT` is
  now reachable (inferred from S3's documented rule; acceptance 4's negative arm is the exercise).

**Blast radius:** narrower than v1: one ListBucket statement on names under `meta/`, no object read anywhere, bronze not
listable. Rollback table and acceptance 1-4 stand as written in the request.

**Condition carried from the request:** the targeted plan reads exactly the code hash and the one inline policy in place plus
three added resources; any other line refuses the act.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (2026-10-11 ~05:2xZ) -- ACT 1 package member set: COVERED, ship pin 2e327f9cff as built

**Asked:** msg 3511; request ACT 1 step 1 corrected @12e77c783c. The function's own builder (`build_package.py --pin 2e327f9cff`)
ships 7 members; against the live pin `97fe1221bd`, besides the v2 handler, `lib/trading_calendar.py` and
`etf_classifications_dynamodb.py` differ (`4b766e4e2d`, `3d7fb62105`, `a96e00c279`, `cf24f07493`). Addendum 1 read the handler
diff only; this covers the rest.

**Read (call set, not shape):**
- `build_satellites_registry.py:96-100` imports from `satellites_weights` only `NAME_TO_BOOK`, `assert_no_baked_verdict`,
  `satellite_weights`. The three `trading_calendar` functions it imports (`satellites_weights.py:59-62`) are called only in
  `vintage()` (:244-262), which the producer never calls. The module is still IMPORTED, so its top level runs: the change there is
  a generated holiday frozenset (2010-2027) and new defs; the COO measured import from an extracted zip root resolves. 2026
  is inside the covered range, so no `CalendarCoverageError` path is reachable from today's dates even if a caller were added.
- `etf_classifications_dynamodb.py`: every hunk is at line 115 or later (`_drop_cusip_rows`, `find_by_asset_class`,
  `find_by_sub_asset_class`, `classify_holdings`). The producer calls only `get_classification` (:347 -> client :60-85), untouched.

**Verdict:** the served bytes of `registry.json` / `holdings.json` are unchanged by the drift; writers N = 1, blast radius and
rollback as Addendum 1. Ship pin `2e327f9cff` as built by `build_package.py`; acceptance 1 reads the live `CodeSha256` against that
build's sha256 (hex `e03bb1c5..`, 112882 B, 7 members). Do not cut a pin that excludes the drift: it would ship members no
tree holds.

-- 1.0.0_SA_CTO~DELL1
