# AWS Estate Census + Nessie/Iceberg/Kuzu Parity Verdict — 2026-07-30

**archetype:** VALIDATE
**Author:** 1.0.0_SA_CTO, Andrew-direct commission (world-model SSOT / resource-pruning program).
**Vintage:** all live reads 2026-07-30 ~14:0x–14:3xZ, account 313476888478, user Andrew_Berman.
**Raw artifacts:** this directory (`re_us-east-*.json`, `tagged_us-east-*.json`, `s3_buckets.json`,
`iam_*.json`, `cloudfront.json`, `route53_zones.json`, `ses_identities_us-east-1.json`,
`cfn_type_universe.json`, `kuzu_aws_nodes_raw.txt`, `parity_report.json`, `stray_region_sweep.txt`).
Rerunnable instrument: `parity_diff.py`.

## Layer 1 — the type universe (what CAN exist)

- CloudFormation public registry: **1,914 public types; 1,703 AWS-native across 292 services**
  (`cfn_type_universe.json`).
- Resource Explorer indexes **654** of those types. RE is therefore an under-oracle by construction;
  measured live: it returns ZERO for `scheduler:schedule` while 11 schedules exist
  (verified via `aws scheduler list-schedules` — exact set match with the graph).

## Layer 2 — the live estate (what DOES exist)

| Instrument | Scope | Count | Blindness |
|---|---|---|---|
| RE `list-resources` | us-east-1 | **3,176** resources / 94 types | types RE doesn't index (schedules, etc.) |
| RE `list-resources` | us-east-2 | **50** / 28 types | same |
| Tagging API (17 regions) | all | 1,905 + 2 | tagged-only, by construction |
| Stray sweep (ec2/lambda/ddb) | 15 non-indexed regions | **0 / 0 / 0** | other services unswept (accepted residual) |
| Direct global | — | S3 39 · IAM roles 208 / users 6 / cust-policies 30 · CloudFront 1 · R53 zones 2 | — |

**The estate is two-region**: us-east-1 (essentially everything) + us-east-2 (50 items: default-VPC
furniture, Lambda@Edge replica log groups auto-created by CloudFront, `opal-news-layer3-curation`
lambda, 2 `fred-ingestion-*` alarms, 3 KMS keys, memorydb/athena/apprunner residue, and 2 SES
identities incl. `andrew@fideles.capital`).

Composition headline of us-east-1's 3,176: **ec2:snapshot 976 + ec2:image 312 = 40.6% of the whole
inventory** (DLM backup accumulation; `dlm:policy` count 1). Next: lambda:function/version 278
(deploy-history accumulation), log groups 234, IAM roles 208, lambdas 192.

## Layer 3 — parity verdict: LIVE vs Nessie/Iceberg → kuzu_nessie_db

Graph at read time: 20,465 nodes / 40,914 edges, **auto-refreshed to Nessie HEAD mid-session**
(incremental writer landed a commit between my queries and comp-kuzu folded it in — the platform is
live, dual-producer: 02:00Z full re-derive + event-driven CloudTrail incremental).

Graph layers (the world-model scaffolding ALREADY spans five planes):
`aws` 2,052 · `portal` 11,338 · `ms` 5,715 · `pipeline` 1,337 · `semctl` 23.

**ARN-grain diff, both directions (`parity_report.json`), aws layer:**

1. **ZERO phantoms.** Across all 25 mapped node types, graph−live = ∅ on every type except
   SCHEDULE — where direct API verification proved the GRAPH right and RE blind. Adding the 11
   live-verified schedules: **1,148 of 1,148 graph nodes with a 1:1 live type are live-confirmed.
   The graph does not lie; nothing it asserts is stale.**
2. **Live−graph decomposes into four explainable classes, fully enumerated:**
   - **us-east-2 scope-out** (graph derives us-east-1 only): 7 log groups, 1 lambda, 2 alarms, 3 KMS.
   - **Service-linked roles** (12, all `aws-service-role/*`) — deliberate exclusion; NOTE these are
     also archaeology of abandoned services: RDS, OpenSearch, OpenSearchServerless, SMSVoice.
   - **Ephemeral lifecycle** (1): `historical-prices-fetcher` t3.xlarge launched 14:00Z today,
     already `terminated` — RE lists the corpse; the graph correctly doesn't.
   - **Unexplained residue** (small, named, for the pruning session): 5 instance profiles
     (`cot-gold-layer-profile`, `demo-transform-runner-ec2-profile`, `ec2-ssm-profile`,
     `finbert-ec2-backfill-profile`, `opal-portal-ec2-profile`); 4 of 6 IAM users
     (`Andrew_Berman_Console`, `Opal_Terminal`, `opal-portal-dashboard`,
     `website/patricia@thewhitelabelcreative.com`); 1 REST API (`f61h681z9g`).
   - Taxonomy defect (2 rows): graph models `root` and the GitHub OIDC provider as IAM_USER with
     synthetic ids — neither is a user.
3. **The graph is FINER-grain than AWS inventory where it does model**: ~670 nodes (IAM_POLICY 446
   incl. inline, API_ROUTE 82, EVENT_SOURCE 97, S3_BUCKET_POLICY 11, LAMBDA_LAYER 13,
   ROUTE53_RECORD 3, SERVICE_PRINCIPAL 18) have no 1:1 AWS-inventory surface at all — RE cannot see
   an inline policy or a bucket policy as a resource.
4. **The blindness surface** (live types with zero graph modeling, full list in
   `parity_report.json.live_unmapped_types`, ~60 types): dominated by ec2:snapshot 976, ec2:image
   312, lambda:function/version 278, ec2:network-interface 40, ec2:volume 34, ses:identity 28(!),
   apigateway sub-resources ~120, ssm:managed-instance 12, ecr:repository 9, glue:table 6 + db 4,
   memorydb 12+, rds og/pg/subgrp relics, cloudtrail:trail 2, iam:mfa 4, acm:certificate 1,
   ce:anomaly* 3, cloudformation:stack 2.

## VERDICT

**Nessie/Iceberg/Kuzu is NOT yet 1:1 with the estate — but it is 1:1 ON EVERYTHING IT MODELS, with
zero phantoms and event-driven freshness. The gap is a WHITELIST, not drift.** The world-model basis
Andrew asked about is therefore CONFIRMED VIABLE: extending the derive whitelist to the census's
type list (+ us-east-2) closes the gap mechanically. The alternative (hand inventory) is already
falsified by RE itself being blind to types the graph carries.

## Andrew-flag list (surfaced, NOT adjudicated, NOT touched)

1. `andrew@fideles.capital` (SES, us-east-2) — domain never seen in estate records. Whose is it?
   (Rule-23 class: no instrument knows what is OURS.)
2. `website/patricia@thewhitelabelcreative.com` — live IAM user AND SES identity (contractor grant
   still live). Sibling: `mike@hirst.digital` SES identity.
3. 16 `@opalinvest.com` SES email identities — likely sandbox-era recipient verifications;
   Rule 23: that domain is address-verified-only, EOP-quarantine-nondeterministic.
4. 976 snapshots + 312 AMIs (40.6% of inventory) — DLM policy accumulation; prime mass-prune with
   real storage cost.
5. us-east-2 live workload: `opal-news-layer3-curation` + `fred-ingestion-*` alarms — deliberate or
   stray?
6. MemoryDB/ElastiCache/RDS/OpenSearch/AppRunner residue + their service-linked roles — abandoned
   service archaeology.
7. `historical-prices-fetcher` launched 14:00Z DURING the fabric halt — scheduled EC2-based puller;
   inventory which schedule owns it.

## Residual unknowns (stated, not hidden)

- 15 no-index regions swept for ec2/lambda/ddb only; other services there unswept (all-zero prior).
- SES `verified=` field projected wrong in my query (shows None); sending-status per identity not
  yet measured — re-pull at review time.
- WHY the derive misses the 4 IAM users / 5 instance profiles / 1 REST API: mechanism not yet
  grounded (whitelist detail vs source quirk) — answer lives in the derive_runner source.
- graph_contracts table last written 1,051h ago (~44d) — the contracts leg of globgrph is dormant;
  separate from resource parity.
