# TO IRPT_BCKEND.TO-IB-m20-201 -- R4: enable the scheduled daily Holdings producer (irpt-holdings-snapshot)

<to_id>IRPT_BCKEND.TO-IB-m20-201</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~43</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-201`
(`decompositions/IRPT_BCKEND_DECOMP_R20_M.md`) | **outcome_ref:** FWD-5, goal criterion 3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-mr-201` -- flip the EventBridge Scheduler schedule `irpt-holdings-snapshot` from DISABLED to ENABLED. Both halves
of the never-widen request are SIGNED:
- request (COO half) `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_R4_ENABLE_20260928.md`,
  blob 342f04c129 (commit 8d601db072);
- CTO half `org/tier1_exec/1.0.0_SA_CTO/deliverables/SIGNOFF_R4_ENABLE_HOLDINGS_SCHEDULE_20260929.md` (f541e1cbf0);
- CRO half `org/tier1_exec/4.0.0_SA_CRO/deliverables/NEVER_WIDEN_SIGNOFF_CRO_HALF_R4_ENABLE_20260929.md` (283d590379).
Read all three first. Their conditions bind you: never a hand-run in place of the scheduled fire; a manual non-QA
invoke only under its own ledger (you make none); the first scheduled fire (Tue 2026-09-29 10:15 America/New_York =
14:15Z) is the per-firm proof -- that read-back is cell IB-mr-204, not yours.

The resource is `aws_scheduler_schedule.irpt_holdings_snapshot` in
`infra/aws/terraform/investor-reporting/directory/schedule.tf` (lines 69-90). Measured 2026-09-29 00:5xZ: `state =
"DISABLED"`, `cron(15 10 ? * MON-FRI *)` America/New_York, target `module.irpt_holdings_refresh.function_arn`, input
`{"kind": "irpt_holdings_refresh", "note": "R4: STILL DISABLED -- ..."}` (no `qa` key: the dispatch serves when `qa` is
absent, `refresh_dispatch.py:134`).

### BUILD

1. Confirm the request blob still reads 342f04c129 (`git rev-parse HEAD:<request path>`); if not, STOP with a row.
2. Open ledger FIRST: `python .tools/deploy_ledger.py open --slug irpt-holdings-schedule-enable-m-20260929 --title
   "R4 step 4: irpt-holdings-snapshot DISABLED -> ENABLED (COO 8d601db072, CTO f541e1cbf0, CRO 283d590379)" --author
   0.9.0_WK_IRPT_BCKEND~43 --leg "A1|activation|safe-apply aws_scheduler_schedule.irpt_holdings_snapshot|Apply complete 0
   added 1 changed 0 destroyed" --leg "V1|verify|scheduler get-schedule|State ENABLED, target irpt-holdings-refresh-lambda,
   no qa in input; re-plan No changes" --leg "V2|verify|the first scheduled fire read back per firm (IB-mr-204)|per firm:
   command id, status, published revision, served manifest VersionId moved on Success / unchanged on failure"`. Commit the
   sentinel and entry at once.
3. Edit only the schedule block: `state = "ENABLED"`; the input `note` becomes "R4: ENABLED under signed halves (COO
   8d601db072, CTO f541e1cbf0, CRO 283d590379)"; the `description` and the two `holdings_snapshot_schedule_*` output
   descriptions stop saying DISABLED. Nothing else in the root moves.
4. `terraform -chdir=infra/aws/terraform/investor-reporting/directory plan -lock=false` must read 0 add / 1 change /
   0 destroy on `aws_scheduler_schedule.irpt_holdings_snapshot` only (anything else: STOP, row). Then
   `HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/directory apply` (-target that
   one address if needed). Read back with boto3 `scheduler.get_schedule(Name="irpt-holdings-snapshot")`; re-plan (No
   changes). Close legs A1 and V1 with that proof. Leave V2 and the ledger OPEN (IB-mr-204 closes them). Commit.
5. Do NOT invoke the dispatch, do NOT stop or start the runner.

### ACCEPTANCE

<criterion id="IBM20-201-AC1" cell_refs="IB-mr-201"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_m201_schedule_enabled.py</invocation><expect>ENABLED followed by the schedule expression and its timezone</expect></criterion>
`IBM20-201-AC1` -- the schedule reads ENABLED on AWS, targets the dispatch with no qa, and ledger legs A1/V1 carry proof.

<expected_criteria>IBM20-201-AC1</expected_criteria>

Dry-run at the base 2026-09-29 01:0xZ: NOT-ENABLED: State DISABLED (FAIL as expected).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **WORLD, bounded:** the one schedule resource. No other Terraform address, no dispatch invoke, no package mint, no
  served write. Rollback: `state = "DISABLED"` and safe-apply, recorded in the ledger.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `IRPT_BCKEND-W43-S<k>`), and do not weaken the test to pass.

<paths>
infra/aws/terraform/investor-reporting/directory/schedule.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-holdings-schedule-enable-m-20260929.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R20_M.md</decomp_doc> (round 20, workstream ~M), cell `IB-mr-201`.
<owned_cells>IB-mr-201</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM20-201-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~43/IRPT_BCKEND.TO-IB-m20-201.r4-enable-the-holdings-schedule.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM20-201-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the plan line, the apply line, the get-schedule read-back, the re-plan, legs A1/V1
proof, commit hashes.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- irpt-holdings-snapshot DISABLED, cron(15 10 ? * MON-FRI *) America/New_York, first fire after the flip = Tue 2026-09-29 14:15Z (a trading day, lib/trading_calendar).
comp-iam: DECLARED-NOT-APPLICABLE -- no policy change; the scheduler role already holds lambda:InvokeFunction on the dispatch only.
comp-adversary: RUN -- the schedule input carries no qa key, so a fire SERVES (refresh_dispatch.py:134); the CTO and CRO halves both require the scheduled fire, not a hand-run, as the proof.
lane: the <paths> block IS the grant; schedule.tf's holdings slot is ~M's (CTO exact-file grant @800e5c8f75).
</preflight>

Source: `STATUS~M.md` @dc913869d8 next-list item 1; CTO ruling 102516.
