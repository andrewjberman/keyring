# DEPLOY LEDGER -- HARVEST ESTATE, STAGE 1: three-backend consolidation

**Status: CLOSED -- COMPLETE AND VERIFIED** (opened 2026-09-11T18:56Z, closed 2026-09-11T19:0xZ, by `4.0.0_SA_CRO~Z`)
**Module:** `infra/aws/terraform/harvest/` | **State:** `harvest/tfstate`
**Authority:** Andrew-direct 2026-09-11 ~17:3xZ and ~18:3xZ (@`bb1800ec4d`, @`135aa5b0d0`), plus his
explicit "go ahead" at ~18:5xZ for the import-and-plan step. Module landed @`632a9a5263`.

## WHAT THIS APPLY DOES

Completes the consolidation of THREE terraform backends into ONE by reconciling the newly-imported
state with the declared configuration. **It is a TAG-AND-STATE apply. It creates nothing, destroys
nothing and replaces nothing.**

## THE PLAN, READ BEFORE APPLYING

```
Plan: 0 to add, 7 to change, 0 to destroy.
  aws_dynamodb_table.harvest_articles                     in-place
  aws_dynamodb_table.harvest_security_metrics             in-place
  aws_iam_role.harvest_enqueue                            in-place
  aws_s3_bucket.harvest                                   in-place
  aws_sqs_queue.harvest_requests                          in-place
  module.harvest_enqueue.aws_cloudwatch_log_group.lambda  in-place
  module.harvest_enqueue.aws_lambda_function.this         in-place
```

**0 DESTROY AND 0 REPLACE IS THE ACCEPTANCE TEST AND IT PASSED.** That is the whole point of Stage 1:
every resource was declared at its CURRENT name and IMPORTED, so the consolidation is provably free.

## THE ONE CHANGE THAT NEEDED VERIFYING RATHER THAN READING

`module.harvest_enqueue.aws_lambda_function.this` shows `+ s3_bucket`, `+ s3_key`,
`+ s3_object_version`, `+ source_code_hash` and `last_modified -> (known after apply)`. Those fields
are NOT populated by `terraform import`, so the plan is reconciling state -- **but a plan that sets a
Lambda's code fields could just as easily be about to deploy DIFFERENT BYTES, and the plan text alone
cannot tell you which.** Measured rather than assumed:

```
deployed CodeSha256            THhzBXqTs1XoNok2IyKS5z+y3RE41aqUMIw4Bno53NM=   (get-function-configuration)
plan's source_code_hash        THhzBXqTs1XoNok2IyKS5z+y3RE41aqUMIw4Bno53NM=
```

**BYTE-IDENTICAL, so this apply deploys no new code.** `s3_object_version dIzmo_pR4wYCv3WyGtjA504TSt5NvVS9`
is the version already running.

## THE TAG CHANGES, AND WHY THEY ADD RATHER THAN STRIP

The first plan of this module proposed `- "Environment" -> null`, `- "Macro" -> null`,
`- "ManagedBy" -> null` on both DynamoDB tables: the pre-consolidation `amgt-resapp` provider carried
`default_tags` and the `research` provider carried none, so a provider with none would have QUIETLY
DROPPED three tags. A `default_tags` block was added to the harvest provider instead --
`Estate=HARVEST, Project=AMGT_RESAPP, Macro=AMGT, Directive=D5, ManagedBy=Terraform,
Environment=Production` -- which preserves them and extends one uniform set across the estate.
`Estate=HARVEST` is the operationally useful one: the feeder resources do NOT share a name prefix
(`opal-data-*`, `opal-amgt-*`, `opal-research-*`), so a tag is the only way to find them as a set.
One disclosed edit of this seat's own: the SQS `Purpose` tag drops the word "Bloomberg"
("on-demand Bloomberg pull request queue" -> "on-demand pull request queue") because the queue now
serves all four publishers, not one.

## BLAST RADIUS

Six live resources plus one log group, all tag metadata only. **No data is touched. No table is
dropped. No bucket is deleted. No portal route changes** -- `POST /api/private/research/pull` keeps
its path by Andrew's word and the portal hold stands.

## NOT IN THIS APPLY -- STAGE 2, SEPARATE AND CONFIRMED SEPARATELY

The approved harvest RENAMES (`opal-data-harvest`, `opal-harvest-articles`,
`opal-harvest-security-metrics`, `opal-harvest-requests`, `opal-harvester-enqueue`). They are
DESTRUCTIVE -- a DynamoDB rename is DESTROY/RECREATE, an S3 rename is create-copy-delete costing 7
non-latest versions and 1 delete marker -- and CLAUDE.md reserves dropping tables and S3 deletes for
explicit human confirmation at the act. `opal-amgt-security-metrics` is additionally sequenced behind
the LIVE writers `AMGT-rd-5` and `AMGT-rd-6`.

## ROLLBACK

Tag-only and state-only: re-applying the prior tag set restores it. The imported state is additive --
the three source states (`research/tfstate`, `amgt-resapp/tfstate`,
`amgt-resapp/rd-2-security-metrics/tfstate`) are **UNTOUCHED by this apply** and still describe the
same live resources, so the pre-consolidation position is recoverable by pointing back at them. They
are cleaned up only after this apply is verified.

## CLOSE-OUT -- 2026-09-11 ~19:0xZ, COMPLETE

```
Apply complete! Resources: 0 added, 7 changed, 0 destroyed.
```

**VERIFIED AGAINST THE LIVE PLANE, NOT FROM THE APPLY'S OWN OUTPUT** (CLAUDE.md: never trust a
producer's self-report or rc=0):

| check | instrument | result |
|---|---|---|
| no drift remains | `terraform plan -detailed-exitcode` | **rc=0** -- "No changes. Your infrastructure matches the configuration." |
| tags actually landed | `aws dynamodb list-tags-of-resource` on the live table | `ManagedBy=Terraform`, **`Estate=HARVEST`** |
| nothing destroyed | the apply's own counts, corroborated by the clean re-plan | 0 added, 0 destroyed |

`-detailed-exitcode` is the discriminating instrument here: it returns **2** when changes are still
pending and **0** only when real infrastructure matches configuration, so a 0 cannot be produced by a
half-finished apply. A plain `plan` printing reassuring prose would not have separated those cases.

**THE ESTATE IS NOW ONE MODULE.** `infra/aws/terraform/harvest/` holds all 15 resources in
`harvest/tfstate`, and the module that could not `plan` or `apply` this morning is repaired --
`terraform validate` returns "Success! The configuration is valid."

**STILL OPEN, DELIBERATELY, AND NOT PART OF THIS ENTRY:**
- The three SOURCE states are untouched and still describe these resources. Cleaning them up
  (`terraform state rm`) is a follow-on act, kept separate so this entry's rollback stays simple.
- **Stage 2, the renames.** Andrew RULED at ~18:5xZ that `opal-data-research` IS renamed
  ("better to have all of this stuff grouped by name right from the start"). ⛔ **His stated reason
  -- "there is no data in there anyway" -- is FALSE: 53 objects / 60 versions, measured
  independently by `1.0.0_SA_CTO~Z` at 18:55:29Z and consistent with this seat's own earlier read of
  7 non-latest versions + 1 delete marker.** The authorised act is therefore a **53-OBJECT DATA
  MIGRATION**, not an empty-bucket rename. Surfaced to him for a re-rule on the corrected facts;
  the ruling is NOT being held hostage to the correction.
- The approved execution order ("consolidation + renames FIRST while both stores are empty") was
  written believing this bucket empty too. **That order needs re-reading against 53 objects before
  the migration runs** -- the DynamoDB tables are genuinely empty (0 items) and unaffected.
