# DEPLOY LEDGER -- ETFS_SATELLITES.TO-6-AE: the satellites registry producer SCHEDULE

**STATUS: CLOSED -- COMPLETE** at 2026-08-28T01:40Z. Applied in full in-session, verified on the
live plane, nothing half-landed. Opened at apply start per CLAUDE.md NEVER#2.

⚠ **CLOSED refers to the DEPLOY, not to the TO.** `T6AE-AC3` (a fire on the schedule's own trigger)
is outstanding until 07:00Z by design -- an un-fired scheduled criterion is not a failed one, and it
is not something an apply can discharge. Do not read this closure as TO-6-AE complete.

| field | value |
|---|---|
| opened | 2026-08-28T01:35Z |
| seat | `0.7.0_AE_CloudOps~S` |
| issuer | `2.0.0_SA_COO~Z` (TO `ETFS_SATELLITES.TO-6-AE`) |
| certifier | `3.0.0_SA_CVO~Z` |
| project | ETFS_SATELLITES (D4, SITEZ-placed) |
| stack | `infra/aws/terraform/cot-pipeline/` |
| source commit | `3f5f8bace5` |
| tag | `cot-pipeline-v0.7.7` (annotated, peels to `3f5f8bace5`) |
| applied | 2026-08-28T01:37Z -- **9 added, 0 changed, 0 destroyed** |
| closed | 2026-08-28T01:40Z |

## WHAT IS BEING APPLIED

New resources only -- no modification or destruction of any existing resource:

| resource | kind |
|---|---|
| `aws_iam_role.cot_satellites_registry_producer` | IAM role |
| `aws_iam_role_policy.cot_satellites_registry_producer_s3` | 2-bucket least-privilege |
| `aws_iam_role_policy.cot_satellites_registry_producer_cross_firm_deny` | NEVER#2 deny |
| `aws_iam_role_policy_attachment.cot_satellites_registry_producer_basic` | basic exec |
| `module.cot_satellites_registry_producer` | Lambda (192 MB / 60 s) |
| `aws_cloudwatch_event_rule.cot_satellites_registry_producer_daily` | **THE SCHEDULE** `cron(0 7 * * ? *)` UTC |
| `aws_cloudwatch_event_target.cot_satellites_registry_producer_daily` | rule -> lambda |
| `aws_lambda_permission.events_cot_satellites_registry_producer` | invoke permission |

Artifact: `s3://opal-313476888478-lambda-artifacts/cot-pipeline/cot-satellites-registry-producer.zip`
(65426 B, sha256 `bfea16181f56bec4bef85ccfe1070b5a9a019c7394b76b72b33c7770cdc9bbad`, built from pin
`3f5f8bace5`, import-verified from the built zip before upload).

## PRE-FLIGHT, MEASURED

- **Baseline plan on this stack: `No changes. Your infrastructure matches the configuration.`**
  Taken BEFORE this file's `.tf` existed, so any diff in the apply plan is attributable to this
  change and to nothing else. (This also falsified a concern I had carried in: `ec2.tf`'s
  "staged but NOT applied" header is STALE -- `aws_instance.cot_exporter` is in state and
  refreshes clean. 68 resources, all applied.)
- Gate on TO-5-DS AC2: **DISCHARGED** -- `s3://opal-data-cot/platinum/satellites/registry.json`,
  2182 B, `LastModified 2026-08-28T01:09:51Z` (UTC, `s3api`), VersionId
  `D1iVAJ4LJOqx1BDPMLmcEXLOUJvcP7wb`, 9 books, `as_of 2026-08-27`.
- Commit gate: clean on both `.py` (py_compile + ds-precommit + ruff), pure ASCII.

## ROLLBACK

All **NINE** applied resources are NEW and independent of anything live. Rollback is
`terraform destroy -target=` each, or revert `3f5f8bace5` and re-apply -- neither touches the
producer, the existing artifact, or any other stack resource. **The published registry artifact is
NOT owned by this deploy** and is unaffected by any rollback here.

⚠ NINE, not the eight listed in the table above: `module.cot_satellites_registry_producer` expands
to TWO resources -- `aws_lambda_function.this` AND `aws_cloudwatch_log_group.lambda`
(`/aws/lambda/cot-satellites-registry-producer`, 14-day retention), which the module creates and
the table's module row hides. Recorded because a rollback driven off the resource TABLE rather off
the apply COUNT would leave the log group orphaned -- a small residue, but the table is the thing a
future reader would work from and it under-counts by one.

## AC3 BASELINE -- CAPTURED BEFORE THE FIRST SCHEDULED FIRE, AND IT IS PERISHABLE

⛔ **CORRECTED 2026-08-28T01:46Z -- THE BASELINE MOVED, AND THE INSTRUMENT I FIRST CHOSE WAS
UNSOUND. BOTH HALVES MATTER.**

    2026-08-28T01:09:51Z  2182 B  D1iVAJ4LJOqx1BDPMLmcEXLOUJvcP7wb  the ad-hoc QA write
    2026-08-28T01:38:46Z  2196 B  xLcuAW7VMbGyF.0kpt2LQ9Wb24WVnQaS  ANOTHER SEAT'S WRITE <- CURRENT BASELINE
    versions at the key: 2 (denominator, s3api list-object-versions)

**(a) THE BASELINE.** Compare a scheduled fire against `xLcuAW7VMbGyF...`, not against the QA
write. A certifier working from the original figure would compare against a version that was
already superseded before this ledger was committed.

**(b) THE INSTRUMENT -- the part worth keeping.** I first armed a watch that fired on ANY new
VersionId at this key. **It fired within 90 seconds, on that 01:38:46Z write, which is not mine:**
this function's own log group carries exactly ONE invocation (01:39:10Z, the dry-run) and it wrote
nothing, raising on the roster read before reaching `publish()`.

>> **VersionId-delta answers "did the key change", NOT "did MY SCHEDULE fire" -- and any seat's
>> ad-hoc run satisfies it.** The TO requires evidence distinguishing a scheduled fire from a
>> manual one, and that instrument structurally cannot. **It was caught only because the timestamp
>> was impossible: had the cron been 01:40Z rather than 07:00Z, another seat's write would have
>> been accepted as this TO's acceptance evidence.**

**THE SOUND ORACLE, now armed instead:** `/aws/lambda/cot-satellites-registry-producer`'s own log
group, watched for its `OK: wrote s3://...` line from a start-time onward. That line is emitted by
the function under test only on a completed write, cannot be produced by another seat running the
same producer elsewhere, and the only other route into that log group is a manual invoke of this
function -- which is under this seat's control and will not be used.

This is the same lesson as the artifact's missing `provenance` field, one turn later and sharper:
**an oracle produced by the system under test, or by anything that shares its output surface, is
not a discriminator.**

WARNING: durability has a SECOND half in a DIFFERENT API call, and it bites here.
`get-bucket-versioning` says `Status: Enabled`, but `get-bucket-lifecycle-configuration` carries
`expire-noncurrent-versions-14d` over `Prefix: ""` -- the whole bucket. So the moment the scheduled
fire writes, the QA version becomes noncurrent and **dies 14 days later**. The baseline above is
recorded HERE, in a durable artifact, precisely so the AC3 comparison survives the expiry of the
thing it compares against.

Note also: the QA artifact does **not** carry a `provenance: ad-hoc-QA` field -- measured, its
top-level keys are `schema_version, as_of, source, claim, books`. So AC3's discriminator rests on
the version/LastModified delta plus the invocation record, NOT on a self-declared provenance field.
That is the stronger instrument anyway: a provenance field is written by the system under test,
whereas the version history and the EventBridge invocation record are produced by different systems.

---

## COMPLETION EVIDENCE -- measured on the live plane, not read from the plan

    APPLY            9 added, 0 changed, 0 destroyed
    RE-PLAN          "No changes. Your infrastructure matches the configuration."
    RULE             cot-satellites-registry-producer-daily  cron(0 7 * * ? *)  ENABLED
    TARGET           -> arn:aws:lambda:...:function:cot-satellites-registry-producer
                        (id CotSatellitesRegistryProducerDaily)
    LAMBDA           python3.11 | 192 MB | 60 s | State Active
                     role cot-satellites-registry-producer-role
    CODE LAYER       deployed CodeSha256  v+oWGB9WvsS++FzP4QcLWpoBnHOUt2tyszx3cM3Ju60=
                     built zip sha256(b64) IDENTICAL -- compared by CONTENT against the
                     build input, never by filename (Rule 22a CODE layer)

### AC2 two-plane census -- both APIs, both denominators

    PLANE 1  EventBridge RULES      139 rule(s), 1 page, NextToken exhausted
                                    matching 'satellites': 1  <- THIS TRIGGER
    PLANE 2  EventBridge SCHEDULER   18 schedule(s), 1 page, NextToken exhausted
                                    matching 'satellites': 0  <- correctly empty

    The Rules denominator moved 138 -> 139 across the apply: exactly one added, which is
    itself a control on the apply's scope.
    POSITIVE CONTROLS (so a 0 is a real 0, not an unreachable probe): the rules probe
    returns 6 for 'cot-'; the SCHEDULER probe returns 1 for 'cot-'. Both probes reach
    their planes and the Scheduler zero is a finding rather than a blind spot.

### IAM, verified on the live primitive with isolated controls

One `--resource-arns` per call; each control a SEPARATE invocation (the multi-ARN
false-deny mode silently disarms the control otherwise):

    GetObject  rebalancer_models/2026-08-27/page_000.json      allowed
    GetObject  rebalancer_model_detail/2026-08-27/abc.json     allowed
    PutObject  opal-data-cot/platinum/satellites/registry.json allowed
    NEGATIVE   GetObject outside the granted prefix            implicitDeny
    NEGATIVE   PutObject on a different platinum key           implicitDeny
    NEGATIVE   ListBucket on opal-data-assets                  implicitDeny

## OBSERVATION (class OBSERVATION, standing INERT) -- A COST OF MY OWN DESIGN THAT NOBODY PRICED

The deployed Lambda was exercised in DRY-RUN (writes nothing, does not touch the served
key, does not muddy the AC3 discriminator). It confirmed the two things only an in-situ
run can: the repo-mirroring zip layout imports correctly under `/var/task`, and the
producer resolved `as_of=2026-08-28 (resolved today-UTC)` -- option (A) working in the
DEPLOYED bytes. Max memory used 96 MB against the 192 MB sizing.

It also surfaced this:

    [ERROR] BLOCKED: no roster partition at .../rebalancer_models/2026-08-28/page_000.json
            (S3 said AccessDenied)

The partition is genuinely absent (upstream lands 06:00:43Z; the run was 01:39Z), and the
IAM simulation above shows the read grant is CORRECT. But S3 returns **403 AccessDenied
rather than 404 NoSuchKey for a missing object when the caller lacks `s3:ListBucket`** --
it will not confirm non-existence to a principal that cannot list.

>> SO "UPSTREAM IS LATE" AND "MY READ GRANT IS BROKEN" PRODUCE A BYTE-IDENTICAL ERROR AT
>> THIS PRODUCER'S SURFACE. Today it is the benign one. If anyone later tightens this
>> role, the failure reads exactly the same and the natural conclusion is "upstream is
>> late again."

This is the SAME SHAPE as the hazard `TO-5-DS` AC3 records for the serving layer -- where
an absent artifact and a forbidden read are the same status, which is why the edge
synthesis was removed @`24a8435642`. It has reappeared one layer up, on the producer's
READ side, and **it is a consequence of my own no-`ListBucket` decision**, which
`2.0.0_SA_COO~Z` ratified on the stated ground of "consistent with rejecting (C)".

REMEDY IF WANTED (not taken unilaterally, because the absence was explicitly ratified):
a prefix-conditioned `s3:ListBucket` on `opal-data-assets` scoped to the two rebalancer
prefixes. That separates the two states -- late upstream reads `NoSuchKey`, broken grant
reads `AccessDenied` -- and it does NOT implement option (C), which was a
newest-partition RESOLUTION strategy rather than a grant. INERT: it does not block AC3,
because the grant is measured correct.
