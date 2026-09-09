# TO ETFS_GUARDRAIL.TO-EG-s-18 -- THE SCHEDULES' FIRING FROM HISTORY: the executions of `etfs-reports-monthly-run` and the two daily rules listed with their initiators and denominators -- the ones that produced the published August artifact and the daily slices

<to_id>ETFS_GUARDRAIL.TO-EG-s-18</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~3</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-09</issued_date>
<status>pending -- issued in round 2's ONE issuance on PRD v0.4 @`a830ea1cc0` (the manual-trigger addendum on Andrew's ~21:4xZ word), s.9 row S18; decomposition v0.2 s.8-s.11. Slot ~3, independent; runs now; read-only.</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.4 (s.9 row S18) | **Decomp cell:** `EG-s-18` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.2, s.8-s.11) | **outcome_ref:** the schedules (rule (4) for FWD-1 and FWD-5) | **verb:** verify | **depends_on:** none

---

## THE CELL

`EG-s-18` (PRD s.9 S18): the published August CSV and the daily slices EXIST, so the schedules have fired -- but the fires were never LISTED as evidence, and rule (4) of the manual-trigger rule wants the schedule's own firing proven from HISTORY with a denominator, never by waiting. This order lists them: the monthly schedule `etfs-reports-monthly-run` (EventBridge Scheduler, `cron(0 10 1 * ? *)` America/New_York, target the orchestrator Lambda) and the two daily rules that fire `cot-etf-ownership-daily` and the served-writer `bd-49f` twin. 10-01 and the daily crons stay CONFIRMATION.

## DELIVERABLE

`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~3/test_egs18_schedules_from_history.py` (the battery) and `the-schedules-from-history.result.md` (the three history tables with denominators and initiators; the configuration read of each schedule; the artifact-to-fire matches), plus the proof-of-spec instance (below).

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry** -- your own `deliverables/<serial>/` folder and THIS ORDER'S OWN FILE for the `<status>` flip. A path you need that it does not name is a BLOCKING row, never an override.
- **READ-ONLY on the plane.** No invoke, no write, no deploy.
- **YOUR AWS IDENTITY IS THE LAUNCHING SEAT'S** (decomposition s.3 decision 1); outputs recorded VERBATIM.
- **CloudTrail's `--start-time` is INCLUSIVE at the second and `lookup-events` PAGINATES**: paginate fully and count client-side; a window opening AT an event's own timestamp contains it -- print the window you used. `aws s3 ls` renders LOCAL time; use `s3api` for UTC.
- **EVERY invocation is bounded.** `timeout 120` per call.
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W3-S<k>`.
- **NEVER `git push`.** Report push state as MEASURED.

## ACCEPTANCE

<criterion id="S18-AC1" cell_refs="EG-s-18"><invocation>timeout 600 python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~3/test_egs18_schedules_from_history.py</invocation><expect>EGS18-SCHEDULES-FIRED-FROM-HISTORY</expect></criterion>
`S18-AC1` -- a battery you write, printing the token ONLY when every arm holds: (a) THE CONFIGURATION READ of each schedule LIVE: `aws scheduler get-schedule --name etfs-reports-monthly-run` (state, expression, timezone, target ARN, next fire in UTC) and the two daily rules (`aws events describe-rule` + `list-targets-by-rule`, or `scheduler get-schedule` if they are Scheduler schedules -- name which; state, expression, target ARN, input); (b) THE MONTHLY HISTORY: CloudTrail `Invoke` events on the orchestrator function over the last 90 days (paginated, denominator printed) with the invoking identity per event -- the rows whose identity is `etfs-reports-scheduler-role` are the rule-initiated fires; the one that produced the published August artifact matched by time to that object's `LastModified` (UTC, `s3api head-object` on the publish keys under `platinum/reports/2026-08/`, BEFORE any re-render this round writes -- read the archive if EG-s-14 has already run, and say which you read); (c) THE DAILY HISTORY: CloudTrail `Invoke` events on each of the two producers over the last 30 days with the initiator per event -- the rule-initiated rows counted, listed by date, beside the daily slices they produced (`daily/<partner>/<date>.json` LastModified within minutes of each fire; the matched pairs counted, denominator = fires); (d) THE NEGATIVE CONTROL: every event whose initiator is a PERSON or another role (this round's manual invokes among them, if already fired) listed separately -- the two populations must differ on the initiator column, or the discriminator is decoration; (e) the table for each schedule printed as `fires N of events M, initiator = <role>`, and the next scheduled fire time in UTC recorded as CONFIRMATION, never as a gate.

<criterion id="S18-AC2" cell_refs="EG-s-18" judgment="true"/>
`S18-AC2` -- graded by the CVO at L9: whether the fires are regular (gaps named), whether every published artifact and every daily slice maps to a rule-initiated fire or to a person (the unmatched ones named), and what CloudTrail's 90-day window cannot show. Evidence with vintage. NO VERDICT.

<expected_criteria>S18-AC1, S18-AC2</expected_criteria>

<paths>
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~3/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>
No code path and no ledger path is granted: this order reads and records. `infra/aws/terraform/etfs-reports/orchestrator.tf` and the two producers' Terraform are READ for the schedule names (never edited).

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.2, cell `EG-s-18`.
<owned_cells>EG-s-18</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at this issuance, 2026-09-09 ~22:2xZ -- WITHIN BUDGET, scanned 5 of 5 carriers, 56.25 s of a 90 s default. GATES ARMED: 25. REACHED-DENOMINATORS C1=23, C2=6, C3=12, C4=20, C5=335. ZERO of the 25 armed gates names ETFS_GUARDRAIL or its schedules. BLIND SPOT: none that bears -- a read-only cell; `comp-trigger` (the scheduler-forensics lens, marquis) is the natural second instrument if it covers these rules -- run it and print its answer beside CloudTrail's, or print why it does not apply.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a verify cell; the negative control is the initiator column.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S18-AC1`, `S18-AC2`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~3/ETFS_GUARDRAIL.TO-EG-s-18.the-schedules-from-history.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), validated with `python .tools/proof-of-spec-check.py <instance> S18-AC1,S18-AC2` BEFORE the complete flip, which you commit yourself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when S18-AC1 PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
