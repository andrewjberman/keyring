# NFRA_INFRPT.P1 increment-2a -- DEPLOY DRIFT section (in-Lambda half-landed-deploy detection) (0.7.0_AE_CloudOps~B)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DEPLOY, DIAGNOSE

Window: since the inc-1 log (d7209ece9). Lane: 0.7.0_AE_CloudOps~B.

## Current State

NFRA_INFRPT.P1 increment-2a is DEPLOYED + in-Lambda-verified (tag `shared-infra-v1.24.0`, pushed). The infra report now has a DEPLOY DRIFT section.

- **`check_deploy_drift()`** (`infra/aws/lambda/infrastructure_monitor/lambda_function.py`): pure-AWS half-landed-deploy detection, NO repo source-map. Lists `opal-313476888478-lambda-artifacts`, maps each `{pipeline}/{fn}.zip` by basename to a function, compares the artifact's `content-sha256` S3 object metadata (set by build-and-upload) vs the deployed `CodeSha256` (from `list_functions`). DIRECTION-classified: artifact NEWER than the function = `half-landed` (uploaded-not-applied -> the NEVER-leave-a-deploy-half-landed signal; NEW->RED, standing->WATCH); artifact OLDER = `deployed-ahead` (stale artifact / possible out-of-band non-TF deploy -> WATCH, never RED). NEW-vs-prior-report state-change via `_load_prior_report()` (newest archive). Helpers `_parse_lambda_lm`. Wired into handler (`report["sections"]["deploy_drift"]`), `format_report` (action-first render), `send_email` (NEW half-landed -> RED -> alert).
- **IAM**: `MonitorDataFreshnessRead` extended with `MonitorArtifactBucketList` (s3:ListBucket) + `MonitorArtifactObjectRead` (s3:GetObject) on `opal-313476888478-lambda-artifacts`. comp-iam gaps 0 missing.
- Deployed sha `fNCp/d0AQNewCQ7csXGNqgZIY1f/+R80tkmC8WbSQYw=` (24K). safe-apply 0 add / 2 change / 0 destroy, 0-diff.

**In-Lambda verify (archive `infrastructure/reports/2026-06-17/15-39-19.json`, deployed IAM, async invoke):** checked 129, MATCH-ON-CLEAN 127/129 (no AccessDenied false-flag-all -> artifact-read IAM works in the role), MISMATCH-FIRES 1 half-landed RED + 1 deployed-ahead WATCH. The §F fix also confirmed in-Lambda (AI error-analysis log-fetches ran with no "Invalid character in term *"). Lambda runs ~103s (> the CLI 60s read-timeout -> the sync-invoke retry-storm root cause; used `--invocation-type Event` + archive-read this time).

**Real finding (candidate stranded deploy):** `opal-portal-volatility-fetcher` = HALF-LANDED candidate. In the source-map at the canonical key `market-overview/opal-portal-volatility-fetcher.zip` (rules out benign different-key). Artifact dated 2026-03-24 but the deployed function `LastModified` = 2026-02-23 -> ~85d-old artifact, 29d newer than running code, never applied. (a) content-only-rebuild / (c) intentional-rollback need owner confirm. SECONDARY: source-map `last_deployed_at=2026-06-03` contradicts the function's actual 2026-02-23 = a stale source-map record. Routed to the market-overview/volatility-fetcher owner (AE/DT lane) for adjudication; not urgent (85d). `opal-partners-data` = deployed-ahead WATCH (93d stale artifact).

## Deployment Sequence (AE)

ds-commit-gate (clean) -> safe-commit (8a7d63459) -> build-and-upload.sh shared-infra (sha fNCp/d0...) -> source-map commit (83afb3143) -> terraform plan (0 add/2 change/0 destroy) -> RAVC1 to CTO+COO (binding pair proven locally) -> safe-apply (0 add/2 change/0 destroy) -> 0-diff -> record-terraform-deploy shared-infra-v1.24.0 -> tag -> push --follow-tags (c6e0426c1 + tag) -> async invoke (Event) -> read archive 15-39-19.json (in-Lambda binding-pair re-confirm).

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-manifest-check | `list` | PASS | oriented: it's the GRAPH-CALL-manifest checker (Rule 20), NOT lambda-source-map -- the TO naming conflation; informed the 2b producer design |
| comp-surface-check | `list` | PASS | 5 critical surfaces (SEV1/2); the commit-time leg (runtime D8 scan is base-AE's, not double-owned) |
| comp-iam | `gaps` | PASS | 0 missing after the artifact-bucket read grant |
| ds-commit-gate.sh | lambda_function.py (x3) | PASS | py_compile + AST + ruff clean each edit |
| build-and-upload.sh | `shared-infra opal-infrastructure-monitor` | PASS | dep-free 2-file zip |
| safe-apply.sh | `-chdir=shared-infra apply` | PASS | HALT-gate passed; 0 add/2 change/0 destroy |

**What worked:** the local-then-in-Lambda binding-pair test (CTO's required check) decisively ruled out the SHA-format false-positive (127/129 match) AND Phase-3 surfaced the direction-semantics refinement (artifact-newer=half-landed vs artifact-older=deployed-ahead) that prevents stale artifacts false-RED-ing. The async-invoke + archive-read verify avoided a second retry-storm. **What failed:** none. **Gap:** 3 of the 4 DRIFT sources (comp-manifest/comp-surface/terraform-plan) can't run in-Lambda -> 2b needs a CI/nightly producer (designed, GO'd).

## Blockers

None. Increment-2b (producer-backed drift) is GO'd; I'm RAVC1-ing the producer mechanism before building (a real infra-architecture sub-decision: tf-plan-in-CI creds).

## Next Steps

- **[0.7.0_AE_CloudOps~B]** increment-2b: CI-on-push comp-manifest + comp-surface -> drift_state.json on S3 + nightly terraform-plan-drift leg + MANDATORY drift_state-age staleness line + Lambda render. RAVC1 the producer mechanism first (tf-plan-in-CI creds vs minimal scheduled fallback, no new EC2).
- **[0.7.0_AE_CloudOps~B / market-overview owner]** Adjudicate `opal-portal-volatility-fetcher`: is the 2026-03-24 artifact a true stranded deploy (apply it) or intentional (record the hold)? + reconcile the stale source-map `last_deployed` record.
- **[2.0.0_SA_COO / 1.0.0_SA_CTO]** inc-2a RAVC2 acceptance.

## Files Modified

See commit messages: `8a7d63459` (deploy-drift section + artifact-read IAM), `83afb3143` (source-map), `c6e0426c1` (record deploy + CHANGELOG).
