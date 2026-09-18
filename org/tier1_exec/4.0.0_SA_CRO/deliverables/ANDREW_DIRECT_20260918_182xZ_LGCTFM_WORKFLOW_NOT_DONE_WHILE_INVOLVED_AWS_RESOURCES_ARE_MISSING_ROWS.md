# ANDREW-DIRECT 2026-09-18 ~18:2xZ -- the legacy-transform workflow is NOT DONE while involved AWS resources are missing from its rows; the workflow must be designed to create rows for them

**Received at:** the `4.0.0_SA_CRO` terminal (this seat's own session), 2026-09-18 ~18:2xZ, two messages in
succession, immediately after this seat's `/exec-sum` of RCN-0009 (the MDPF_CANON subject analysis,
committed @edcbe51fb4), whose Stage 2 card read: "Compute (the functions and servers) never appears in its rows."
**Recorded by:** `4.0.0_SA_CRO`. **Channel:** Andrew-direct, typed at this terminal.
**Verbatim, message 1:**

> If we are missing lambdas/ec2/eventbridge rules or schedules/ddb/etc, any involved aws resources, then the
> workflow process is not done.

**Verbatim, message 2:**

> that means that the workflow must be designed to create rows for these items

Typos and casing his, preserved. The phrasing IS the ruling; nothing below paraphrases it into a wider or
narrower rule.

## What it was said about (context, not adjudication)

The `/legacy-transform` workflow (`LGIC_LGCTFM`, D14): its engine `lib/opal_lgctfm.py` and the contract each
run emits. The measured facts in front of him when he said it (RCN-0009,
`org/tier1_exec/4.0.0_SA_CRO/deliverables/LGCTFM_SUBJECT_ANALYSIS_MDPF_CANON_AS_FIRST_LEGACY_TRANSFORM_20260918.md`
@edcbe51fb4, s.2.5):

- The 49 Financial graded run (`workflows/legacy_transform/blackdiamond-49financial/20260918T011619Z-8db9eb1/`):
  184 rows, LAMBDA 0, EC2_INSTANCE 0, DYNAMODB_TABLE 0; EVENT_RULE 21 of 144 census'd, SCHEDULE 1 of 23; the
  rendered flow's COMPUTE section reads "(none)".
- This seat's read-only `mdpf` run (scratchpad, run-id 20260918T174353Z-685dc7e): 14 real rows against 60 live
  nodes carrying the `mdpf` token (comp-find --corpus aws, 2590 nodes scanned) -- 0 of 6 LAMBDA, 0 of 1
  EC2_INSTANCE, 0 of 13 IAM_ROLE, 0 of 11 IAM_POLICY, 1 of 1 EVENT_RULE, 4 of 6 SCHEDULE.
- Cause as measured: the walk is bucket-seeded (`--seed <bucket-or-prefix>`); a resource whose name, ARN or
  props do not carry a seed bucket is not a row. The method note names the trigger half of this hole itself
  (`infra/logic/10_LEGACY_TRANSFORM.md`, "Coverage hole").

## What it binds, read exactly as narrow as the words

1. DONE for the workflow is conditioned on COVERAGE of involved AWS resources: Lambdas, EC2, EventBridge rules,
   Scheduler schedules, DynamoDB, "etc, any involved aws resources". A run that omits an involved resource is
   not a done workflow.
2. The remedy he names is DESIGN: the workflow must be designed to CREATE ROWS for those items -- not a
   caveat, not a coverage note beside the run.

## What it does NOT decide (and this seat does not decide either)

- Which carrier executes it: an addendum outcome on `LGIC_LGCTFM` (whose register reads rounds 1-2 CLOSED,
  REALIZED 8 of 10), a defect against an existing outcome, or a cell in the migration projects' own MAP step.
  That is `1.0.0_SA_CTO`'s at L2/L4. This record SURFACES; it does not adjudicate scope (org/XXX.md: "The
  receiving agent does NOT adjudicate scope").
- Whether "involved" is measured by name token, by trigger target, by IAM grant, by source text, or all of
  them -- the instrument choice is the design's, and RCN-0009's P1/P2 are proposals on it, not rulings.
- Nothing here is a gate on any seat. No approval step is created (CLAUDE.md "DO NOT MANUFACTURE FRICTION").

## Broadcast

Sent the same turn to `1.0.0_SA_CTO`, `2.0.0_SA_COO~G` (the lane holding LGIC_LGCTFM) and `0.0.0_AB_MSTR`,
with this record's commit hash and its push state as measured at send time. `2.0.0_SA_COO` base is not
live on the roster at this time; the lane that holds the project is addressed instead of a base with no
session ("Queued if not live is a WISH").

**Author:** 4.0.0_SA_CRO (Chief Research Officer) . **Home:** org/tier1_exec/4.0.0_SA_CRO/
