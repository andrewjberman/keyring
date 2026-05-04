# Portal PROD Deploy — portal-v2.1.70

**Date:** 2026-05-04
**Agent:** 0.4.0_DT_ClientPlatform
**Authorization:** Andrew direct confirmation (AC6 edits confirmed verbally; supersedes RD 0.4.2 hardware sign-off pending)

---

## Current State

`portal-v2.1.70` is live on PROD. Three commits bundled from portal DEV:

| Commit | Subject | Gate |
|--------|---------|------|
| `c9b0f649` | feat(DASH_STSTRP): stat-strip density tightening (Option A) — 4-file CSS class diff | AC1-AC5 PASS (DE /frontend-dev Playwright); AC6 confirmed by Andrew |
| `61e13bea` | fix(INFLEC): add inf->inflection to LAMBDA_FIRM_ID | Prerequisite for Inflection S7 — unblocks all Lambda-routed Book endpoints |
| `6ba6d2ee` | fix(inflec): wire realized/unrealized tax + household_id->client_key normalization | DE fix for TaxCostBasisPanel null + L3 client-name drilldown; typecheck clean |

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | `bun run typecheck` (tsc -b --noEmit) on portal HEAD `6ba6d2ee` | Exit 0 — clean |
| 2 | Review new commit `6ba6d2ee` (DE, 2-file Inflection tax/client-key fix) | PASS — legitimate DE fix, typecheck already covered |
| 3 | `git checkout PROD && git merge DEV --ff-only` | `12e84c70..6ba6d2ee` (3-commit fast-forward) |
| 4 | `git push origin PROD` | Pre-push hook typecheck PASS — OK: `12e84c70..6ba6d2ee` |
| 5 | `git checkout DEV && git push origin DEV` | `12e84c70..6ba6d2ee` |
| 6 | `gh run watch 25327372442 --exit-status` | Build / Deploy S3+CF / Tag — all success |
| 7 | `git fetch --tags origin` | `portal-v2.1.70` fetched |
| 8 | Workspace pointer bump | Already committed at `5f2ba8a2d` (prior agent) — no duplicate needed |

---

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| portal | `portal-v2.1.70` | `6ba6d2ee` |

---

## Verification

CI run `25327372442`:
- Build Production Assets: success
- Deploy to S3 + CloudFront: success
- Tag Deployment: success (`portal-v2.1.70`)

Portal DEV == PROD == `6ba6d2ee` post-deploy (confirmed via `git log origin/PROD..origin/DEV` → empty).

---

## Bundled Commits Detail

**DASH_STSTRP.001** (`c9b0f649`):
- Files: AccountDistributionMetrics.tsx, DistributionTab.tsx, AUMGrowthMetrics.tsx, ConsolidatedOverviewPanel.tsx
- Change: 4-file CSS class diff (gap-x-2, px-3 py-1 min-w-[88px] anchors, text-base pills)
- AC1-AC5 PASS (DE Playwright). AC6 confirmed by Andrew.

**LAMBDA_FIRM_ID fix** (`61e13bea`):
- File: portal/src/api/endpoints/advisor-intelligence.ts:72
- Change: Added `inf: 'inflection'` to LAMBDA_FIRM_ID map
- Unblocks all Inflection Lambda-routed Book endpoints (getPlatinumAdvisorSummary, getAdvisorBook, getBooksClientDetail)

**Inflection tax/client-key fix** (`6ba6d2ee`, DE):
- Files: AdvisorBookView.tsx, types.ts
- Change: realized/unrealized tax wiring for Inflection L2 TaxCostBasisPanel; household_id→client_key normalization for L3 client-name lookup + ClientListPanel row-click

---

## Compiler Tools

| Tool | Reason | Result |
|------|--------|--------|
| `bun run typecheck` (tsc -b --noEmit) | Pre-push gate — portal-only change, no boto3/IAM/S3/Lambda changes | Exit 0 — PASS (x2: manual + pre-push hook) |
| comp-routes behaviors | Not run — no CF behavior change; pure portal JS/TS diff | N/A |
| comp-transform schema-check | Not run — no new rendered fields; DE confirmed schema-check CLEAN in DASH_STSTRP session | N/A |
| comp-iam service | Not run — no Lambda code change in this deploy | N/A |

---

## Next Steps

- [RD 0.4.2] S7 re-test now gated ONLY on AE 0.6.1 INF_D_04 dispatch (summary.json in s3://opal-data-inf). LAMBDA_FIRM_ID fix is live on PROD. MCP sent to RD.
- [AE 0.6.1] INF_D_04 dispatch needed to populate platinum/advisors/*/summary.json for Inflection S7 smoke.
- [COO] RAVC4 dispatched: portal-v2.1.70 live, 3-commit bundle, CI green.
