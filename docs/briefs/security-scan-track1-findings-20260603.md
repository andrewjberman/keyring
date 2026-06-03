# Security Scan — Track 1 Findings (no-compiler-dependency axes)

**archetype:** DIAGNOSE
**secondary_archetypes:** EXPLORE, VALIDATE
**Author:** 0.7.0_AE_CloudOps
**Date:** 2026-06-03
**Trigger:** Andrew-direct — comprehensive FE→back security scan; Track 1 = the axes that need NO compiler (run early while 0.4.0 hardens comp-iam for the deep pass).
**Doubles as:** ADHC_CMPAWS per-bucket enrichment / CVO hand-audit fixture (COO ruling 152755Z) — the encryption+access census below is the fixture; carries the SSE-Deny operational-pain flag.

## Scope + method
Two axes, live-AWS + live-deps (not Terraform-desired): (A) dependency/CVE scan, (B) encryption-at-rest/in-transit + public-access census. Account 313476888478, us-east-1.
**NOT in Track 1** (deferred to the comprehensive pass, gated on 0.4.0's comp-iam Deny/scoping/unmodeled fix): IAM over-permissioning / least-privilege, secrets-in-code, EC2/SG/network exposure, CloudFront/edge auth-bypass, injection/exploit code review. Reason: comp-iam currently has dangerous false-greens (reads explicit Deny as granted; non-s3/ssm/dynamodb services invisible; ignores resource/condition scoping) — a least-privilege audit leaning on it would be falsely reassured.

---

## AXIS A — Dependency / CVE

### Frontend (portal) — `bun audit`: 47 vulnerabilities (23 HIGH, 23 moderate, 1 low)
Highest-priority (runtime / direct — ships to users):
| Package | Sev | Issue | Path | Note |
|---|---|---|---|---|
| **xlsx (SheetJS)** <0.19.3 | **HIGH x2** | Prototype Pollution + ReDoS | **DIRECT dep** | No fix on npm (SheetJS moved off npm registry); if portal parses/builds Excel client-side this is live. Highest-priority — needs migration to the SheetJS CDN build or server-side xlsx. |
| **axios** | moderate | XSRF-token cross-origin leakage via prototype-pollution gadget in `withXSRFToken`; + follow-redirects transitive | DIRECT (API client, every call) | Auth-relevant — portal sends Bearer tokens. `bun update axios` to patched. |
| **lodash** <=4.17.22 | **HIGH** | Code injection via `_.template`; + prototype pollution | transitive via @nivo/@visx charting | Runtime (charts). |
| **postcss** <8.5.10 | moderate | XSS via unescaped `</style>` in stringify | DIRECT | Mostly build-time. |
| rollup, flatted, ajv, brace-expansion, picomatch, esbuild | high/mod | ReDoS / path-traversal / proto-pollution | transitive via vite + eslint/typescript-eslint | Build/dev-time — lower prod risk but real. |

Remediation lever: `bun update` (compatible) clears many; the high ones (xlsx, lodash via charts) need major bumps / migration (`bun update --latest`, breaking) — sequence as an RD/DE FE task with a test pass. **xlsx is the standout** (direct + no-npm-fix).

### Backend (Python Lambda layers) — pinned-version inventory: HEALTHY
Recent, well-pinned across the deployed layers (numpy 2.2.6, scipy 1.16.3, openai 2.23.0, httpx 0.28.1, anthropic 0.45.0, pydantic 2.12.5, requests 2.33.1, urllib3 2.6.3, certifi 2026.x, Pillow 11.1.0, lxml 5.3.x). No obviously-stale/EOL runtime deps.
- MINOR: `security-scanner-deps/requirements.txt` pins pandas/openpyxl with **NO version** (non-reproducible build; could pull a vulnerable release) — pin them.
- MINOR: `find-insure-browser-deps` playwright==1.40.0 is stale (late-2023); internal scraper, low exploit surface — bump opportunistically.
- (A live `pip-audit` pass would confirm transitive CVEs — pip-audit not on PATH; recommend adding it to the runner image for the comprehensive pass.)

---

## AXIS B — Encryption-at-rest / in-transit + public access (S3 / DynamoDB / KMS / Secrets)

### S3 (31 buckets) — STRONG baseline
- **At rest: 100% SSE-AES256** (no unencrypted bucket). GOOD.
- **Public access: 100% Block-Public-Access fully on (all 4 flags True)** (no public bucket). GOOD.
- **GAP — TLS-in-transit enforcement: only `opal-data-schwab`** has a `DenyInsecureTransport` (aws:SecureTransport=false) bucket policy. The other **30 buckets do not enforce TLS at the policy layer** (clients use TLS by default, but nothing blocks a plaintext request). LOW-MED — add the standard 2-line Deny to data buckets.
- **GAP — SSE tier: all SSE-S3 (AES256), zero SSE-KMS.** For PII/financial buckets (schwab, trade-submissions, portal-v2, users-data, imo) SSE-KMS adds key-access CloudTrail audit + rotation + grant control. (find-insure KMS upgrade already roadmapped per imo PRD.) MED for sensitive buckets.
- **GAP — versioning disabled on 10 buckets** (incl. opal-cloudtrail-logs, opal-data-etfs/news-av/pm, opalinvest-portal, ci-staging): no object-version recovery (ransomware/accidental-delete). cloudtrail-logs non-versioned is a mild audit-integrity concern. LOW-MED.

### DynamoDB — TIER INCONSISTENCY (real finding)
Most tables use KMS SSE, but **sensitive tables sit on AWS-owned default** (encrypted, but no CloudTrail key-audit / rotation / control):
- **`opal-trade-submissions`** (financial) — AWS-owned default.
- **`opal-partner-49financial` / `opal-partner-cottonwood` / `opal-partner-inflection`** — AWS-owned default. *These mint JWT identity claims (firmRole/advisorId)* — yet `opal-users-v2` and `opal-pii-lookup` (comparable sensitivity) ARE on KMS. Inconsistent bar.
- (Lower-sensitivity AWS-owned: bd-securities, etf-classifications, find-insure-cost-state, opal-inf-launch-locks, opal-keyword-intelligence, seeking-alpha-article-urls — acceptable.)
- RECOMMEND: bring opal-trade-submissions + the 3 opal-partner-* tables to KMS to match the user/PII tables. MED.

### KMS / Secrets
- Only 2 customer-managed CMKs (find-insure-data-key, inf-ebs-key); most KMS-SSE uses the aws-managed `aws/dynamodb` key (acceptable — still CloudTrail-auditable, better than AWS-owned).
- Secrets Manager: ~10 secrets, predominantly on the default aws-managed key (acceptable; CMK optional for higher control).

---

## Severity-ranked action list
1. **HIGH — xlsx/SheetJS (FE, direct, no-npm-fix):** migrate off the vulnerable npm xlsx (CDN build or server-side). RD/DE.
2. **HIGH/MED — FE dependency sweep:** `bun update` + planned major bumps for lodash(charts)/axios; re-run `bun audit` to 0-high. RD/DE.
3. **MED — DynamoDB KMS tier:** opal-trade-submissions + opal-partner-{49financial,cottonwood,inflection} → KMS (match opal-users-v2). AE/CloudOps (TF).
4. **MED — SSE-KMS for PII/financial S3 buckets** (schwab/trade-submissions/portal-v2/users). AE/CloudOps (TF).
5. **LOW-MED — TLS-enforcement Deny** on the 30 data buckets lacking it (the inverse of schwab). AE/CloudOps (TF, cheap).
6. **LOW-MED — enable versioning** on the 10 disabled buckets (esp. cloudtrail-logs). AE/CloudOps.
7. **MINOR — pin** security-scanner-deps pandas/openpyxl; bump playwright; add pip-audit to runner for the comprehensive Python pass.

## Operational-pain flag carried forward (for the CVO oracle / CMPAWS)
`opal-data-schwab` SSE-enforcement Deny (`s3:x-amz-server-side-encryption != AES256` → AccessDenied on PutObject) = the BMKAUD-class footgun: any writer omitting the SSE header gets a silent AccessDenied. The census captures the Deny condition so the compiler can flag every writer-role/path that could trip it.

## Track 2 (the comprehensive pass) — gated handoff
Once 0.4.0 lands the comp-iam Deny/scoping/unmodeled fix + my comp-aws live IAM census, run: IAM least-privilege/over-permissioning, secrets-in-code, EC2/SG/network exposure, edge auth-bypass, and an injection/exploit code-review pass FE→Lambda. Scope skeleton to be authored + registered (COO/CTO).
