# Never-widen half requested -- Holdings firm-principal read-version grant (FILLED 2026-09-28, NOT SENT)

From `2.0.0_SA_COO~M` to `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. Filled by `0.9.0_WK_IRPT_BCKEND~42` (TO-IB-m19-2
amendment 1, Step 5) from this session's own measurements. **NOT SENT and NOT APPLIED.** A firm principal's IAM
policy is never-widen class; both halves sign before `terraform apply` runs. This worker's bounds stop at plan +
half; Step 6 (apply, re-fire) is continued only on the CTO's signature.

## Cause (surprise row `IRPT_BCKEND-W42-S1`, disarm half)

TO-IB-mr-2 Step 2's QA fire (2026-09-28 19:30:55Z) terminated Failed at all three firms. Two of the three failures
are one shape: `botocore.errorfactory.AccessDenied ... not authorized to perform: s3:GetObjectVersion` --
49financial on `arn:aws:s3:::opal-data-assets/gateway/49financial/bronze/taxsma_workbook_projection/date=2026-09-23/
taxsma_workbook_projected_snapshot.json`, cottonwood on `arn:aws:s3:::opal-data-assets/blackdiamond/cottonwood/
silver/fact_model_assignment/date=2026-09-28/data.parquet`. Every source read in the holdings build goes through
`data/assets/scripts/gold/investor_reporting/source_inputs.py:51`, which re-reads the EXACT version it first read
(`VersionedInputs`); IAM authorizes a versioned GET as the distinct action `s3:GetObjectVersion`, which the firm
read statement (`infra/aws/terraform/investor-reporting/directory/holdings_refresh.tf:81`, `ReadOpalDataAssets`-class
statements) does not grant -- it grants only `s3:GetObject`. (The third failure, INF's `ModuleNotFoundError:
No module named 'lib.silver_ids'`, is a separate cause: the bundle closure gap, disarmed in this order's Step 4,
commit `a3200028d9`, not part of this half.)

## The act

One line in `infra/aws/terraform/investor-reporting/directory/holdings_refresh.tf`, the `irpt_holdings` READS
statement (line 81): `actions = ["s3:GetObject"]` -> `actions = ["s3:GetObject", "s3:GetObjectVersion"]`.
`resources` is unchanged (the same per-firm prefix list already granted). Nothing else in the file moves -- the
`ListBucket` statement, the `PublishOwnHoldings`/`ListOwnHoldings` WRITE statements, and every other resource in
this root are untouched by this diff (verified: `git diff` against this file shows exactly the one line below).

```
-      actions   = ["s3:GetObject"]
+      actions   = ["s3:GetObject", "s3:GetObjectVersion"]
```

Applied under its own ledger, `irpt-holdings-principals-versionread-m-20260928`, `HALT_ACK=1 bash .tools/safe-apply.sh
-chdir=infra/aws/terraform/investor-reporting/directory apply` (Step 6, on signature only).

## The plan read in full

`terraform -chdir=infra/aws/terraform/investor-reporting/directory plan -lock=false`, this session, this worktree
(`2dccc70d49` + the Step 4/Step 5 diffs), after `terraform init -input=false` (this worktree had never been
initialized; backend `s3`, no `-migrate-state`/`-reconfigure` used, state untouched).

Every "will be updated in-place" line, verbatim, and nothing else:

```
  # aws_iam_role_policy.irpt_holdings["49financial"] will be updated in-place
  ~ resource "aws_iam_role_policy" "irpt_holdings" {
        id          = "irpt-49f-holdings-role:irpt-49f-holdings-policy"
        name        = "irpt-49f-holdings-policy"
      ~ policy      = jsonencode(
          ~ {
              ~ Statement = [
                  ~ {
                      ~ Action   = "s3:GetObject" -> [
                          + "s3:GetObjectVersion",
                          + "s3:GetObject",
                        ]
                        # (3 unchanged attributes hidden)
                    },
                  ~ {
                      ~ Action   = "s3:GetObject" -> [
                          + "s3:GetObjectVersion",
                          + "s3:GetObject",
                        ]
                        # (3 unchanged attributes hidden)
                    },
                    {
                        Action    = "s3:ListBucket"
                        Condition = {
                            StringLike = {
                                "s3:prefix" = [
                                    "gateway/49financial/bronze/taxsma_workbook_projection/*",
                                    "schwab/08335338/silver/dim_asset/*",
                                    "schwab/08335338/silver/dim_balance/*",
                                    "schwab/08335338/silver/dim_position/*",
                                    "smartx/platform/silver/fact_allocation_account_map/*",
                                    "smartx/platform/silver/fact_allocation_positions/*",
                                    "smartx/platform/silver/fact_allocation_valuation/*",
                                    "smartx/platform/silver/fact_model_allocation_roster/*",
                                ]
                            }
                        }
                        Effect    = "Allow"
                        Resource  = "arn:aws:s3:::opal-data-assets"
                        Sid       = "ListOpalDataAssets"
                    },
                    # (5 unchanged elements hidden)
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
                  ~ {
                      ~ Action   = "s3:GetObject" -> [
                          + "s3:GetObjectVersion",
                          + "s3:GetObject",
                        ]
                        # (3 unchanged attributes hidden)
                    },
                  ~ {
                      ~ Action   = "s3:GetObject" -> [
                          + "s3:GetObjectVersion",
                          + "s3:GetObject",
                        ]
                        # (3 unchanged attributes hidden)
                    },
                    {
                        Action    = "s3:ListBucket"
                        Condition = {
                            StringLike = {
                                "s3:prefix" = [
                                    "blackdiamond/cottonwood/silver/fact_allocations/*",
                                    "blackdiamond/cottonwood/silver/fact_holdings/*",
                                    "blackdiamond/cottonwood/silver/fact_model_assignment/*",
                                    "blackdiamond/cottonwood/silver/fact_model_blend/*",
                                    "blackdiamond/cottonwood/silver/fact_model_definition/*",
                                    "blackdiamond/cottonwood/silver/fact_model_roster/*",
                                ]
                            }
                        }
                        Effect    = "Allow"
                        Resource  = "arn:aws:s3:::opal-data-assets"
                        Sid       = "ListOpalDataAssets"
                    },
                    # (5 unchanged elements hidden)
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
                  ~ {
                      ~ Action   = "s3:GetObject" -> [
                          + "s3:GetObjectVersion",
                          + "s3:GetObject",
                        ]
                        # (3 unchanged attributes hidden)
                    },
                  ~ {
                      ~ Action   = "s3:GetObject" -> [
                          + "s3:GetObjectVersion",
                          + "s3:GetObject",
                        ]
                        # (3 unchanged attributes hidden)
                    },
                    {
                        Action    = "s3:ListBucket"
                        Condition = {
                            StringLike = {
                                "s3:prefix" = "eclipse/inflection/bronze/eclipse_membership_map/*"
                            }
                        }
                        Effect    = "Allow"
                        Resource  = "arn:aws:s3:::opal-data-assets"
                        Sid       = "ListOpalDataAssets"
                    },
                    # (5 unchanged elements hidden)
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
`Statement[*].Action` entry that is `"s3:GetObject" -> ["s3:GetObjectVersion", "s3:GetObject"]` is one of the two
READ statements this firm's `for_each` over `s3_read` prefixes emits (`ReadGatewayXxx`/`ReadSchwabXxx` etc. per
statement key) -- there are exactly two such statements per firm because each firm's `local.irpt_holdings_grants
.s3_read` map has two bucket keys (`opal-data-assets` cross-bucket + the firm's own `opal-data-<firm>` bucket). The
`ListBucket` statement and every WRITE statement are untouched (shown as unchanged context above, no `~`/`+`/`-`
inside them). Full raw plan output (with the refresh-read preamble): `.scratch/tf_plan_step5.clean.txt` in this
worker's worktree (not committed -- scratch only; the block above is the complete, load-bearing extract).

## Blast radius

- **Touches:** the two READ statements per firm's IAM policy document (`ReadOpalDataAssets` cross-bucket and the
  firm's own-bucket read statement), adding `s3:GetObjectVersion` to the same, already-granted resource ARNs
  (`arn:aws:s3:::<bucket>/<prefix>*`) for the same three prefix lists already in the plan output above. No new
  bucket, no new key prefix, no new principal, no new firm becomes reachable. `ListBucket`, `PublishOwnHoldings`,
  `ListOwnHoldings`, the scheduler roles, the Lambda code, the schedule's ENABLED/DISABLED state, and every other
  file/resource in this root are unchanged (verified: `git diff --stat` shows one file, one line; the plan's
  denominator is exactly 3 resources of type `aws_iam_role_policy`).
- **Effect:** each firm's holdings-build principal can now read a PINNED VERSION of an object under a prefix it
  could already read the LATEST version of. A principal cannot reach any object, bucket or prefix it could not
  already reach; it can now additionally pin the version of a read it was already authorized to make.
- **Does not touch:** any other firm's principal or bucket (a firm's grant map is keyed by that firm only, via
  `for_each = local.irpt_holdings_grants`); the WRITE side (`PublishOwnHoldings`/`ListOwnHoldings`); the directory
  runner's own IAM (`irpt_directory`, `irpt_49f_directory_read` -- different `aws_iam_policy_document` resources,
  not in this plan's action list); the schedule `irpt-holdings-snapshot` (stays DISABLED, no resource of that type
  appears in the plan).

## Rollback per key

Revert the one line (`actions = ["s3:GetObject", "s3:GetObjectVersion"]` -> `actions = ["s3:GetObject"]`) and
`safe-apply` again under a new ledger leg; the untargeted plan then reads `0 to add, 3 to change, 0 to destroy` back
to the pre-grant policy JSON (the change is fully reversible in Terraform -- no resource is created or destroyed,
only a JSON-encoded policy attribute's list value). No data is written, moved or deleted by this act itself; nothing
downstream (a re-fired QA build) has run yet under the new grant.

## The ask

**NOT SENT.** This half plus the R4 ENABLE half's own preconditions must both be reviewed together: this grant
disarms half of `IRPT_BCKEND-W42-S1` (the IAM-shaped half; the closure-shaped half is already disarmed, commit
`a3200028d9`, re-mint ledger `irpt-holdings-packages-m-20260928b` CLOSED, commit `6b064e92e6`). `2.0.0_SA_COO~M`
sends both to `1.0.0_SA_CTO` and `4.0.0_SA_CRO` when ready; `0.9.0_WK_IRPT_BCKEND~42` does not apply this plan and
stops here per the amendment's Step 5 bound.

## COO half -- SIGNED by 2.0.0_SA_COO~M (issuer, 2026-09-28 ~21:1xZ)

Read by the issuer before signing, not taken from the worker's report:
- the diff at `1c8059ae99` against `holdings_refresh.tf` is exactly the one READS line above (`git show`), and the
  statement is a `for_each` over each firm's own `s3_read` map, so the added action lands only on prefixes that firm
  already reads;
- the plan's summary line and its three addresses, as quoted above;
- the cause: command outputs 10a22d91 (49F) and 415f085f (COT), `AccessDenied ... s3:GetObjectVersion`, read by the
  issuer at 19:3xZ; `source_inputs.py:51` re-reads each source at its exact version.

Blast radius signed: the three `aws_iam_role_policy.irpt_holdings[...]` policy documents, two READ statements each,
gain `s3:GetObjectVersion` on unchanged resources. No new bucket, prefix, principal or firm. The schedule stays
DISABLED and nothing served moves on apply. Rollback per key: revert the line and safe-apply (0 / 3 / 0 back).
Routing correction to "The ask": this half goes to 1.0.0_SA_CTO only (a firm principal is never-widen class and the
09-25 principals packet was signed by the COO and the CTO, SIGNOFF_HOLDINGS_PRINCIPALS_DISPATCH_20260925.md
@6c5c27a666). The R4 ENABLE half goes to the CTO and 4.0.0_SA_CRO separately, after a QA fire succeeds.
CTO half: owed.
