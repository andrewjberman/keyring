# Session Log — 0.7.0_AE_CloudOps~B
**Date:** 2026-06-10T13:31Z
**Tick type:** substantive (major — 3 workstreams closed)

---

## 1. bd/cot complete separation — AE structural guards (NFRA_DTAFLP)
Andrew sovereign 2026-06-10: bd + cot Black Diamond pipelines COMPLETELY separate (full fork, no shared code, separate S3, + 2 guards). Banked: feedback_bd_cot_complete_script_separation_no_shared.
- **Guard 1 (deploy-gate AST):** ds-precommit-check.py check_cross_firm_bucket_refs — blocks data/cot/ -> opal-data-bd/inf refs (+ data/black_diamond/ -> opal-data-cot) at commit. Real-bucket-ref match + docstring skip = 0 false-positives (verified). Commit 97e40bd14.
- **Guard 2 (IAM hard-Deny):** cot_exporter/cot_gold_layer Deny opal-data-bd+inf; bd_exporter Deny opal-data-cot. Applied + verified live. Commit 20617a347. Tags cot-pipeline-v0.3.8 + bd-v2.29.0.
- **ssm.tf footgun doc:** replaced "MIRROR of 49F" comment with loud DO-NOT-re-mirror warning (protects $373.2M cot patches).
- RAVC2-COMPLETE to COO + CTO (both ACK'd).
- DS conflict: my guard correctly blocks DS TO-1 seed-preservation (46 forked files w/ bd refs). Sent guard-owner input to COO (audited seed-import bypass + shared-custodian allowlist is a CTO/Andrew divergence-phase call; won't weaken guards unilaterally). Flagged IAM-Deny interaction (cot reads of opal-data-bd/schwab now blocked at runtime too; moot for v1 — Schwab skipped).

## 2. NFRA_GLOBGRPH pre-cron blockers — both FIXED + clean test PASS
02:00Z 2026-06-10 cron had FAILED the gate. Diagnosed + fixed:
- **Blocker 1 (AccessDenied):** ROOT-CAUSE CORRECTION — not 11 per-service perms; ~15 collectors all failed on ONE missing s3:ListBucket on opal-313476888478-terraform-state (tf_managed enrichment) + states:ListActivities. Fixed item2a.tf (TerraformStateRead + ListActivities), applied. Commit a674a4f7d.
- **Blocker 2 (Nessie tag 400):** createReference takes name+type as QUERY params, body=source ref (code had them in body). Fixed derive_runner.py.
- **Image build:** local Docker unreliable (Andrew-confirmed) -> built via CodeBuild (reused semantic-clustering project, source-override); Dockerfile base -> public.ecr.aws mirror (Docker Hub 429 fix). Commit bd38bf215. Memory: reference_docker_unreliable_use_codebuild_for_containers.
- **Clean test (ECS ef55cec9, exit 0):** 0 AccessDenied, nodes 359->1176, NESSIE_TAG_CREATED audit-baseline-2026-06-10. RAVC2-COMPLETE to COO+CTO. 02:00Z is now the official gate run.
- **New finding (non-gating):** transient Iceberg 409 commit-conflict on first run (concurrent item2b writer on my session's CloudTrail noise); retry clean. Recommend commit-retry/backoff follow-up.

## Carryover
- NFRA_COSTAWS AC5 (historical-prices cost tags): source committed c92c2fc2c, deploy deferred (validates next nightly).
- GLOBGRPH 02:00Z tonight: RAVC2 results to CVO for P1/Item-2a endorsement.
- Dedicated TF-managed globgrph CodeBuild project (vs reusing news project) = clean follow-up.
