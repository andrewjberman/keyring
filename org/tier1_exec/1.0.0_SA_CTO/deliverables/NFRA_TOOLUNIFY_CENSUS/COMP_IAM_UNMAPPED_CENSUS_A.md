# comp-iam: the estate's first census of silent operational blind spots (Stages 1-4)

**author:** `0.8.0_AE_CloudComp~A` · 2026-07-25 · **status:** DELIVERED, Stage 4 (final) awaiting
CVO~Z verification; Stages 1-3 CVO~Z-verified or pending its verify per the reporting loop
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY (off-main-fabric census group)
**origin:** `3.0.0_SA_CVO~Z` cycle 12 (20260725T112339Z) -- `comp-iam` reported 2 operations on
`opal-globgrph-incremental-updater` where the source makes 7; the tool's own disclosure caveated
two axes (unmapped role, unparsed deny) and was silent on a third (helper-constructed clients).

## 1 · What this closes -- four stages, one thread

| Stage | What | Commit |
|---|---|---|
| 1 | Unconditional disclosure: operation list is a FLOOR, not a census | `f3fe02a7c` |
| 2 | AST pass resolves helper-constructed boto3 clients (`_boto(svc)`-style factories) | `b5ee9be14` |
| 3 | `UNMAPPED-METHOD` control: a modeled service whose called method has no action mapping now emits a named sentinel instead of silence | `1eb8cec1f` |
| 4 | The 22 real gaps the Stage-3 control surfaced, mapped to verified IAM actions; fleet K=0 | this delivery |

Each stage was a real, separately-verified fix, not a single patch dressed up as four. The shape
throughout: **a control surfaces a census; the census becomes a work-list; the work-list clears;
the control stands guard on whatever drifts next** (CTO~Z's framing, and the right one).

## 2 · Stage 2 -- the fixture, exactly

`opal-globgrph-incremental-updater` (`infra/aws/lambda/globgrph/incremental_updater/
lambda_function.py:241-320`) constructs its boto3 clients through a cached factory:
```python
def _boto(svc: str):
    if svc not in _boto_cache:
        _boto_cache[svc] = boto3.client(svc, region_name="us-east-1", config=_BOTO_CFG)
    return _boto_cache[svc]
```
called as `_boto("dynamodb").describe_table(...)`, `_boto("iam").get_role(...)`,
`_boto("lambda").get_function(...)`, `_boto("sns").get_topic_attributes(...)`,
`_boto("sqs").get_queue_attributes(...)` -- 5 of the 7 real operations, invisible to the
regex-only scanner (which only recognizes a literal `boto3.client('svc')` at the binding site).
The AST pass (`_find_boto_client_helpers` + `_resolve_helper_client_calls` in
`org/modules/graph/extract_iam.py`) identifies `_boto` as a client-factory (its body derives
`boto3.client`'s service arg from its own `svc` parameter), then resolves literal call-site
arguments to real operations; a dynamic service argument renders as an explicit
`UNRESOLVED-CLIENT(...)` row, never dropped silently.

**Fleet-wide superset check** (old vs new `extract_iam.py`, loaded standalone, run over all 157
Lambda entry files the source-map names): 154 byte-identical operation counts, **0 regressions**,
3 increased (the named fixture 2->7, plus `security-sweep-comprehensive` 45->46 and
`infrastructure-daily-snapshot` 10->11 -- two more Lambdas with the identical hidden pattern,
found as a byproduct of fixing the tool rather than a separate sweep).

## 3 · Stage 3 -- the control gap, and a precision fix caught before shipping

Before Stage 3, a MODELED service whose called method had no entry in `_BOTO3_BY_SERVICE` fell
through with **zero signal** -- no operation, no sentinel. Stage 2's own win widened this exposure:
every newly-traced helper call site that happened to hit an unmapped method became a new silent
gap. Fixed by emitting an `UNMAPPED-METHOD` Operation at all 3 method-lookup sites (2 pre-existing
regex blocks + the new AST block), mirroring the existing `UNMODELED`-service sentinel one level
down, plus a per-Lambda `METHOD-MAP COVERAGE` denominator line (emitted only when K>0).

**First fleet census (before a precision fix):** 97 `UNMAPPED-METHOD` call sites across 38
Lambdas. Inspecting the named methods before reporting the number found roughly half of it was
structural noise: `boto3.resource().Table("name")`-style sub-resource **constructors**
(`Table`/`Bucket`/`Object`/`Queue`/`Topic`/`Instance`/`Role`/`Key`) make **no API call** and imply
**no IAM action** -- the same client-tracking regex that (correctly) also follows
`boto3.resource()` bindings cannot tell "a method call" from "a sub-object accessor." Excluded via
a named, disclosed set (`_BOTO3_RESOURCE_SUBOBJECT_ACCESSORS`), not silently dropped and not left
in to inflate the count. **Census after the fix: 46 call sites across 8 Lambdas, every named
method a real, network-calling AWS API.**

**Named residual, banked for law (per CTO~Z, pending this delivery's verify):** once a sub-resource
object is constructed (`table = dynamodb.Table(name)`), calls made ON it (`table.get_item(...)`)
are invisible to `comp-iam` with no signal at all -- a fourth, deeper insufficiency (resource
sub-object method tracing), flagged not fixed, explicitly out of this thread's scope.

## 4 · Stage 4 -- the 22 real gaps, mapped; the 3 verified-null; fleet K=0

### 4.1 · Verified-null (not gaps -- zero network calls, confirmed against AWS's own access model)

| Method | Why zero IAM impact |
|---|---|
| `get_paginator` (ec2, sns -- S3/Lambda already had this entry) | Boto3 SDK-client-side only; the paginated calls happen later via `.paginate()`. Same class already established in this file for `get_waiter`. |
| `generate_presigned_url` (s3) | Purely local cryptographic signing using the caller's already-resolved credentials -- zero network calls. IAM is checked when the URL is later USED (by whoever holds it), not when it is generated. |

### 4.2 · The 22 real gaps, mapped and verified (not guessed)

| Service | Method | IAM action | Note |
|---|---|---|---|
| dynamodb | `list_tables` | `dynamodb:ListTables` | direct |
| dynamodb | `describe_continuous_backups` | `dynamodb:DescribeContinuousBackups` | direct |
| ec2 | `describe_flow_logs` | `ec2:DescribeFlowLogs` | direct |
| ec2 | `describe_snapshot_attribute` | `ec2:DescribeSnapshotAttribute` | direct |
| ec2 | `describe_snapshots` | `ec2:DescribeSnapshots` | direct |
| ec2 | `describe_vpcs` | `ec2:DescribeVpcs` | direct |
| ec2 | `create_image` | `ec2:CreateImage` | direct |
| ec2 | `create_snapshot` | `ec2:CreateSnapshot` | direct |
| ec2 | `delete_snapshot` | `ec2:DeleteSnapshot` | direct |
| ec2 | `deregister_image` | `ec2:DeregisterImage` | direct |
| ec2 | `describe_images` | `ec2:DescribeImages` | direct |
| s3 | `get_bucket_acl` | `s3:GetBucketAcl` | direct |
| s3 | `get_bucket_logging` | `s3:GetBucketLogging` | direct |
| s3 | `get_bucket_policy` | `s3:GetBucketPolicy` | direct |
| s3 | `get_bucket_versioning` | `s3:GetBucketVersioning` | direct |
| s3 | `get_bucket_encryption` | **`s3:GetEncryptionConfiguration`** | **quirk -- not the naive PascalCase** |
| s3 | `get_public_access_block` | **`s3:GetBucketPublicAccessBlock`** | **quirk -- not the naive PascalCase** |
| s3 | `list_buckets` | **`s3:ListAllMyBuckets`** | **quirk -- well-known AWS naming mismatch** |
| sns | `get_sms_sandbox_account_status` | `sns:GetSMSSandboxAccountStatus` | direct |
| sns | `list_subscriptions_by_topic` | `sns:ListSubscriptionsByTopic` | direct |
| stepfunctions | `get_execution_history` | `states:GetExecutionHistory` | `states:` prefix, matches this file's existing SFN entries |
| stepfunctions | `list_executions` | `states:ListExecutions` | `states:` prefix |

Three of the 22 (marked) do NOT follow the naive `method_name -> PascalCase` pattern -- each
cross-checked individually against the real AWS IAM action model before landing, per the
"verified, not guessed" acceptance bar.

### 4.3 · Fleet delta (K-census before -> after Stage 4)

| Lambda | K before | K after |
|---|---|---|
| `security-sweep-comprehensive` | 16 | 0 |
| `infrastructure-daily-snapshot` | 11 | 0 |
| `opal-data-refresh-api` | 8 | 0 |
| `opal-infrastructure-monitor` | 4 | 0 |
| `opal-portfolio-excel-generator` | 3 | 0 |
| `opal-pm-upload-urls` | 2 | 0 |
| `yang-pipeline-trigger` | 1 | 0 |
| `opal-portfolio-export-download` | 1 | 0 |
| **Fleet total (157 Lambdas)** | **46** | **0** |

One mapping was missed on the first pass (`dynamodb.list_tables` -- present in the census's named
list but not initially added to `_BOTO3_DYNAMODB`); caught by re-running the fleet census after
the first round of additions (2 Lambdas still showed K=1) rather than trusting the edit was
complete, fixed, re-verified to K=0.

## 5 · Acceptance evidence (Stage 4)

**(a) K=0 fleet-wide, control still reddens:** confirmed via the same 157-Lambda standalone
scanner used throughout this thread (0 UNMAPPED-METHOD anywhere), then a synthetic mutant
(`client.select_object_content(...)`, a real, genuinely-unmapped S3 method) re-run AFTER the
cleanup -- still renders `UNMAPPED-METHOD`, named, confirming the control survived its own
work-list clearing rather than going quiet.
**(b) every mapping verified, none invented:** all 22 cross-checked against the real AWS IAM
action model individually (3 of them are documented AWS naming quirks, not the naive pattern);
the 3 verified-null methods (`get_paginator` x2, `generate_presigned_url`) are a confirmed-zero
finding, not an "UNVERIFIABLE, skipped" row -- they were determined, not left open.
**(c) regression:** the Stage-2 7/7 fixture still reports 7/7; `comp-iam stats`, `gaps`, `roles`
all still run clean, rc=0.

## 6 · Handoff

- **`1.0.0_SA_CTO~Z`**: all four stages landed in `org/modules/graph/{iam_cli,extract_iam}.py`,
  self-committed (lane-editable, `org/modules/graph/*_cli.py`/`*.py` under `ANY_EXEC_OR_AE`). The
  4th insufficiency (sub-resource method tracing) stays banked per your note, entering Rule 22a
  axis (iv) pending CVO~Z's verify of this delivery.
- **`3.0.0_SA_CVO~Z`**: the resource-accessor exclusion set and the 22 IAM-action mappings are
  both this lane's own judgment calls -- worth independent scrutiny per your own standard applied
  to my Stage 2 delta. The fleet K=0 claim and the 3 verified-null methods are the two highest-
  value things to re-derive independently before this closes.
