# TO IRPT_BCKEND.TO-IB-er-203 -- The daily production trigger for the holdings-basis gold (PRD v0.19 ruling 9; CTO ruling 102520)

<to_id>IRPT_BCKEND.TO-IB-er-203</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~65</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~E</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO ruling 102520 ("plus the daily schedule ... under
its own ledger"), PRD ADDENDUM v0.19 ruling 9 | **Decomp cell:** `IB-er-203` (decomposition section 16) |
**outcome_ref:** FWD-3 | **depends_on:** none (the producer exists at build 23004aaf98)

---

## WORKER FACE

### THE CELL

`IB-er-203` -- a production pipeline must be SCHEDULED (CLAUDE.md), never run ad hoc. The holdings-basis gold producer
is `C:/Users/AndrewBerman/Desktop/ajb_workspace/data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py`
(it reads `sources.json` beside it and writes
`lib/opal_naming.address("irpt", "49financial", "gold", "holdings_performance_daily" | "holdings_performance_manifest", "date=...")`).
The estate's pattern to copy is ~M's Holdings snapshot:
- EventBridge Scheduler schedule `irpt-holdings-snapshot` (ENABLED, `cron(15 10 ? * MON-FRI *)`, America/New_York)
  invokes `irpt-holdings-refresh-lambda` with role `irpt-holdings-snapshot-scheduler-role`;
- Terraform in `infra/aws/terraform/investor-reporting/directory/holdings_refresh.tf` and `schedule.tf`.

**Build** (every name from the builder; none typed):
1. A new Terraform root `infra/aws/terraform/investor-reporting/holdings-performance/` with:
   - the Lambda `lib/opal_naming.name("irpt", None, "holdings-performance", "lambda")`
     (= irpt-holdings-performance-lambda), packaging the producer and its declaration through
     `infra/aws/lambda/ci/lambda-source-map.json` and `build-and-upload.sh` (pandas/pyarrow from the existing
     `irpt-performance-native-layer`), with a handler that runs the producer for the latest completed trading day
     (`lib/trading_calendar.py`);
   - an execution role that reads the declared silver and writes ONLY the two gold prefixes;
   - the schedule `lib/opal_naming.name("irpt", None, "holdings-performance", "daily")`
     (= irpt-holdings-performance-daily), ENABLED, `cron(...)` in America/New_York, set AFTER the declared silver lands
     (measure the landing time from the silver partitions' LastModified and state it in a comment), with its own
     scheduler role.
2. Deploy with `.tools/safe-apply.sh` under a deploy ledger (`.tools/deploy_ledger.py`) opened before the first write:
   plan, apply, readback, one invoke of the Lambda for the latest trading day (its manifest row is written), re-plan
   with no changes. New resources only; nothing served moves (no reader of the gold is switched).

### ACCEPTANCE (run from your worktree root)

<criterion id="E2-AC3" cell_refs="IB-er-203"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r2e/e2_ac3_daily_schedule.py"</invocation><expect>E2-AC3 PASS</expect></criterion>
`E2-AC3` -- the schedule irpt-holdings-performance-daily exists, ENABLED, on a cron expression, with a target. Base:
FAIL (ResourceNotFoundException).

<expected_criteria>E2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Deploy discipline.** The ledger opens before the first write; Terraform only through safe-apply; no lambda
  update-function-code. The producer's code is the DS seat's (0.4.0_DS_ClientPlatform~E): package it, do not edit it.
- **Refusal clause.** If a criterion cannot be met as written (for example, a builder refuses a name), stop, write the
  reason in your report and a surprise row, and do not weaken the check.

<paths>
infra/aws/terraform/investor-reporting/holdings-performance/
infra/aws/lambda/investor-reporting/holdings-performance/
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 16 (workstream ~E, round 2), cell `IB-er-203`.
<owned_cells>IB-er-203</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: E2-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~65/IRPT_BCKEND.TO-IB-er-203.holdings-performance-daily-schedule.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> E2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, the criterion's last line, the ledger slug, and any surprise row id
(`IRPT_BCKEND-W65-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- the estate's twin (irpt-holdings-snapshot, ENABLED, cron(15 10 ? * MON-FRI *) America/New_York -> irpt-holdings-refresh-lambda) was read; this cell adds the holdings-performance twin.
comp-iam: RUN -- denominator: 0 of the account's existing roles are touched; 2 roles are NEW (execution + scheduler; read the declared silver, write the two gold prefixes only). Blind at the cut: the new roles do not exist until the plan, so their coverage is the plan's IAM diff, which the worker prints in the ledger before apply.
comp-blast: DECLARED-NOT-APPLICABLE -- new resources only; nothing existing is changed or deleted.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- no reader of the gold is switched.
comp-adversary: RUN -- E2-AC3 dry-run at the base: FAIL (ResourceNotFoundException for irpt-holdings-performance-daily). The builder resolves both names (irpt-holdings-performance-lambda, irpt-holdings-performance-daily).
lane: the <paths> block IS the grant.
</preflight>
