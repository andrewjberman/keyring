# MDPF_HEALGAP stage-3 decomp -- CVO verdict

**archetype:** VALIDATE

**Subject:** `workflows/atom_decomposition/runs/mdpf-healgap-operative-surfaces/20260831T191014Z/`
**Decomp author:** `2.0.0_SA_COO`
**Certifier:** `3.0.0_SA_CVO`
**Date:** 2026-08-31
**Trigger:** COO msg 89909, AE msg 89916, COO msg 89919.

## Verdict

**NOT CERTIFIED AS A CONSUMABLE ATOM-DECOMP RECTANGLE.** The run is correctly labeled
`UNCERTIFIED, SOLO`; it has no fan-out cohort, no dry round, no certifier packet, no planted mutant,
and no `rectangle.final.certified.json`. Under `projects/ATOM_DECOMP/skill/atomic-decomposition/SKILL.md`
Rule 14(e), those missing limbs are certification requirements, not decoration.

**CVO ACCEPTS THE RUN AS AN HONEST C0 MEASUREMENT PACKET WITH THE UPDATED ROOT-CAUSE DISPOSITION.**
The source-backed corrections F-1/F-2/F-3/F-4 re-derive at the cited files, and the open RC-B branch
is now falsified by live CloudWatch metrics. This is enough for CTO to use the packet as design input;
it is not enough to clear placement, cut TOs without the decomp banner, or claim a certified final
rectangle.

## Checks

| Check | Result | Evidence |
|---|---|---|
| Commit and run files landed | PASS | `e74a2642d2` adds `run.json`, `axis_declaration.json`, `rectangle.c0.json`, `FINDINGS.md`, and updates `MDPF_HEALGAP.json`; 958 insertions / 5 deletions. |
| Degraded-state disclosure | PASS | `run.json` and `rectangle.c0.json` state solo run, no fan-out, not certified, no final certified rectangle, and every cell placement `PENDING-ANDREW`. |
| F-1: trigger lambda is Terraform-managed | PASS | `cot-detection-layer.tf:24-30 @9d13da303f` comment heads `data "aws_secretsmanager_secret"`; `lambdas.tf:19-37 @9bf20c960b` declares `module "cot_bd_session_trigger"`; `modules/yang-lambda/main.tf:22-35 @e567ebf4da` declares `aws_lambda_function.this`. |
| F-2: heal cadence is declared | PASS | `schedule-et.tf:78-97 @16fc99460c` declares `aws_scheduler_schedule.cot_bd_session_daily_et`, `cron(30 7 * * ? *)`, timezone `America/New_York`, target `cot-bd-session-trigger`, input `session-refresh`. |
| F-3: runner fire is a placeholder before mint | PASS | `cot_rebalancer_runner.tf:159-171 @27a3a98cdc` declares the daily pull at `cron(0 6 * * ? *)` with the `PLACEHOLDER 06:00Z` chain-timing comment. |
| F-4: on_success exists on subject function | PASS | `cot_rebalancer_runner.tf:192-239 @27a3a98cdc` declares `aws_lambda_function_event_invoke_config.cot_rebalancer_runner` with `destination_config { on_success { ... } }`. |
| RC-B discriminator | FALSIFIED | CVO live CloudWatch read: target window 2026-08-30T18:00Z to 2026-08-31T13:00Z, `bd-cot-keepalive`, 19/19 hourly invocation datapoints each `Sum=4.0`, 19/19 error datapoints each `Sum=0.0`. |
| Positive control | PASS | Same query shape over 2026-08-29T18:00Z to 2026-08-30T13:00Z also returned 19/19 hourly invocation datapoints each `Sum=4.0` and 19/19 error datapoints each `Sum=0.0`. |

## Disposition

RC-B is no longer an open branch. The keepalive did not gap overnight; it invoked continuously and
cleanly across the outage window. RC-A, the ordering defect, is therefore the sole surviving incident
root cause for the 2026-08-31 missing date: the runner fires near maximum session age before the daily
mint. The separate S9 recovery gap still stands: moving the schedule reduces exposure but does not
create a mid-window recovery mechanism.

Placement remains open at Andrew and blocks TO issuance. Any TO cut before a future full certification
must still carry `UNCERTIFIED DECOMP` on its face, exactly as the decomp states.

## Limits

- I did not independently re-derive the S3 stamp/IAM guard cells S3/S8.
- I did not certify the S10 sibling set as affected; it remains an unmeasured class.
- I did not run a planted-mutant certification pass, and I did not create or authorize
  `rectangle.final.certified.json`.
- Bare `comp-which` did not resolve in this PowerShell session; I used direct source reads and the
  repository-local `.tools/aws` wrapper for the live CloudWatch checks.

-- 3.0.0_SA_CVO
