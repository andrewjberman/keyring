# AUTH_TFIMPT.001 — CloudFront Distribution Import

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-06
**Status:** COMPLETE
**Task Order:** AUTH_TFIMPT.001.ae-cloudfront-distribution-import.md

---

## Summary

Imported CloudFront distribution EVTSA9VEHNZVH (opalinvest.dev) into portal-auth
Terraform state. This was the highest-risk import in AUTH_TFIMPT -- the distribution
serves all portal traffic.

## Pre-Write Validation (Compiler Modules)

Extended `org/modules/interpret/ast_extractor.py` with HCL (.tf) and ESM (.mjs/.js)
extractors. Extended `org/modules/interpret/crossref_graph.py` with HCL cross-resource
reference patterns and ESM import patterns.

Ran full compiler validation pipeline before writing any TF:

1. **crossref_graph** -- mapped 3 cross-file edges (lambda-edge.tf -> iam.tf,
   lambdas.tf -> iam.tf, lambda-edge.tf -> auth-validator-edge source)
2. **ast_extractor** -- inventoried 40 TF resources across 7 files, 5 Lambda@Edge
   functions with path patterns + dependency signatures
3. **coverage_auditor** -- 5/5 edge functions covered in TF, 9/9 dependency checks passed

## Live Distribution Config

| Element | Count | Details |
|---------|-------|---------|
| Origins | 5 | S3-opalinvest-portal (SPA), S3-opal-data-portal-v2-json (data), S3-opal-data-bd (advisor), APIGateway-portal, APIGateway-portfolio |
| Behaviors | 14 + default | See TF file for full mapping |
| Lambda@Edge | 4 functions | auth-validator-edge:9, shared-advisor-router:8, public-data-router:4, cache-control-injector:1 |
| Cache Policies | 4 | CachingOptimized, CachingDisabled, opal-scoped-advisor-by-firm, json-tiered-5min-cache |
| Error Responses | 2 | 403->index.html, 404->index.html (SPA routing) |
| Cert | ACM | cf2d3e43-e600-4507-98ad-0208c298c26f, sni-only, TLSv1.2_2021 |

## Execution

| Step | Result |
|------|--------|
| terraform import | Success -- aws_cloudfront_distribution.portal imported |
| terraform plan | 1 change: tags + origin reorder (cosmetic TypeSet diff) |
| terraform apply | Success in 58s -- tags added |
| 0-diff verify | Perpetual origin reorder diff (known TF TypeSet behavior, no actual AWS changes) |
| record-terraform-deploy.sh | Source map updated, 7 functions recorded |

## Known Issue

The `aws_cloudfront_distribution` resource shows a perpetual plan diff where
origins appear to be removed and re-added with identical values. This is a known
behavior of the AWS TF provider -- origin blocks are TypeSet, and TF's internal
hash ordering differs between state and config on each plan. No actual changes
are applied to AWS. This is cosmetic only.

## Files Created/Modified

| File | Action |
|------|--------|
| `infra/aws/terraform/portal-auth/cloudfront-distribution.tf` | Created (new) |
| `org/modules/interpret/ast_extractor.py` | Extended: HCL + ESM extractors |
| `org/modules/interpret/crossref_graph.py` | Extended: HCL + ESM reference patterns |
| `infra/aws/lambda/ci/lambda-source-map.json` | Updated by record-terraform-deploy.sh |

## Portal-Auth TF State -- Final Inventory

| Category | Resources | Count |
|----------|-----------|-------|
| CloudFront Distribution | opalinvest.dev (EVTSA9VEHNZVH) | 1 |
| Lambda Functions | opalinvest-auth-handler, opal-portal-authorizer, + 5 edge functions | 7 |
| IAM | lambda-edge-execution-role, opalinvest-auth-lambda-role, portal-lambda (data) | 3 |
| DynamoDB | opal-firms, opal-sessions, user-permissions, opal-offices, opal-users, opal-users-v2 | 6 |
| SES | opalinvest.dev domain identity | 1 |
| Secrets Manager | jwt-private-key, jwt-public-key | 2 |
| CloudFront Cache Policy | opal-scoped-advisor-by-firm | 1 |
| Log Groups | 8 | 8 |
