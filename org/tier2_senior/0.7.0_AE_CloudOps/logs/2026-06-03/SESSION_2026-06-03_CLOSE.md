# 0.7.0_AE_CloudOps — Session Close Log 2026-06-03

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, DIAGNOSE, SCRIBE, COORDINATE
**Scope:** full-day session — Andrew-direct cold-start remediation → fabric-wide security scan → CMPAWS census build → live IAM-security walkthrough. Supersedes the early SESSION_2026-06-03.md (first-half only). Per-tick detail in work_*.md.

---

## SHIPPED + VERIFIED (closed this session)
| Item | Evidence |
|---|---|
| Keep-warm FIX2 backend `?warm=1` no-op (opal-partners-data + data-proxy) | partners-api-v1.16.3 + market-overview-v1.11.1 (verified 200 no-store {"warm":true}) |
| Cold-start FIX1 (`retry:false` false-empty) | RD portal DEV 21be552d (validated) |
| xlsx/SheetJS HIGH CVEs → CDN-build swap | RD portal DEV 3e0ce8d0 (pending DT promote v2.1.114) |
| DynamoDB-KMS — 4 sensitive tables (3 opal-partner JWT-claims + opal-trade-submissions) AWS-owned→KMS | da7996b18 (in-place, 0-loss) |
| inf-otp-relay public-unauth hardening (?k= token-gate + state-gate + Twilio-removal + /status gate) | inf-pipeline-v1.7.70 (API-GW 403/200 verified) |
| inf-otp-relay dead SCP-blocked Function URL + public-invoke permission deleted | inf-pipeline-v1.7.71 |
| yang-pipeline-lambda-role cloudwatch:PutMetricData grant (silent-metric-loss fix) | yang-pipeline-v1.4.1 (namespace-scoped) |
| INF fee-split deploy (ADVI_FEREFI.W2 #6) | inf-pipeline-v1.7.69 (DS verify PASS) |
| MDPF_SCOPED.OPS1 closure (AC1-6, 2 consecutive scheduled clean runs) | ab072abd8 (RAVC2-accepted) |
| CMPAWS census fixtures (S3 / IAM+tf_managed / compute) — CVO hand-audit GREEN (G1 closed) | c8531c23c, de474e6d9, ee462b4f7, b9d04e3fa |
| Security engagement canonical tracker | 535cde2df |

## VERIFIED-CLEAN (no action — good posture)
S3: 31/31 SSE-AES256 + 31/31 Block-Public-Access on. EC2 EBS 100% encrypted. Security groups: 0 world-open non-web ports. SQS encrypted. Portal auth = RS256 asymmetric. No AWS secret keys / private keys / committed .env.

---

## NEXT STEPS (forward queue — for resume)

### A. Security review — Track-2 remediation list (HELD for Andrew priority; canonical tracker `docs/briefs/security-engagement-tracker-20260603.md` 535cde2df)
Live walkthrough was mid **finding #1 (over-broad IAM exec roles)** when paused. Per-role disposition (verify-before-detach discipline — caught 2 unsafe-blind cases):
- **#1 market-update-lambda-role** (`S3FullAccess`+`DynamoDBFullAccess`+`SecretsManagerReadWrite`): DO NOT detach blind — 3 functions are EXTERNAL (code not in repo) + scoped policy region-mismatched (us-east-2 vs us-east-1 funcs). NEXT = derive least-priv from CloudTrail/IAM-Access-Analyzer, monitored cutover. NOT a quick detach.
- **#1 opal-news-lambda-role** (`DynamoDBFullAccess`+`SecretsManagerReadWrite`+`S3ReadOnlyAccess`): the ONE cleanly-actionable role — 1 in-repo function (opal-news-layer3-curation), usage enumerated (tables opal-news-articles + opal-news-trending-daily, secret openai-api-key, buckets opal-data-news-av + opal-data-portal-v2, lambda-invoke already scoped). NEXT = AUTHOR a scoped inline → attach → detach the broad policies → plan/apply/verify (reversible). **Recommended first #1 win.**
- **#1 seeking-alpha-scraper-role** (`ECRFullAccess`): role shared by 7 in-repo Lambdas + a stopped EC2; the seeking-alpha NEWS pipeline is ACTIVE (ran today, daily cron) — DO NOT decommission. ECRFullAccess is for the (stopped) EC2 Docker pulls; removal needs care (EC2 manifest-registered, may restart).
- **#2 IMDSv2** not enforced on 5 EC2 (SSRF→cred-theft): bd-gold-layer-runner + smartx-exporter are start-stop RUNNERS (stopped ≠ mitigated). NEXT = HttpTokens=required WITH IMDSv1-caller check (don't break the nightly).
- **#3** 2-secret rotation: Bright Data creds in a committed log (Google CSE moot — unused). **#4** S3-SSE-KMS for PII buckets. **#5** FE dep-sweep (45 non-xlsx CVEs, non-breaking, RD plan 867660fd5). **#6** TLS-Deny on 30 buckets / S3 versioning on 8 / 7 SNS unencrypted / 2 shadow S3 buckets into IaC.
- **IAM-governance (new, from CMPAWS):** 19 Terraform-ungoverned live roles (14 import-candidates incl portal-auth/portfolio-management/schwab-anonymizer; 5 accept-external). Disposition ONCE across cert+security lenses (CVO+COO coordinating).
- **TOP-MATERIALITY (operator):** laptop on long-lived `*:*` admin access key → move to SSO/short-lived + scoped agent-operator role. Andrew decision.
ROUTING (COO ruling): Andrew-live GO = execute-direct (no TO gate), careful-verify still applies; COO TOs post-hoc off the tracker.

### B. NFRA (cost-governance) — I am proposed owner (org/projects/NFRA.json; source brief 813651cf4). Queued behind security.
NEXT = RAVC COO a W1→W5 sequencing plan. Workstreams:
- W2(c) fleet telemetry rollout (inf/smartx/mdpf/t3) + fix inf-gold cpu:null · W2(d) monthly perf-rollup cadence
- W1 cost-attribution (resource-level Cost Explorer + cost-allocation tags project/dispatch/runner + optional CUR→Athena)
- W3 right-sizing (bd-gold + QA-runner first) — **VALIDATE ON SCHEDULED NIGHTLIES ONLY (Andrew compute-discipline, binding — no manufactured gold runs)**; rigor = units-verified, CPU-instance-%-not-per-core, live-corroboration, wall-time-vs-cost
- W4 runner lifecycle/hygiene (auto-shutdown esp QA GOLD_KEEP_ALIVE, EBS orphan/oversize sweep, S3 lifecycle, ephemeral-vs-persistent policy)
- W5 cadence + ownership (monthly cost review, wire cost-anomaly-scanner, thresholds/alarms)
- (Not mine: W2(a) telemetry wire = 0.6.0; W2(b) gold_prof = DS — I'm CC.)

### C. CMPAWS PASS-2 (CVO cert; sanctioned capacity-fill) — G1 closed-green.
NEXT = G2 edge census (compute→IAM, role→bucket, compute→SG, SNS→subscriber) → ping CVO PASS-2. Then G3 (CloudFront/EventBridge/StepFn/CloudWatch nodes), G4 (EC2 type/EBS-size).

### D. PMTRDX deploy (RD~B prepped, non-urgent — broker orders already correct).
NEXT = TF-deploy portfolio_excel_generator (÷100 fraction fix) [portfolio-management pipeline] + 2 trade-pipeline excel_generators, then run the standalone remediation script (dry-run → COO/CTO/Andrew-gated --apply). Pre-flight live-CodeSha-vs-repo first.

### E. With others (no AE action pending)
keep-warm FE-hook promote browser-smoke (Andrew visual) · bd-publisher decommission (CTO ruling) · CVO PASS-2.

---

## Compiler Tools
comp-iam (yang fix verify [GRANTED] + the 0.4.0 reconcile collab — my IAM census feeds comp-iam's live-AWS overlay) · comp-iam-service (no-IAM-delta confirms) · build-and-upload / safe-apply / record-terraform-deploy (all deploys) · live boto3 census (S3/IAM/EC2/SNS/SQS/DynamoDB) for CMPAWS fixtures. comp-validate NO_CONFIG→exit2 flip (LD-0148) noted for future gold-signal.
