# Portal Time Machine — Project Registration and PRD — 1.0.0_SA_CTO

**Date:** 2026-03-10

## Objective

Register and scope the Portal Time Machine project (DRFR_PTMCH). Andrew wants to replace
the unfinished per-execution rollback button in DataRefresh/HistoryTab with a full
portal-wide "time machine" that can restore every data source to 5pm ET on a given date.
This session produces the research PRD, project registration, and AE discovery task orders.

---

## Work Completed

### 1. Architecture Research

Read the full DataRefresh pipeline end-to-end before writing the PRD:

| Component | Key Finding |
|-----------|-------------|
| `yang-move-to-processed` | PKL files copied to `benchmarks/data_{version}.pkl` with canonical version naming |
| `yang-generate-latest` | Overwrites `benchmarks/LATEST.json` pointer on each run |
| `yang-capture-output-versions` | Scans `json/` for files modified in last 10 min, records S3 versionIds to `data-refresh/archive/{execId}/outputs-manifest.json` |
| `handle_rollback` in `opal-data-refresh-api` | Two paths: version-based (preferred, uses versionIds) and re-processing (fallback, re-runs pipeline from archived PKLs) |
| `bd-portal-publisher` | Writes to `opal-data-bd/gold/` — no versioning, no snapshot, overwrite-in-place |
| `semantic-trending-topics-portal-publisher` | Reads DynamoDB `semantic-news-trending-daily` keyed by date — inherent time machine, no S3 restore needed |

**Critical unconfirmed dependency**: The version-based rollback path depends on S3 versioning
being enabled on `opal-data-portal-v2`. The `capture-output-versions` Lambda captures
versionIds but if versioning is off, every versionId is null and the restore is impossible.
This is the single most important fact to confirm before any implementation.

### 2. Project Registration

- Created `DRFR_PTMCH` using existing `DRFR` macro code (DataRefresh surface area)
- Added row to `org/projects/REGISTRY.md`
- Created `org/projects/DRFR_PTMCH.json`

### 3. PRD Written

`docs/architecture/DRFR_PTMCH_PRD.md` — research PRD covering:
- Architecture inventory (yang, BD, news, FRED, market-overview)
- Time Machine design hypothesis (4 layers, different mechanisms per pipeline)
- Precise open questions for each AE (what must be confirmed before implementation)
- Post-discovery implementation phases

### 4. AE Task Orders Issued

| Agent | Task Order | Primary Question |
|-------|------------|-----------------|
| `0.7.0_AE_CloudOps` | `DRFR_PTMCH.001.cloudops-versioning-iam-audit.md` | Is S3 versioning enabled? CloudFront routing? IAM gaps? DynamoDB PITR? |
| `0.5.0_AE_OpalETL` | `DRFR_PTMCH.001.opal-pipeline-archive-audit.md` | Are versionIds non-null in archive? yang-ingest-dynamodb scope? FRED/market-overview paths? |
| `0.6.0_AE_PartnerETL` | `DRFR_PTMCH.001.bd-pipeline-snapshot-audit.md` | BD gold/ size? rebuild cadence? snapshot cost? publisher parameterization? |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Research PRD first, implementation PRD after AE findings | The most important architectural question (S3 versioning status) cannot be answered from the codebase alone — requires live AWS audit. Writing implementation code before confirming this would be wasted work if versioning is off. |
| Three-AE dispatch, no dependency ordering | CloudOps and OpalETL both touch S3 versioning — cross-noted in task orders but can run in parallel, coordinate on findings. |
| News/trending scoped as Layer 3 (re-publish, not restore) | DynamoDB is already date-keyed. No S3 restore needed. This simplifies scope significantly. |
| BD snapshot archive (not S3 versioning) as primary hypothesis | Versioning on a large frequently-overwritten bucket accumulates cost and generates noisy version history. Snapshot pattern is cleaner and bounded. AE to validate cost estimate. |
| SmartX descoped | Portfolio construction data; not meaningful as "portal state at a date" for client presentation use case. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `docs/architecture/DRFR_PTMCH_PRD.md` | New research PRD | No |
| `org/projects/DRFR_PTMCH.json` | New project JSON | No |
| `org/projects/REGISTRY.md` | Added DRFR_PTMCH row to Active; moved ADVI_NNAVAR + ADVI_AUAVAR to Completed | No |
| `org/projects/ADVI_NNAVAR.json` | Thread status active → complete | No |
| `org/projects/ADVI_AUAVAR.json` | Thread status active → complete | No |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/DRFR_PTMCH.001.cloudops-versioning-iam-audit.md` | New task order | No |
| `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/DRFR_PTMCH.001.opal-pipeline-archive-audit.md` | New task order | No |
| `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/DRFR_PTMCH.001.bd-pipeline-snapshot-audit.md` | New task order | No |

---

## Blockers

None. All AE task orders are dispatched. Waiting on discovery findings.

---

## Current State

**Status:** COMPLETE (CTO scope for this session)
**Active branch:** CLOUD

Project DRFR_PTMCH registered. Research PRD written. Three AE discovery task orders
dispatched. Project is blocked on AE audit findings — specifically whether S3 versioning
is enabled on `opal-data-portal-v2` (0.7.0 + 0.5.0 both checking) and whether the
yang-capture-output-versions archive is actually producing non-null versionIds in
production (0.5.0 checking). BD snapshot feasibility depends on 0.6.0 findings.

---

## Next Steps

1. **[0.7.0_AE_CloudOps] Run cloud infra audit** — S3 versioning, CloudFront routing, IAM gaps, DynamoDB PITR
2. **[0.5.0_AE_OpalETL] Run yang archive audit** — confirm versionIds non-null, json/latest/ inventory, ingest-dynamodb scope, FRED/market-overview paths
3. **[0.6.0_AE_PartnerETL] Run BD pipeline audit** — gold/ inventory, rebuild cadence, snapshot cost, publisher parameterization
4. **[1.0.0_SA_CTO] Write implementation PRD** — after all three findings documents are in, update DRFR_PTMCH_PRD.md Section 5 with concrete implementation plan and hand to COO for decomposition

**Files to touch next:**
- `docs/architecture/DRFR_PTMCH_PRD.md` — update Section 5 once AE findings are in

**Do NOT:**
- Begin any Lambda code or Terraform changes before AE findings confirm feasibility
- Enable S3 versioning via CLI as part of this audit — document-only phase
