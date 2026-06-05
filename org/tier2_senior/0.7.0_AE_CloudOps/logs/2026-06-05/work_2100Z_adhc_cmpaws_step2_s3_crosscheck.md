# ADHC_CMPAWS Phase 1 Step 2 — Live-AWS S3 Cross-Check (AE 0.7.0)

**Auditor:** 0.7.0_AE_CloudOps
**Date:** 2026-06-05 ~20:42-21:00Z
**Oracle fixture:** `org/modules/graph/aws-shapes/s3-hand-audit-fixture-v1.0.yaml` (CVO, commit 7cfd37b1e)
**Method:** live `aws s3api` get-bucket-versioning / get-public-access-block / get-bucket-notification-configuration / get-bucket-policy + cloudfront list-cloud-front-origin-access-identities + events list-rules. Read-only; us-east-2 via `--region us-east-2`.

## Headline
24/24 buckets cross-checked. **Versioning + public-access-block: 24/24 EXACT match (zero drift).** 4 discrepancies found (all additive — live richer than oracle), 7 oracle gaps resolved.

## Confirmations (oracle correct)
- **Versioning + PAB, all 24 buckets:** every us-east-1 bucket matches fixture versioning_enabled + public_access_block exactly (22/22). us-east-2 resolved below.
- **opal-data-inf notifications:** 2 direct S3->Lambda (inf-portal-publisher gold/meta/*pipeline-complete.json; inf-silver-aggregator silver/_silver_complete/*.json) — MATCH. EventBridge enabled = true — MATCH (fixture eventbridge_enabled: true).
- **opal-data-portal-v2 notifications:** 2 (yang-pipeline-trigger uploads/*manifest.json; opal-security-scanner-processor security_scanner/uploads/*.xlsx) — MATCH.
- **opal-data-mdpf / opal-data-etfs:** no notifications — MATCH (fixture []).
- **bd + inf OAI principal E139998VWH0PD ("opal-scoped-advisor-oai"):** present in both bucket policies — MATCH fixture bucket_policy_expected_principals.

## Discrepancies (fixture corrections for CVO adjudication)

**D1 — opal-data-bd has a THIRD notification trigger not in the fixture (P1, GRANTS/TRIGGERS edge missing).**
Live opal-data-bd has 3 LambdaFunctionConfigurations; fixture lists 2. Missing:
  - Id `PortalPublisherTrigger` -> `bd-portal-publisher`, event s3:ObjectCreated:*, prefix `gold/pipeline-complete`, suffix `.json`.
  Fixture summary s3_trigger_edges should be **7, not 6**. Add the S3->Lambda edge opal-data-bd -[TRIGGERS]-> bd-portal-publisher.

**D2 — opal-data-portal-v2 bucket policy OAI is EU39UXW7CMSI5, NOT the fixture's guessed E139998VWH0PD (P1, GAP-1).**
Fixture line 443 guessed "likely OAI E139998VWH0PD". ACTUAL policy (2 statements):
  - Sid `AllowCloudFrontOAI`: Principal AWS `arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity EU39UXW7CMSI5` (= "OAI for opalinvest.dev S3 bucket"), Action s3:GetObject.
  - Sid `AllowCloudFrontOACPublicData`: Principal Service cloudfront.amazonaws.com, Action s3:GetObject, Condition AWS:SourceArn = distribution/EVTSA9VEHNZVH (modern OAC).
  Correct the guessed principal + add the OAC statement.

**D3 — bd + inf bucket policies each carry an OAC statement the fixture did not track (P1, GAP-2/GAP-3 GRANTS-edge completeness).**
The fixture drift-check only asserted OAI presence. Full live statement lists:
  - opal-data-bd: [Sid `AllowCloudFrontOACReadGold` = Service cloudfront.amazonaws.com + SourceArn EVTSA9VEHNZVH (OAC)] + [Sid `AllowScopedAdvisorOAI` = OAI E139998VWH0PD]. 2 statements.
  - opal-data-inf: [Sid `AllowScopedAdvisorOAI` = OAI E139998VWH0PD] + [Sid `AllowCFDistributionGold` = Service cloudfront.amazonaws.com + SourceArn EVTSA9VEHNZVH (OAC)]. 2 statements.
  Add the OAC (cloudfront service-principal + SourceArn EVTSA9VEHNZVH) GRANTS edges for both.

**D4 — GAP-7: TWO EventBridge rules match the bronze-complete pattern, fixture named one.**
Live ENABLED rules on opal-data-inf `bronze/orion-api/*/_BRONZE_COMPLETE.json` (detail-type Object Created, source aws.s3):
  - `inf-silver-chain-bronze-complete` (the one fixture named)
  - `inf-assets-trigger-bronze-complete` (NOT in fixture)
  Both via EventBridge (bucket EventBridgeConfiguration enabled), not direct S3 notification. Edge-taxonomy (S3 -[TRIGGERS via EventBridge]-> LAMBDA) is CTO-owned per GAP-7; flagging both rules for the edge set.

## Gap resolutions
- **GAP-1 (portal-v2 policy):** RESOLVED — see D2. OAI EU39UXW7CMSI5 + OAC EVTSA9VEHNZVH.
- **GAP-2 (bd policy full statements):** RESOLVED — see D3. OAC AllowCloudFrontOACReadGold + OAI E139998VWH0PD.
- **GAP-3 (inf policy full statements):** RESOLVED — see D3. OAI E139998VWH0PD + OAC AllowCFDistributionGold.
- **GAP-4 (us-east-2 schwab + market-update):** RESOLVED — BOTH versioning=Enabled, PAB=all-true (BlockPublicAcls/IgnorePublicAcls/BlockPublicPolicy/RestrictPublicBuckets all True). Fixture had null.
- **GAP-5 (terraform-state):** RESOLVED — versioning=Enabled; MFADelete=Disabled (absent from get-bucket-versioning); replication=none (ReplicationConfigurationNotFound). Bootstrap-bucket state confirmed.
- **GAP-6 (IAM_PRINCIPAL stubs):** RESOLVED (AE portion) — 2 live CF OAIs: `EU39UXW7CMSI5` (Comment "OAI for opalinvest.dev S3 bucket (us-east-1)"; CanonicalUser 7579b8...) used by portal-v2; `E139998VWH0PD` (Comment "opal-scoped-advisor-oai"; CanonicalUser d4ad9d...) used by bd+inf. Plus the OAC pattern = service principal cloudfront.amazonaws.com gated by AWS:SourceArn distribution/EVTSA9VEHNZVH. CVO adjudicates node/edge mapping.
- **GAP-7 (EventBridge edge):** see D4 — CTO edge-taxonomy call; 2 live ENABLED rules verified.

## Evidence commands (reproducible)
`aws s3api get-bucket-versioning|get-public-access-block|get-bucket-notification-configuration|get-bucket-policy --bucket <b>`; us-east-2 with `--region us-east-2`; `aws cloudfront list-cloud-front-origin-access-identities`; `aws events list-rules`.
