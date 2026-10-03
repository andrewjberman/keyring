# ETFS_RIVALS -- round 6 L8/L9 adjudication, parts A and B (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-02 ~18:45Z. Round 6 is drained: 59 of 59 orders are terminal (52 complete, 7 superseded) at
CLOUD 0f96844ea9. This seat's suite run reads 527 passed, 0 failed. No drain-end packet had arrived at this compile; the
rows are read from CLOUD.

**Scope:** the 6 rows surfaced in round 6 (the channel reads 139, against 133 compiled through round 5). This document carries
no `<sweep_watermark>`: no new remediation row is written here, so it is not the slug.

**Part B (2026-10-02 ~20:25Z, after the round-6 apply at eb6e9f04ff):**
- C-S23 closes W1-S42: the secret was created at 19:44:32Z, before the apply.
- C-S24 is a new finding of this seat, graduated in `remediations/REMEDIATION_v6.Z.md`: the scheduled path does not reach the AI stage on a normal day (RIV-ap-1's J1 is FAIL).
- The six J1 grades are in `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R6_REVIEW_20261002.md`.

**Part A, disposition:**
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
  },
  {
    "id": "ETFS_RIVALS-Z-C-S23",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-02T20:25:00Z",
    "one_line": "W1-S42 is resolved: the secret rivalfunds/openai-api-key was created at 19:44:32Z, before the round-6 apply (~19:46Z). The daily Lambda's role can read it and only it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W1-S42"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "This seat's `secretsmanager describe-secret rivalfunds/openai-api-key` reads CreatedDate 2026-10-02T15:44:32-04:00. The daily Lambda is LastModified 19:46:29Z with Environment {RIVALFUNDS_AI_ENABLE: 1, RIVALFUNDS_OPENAI_SECRET: rivalfunds/openai-api-key}. simulate-principal-policy on its role reads GetSecretValue on rivalfunds/openai-api-key-* allowed and on opal/openai/news-trending-* implicitDeny.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ETFS_RIVALS-Z-W1-S42",
        "this seat's describe-secret, get-function-configuration and simulate-principal-policy reads, 2026-10-02 ~20:05-20:10Z",
        "ledger org/critical_paths/change_management/20261002T1942Z_etfs-rivalfunds-round6_deploy_completion.md (leg S1 secret before N1 apply)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The precondition was met before the apply."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S24",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-02T20:25:00Z",
    "one_line": "RIV-ap-1's outcome is not reached on a normal day: the AI stage runs only inside publish_page in the daily Lambda, and the 09:00 ET sweep runs publish-page only when no publish-page marker exists. The marker-driven publish-page Lambda (no AI gate) has always written that marker by ~07:05 ET, so a scheduled page gets no accounts. The graded 09-30 run was a deliberate `only:[publish-page]` fire.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "Round-5 analysis s.4 item 1 and RIV-ap-1: wire the AI chain into the scheduled Lambda path, so the scheduled page carries accounts with no seat awake. RIV-ap-1 J1: the first scheduled account reads as well as a seat run's.",
    "world_is": "data/etfs/scripts/rivalfunds/sweep.py:469-472 runs publish-page only when `not mk.has_marker(\"publish-page\", date, sink)`. On 2026-10-02 the marker-driven publish (state/publish_page/date=2026-10-02/096abf8e...) landed at 11:04:10Z, and the 13:00Z sweep ran nothing (COO~RV STATUS 'Round 5 drains': ran [], the served page stayed 1002e). rivalfunds-publish-page-lambda has Environment null, so ai_stage.run_for_day returns SKIPPED_GATE there. The 09-30 run (20261002T195217Z-ai, 24/24 PASS, run_path 'scheduled' in its manifest) was invoked as `{only:[publish-page], date 2026-09-30, mode daily, batch rv-ai-0930r6}` (deploy ledger 20261002T1942Z, RequestId b6b33974, 344.1 s), which bypasses that check. Also, publish_page.py:643-651 runs the AI stage BEFORE the page is rendered and written, with no deadline: client timeout 120 s, 12 funds x 2 prompts x up to 2 attempts, against a 900 s Lambda. On the daily Lambda a slow vendor day loses that invocation's republish.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/sweep.py:469-472 and :510-528 (`only` bypass) at CLOUD 0f96844ea9",
        "data/etfs/scripts/rivalfunds/publish_page.py:643-651; ai_client.py:22 TIMEOUT_S = 120; ai_accounts.run_day loop over universe.entries() with attempts (1, 2)",
        "this seat's get-function-configuration: rivalfunds-publish-page-lambda Environment null; etfs-rivalfunds-daily-lambda gated",
        "deploy ledger 20261002T1942Z_etfs-rivalfunds-round6 (the 09-30 fire's event); CloudWatch REPORT b6b33974 Duration 343973.51 ms"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV
