# AE 0.7 /work cycle #2-sub — 2026-05-26 ~15:34Z — CDNCOHT TO-001 SHIP

**Agent:** 0.7.0_AE_CloudOps
**Trigger:** Off-cycle sub-tick spawn-from-RAVC2-ACCEPT (LEDGEH close 15:30Z → CDNCOHT start same turn per /work skill "manually OK after RAVC2-Accept to pick up next TO")
**Cycle outcome:** SUBSTANTIVE — 3 commits + tag + 2 terraform applies + CF invalidation + RAVC2-Request to ws COO

---

## TL;DR

CDNCOHT TO-001 implementation + deploy complete in single sub-tick post LEDGEH-CLOSE RAVC2-ACCEPT. ~30min wall RAVC2-ACCEPT-receive → CDNCOHT TO-001 ship complete. Tag `portal-auth-v1.16.1` pushed; CF invalidation InProgress.

Defense-in-depth Layer 2 (CDN edge) now structurally covered. 5-project ADHC defense-in-depth corpus: FECACHE_COHERENCE (Layer 1 FE) + CDNCOHT (Layer 2 CDN, THIS) + LEDGEH (Origin error envelope; now extended) + BPMVH + TRIGMRK (Phase 2 in-flight).

## Phase 1 compiler-mandate

| Tool | Output | Finding |
|---|---|---|
| `comp-iam service shared-advisor-router-response` | No service match | L@E not in comp-iam Lambda index (same as LEDGEH); IAM role unchanged expected |
| `comp-blast shared-advisor-router-response` | No downstream consumers | Terminal node; blast contained to 4 CF behaviors via existing TF wiring |
| `bun build --target=node` | 1 module, 1.39KB bundled | Handler syntax-clean |

## Phase 2 implementation

Handler refactor 65→70 LOC (`infra/aws/lambda-edge/shared-advisor-router-response/index.mjs`):
- `isArtifact` filter promoted to top (DRY: shared between success + error paths)
- `!isArtifact` → early-return unchanged (SPA deep-link preserved; LEDGEH AC2 invariant)
- SUCCESS PATH (status < 400, isArtifact): inject `Cache-Control: public, max-age=60, must-revalidate`
- ERROR PATH (status >= 400, isArtifact): existing LEDGEH envelope logic preserved verbatim

Behavioral equivalence: non-artifact paths unchanged ✓; artifact success now injects Cache-Control (intended) ✓; artifact error retains LEDGEH envelope ✓.

## Phase 3 deploy

| Step | Outcome |
|---|---|
| Source commit | `0a9c90b16` (31 ins / 26 del) |
| Build + S3 upload | `infra/aws/lambda/ci/build-nodejs-lambda.sh portal-auth shared-advisor-router-response`; SHA256 `lXR6VS/ZFToE3k62AhavrFdidXJtad87dcLgkUO5Q5A=` |
| Source-map commit | `be724538a` |
| Plan (Lambda) | `aws_lambda_function.shared_advisor_router_response` in-place; s3_object_version swap; new v2 publish |
| Apply 1 (Lambda) | `safe-apply.sh` HALTGT-gated; 6s; 0 added 1 changed 0 destroyed |
| Plan (CF) | `aws_cloudfront_distribution.portal` in-place; 4 `lambda_function_association` :1 → :2 |
| Apply 2 (CF) | `safe-apply.sh` HALTGT-gated; 1m20s; 0 added 1 changed 0 destroyed |
| 0-diff verify | "No changes. Your infrastructure matches the configuration." |
| Record deploy | `record-terraform-deploy.sh portal-auth`; bookkeeping commit `216dd8a45` (initial commit blocked on owned-paths stale git config = 0.4.0_DE; re-committed with safe-commit + correct author) |
| Tag | `portal-auth-v1.16.1` |
| Push | `git push --follow-tags origin CLOUD`; 4 commits + 1 tag |
| CF invalidation | `aws cloudfront create-invalidation --distribution-id EVTSA9VEHNZVH --paths /api/scoped/advisor-intelligence/*` → `ID31U80S1MI2V6UGFRQDWOCHAF` InProgress |

## AC closure

| AC | Status |
|---|---|
| AC1 (Cache-Control header verifiable post-deploy) | DEFERRED TO TO-VAL (L@E propagation wait + synthetic harness) |
| AC2 (T0/T0+30s/T0+90s `x-cache` sequence) | DEFERRED TO TO-VAL |
| AC3 (LEDGEH error-path regression preserved) | STRUCTURAL PASS (diff inspection) |
| AC4 (comp-iam unchanged) | PASS (L@E execution role reused) |
| AC5 (terraform plan 0-diff) | PASS (verified post-2nd-apply) |
| AC6 (L@E propagation wait ~15-30min) | IN-PROGRESS (started 15:33Z; verifiable 15:48Z+) |
| AC7 (CF invalidation `/api/scoped/advisor-intelligence/*`) | DONE (ID31U80S1MI2V6UGFRQDWOCHAF) |

## Project JSON + TO closure

- TO file: `<status>` pending → complete with `<shipped>` evidence stamp
- Project JSON: `status` `phase2_to001_interim_shipped_to001_dispatched_ae07_inflight` → `phase2_to001_shipped_VAL_pending`

## Pattern bank candidate

**Off-cycle sub-tick spawn-from-RAVC2-ACCEPT:** ~30min wall RAVC2-ACCEPT-receive (15:30Z) → next-TO ship complete (~16:00Z) including 2 production terraform applies + CF propagation start. Sister to [[feedback_spawn_with_direction_fast_orient_pattern]] worker-side fast-orient. /work skill spec explicitly permits this pattern: "Manually OK via `/work` for an off-cycle tick if needed (e.g., immediately after RAVC2-Accept to pick up next TO)". Confirmed empirical anchor.

## Next /work tick (cron *20m)

TO-VAL author + ship: consolidated `ADHC_CDNCOHT.VAL` covering both LEDGEH AC1 (error-path empirical regression) + CDNCOHT AC1/AC2 (success-path Cache-Control + age<60s revalidation). Gated on L@E propagation completion (~15:48Z+) + CF invalidation completion.
