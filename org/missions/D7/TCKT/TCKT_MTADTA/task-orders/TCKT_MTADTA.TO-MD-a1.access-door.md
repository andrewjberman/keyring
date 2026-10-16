# TO TCKT_MTADTA.TO-MD-a1 -- the access door: IAM group, role, the one reader/writer Lambda, and the two single-principal policies

<to_id>TCKT_MTADTA.TO-MD-a1</to_id>
<project>TCKT_MTADTA</project>
<issued_to>0.9.0_WK_TCKT_MTADTA~1</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D7 | **Fabric:** dell1 | **Decomp cell:** `MD-a-1` (`decompositions/TCKT_MTADTA_DECOMP.md`) |
**outcome_ref:** FWD-6, FWD-8 | **depends_on:** `MD-h-1` (this slot's previous order; `access.tf` names the resources its `main.tf` declares)

---

## WORKER FACE

### THE CELL

`MD-a-1`, the DOOR. Andrew, 06:2xZ, VERBATIM: "yes, only iam globgrph group can access, if you want to access you have to go through the
reader/writer lambda". PRD C-ACCESS: (1) a NEW IAM group, builder name `globgrph-trino-access-group`; its members, and only they, may invoke
the access Lambda. (2) ONE reader/writer Lambda, `globgrph-trino-access-lambda`, is the only door for reading and writing. (3) Its execution
role, `globgrph-trino-access-role`, is the ONLY principal the bucket policy admits; every other principal is explicitly denied the data
actions, IAM admin users and the account's other roles included. (4) The bucket's KMS key policy admits the same role alone. A bucket policy
cannot name an IAM group as a principal, so the group gates who may invoke and the role gates the bucket. The Lambda returns query results,
never raw bronze objects, and every call is logged.

The previous order of your queue (`TO-MD-h1`) wrote `infra/aws/terraform/trino/main.tf`. READ it first: you reference its labels
`aws_s3_bucket.trino`, `aws_kms_key.trino`, `local.bucket` and `data.aws_caller_identity.current`, and you edit none of them.

### THE DOOR CONTRACT (fixed by the decomposition; build to it exactly)

`handle(event, context=None, s3=None, log=print, silver_reader=None, silver_builder=None) -> dict`. `s3` is an injected client with
`put_object(Bucket, Key, Body, **kw)`, `get_object(Bucket, Key)` (returns `{"Body": <file-like>}`) and `list_objects_v2(Bucket, Prefix)`
(returns `{"Contents": [{"Key": ..}], "IsTruncated": False}`); production code builds the real client only inside `lambda_handler`, which
calls `handle`. Prefix `m365-metadata/trino/`; bucket name read from an environment variable the Terraform sets from `local.bucket`.
Every call writes ONE log line via `log` (the op and the outcome; never a body, never a key's content). Every `put_object` carries
`ServerSideEncryption='aws:kms'`.

| op | request | answer |
|---|---|---|
| `put` | `{op, dataset: bronze\|silver\|state\|gold, key, body_b64}` | `{"ok": true, "key": key}`; `{"ok": false, "error": ...}` when the key is outside the prefix or holds `..` (nothing is written) |
| `get_state` | `{op, key}`, a key under `state/` or `gold/collection_coverage/` only | `{"ok": true, "body_b64": ...}`, or `{"ok": false}` |
| `get_day` | `{op, person, date}`; `person` is one of the eight UPNs, `date` is `YYYY-MM-DD` | `{"ok": true, "rows": [..]}`: the person's silver rows from `silver_reader.read_day_rows(s3, bucket, prefix, person, date)`, filtered to `actor == person` and sorted by `creation_time`; `{"ok": false}` for a non-member, before any S3 call |
| `derive_silver` | `{op, date}` (`YYYY-MM-DD`, Eastern) | lists and reads EVERY bronze object under `.../bronze/audit_events/date=YYYYMMDD/` (gzip JSON lines), calls `silver_builder.build(events) -> bytes`, writes `.../silver/activity_events/date=YYYY-MM-DD/data.parquet` (idempotent rewrite); `{"ok": true, "rows": n}` |
| `get` of bronze, and any other op | -- | `{"ok": false, "error": ...}`; bronze is NEVER returned |

The eight UPNs: `andrew`, `alyssa`, `bobby`, `manav`, `yang`, `menachem`, `jim`, `jeanette`, each `@opalinvest.com`. In production
`lambda_handler` imports `silver_builder` (a sibling module another cell writes at
`infra/aws/lambda/globgrph-trino-access/silver_builder.py`) and a `silver_reader` of your own in `handler.py`; in tests both are injected.

### BUILD

1. **`infra/aws/lambda/globgrph-trino-access/handler.py`** -- the contract above, stdlib plus `boto3` imported lazily inside
   `lambda_handler` only. Python 3.12 runtime.
2. **`infra/aws/lambda/globgrph-trino-access/build.sh`** -- zips `handler.py` and `silver_builder.py` (and nothing else) to
   `build/globgrph-trino-access.zip`; model it on `infra/aws/lambda/transcripts-pull/build.sh` (read it). It does not run `pyarrow`: the
   silver builder uses the AWS-managed pandas layer (a Terraform variable below).
3. **`infra/aws/lambda/globgrph-trino-access/tests/test_handler.py`** -- pytest, the fake client injected, covering every row of the
   table including the refusals.
4. **`infra/aws/terraform/trino/access.tf`** -- every name from the builder, by the same mechanism `infra/aws/terraform/transcripts/pull.tf`
   uses to take names (read it): the group `globgrph-trino-access-group` (`aws_iam_group`), the Lambda role
   `globgrph-trino-access-role` (`aws_iam_role`), the function `globgrph-trino-access-lambda` (`aws_lambda_function`, runtime
   python3.12, handler `handler.lambda_handler`, the zip from `build.sh`, environment `BUCKET` from `local.bucket`, an AWS-managed pandas
   layer ARN taken from a `variable`).
   - **Group policy** (`aws_iam_group_policy`): `lambda:InvokeFunction` on THIS function's ARN and nothing else.
   - **Role policy**: `s3:PutObject`, `s3:GetObject`, `s3:ListBucket` on the bucket and `m365-metadata/trino/*`; `kms:GenerateDataKey`,
     `kms:Decrypt` on `aws_kms_key.trino` with the two conditions of the `transcripts` grant (`kms:ViaService` = S3 in us-east-1; the
     encryption context = this bucket's ARN); CloudWatch Logs create/put on this function's log group (declare the log group).
   - **Bucket policy** (`aws_s3_bucket_policy`): ONE Allow is not needed; write ONE explicit **Deny** of the data actions
     (`s3:GetObject`, `s3:GetObjectVersion`, `s3:PutObject`, `s3:DeleteObject`, `s3:DeleteObjectVersion`, `s3:ListBucket`,
     `s3:ListBucketVersions`, `s3:AbortMultipartUpload`) to every principal whose `aws:PrincipalArn` is not this role (`StringNotEquals`),
     plus a Deny of any non-TLS request. Do NOT deny the bucket-configuration actions (`s3:PutBucketPolicy` and the like): the account's
     administrators keep them, and the residual is stated, not hidden (PRD C-RESIDUAL).
   - **Key policy** (`aws_kms_key_policy` on `aws_kms_key.trino`): the account root ADMINISTERS the key and cannot use it (the
     `RootAdministersTheKeyAndCannotUseIt` statement of `transcripts/main.tf`), and this role USES it (Encrypt, Decrypt, ReEncrypt,
     GenerateDataKey, DescribeKey). No other principal.
   - No wildcard principal, no SNS, no alarm, no notification resource (standing moratorium).

### ACCEPTANCE

<criterion id="MD1-a1-AC1" cell_refs="MD-a-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS/r1_check_a1.py handler</invocation><expect>A1-HANDLER-OK</expect></criterion>
`MD1-a1-AC1` -- the door, driven with a fake client: a put under the prefix lands with SSE-KMS; a foreign or dot-dot key is refused and writes nothing; bronze is never returned; a non-member is refused; every call is logged.

<criterion id="MD1-a1-AC2" cell_refs="MD-a-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/TCKT_MTADTA_R1_CHECKS/r1_check_a1.py tf</invocation><expect>A1-TF-OK</expect></criterion>
`MD1-a1-AC2` -- `access.tf` declares the group, role, function, group policy, bucket policy and key policy, builder-named, with an explicit Deny and no wildcard principal or alarm.

<expected_criteria>MD1-a1-AC1,MD1-a1-AC2</expected_criteria>

Dry-run at the base 2026-10-16 ~06:5xZ: AC1 `A1-HANDLER-REFUSED no handler.py`, AC2 `A1-TF-REFUSED no access.tf` -- each FAIL as expected;
AC1 was also driven GREEN against a throwaway reference outside the repository. Run from the repository (worktree) root.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **WORLD by the gate's path floor; NOTHING is applied.** No `terraform apply`/`init` against the backend, no AWS call, no S3 access, no
  Lambda invoke. `terraform fmt -check` is welcome (no network).
- `silver_builder.py` is another cell's file (`MD-s-1`): never create or edit it. Your tests inject a stub with `build(events) -> bytes`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `TCKT_MTADTA-D1-W1-S<k>`), and do not weaken a check to pass it.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_TCKT_MTADTA~1 <0.9.0_WK_TCKT_MTADTA~1@opal.agent>"`, `-F` a message
  file you write with the Write tool, and `-- <paths>`.

<paths>
infra/aws/terraform/trino/access.tf
infra/aws/lambda/globgrph-trino-access/handler.py
infra/aws/lambda/globgrph-trino-access/build.sh
infra/aws/lambda/globgrph-trino-access/tests/test_handler.py
org/missions/D7/TCKT/TCKT_MTADTA/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_MTADTA/decompositions/TCKT_MTADTA_DECOMP.md</decomp_doc> (round 1), cell `MD-a-1`.
<owned_cells>MD-a-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: MD1-a1-AC1, MD1-a1-AC2. Instance at `org/missions/D7/TCKT/TCKT_MTADTA/deliverables/0.9.0_WK_TCKT_MTADTA~1/TCKT_MTADTA.TO-MD-a1.access-door.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> MD1-a1-AC1,MD1-a1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the two check lines, the names `access.tf` takes from the builder (verbatim), the `pytest` summary line of your own tests, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in this cell.
comp-iam: RUN at the drain (`comp-iam gaps` over the merged `trino` root); blind to the live plane until the apply (decomposition battery).
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round. The PRD's C-RESIDUAL (admins can edit the policies) is why the bucket policy denies only the data actions.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.2 C-ACCESS, C-RESIDUAL, DECISION 2, FWD-6, FWD-8; decomposition cell MD-a-1 and the DOOR CONTRACT.
