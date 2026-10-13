# AMGT_HARVST task order -- `HVST-bz-8` -- ROUND 84, workstream BRIEFOFF (`1.0.0_SA_CTO~DELL1` msg 5131, Andrew-direct ~20:0xZ call 7): THE 3 AM WSJ/FT MORNING BRIEF SCHEDULE IS DISABLED, NOTHING DELETED

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bz-8.the-3am-morning-brief-schedule-is-disabled</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bz-8</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~HV1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the ONE schedule touched is `astn-wsjft-3am-run` (EventBridge Scheduler, default group, us-east-1); no other schedule, rule or runner task is stopped, started or changed.
comp-iam: RUN at L5 -- no IAM change: no role, policy, trust or permission boundary is touched; the apply changes the `state` attribute of one scheduler schedule only.
comp-adversary: RUN at L5 -- the adversary is an apply that changes more than the one attribute (the plan is read first and anything beyond 0 to add / 1 to change / 0 to destroy is a STOP), an untargeted apply that sweeps unrelated drift in the module, and an edit that deletes the schedule instead of disabling it.
</preflight>

## 0. THE CELL

Andrew-direct (recorded `ANDREW_DIRECT_20261013_200xZ_NINE_OPEN_CALLS_ANSWERED_FIRMBKTS_DEMQUE_BRIEF_HARVEST.md` item 7): "No let's turn that off we don't need that." The 3 AM digest of WSJ and
FT news (Bright Data pull, summary, SES email) is turned off by DISABLING its schedule. The schedule is the only trigger: the Lambda, its IAM, the bucket and the instance stay as they are.
- **The schedule:** `astn-wsjft-3am-run`, EventBridge Scheduler, default group, us-east-1. Read on 2026-10-13 ~20:2xZ: `State ENABLED`, `ScheduleExpression cron(0 3 * * ? *)`, timezone
  `America/New_York`, target Lambda `astn-wsjft-orchestrator`, input `{"mode":"run"}`. One schedule and no EventBridge rule carry the `astn` prefix.
- **Its Terraform:** module `infra/aws/terraform/astn-pipeline`, resource `aws_scheduler_schedule.astn_run` in `orchestrator.tf`, one `state = "ENABLED"` line. It is the only writer of the property.
- **Timing:** it fires at 03:00 ET, which is 07:00Z. An apply that lands before then spares tonight's run.

## 1. START CONDITIONS (all four read at the start, not assumed; any false: DO NOT START, file one row)

- (a) BOTH never-widen halves are on file and read SIGNED at their pins: COO half `deliverables/2.0.0_SA_COO_W1/round84/NEVER_WIDEN_HALF_COO_BZ8_BRIEF_OFF.md` and CTO half
  `ledger/NEVER_WIDEN_ROUND84_BZ8_CTO_HALF.md` (`git show <pin>:<path>`; the issuer states the pins in the message that sends this order).
- (b) `.tools/aws scheduler get-schedule --name astn-wsjft-3am-run --query State --output text` reads `ENABLED`. If it already reads `DISABLED`, make NO change, take no apply, and go to step 5.
- (c) You work in your own linked worktree cut from the pin the issuer states (`git worktree add ../<slot> -b <branch> <pin>`), never in the shared tree.
- (d) A deploy-completion ledger entry is open (step 1) before any edit.

## 2. THE ACT (dell1, once)

1. **Open the ledger:** `python .tools/deploy_ledger.py open --slug astn-3am-off-20261013 --title "HVST-bz-8: disable the astn-wsjft-3am-run schedule" --author 0.7.0_AE_CloudOps~HV1
   --leg "EDIT|git|orchestrator.tf state DISABLED|commit hash" --leg "APPLY|tf-schedule|targeted safe-apply of aws_scheduler_schedule.astn_run|plan 0/1/0 then Apply complete 0 added 1 changed 0 destroyed"
   --leg "VERIFY|verify|get-schedule State DISABLED, expression target input unchanged|AC1 AC2 AC3" --window-hours 4`.
2. **Edit ONE attribute** in `infra/aws/terraform/astn-pipeline/orchestrator.tf`: line 175 `state = "ENABLED"` becomes `state = "DISABLED"`, and the comment line above the resource
   (`# 3am ET digest run -- ENABLED at go-live ...`) gains a second line `# DISABLED 2026-10-13 (Andrew-direct, call 7): the morning brief is off; re-enable = set state back to "ENABLED" and apply.`
   No other line moves. Commit it with `.tools/safe-commit.sh` under your own author line.
3. **Plan, targeted, and READ it before any apply:** `terraform -chdir=infra/aws/terraform/astn-pipeline plan -target=aws_scheduler_schedule.astn_run -out=bz8.tfplan`. Save the whole output as `bz8_plan.out`.
   - It must read exactly `Plan: 0 to add, 1 to change, 0 to destroy`, and the one change must be `state: "ENABLED" -> "DISABLED"` on `aws_scheduler_schedule.astn_run`.
   - **Anything else (a replace, a second change, a destroy, a changed expression, target or input) is a STOP:** no apply, one row naming the line, keep working.
4. **Apply that saved plan, targeted:** `.tools/safe-apply.sh -chdir=infra/aws/terraform/astn-pipeline apply bz8.tfplan`. It must read `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.` Save as `bz8_apply.out`.
   Never `aws scheduler update-schedule` or any CLI edit: the source of truth is Terraform and a CLI edit would leave the source saying ENABLED.
5. **Read the world back** with the three criteria below, save each as `bz8_ac<n>.out`, close the ledger legs with their proof and `python .tools/deploy_ledger.py close --slug astn-3am-off-20261013`.
6. **Rollback (if the issuer or Andrew asks, and only then):** set the line back to `"ENABLED"`, plan targeted (must read 0 to add, 1 to change, 0 to destroy), `safe-apply` that plan. Nothing was deleted, so nothing is rebuilt.
Do NOT touch the Lambda, IAM, the bucket `opal-data-astn`, the SNS topic, SES, the EC2 instance or any other resource. Do NOT run an untargeted `terraform apply`.
Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round84/`. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>`, then keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round84/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/
infra/aws/terraform/astn-pipeline/orchestrator.tf
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bz-8"><invocation>.tools/aws scheduler get-schedule --name astn-wsjft-3am-run --query State --output text</invocation><expect>(?m)^DISABLED$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bz-8"><invocation>.tools/aws scheduler get-schedule --name astn-wsjft-3am-run --query ScheduleExpression --output text</invocation><expect>(?m)^cron\(0 3 \* \* \? \*\)$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bz-8"><invocation>grep -n -E "^[[:space:]]*state[[:space:]]*=" infra/aws/terraform/astn-pipeline/orchestrator.tf</invocation><expect>(?m)^\d+:\s*state\s*=\s*"DISABLED"$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC1 is the act, AC2 reads that the schedule was disabled and not altered or deleted (it exists with its own expression), AC3 reads that the Terraform
  source agrees with the world, so the next apply of the module cannot turn the schedule back on.
- **Dry-run at the base (issuer, dell1, 2026-10-13 ~20:3xZ):** AC1 base FAIL as expected (reads `ENABLED`); AC2 base PASS as expected (reads `cron(0 3 * * ? *)`, and it is also the after-state, so it is a control and
  not a discriminator); AC3 base FAIL as expected (the one `state` line reads `"ENABLED"`).
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/AMGT_HARVST.TO-HVST-bz-8.the-3am-morning-brief-schedule-is-disabled.proof_of_spec.json`
  (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-bz-8.the-3am-morning-brief-schedule-is-disabled`.
- Commit on your box branch with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 5131 and Andrew-direct ~20:0xZ call 7, "No let's turn that off we don't need that." The CTO's wording: "Disable astn-wsjft-3am-run under a pair; nothing deleted, rollback = re-enable."
- **What was read to size it (names and metadata only):** `aws scheduler get-schedule` (State, expression, timezone, target ARN, input, last modified 2026-06-25); `aws scheduler list-schedules --name-prefix astn` (1) and
  `aws events list-rules --name-prefix astn` (0); `comp-find` over the module's four `.tf` files for the scheduler resource (1 hit, `orchestrator.tf:173`); `org/projects/ASTN_WSJFT.json` (CLOSED 2026-08-25).
- **Why a workstream in round 84:** the schedule fires nightly at 07:00Z and the round-84 L10 is not tonight; see decomposition section 103. Disjoint boundary, disjoint write surface, a different `~lane`.
- **Not read here:** the orchestrator's other modes (`absence_check`) and whether anything else invokes the Lambda; the apply changes only the schedule, so neither is touched. The state of the Terraform backend lock and of any
  unrelated drift in the module is the seat's first plan read, which is why the plan is targeted and must read 0/1/0.
- **Pair:** COO half `deliverables/2.0.0_SA_COO_W1/round84/NEVER_WIDEN_HALF_COO_BZ8_BRIEF_OFF.md`; CTO half `ledger/NEVER_WIDEN_ROUND84_BZ8_CTO_HALF.md` (owed). The act does not start without both on file.
- **Risk named:** an apply that is wider than one attribute, and a CLI-side edit that leaves Terraform saying ENABLED. The first is stopped by the 0/1/0 plan read, the second by AC3.
- Seat `0.7.0_AE_CloudOps~HV1` is not registered at the cut; the issuer seats it (`/mstr-spawn`) once both halves are on file.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>84</round>
<workstream>BRIEFOFF</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
