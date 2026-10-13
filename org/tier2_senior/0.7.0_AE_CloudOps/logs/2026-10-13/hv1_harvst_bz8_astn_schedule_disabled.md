# The 3 AM morning-brief schedule disabled, and the instance the provider started stopped -- 0.7.0_AE_CloudOps~HV1

**Date:** 2026-10-13
**Task Order:** AMGT_HARVST.TO-HVST-bz-8.the-3am-morning-brief-schedule-is-disabled (round 84, workstream BRIEFOFF)
**Status:** COMPLETE (seat stands down)

---

## Objective

Disable the EventBridge Scheduler schedule `astn-wsjft-3am-run` (Andrew-direct 2026-10-13, call 7: "No let's turn that off we don't need that.") through Terraform, nothing deleted,
before its 07:00Z fire. The seat was re-seated by `0.0.0_AB_MSTR~DELL1` for this one order (CTO~DELL1 msg 5148) and stands down after it.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find "kit-terraform-pack" --files --limit 15` | PASS | DENOMINATOR 14 hits across 89236 files, corpus=all; found `KIT_TERRAFORM_PACK_RECORD.md`, which says the kit mirror was cut with archive 2.8.1 |
| comp-schedule | not run | SKIPPED | the order's preflight assigns it to L5 (the issuer); the one schedule was read directly with `aws scheduler get-schedule` before and after |
| comp-iam | not run | SKIPPED | no IAM object changed; the plan showed no role, policy or trust diff |

**What worked:** comp-find located the mirror record in one call. The rail's denials of a `find` over the mirror and of a piped census were taken as written; Glob and an unpiped call answered both.
**What failed:** nothing in the tools. The order's own `deploy_ledger.py` leg kind `tf-schedule` is not a valid kind (valid: git, s3-prefix, activation, ec2-baked-asset, verify, tf-lambda), and the order's literal `ps ... | head -40` cannot grade a process census (see Work Completed 5).
**Gap found:** `deploy_ledger.py` has no reopen or add-leg, so an entry closed under one message cannot be held open under the next.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Start conditions: both halves SIGNED at pins (COO `e56b1f595c`, CTO `a6c3b949e6`); schedule read ENABLED; worktree `C:/dev/wk-hv1-bz8` cut from `a6c3b949e6` | all four true |
| 2 | Ledger `astn-3am-off-20261013` opened (APPLY leg kind `activation`, the nearest valid) | OPEN |
| 3 | Edit `orchestrator.tf` line 175 plus one comment line, `safe-commit.sh` | `532f6f04cf`, 2 insertions, 1 deletion |
| 4 | `terraform init`: failed, lock pins archive 2.8.0 and the kit mirror holds only 2.8.1; archive block removed from the WORKTREE lock copy, uncommitted | init rc=0, aws stays 5.100.0 |
| 5 | Targeted plan (`-target=aws_scheduler_schedule.astn_run`) | `Plan: 0 to add, 3 to change, 0 to destroy` -- NOT 0/1/0: STOP, no apply, row D1-S14 |
| 6 | Amendment 1 probe: `terraform plan -help` | v1.15.8 lists no `-exclude`; stopped per the order |
| 7 | Pair re-signed for the 0/3/0 (COO `2c4840c471`, CTO `0e1ec395b4`); fresh targeted plan with `-out` | exactly the three signed changes, no replace or destroy |
| 8 | Pre-apply: instance `stopped` at 20:46:51Z; broker read 3 of 3 messages READ | clear |
| 9 | `.tools/safe-apply.sh -chdir=infra/aws/terraform/astn-pipeline apply bz8.tfplan` | `Apply complete! Resources: 0 added, 3 changed, 0 destroyed.` |
| 10 | Read-back | AC1 `DISABLED`, AC2 `cron(0 3 * * ? *)`, AC3 line 176 `state = "DISABLED"`; target, input, timezone unchanged |
| 11 | Instance found `running` (LaunchTime 20:48:11Z): the provider started it for the `user_data` change; row D1-S15 | no seat stops it unasked |
| 12 | Section 2b step 1: SSM process names | none of python, node, chrome, Xvfb, run.py (94 processes, 28 non-kernel, all listed) |
| 13 | Andrew's relayed yes (CTO ADDENDUM 3 `dfecbbe7d4`, COO msg 5199): ONE `stop-instances` | `stopping` 21:04:03Z, `stopped` read 21:04:28Z |
| 14 | Ledgers `astn-3am-off-20261013` (closed 20:51Z) and `astn-instance-started-20261013` (closed ~21:05Z) | both CLOSED |

Not done, and not asked by the order: a release tag, `record-terraform-deploy.sh`, and an UNTARGETED 0-diff plan. The post-apply plan was targeted: no resource changes, one output (`astn_public_ip`) moved because the instance was running.

## Verification

```
.tools/aws scheduler get-schedule --name astn-wsjft-3am-run --query State --output text            -> DISABLED
.tools/aws scheduler get-schedule --name astn-wsjft-3am-run --query ScheduleExpression --output text -> cron(0 3 * * ? *)
grep -n -E "^[[:space:]]*state[[:space:]]*=" infra/aws/terraform/astn-pipeline/orchestrator.tf       -> 176:  state                        = "DISABLED"
describe-instances i-059405dfefcb4b44a -> stopped, User initiated (2026-10-13 21:04:03 GMT)
```
The issuer re-read AC1 and AC2 independently at 20:5xZ. The proof_of_spec instance passed `proof-of-spec-check.py` (VALID, rc=0).

---

## Work Completed

### 5. The process-name read

The order's literal command (`ps -eo pid,etime,comm --sort=-etime | head -40`) sorts oldest first and caps at 40 lines: it printed 39 kernel threads, so its "NONE" would have been an empty verdict. It is kept in `bz8_instance_ps.out`, labelled UNDETERMINED. A second names-only read on the same SSM route (a variation the order did not spell out) printed totals and every non-kernel row, with the SSM agent rows as the positive control.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Stopped at 0/3/0 without applying | The order and both halves sign 0/1/0 only; the extra diffs deploy HG-t-18 Lambda code and change `user_data` |
| Removed the archive lock block in the worktree only | Init could not run otherwise; uncommitted and outside the order's paths, so a drift in the plan would still read as a STOP |
| Opened a second ledger entry for the instance | The first was closed under msg 5182 before 5183 asked to keep it open; the tool cannot reopen |
| Did not stop the instance until Andrew's yes | EC2 stop is reserved for Andrew's confirmation (CLAUDE.md Agent Autonomy) |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/terraform/astn-pipeline/orchestrator.tf` | `state` ENABLED to DISABLED plus a comment line | Yes -- `532f6f04cf` on `wk-hv1-bz8-astn-off`, drained to `box/dell1` |
| `infra/aws/terraform/astn-pipeline/.terraform.lock.hcl` | archive block removed (worktree only) | No -- local only, by design |
| `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round84/` | plan, apply, readback, ps and stop evidence | Yes -- `206d10edb6`, `74614b6fe3` (branch); first three files also on `box/dell1` |
| `.../0.7.0_AE_CloudOps~HV1/AMGT_HARVST.TO-HVST-bz-8....proof_of_spec.json` | the instance, VALID | Yes -- `1bdb4499b2` (drained). Its `session_log` field reads NONE-YET; this file is the log |
| `org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md` | rows D1-S14, D1-S15 | Yes -- `f2718141c5`, `f40f72599e` on `box/dell1` |
| `org/critical_paths/change_management/...astn-3am-off-20261013..., ...astn-instance-started-20261013...` | two ledger entries, opened and closed | Yes -- branch, `74614b6fe3` carries the second close |

---

## Blockers

None. Push state: LOCAL on `box/dell1`; no push by this seat.

---

## Current State

`astn-wsjft-3am-run` is DISABLED in the world and in `orchestrator.tf`, nothing deleted; the orchestrator Lambda now carries the dormant HG-t-18 `ft_reattempt` build and the instance `user_data` hash is the new one. The instance `i-059405dfefcb4b44a` is stopped (21:04:28Z). Both ledger entries are closed. Branch `wk-hv1-bz8-astn-off` at `74614b6fe3` holds one commit not yet drained into `box/dell1`; worktree `C:/dev/wk-hv1-bz8` and `bz8.tfplan` (module dir, untracked) remain.

**Lesson for the next pair touching an `aws_instance` `user_data`:** the provider stops a running instance to modify it and STARTS a stopped one afterwards; name the start in the blast radius.

---

## Next Steps

1. **[2.0.0_SA_COO~W1] Drain `wk-hv1-bz8-astn-off` @74614b6fe3** -- the stop evidence and the second ledger close.
2. **[2.0.0_SA_COO~W1] Disposition rows D1-S14 and D1-S15** -- both `UNDER_INVESTIGATION`; the disarm owner is the issuer.
3. **[0.0.0_AB_MSTR~DELL1] Remove worktree `C:/dev/wk-hv1-bz8` and its branch** once drained; the archive-lock edit dies with it.
