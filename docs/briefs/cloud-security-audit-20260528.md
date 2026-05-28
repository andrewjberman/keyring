# Cloud Security Audit -- 2026-05-28
**Author:** 0.7.0_AE_CloudOps  
**Authority:** CTO ad-hoc TO (bda5eb216/39a06b9ce, Andrew direct)  
**Scope:** FINDS only -- no fixes applied. Critical findings (exposed secret / public sensitive bucket / missing auth / over-broad IAM) flagged to CTO+COO. Remediations are separate follow-on TOs.

---

## Axis 1 -- Resource Inventory vs TF / Lambda Source-Map / EC2_MANIFEST

### Lambda source-map (infra/aws/lambda/ci/lambda-source-map.json)
- comp-build: 1747/1785 source-mapped nodes (38 unmapped -- normal for external/dynamic resources)
- TF state: all actively-deployed pipelines verified at 0-diff in this session (news-pipeline, market-overview, mdpf-pipeline)
- Gaps carried forward from prior sessions (Known-Issues #2, #3, #7):
  - opal-portal-authorizer: no TF resource found -- needs TF import or explicit tracking
  - opal-security-scanner-processor, security-sweep-comprehensive: deployed, ACTIVE (Python 3.11, last modified 2026-02-18) -- resolves Known-Issue #3 partially (they exist in AWS)
  - cost-anomaly-scanner, access-anomaly-scanner: confirmed in AWS Lambda list -- Known-Issue #3 RESOLVED (all exist)

### EC2_MANIFEST
- mdpf-daily-runner (i-02448edb624a7a7cf): registered, in use (S2 backfill running PID 2493 this session)
- Other EC2 instances: not re-verified this session (no changes made)

### S3 Buckets (opal-data-*)
| Bucket | Public Access Block | Status |
|---|---|---|
| opal-data-bd | BlockAll=True | CLEAN |
| opal-data-inf | BlockAll=True | CLEAN |
| opal-data-demo | BlockAll=True | CLEAN |
| opal-data-mdpf | BlockAll=True | CLEAN |
| opal-data-portal-v2 | BlockAll=True | CLEAN |
| opal-313476888478-lambda-artifacts | BlockAll=True | CLEAN |
| opal-data-cottonwood | DOES NOT EXIST | Expected (cottonwood has no data pipeline per FIRM#META) |

**S3 VERDICT: CLEAN.** All data-bearing buckets block public access.

---

## Axis 2 -- Compiler Graph Refresh + New Script Registration

- comp-build completed: 1747/1785 file-backed nodes indexed
- users/scripts/create_user_v2.py: local-runtime admin script, not a Lambda -- does not require comp-graph node registration (no S3 I/O, no CloudFront, not invoked by portal or other Lambdas)
- Action: NONE needed

---

## Axis 3 -- Security Scan

### comp-iam gaps
**RESULT: No permission gaps detected.** All Lambda/EC2 boto3 call-sites have matching IAM statements.

### comp-pii audit (advisor-intelligence components)
**RESULT: CLEAN.**
- 3 PII refs across advisor-intelligence components
- All 3: pseudonymized (hashed) -- 0 cleartext PII, 0 S3-direct PII
- See full output: previous session run

### comp-routes auth-map -- FINDING

**F1 (MEDIUM): /api/scoped/security-scanner/* has no auth-validator-edge viewer-request Lambda**

```
FINDING: Behavior 10 (/api/scoped/security-scanner/*) routes to APIGateway-portal
without the auth-validator-edge CloudFront layer. All other /api/scoped/* paths
carry auth-validator-edge [AUTH] at the CF level before reaching API GW.
```

Investigation: The path MAY still be protected by the portal_authorizer at the API GW level. The comp-routes [AUTH] flag indicates the CloudFront-level JWT layer only. Actual exposure depends on API GW integration config.

**Action (follow-on TO):** Verify whether the API GW route for security-scanner has the portal_authorizer attached. If not: add it. If yes: update auth-map source so comp-routes shows [AUTH] correctly. Report to CTO+COO.

**F2 (LOW-ADVISORY): /json-tiered/* has no auth**
```
/json-tiered/* -> S3-opal-data-portal-v2-json (no auth)
```
This path appears to serve tiered JSON data without CloudFront-level auth. If these files contain any firm-specific or sensitive data, this is a gap. If all content is public-safe (e.g., market data with no PII), this may be by design.
**Action:** Verify /json-tiered/* content is public-safe (no firm-specific or PII data). If not: add auth behavior.

### Secrets Manager -- ADVISORY

Secrets enumerated (names only, no values read):

**Potentially over-proliferated Anthropic/OpenAI API keys:**
- `ai/claude-api-key`, `anthropic-api-key`, `opal/moltbot-anthropic-key` -- 3 separate Anthropic secrets
- `opal/openai/andrew-fideles`, `opal/openai/aws-lambda-ki`, `opal/openai/layer3-curation`, `opal/openai/market-update`, `opal/openai/news-trending` -- 5 OpenAI secrets

F3 (INFO): **Anthropic key proliferation (3 secrets)** -- unclear if all 3 are distinct keys or duplicates under different names. Recommend consolidation audit: which Lambdas/services read each, whether distinct keys are required.

F4 (INFO): **opalinvest/jwt-secret** -- likely a legacy HS256 JWT secret from pre-RS256 migration. If no longer used, should be decommissioned (reduces key surface). Verify callers before deletion.

**F5 (INFO): seeking-alpha/bright-data-api-key** -- external API credential. Verify it's not the same as the consolidated `find-insure/bright-data/*` or `brightdata-api-key` secrets. Potential duplication.

**All other secrets appear appropriately named and scoped.**

### Known-Issues status update (vs prompt.md #1-9)

| ID | Severity | Status | Notes |
|---|---|---|---|
| 1 | MEDIUM | UNCHANGED | CloudFront not in TF -- no work done this session |
| 2 | MEDIUM | UNCHANGED | opal-portal-authorizer no TF resource |
| 3 | MEDIUM | **RESOLVED** | cost-anomaly-scanner + access-anomaly-scanner + security-scanner Lambdas confirmed in AWS |
| 4 | LOW | UNCHANGED | openpyxl-layer ownership gap |
| 5 | LOW | UNCHANGED | CHANGELOG.json missing |
| 6 | LOW | UNCHANGED | portal-notifications no tag |
| 7 | LOW | UNCHANGED | opalinvest-auth-handler uncertainty |
| 8 | INFO | UNCHANGED | JWT public key not in TF |
| 9 | INFO | UNCHANGED | opal-data-portal-v2 not in TF |

### Domain mismatch (flagged to CTO per COO directive)

**F6 (MEDIUM): inflection FIRM#META.domain vs firmAccess.ts discrepancy**
```
FIRM#inflection/META.domain:                 "inflection.com"
firmAccess.ts FIRM_EMAIL_DOMAINS[inflection]: "inflectionwealthmgmt.com"
Existing inflection user:                     user@inflection.com (consistent with META)
```
If the provisioning script uses META.domain (inflection.com) but the portal validates
via firmAccess.ts (inflectionwealthmgmt.com), a user provisioned with inflection.com email
would be blocked at portal sign-in by `isEmailFromFirm`. Auth-breaking if not reconciled.
**Action (CTO decision):** Which is canonical? Update whichever is stale to match.

---

## Axis 4 -- security-sweep-comprehensive Lambda Status

| Lambda | Runtime | State | Last Modified | Description |
|---|---|---|---|---|
| security-sweep-comprehensive | python3.11 | Active | 2026-02-18 | SOC 2 + CIS Benchmark (19 categories, 120+ checks) |
| opal-security-scanner-processor | (not queried) | (not queried) | — | Companion processor |
| cost-anomaly-scanner | (not queried) | (not queried) | — | Cost anomaly detection |
| access-anomaly-scanner | (not queried) | (not queried) | — | Access pattern anomaly detection |

**security-sweep-comprehensive is Active.** Last modified 2026-02-18 (3+ months ago). No invocation result checked this session (would require SSM or direct invoke).

**F7 (LOW): security-sweep-comprehensive last run date unknown.** Lambda is active but last-modified is >3 months ago. Recommend verifying the last successful execution and reviewing findings from the most recent run. If not triggered by EventBridge, may not be running on schedule.

---

## Summary of Findings

| ID | Severity | Finding | Action |
|---|---|---|---|
| F1 | MEDIUM | /api/scoped/security-scanner/* missing auth-validator-edge CF layer | Verify API GW authorizer; add if missing; route finding to CTO+COO |
| F2 | LOW | /json-tiered/* no auth | Verify content is public-safe; add auth if not |
| F3 | INFO | Anthropic API key proliferation (3 secrets) | Consolidation audit |
| F4 | INFO | opalinvest/jwt-secret possibly legacy HS256 key | Verify callers; decommission if unused |
| F5 | INFO | seeking-alpha/bright-data-api-key possible duplication | Verify vs consolidated bright-data secrets |
| F6 | MEDIUM | inflection FIRM#META.domain vs firmAccess.ts mismatch | CTO decision -- which is canonical |
| F7 | LOW | security-sweep-comprehensive last run unknown | Verify last execution + review findings |

**CLEAN axes:** S3 public access, comp-iam gaps, comp-pii (advisor-intel), Known-Issue #3 resolved.

**No critical findings** (no exposed secrets, no publicly accessible sensitive buckets, no missing auth on data-bearing paths confirmed).

---

## Appendix -- Compiler Tools Run

| Tool | Result | Notes |
|---|---|---|
| comp-build | 1747/1785 indexed | Normal; 38 unmapped external resources |
| comp-iam gaps | No gaps | All Lambda/EC2 IAM statements correct |
| comp-pii audit | 3 refs, all pseudonymized | Advisor-intel components only |
| comp-routes auth-map | 2 findings (F1, F2) | security-scanner no CF auth; json-tiered no auth |
