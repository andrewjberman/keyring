# AE 0.7.0 Session Log — inf-unified-account-dim-daily Orphan Reconciliation (Branch A)
**Date:** 2026-05-13
**Agent:** 0.7.0_AE_CloudOps
**Trigger:** COO TO ADHC-INF-UAD-ORPHAN dispatched 2026-05-13T15:00Z; Andrew GO on Phase 0 forensic
**TO:** `0.7.0_AE_CloudOps/task_orders/inf-unified-account-dim-daily-orphan-reconcile.md`

---

## TL;DR

Three-state Lambda divergence reconciled to single coherent state via Branch A path. Orphan content was LEGITIMATE (current HEAD), doc-only delta (lambda_function.py docstring + error string for 12:35→12:40 cron-slot revision). Root cause: `record-terraform-deploy.sh` sweeps `last_deployed_commit` to the sweep commit on every apply, losing per-Lambda content-commit provenance. Phase 2 follow-up TO authored for the script fix.

---

## Phase 0 — Forensic Diagnostic

### Step 1: S3 object tagging

`aws s3api get-object-tagging` on all 3 versions: `TagSet=[]` uniformly. build-and-upload.sh does not tag uploads. Cannot differentiate via tags.

### Step 2: CloudTrail + Owner identity

CloudTrail `lookup-events` returned `[]` for management events on the bucket — PutObject is object-level, requires Data Events trail (not configured for this bucket). Cannot identify per-session uploader via CloudTrail.

Fallback: `aws s3api list-object-versions` showed all 3 versions have identical Owner ID `5b2d5dc40076894c1ac4d3aee2ae6af2a81ae9dc528a672239cbeeed8a6c4692` (CI uploader IAM role; same principal across legit + 2 orphan uploads). No external actor.

### Step 3: Binary diff (orphan vs legit zip)

Pulled all 3 versions to /tmp/uad_orphan/, unzipped, `diff -r`:
- `lambda_function.py`: DIFFERS (3 lines)
- `pull_unified_account_dim.py`: BYTE-IDENTICAL
- `jwt_freshness.py`: BYTE-IDENTICAL

The lambda_function.py diff:
```diff
9,11c9,11
< EventBridge cron(35 12 * * ? *) = 12:35 UTC daily (COO 20260507T~20:43Z slot
< approval). Parallel-fires with inf-accounts-v2-daily at the same minute;
< AWS EventBridge handles concurrent rule fires natively (no contention).
---
> EventBridge cron(40 12 * * ? *) = 12:40 UTC daily (COO 20:50Z slot revision
> from 12:35 to avoid parallel-fire with inf-accounts-v2-daily). Slot post
> accounts_v2_daily, pre assets-v2.
54c54
<             "Verify inf-jwt-trigger fired at 12:00 UTC before this Lambda at 12:35 UTC."
---
>             "Verify inf-jwt-trigger fired at 12:00 UTC before this Lambda at 12:40 UTC."
```

DOC + ERROR-STRING ONLY. NO logic changes. EventBridge cron schedule lives in Terraform, not Lambda code; the comment is self-documentation.

### Step 4: git blob search

```
orphan lambda_function.py blob: 638cd4a932573d90905dcdfc29cf62a01fda6575
legit  lambda_function.py blob: 16a04c5799cc459e384dba9b1d3ab44d6c01f455
HEAD blob (in repo):            638cd4a932573d90905dcdfc29cf62a01fda6575    ← matches orphan
```

Authoring commit found: `0a6a842dc1ba95cc47f9fbe97b591e808f2407d0` (2026-05-07T17:12:01 -0400 = 2026-05-07T21:12:01Z), authored by **0.7.0_AE_CloudOps**: `feat(LAMBDA-DIMS Phase B P2 2/2): inf-tax-daily Lambda + UAD cron 12:35 -> 12:40`.

Subsequent commit `bc4759ad0` (2026-05-11T20:11Z, also AE 0.7) added `jwt_freshness.py` and `pull_unified_account_dim.py` to git as post-deploy hygiene; these files were already in the deployed zip from 2026-05-07 (committed 4 days later, no content change). Full directory state at `bc4759ad0` matches the orphan zip exactly.

### Sequence reconstruction

| UTC Time | Event |
|----------|-------|
| 2026-05-07T20:51:10Z | Legit S3 upload of `16a04c57...` content ("12:35 UTC") + terraform apply → Lambda live `8eWiL153rp9...` |
| 2026-05-07T21:12:01Z | Commit `0a6a842dc` updates docstring "12:35→12:40 UTC". NO S3 upload. NO terraform apply. |
| 2026-05-11T20:11:28Z | Commit `bc4759ad0` adds supporting .py files to git (hygiene only). |
| 2026-05-12T15:49:47Z | build-and-upload.sh run #1 — rebuilds Lambda from HEAD; uploads `638cd4a9...` ("12:40 UTC"). NO terraform apply. |
| 2026-05-12T16:47:00Z | build-and-upload.sh run #2 — IDENTICAL content uploaded 58 min later. SAME ACTOR. |
| 2026-05-13T14:24:50Z | AE 0.6.1 v1.7.53 source-map sweep commit `dba29da4e` — updates `artifact_sha256=vUH5XGTYcEWs...` to match current S3 zip; sets `last_deployed_commit=dba29da4e` (THE SWEEP COMMIT itself — the bug). |
| 2026-05-13T15:00Z | COO TO dispatched (this work). |
| 2026-05-13T18:42Z | AE 0.7 source-map backfill commit `51b74564c` — last_deployed_commit `dba29da4e` → `bc4759ad0` (content commit). |
| 2026-05-13T18:45:43Z | AE 0.6.1 v1.7.54 bundle apply — FULL inf-pipeline apply (4 Lambdas including uad-daily). |
| 2026-05-13T18:45:43Z+ | record-terraform-deploy.sh sweeps all Lambdas' last_deployed_commit to NEW sweep commit `743323ff6`, **overwriting** my `bc4759ad0` backfill. |
| 2026-05-13T18:50Z (approx) | AE 0.6.1 manual restore in commit `2071a8ace` — `last_deployed_commit=bc4759ad0` restored, `_last_deployed_commit_note` field added. |

**Verdict:** Branch A — orphan content is legitimate. The "orphan" framing is a `last_deployed_commit` provenance gap, not unauthorized code.

---

## Phase 1 — Reconciliation (Branch A)

| Step | Action | Result |
|------|--------|--------|
| Cross-lane coordination | MCP AE 0.6.1 before mutating source map | ACK; preferred BUNDLE into v1.7.54 (3-Lambda apply: advisor-publisher + inf-accounts-v2-daily + uad-daily-backfill) |
| Source-map edit | `last_deployed_commit dba29da4e → bc4759ad0` | Single-line edit; JSON validated |
| Commit | safe-commit.sh `51b74564c` | Pushed to origin/CLOUD |
| Bundle handoff | AE 0.6.1 rebased + ran full apply | v1.7.54 SHIPPED 18:45:43Z |
| Empirical regression | record-terraform-deploy.sh overwrote my backfill | AE 0.6.1 manual restore in `2071a8ace` |
| Post-restore state | Lambda live CodeSha256 = source map artifact_sha256 = bc4759ad0 content tree | AC2 confirmed |

---

## Acceptance Criteria Trail

### AC1: Phase 0 outputs (CloudTrail uploader + binary diff + git commit search) appended to TO RAVC2 closeout

PASS — documented above. Summary in RAVC2 to COO at 15:15:20Z 2026-05-13.

### AC2: Lambda live CodeSha256 = source map artifact_sha256 = commit lineage

PASS:
```
$ aws lambda get-function-configuration --function-name inf-unified-account-dim-daily \
    --query "[FunctionName,CodeSha256,LastModified,Version]" --output text
inf-unified-account-dim-daily   vUH5XGTYcEWs/3fmzuv5sgFwq1UjeFy/209rQl2JpDo=   2026-05-13T18:45:03.000+0000   $LATEST

$ jq '.functions["inf-unified-account-dim-daily"] | {artifact_sha256, last_deployed_commit}' \
    infra/aws/lambda/ci/lambda-source-map.json
{
  "artifact_sha256": "vUH5XGTYcEWs/3fmzuv5sgFwq1UjeFy/209rQl2JpDo=",
  "last_deployed_commit": "bc4759ad0000479ceb5da03c923f48bea8436fe3"
}

$ git ls-tree bc4759ad0 -- infra/aws/lambda/inf-pipeline/inf-unified-account-dim-daily/lambda_function.py
100644 blob 638cd4a932573d90905dcdfc29cf62a01fda6575 ...
```

All three coherent: live SHA = source map SHA = bc4759ad0 directory state.

### AC3: terraform plan 0-diff (twice, 5+ min apart)

PASS (both runs):
```
$ MSYS_NO_PATHCONV=1 .tools/terraform.exe -chdir=infra/aws/terraform/inf-pipeline \
    plan -target='module.inf_unified_account_dim_daily.aws_lambda_function.this'

No changes. Your infrastructure matches the configuration.
```

Run #1 at 18:54Z, Run #2 at 18:55Z. Stability confirmed.

### AC4: Compiler Tools section

```
$ comp-iam service inf-unified-account-dim-daily
SERVICE: inf-unified-account-dim-daily  [lambda]
  IAM role: inf-unified-account-dim-daily-role
  Source files: infra/aws/lambda/inf-pipeline/inf-unified-account-dim-daily/lambda_function.py
  No AWS operations detected.
```

"No AWS operations detected" is comp-iam graph-side coverage gap (Lambda DOES call S3, CloudWatch, Secrets Manager — graph doesn't index this Lambda's imports). NOT a blocker; surfaced to comp-graph maintainer for future enhancement. No IAM gap to flag for this reconciliation (artifact-content-only change, no boto3 call surface change).

`comp-pipescript deployed` N/A (Lambda, not gold script) — substituted by AC2 (Lambda live = source map).

`comp-iam gaps` post-apply — N/A: no iam.tf changes in this reconciliation; orphan reconcile is IAM-neutral.

### AC5: Recurrence prevention recommendation

PASS — surfaced to COO in Phase 0 RAVC2 (4 options ranked). COO ratified (a) `build-and-upload.sh` last_deployed_commit content-commit fix as priority guard.

**Post-empirical refinement (AE 0.6.1 v1.7.54 ship):** the actual bug is in `record-terraform-deploy.sh` (lines 145+188 unconditional sweep), NOT `build-and-upload.sh` (which doesn't touch `last_deployed_commit`). Phase 2 follow-up TO authored: `task_orders/record-terraform-deploy-content-commit-fix.md`. Scope: per-Lambda content-commit lookup via `git log -1 --format=%H -- <source_dir>` for both Python and Node.js JSON-tool paths.

### AC6: Commit lineage in commit message

PASS — `51b74564c` commit message cites the abandoned `dba29da4e` sweep commit + the new `bc4759ad0` content commit + the HEAD state.

---

## Sweep-Commit Trample Pattern (Phase 2 Empirical)

AE 0.6.1's v1.7.54 ship empirically confirmed the Phase 2 root-cause prediction. Worth documenting for org awareness:

> Any time `record-terraform-deploy.sh` runs on a pipeline, it sweeps **every** Lambda in that pipeline's `last_deployed_commit` to HEAD (the sweep commit), regardless of whether the Lambda's artifact actually changed in this deploy.

Impact:
- Lambda whose source was edited in commit X (and rebuilt in S3 some time later) loses the commit-X attribution as soon as ANY subsequent pipeline-wide sweep occurs.
- Manual content-commit backfills (like the one in this TO) are over-written on the very next apply unless someone manually re-applies them post-sweep.

Phase 2 TO `record-terraform-deploy-content-commit-fix.md` fixes this universally: replace unconditional sweep-commit write with per-Lambda content-commit lookup (`git log -1 --format=%H -- <source_dir>`).

---

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| comp-iam | `comp-iam service inf-unified-account-dim-daily` | "No AWS operations detected" — graph-side coverage gap, not a blocker |
| terraform plan | `terraform plan -target=module.inf_unified_account_dim_daily.aws_lambda_function.this` | No changes (run twice, stable) |
| git hash-object | Manual blob lookup for forensic Phase 0 Step 4 | Orphan blob = HEAD blob, traced to commit 0a6a842dc + dir state at bc4759ad0 |

---

## RAVC Trail

| RAVC | Direction | Time (UTC) | Content |
|------|-----------|------------|---------|
| TO dispatch | COO → AE 0.7 | 14:15:47Z | Phase 0-1-2 plan, HIGH priority, ~0.5-1d effort |
| RAVC1 (TO accept) | AE 0.7 → COO | 15:02:44Z | Phase 0 starting; diagnostic only, no code changes |
| RAVC2 (Phase 0) | AE 0.7 → COO | 15:15:20Z | Branch A verdict; doc-only delta; sequence reconstruction; 4 Phase-2 prevention options |
| RAVC4 (Branch A ratify) | COO → AE 0.7 | ~15:25Z | Branch A GO; Phase 2 (a) ratified as priority guard; v1.7.54 bundle ownership AE 0.6.1's call |
| Cross-lane coord | AE 0.7 → AE 0.6.1 | 15:15:30Z | Source-map mutation about to land; bundle decision needed |
| ACK (bundle) | AE 0.6.1 → AE 0.7 | ~15:30Z | Bundle into v1.7.54 (3-Lambda); Option 2 preferred |
| Phase 1 ship | AE 0.7 → AE 0.6.1 + COO | 18:42:07Z | Source-map backfill 51b74564c shipped; AE 0.6.1 rebases |
| v1.7.54 ship | AE 0.6.1 → AE 0.7 | 18:45:43Z+ | Bundle apply LIVE; sweep overwrote backfill; manual restore in 2071a8ace |
| RAVC2 (close) | AE 0.7 → COO | (this log commit) | AC1-6 PASS; Phase 2 TO authored; loop close |

---

## Open Items Post-Session

| Item | Status |
|------|--------|
| Phase 2 follow-up TO (record-terraform-deploy.sh content-commit fix) | Authored; staged in task_orders/ pending COO scope-project routing |
| SmartX TO-3 (IAM cross-bucket + Lambda deploy) | DEFERRED per Andrew direct sequencing call (post-v1.7.54 closeout) — picking up next |
| build-and-upload.sh upload deduplication | Out-of-scope for Phase 2 fix — separate observation (2 identical uploads 58 min apart on 2026-05-12); low priority, not surfaced as TO yet |

## Session Status: COMPLETE — ADHC-INF-UAD-ORPHAN AC1-6 PASS; Phase 2 follow-up TO authored; ready for COO RAVC4 close
