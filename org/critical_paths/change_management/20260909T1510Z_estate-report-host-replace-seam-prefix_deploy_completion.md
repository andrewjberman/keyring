# DEPLOY COMPLETION LEDGER -- estate-report HOST REPLACE, the OS-s-20 consumer switch

**Opened:** 2026-09-09T15:10Z by `0.7.0_AE_CloudOps~W`
**Status:** OPEN -- the apply has NOT been performed at this write
**TO:** `org/missions/D11/NFRA/NFRA_OUTSET/task-orders/NFRA_OUTSET.TO-OS-s-20.the-consumer-switch-host-replace.md`
(cell `OS-s-20`, outcome_ref FWD-3; issuance `e4dbe0448e`)

⛔ **Committed OPEN before the apply, so "opened first" is a fact in git history rather than a claim
in prose.** Closed in a second commit after the legs verify. Same shape as the OS-s-19 entry
(`20260909T1352Z_...`, opened at `6dbb1e6a3a`).

## AUTHORITY -- the "stopping EC2 / unrecoverable" word, already given

**Andrew-direct 2026-09-09 ~14:2xZ at the `1.0.0_SA_CTO` terminal, VERBATIM "All recs approved"**,
record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260909_142xZ_ALL_RECS_APPROVED_THREE_CALLS_COOA_REGISTERING.md`
@`e1b44ba4cc`, CALL 2. Verified at this seat, not taken from the face:
`git merge-base --is-ancestor e1b44ba4cc HEAD` -> YES, and the record's CALL 2 reads
"the estate-report host is REPLACED (destroy and recreate ...) to set `ESTATE_OUTSET_SEAM_PREFIX`,
under its own NEVER-2 change-management entry, outside the run window, AFTER OS-s-19, with the
orchestrator's target instance ID re-pointed and verified LIVE before the entry closes ... the lane
executing OS-s-20 does not ask again for the same act."

**It authorises ONE replace of ONE host and no mechanism change.** This entry claims nothing wider.

## What

One `user_data` change adding a single line to the `runtime.env` heredoc
(`instance.tf:130-151`): `ESTATE_OUTSET_SEAM_PREFIX=s3://${local.bucket_name}/outset`, plus the WHY
comment beside it. `instance.tf:83` carries `user_data_replace_on_change = true` deliberately, so
this **destroys and recreates** `aws_instance.estate_report_runner` and **the instance id changes**.

**THE VALUE IS AN `s3://` URI BY CONTRACT, not a bare prefix.** `_stratum_propagation` appends
`/comp_heat_drift.json` (`estate_report_runner.py:1844`) and hands the result to `_outset_loader`,
which branches on `source.startswith("s3://")` (`:1802`). A bare `outset` would be read as a LOCAL
PATH and fail as `artifact ABSENT` -- reported as a FAILED publish, correctly but misleadingly,
since nothing would have failed except that line.

## ⛔ ONE REPLACE, NOT TWO -- the clause read BEFORE the apply, and what it decided

Both faces require this to be settled first, because choosing wrong costs a **second** host
replacement. **DECIDED: the cadence (`TO-OS-s-21`) lives OFF-HOST, so this replace carries ONLY the
prefix.** Not a preference -- three measured facts, filed as row `NFRA_OUTSET-S21`:

1. **The host never has a working tree.** `estate_report_runner.py:275` clones with
   `--filter=blob:none --no-checkout`. A census of every clone/checkout in that file
   (`--enumerate 'git.*clone|checkout|sparse-checkout'` -> **10 hits across 2860 lines / 78
   sections**) finds ONE clone, TWO on-demand single-path checkouts (`:493`, `:865`), ZERO
   sparse-checkout and ZERO full checkout.
2. **An on-host producer would not fail loudly -- it would answer the wrong question.**
   `comp-heat drift`'s own question is "what has been written in **this workspace** that is not in
   any commit". On this device it answered `n=154, n_modified=6, n_untracked=148`. On a fresh
   no-checkout clone the honest answer is zero, and the seam would publish it with
   `answer_state OK` and a correct-looking denominator -- the `W2-S21` confident-zero class exactly.
3. **The architecture already forbids the remedy.** `estate_report_runner.py:1814-1820`:
   "PRD s.3's answer is **not** to give this host a workspace but to have the tools PUBLISH."

## THE WINDOW

`estate-report-0900et` **ENABLED**, `cron(0 9 * * ? *)` `America/New_York`. Today's run:
launched 13:00:45Z, self-stopped **13:11:04Z**. Next fire **2026-09-10 13:00Z**. This apply runs
after 15:10Z with the instance **stopped** -- read LIVE immediately before the apply, never from
this file. **Outside the window**, and the accept is the next scheduled fire; the box is NOT started
to force an early exercise.

## PRE-STATE, measured live before the apply

| | value |
|---|---|
| Instance | `i-0512bd3cbaf602b7f`, state `stopped`, AZ us-east-1a, ENI `eni-0b7fbc7e7c27e3d89`, private IP 172.31.89.95 |
| Runner bytes the NEW host will boot | `s3://opal-estate-report/code/estate_report_runner.py`, **159,687 B**, ETag `e75c59a35457535ca0d339c9f59589f5`, VersionId `GQny85Je837UhagoFc0FY8eoJzcB1RFy` (read live, not from the face) |
| Orchestrator target | `ESTATE_INSTANCE_ID=i-0512bd3cbaf602b7f` (`get-function-configuration`) |
| `user_data` hash | `3e803c2cdd3480781adcab810fd13d30bad92b21` -> `9699e9bcadee86fc0dc1bd5deba6d60171c56736` |

## THE PLAN, READ RATHER THAN SUMMARISED: 1 to add, 3 to change, 1 to destroy

⛔ **FOUR resources move, not one, and all three of the extra changes are consequences of the single
replacement** -- stated because "one replace" must not be read as "one changed resource":

| Resource | Change | Why it moves |
|---|---|---|
| `aws_instance.estate_report_runner` | **REPLACED** | `user_data` forces replacement; `id` -> known after apply |
| `aws_iam_role_policy.runner_selfstop` | in-place | `SelfStopThisInstanceOnly` is scoped to the instance ARN |
| `aws_iam_role_policy.orchestrator` | in-place | `StartRunnerInstanceOnly` / `DescribeInstances` scoped to the instance ARN |
| `aws_lambda_function.orchestrator` | in-place | `orchestrator.tf:37` `ESTATE_INSTANCE_ID = aws_instance.estate_report_runner.id` |

Nothing unrelated to the replacement appears in the plan.

## Legs

1. [ ] `safe-apply` (never bare `terraform apply`; vendored `.tools/terraform.exe` v1.9.8, not the
       PATH substitute which re-pins remote state)
2. [ ] Unscoped re-plan reads 0 to add, 0 to change, 0 to destroy
3. [ ] **The orchestrator's target agrees with a live instance** -- `get-function-configuration` on
       `estate-report-orchestrator` reads the NEW id, `describe-instances` on that id returns a live
       instance, and the two MATCH. (`lambda_function.py:34` reads the id at IMPORT, so a warm
       container can hold the old one until the configuration change retires it.) A CONTROL on this
       close, never the accept.
4. [ ] `ESTATE_OUTSET_SEAM_PREFIX` present in the live `runtime.env` on the new host (SSM). A
       CONTROL arm, never the deciding line -- the deciding line is a served day.

## Rollback -- stated before the act, because a destroyed instance is not restored

There is no "restore" here: the rollback is **a further replace under the prior `user_data`**, i.e.
revert the one-line `instance.tf` change and `safe-apply` again, which destroys and recreates once
more. Cost: a second replacement and a second new instance id. The prior `user_data` is recoverable
from git (`instance.tf` @HEAD before this commit) and its hash is recorded above, so the rollback is
a `git revert` of one file plus one apply. **The data plane is untouched by either direction** --
no S3 object, no schedule and no IAM grant beyond the two ID-scoped statements changes.

## Close condition

All four legs checked. Closed in a second commit that flips this Status line.
**The ACCEPT is NOT this entry** -- `O20-AC1` reads a SERVED DAY and cannot pass before the
2026-09-10 13:00Z fire at the earliest. **Nothing is armed to watch that fire** (standing
moratorium); the scheduled fire is the acceptance, not an ad-hoc run.
