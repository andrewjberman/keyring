# ADHC_CMPAWS Phase-0 — CVO Hand-Audit PASS 1 (the certification oracle)

**archetype:** CERTIFY (hand-audit oracle)
**Author:** 3.0.0_SA_CVO
**Date:** 2026-06-03
**For:** 2.0.0_SA_COO (RAVC2) + 0.7.0_AE_CloudOps (async co-sign + question-bank)
**Inputs audited:** `cmpaws-s3-iam-census-fixture-20260603.json` (c8531c23c),
`cmpaws-compute-census-20260603.json` (b9d04e3fa), `cmpaws-iam-axis-census-20260603.json` (de474e6d9)
**Cross-ref (per COO directive, not re-derived):** `security-engagement-tracker-20260603.md`

The ADHC_CMPAWS cert oracle certifies **inventory completeness + correct typing + internal
consistency** — the regression fixture the sub-compiler must diff-to-0-diff against. This is a
DISTINCT lens from the security tracker (which asks "is it secure?"); this pass asks "is the
inventory complete, correctly typed, and self-consistent enough to BE the cert baseline?"

---

## 1. INTERNAL CONSISTENCY — PASS (all three fixtures self-reconcile)

Every summary statistic was re-derived from the per-resource arrays independently:

- **S3 fixture:** 31 buckets (counted), 9 has_policy (counted, matches the named list), 1 deny
  bucket (schwab, deny_count=2), 31/31 SSE-AES256, 31/31 PAB-all-on, 8 versioning-disabled
  (counted), 2 shadow tf_managed=false (ajb-workflow, opal-data-aaii-v2). **DDB:** 34 tables, 28
  KMS / 6 AWS-owned (counted, matches the named list). ALL RECONCILE.
- **Compute fixture:** 25 EC2 (counted), 5 IMDSv1-not-required *instances* (4 distinct names —
  seeking-alpha-scraper appears on 2 distinct instance_ids, correctly instance-id-keyed), 4
  public-IP, 8 SNS / 7 unencrypted (counted), 2 SQS both SSE-SQS. ALL RECONCILE.
- **IAM-axis fixture:** 111 roles (counted, zero duplicate role_names), 3 over-perm flags
  (market-update / opal-news / seeking-alpha-scraper) — matches tracker C1 exactly.

**Cross-fixture vs tracker B/C:** versioning-8, shadow-2, TLS-deny-1, IMDSv2-5, SNS-unenc-7,
SSE-31, PAB-31 — all consistent. No contradictions between the censuses and the tracker.

Verdict on consistency: **GREEN.** The fixtures are trustworthy node inventories.

---

## 2. CERT-BLOCKING COMPLETENESS GAPS (the oracle's substantive output)

These are the items that prevent a sub-compiler from being certified to 0-diff. They are
legitimate Phase-0-census-shape deferrals — flagged here as the cert long-pole, NOT as fixture
defects.

### G1 — IAM axis has NO declared-vs-live drift field (cert-blocking)
The S3 fixture carries `tf_managed:bool` per bucket (that field is what enabled the 2-shadow-bucket
finding). The IAM census carries **no per-role `tf_managed`** — `source` is per-*statement*
(inline/attached), not per-role TF-provenance. The defining ADHC_CMPAWS 3-source cert axis
(declared TF / live AWS / on-disk) is therefore **uncomputable for IAM from this fixture.**

Independent CVO re-derivation of the candidate drift set (diff of 111 live role_names vs all
`infra/aws/terraform/**` source text):
- **92/111 role names present in TF; 19/111 ABSENT.** The 19 (UPPER BOUND — see honest-limit):

  | Likely-benign (AWS-service / CI / console) | Likely real shadow-drift (app/pipeline roles) |
  |---|---|
  | ecsTaskExecutionRole, rds-monitoring-role, vpc-flow-logs-role, github-actions-opal-deploy, codebuild-semantic-clustering-role | bd-merge-daily-lambda-role, opal-smartx-lambda-role, portal-auth-lambda-role, portfolio-management-lambda-role, schwab-anonymizer-lambda-role, sentiment_query_api-role, workspace-sync-lambda-role, bd-pipeline-task-role, finbert-ec2-backfill-role, lambda-access-anomaly-scanner-role, lambda-cost-anomaly-scanner-role, lambda-ec2-runtime-monitor-role, lambda-test-role, security-sweep-dedicated-role |

  **HONEST LIMIT:** exact-name substring test. A role declared in TF via `name_prefix` or
  `name = "${var.x}-role"` interpolation is a false-positive "absent." So 19 is the UPPER bound on
  shadow drift; the true shadow set is ≤19. The right→left split above is the oracle's *hypothesis*,
  not a verdict — each needs per-role disposition with AE's TF knowledge. This is the exact analog
  of the S3 "intentionally-no-policy vs missing-policy" judgment the census-shape brief flags as
  the oracle's call.

  **Cert impact:** the IAM sub-compiler cannot diff-to-0-diff on a drift axis the fixture doesn't
  enumerate. FIX = add `tf_managed:bool` + `tf_source` per role to the IAM census (parity with the
  S3 schema), then disposition the ≤19 candidates.

### G2 — EDGE census absent across all three fixtures (the Phase-0 long-pole)
ADHC_CMPAWS's defining deliverable is a TYPED graph with EDGES. All three fixtures are pure NODE
inventories — zero edges. The census-shape brief itself *proposes* an `IAM edge: role→bucket`
schema that no fixture yet realizes. Missing edge classes:
- **compute→IAM-role** (EC2 instance-profile/role not in the compute census at all)
- **compute→SG** (the tracker asserts "0 world-open non-web SGs" — but the SG census is NOT in any
  fixture, so that security assertion is **not certifiable from the fixture as delivered**)
- **role→S3-bucket effective-permission** (the brief's proposed edge — the NEW value over comp-iam's
  allow-axis; this is the bucket-policy-Deny × writer-role cross-ref that flags the schwab
  SSE-write-trip footgun per-writer)
- **SNS→subscriber** messaging edges (+ SNS/SQS access policies)
- **CloudFront→origin** (no CloudFront census at all — see G3)

This is precisely "the edge/resource census the tracker doesn't cover" per the COO directive.

### G3 — Node-class coverage vs PRD taxonomy (4 classes uncensused)
PRD enumerates 13 node classes. Censused: S3, DynamoDB, IAM, EC2, SNS, SQS (+ KMS count-only [2
CMKs] + Secrets count-only [10]). Lambda deferred to comp-lambdamap absorb (OK). **NOT yet
censused: CloudFront, EventBridge, StepFunctions, CloudWatch.** KMS + Secrets are count-only, not
enumerated nodes. Cert completeness requires these as enumerated nodes.

### G4 — (Minor, schema) Compute nodes lack cost/edge attributes
EC2 nodes lack `instance_type` + EBS volume IDs/sizes — needed for the NFRA cost axis these same
fixtures feed (right-sizing) and the compute→EBS edge. Low priority; note for the schema pass.

---

## 3. BANKED QUESTIONS FOR AE-JOIN (async co-sign)
- **Q1 (G1 disposition):** Of the 19 TF-absent roles — which are intentionally non-TF (the
  left-column AWS-service/CI roles) vs real shadow drift to import (the right-column app-Lambda
  roles)? And are ANY of the 19 actually TF-managed via `name_prefix`/interpolation (false-positive
  in my exact-name test)?
- **Q2 (count reconciliation):** comp-iam parses **76** roles; TF has **88** `aws_iam_role` blocks;
  live census has **111** customer roles. The cert baseline needs a documented reconciliation of all
  three numbers (76→88 = comp-iam scope filter? 88→111 = ~23 live-only incl. service-linked?).
- **Q3 (security cross-edge, banked from the consistency pass):** bd-gold-layer-runner +
  smartx-exporter are BOTH public-IP AND IMDSv1-not-required — the elevated SSRF→cred-theft surface.
  Mitigant: both are currently `stopped`; the two *running* public instances (demo-transform-runner,
  inf-exporter) are both IMDSv2-required (safe). Confirm stopped-state is the accepted mitigant, or
  prioritize tracker-C2 IMDSv2 on those two first.

---

## 4. VERDICT
- **Fixtures-as-delivered:** GREEN for internal consistency + typing of the censused node classes.
  Trustworthy baseline for the node axis.
- **Cert-to-0-diff readiness:** NOT YET — blocked on G1 (IAM tf_managed/drift field) + G2 (edge
  census) + G3 (4 missing node classes). These are the Phase-0 long-pole, correctly identified by
  the PRD; this pass converts them from "deferred" to a concrete, prioritized cert-gap list with the
  19-role candidate drift set pre-derived.
- **Recommended next (oracle→build):** (1) AE answers Q1–Q3; (2) add `tf_managed`+`tf_source` to the
  IAM census schema (S3-parity) and disposition the ≤19; (3) ship the role→bucket + compute→IAM +
  compute→SG edge census as the next fixture; (4) census the 4 missing node classes. PASS-2 of this
  hand-audit certifies those increments.

Status: HAND-AUDIT PASS 1 COMPLETE. No fixture defects; 4 cert-completeness gaps (G1 cert-blocking,
G2 long-pole, G3 coverage, G4 minor) routed to the build. AE-join async.

---

## 5. AE CO-SIGN + Q-RESOLUTION (0.7.0_AE_CloudOps, 20260603T184358Z) — PASS-1 JOINTLY SIGNED

AE co-signed the GREEN node-consistency/typing verdict. All 3 banked Qs resolved:

- **Q1 RESOLVED + REFINED:** AE diffed all 14 "app-role shadow" candidates vs TF *including
  name_prefix/interpolation stems* — **all 14 are genuinely not-in-TF, zero false-positives.** So the
  upper-bound 19 narrows to a CONFIRMED split: **14 = real shadow drift (import candidates)** + **5 =
  intentionally-non-TF (accept-external: ecsTaskExecutionRole, rds-monitoring-role, vpc-flow-logs-role,
  github-actions-opal-deploy, codebuild-semantic-clustering-role).** Highest-priority imports:
  portal-auth + portfolio-management + schwab-anonymizer (auth/financial/PII-adjacent ungoverned).
  NEW FLAG from AE: `lambda-test-role` live in prod = scrutinize (likely leftover, possibly
  over-permissioned). AE will add `tf_managed` to the IAM census via literal-grep (the method that
  caught the opalinvest false-positive on the S3 fixture).
- **Q2 RESOLVED:** 76 (comp-iam MODELS — lambda-source-map subset) / 88 (all TF aws_iam_role decls,
  superset incl EC2/non-Lambda) / 111 (live customer roles, census skips AWSServiceRole*). 111 −
  ~88-applied ≈ 23 live-only = the 19 shadow + a few exact-name edge cases. AE documents the 3-way
  reconciliation in the fixture `_meta`; exact intersection closes when `tf_managed` lands per-role.
- **Q3 CORRECTED (my hypothesis was wrong — material):** stopped-state is **NOT** an acceptable
  mitigant. bd-gold-layer-runner runs the bd gold chain NIGHTLY (starts/stops) and smartx-exporter is
  periodic → the public-IP + IMDSv1 SSRF window OPENS on every scheduled run. AE prioritizes tracker-C2
  IMDSv2-enforce (`HttpTokens=required`) on both, WITH an IMDSv1-caller check first (confirm the
  launch-template/user-data SDK is IMDSv2-compatible so the nightly doesn't break). The 2 always-running
  publics being IMDSv2-required already is the good baseline. **This corrects §3 Q3's "stopped = latent
  mitigant" framing — banked-as-question, not asserted, precisely because it needed AE's operational
  knowledge of the run schedule.**

**PASS-2 (AE-build-gated, queued post-Andrew-walkthrough):** add `tf_managed` to IAM census + ship the
edge census (compute→IAM, role→bucket, compute→SG). AE pings CVO for hand-audit PASS-2 on landing.

**PASS-1 disposition: JOINTLY SIGNED (CVO oracle + AE co-sign). Node axis certified GREEN; edge axis +
IAM-drift field are the certified-open cert-gaps carried to PASS-2.**
