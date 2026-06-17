# DRIVE -- DRIFT iterate: over-report 10 -> precise 5 via 2 accuracy fixes (0.7.0_AE_CloudOps~B)

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE, VALIDATE

Window: COO /drive GO (184952Z) -> the DRIFT-section continuation. Lane: 0.7.0_AE_CloudOps~B.

## Current State

COO /drive directed working the DRIFT findings actively (fabric flagged idle). Worked the 10 terraform-drift findings -> the section was OVER-REPORTING; I diagnosed + landed 2 accuracy fixes -> it's now PRECISE (5 real). NFRA_INFRPT.P1 TO flipped COMPLETE (COO/CVO /to-check); the DRIFT iterate rides as follow-on.

ADJUDICATION METHOD: re-ran each flagged module's `terraform plan` LOCALLY (locked providers) to ground-truth real-vs-noise (vs trusting the CI plan). This surfaced the two accuracy bugs.

TWO ACCURACY BUGS (both fixed):
1. **Unlocked-provider false-drift** (CTO's fix, 19ccf2e37): the GH-Action zip excluded `.terraform.lock.hcl` -> CodeBuild `terraform init` resolved UNLOCKED/latest providers -> recompute false-drift (yang clean-locally, drift-in-CI; fresh source.zip -> same, proving not stale-source). Fix: keep lock files in the zip. (Caveat: per-platform lock hashes -- if a module's lock lacks linux_amd64, CI re-fetches; durable fix `terraform providers lock -platform=linux_amd64`.)
2. **Lambda s3_object_version churn** (my fix, b2d98f10b): terraform tracks s3_object_version, which churns when an artifact is re-uploaded with IDENTICAL content (build-and-upload makes a new S3 version even byte-identical) -> `aws_lambda_function [update]` with source_code_hash UNCHANGED = cosmetic, not real. drift_producer now skips Lambda updates where before.source_code_hash == after.source_code_hash (cross-corroborated by the deploy-drift sha-check). Empirical: smartx 3 lambdas' deployed CodeSha256 == artifact sha (08Ksq6Ow/MCsLEpIg/SnPiO8B8) -> were false-drift.

RESULT (accurate run 8429d78b, both fixes live): 10 -> 5 real. Dropped-as-false (pure version-churn): data-refresh, deck-generation, market-overview, partners-api, portfolio-management. The 5 real:
- exec-summary: REAL config (event_rule trigger->placeholder rename, committed-not-applied; confirmed locally) -> route owner.
- news-pipeline: REAL code (ai_sentiment + semantic_clustering source_code_hash drift = deployed-code != artifact) -> route owner.
- ycharts-pipeline: REAL code (ycharts_session_capture source_code_hash drift) -> route owner.
- smartx-pipeline: now ONLY aws_instance.smartx_exporter tags (3 lambdas correctly dropped) -- MINE, held: the reconcile DROPS deployed Pipeline=smartx/Project=smartx for default_tags OpalPortal = a default_tags-migration intent-check (cost-allocation), deliberate.
- yang-pipeline: only aws_sfn_state_machine [update] but CLEAN LOCALLY -> likely platform-serialization residual (per-platform lock caveat), low-confidence -> owner-confirm.

bd-pipeline cannot-assess = SS4c canary committed-before-apply (gldinc-ss4c-canary.zip not uploaded), INTENTIONAL gated state (0.6.0_AE owns; deploy_ledger clean) -- detection correct, dispositioned not-a-violation. Coverage held 66% -- the 10 cannot-assess are REAL config/var errors (lock-fix did NOT clear them), not provider-noise -> per-module continuation.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| terraform plan (local) | per-module (exec-summary/smartx/yang/bd) -lock=false | PASS | the real-vs-noise ground-truth (locked providers); found the 2 accuracy bugs |
| ds-commit-gate.sh | drift_producer.py | PASS | version-churn suppression clean |
| gh workflow run / codebuild start-build | drift-producer-push.yml dispatch + CodeBuild | PASS | accurate-drift re-run (both fixes) |

**What worked:** LOCAL plan re-run (locked providers) as the adjudication oracle (vs trusting CI) -- it caught BOTH the unlocked-provider false-drift AND (via the deploy-drift sha cross-check) the version-churn false-drift. The 2 fixes narrowed 10->5 precisely. **What failed:** the lock-fix did NOT clear the cannot-assess (so those are real config/var errors). **Gap:** coverage 66% (the 10 cannot-assess per-module config/var errors) + yang's possible platform-serialization residual = the continuation.

## Blockers

None. The DRIFT-precision work is done. Coverage continuation (cannot-assess per-module) is iterate-on-the-run; the guard honestly reports 66% meanwhile.

## Next Steps

- **[exec-summary / news / ycharts owners, via COO]** Reconcile the 3 real code/config drifts (apply-or-investigate).
- **[0.7.0_AE_CloudOps~B]** smartx EC2 default_tags-migration intent-check (deliberate); the coverage continuation (cannot-assess per-module: var-provision for var-requiring modules, the ec2.tf function error); yang providers-lock -platform=linux_amd64 if confirmed quirk. Deliberate queue: volatility-fetcher+partners, deploy-role OIDC hardening, comp-baseline-in-CI. Standing: GCONTR TO-3.

## Files Modified

See commit messages: `b2d98f10b` (version-churn suppression). CTO's lock-fix `19ccf2e37` + workflow_dispatch `c1a8aed6c` (BASE_EXEC).
