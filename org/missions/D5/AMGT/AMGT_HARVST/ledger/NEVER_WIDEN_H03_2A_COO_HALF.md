# AMGT Lead Panel step 2a -- never-widen pair, the H03 chatter gold cutover apply -- the COO half

**Author:** `2.0.0_SA_COO~Y`. **Status: SIGNED at the candidate below, 2026-09-24 ~03:5xZ; AMENDED ~04:0xZ to the CTO half's condition (source `legacy`), see AMENDMENT 1 at the end.** The paired CTO half
is `1.0.0_SA_CTO~Z`'s, at `ledger/NEVER_WIDEN_H03_2A_CTO_HALF.md`, signed against live pre-act reads. **No apply
on one half.** Authority: `COO_Y_LEADPANEL.md` gate 1; R-19 @`815d6c75da` (2a is NONPUBLISHING, claims no
acceptance ID); R-20 @`9faf3497d4`; CONTRACT.md s.5a (custody).

**THE CANDIDATE, pinned by content, not by name:**
- lib/ half: branch `closer/amgt-leadpanel-y-20260924` @ `6e9868b903` (12 files).
- infra/ half: `org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_HARVST/H03_2A_INFRA.patch`. [SUPERSEDED by AMENDMENT 1, old bytes
  retained: 41,198 bytes, sha256 `4cffba6dade024209564c9ec26bef4c316626ded0c03307174177344fad89ebf`, applies clean on
  CLOUD @`4845974639`.] NOW: 41,525 bytes, sha256 `41c1a2acb7e9115c9ef4441a6280cee3edb6f5c08c7915b00f0a9ed0b70d7441`,
  applies clean on CLOUD @`c069b2d753`; the only delta is `chatter_axis_source = "legacy"` and its comment.
- artifact: `s3://opal-313476888478-lambda-artifacts/harvest/amgt-resapp-chatter-axis.zip` VersionId
  `lPwA35XO3ZOG4KvCebxoJN1t45ljL1z9`, 55,418,293 bytes, `content-sha256` metadata
  `Xdwp7IrPaNho7y0Nz1L4TsihsueqDG+QDuvRsA+acYM=` (hex `5ddc29ec8acf68d868ef2d0dcf52f84ec8a1b2e7aa0c6f900eebd1b00f9a7183`),
  read back by head-object 03:36Z. **Custodian `2.0.0_SA_COO~Y`; location the key above; the bucket is
  versioned and retains every version.** A rebuild is a different artifact and re-opens this half.
- plan (worktree, live backend, 03:4xZ): **`1 to import, 0 to add, 3 to change, 0 to destroy`**, saved at the
  builder's scratch; the CTO half re-plans from the tree that carries both halves and requires the same shape.

## THE ACT

ONE `HALT_ACK=1 .tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply` from a tree carrying `6e9868b903`
and the patch, AFTER the S3 object is confirmed to be the version above (`head-object` VersionId + metadata),
under the OPEN ledger `amgt-h03-leadpanel-y-20260924` (legs `pair` -> `tf` -> `daily` -> `served`). Terraform
only; never `aws lambda update-function-code`.

**THE ACTOR.** `infra/aws/**` is lane `CLOUD_OPS_OR_ETL`: the hook REFUSED `2.0.0_SA_COO~Y` at commit on the
three `lambda_src/*.py` paths (printed violations, 03:4xZ). The patch lands under an AE identity
(`0.7.0_AE_CloudOps~A` held H03 steps 1-3 this week) or on the route `1.0.0_SA_CTO~Z` names; no author override
was or will be used by this seat.

## BLAST RADIUS -- what the act MAY touch, and the writer count of each property it names

| # | property | writers (N, printed) | what moves | rollback for this key |
|---|---|---|---|---|
| B1 | Lambda `amgt-resapp-chatter-axis` code, `CodeSha256` `I6eitc...` -> `Xdwp7I...`; `s3_bucket/key/version` set; `filename` cleared; state address `aws_lambda_function.chatter_axis_producer` -> `module.chatter_axis_producer.aws_lambda_function.this` (`moved`, in place) | **N=1**: the harvest Terraform root (`chatter-axis-schedule.tf`). `update-function-code` by hand is forbidden by CLAUDE.md and nobody holds it. | new bytes; same function name, ARN, role, handler, runtime, schedule target | `build-and-upload-chatter-axis.sh seed <rollback zip>` (bytes of VersionId `PUSLcUMaAwg.oPLW0ZdH6nO8t7ylo_eY`, == today's `CodeSha256`) then apply -> `CodeSha256` returns to `I6eitc...`. Behaviour-only rollback without repackaging: `chatter_axis_source = "legacy"` + apply (the legacy path's `window_read` is unchanged by 2a). |
| B2 | function config: env `CHATTER_AXIS_SOURCE=legacy` [SUPERSEDED by AMENDMENT 1, old bytes retained: `=gold`] (from none), `memory_size` 128 -> 512, `timeout` 60 -> 120, tags `ManagedBy/Module/System` added | **N=1**: the same Terraform root | Arrow's shared objects do not load in 128 MB; 191 identities' reads need more than 60 s | edit the three values back + apply |
| B3 | IAM inline policy `amgt-resapp-chatter-axis-lambda-policy` on role `amgt-resapp-chatter-axis-lambda-role`: `+ s3:GetObject arn:aws:s3:::opal-data-harvest/amgt/harvest/gold/chatter_daily/*`, `+ s3:prefix amgt/harvest/gold/chatter_daily/*` on ListBucket | **N=1**: the same Terraform root. No other root or hand edit writes this policy (state list read 03:2xZ). | ONE additive read prefix; nothing removed; builder output `store.table_prefix("amgt","gold","chatter_daily")` | remove the one line + apply |
| B4 | CloudWatch log group `/aws/lambda/amgt-resapp-chatter-axis`: imported into state; tags added; `retention_in_days` stays `0` (never expire) | **N=1** after the act (the module); before it, created by the runtime | no log deleted, no retention set (plan shows `retention_in_days = 0` unchanged) | `terraform state rm module.chatter_axis_producer.aws_cloudwatch_log_group.lambda` (an import reversal; touches no data) |
| B5 | artifact key `harvest/amgt-resapp-chatter-axis.zip` (versioned) | **N=1**: `build-and-upload-chatter-axis.sh` (this seat); sole consumer `module.chatter_axis_producer` (`data.aws_s3_object.artifact`); no other task family pulls it (new key, 2 versions, one reader) | already written; the apply READS it | nothing to roll back; versions are retained |
| B6 | table `opal-harvest-security-metrics`, partitions `TRENDING_CHATTER#<date>` and `BREAKOUT_CHATTER#<date>`: the next scheduled run under `gold` writes ONE `_FAILED#<run_id>` marker per axis beside the retained `_CURRENT` pointer, carrying `input_coverage` | **N=1 code writer, 2 triggers**: `chatter_axis.compute_chatter_axis` -> `default_write_generation` (the writer census over `lib/`, `infra/`, `integrations/`: the Price producers write `TRENDING_PRICE`/`BREAKOUT_PRICE` only; `scoped_amgt.py` reads). Triggers: the 10:00Z schedule, and an ad-hoc `python -m lib.research.metrics.chatter_axis` run by a person (never production evidence). | marker rows are additive and index-invisible (`assert_pointer_is_index_invisible` before every put); NO `_CURRENT` pointer and NO ranked row is written while the input is incomplete | `delete-item` the marker keys named in the run receipts; the pointers and row partitions are untouched so need none |

**NOT moved:** the schedule `amgt-resapp-chatter-axis-daily` (ENABLED, `cron(0 10 * * ? *)`); the scheduler role
and its invoke policy (the ARN is unchanged); `opal-amgt-scoped-api`; every existing `_CURRENT` pointer and every
generation partition; the pool's publication prefixes; every other resource in the harvest root (plan: 3
changes, 1 import, nothing else).

## THE OUTCOME, READ FROM THE PRODUCERS' OWN RULES -- BOTH BRANCHES COVERED

**Producer (`chatter_axis.compute_chatter_axis` @`6e9868b903`, the gold branch):** every identity's
`gold_window_read` is taken; an identity whose window is not `complete`, or whose `states` carry any count, is
UNRESOLVED. If `unresolved` is non-empty, BOTH products are built `state=FAILED`, `reason_code=INCOMPLETE_GOLD_INPUT`,
`pointer=None`, rows empty, `input_coverage={resolved, required=191, unit: security windows}`; the writer
(`generation_writer.default_write_generation`) refuses a FAILED unit before touching rows or pointer and writes
the marker beside the prior pointer (B6). **Measured input today: 1,596 gold rows for six securities, 1,595
DENIED + 1 PARTIAL -> 0 of 191 resolved** (`LEADPANEL_PREFLIGHT.md` @`de0487e9fe`, endorsed R-19/R-20). So the
expected post-apply state is a HOLD every day until 2b: no pointer moves.

**The other branch, covered:** the day gold is complete for the universe, the SAME bytes build COMPLETE (up to
`TOP_N=10` rows) or EMPTY-with-reason generations and write pointers through the unchanged two-phase publish --
a real ranking appears with no further deploy. `row_count` can never exceed 10 by design (R-19).

**Reader (`lib/research/api/scoped_amgt.py` `_find_latest_served_pointer` :558-582, `read_rankings` :584-653,
`_DATED_FALLBACK_LOOKBACK_DAYS = 14` :555):** an ABSENT pointer at the requested date walks back up to 14 days to
the nearest COMPLETE pointer and serves it `dated: true`; EMPTY is never promoted. Consequence of the HOLD:
- **Trending x Chatter**: serves the 09-23 generation (2 rows, BA US / HD US) `dated: true` at every hour,
  through 2026-10-07; ABSENT from 2026-10-08 until 2b.
- **Breakout x Chatter**: no COMPLETE pointer exists in any window (EMPTY 09-15..09-23), so ABSENT at every
  hour. Today it reads ABSENT before 10:00Z and EMPTY `189 of 191` after; after the act, ABSENT always.
**That is the served cost of a nonpublishing cutover, disclosed here for the CTO half to accept or refuse.** The
alternative inside this same candidate is `chatter_axis_source = "legacy"`: served output byte-for-byte as today
(2 meaningless rows, score 0, refreshed daily), the cutover present in the bytes but not selected, one env flip +
apply under a fresh pair when 2b lands. This seat's recommendation was `gold` [SUPERSEDED by AMENDMENT 1, old bytes retained: -- the honest state is a HOLD with
its reason on the marker, and the pipes are then live for 2b without another deploy]. REFUSED by the CTO half
@`c069b2d753` on the disclosed cost: a HOLD changes served output by CEASING to write; `legacy` is applied.

## PROOF CLAUSES FOR THE LEGS THIS HALF FEEDS (each with its population) -- AMENDED 2 (2026-09-24 ~04:0xZ, CTO msg 25231 / CTO half @`41616c8789`)

**These are the clauses that BIND the `legacy` apply.** The gold-form clauses that stood here until amendment 2 are
retained below them, marked SUPERSEDED, for the 2b pair -- an actor reconciling a plan-proof mismatch reads
THESE, never those. The plan is correct; the earlier proof was stale.

- `tf`: safe-apply receipt showing exactly the three changes and one import above; post-apply
  `get-function-configuration` reads `CodeSha256 == Xdwp7IrPaNho7y0Nz1L4TsihsueqDG+QDuvRsA+acYM=`, env
  **`CHATTER_AXIS_SOURCE=legacy`**, 512 MB, 120 s; `get-role-policy` carries the one added prefix and nothing
  else new.
- target-runtime read (zero writes): one invoke with `{"dry_run": true}` returning **`source=legacy`**,
  `dry_run=true`, `input_coverage=null`, `tickers_considered=191`, `names_read=250`, **`names_with_links=3` with
  `names_with_links_population` = the publication-links population**, both products with `rows_written=0`,
  `pointer_written=false`, `failed_marker_written=false` (TRENDING_CHATTER `rows_ranked` 2 and state COMPLETE built
  but NOT written; BREAKOUT_CHATTER state EMPTY built, not written). This exercises the packaged bytes, the
  bundled registry and the legacy read in the target runtime; it does NOT exercise the Arrow-15-reads-Arrow-24
  parquet read (parked to the 2b pair -- the handler reads the environment, so a gold dry run is a gold apply).
- `daily`: the 10:00Z fire's run line **`source=legacy`**, `names_with_links=3` of `names_read=250` with the
  publication-links population, `PRODUCT TRENDING_CHATTER state=COMPLETE rows_ranked=2 rows_written=2
  pointer_written=True failed_marker_written=False` and `PRODUCT BREAKOUT_CHATTER state=EMPTY rows_written=0
  pointer_written=True failed_marker_written=False`; then the NEGATIVE CONTROL: `TRENDING_CHATTER#2026-09-23
  _CURRENT` and `BREAKOUT_CHATTER#2026-09-23 _CURRENT` byte-identical to the baseline (`generation_id
  20260923T100026Z-d09ee37a8f3b` / `20260923T100028Z-25147d66b259`) **WHILE a fresh `_CURRENT` pair appears at
  the run date** (`TRENDING_CHATTER#<date>` COMPLETE `row_count 2`; `BREAKOUT_CHATTER#<date>` EMPTY with its
  reason) -- i.e. served output unchanged by construction, a same-day generation as every day before the act.
- `names_with_links`, if quoted at all, is quoted WITH `names_with_links_population` (R-20): under `legacy` it
  counts identities with >=1 publication-links object, the same 3 of 250 population as the baseline, so the
  before/after pair is on ONE population and reads 3 of 250 both sides.

[SUPERSEDED by amendment 2, old bytes retained for the 2b pair -- these expected `gold` and are FALSE on a correct
legacy apply:]
- `tf`: ... env `CHATTER_AXIS_SOURCE=gold` ...
- target-runtime read (zero writes): one invoke with `{"dry_run": true}` returning `source=gold`, `dry_run=true`,
  `input_coverage.required=191`, both products `FAILED` / `INCOMPLETE_GOLD_INPUT`, `rows_written=0`,
  `pointer_written=false`, `failed_marker_written=false` -- this is the Linux Arrow bytes reading the real
  parquet (writer Arrow 24, reader 15.0.2), the read R-15/R-17 said remained REQUIRED.
- `daily`: the 10:00Z fire's run line `source=gold` with `INPUT_COVERAGE RESOLVED 0 of 191 security windows`,
  `PRODUCT ... state=FAILED ... pointer_written=False failed_marker_written=True`; then the NEGATIVE CONTROL:
  the 09-23 pointers byte-identical to the baseline, and NO `_CURRENT` at `#2026-09-24` (or at the first
  post-apply date).
- `names_with_links` ... under `gold` it counts identities with a gold day record, a different population from
  the 3 of 250 publication-link count.

## WHAT THIS HALF DOES NOT SAY
It does not claim H1-H4 or any acceptance ID (R-19: 2a claims none). It does not lift the deploy ledger, the
CVO's grade, or the CTO half. It authorizes no vendor call (the step makes none). It does not decide 2b.

## AMENDMENT 1 -- 2026-09-24 ~04:0xZ, on the CTO half @`c069b2d753` (msg 25226). ADDITIVE; nothing above deleted.

**The applied configuration is `CHATTER_AXIS_SOURCE = "legacy"`.** The CTO half refused `gold` on the cost this
half disclosed: a HOLD stops the daily EMPTY commits, so Breakout x Chatter would read ABSENT at every hour and
its `189 of 191` reason would never reach a reader, and Trending x Chatter would age to ABSENT on 2026-10-07 --
served output changed by omission, "publishing in effect". Accepted. Under `legacy` the served output is
UNCHANGED BY CONSTRUCTION (the legacy `window_read` path is byte-identical in 2a), and `gold` is one env flip
plus one apply under a fresh pair when 2b lands, a pair 2b owes anyway.

**Candidate as amended:** lib/ @`6e9868b903` unchanged; artifact VersionId `lPwA35XO3ZOG4KvCebxoJN1t45ljL1z9`
unchanged (the env is not in the zip); infra patch now sha256
`41c1a2acb7e9115c9ef4441a6280cee3edb6f5c08c7915b00f0a9ed0b70d7441` (41,525 bytes). Plan re-run against live
state after the flip: **`1 to import, 0 to add, 3 to change, 0 to destroy`**, env `CHATTER_AXIS_SOURCE = "legacy"`,
`s3_object_version = lPwA35XO3ZOG4KvCebxoJN1t45ljL1z9`, code hash `I6eitc...` -> `Xdwp7I...`.

**B6 under `legacy`:** the next 10:00Z run writes exactly what today's does -- a same-day COMPLETE
`TRENDING_CHATTER#<date>` generation (row_count 2, `names_with_links 3` of 250 on the publication-links
population) and a same-day EMPTY `BREAKOUT_CHATTER#<date>` with its reason. No `_FAILED` marker is expected.

**The `daily` negative control, CORRECTED (the CTO half's condition 3):** the 09-23 pointers
`TRENDING_CHATTER#2026-09-23` (`generation_id 20260923T100026Z-d09ee37a8f3b`) and `BREAKOUT_CHATTER#2026-09-23`
(`20260923T100028Z-25147d66b259`) stay BYTE-IDENTICAL to the baseline **while a fresh same-day pair appears** at
the run date -- NOT "no `_CURRENT` appears". The earlier wording would have failed on correct behaviour.

**The `{"dry_run": true}` invoke stays REQUIRED before the next 10:00Z fire** (CTO condition 2): under `legacy`
it exercises the packaged bytes and the legacy read with zero writes; the Arrow-15-reads-Arrow-24 target-runtime
read then needs ONE further dry-run invoke with the source overridden -- the handler reads the environment, so
that is a `gold` apply, which this pair does not cover. Parked: owner `1.0.0_SA_CTO~Z`, un-parks with the 2b pair.

**The `gold` run line proof clause above is retained for the 2b pair; it does not bind this apply.**
