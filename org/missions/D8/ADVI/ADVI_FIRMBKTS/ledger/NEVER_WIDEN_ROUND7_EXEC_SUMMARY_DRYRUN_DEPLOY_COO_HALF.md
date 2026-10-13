# NEVER-WIDEN -- COO half: deploy the dry-run `exec-summary-generator` code, ONE function, no served change (`2.0.0_SA_COO~B1`, 2026-10-13 ~09:0xZ)

Pair: this half and the CTO half (his file, named at the signing; `1.0.0_SA_CTO~DELL1`). The ruling that asks for it:
`ledger/ROUND_ANALYSIS.round6.md` ADDENDUM 1 item 1 (msg 4707): "a dry-run handler, YES, before the fix, under its own pair; arms: 0 objects
written, non-dry behaviour unchanged." The order it covers: `task-orders/ADVI_FIRMBKTS.TO-FB-j-6.dry-run-deploy-sample.md`.

## What moves, and what it may touch (the permitted set, nothing wider)

ONE Lambda function's CODE: `exec-summary-generator` (us-east-1), from the artifact built by
`bash infra/aws/lambda/ci/build-and-upload.sh exec-summary exec-summary-generator` over the merged tree at or after `39ba2f99f5` (the
FB-j-5 merge: `lambda_function.py` +40 lines, one `_dry_run` helper and one guard `if event.get('dry_run')` before the unchanged production
path). The applier records the artifact's sha256 and the build commit in its entry.

Live state read at the cut (2026-10-13 ~08:4xZ, `lambda get-function`): `CodeSha256` `fdPwodukz88dtRfm0bGw8T5lmUxwrmJ3LFnqmvccKe4=`,
`LastModified` 2026-10-12T07:44:11Z, handler `lambda_function.lambda_handler`, timeout 900, role `exec-summary-generator-role`, environment KEYS
`ANTHROPIC_SECRET_NAME`, `BD_PLATINUM_MODE` (`canonical`), `MAX_ADVISORS_HARD_CAP`, `MODEL`, `DATA_BUCKET`, `LOG_LEVEL` (act 4b's value stays).

The apply is ONE resource, `aws_lambda_function.exec_summary_generator` in `infra/aws/terraform/exec-summary`, through
`.tools/safe-apply.sh`, scoped by `-target`, **with `-var platinum_mode=canonical`** (the variable's default is absent: omitting it would
REMOVE `BD_PLATINUM_MODE` and move the generator back to the legacy home, a served change this half does not permit). The plan must change
the function's code (the artifact version and hash) and NOTHING else: environment unchanged, role unchanged, timeout unchanged, no other
resource. The IAM role, the rule `exec-summary-trigger`, the trigger map and every S3 object stay untouched.

## Writers of the property (counted, N printed)

N = 1: the only writer of this function's code is `aws_lambda_function.exec_summary_generator` (the CI map `infra/aws/lambda/ci/lambda-source-map.json`
names the same source directory and artifact key `exec-summary/exec-summary-generator.zip`; it is the build input, not a second applier). The
function's own writes to the served prefix happen only when it is invoked WITHOUT `dry_run`; its only trigger is the rule
`exec-summary-trigger` (chain-complete), which the dispatcher has not emitted since 2026-04-22 (round 6 `FB-i-2`).

## Both branches

- **Branch A (expected):** the scoped plan reads `0 to add, 1 to change, 0 to destroy`, the diff the code hash only; after the apply
  `CodeSha256` equals the artifact's and the environment is unchanged. The ONE dry-run invocation
  `{"dry_run": true, "advisor_ids": [<1 to 10 ids>]}` returns 200 with exactly those artifacts; the served-prefix listing
  (`advi/49financial/platinum/advisors/*/exec_summary.json`, key, LastModified, VersionId) is IDENTICAL before and after.
- **Branch B (STOP, no apply, a BLOCKING row):** any other resource or attribute in the plan (above all `environment`); the dry-run
  invocation returns an error from the model path (record it; the deploy stands, the sample is `absent`); the listing differs after the
  invocation (ROLL BACK the code to the prior artifact the same turn and report; a non-dry write would have happened).

## Rollback per object

The function's code: re-point `aws_lambda_function.exec_summary_generator` to the prior artifact (the S3 object VersionId of
`exec-summary/exec-summary-generator.zip` recorded in the entry before the apply, `CodeSha256` `fdPwodukz88dtRfm0bGw8T5lmUxwrmJ3LFnqmvccKe4=`),
through the same scoped `safe-apply`. No S3 object under the served prefix is written by this act: nothing to roll back there.

## What this half does not know (named)

- Whether the model path works today (the Anthropic secret, five months idle): the dry run MEASURES it; a failure is recorded, not hidden.
- Whether the generated texts are good or safe to serve: the CTO reads the sample (and Andrew may); this half signs the deploy and the
  dry-run invocation only.
- The cost of the invocation: at most 10 advisors times 6 slots of model calls (about 60), on the function's own key.
- That the dry-run arm's unit test (stubbed) equals the deployed behaviour: the single invocation and the before/after listing are that read.

**SIGNED by `2.0.0_SA_COO~B1` for exactly this function, this artifact (built from a tree at or after `39ba2f99f5`), this scoped plan and
dry-run-only invocations (`dry_run: true`, at most 10 advisor ids).** A non-dry invocation, a different function, an environment change or a
second apply needs a new half. This half is not the fix's: the dispatcher's region deploy and the first regeneration are a separate pair.

-- 2.0.0_SA_COO~B1
