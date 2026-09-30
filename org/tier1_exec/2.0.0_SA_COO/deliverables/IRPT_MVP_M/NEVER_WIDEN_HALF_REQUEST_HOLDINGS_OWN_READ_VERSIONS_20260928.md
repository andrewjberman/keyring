# Never-widen half requested -- Holdings firm-principal OWN-PREFIX read-version grant (FILLED 2026-09-28, NOT SENT)

From `2.0.0_SA_COO~M` to `1.0.0_SA_CTO`. Filled by `0.9.0_WK_IRPT_BCKEND~42` (TO-IB-m19-2 amendment 2, Step 7) from
this session's own measurements. **NOT SENT and NOT APPLIED.** A firm principal's IAM policy is never-widen class;
both halves sign before `terraform apply` runs. This worker's bounds stop at plan + half; the apply (a Step-6-shaped
continuation) runs only on the CTO's signature and a ruling on the Step 8 kill verdict.

## Correction to the first read-version half

The first half (`NEVER_WIDEN_HALF_REQUEST_HOLDINGS_READ_VERSIONS_20260928.md`, CTO-signed `635481d716`, applied and
closed under ledger `irpt-holdings-principals-versionread-m-20260928`) stated under "Does not touch": "the WRITE side
(`PublishOwnHoldings`/`ListOwnHoldings`)" -- i.e. that the publication side needed no versioned read. **That was
wrong.** The Step 6 re-fire (after that grant applied and read back clean) still failed 2 of 3 firms, past the source
reads, on a versioned read of the firm's OWN publication object. The build's read-after-write / compare-and-set
step re-reads its own PRIOR revision at a pinned version, and that read lives on the `PublishOwnHoldings` statement,
not on either `READS` statement the first grant touched.

## Cause (row `IRPT_BCKEND-W42-S2`, disarm half)

TO-IB-mr-2 Step 6's re-fire (after ledger `irpt-holdings-principals-versionread-m-20260928` CLOSED) terminated
Failed at all three firms:
- inflection (command `d3275e05`) and cottonwood (command `1f3650bb`): `AccessDenied ... not authorized to perform:
  s3:GetObjectVersion` on the firm's OWN `irpt/<firm>/gold/holdings_qa/date=2026-09-25/<rev>.parquet` in its own
  publication bucket. The build re-reads its own prior revision at a pinned version there; the `PublishOwnHoldings`
  statement (`infra/aws/terraform/investor-reporting/directory/holdings_refresh.tf:105`) grants only `s3:GetObject`
  and `s3:PutObject` -- no versioned-read action.
- 49financial (command `b4d4b0d8`): `rc=137` (SIGKILL), status TimedOut, execution 21:29:07Z-21:33:35Z (~4.5 min,
  SSM's own start/end, not a 3600s hang), while all three firm builds ran concurrently on the one runner. Cause
  UNMEASURED at this half; carried separately in `R19_QA_FIRE_49F_KILL_20260928.json` (Step 8) and is NOT part of
  this IAM half -- this half disarms only the `PublishOwnHoldings` versioned-read gap.

Ruling (issuer, amendment 2): both causes are inside this cell; this half answers the IAM-shaped one.

## The act

One line in `infra/aws/terraform/investor-reporting/directory/holdings_refresh.tf`, the `irpt_holdings`
`PublishOwnHoldings` statement (line 105): `actions = ["s3:GetObject", "s3:PutObject"]` -> `actions = ["s3:GetObject",
"s3:GetObjectVersion", "s3:PutObject"]`. `resources` is unchanged (the same per-firm publication-prefix list already
granted). Nothing else in the file moves -- the `ListOwnHoldings` statement, both `READS`/`List` statement pairs (already
carrying `s3:GetObjectVersion` from the first grant), `FetchOwnPackage`, `ClassifierScan`, and every other resource in
this root are untouched (verified: `git diff` against this file shows exactly the one line below).

```
-      actions   = ["s3:GetObject", "s3:PutObject"]
+      actions   = ["s3:GetObject", "s3:GetObjectVersion", "s3:PutObject"]
```

Applied under its own ledger, `irpt-holdings-principals-ownread-m-20260928`, `HALT_ACK=1 bash .tools/safe-apply.sh
-chdir=infra/aws/terraform/investor-reporting/directory apply` (continuation, on signature only). Not opened or
applied this session.

## The plan read in full

`terraform -chdir=infra/aws/terraform/investor-reporting/directory plan -lock=false`, this session, this worktree
(after the merge to CLOUD carrying the first grant's applied state), no `init` needed (this worktree already
initialized this session; backend `s3`, state untouched).

Every "will be updated in-place" line, verbatim, and nothing else:

```
  # aws_iam_role_policy.irpt_holdings["49financial"] will be updated in-place
  ~ resource "aws_iam_role_policy" "irpt_holdings" {
        id          = "irpt-49f-holdings-role:irpt-49f-holdings-policy"
        name        = "irpt-49f-holdings-policy"
      ~ policy      = jsonencode(
          ~ {
              ~ Statement = [
                    # (3 unchanged elements hidden)
                    {
                        Action    = "s3:ListBucket"
                        Condition = { StringLike = { "s3:prefix" = "investor-reporting/directory/*" } }
                        Effect    = "Allow"
                        Resource  = "arn:aws:s3:::opal-data-bd"
                        Sid       = "ListOpalDataBd"
                    },
                  ~ {
                      ~ Action   = [
                            "s3:PutObject",
                          + "s3:GetObjectVersion",
                            "s3:GetObject",
                        ]
                        # (3 unchanged attributes hidden)
                    },
                    {
                        Action    = "s3:ListBucket"
                        Condition = { StringLike = { "s3:prefix" = [
                            "irpt/49financial/gold/holdings/*", "irpt/49financial/gold/holdings_qa/*",
                            "irpt/49financial/platinum/holdings/*", "irpt/49financial/platinum/holdings_qa/*",
                        ] } }
                        Effect    = "Allow"
                        Resource  = "arn:aws:s3:::opal-data-49financial"
                        Sid       = "ListOwnHoldings"
                    },
                    # (2 unchanged elements hidden)
                ]
                # (1 unchanged attribute hidden)
            }
        )
        # (2 unchanged attributes hidden)
    }

  # aws_iam_role_policy.irpt_holdings["cottonwood"] will be updated in-place
  ~ resource "aws_iam_role_policy" "irpt_holdings" {
        id          = "irpt-cot-holdings-role:irpt-cot-holdings-policy"
        name        = "irpt-cot-holdings-policy"
      ~ policy      = jsonencode(
          ~ {
              ~ Statement = [
                    # (3 unchanged elements hidden)
                    {
                        Action    = "s3:ListBucket"
                        Condition = { StringLike = { "s3:prefix" = "investor-reporting/directory/*" } }
                        Effect    = "Allow"
                        Resource  = "arn:aws:s3:::opal-data-cot"
                        Sid       = "ListOpalDataCot"
                    },
                  ~ {
                      ~ Action   = [
                            "s3:PutObject",
                          + "s3:GetObjectVersion",
                            "s3:GetObject",
                        ]
                        # (3 unchanged attributes hidden)
                    },
                    {
                        Action    = "s3:ListBucket"
                        Condition = { StringLike = { "s3:prefix" = [
                            "irpt/cottonwood/gold/holdings/*", "irpt/cottonwood/gold/holdings_qa/*",
                            "irpt/cottonwood/platinum/holdings/*", "irpt/cottonwood/platinum/holdings_qa/*",
                        ] } }
                        Effect    = "Allow"
                        Resource  = "arn:aws:s3:::opal-data-cottonwood"
                        Sid       = "ListOwnHoldings"
                    },
                    # (2 unchanged elements hidden)
                ]
                # (1 unchanged attribute hidden)
            }
        )
        # (2 unchanged attributes hidden)
    }

  # aws_iam_role_policy.irpt_holdings["inflection"] will be updated in-place
  ~ resource "aws_iam_role_policy" "irpt_holdings" {
        id          = "irpt-inf-holdings-role:irpt-inf-holdings-policy"
        name        = "irpt-inf-holdings-policy"
      ~ policy      = jsonencode(
          ~ {
              ~ Statement = [
                    # (3 unchanged elements hidden)
                    {
                        Action    = "s3:ListBucket"
                        Condition = { StringLike = { "s3:prefix" = [
                            "investor-reporting/directory/*", "silver/api_dims/accounts_v2/*",
                            "silver/api_dims/positions_mv/*", "silver/eclipse/*",
                        ] } }
                        Effect    = "Allow"
                        Resource  = "arn:aws:s3:::opal-data-inf"
                        Sid       = "ListOpalDataInf"
                    },
                  ~ {
                      ~ Action   = [
                            "s3:PutObject",
                          + "s3:GetObjectVersion",
                            "s3:GetObject",
                        ]
                        # (3 unchanged attributes hidden)
                    },
                    {
                        Action    = "s3:ListBucket"
                        Condition = { StringLike = { "s3:prefix" = [
                            "irpt/inflection/gold/holdings/*", "irpt/inflection/gold/holdings_qa/*",
                            "irpt/inflection/platinum/holdings/*", "irpt/inflection/platinum/holdings_qa/*",
                        ] } }
                        Effect    = "Allow"
                        Resource  = "arn:aws:s3:::opal-data-inflection"
                        Sid       = "ListOwnHoldings"
                    },
                    # (2 unchanged elements hidden)
                ]
                # (1 unchanged attribute hidden)
            }
        )
        # (2 unchanged attributes hidden)
    }

Plan: 0 to add, 3 to change, 0 to destroy.
```

Exactly three resource addresses change, no others: `aws_iam_role_policy.irpt_holdings["49financial"]`,
`aws_iam_role_policy.irpt_holdings["cottonwood"]`, `aws_iam_role_policy.irpt_holdings["inflection"]`. Every
`Statement[*].Action` entry that gains `s3:GetObjectVersion` is the single `PublishOwnHoldings` statement (one per
firm, the write-side statement over `each.value.s3_write` prefixes in the firm's own publication bucket) -- there is
exactly one such statement per firm. The `ListOwnHoldings`, `ListOpalData*`, `READS`, `FetchOwnPackage` and
`ClassifierScan` statements are untouched (shown as unchanged context above, no `~`/`+`/`-` inside them). Full raw
plan output: `.scratch/tf_plan_step7.clean.txt` in this worker's worktree (not committed -- scratch only; the block
above is the complete, load-bearing extract).

## Blast radius

- **Touches:** the one `PublishOwnHoldings` WRITE statement per firm's IAM policy document, adding
  `s3:GetObjectVersion` to the same, already-granted resource ARNs (`arn:aws:s3:::<publication_bucket>/<p>*` for each
  `p` in that firm's `s3_write` prefix list -- the firm's own `holdings`/`holdings_qa` gold+platinum prefixes,
  identical to the resources already listed for `GetObject`/`PutObject`). No new bucket, no new key prefix, no new
  principal, no new firm becomes reachable.
- **Effect:** each firm's holdings-build principal can now read a PINNED VERSION of an object under its OWN
  publication prefix it could already read the LATEST version of and already write. A principal cannot reach any
  object, bucket or prefix it could not already reach; it can now additionally pin the version of a read it was
  already authorized to make (the mirror of the first grant, now on the write-side statement instead of the
  read-side statements).
- **Does not touch:** any other firm's principal or bucket (`for_each = local.irpt_holdings_grants`, keyed per firm);
  the `READS`/`List` statement pairs (already carrying `s3:GetObjectVersion` from the first, applied grant);
  `ListOwnHoldings`, `FetchOwnPackage`, `ClassifierScan`; the directory runner's own IAM; the schedule
  `irpt-holdings-snapshot` (stays DISABLED, no resource of that type appears in the plan).

## Rollback per key

Revert the one line (`actions = ["s3:GetObject", "s3:GetObjectVersion", "s3:PutObject"]` -> `actions =
["s3:GetObject", "s3:PutObject"]`) and `safe-apply` again under a new ledger leg; the untargeted plan then reads
`0 to add, 3 to change, 0 to destroy` back to the pre-grant policy JSON (fully reversible -- no resource is created
or destroyed, only a JSON-encoded policy attribute's list value). No data is written, moved or deleted by this act
itself; nothing downstream (a re-fired QA build) has run yet under the new grant.

## The ask

**NOT SENT.** This half disarms the IAM-shaped half of row `IRPT_BCKEND-W42-S2` (the 49F `rc=137` kill is a separate,
UNMEASURED cause, carried in `R19_QA_FIRE_49F_KILL_20260928.json`, Step 8, and is NOT answered by this half).
`2.0.0_SA_COO~M` sends this to `1.0.0_SA_CTO` when ready, alongside a ruling on the Step 8 kill verdict;
`0.9.0_WK_IRPT_BCKEND~42` does not apply this plan and stops here per amendment 2's Step 7 bound.

## COO half -- SIGNED by 2.0.0_SA_COO~M (issuer, 2026-09-28 ~22:0xZ)

Read by the issuer before signing: the diff at `2dba2ba162` is the one `PublishOwnHoldings` line (`git show`); the
statement's resources are each firm's own `s3_write` prefixes in its own publication bucket, unchanged; the plan
reads 0 add / 3 change / 0 destroy on the three `aws_iam_role_policy.irpt_holdings[...]`; the cause is the issuer's
own read of d3275e05 (INF) and 1f3650bb (COT) at 21:3xZ. The correction above is the issuer's: the first half's
"publication needs no versioned read" was wrong.
Blast radius signed: own-prefix reads at a pinned version; no new bucket, prefix, principal or firm; the schedule stays
DISABLED; nothing served moves on apply. Rollback per key: revert the line, safe-apply (0 / 3 / 0 back).
Not covered by this half: 49F's build is OOM-killed on the t3.medium runner on its own (R19_QA_FIRE_49F_KILL_20260928.json,
verdict OOM-SINGLE). The issuer rules that into the ~M workstream as a build-memory cell; this grant does not depend
on it, and INF and COT can exercise it at the next QA fire.
## CTO half -- owed
