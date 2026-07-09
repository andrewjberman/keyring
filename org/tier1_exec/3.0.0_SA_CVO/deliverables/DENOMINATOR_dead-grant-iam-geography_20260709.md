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

## REFINEMENT 1 -- dual-grant (COO's "sharp one"): 9 -> 8 truly-dead

The dual-grant check is pure-IAM (my axis), computed from the same authorization-details: a us-east-2
grant is a FALSE POSITIVE if the same role ALSO holds a us-east-1 (or region-wildcard) grant to the same
secret -- the us-east-2 one is then inert and the read succeeds. Result:

- **8 TRULY-DEAD roles** (us-east-2 grant, NO us-east-1/wildcard for that secret): FredIngestionLambdaRole,
  market-update-lambda-role, news-ingestion-lambda-role, opal-layer3-ec2-role, opal-smartx-lambda-role,
  schwab-anonymizer-lambda-role, workspace-sync-lambda-role, yang-pipeline-lambda-role.
- **1 DUAL-INERT (dropped): `opal-portal-lambda-role`** -- its us-east-2 grants to `opal/external-apis` +
  `opal/smartx/config` are inert; it holds us-east-1 grants to both. NOT a break.

The sharpened triage list is **8**, not 9. (Stem-matching is heuristic; opal-portal is the clearest case
-- explicit us-east-1 grants to the identical two stems.)

## REFINEMENT 2 -- second axis (CTO 130155Z): us-east-1 grant to a missing secret = 0 (verified)

CTO named the completeness edge: the us-east-2 axis is one mechanism; a us-east-1 grant to a secret ABSENT
in us-east-1 is a dead grant OUTSIDE the 9. Enumerated every us-east-1 specific-name secretsmanager grant
against the live 78-name inventory. **3 candidates surfaced, ALL verified FALSE POSITIVES** (a trailing-slash
bug in my matcher): `find-insure/{bright-data,job-board,lusha-ai}/*` all match real secrets
(bright-data/api-key, 9x job-board/*, lusha-ai/api-key). CTO's seed `orion/eclipse_jwt/current` **EXISTS**
in us-east-1 -> not dead. **Second-axis dead grants: 0.** (Caught my own instrument's false positives before
asserting -- no raw-as-finding.) So the complete A-axis dead-grant universe = **8** (us-east-2) + **0**
(us-east-1-missing) = **8 truly-dead roles**.

## ROUTE

Complete A-axis denominator = **8 truly-dead roles** -> 0.5.0 intersects with comp-deadgrant (B-axis:
reads-it + fail-silent) -> the confirmed live/latent-degrade set -> CTO SEV-triage -> Andrew CLASS-brief on
the reconciled universe. The count is the reconciled intersection, NOT the 8 and NOT the stumbled-on 3.
Two-directionally-proven universe (pure-IAM denominator + code-side detector), the same rigor that closed
the credential universe from both READ-sweep and WRITE-simulate. I verify 0.5.0's v3 rows against the
artifact before they reach triage.
