# ADHC_CMPAWS Phase-1 IAM/EC2 — Live-AWS Cross-Check D-LIST (AE 0.7.0)

**archetype:** VALIDATE
**secondary_archetypes:** TRACE
**Auditor:** 0.7.0_AE_CloudOps · **Date:** 2026-06-08 ~14:00-14:15Z
**Oracle:** `org/modules/graph/aws-shapes/iam-ec2-hand-audit-fixture-v0.1.yaml` (CVO, commit b8d8efc00)
**Live feed:** `.runtmp/cmpaws_iamec2_xcheck/{iam-axis,compute}-census-20260608*.json` (fresh 06-08, enriched)
**Method:** live-AWS read-only (boto3/CLI) — ec2/iam/autoscaling describe + get-instance-profile + list-attached-role-policies (boto3, in-process) + local TF scan. Schema = AE-CVO handshake 1342Z.
**Scope:** inventory catalog + diff (NOT remediation — over-perm/IMDSv2/SNS are CATALOGED-HELD for Andrew steer).

## Headline
6 oracle gaps worked. EC2: the ~13 apparent LIVE-no-DECLARED are **confirmed genuinely unmanaged** (0 ASG, 0 launch-template account-wide). IAM: role SET stable 111/111; 3 broad-managed = exactly the overperm set; both statement-drifts are TF-DECLARED updates (no live mutation). One method-finding (IE-GAP-3 tf-recon needs HCL-aware parser). Two dispositions for CVO/COO (moltbot removal; seeking-alpha no-profile).

## D-LIST (IE-GAP-1..6)

### IE-GAP-1 (P1, HIGH-VALUE) — RESOLVED: genuinely LIVE-no-DECLARED (unmanaged)
- **0 Auto Scaling Groups, 0 Launch Templates account-wide.** `describe-auto-scaling-groups` empty; `describe-launch-templates` empty; every live instance has NO LaunchTemplate assoc, NO `aws:autoscaling:groupName`, NO `aws:ec2launchtemplate:id` tag → provenance=NONE for all 24.
- Therefore the apparent-LIVE-no-DECLARED set is **REAL** unmanaged compute (ad-hoc/manual `run-instances`, console or CLI), NOT launch-template/ASG/spot-fleet provenanced: **bd-gold-layer-runner** (r6i.4xlarge), **bd-gold-qa-runner** (c6i.16xlarge — the ~34%-of-bill driver), **seeking-alpha-scraper x2**, **historical-prices-fetcher fleet**, and the rest of the live set beyond the 12 TF-declared.
- **NEW SUB-FINDING — hpf fleet count is VOLATILE:** live shows **9** historical-prices-fetcher (incl `i-0f8dd54ec78384c0f`) vs **8** in my census pulled minutes earlier → the fleet churns (ad-hoc launch/terminate). The "13 apparent live-no-declared" is a moving target; recommend the oracle treat the hpf fleet as a *dynamic unmanaged backfill set* (count not pinned), not N fixed nodes.
- Drift class for all: **LIVE-no-DECLARED** (confirmed, not launch-template).

### IE-GAP-2 (P1) — DONE: EC2 shape enriched
- Added `instance_type` + `instance_profile` to all live EC2 (`compute-census-20260608-enriched.json`). Authoritative instance types: **bd-gold-qa-runner=c6i.16xlarge** (the expensive one — corrects oracle v0.1's mis-attribution to bd-gold-layer-runner), bd-gold-layer-runner=r6i.4xlarge, inf-gold-layer-runner=c6a.4xlarge, bd-gold-detail-generator=r6i.xlarge, hpf=t3.xlarge, bd-exporters/mdpf=t3.medium, inf-bronze/smartx=t3.small. owner_pipeline/tf_managed resolve from oracle's declared side.

### IE-GAP-3 (P1) — METHOD FINDING: naive text-scan undercounts declared; 92/19 baseline stands
- My 06-08 re-derive (both non-greedy regex AND brace-safe line-scan) yields **76 declared / 35 shadow** — but this is a **text-scan undercount**, NOT real drift: I PROVED ≥16 of the "extra shadow" are TF-declared (e.g., `FredIngestionLambdaRole` IS in `fred-pipeline/iam.tf`; `opal-portal-lambda-role`, `smartx-exporter-role-*`, the `lambda-causality-*` fleet all real TF roles). Naive `.tf` scanning misses roles whose `name` is interpolated / `name_prefix` / multi-line / past nested `assume_role_policy` braces.
- **Resolution:** the **92 declared / 19 shadow** baseline (06-03, robust method) STANDS; the live role SET is stable (111/111, 0 added/removed 06-03→06-08), so the split carries forward unchanged. **Correctness note for comp-iam:** `tf_managed` determination must use an **HCL-aware parser** (or `terraform state list` per module), not text-grep — text-grep produces false LIVE-no-DECLARED. (This is itself a sub-compiler design finding.)

### IE-GAP-4 (P1) — DONE: per-role managed-vs-inline breakout
- 111 roles: **83 have >=1 attached managed policy; 92 total managed attachments** (boto3 `list_attached_role_policies`; inline captured via `statements.source`). [Capture note: shell `while read` loops returned all-empty due to CRLF `\r` on role names + stdin consumption — boto3 in-process is the reliable method.]
- **Broad-managed (FullAccess/Admin): exactly 3** = `market-update-lambda-role` (DynamoDB+S3 FullAccess), `opal-news-lambda-role` (DynamoDB FullAccess), `seeking-alpha-scraper-role` (ECR FullAccess) — **identical to the overperm set**, NO new broad-managed roles. Consistent with Track-2 F1.

### IE-GAP-5 (P2) — DONE: INSTANCE_PROFILE -[ASSUMES]-> IAM_ROLE
- 9 unique profiles mapped 1:1 to roles: bd-exporter-profile→bd-exporter-ec2-role; bd-gold-detail-generator-profile→bd-gold-detail-generator-role; inf-{bronze-runner,exporter,gold-layer,gold-qa-runner}-profile→matching *-ec2-role; mdpf-daily-runner-profile→mdpf-daily-runner-ec2-role; smartx-exporter-profile-*→smartx-exporter-role-*; seeking-alpha "seeking-alpha-scraper-role" profile→seeking-alpha-scraper-role.
- **FINDING (HAS_PROFILE gap):** seeking-alpha-scraper 2nd instance `i-06376c11d8b3c3443` has **NO instance_profile** (the other, `i-07ebae29a16e43ed1`, has seeking-alpha-scraper-role). Disposition needed: intentional no-role instance vs config gap.

### IE-GAP-6 (P2) — RESOLVED: both statement drifts are DECLARED (TF-tracked) updates
- `smartx-ingestion-lambda-role` 3→4 stmts: +1 NEW inline `smartx-s3-access` = `s3:GetObject/ListBucket` on `opal-data-mdpf` + `/*`. **TF-DECLARED** — the opal-data-mdpf grant IS in `smartx-pipeline/iam.tf`. Cross-pipeline read (smartx reading MDPF), tracked.
- `FredIngestionLambdaRole` 5→5 stmts: inline `yield-curve-artifact-write` expanded `s3:PutObject` → `s3:GetObject + s3:PutObject` on `opal-data-portal-v2/json/macro/yield_curve_fred.json`. **TF-DECLARED** — IS in `fred-pipeline/iam.tf`. Yield-curve work, tracked.
- Neither is a LIVE-no-DECLARED mutation. Clean.

## Dispositions (for CVO adjudication / COO)
1. **moltbot** `i-0b784d4908e320fc4` removed from live (was the persistent Claude-Code agent host; never TF-declared → was always LIVE-no-DECLARED). Its IAM role `MoltbotEC2Role` PERSISTS (orphaned). Likely intentional agent-host teardown (not a pipeline instance) — needs COO/Andrew confirm expected-vs-drift; if expected, orphaned-role cleanup is a (held) finding.
2. **demo-transform-runner** removal = EXPECTED (R5 decommission 9bfd1c7b5) — oracle pre-recorded DECLARED-no-LIVE; confirmed, not flagged.

## Net vs oracle
EC2 12-declared baseline holds; live-no-declared CONFIRMED genuinely unmanaged (0 LT/ASG). IAM SET stable; 92/19 baseline stands (tf-recon method caveat); 3 overperm/broad-managed unchanged; statement drifts both TF-declared. Ready for CVO adjudication → certify (fold corrections: c6i.16xlarge=bd-gold-qa-runner; hpf fleet dynamic; tf-recon needs HCL-parser; moltbot+seeking-alpha-noprofile dispositions).

## Compiler Tools
comp-iam not re-run this pass (the cross-check IS the comp-iam tf_managed axis at finer grain; the IE-GAP-3 finding feeds back to comp-iam's tf_managed method). boto3 live pulls + local TF scan substituted, per the S3 Step-2 pattern.
