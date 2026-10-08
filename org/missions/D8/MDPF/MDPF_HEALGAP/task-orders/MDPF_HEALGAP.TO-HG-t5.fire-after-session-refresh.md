# TO MDPF_HEALGAP.TO-HG-t5 -- round 2 HG-t-5: the morning pull fires after the login refresh it depends on, summer and winter
<to_id>MDPF_HEALGAP.TO-HG-t5</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~4</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-5` (`decompositions/MDPF_HEALGAP_DECOMP.md`, ROUND 2) |
**outcome_ref:** FWD-5 | **depends_on:** HG-t-4

---

## WORKER FACE

### THE CELL

`HG-t-5`. FWD-5: the morning pull is scheduled after the daily login refresh it depends on, with room to spare in summer and winter time.
A mitigation that makes FWD-1 rarer, never a replacement for it. **Depends on `HG-t-4`** (same file; do it after t-4 is committed).

**The estate, read at the base.** `infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf:168-173`: `aws_cloudwatch_event_rule.cot_rebalancer_runner_daily`, `schedule_expression =
"cron(0 6 * * ? *)" # PLACEHOLDER 06:00Z ...`. The session refresh: EventBridge Scheduler `cot-bd-session-daily-et` = `cron(30 7 * * ? *)`
in America/New_York (11:30Z summer, 12:30Z winter); its sentinel lands 1.5-4.3 min after the fire (10-01..10-08). The 13:30Z gold floor
run reads silver at 13:30Z. C-SESSION: you never change the session's time; the floor margin is re-derived FIRST.

**Build:**
1. Re-derive the margin: run `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R2_CHECKS/hg_t5_schedule.py` with a candidate in a scratch copy (or reason it out) and record in your report
   the after-session and before-floor minutes for a summer and a winter date. 12:45Z is the issuer's proposal (75/15 min after the
   session fire, 45 min before the floor); choose another UTC time only if it passes the check with more room and say why.
2. Change ONLY that rule's `schedule_expression`, and replace the PLACEHOLDER comment with the derivation (session time in both seasons,
   sentinel spread, floor, chosen time, this order).

### ACCEPTANCE

<criterion id="HG2-t5-AC1" cell_refs="HG-t-5"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R2_CHECKS/hg_t5_schedule.py</invocation><expect>SCHEDULE-OK</expect></criterion>
`HG2-t5-AC1` -- the daily rule fires >= 10 min after the session refresh and >= 30 min before the 13:30Z floor on a summer and a winter date.

<criterion id="HG2-t5-AC2" cell_refs="HG-t-5"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R2_CHECKS/hg_tf_fmt.py infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf</invocation><expect>FMT-OK</expect></criterion>
`HG2-t5-AC2` -- the edited file is `terraform fmt` clean.

<expected_criteria>HG2-t5-AC1 HG2-t5-AC2</expected_criteria>

Run each invocation from the worktree root. AC1 FAILS at the base: `SCHEDULE-BAD ... pull only -330 min after session ...`. AC1 reads AWS (`scheduler:GetSchedule`) read-only.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Lambda invoke, no vendor call, no `terraform init`/`plan`/`apply`, no `safe-apply`.** Every deploy and apply is the
  issuer's, at the drain. Read-only AWS reads are allowed where a criterion names them.
- **Restore mechanisms (CTO round-1 analysis 2.2):** you arm no timer, background task or OS task. If you ever arm one, name it in your
  report with its state at your close.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_HEALGAP-W4-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation
  file below, and do not weaken a check. Rows are APPEND-ONLY: never edit an existing row.

<paths>
infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 2, the enrichment), cell `HG-t-5`.
<owned_cells>HG-t-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG2-t5-AC1, HG2-t5-AC2. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~4/MDPF_HEALGAP.TO-HG-t5.fire-after-session-refresh.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG2-t5-AC1 HG2-t5-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 (decomposition ROUND 2: the rule and the session schedule read live; sentinel spread 10-01..10-08).
comp-iam: DECLARED-NOT-APPLICABLE one schedule expression; no grant.
comp-adversary: DECLARED-NOT-APPLICABLE the lens is the margin check itself (summer and winter, floor room), run in AC1.
risk: WORLD -- a schedule change; the apply is the issuer's at the drain under its own never-widen pair (C-SESSION; D1-S1).
direct_act: false -- the class is WORLD.
</preflight>

Source: PRD v0.2 ENDPOINT FWD-5; CTO round-1 analysis @475c742f71 section 3; decomposition round 2.
