# Security Engagement — Master Findings + Remediation Tracker (2026-06-03)

**archetype:** SCRIBE
**Author:** 0.7.0_AE_CloudOps
**Scope:** Andrew-direct FE→back security scan + the cold-start remediation it began with. Consolidates the session's findings (scattered across the briefs linked below) into one prioritized tracker for Andrew's steer, COO TO-routing, and CVO hand-audit.
**Method:** live-AWS (boto3/CLI read-only) + tracked-file/source scan + manual disambiguation. No dedicated CVE/secrets tooling available (gitleaks/trufflehog/pip-audit absent) — pattern + manual; `bun audit` for FE.

## Source briefs (detail)
- `security-scan-track1-findings-20260603.md` — dependency/CVE + encryption-at-rest census
- `secrets-in-code-scan-20260603.md` — secrets scan
- `fe-driven-lambda-keep-warm-feasibility-20260603.md` + `advi-books-publicprofile-coldstart-false-empty-fe-brief-20260603.md` — cold-start remediation
- `cmpaws-{s3-iam,iam-axis,compute}-census-*.json` — CMPAWS census fixtures (CVO hand-audit oracle)

---

## A. SHIPPED + VERIFIED this session (closed)
| Item | Evidence |
|---|---|
| xlsx/SheetJS HIGH CVEs (proto-pollution+ReDoS, no npm fix) → CDN-build swap | RD portal DEV 3e0ce8d0 (pending DT promote) |
| Cold-start FIX1 — `retry:false` false-empty on ADVI deep drilldowns | RD portal DEV 21be552d |
| Cold-start FIX2 — keep-warm `?warm=1` no-op (opal-partners-data + data-proxy) | partners-api-v1.16.3 + market-overview-v1.11.1; FE hook RD ed16010c (promote browser-smoke = Andrew) |
| DynamoDB-KMS — 4 sensitive tables (3 partner JWT-claims + trade-submissions) AWS-owned→KMS | da7996b18 (in-place, 0-loss) |
| inf-otp-relay — public unauth OTP relay → `?k=` token-gate + state-gate + Twilio-path removed + /status gated | inf-pipeline-v1.7.70 (API GW 403/200 verified) |
| inf-otp-relay dead Function URL + public-invoke permission deleted (SCP-blocked) | inf-pipeline-v1.7.71 |
| yang-pipeline-lambda-role missing `cloudwatch:PutMetricData` (silent metric loss) | yang-pipeline-v1.4.1 (namespace-scoped) |

## B. CLEAN (verified good — no action)
- **S3:** 31/31 buckets SSE-AES256 at rest + 31/31 Block-Public-Access fully on (no unencrypted, no public bucket).
- **EC2:** EBS volumes 100% encrypted. Security groups: 0 world-open (`0.0.0.0/0`) non-web ports.
- **DynamoDB:** sensitive tables now KMS (post-fix); remaining AWS-owned are low-sensitivity reference/lock tables.
- **Auth:** portal uses RS256 asymmetric (public key in SM = correct). No AWS secret keys / private keys / committed `.env`.
- **SQS:** both queues encrypted.

## C. HELD — Track-2 remediation tracker (awaiting Andrew priority steer → COO TOs)
| # | Finding | Sev | Lane | Fix | Status |
|---|---|---|---|---|---|
| 1 | 3 execution roles on `*FullAccess` (market-update=S3+Dynamo, opal-news=Dynamo, seeking-alpha=ECR) — account-wide reach | MED | AE | replace managed FullAccess w/ scoped inline | HELD |
| 2 | 5 EC2 don't enforce IMDSv2 (SSRF→cred-theft): seeking-alpha-scraper, bd-gold-layer-runner, bd-gold-qa-runner, smartx-exporter | MED | AE | `HttpTokens=required` (care: IMDSv1 callers) | HELD |
| 3 | Bright Data proxy creds committed in a session log | MED | AE | rotate + redact log; (Google CSE moot — unused) | HELD |
| 4 | S3 PII/financial buckets all SSE-S3, none SSE-KMS | MED | AE | per-bucket KMS (schwab/trade-submissions/portal-v2/users) | HELD |
| 5 | FE dep-sweep — 45 non-xlsx CVEs, all non-breaking (axios/postcss/lodash via charts) | LOW-MED | RD/DE | `bun update` (plan ready 867660fd5) | HELD |
| 6 | TLS-Deny absent on 30 buckets (only schwab enforces); SSE-write-trip footgun is the schwab Deny | LOW | AE | add DenyInsecureTransport | HELD |
| 7 | 8 S3 buckets versioning-disabled (incl cloudtrail-logs) | LOW | AE | enable versioning | HELD |
| 8 | 7 SNS topics unencrypted at rest (ops alerts) | LOW | AE | KMS on topics | HELD |
| 9 | 2 shadow S3 buckets not in IaC (ajb-workflow, opal-data-aaii-v2) | LOW | AE | import to Terraform | HELD |
| 10 | Old known secrets in git HISTORY (FRED/NEWS/OPENAI/JWT_SECRET in removed snapshot) | LOW | — | Andrew WONTFIX'd scrub; free keys; JWT de-fanged by RS256 | ACCEPTED |

## D. TOP-MATERIALITY (operator-level, above the table)
**The laptop running the agent fabric on a long-lived `*:*` admin access key (`Andrew_Berman`, AKIA key ~7mo, MFA on console but NOT on the programmatic path) + the lethal-trifecta exposure is the single highest-materiality risk.** Recommendation: move to AWS SSO/short-lived creds + a scoped agent-operator role (not `*:*`). Operator decision — not an AE auto-fix. (Detail in the IAM/laptop analysis turn.)

## E. CMPAWS census fixtures (for CVO hand-audit oracle + sub-compiler 0-diff baseline)
S3+IAM (per-bucket), IAM-axis (111 roles, 0.4.0 comp-iam reconcile contract shape), compute (EC2/SNS/SQS). Awaiting CVO when its verification queue drains. comp-iam (0.4.0) source-side hardened (deny-aware + unmodeled-sentinels); IAM-axis completeness = source-side + this live census jointly.

## F. With others
keep-warm FE-hook promote browser-smoke (Andrew) · bd-publisher decommission (CTO ruling) · CVO hand-audit of E · Track-2 dep-sweep (RD).
