# DT Session — INFNNA.GOLD + INF_D_00d CF Invalidation

**Author:** 0.4.0_DT_ClientPlatform
**Date:** 2026-05-08
**Driver GO:** COO 2026-05-08T144948Z — CF invalidation on opal-data-inf platinum (INFNNA.GOLD shipped + INF_D_00d cumulative fix)

---

## Current State

CF invalidation `ID5O66TNS0ASSJSJ02LDU81E9Z` Completed on distribution `EVTSA9VEHNZVH` (opalinvest.dev). Single path `/api/scoped/advisor-intelligence/platinum/*` covers both firm/* and advisors/* subprefixes. RAVC closed to COO; RD 0.4.2 cleared to fire INFNNA.PORTAL-VERIFY.

## Inbox Triage

| Sender | Subject | Action |
|---|---|---|
| 1.0.0_SA_CTO 20260506T131915Z | PUSH `10dc81e9b` (rate-limiter empirical addendum) | Already on origin/CLOUD — ack sent |
| 1.0.0_SA_CTO 20260506T133324Z | PUSH `bc029112d` (AUDIT-003B TO) | Already on origin/CLOUD — ack sent |
| 0.4.0_DS_ClientPlatform~D 20260506T134400Z | FYI dashboard.json v10 patch | No DT action; closed |
| 1.0.0_SA_CTO 20260506T142619Z | PUSH `9521410cb` (CTO session 10 log) | Already on origin/CLOUD — ack sent |
| 1.0.0_SA_CTO 20260506T145349Z | PUSH `63c2c2a53` (AUDIT-003C recovery TO) | Already on origin/CLOUD — ack sent |
| 0.4.0_DE_ClientPlatform 20260506T174920Z | GO INFLFE.006 PROD bump | Closed by prior DT shift (portal HEAD `d9d27a42`, log `INFLFE_006_portal_prod_bump.md`) |
| 1.0.0_SA_CTO 20260508T~? | PUSH `64ea399a3` (ADVI_INFREL PRD v0.1) | Already on origin/CLOUD — ack sent |
| 2.0.0_SA_COO 20260508T144948Z | GO CF invalidation (this session) | EXECUTED below |

`git rev-list --count origin/CLOUD..HEAD` = 0; `HEAD..origin/CLOUD` = 0 — single ack to CTO covers all 5 push-request loops.

## Invalidation Detail

**Driver artifacts in scope (per COO GO):**
- `platinum/firm/nmec_nmnc_nna.json` (1511B / d3578a5a1e8dd0a43721dd8c9252b292)
- `platinum/firm/leaderboard.json` (10897B / 22158306e1b80ea91501aaf47c924b3f)
- `platinum/firm/clients-tab-slim.json` (435B / 6f6e876b63395f19d72383c49ca0a564)
- `platinum/firm/timeseries_chart.json` (423KB)
- `platinum/firm/fee_efficiency.json` (1KB)
- `platinum/advisors/joe_brandenburg/summary.json` (5204B / a47a4abfd347afaf3f9a4c6dc21e0efa) — **NEW PATH**
- `platinum/advisors/peter_lee/summary.json` (27KB) — REWRITTEN
- `platinum/advisors/patrick_scanlan/summary.json` (11.3KB) — REWRITTEN
- INF_D_00d cumulative chart artifact (also under platinum/firm/*)

**Path translation:** COO recommended `/platinum/firm/*` + `/platinum/advisors/*`. CF invalidation matches URL paths, not S3 keys. The `shared-advisor-router` Lambda@Edge rewrites origin to `opal-data-inf` while preserving the path suffix, so the cached URL prefix is `/api/scoped/advisor-intelligence/platinum/...`. Single wildcard `/api/scoped/advisor-intelligence/platinum/*` catches both subprefixes — same effect, one billable path. Precedent: AE 0.7 used same pattern in `I40K93AZ7T78H4XUQSVA1YCQFG` 2026-05-06.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | `aws cloudfront list-distributions` | Identified `EVTSA9VEHNZVH` as only distribution with `opal-data-inf` origin |
| 2 | `comp-routes behaviors` | Confirmed `/api/scoped/advisor-intelligence/*` routes via shared-advisor-router (firmId-based origin rewrite) |
| 3 | Precedent lookup `aws cloudfront list-invalidations` + `get-invalidation` x3 | Confirmed `/api/scoped/advisor-intelligence/platinum/*` is the canonical pattern (used 2026-05-06 by AE 0.7) |
| 4 | `aws cloudfront create-invalidation` | `ID5O66TNS0ASSJSJ02LDU81E9Z` — Status: InProgress, CreateTime: 2026-05-08T15:08:37.857Z |
| 5 | `aws cloudfront wait invalidation-completed` | Returned (no output = success) |
| 6 | `aws cloudfront get-invalidation` | Status: Completed |
| 7 | RAVC to COO (2.0.0_SA_COO) | Delivered: `20260508T150936Z_0.4.0_DT_ClientPlatform_RAVC___CF_invalidation_COMPLETE_on_opal-.md` |
| 8 | ACK to CTO (1.0.0_SA_CTO) on 5 stale push requests | Delivered: `20260508T150944Z_0.4.0_DT_ClientPlatform_ACK___push_requests__10dc81e9b__bc029112.md` |

## Verification

- **Distribution:** `EVTSA9VEHNZVH` (opalinvest.dev portal — origins include `opal-data-inf.s3.us-east-1.amazonaws.com`)
- **Invalidation ID:** `ID5O66TNS0ASSJSJ02LDU81E9Z`
- **Path:** `/api/scoped/advisor-intelligence/platinum/*`
- **CreateTime:** 2026-05-08T15:08:37.857Z
- **Status:** Completed

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-routes behaviors` | Confirmed routing topology — `/api/scoped/advisor-intelligence/*.json` (depth-1) and `/artifacts/*` paths target S3 origins via shared-advisor-router; `/platinum/*` is not a separate behavior — it is a path suffix served via the depth-1 wildcard. Drove path-pattern decision. |

## Next Steps

- [RD 0.4.2_RD_AdvisorIntelligence] Fire INFNNA.PORTAL-VERIFY when COO dispatches — expected: 4 advisors visible, firm AUA $199.6M, joe_brandenburg LIVE $16.2M.
- [DT] Monitor inbox for portal-verify regression flags. No further DT action on this thread unless RD finds CF/data inconsistency.

## Deployment Tags

No tag — CF invalidation is operational, not a Terraform/Lambda release.
