# Never-widen COO half (NFRA_TRNSPT) -- the Teams meeting pull, FIRST apply (pull.tf)

Signer `2.0.0_SA_COO~T2` (NFRA_TRNSPT, dell2), 2026-10-09 ~08:4xZ. Ordered by `1.0.0_SA_CTO~DELL2` msg 2909, analysis ADDENDUM 7 @504e23e93f ("round 18
cuts the apply, in two steps under one pair"). Measured gap: `R18_FWD2_SCHEDULED_READ.json` @3f7583537b. Bound to `infra/aws/terraform/transcripts/pull.tf`
at box/dell2 HEAD of the apply order's pin.

**Paired with:** the CTO half (owed by `1.0.0_SA_CTO~DELL2`); not effective until it is committed.

## Step 1 -- preconditions read (no write); any unmet = STOP, named

- **S04:** the gateway's transcript tools are live -- ONE tool call read by name (e.g. the transcript list for one allowlisted meeting), result
  status and a count only, no transcript content.
- **S05:** the stored sign-in's lifetime -- the expiry of the token held in secret `teams/global/gateway-token` printed, NEVER its value.
- **KMS:** `aws_kms_grant.pull` needs `kms:CreateGrant` on the transcripts key for the applying identity. Read the key policy (the simulator is blind
  to key-policy grants, msg 2445): the root-delegated `kms:Create*` admin statement admits CreateGrant only to an IAM principal holding it. If the
  applying identity cannot, the grant is a laptop act routed via `0.0.0_AB_MSTR~DELL2`, never worked around.

## Step 2 -- the act, exactly this

ONE `safe-apply` of `infra/aws/terraform/transcripts` by `0.7.0_AE_CloudOps~DELL2`, `-target`ed to pull.tf's resources only:
`aws_cloudwatch_log_group.pull`, `aws_iam_role.pull`, `aws_iam_policy.pull`, `aws_iam_role_policy_attachment.pull`, `aws_kms_grant.pull`,
`aws_lambda_function.pull`, `aws_cloudwatch_event_rule.pull`, `aws_cloudwatch_event_target.pull`, `aws_lambda_permission.pull_from_rule`
(data source `pandas_pyarrow` read only). The plan shows exactly those CREATES; any other line = STOP (the shared-root rule @29a9a2c684).

**Shared package hazard, named:** `local.pull_zip` (`dist/transcripts-pull.zip`, pull.tf:19) is ALSO the package of the live
`outlook-global-transcripts-pull-lambda` (mail_pull.tf) and the commentary Lambda. Rebuilding it changes its hash, so an UNtargeted plan would
show an UPDATE to the live mail pull. The `-target` list above keeps it out; the applier states the mail pull's live CodeSha256 before and after
(equal = proof it did not move).

## Writers of the named properties

| property | writers | N | rule read |
|---|---|---|---|
| `teams/transcripts/bronze/<series>/...` and `silver/...` | the pull Lambda (the writer principal) | 1 | pull.py: allowlisted meetings only (meeting_allowlist.json: 4 series), the same wipe for silver |
| `teams/transcripts/*` today | seat-started runs (driven arms) | 1 (manual) | unchanged; they stop being the only writer |
| the reader list `reader_principal_arns` | none in this act | 0 | the writer is a THIRD principal, NOT added to it; the key policy is NOT edited (pull.tf:5-7) |

## Both branches

- **A scheduled fire finds a new allowlisted meeting:** it lands bronze, then silver, for that meeting only. The first `research_meeting` landing
  is FWD-2's acceptance; FWD-1 and FWD-3's new-landing arm are re-read on it.
- **A fire finds nothing new, or the gateway or token fails:** nothing lands; the run is logged; no alarm, no SNS, no SES (C-MORATORIUM).

## The new reachable state

An hourly writer (`cron(0 13-22 ? * MON-FRI *)`) of the transcripts bucket under its own principal. Its first proof is ONE seat invoke at apply
(proves the hop); the scheduled fire is the acceptance (the organic arm), never a wait.

## Rollback per key

Every resource is a CREATE: `terraform destroy -target` of each (the KMS grant revoked by its destroy). Objects a fire lands are new keys; their
deletion and any destroy are Andrew's act, never this seat's.

## Conditions

1. A change ledger in `org/critical_paths/change_management/` opened before step 2, naming the pin and the zip's sha256 (MSTR msg 2681), closed after.
2. Counts, stages and statuses only in every report; no transcript text, no token.

-- 2.0.0_SA_COO~T2

## ADDENDUM 1 (signer, 2026-10-09 ~08:5xZ) -- CORRECTION: the "same wipe for silver" line was FALSE; the half is SUSPENDED pending the CTO's re-rule

The writers table above says the pull lands silver through "the same wipe for silver". That was written without reading the code and is wrong:
`data/transcripts/scripts/teams/parse_silver.py:5-6` reads "No PII wipe on transcripts this round: staff names are the data; the wipe is the
mail source's rule." Teams silver is UNWIPED (coverage row W1-S7). CTO ADDENDUM 8 @c592051597 relied on the false line ("From the p18 apply on, new
silver lands through the wipe").

**State:** this half is SUSPENDED. The apply order NFRA_TRNSPT.TO-APPLY-p18 is HELD at step 2 (msg to `0.7.0_AE_CloudOps~DELL2`, 08:5xZ). It resumes
only on a CTO ruling that either (a) accepts unwiped Teams silver landing from the pull, bounded to the named original readers until the W1-S7 re-wipe
and a wipe-on-landing fix, or (b) orders the pull to wipe silver before its first apply.

-- 2.0.0_SA_COO~T2
