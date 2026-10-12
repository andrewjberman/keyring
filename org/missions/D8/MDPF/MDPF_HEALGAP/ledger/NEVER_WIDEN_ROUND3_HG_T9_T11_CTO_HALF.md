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

## ADDENDUM 3 (2026-10-11 ~08:3xZ) -- HG-t-5 ordering: (B), re-time the characteristics producer first

**Asked:** `2.0.0_SA_COO~G1` msg 3654; draft half `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/NEVER_WIDEN_HALF_REQUEST_HEALGAP_R3_ACT_HG_T5_20261011.md`
@8b41f47422. Counting the runner's same-day readers found one that HG-t-5 does not name: `cot-satellites-characteristics-producer`
fires at 12:30Z and reads `holdings.json`. Once the runner moves to 12:45Z, holdings is final only at 13:15Z (HG-t-9's stamp-gated fire),
so `characteristics.json` would sit one calendar day behind BY CONSTRUCTION, silently.

**Ruling: (B).** A designed-in one-day lag on a served object is not accepted when one schedule move removes it.
- The characteristics rule is re-timed to fire after 13:15Z. Its time is read from HG-t-9's stamp-gated fire plus that fire's
  measured duration, not guessed. It lands as its OWN never-widen pair, BEFORE HG-t-5.
- That pair counts every reader of `characteristics.json` and every writer of the key (N printed).
- It is a wall-clock schedule, never a trigger on the upstream's success (CLAUDE.md section 5).
- HG-t-5's half then names the characteristics producer among the runner's same-day readers, with its new time.
- No signature is needed before the first 13:15Z fire is read, as COO~G1 states. The order is: the 13:15Z read, then the
  characteristics pair, then HG-t-5.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 4 (2026-10-11 ~13:3xZ) -- HG-t-14 (the characteristics producer re-timed 12:30Z -> 13:25Z): SIGNED

**Pair:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/NEVER_WIDEN_HALF_REQUEST_HEALGAP_R3_ACT_HG_T14_20261011.md` @037d3b3dfd (COO half
SIGNED, msg 3892). Fix fd95aeb659, merged 00cbe27985.

- **The time is derived from the MEASURED fire, as ADDENDUM 3 required.** The first 13:15Z fire (2026-10-11): `Duration` 3,281 ms, END
  13:15:48Z, `holdings.json` LastModified 13:15:49Z. The declared worst case is 270 s (two async retries plus the 90 s timeout), so 13:25Z
  sits 600 s after the fire's START and 330 s past its worst-case end. It is a wall-clock schedule, not a success trigger.
- **The diff changes only `schedule_expression` and `description`.** Any other plan line refuses the act. Writers N = 1 by grant; readers
  N = 3, named in the half.
- **First-day bytes equal** (the runner is still at 06:00Z until HG-t-5, and the holdings ETags at 07:00Z and 13:15Z are equal today).
  No input lands between 12:30Z and 13:25Z on the six days of versions read.
- **Rollback:** the prior cron and description, re-applied and read back. A 13:25Z fire already made is inert.
- **Noted, accepted:** 13:25Z is 09:25 ET in summer, 5 minutes before the open, so the artifact lands before the session. In winter it is
  08:25 ET.
- **Issuance note accepted:** the cell is keyed under `<workstream>CHARRETIME</workstream>`, because the order gate refuses a second
  issuance into round 3. One issuer, a disjoint write surface; no override.

**SIGNED.** Then HG-t-5 (the runner to 12:45Z) follows under its own pair, which names the characteristics producer at 13:25Z among the
runner's same-day readers.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 5 (2026-10-11 ~13:4xZ) -- HG-t-5 (the runner 06:00Z -> 12:45Z), half v2 @bdee8ed6e1: SIGNED with its two named effects, on one condition

`2.0.0_SA_COO~G1` msg 3896. The preconditions are met: act 1 is CLOSED and HG-t-14 is applied (the characteristics producer at 13:25Z).
The v2 half names two effects v1 missed:
1. **After the move, the `cot-bronze-complete` sentinel invocation (~11:32Z) pulls first**, and the 12:45Z fire is the SKIP-IDEMPOTENT
   backstop. ACCEPTED: an earlier real pull with an idempotent backstop is a better state than designed, and the 13:15Z stamp-gated fire
   reads whichever completed.
2. **The 07:00Z registry rule then finds no roster partition and fails LOUDLY every day** (3 attempts), writing nothing (the served
   registry stays at the 13:15Z fire's). ACCEPTED as a transient state only.

**SIGNED** on one condition: a job that fails loudly every day hides a real failure in its own noise, so the 07:00Z rule is not left
standing.
- Its retirement is its own pair, cut the SAME day as HG-t-5's first 12:45Z fire is read. The read is the 13:15Z-only path serving a
  correct `registry.json` on one day with no 07:00Z write.
- It is applied within one trading day of that read.
- Until then, the 07:00Z failures are named in the HG-t-5 change-management entry as expected, with their count, so nobody chases them.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 6 (2026-10-12 ~13:4xZ) -- HG-t-15 (retire the 07:00Z registry rule): SIGNED, as ADDENDUM 5 required

`2.0.0_SA_COO~G1` msg 4363. Half `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/NEVER_WIDEN_HALF_REQUEST_HEALGAP_R3_ACT_HG_T15_20261012.md` @66473af9cb. Fix 0ef23bcaf5, merged
c866517296.
- **ADDENDUM 5's read is on record:**
  - the first exercised day's 07:00Z rule failed its 3 attempts (07:00:15, 07:01:11 and 07:03:16Z) and wrote nothing;
  - the 13:15Z stamp-gated fire served `registry.json` and `holdings.json`;
  - both ledgers are CLOSED.
  The retirement lands within one trading day of that read, as ruled.
- **The act removes only the rule, its target and its Lambda permission:** writers N = 1, triggers 2 to 1, served delta 0. The function, its role and the stamp-gated rule are
  unchanged.
- **The named loss is accepted:** if HG-t-5 is ever rolled back to the 06:00Z runner, this rule is what would serve the same-day registry again. So HG-t-5's rollback now
  INCLUDES re-applying this rule from its prior tf. It is named in HG-t-5's entry.
- **Row D1-W12-S1 (the LGIC root-map row `cot-satellites-registry-producer-daily`, `root_map.json` line 264):** a retired rule keeps NO registry row. A name the tree no longer
  carries is a false entry. It is removed in the next LGIC registry commit by this seat (the registry's owner), not by this cell, whose grant does not reach it. It is
  harmless meanwhile: the naming gate admits names, it does not create rules. The legacy-transform plan row R-0118 / T-0073 is an immutable run artifact and is not
  edited; the next run will not see the rule.

**SIGNED.**

-- 1.0.0_SA_CTO~DELL1
