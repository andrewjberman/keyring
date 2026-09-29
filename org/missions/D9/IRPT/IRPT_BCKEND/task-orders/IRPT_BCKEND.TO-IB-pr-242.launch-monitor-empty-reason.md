# TO IRPT_BCKEND.TO-IB-pr-242 -- The INF EC2 launch monitor never suppresses a stop whose reason reads empty

<to_id>IRPT_BCKEND.TO-IB-pr-242</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~85</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-29</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** row S216 and WK~81's diagnosis (TO-IB-pr-241, drained @0b5cdb06f9);
1.0.0_SA_CTO 102969 | **Decomp cell:** `IB-pr-242` (decomposition section 23) | **outcome_ref:** FWD-3 (INF) |
**depends_on:** none

---

## WORKER FACE

**The cell.** Inflection's raw Orion files come from EC2 instance `i-083ad9ae297f88e9f` (`inf-bronze-runner`), which
Lambda `inf-bronze-trigger` starts daily at 11:15Z.
- When a start fails, Lambda `inf-ec2-launch-monitor` (EventBridge EC2 state change -> `lambda_handler`) is meant to
  hand the failure to `inf-ec2-retry-launch`.
- On 2026-09-29 the start failed (`Server.InternalError`). The monitor's `describe_instances` read the
  `StateTransitionReason` as EMPTY, because AWS had not populated it yet.
- In `C:/Users/AndrewBerman/Desktop/wk-irpt-p-85/infra/aws/lambda/inf-pipeline/inf-ec2-launch-monitor/lambda_function.py`,
  `NORMAL_PATTERNS` contains `''` ("empty reason"), and `if any(p in reason for p in NORMAL_PATTERNS)` matches `''`
  against every string. So the failure was "Suppressed normal shutdown" and no retry happened. The decision tree's
  rule 3 (an empty or unknown reason within 15 s of launch means ALERT) is unreachable.

**Your change.** An empty reason must never be treated as a normal shutdown:
- remove `''` from `NORMAL_PATTERNS`, so an empty reason falls through to rule 3 (the 15-second launch check) and rule
  4 (a named unknown);
- keep every explicit ALERT and NORMAL pattern and all other behaviour;
- add a unit test beside the Lambda that drives the handler with fake clients;
- change nothing else. No deploy: the served move is the issuer's, under both halves.

<criterion id="P24-2-AC1" cell_refs="IB-pr-242"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r24/p24_2_ac1_monitor_empty_reason.py" .</invocation><expect>P24-2-AC1 PASS</expect></criterion>
`P24-2-AC1` -- with fake EC2, SNS and Lambda clients, four arms:
- an empty reason 5 s after launch is handed to retry;
- an empty reason 2 h after launch is NOT suppressed as normal;
- "User initiated" 2 h after launch is suppressed;
- `Server.InternalError` is handed to retry.
Base: FAIL (both empty-reason arms are suppressed). A copy with the `''` entry removed PASSES (measured at the cut).

<expected_criteria>P24-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **No deploy, no AWS write.**
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the check.

<paths>
infra/aws/lambda/inf-pipeline/inf-ec2-launch-monitor/lambda_function.py
infra/aws/lambda/inf-pipeline/inf-ec2-launch-monitor/tests/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 23 (round 25, workstream ~P), cell `IB-pr-242`.
<owned_cells>IB-pr-242</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P24-2-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~85/IRPT_BCKEND.TO-IB-pr-242.launch-monitor-empty-reason.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P24-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, the criterion's last line, and any surprise row id (`IRPT_BCKEND-W85-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the EventBridge rule that invokes the monitor is untouched.
comp-iam: DECLARED-NOT-APPLICABLE -- code only; 0 roles touched.
comp-blast: RUN -- one Lambda's decision tree: empty-reason stops move from 'suppressed' to rule 3/4; explicit patterns unchanged.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache.
comp-adversary: RUN -- P24-2-AC1 base FAIL (arms A and B suppressed); positive control on a copy without '' PASS (A handed to retry, B no-op-unknown, C suppressed, D handed).
lane: the <paths> block IS the grant.
</preflight>
