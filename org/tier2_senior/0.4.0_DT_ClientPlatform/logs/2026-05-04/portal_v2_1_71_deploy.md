# Portal PROD Deploy — portal-v2.1.71

**Date:** 2026-05-04
**Agent:** 0.4.0_DT_ClientPlatform
**Authorization:** Andrew direct — "MAKE SURE ALL THE PORTAL EDITS ARE PROPERLY COMMITTED AND PUSHED, NEED FULL DEPLOY TO PROD"

---

## Current State

`portal-v2.1.71` is live on PROD. Four commits bundled (Andrew's MDLP_RVVALT work):

| Commit | Author | Subject |
|--------|--------|---------|
| `a6cf9da5` | Andrew Berman | feat(MDLP_RVVALT): 3-view toggle on ReturnVolatilityScatter — Rolling Sharpe + Max Drawdown |
| `b648c221` | Andrew Berman | feat(MDLP_RVVALT): MaxDrawdownChart — model cards + benchmark drawdown line |
| `dc158fa8` | Andrew Berman | fix(MDLP_RVVALT): UI label + Period toggle placement polish |
| `8e31ec7e` | Andrew Berman | fix(MDLP_RVVALT): right-align Period and Interval toggles in content area |

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Audit portal state — `git log origin/PROD..HEAD` | 4 commits ahead on DEV local; all Andrew's MDLP_RVVALT commits |
| 2 | `bun run typecheck` (tsc -b --noEmit) on HEAD `8e31ec7e` | Exit 0 — clean |
| 3 | Review 4 commits (`--stat --no-patch`) | All Andrew's own work: portal-proxy.ts + MaxDrawdownChart.tsx + ReturnVolatilityScatter.tsx + RollingSharpeChart.tsx — new chart components + 3-view toggle |
| 4 | `git checkout PROD && git merge DEV --ff-only` | `6ba6d2ee..8e31ec7e` (4-commit fast-forward) |
| 5 | `git push origin PROD` | Pre-push hook typecheck PASS — OK: `6ba6d2ee..8e31ec7e` |
| 6 | `git checkout DEV && git push origin DEV` | `6ba6d2ee..8e31ec7e` |
| 7 | `gh run watch 25330593900 --exit-status` | Build / Deploy S3+CF / Tag — all success |
| 8 | `git fetch --tags origin` | `portal-v2.1.71` fetched |
| 9 | `git add portal && safe-commit.sh -- portal` | `2412fc954` workspace pointer bump |
| 10 | `git push origin CLOUD` | `056780bf0..2412fc954` — PUSH OK |

---

## Final State Verification

| Check | Result |
|-------|--------|
| Portal local HEAD | `8e31ec7e` |
| `origin/PROD` | `8e31ec7e` |
| `origin/DEV` | `8e31ec7e` |
| DEV ahead of PROD | 0 commits — clean |
| Workspace pointer (`git ls-tree HEAD portal`) | `8e31ec7e` |
| CI run 25330593900 | completed / success |
| Tag | `portal-v2.1.71` |

---

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| portal | `portal-v2.1.71` | `8e31ec7e` |

---

## What Shipped (MDLP_RVVALT Feature)

- **portal-proxy.ts**: new `ModelTimeseriesPoint`, `ModelTimeseriesResponse`, `getModelPortfolioTimeseries` fetch
- **ReturnVolatilityScatter.tsx**: 3-view toggle (Period Volatility / Rolling Sharpe / Max Drawdown); lazy-loads timeseries on first switch
- **RollingSharpeChart.tsx** (new): model selector cards (Factor Spreads layout, INT default); Interval toggle; rolling calc over last 365 days; solid/dashed lines per model; canonical MODEL_COLOR_KEYS colors
- **MaxDrawdownChart.tsx** (new): running peak-to-trough drawdown per model; Factor Spreads card UI; solid model + dashed benchmark drawdown lines; canonical colors

---

## Compiler Tools

| Tool | Reason | Result |
|------|--------|--------|
| `bun run typecheck` (tsc -b --noEmit) | Pre-deploy gate (manual + pre-push hook) | Exit 0 x2 — PASS |
| comp-transform schema-check | Not run — no Inflection/advisor data changes; pure ModelPortfolios chart component additions | N/A |
| comp-blast | Not run — new chart components only; no gold script / Lambda output path changes | N/A |

---

## Current State

Portal DEV == PROD == `8e31ec7e` (`portal-v2.1.71`). All portal edits deployed. Index clean (only untracked `.frontend-dev/` testing artifacts from RD — not portal source).

## Next Steps

- [RD 0.4.2] S7 smoke re-test still pending (LAMBDA_FIRM_ID + summary.json both live). Awaiting RD result.
- [DT] No further portal work queued. Standing by.
