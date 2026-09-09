# DEPLOY COMPLETION LEDGER -- estate-report HOST REPLACE, the OS-s-20 consumer switch

**Opened:** 2026-09-09T15:10Z by `0.7.0_AE_CloudOps~W` (committed OPEN at `4c173cddbc`)
**Status:** **CLOSED 2026-09-09T15:05Z** -- all four legs verified; the ACCEPT remains pending the
2026-09-10 13:00Z scheduled fire and is NOT claimed here
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

1. [x] `safe-apply` at 14:56:4xZ. Instance state read LIVE immediately before: **`stopped`**
       (14:56:30Z); schedule read LIVE: ENABLED, `cron(0 9 * * ? *)`. Result: **`Apply complete!
       Resources: 1 added, 3 changed, 1 destroyed`**. `i-0512bd3cbaf602b7f` destroyed in 11s,
       **`i-0584e17d283fa7ef4`** created in 14s.
2. [x] Unscoped re-plan: **"No changes. Your infrastructure matches the configuration."**
3. [x] **The orchestrator's target agrees with a live instance.**
       `get-function-configuration` -> `ESTATE_INSTANCE_ID = i-0584e17d283fa7ef4`;
       `describe-instances` on that id -> exists, state `running`; terraform output
       `estate_report_runner_instance_id = i-0584e17d283fa7ef4`. **All three agree.**
       NEGATIVE CONTROL on the comparator, because an equality test that cannot fail is not a test:
       the retired id `i-0512bd3cbaf602b7f` against the new one -> **MISMATCH**, so the match above
       is a measurement.
4. [x] `ESTATE_OUTSET_SEAM_PREFIX` in the live `runtime.env` on the NEW host, read via SSM:
       **`ESTATE_OUTSET_SEAM_PREFIX=s3://opal-estate-report/outset`**, 1 occurrence, and the file
       now carries **12** variables against 11 before. The SSM principal was read inside the same
       invocation and is
       `arn:aws:sts::313476888478:assumed-role/estate-report-runner-role/i-0584e17d283fa7ef4`, so
       this is the new host and not a stale one.
       **AND THE GRANT STILL HOLDS ON THE NEW INSTANCE** (a fresh instance profile assumption):
       `get-object outset/comp_heat_drift.json` -> rc 0, **27,060 B**; NEGATIVE CONTROL on a `logs/`
       object the role has no `GetObject` on -> rc 254 AccessDenied.

## POST-STATE

| | value |
|---|---|
| Instance | `i-0584e17d283fa7ef4`, LaunchTime 2026-09-09T14:57:29Z (was `i-0512bd3cbaf602b7f`) |
| Orchestrator target | `ESTATE_INSTANCE_ID=i-0584e17d283fa7ef4`, agreeing with a live instance |
| `runtime.env` | 12 variables, including the seam prefix as an `s3://` URI |
| Terraform | unscoped plan 0/0/0 |

## ⛔ A CONSEQUENCE NO FACE NAMED: THE REPLACE FIRED A REPORT RUN

Filed as row **`NFRA_OUTSET-S22`**. The order requires the replace "outside the run window" and
forbids starting the box to force an early exercise. **The replacement starts it anyway**:
`instance.tf:236-241` deliberately STARTS the units on the creation boot rather than only enabling
them, because an earlier creation boot left both units enabled-and-inactive with no dead-man's
switch armed. Measured via SSM: `estate-report.service` `activating`, `ExecMainStartTimestamp`
**Wed 2026-09-09 14:58:27 UTC**; deadman `active`. Nobody started the box; the replace did, and any
future replacement of this host will do the same.

**It does not contaminate the accept and it is not admissible as one.** `O20-AC1` reads a SCHEDULED
run; a creation-boot run is not scheduled, and ad-hoc artifacts are never production evidence. It is
QA signal only.

⛔ **AND IT OVERWRITES TODAY'S SERVED REPORT AT THE SAME KEY**, which would have destroyed
`O20-AC1`'s own negative arm -- the face requires "the 2026-09-09 served report (run under the
un-switched host) reads `INSTRUMENT_UNAVAILABLE` on the same stratum". Bucket versioning is
**Enabled**, and the un-switched baseline is pinned here BEFORE the overwrite:

| | value |
|---|---|
| Key | `daily/2026/09/09/estate-report-2026-09-09.json` |
| VersionId | **`8SP4fGAuhE8twzBpucMPsYbotD6Tddty`** |
| Written | 2026-09-09T13:11:02Z by `i-0512bd3cbaf602b7f` (the un-switched host), 162,172 B |
| Its propagation reading | `/ai/groups/A/stratum_status` = **`INSTRUMENT_UNAVAILABLE`** (also at `/run_bundle/stages[3]/strata_status/A`) |

The negative arm addresses that VersionId explicitly rather than the key, so it survives every later
run. Nothing was deleted (PRD R-5).

## Rollback -- stated before the act, because a destroyed instance is not restored

There is no "restore" here: the rollback is **a further replace under the prior `user_data`**, i.e.
revert the one-line `instance.tf` change and `safe-apply` again, which destroys and recreates once
more. Cost: a second replacement and a second new instance id. The prior `user_data` is recoverable
from git (`instance.tf` @HEAD before this commit) and its hash is recorded above, so the rollback is
a `git revert` of one file plus one apply. **The data plane is untouched by either direction** --
no S3 object, no schedule and no IAM grant beyond the two ID-scoped statements changes.

## Close condition -- MET

All four legs checked and the post-state measured. Closed in a second commit flipping the Status
line above.

⛔ **THE ACCEPT IS NOT THIS ENTRY, AND THE ORDER DOES NOT FLIP HERE.** `O20-AC1` reads a SERVED DAY
produced by a SCHEDULED run of the replaced host, so it cannot pass before **2026-09-10 13:00Z** at
the earliest. This entry records that the ACT landed and is verified on the infrastructure plane;
the ACCEPT is a separate reading on a separate day. **Nothing is armed to watch that fire** (standing
moratorium), and the box was not started to force an early exercise -- the one run that did occur was
caused by the replacement itself and is recorded above as QA, never as evidence.

## Rollback -- NOT exercised, and still stated

Unused. Had a leg failed, the path was a further replace under the prior `user_data` (revert one
file, apply again, accept a second new instance id), with the data plane untouched in either
direction. Recorded before the act at `4c173cddbc` rather than reconstructed here.
