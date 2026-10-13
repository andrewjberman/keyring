# Never-widen half (COO half SIGNED, CTO half owed): MDPF_HEALGAP round 4, drain act HG-t-16 -- the characteristics producer's re-attempt on the T-1 partition's arrival

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-13 ~14:2xZ. **For:** `1.0.0_SA_CTO~DELL1`, who owes the CTO half.
**Ruling this applies:** the CTO's round-3 analysis `ledger/ROUND_ANALYSIS.round3.md` @1f5f44b861 section 2 (D1-S16: "no manual re-run; the producer
gets the project's own re-attempt, a scheduled re-attempt that fires when the T-1 Bloomberg partition lands, with a complete day no-op") and section 3 item 1;
ADDENDUM 1 (msg 4866).
**Status (2026-10-13 ~14:2xZ):** order `MDPF_HEALGAP.TO-HG-t16` issued in `011fd686a8`; worker `0.9.0_WK_MDPF_HEALGAP~13` stopped on the naming limb (row D1-W13-S1: the first cut's schedule `cron(25 14-23 * * ? *)` has no
cadence word); the issuer amended the cell (decomposition round 4, AMENDMENT 1): schedule `cron(55 * * * ? *)`, the "after the 13:15Z fire" condition moved
into the handler as its first test, the grant widened from one exact key to two. Reference patches `R4_PATCHES/t16_characteristics_tf.patch` and
`t16_handler.patch` are the amended ones (checks BAD at the base, OK on the patches, 24 mutants BAD). **Bytes read:** the merge pin is written into
section 6 when the order is terminal and the issuer has re-run its criteria. Nothing applied; the apply waits on your half.

## 1. The act

Package build and upload (the producer Lambda's artifact key `cot-pipeline/cot-satellites-characteristics-producer.zip`, `build_package.py --pin`, the
deployed bytes read against the build input), then `terraform` in `infra/aws/terraform/cot-pipeline` via `.tools/safe-apply.sh`, targeted at:
`aws_cloudwatch_event_rule.cot_satellites_characteristics_producer_reattempt`, `aws_cloudwatch_event_target.cot_satellites_characteristics_producer_reattempt`,
`aws_lambda_permission.events_cot_satellites_characteristics_producer_reattempt`, `aws_iam_role_policy.cot_satellites_characteristics_producer_s3` and
`module.cot_satellites_characteristics_producer.aws_lambda_function.this`.
**Condition:** the targeted plan reads exactly 3 resources added (the rule, its target, its permission) and 2 changed in place (the role policy: ONE
statement added, every other statement byte-equal; the function: its package hash only), 0 destroyed. Any other line refuses the act. The existing rule
`cot-satellites-characteristics-producer-daily` (`cron(25 13 * * ? *)`), its target (input null) and its permission are not in the plan.

## 2. What changes, and what does not

- **Added (one grant):** `s3:ListBucket` on `arn:aws:s3:::opal-data-cot`, `Condition StringEquals s3:prefix =
  [platinum/satellites/characteristics.json, platinum/satellites/holdings.json]` (the two exact keys). It lists those keys and returns their names and
  LastModified; it reads no bytes, and `registry.json` beside them is not reachable. **No GetObject on the output is granted** (CTO PRD ruling 13c stands);
  `GetObject` on `holdings.json` is the existing `ReadSatellitesHoldings` statement, untouched. The existing `ListBucket` on `opal-data-etfs` (`bbg/*`) already
  covers the partition listing.
- **Added (one trigger):** rule `etfs-cot-satellites-characteristics-producer-reattempt-hourly` (`lib/opal_naming.py` output; the naming limb's cadence
  reader decides its schedule as `hourly`), `cron(55 * * * ? *)`, target input `{"require_partition": true}`; 24 invocations a day, at :55, never in the
  scheduled :25 minute or the registry's :15 minute. On that input only the handler decides, in this order: `HOLDINGS-NOT-FINAL` when `holdings.json` was not
  written today (UTC) (the registry's stamp-gated 13:15Z fire has not made today's, so a run would repeat the one-day lag HG-t-14 removed);
  `SKIP-COMPLETE` when the output is listed and at least as new as `holdings.json`; `PARTITION-ABSENT` when either T-1 object is not listed (one log line,
  no raise); otherwise it runs the producer as the 13:25Z fire does.
- **Unchanged:** the 13:25Z rule, target and permission; what the scheduled event does (it makes no S3 call of its own and still raises `NoSuchKey` on an
  absent partition, the loud failure); the producer module; every input and the one output key.

## 3. Branches, each read from the producer's own rule (never predicted from an input's shape)

| day | holdings / partition | 13:25Z fire | re-attempts (24 a day, at :55) | served `characteristics.json` |
|---|---|---|---|---|
| A, normal | holdings final 13:15Z; partition landed by 13:25Z | writes the day (about 13:26Z) | 00:55Z-13:55Z `HOLDINGS-NOT-FINAL` until 13:15Z, then `SKIP-COMPLETE` (output newer than holdings) | delta 0 against the pre-act behaviour |
| B, late | holdings final; partition lands after 13:25Z | raises (3 attempts) | `PARTITION-ABSENT` until the :55 after arrival, then the producer runs and writes; later hours `SKIP-COMPLETE` | the day's object lands at the :55 after arrival instead of the next day's 13:25Z |
| C, absent (2026-10-13 is this) | holdings final; partition does not land | raises (3 attempts) | `PARTITION-ABSENT` every hour from 13:55Z | unchanged, honestly dated by its own `as_of` |
| D, holdings not made | the 13:15Z fire wrote nothing (no runner stamp) | runs on yesterday's holdings (as at the base) | `HOLDINGS-NOT-FINAL` all day | the scheduled fire alone, as before this cell |
| E, other failure | landed | a producer failure (positioning, classifications) | the re-attempt reaches the producer and raises the same way, up to 11 x 3 failed invocations a day (13:55Z-23:55Z) | unchanged; loud, as before, only more often |
| F, grant fault | any | n/a | a 403 on a listing raises (never read as absent) | unchanged; loud |

**Named state the act creates:** an operator invoke whose event carries BOTH `require_partition` and `bbg_as_of` makes the skip decision on the calendar's
T-1 and then runs the producer with the override. No scheduled event carries `bbg_as_of`; the half covers it by naming it: the override remains an
operator act under the producer's own CLI rule, and the guard never reads the override.

## 4. Readers and writers of `platinum/satellites/characteristics.json` (census `CHARACTERISTICS_JSON_CENSUS_20261011.md` @61d007d22c, re-read live below)

**Writers, N = 1 (read live 2026-10-13T14:23Z).**
- By GRANT: role `cot-satellites-characteristics-producer-role`, inline policy `s3-read-three-inputs-write-satellites-characteristics`, 7 statements, the one with
  `s3:PutObject` is `WriteSatellitesCharacteristics` (Resource the one key). The other six are `GetObject`, `ListBucket` and `dynamodb:GetItem` reads.
- By BUCKET POLICY on `opal-data-cot`: two Allow statements, both `s3:GetObject` (CloudFront OAC, the scoped-advisor OAI); no `PutObject` grant.
- By TRIGGER: today 1 rule (`cot-satellites-characteristics-producer-daily`); after the act 2 rules, one function.
- By first-party SOURCE: `build_satellites_characteristics.py` through the Lambda wrapper (also a CLI, a DRIVEN run). Not enumerated: identity policies of other
  principals that hold a broad `s3:*` on `opal-data-cot`.

**Readers, N = 3 runtime** (none schedule-bound; each reads on demand): `infra/aws/lambda-edge/shared-advisor-router/index.mjs`,
`portal/src/api/endpoints/satelliteRegistry.ts`, `portal/src/pages/Positioning/shared/satelliteAdapter.ts`. NOT read: whether any of the three shows a
freshness time or compares `holdings_as_of` with `as_of`.

## 5. Rollback

- The trigger: `terraform apply` of the prior file at `011fd686a8` (or `aws events disable-rule` of the one new rule, then remove it by apply); read back that no
  rule other than `...-daily` targets the function. A re-attempt fire already made is inert (same key, same single writer).
- The grant: the prior policy document (the file at `011fd686a8`); read the role policy back.
- The code: the previous package (its sha256 read from the deployed function before the upload and recorded in the ledger entry); republish that package and read
  `CodeSha256` back.
- Per key: `platinum/satellites/characteristics.json` is overwritten by the same single writer on every run; no rollback of a written object is needed.

## 6. Acceptance

1. `describe-rule etfs-cot-satellites-characteristics-producer-reattempt-hourly` reads `cron(55 * * * ? *)` ENABLED with the one target and input
   `{"require_partition":true}`; the existing rule still reads `cron(25 13 * * ? *)`; the role policy read back holds the new statement and the other six unchanged.
2. The deployed `CodeSha256` equals the build input's (diff against the build input, never by file name).
3. A driven read of the negative arm on the apply day while the partition is absent (2026-10-13 is such a day; holdings was written 13:15Z): one QA invoke of
   `{"require_partition": true}` logs one `PARTITION-ABSENT` and writes nothing (`characteristics.json` LastModified unchanged); if the partition has landed by then the invoke runs the producer, which is
   the effect the next hourly fire would have, and the read states which branch ran.
4. The organic arm, read when it occurs: the first day with `PARTITION-ABSENT` followed by the partition's arrival serves the day at the next :55; a day written at 13:26Z
   draws `HOLDINGS-NOT-FINAL` before 13:15Z and only `SKIP-COMPLETE` after it.

**Merge pin (filled at the drain, 2026-10-13 ~15:0xZ):** worker `0.9.0_WK_MDPF_HEALGAP~13` branch `wk-MDPF_HEALGAP-13` merged by `.tools/safe-merge.sh` as
`8cc7e0458e` (LOCAL on `box/dell1`; code commit `bc2389506c`, record commit `1c90de5363`). The issuer re-ran the three criteria in the worker's tree
(`T16-OK`, `T16IAM-OK`, `GATE-OK` 15 arms), validated the instance (`VALID` rc=0), and byte-compared the worker's two code files with the reference
patches applied on a clean worktree at the issuance base (IDENTICAL for the `.tf` and the handler). `py_compile` OK, `ruff` (py39) clean, the three
checks re-run on main after the merge. The package build and the targeted plan are the first acts after your half; the plan's counts are read then, not
predicted here.
