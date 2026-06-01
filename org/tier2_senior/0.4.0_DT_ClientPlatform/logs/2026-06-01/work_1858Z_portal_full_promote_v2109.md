# work 1858Z — Portal FULL DEV->PROD promote v2.1.109 (Andrew-direct merge-deploy via COO)

**archetype:** DEPLOY

## Current State — SHIPPED, PROD LIVE + CF-confirmed

ws COO `[DRIVE-GO]` `20260601T185515Z` relaying Andrew-direct ("tell 0.4.0_DT_ClientPlatform to merge
deploy new PROD"). This is the NEXT promote after v2.1.107 — and a FULL DEV->PROD this time: the items I
held from the v2.1.107 synthesis-cut (Macro YYYY-MM + Inflection colors) are now all ready, so the whole
DEV delta ships with nothing to exclude. Andrew-direct GO is my authority (he cleared the visual-smoke
process). RAVC2 sent to COO + CTO; Andrew via thread.

## Delta — full 7-commit linear chain (origin/PROD 456d134e -> origin/DEV d4c1b5cf)

| Commit | Subject |
|--------|---------|
| 39555946 | polish(MDPF): distinct colors for Inflection 50/50 blend portfolios |
| b0a5a55a | fix(Macro): year-qualified (YYYY-MM) month-key lookup in MacroHeatmap |
| 998ff784 | fix(Macro): read producer's values_ym (YYYY-MM) field, not values[] |
| 3c2aa71b | chore(MDPF S4): canonical model names in Positioning HoldingsTab PORTFOLIOS array |
| c9a187f3 | polish(MDPF): 50/50 ST/INT blend color -> chartreuse (Andrew, was yellow) |
| 324f620b | DE: retire ETF_NAME_FALLBACKS (HoldingsTab) — backend-canonical post A+, DE serving-verified 0 divergence |
| d4c1b5cf | fix(MDPF): canonical blend label '50/50 INT/LTC' -> '50/50 INT/LT' (LTC->LT) |

Files: `modelPortfolioColors.ts`, `Macroeconomics/panels/MacroHeatmap.tsx`, `Macroeconomics/types.ts`,
`Positioning/tabs/HoldingsTab.tsx` (4 files, +73/-93). MDPF Schwab re-derive is data-layer (timeseries
artifacts already serving) — renders on this build automatically, no FE commit.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Pre-flight | origin/PROD `456d134e` (rollback ref / v2.1.107); origin/DEV `d4c1b5cf`; local DEV HEAD already == d4c1b5cf (working tree AT promote target — clean); working tree clean (no WIP to disturb); delta = exactly the 7 dispatched commits; scope 4 files +73/-93; SUPERSET-LOSS EMPTY |
| 2 | Rule 19 commit-tree (FULL, not synthesis-cut) | TREE=`694902f0` (= origin/DEV^{tree}); MERGE=`a810bbef` (`commit-tree origin/DEV^{tree} -p origin/PROD -p origin/DEV`); `git diff --stat MERGE origin/DEV` EMPTY (byte-identical to DEV — PROD==DEV) |
| 3 | HALTGT (manual) | inbox empty, no STOP-class before irreversible push |
| 4 | Push MERGE:PROD | `456d134e..a810bbef -> PROD`; VALGATE D-1 PASS + typecheck PASS. NOTE: working tree was AT d4c1b5cf this time, so the pre-push typecheck validated the EXACT promoted content (no stale-working-tree mismatch like the v2.1.107 tick) |
| 5 | Tag | `portal-v2.1.109` -> a810bbef, pushed (CI auto-tagged v2.1.110 same commit) |
| 6 | CI watch | run `26775419221` "Deploy to Production" = SUCCESS (Build / Deploy S3+CloudFront / Tag all green) |
| 7 | CF invalidation | explicit /* on EVTSA9VEHNZVH = `IR7TXKCX75J492NGA4L85DEMA` = COMPLETED (edge flushed) + CI's own ran |
| 8 | Rule 19 invariant | main portal/ tree STILL on DEV; commit-tree never touched working tree — verified |

## Deployment Tags
| Pipeline | Tag | Commit |
|----------|-----|--------|
| portal | portal-v2.1.109 (DT) + portal-v2.1.110 (CI auto) | a810bbef (PROD) |

## Verification
- PROD tree byte-identical to origin/DEV (d4c1b5cf) — PROD == DEV.
- CI Deploy-to-Production 26775419221 SUCCESS (all 3 jobs); CF invalidation Completed.
- Rendered-pixel re-verify human-only (headless-Chrome blocked fabric-wide; CF portal fetch = 403 auth gate).
  Data/asset-layer evidence = CI Deploy-to-S3+CF SUCCESS + byte-identical tree + Andrew cleared visual-smoke process.

## Next Steps
- **[COO/Andrew/CTO]** RAVC2 sent — PROD v2.1.109 LIVE + CF-confirmed.
- Rollback path if needed: PROD `456d134e` (v2.1.107).
- /work loop continues; no held-TO changes this tick (the COO dispatch was the work).

## Compiler Tools
No comp-* — portal FE promote (git plumbing + CI + CloudFront), not a Lambda/script/IAM edit. Pre-push
VALGATE D-1 + typecheck served as the change-gate. AWS CF `/*` invalidation used `--invalidation-batch
'{...}'` JSON form to dodge Git-Bash path mangling.
