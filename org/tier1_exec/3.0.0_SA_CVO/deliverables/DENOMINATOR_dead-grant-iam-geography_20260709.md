# CVO DELIVERABLE -- IAM-geography DEAD-GRANT DENOMINATOR (freshness-integrity class)

**Requested:** COO 122659Z (prove-the-universe completeness bound on the dead-grant universe).
**Axis:** pure-IAM (the A-axis), independent of 0.5.0's code-side comp-deadgrant detector (the B-axis).
**Method:** `get-account-authorization-details` (Role + LocalManagedPolicy) -- ONE paginated pass, no
per-role fan-out, no throttle, COMPLETE (180 roles, 11 local-managed policies). Enumerated by resource.
**Ground truth:** us-east-2 holds **0 secrets** (list-secrets us-east-2 = 0 both forms, confirmed 1206Z).
So ANY secretsmanager grant to a `us-east-2` resource ARN is **dead by definition** -- it can only ever
resolve AccessDenied. Date: 2026-07-09.

## THE DENOMINATOR: 9 roles with an EXPLICIT us-east-2 secretsmanager grant

| # | role | dead-region secret(s) | tonight's status |
|---|---|---|---|
| 1 | `FredIngestionLambdaRole` | FredApiKey | **NEW** (not stumbled-on) |
| 2 | `market-update-lambda-role` | openai-api-key | known (SEV2 fabricate-on-denial) |
| 3 | `news-ingestion-lambda-role` | github-token, newsapi-keys, openai-api-key | known (daily-agenda LIVE) |
| 4 | `opal-layer3-ec2-role` | openai-api-key | **NEW** |
| 5 | `opal-portal-lambda-role` | opal/external-apis, opal/smartx/config | **NEW** |
| 6 | `opal-smartx-lambda-role` | opal/smartx/config | **NEW** |
| 7 | `schwab-anonymizer-lambda-role` | schwab/anonymization-key | **NEW** |
| 8 | `workspace-sync-lambda-role` | github-token, opal/*, openai-api-key | **NEW** |
| 9 | `yang-pipeline-lambda-role` | opal/external-apis | known (empty-VIX LATENT-175d) |

**Completeness bound: 9 dead-grant roles vs 3 stumbled-on tonight = 6 NEW candidates** (Fred, layer3,
portal, smartx, schwab-anonymizer, workspace-sync). If 0.5.0's comp-deadgrant dead-reach set != these 9,
the detector missed a dead grant -- this is the bound that catches a code-side blind spot.

## HONEST CAVEATS -- this is a DENOMINATOR, NOT a live-degrade count

1. **A-axis only.** A dead grant is a LIVE degrade only when intersected with the B-axis: the consumer
   actually READS that secret AND fails silent on the AccessDenied. 9 dead grants != 9 live degrades.
2. **Dual-grant refinement REQUIRED before any row is called a break.** This sweep flags us-east-2
   grants; it does NOT check whether the same role ALSO holds a us-east-1 grant to the same secret (a
   dual grant -> the us-east-2 one is inert, the read succeeds via us-east-1). True dead-reach =
   *reads secret X AND its only grant to X is us-east-2*. Each of the 9 needs: (a) does its consumer read
   that secret? (b) is there a us-east-1 grant to the same secret? Only "reads-it + us-east-2-only" =
   live/latent degrade. **This is where the denominator meets 0.5.0's code-side detector** -- neither
   axis alone is a finding; the intersection is.
3. **Region-agnostic grants are NOT dead** (reported separately, not counted): 4 roles hold
   secretsmanager on `Resource:*` / region-wildcard (`news-dashboard-processor-role`,
   `opal-globgrph-derive-runner-task`, `opal-globgrph-incremental-updater`,
   `security-sweep-dedicated-role`) -- these match us-east-1 too, so they reach live secrets. 0
   AWS-managed secretsmanager policies attached (SecretsManagerReadWrite detachment from B1 confirmed).

## ROUTE

Denominator (A-axis) -> 0.5.0 intersects with comp-deadgrant (B-axis) + the us-east-1-dual-grant check
-> the confirmed live/latent-degrade set -> CTO SEV-triage. Two-directionally-proven universe (pure-IAM
denominator + code-side detector), the same rigor that closed the credential universe from both
READ-sweep and WRITE-simulate. I verify 0.5.0's v3 rows against the artifact before they reach triage.
