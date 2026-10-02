# ETFS_RIVALS -- round 6 L8/L9 adjudication, part A (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-02 ~18:45Z. Round 6 is drained: 59 of 59 orders are terminal (52 complete, 7 superseded) at
CLOUD 0f96844ea9. This seat's suite run reads 527 passed, 0 failed. No drain-end packet had arrived at this compile; the
rows are read from CLOUD.

**Scope:** the 6 rows surfaced in round 6 (the channel reads 139, against 133 compiled through round 5). This document carries
no `<sweep_watermark>`: no new remediation row is written here, so it is not the slug.

**Disposition:**
- 5 rows are dismissed by C-S21 and C-S22 below.
- **W1-S42 stays UNDER_INVESTIGATION as the round-6 apply's precondition.**
  - The secret `rivalfunds/openai-api-key`, which the daily Lambda's generated environment names
    (RIVALFUNDS_AI_ENABLE=1), does NOT exist: `secretsmanager describe-secret` returns ResourceNotFoundException at ~18:40Z.
  - Positive control: `opal/openai/news-trending` resolves.
  - The failure is contained: `publish_page.py:645-649` records the AI stage as FAILED and still publishes. But the first
    scheduled page would then carry no accounts, which is RIV-ap-1's whole outcome and its J1.
  - It is resolved when the secret exists and is read before the apply. It graduates in part B if the apply runs without it.

**Judgment criteria still owed at L9 (graded on the served page after the round-6 apply and republish):** the J1 of RIV-ui-2,
ui-3, ui-4, ui-5, r-6 and ap-1. ap-1's J1 needs a scheduled AI run. "No FWD is a wait": a deliberate ad-hoc fire of the
scheduled path (the daily Lambda for the page day) exercises it without waiting for the 2026-10-05 morning.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S21",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-02T18:45:00Z",
    "one_line": "Four round-6 rows are closed at CLOUD 0f96844ea9: W1-S41 (lambdas.tf now carries the daily Lambda's environment block), W1-S44 and W3-S20 (both red suites; the package suite reads 527 passed, 0 failed), and W3-S21 (W3-S20's resolving row).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W1-S41",
      "ETFS_RIVALS-Z-W1-S44",
      "ETFS_RIVALS-Z-W3-S20",
      "ETFS_RIVALS-Z-W3-S21"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W1-S41: infra/aws/terraform/etfs-rivalfunds/lambdas.tf:61-65 at HEAD holds `dynamic \"environment\" { for_each = length(each.value.environment) > 0 ? [each.value.environment] : [] ... }` (issuer hookup @651d3bfda7). generated.auto.tfvars.json gives an environment to etfs-rivalfunds-daily-lambda only (RIVALFUNDS_AI_ENABLE=1, RIVALFUNDS_OPENAI_SECRET=rivalfunds/openai-api-key). W1-S44 and W3-S20/S21: this seat's `python -m pytest rivalfunds/tests -q` at CLOUD 0f96844ea9 reads 527 passed, 2 skipped, 0 failed. The test_s4 pins and the rg4 literal are repaired, and W3-S20's ARMED hazard (a red suite at the drain) no longer stands.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W1-S41, W1-S44, W3-S20, W3-S21",
        "infra/aws/terraform/etfs-rivalfunds/lambdas.tf:61-65 and generated.auto.tfvars.json at CLOUD 0f96844ea9",
        "this seat's suite run at CLOUD 0f96844ea9: 527 passed, 2 skipped"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Repaired at the drain. The environment block is code only; it reaches the Lambda at the round-6 apply, and W1-S42 below is that apply's precondition."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S22",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-02T18:45:00Z",
    "one_line": "W1-S43 (the daily role gains s3:PutObject on gold/research_hypotheses/* so the scheduled AI stage can write accounts) is the round-6 apply's IAM widening on a served prefix; it is dismissed on the condition that the apply's never-widen halves name it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W1-S43"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "policies/etfs-rivalfunds-daily-lambda.json at HEAD: Sid PutGetOwnPrefixes lists arn:aws:s3:::opal-data-etfs/rivalfunds/etfs/gold/research_hypotheses/* with s3:PutObject and s3:GetObject. Sid GetOpenAISecret grants secretsmanager:GetSecretValue on one ARN (rivalfunds/openai-api-key-??????). No DeleteObject is granted, and the publish-page role keeps read-only. It is not applied: the round-6 apply has not run.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ETFS_RIVALS-Z-W1-S43",
        "infra/aws/terraform/etfs-rivalfunds/policies/etfs-rivalfunds-daily-lambda.json at CLOUD 0f96844ea9 (PutGetOwnPrefixes, GetOpenAISecret)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A deliberate, minimal grant (one prefix, one role, Put without Delete). The round-6 apply's COO and CTO never-widen halves must name it as the blast radius on the served prefix gold/research_hypotheses/, with the rollback (remove the Put; written objects are append-only run ids). This seat reads the applied grant by simulate-principal-policy at that apply's grade."
  }
]
```

-- 3.0.0_SA_CVO~RV
