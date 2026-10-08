# TO MDPF_HEALGAP.TO-HG-t4 -- round 2 HG-t-4: the runner's retry settings say what the async engine actually does
<to_id>MDPF_HEALGAP.TO-HG-t4</to_id>
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
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-4` (`decompositions/MDPF_HEALGAP_DECOMP.md`, ROUND 2) |
**outcome_ref:** FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-4`. FWD-4: someone reading only the runner's settings correctly predicts how it retries; settings that promise a window the system
cannot deliver fail.

**The estate, read at the base.** `infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf:222-239`: `aws_lambda_function_event_invoke_config.cot_rebalancer_runner` with
`maximum_retry_attempts = 2`, `maximum_event_age_in_seconds = 21600`, and a comment saying these are "the AWS defaults". Live:
`MaximumRetryAttempts 2`, `MaximumEventAgeInSeconds 21600`. AWS Lambda async, on a FUNCTION error: at most 2 retries, ~1 min then ~2 min
after the failure; the event age only bounds queue wait (throttling) and never adds attempts. So the 6-hour age is a window no failed
pull ever gets.

**Build:**
1. Set `maximum_event_age_in_seconds = 900` (covers the ~3-minute retry chain with margin, promises nothing longer). Keep
   `maximum_retry_attempts = 2`. Rewrite the comment above them to state what the engine does (attempts, spacing, what age bounds) and
   cite this order. Touch nothing else in the file.
2. NEW `infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/retry_schedule.py` with `predict(max_retry_attempts: int, max_event_age_seconds: int) -> dict` returning
   `{"attempts": <1 + retries the age allows>, "last_attempt_offset_seconds": <offset of the last attempt>}` using the documented
   60 s / 120 s spacing (an attempt whose offset exceeds the age is dropped). A short module docstring cites the AWS behaviour.

### ACCEPTANCE

<criterion id="HG2-t4-AC1" cell_refs="HG-t-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R2_CHECKS/hg_t4_settings.py</invocation><expect>SETTINGS-OK</expect></criterion>
`HG2-t4-AC1` -- from the file's settings the predictor gives 3 attempts over ~180 s, and the age covers that chain without promising more than an hour.

<criterion id="HG2-t4-AC2" cell_refs="HG-t-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R2_CHECKS/hg_tf_fmt.py infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf</invocation><expect>FMT-OK</expect></criterion>
`HG2-t4-AC2` -- the edited file is `terraform fmt` clean.

<expected_criteria>HG2-t4-AC1 HG2-t4-AC2</expected_criteria>

Run each invocation from the worktree root. AC1 FAILS at the base: `SETTINGS-BAD no predictor ... (retries=2 age=21600)`. AC2 is a regression guard (`FMT-OK` at the base).

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
infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/retry_schedule.py
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 2, the enrichment), cell `HG-t-4`.
<owned_cells>HG-t-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG2-t4-AC1, HG2-t4-AC2. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~4/MDPF_HEALGAP.TO-HG-t4.retry-settings-made-true.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG2-t4-AC1 HG2-t4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule change (t-5 is the schedule cell).
comp-iam: DECLARED-NOT-APPLICABLE a settings value and a pure-python predictor; no grant.
comp-adversary: DECLARED-NOT-APPLICABLE the change shortens a queue-age bound only; attempts and spacing are unchanged.
risk: WORLD -- an infrastructure path; the apply is the issuer's at the drain.
direct_act: false -- the class is WORLD.
</preflight>

Source: PRD v0.2 ENDPOINT FWD-4; CTO round-1 analysis @475c742f71 section 3; decomposition round 2.
