# TO MDPF_HEALGAP.TO-HG-t2 -- round 1 HG-t-2: the Rebalancer runner re-runs after the Cottonwood login chain succeeds

<to_id>MDPF_HEALGAP.TO-HG-t2</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~2</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-2` (`decompositions/MDPF_HEALGAP_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-2`. FWD-1: on a day the 06:00Z Cottonwood Rebalancer pull fails because the vendor login lapsed, the day's three bronze feeds still land
the same day with nobody acting. This cell declares the second attempt: the runner is invoked again once the login chain has proven a working
login that day. A sibling cell makes the runner skip a day that is already complete, so on a normal day the second attempt is a no-op.

**The estate, read at the base.**
- The runner: `infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf` -- `module "cot_rebalancer_runner"` (function `cot-rebalancer-runner`,
  outputs `function_arn` and `function_name`), its daily rule `aws_cloudwatch_event_rule.cot_rebalancer_runner_daily` with target input
  `jsonencode({ mode = "pull" })`, and `aws_lambda_permission.cot_rebalancer_runner_daily` (principal `events.amazonaws.com`, `source_arn` the
  rule's ARN). Copy that file's style.
- The login chain's last step: rule `cot-bronze-complete`, declared in ANOTHER root (`infra/aws/terraform/cot-pipeline/eventbridge.tf:172-206`,
  owner `0.6.2_AE_PartnerETL`; READ, never edit). Live 2026-10-07: ENABLED, pattern source `aws.s3`, detail-type `Object Created`, bucket
  `opal-data-cot`, key suffix `_BRONZE_COMPLETE.json`. It fires once a day at about 11:32Z on the same UTC date as the 06:00Z pull, after either
  leg of the session chain, and today has one target (`CotSilverOnBronzeComplete`).
- A target can be attached to a rule by NAME from any root; the opal-assets root does not declare the rule, so the permission's `source_arn` is
  built as `arn:aws:events:<region>:<account>:rule/cot-bronze-complete` (use the root's existing caller-identity / region data sources if it
  has them, else declare them in your file).

**Build:** NEW file `infra/aws/terraform/opal-assets/cot_rebalancer_reattempt.tf`, with a header comment in the house style saying what it is
(MDPF_HEALGAP FWD-1 hop 3; a step of the existing chain, no new schedule or rule; the runner's guard makes it a no-op on a complete day):
1. `aws_cloudwatch_event_target` with `rule = "cot-bronze-complete"`, a `target_id`, `arn = module.cot_rebalancer_runner.function_arn`, and
   `input = jsonencode({ mode = "pull" })`. No `date` in the input: the runner defaults to today UTC, which is the morning pull's date.
2. `aws_lambda_permission` with `function_name = module.cot_rebalancer_runner.function_name`, `principal = "events.amazonaws.com"`, a
   `statement_id` distinct from `AllowEventBridgeInvokeDaily`, and `source_arn` ending `rule/cot-bronze-complete`.
3. `terraform fmt` the file.

### ACCEPTANCE

<criterion id="HG1-t2-AC1" cell_refs="HG-t-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R1_CHECKS/hg_t2_tf_check.py</invocation><expect>TF-OK</expect></criterion>
`HG1-t2-AC1` -- the file declares exactly one target on `cot-bronze-complete` invoking the runner with `mode = "pull"` and exactly one permission scoped to that rule, and is fmt-clean.

<criterion id="HG1-t2-AC2" cell_refs="HG-t-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R1_CHECKS/hg_t2_seam.py</invocation><expect>SEAM-OK</expect></criterion>
`HG1-t2-AC2` -- the seam with the real neighbour: the rule your file names is live and ENABLED, and its live pattern matches the newest real sentinel and refuses a non-sentinel key.

<expected_criteria>HG1-t2-AC1 HG1-t2-AC2</expected_criteria>

Run each invocation from the worktree root. Both FAIL at the base (2026-10-07): `TF-BAD no file ...` and `SEAM-BAD no file ...`. AC2 reads
AWS read-only (`events:DescribeRule`, `s3:ListBucket` on `opal-data-cot`) with the box's credentials.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No `terraform init`, `plan` or `apply`, no `safe-apply`, no AWS write, no Lambda invoke.** The apply is the issuer's, at the drain.
- Do not edit `cot_rebalancer_runner.tf` or anything under `infra/aws/terraform/cot-pipeline/`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_HEALGAP-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) in the investigation file below, and do not weaken a check.

<paths>
infra/aws/terraform/opal-assets/cot_rebalancer_reattempt.tf
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 1, the thread), cell `HG-t-2`.
<owned_cells>HG-t-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG1-t2-AC1, HG1-t2-AC2. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~2/MDPF_HEALGAP.TO-HG-t2.reattempt-on-bronze-complete.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG1-t2-AC1 HG1-t2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the file, both checks' output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; an event target on an existing rule, no new schedule.
comp-iam: RUN at L5 (comp-iam service cot-rebalancer-runner, 2026-10-07); the new aws_lambda_permission is a resource policy on the runner, not a role grant; no role changes.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
risk: WORLD -- the L6 floor for an infrastructure path (a Terraform file). The worker writes the file, never applies it; the apply is the issuer's WORLD act at the drain, held on PRD ACT 1 (standing vendor word) with a never-widen half and a change-management entry.
direct_act: false -- the class is WORLD, so the direct-act path does not apply.
</preflight>

Source: PRD v0.1 @78db344481 section 2 (THREAD hop 3), C-ONE-PIPELINE, C-SESSION; decomposition round 1.
