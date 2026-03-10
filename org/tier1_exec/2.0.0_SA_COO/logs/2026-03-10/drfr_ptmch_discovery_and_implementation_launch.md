# DRFR_PTMCH Discovery Thread + Phase 1 Implementation Launch — 2.0.0_SA_COO

**Date:** 2026-03-10
**Start Time:** 19:30
**End Time:** 22:00

## Objective

Drive DRFR_PTMCH (Portal Time Machine) from Phase 0 (research dispatched) to Phase 2
(implementation code complete, Phase B deploy gated on CloudOps CF audit). Run DRFR_PTMCH-001
discovery thread, absorb CLI facts from Andrew, issue corrected implementation task orders,
and coordinate three AEs through Phase A delivery.

---

## Work Completed

### 1. Governance correction: CTO-issued task orders (pre-session)

Three task orders (DRFR_PTMCH.001) had been issued by 1.0.0_SA_CTO directly to the AE agents.
This is a protocol violation -- CTO issues PRDs, COO issues task orders. Task orders marked
superseded, work absorbed into the discovery thread. Protocol enforced going forward.

### 2. Thread DRFR_PTMCH-001 -- AE discovery (Pattern 2, 3 AEs)

| Field | Value |
|-------|-------|
| Thread ID | DRFR_PTMCH-001-portal-time-machine-ae-infrastructure-di |
| Participants | 0.7.0_AE_CloudOps, 0.5.0_AE_OpalETL, 0.6.0_AE_PartnerETL |
| Model | gpt-5.2, tools enabled |
| Turns | 2 per agent (6 total) |
| Status | COMPLETE |

Key repo-confirmed findings from thread:
- `yang-ingest-dynamodb` writes to DynamoDB table `opal-portal-market-data` -- portal reads at runtime (Market Overview)
- `yang-refresh-fred-cache` writes to `cache/fred/` -- NOT under `json/`, NOT captured by archive
- `yang-capture-output-versions` runs on every execution per Step Functions definition
- BD publisher source path is env-var backed (`INPUT_BUCKET`, `OUTPUT_BUCKET`)

### 3. CLI audit (Andrew ran four commands)

| Command | Result |
|---------|--------|
| `get-bucket-versioning opal-data-portal-v2` | `"Status": "Enabled"` |
| `get-bucket-versioning opal-data-bd` | `"Status": "Enabled"` |
| Archive manifest spot-check (exec 7a407b33) | 83 files, all versionIds non-null |
| DynamoDB PITR on `opal-portal-market-data` | ENABLED, 35-day window, earliest ~2026-02-13 |

**Major PRD correction:** opal-data-bd versioning already enabled -- PRD's snapshot archive
approach (copy `gold/` to `snapshots/{date}/`) is unnecessary. Both layers use same
version-restore pattern. Significant implementation simplification.

### 4. Phase 1 task orders issued (P1, P2, P3)

Initial task orders issued, then revised after agent review surfaced three corrections:

| Correction | Agent | Issue |
|-----------|-------|-------|
| IAM scope | CloudOps | Task order said yang-pipeline/iam.tf -- wrong. Each pipeline AE owns their own IAM. CloudOps P1 scoped to lifecycle rules + CF audit only. |
| S3 trigger impossible | PartnerETL | Two S3 notification rules with same prefix+suffix not allowed. bd-capture-output-versions must be Lambda-to-Lambda fan-out from bd-portal-publisher. |
| News publisher path | OpalETL | Correct path is `infra/aws/lambda/semantic-trending-topics-portal-publisher/` not `news-pipeline/` subdirectory. |
| pkl_version source | OpalETL | Must read `manifest.json` not `metadata.json` to rebuild LATEST.json. |
| Dedicated IAM roles | PartnerETL | Option A (new bd-capture-versions-lambda-role + bd-time-machine-lambda-role) confirmed over extending shared publisher role. |

All three task orders revised and committed at `1fbda5f8`.

### 5. Phase A execution -- all three AEs delivered

| Agent | Deliverable | Commit |
|-------|------------|--------|
| 0.7.0_AE_CloudOps | Lifecycle rules deployed (opal-data-portal-v2 + opal-data-bd), CF audit complete | `37661a18`, tag `shared-infra-v1.4.0` |
| 0.5.0_AE_OpalETL | yang-time-machine Lambda + DataRefresh endpoints code, news-v2.7.0 deployed | `5ce67698`, `08e3e981` |
| 0.6.0_AE_PartnerETL | bd-capture-output-versions + bd-time-machine + publisher fan-out, IAM roles | `b3207410` |

### 6. CloudFront invalidation path correction

AE7's CF audit (CloudOps P1 req 3) revealed the yang invalidation path is NOT `/api/public/*`
(PRD assumption) -- it is `/api/general/*`. BD is `/api/scoped/advisor-intelligence/*`.

| Layer | Correct invalidation path |
|-------|--------------------------|
| Yang (Layer 1) | `/api/general/*` |
| BD (Layer 2) | `/api/scoped/advisor-intelligence/*` |

OpalETL's yang-time-machine Lambda had `['/*']` as placeholder. COO patched to
`['/api/general/*']` in this session before Phase B deploy.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Snapshot archive approach superseded | opal-data-bd versioning already enabled. Version-restore is simpler and already works. |
| IAM owned by each pipeline AE | CloudOps shouldn't have cross-pipeline IAM scope. Cleaner separation. |
| bd-capture fan-out via Lambda-to-Lambda | S3 notification rule constraint (two rules same filter not allowed). Same proven pattern as advisor-publisher. |
| FRED cache as explicit exception | cache/fred/ not under json/, not captured. Accepted exception for Phase 1. |
| `/api/general/*` not `/*` for yang invalidation | Precise invalidation. Avoids unnecessary BD cache flush on yang-only restores. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/projects/DRFR_PTMCH.json` | Phase updated to Phase 2, CF paths recorded, phase_b_gate set | This session |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/DRFR_PTMCH.P1.*` | Revised: IAM removed, lifecycle + CF audit only | `1fbda5f8` |
| `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/DRFR_PTMCH.P2.*` | Revised: path fix, pkl fix, role confirmed, go-ahead | `1fbda5f8` |
| `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/DRFR_PTMCH.P3.*` | Revised: S3 trigger corrected, dedicated roles confirmed | `1fbda5f8` |
| `infra/aws/lambda/v2_portal/yang_pipeline/outputs/yang-time-machine/lambda_function.py` | CF invalidation paths patched to `/api/general/*` | This session |

---

## Task Order Dispatch

| Agent | Task Order | Status |
|-------|-----------|--------|
| 0.7.0_AE_CloudOps | DRFR_PTMCH.P1 | COMPLETE -- shared-infra-v1.4.0 deployed |
| 0.5.0_AE_OpalETL | DRFR_PTMCH.P2 | IN PROGRESS -- code committed, news-v2.7.0 deployed, yang-pipeline + data-refresh deploy gated on Phase B |
| 0.6.0_AE_PartnerETL | DRFR_PTMCH.P3 | IN PROGRESS -- Phase A committed (b3207410), bd-pipeline apply gated on Phase B |

Execution dependencies:
  CloudOps P1 COMPLETE -> OpalETL P2 Phase B (yang-pipeline + data-refresh apply)
  CloudOps P1 COMPLETE -> PartnerETL P3 Phase B (bd-pipeline apply)
  OpalETL P2, PartnerETL P3 (parallel, no blocking between them)

---

## Blockers

None. CloudOps P1 is complete. OpalETL P2 and PartnerETL P3 Phase B are unblocked.

---

## Current State

**Status:** IN PROGRESS
**Active branch:** CLOUD

Phase A fully delivered by all three AEs. CloudOps P1 complete (shared-infra-v1.4.0).
OpalETL code committed (5ce67698). PartnerETL Phase A committed (b3207410).
COO patched yang-time-machine CF invalidation paths to `/api/general/*` (was `/*` placeholder).
Phase B (terraform apply for yang-pipeline + bd-pipeline) is unblocked -- AEs should proceed.

---

## Next Steps

1. **[0.5.0_AE_OpalETL] Phase B** -- build-and-upload.sh for yang-time-machine, terraform apply
   yang-pipeline (tag yang-v2.2.0), terraform apply data-refresh (tag data-refresh-v2.1.0).
   Use CF path `/api/general/*` confirmed by CloudOps P1 findings (already patched by COO).

2. **[0.6.0_AE_PartnerETL] Phase B** -- build-and-upload.sh for bd-capture-output-versions,
   bd-time-machine, bd-portal-publisher (fan-out change). Terraform apply bd-pipeline.
   Tag bd-v2.18.0.

3. **[2.0.0_SA_COO] Phase 4 task orders** -- after P2 + P3 Phase B complete, issue
   portal-time-machine orchestrator Lambda task order to OpalETL and DataRefresh frontend
   task order to 0.3.0_DE_TradingOperations + RD for HistoryTab Time Machine control.

4. **[2.0.0_SA_COO] Market Overview time travel** -- DynamoDB PITR is enabled (35-day window).
   Decide with Andrew: scope Market Overview into Time Machine via DAILY# re-publish path,
   or explicitly descope for Phase 1 and document "Market Overview always shows current data."

**Do NOT:**
- Use `/*` for yang CloudFront invalidation -- use `/api/general/*` (already patched)
- Implement BD snapshot archive pattern -- versioning + version-restore is the approach
- Modify `yang-capture-output-versions` capture window in this phase
