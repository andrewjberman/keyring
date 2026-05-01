# Partner Portal Page Lineup Consolidation — DT 0.4

**Date:** 2026-05-01
**TO source:** CTO GO 2026-05-01 (`20260501T202041Z_1.0.0_SA_CTO_GO___Partner_portal_page_lineup_consolid.md`)
**Project:** Partner-facing surface area policy — cross-firm

## Current State

Canonical 8-page partner lineup is live across all three current partner firms.

- **49Financial:** 8 pages (Market Overview, Model Portfolios, Advisor Intelligence, Capital Markets, Positioning, Valuations, Macroeconomics, Trade Submission)
- **Inflection:** 8 pages (same as 49F)
- **Cottonwood:** 7 pages (above minus Advisor Intelligence — preserved per AUTH_COTTON 2026-04-29)
- **Internal `opal-capital`:** unchanged (sees all pages including Attribution / Factor Tilts / Correlations)

Removed from partner-facing nav/allowlist: `/attribution`, `/factor-tilts`, `/correlations` (these were exposed to Cottonwood only). Added to 49F + Inflection: `/valuations`. Net diff in `portal/src/lib/firmAccess.ts` is `+2 / -3` lines.

All target paths were already wired in `App.tsx` Routes (lines 397-455). Nav items rendered from `NAV_SECTIONS` are filtered via `isPathAllowedForFirm(claims?.firmId, item.path)` at App.tsx:291. Direct-URL probe protection is enforced in `ProtectedRoute` at component:57 — partners hitting a removed path redirect to `FIRM_DEFAULT_LANDING = '/market'`.

Portal commit `12e84c70` shipped on PROD via CI run `25231731050` (success); tag `portal-v2.1.69` cut by `Tag Deployment` job. Workspace pointer bumped at `91840cab6`.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read CTO GO + verify `firmAccess.ts` paths against current state | 49F 7→8 (add /valuations), INF 7→8 (add /valuations), COTTON 10→7 (remove /attribution, /factor-tilts, /correlations) |
| 2 | Edit `portal/src/lib/firmAccess.ts` | +2 / -3 lines (single-file allowlist consolidation) |
| 3 | `bun run typecheck` (tsc -b --noEmit) on portal | PASS (no output = success) |
| 4 | `safe-commit.sh` on `src/lib/firmAccess.ts` from portal/ | `12e84c70` on DEV |
| 5 | `git checkout PROD && git merge DEV --ff-only` | ba6abac7..12e84c70 (7-commit fast-forward) |
| 6 | `git push origin PROD` | OK (pre-push hook ran typecheck again, PASS) |
| 7 | `git checkout DEV && git push origin DEV` | eda8ef19..12e84c70 |
| 8 | `gh run watch 25231731050 --exit-status` | conclusion=success: Build / Deploy S3 / Invalidate CloudFront / Tag all green |
| 9 | `git fetch --tags origin` | new tags portal-v2.1.67/68/69 visible (mine: portal-v2.1.69) |
| 10 | Parent `safe-commit.sh -- portal` | `91840cab6` on CLOUD (1 file, +1 / -1) |
| 11 | `git push origin CLOUD` | 83776f53b..91840cab6 |

## Bundling

The PROD push carried 7 portal commits ahead of `origin/PROD` (including CTO-flagged `9cee67b5`):

| Commit | Subject |
|---|---|
| `12e84c70` | feat(firmAccess): canonical 8-page partner lineup consolidation [this TO] |
| `9cee67b5` | fix(ADVI_INFSHIP.PHASE3-FE-BUGS): Inflection portal validation sweep — 3 FE bug fixes |
| `eda8ef19` | feat(ADVI_INFLEC): add joe_brandenburg to INFLECTION_LAYOUT, maxEntries 3→4 |
| `717eb50c` | test(ADVI_INFLEC): add V1 structural smoke test suite + constitution |
| `1f307960` | fix(ADVI_INFLEC.DIAGFIX.005b): render revenueOpsSlot standalone when clientsTabData null |
| `819246aa` | feat(market): remove legacy precomputed edge fallback path |
| `d565f8b3` | fix(ADVI_INFLEC.DIAGFIX.005): Books null-guard + date cap for in-progress quarter |

Per CTO GO bundling note — surfaced in RAVC4 to CTO and listed in workspace pointer-bump commit body.

## Deployment Tags

| Pipeline | Tag | Commit |
|---|---|---|
| portal | `portal-v2.1.69` | `12e84c70` |

## Verification

```
$ git diff src/lib/firmAccess.ts
@@ -24,6 +24,7 @@
     '/advisor-intelligence',
     '/cma',
     '/positioning',
+    '/valuations',
     '/macro',
     '/trade-submission',
   ]),
@@ -33,6 +34,7 @@
     '/advisor-intelligence',
     '/cma',
     '/positioning',
+    '/valuations',
     '/macro',
     '/trade-submission',
   ]),
@@ -41,10 +43,7 @@
     '/portfolios',
     '/cma',
     '/positioning',
-    '/attribution',
-    '/factor-tilts',
     '/valuations',
-    '/correlations',
     '/macro',
     '/trade-submission',
   ]),
```

Acceptance criteria status:

| AC | Status | Evidence |
|---|---|---|
| 1. 49F sees 8 pages incl. AI; no Attribution/FactorTilts/Correlations | CODE-VERIFIED (allowlist diff above; all 8 paths in `App.tsx` Routes) | Andrew per-firm login validation pending |
| 2. Inflection sees 8 pages incl. AI | CODE-VERIFIED | Andrew validation pending |
| 3. Cottonwood sees 7 pages (no AI) | CODE-VERIFIED | Andrew validation pending |
| 4. Internal opal-capital regression-safe | PASS by construction (`firmId === INTERNAL_FIRM_ID` short-circuits to true at firmAccess.ts:64) | — |
| 5. Direct-URL probe on removed page redirects | PASS by construction (ProtectedRoute redirects to `FIRM_DEFAULT_LANDING = '/market'` at ProtectedRoute.tsx:57) | — |
| 6. Portal version bump + DT push | PASS — `portal-v2.1.69`, CI green, workspace pointer bumped | — |

## Compiler Tools

| Tool | Reason | Result |
|---|---|---|
| (none) | Single-file TS allowlist edit, no boto3/IAM/S3/CloudFront/component-data changes; `comp-transform schema-check` not relevant (no field rendering); `comp-routes behaviors` not relevant (no CF behavior change); `comp-blast` not relevant (allowlist data, no fn-graph change). Typecheck (`tsc -b --noEmit`) was the appropriate guard and passed. | N/A |

## Next Steps

- [Andrew] Per-firm login smoke (49F + Inflection + Cottonwood) to validate ACs 1-3 against deployed `portal-v2.1.69`.
- [1.0.0_SA_CTO] RAVC4 dispatched (this log + commit hashes + tag).
- [DT 0.4 housekeeping] Stale `<status>staged</status>` on `ADVI_49EXEC.007` — comment confirms the work shipped (`ecc9b2a5` + `8e50d35c`); project closed in REGISTRY 2026-04-28. One-line flip available next time the index is clean.
