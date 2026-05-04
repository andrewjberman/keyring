# Portal PROD Deploy — portal-v2.1.74

**Date:** 2026-05-04
**Agent:** 0.4.0_DT_ClientPlatform
**Authorization:** Andrew direct — "make sure all of DE commits are pushed to DEV and do a FF merge deploy to PROD ... we want all of those edits committed and pushed, the tree shouldn't be dirty"

---

## Current State

`portal-v2.1.74` is live on PROD. Two commits bundled (DE 0.4.0 MDLP_RVVALT polish):

| Commit | Author | Subject |
|--------|--------|---------|
| `1d7dd022` | 0.4.0_DE_ClientPlatform | fix(MDLP_RVVALT): Rolling Sharpe x-ticks — month-end only, MM-YYYY format |
| `a423e646` | 0.4.0_DE_ClientPlatform | fix(MDLP_RVVALT): MaxDrawdown month-end x-ticks + RollingSharpe interval entry-counts (22/65/131/261 to match weekday-only timeseries) |

`a423e646` was the previously-uncommitted dirty working tree captured at session start (DE in-progress continuation of the MDLP_RVVALT chart work — month-end tick parity on MaxDrawdown matching `1d7dd022` + Sharpe interval entry-count alignment with Return-vs-Vol scatter calendar-day cutoff). Andrew authorized commit + ship rather than stash.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Audit `git log origin/PROD..HEAD` + `git status` | DEV +1 ahead (`1d7dd022` DE-authored); 2 dirty files MaxDrawdownChart.tsx + RollingSharpeChart.tsx |
| 2 | `bun run typecheck` (tsc -b --noEmit) | Exit 0 |
| 3 | Initial `git checkout PROD && git merge DEV --ff-only` blocked by overlapping dirty files | stash → checkout DEV → unstash to relocate dirty edits to DEV branch |
| 4 | `git commit --only --author="0.4.0_DE_ClientPlatform <0.4.0_DE_ClientPlatform@opal.agent>"` MaxDrawdownChart.tsx + RollingSharpeChart.tsx | `a423e646` on DEV |
| 5 | `bun run typecheck` (post-commit) | Exit 0 |
| 6 | `git push origin DEV` | `1d7dd022..a423e646` |
| 7 | `git checkout PROD && git merge DEV --ff-only` | `71b5532d..a423e646` (2-commit FF) |
| 8 | `git push origin PROD` | Pre-push hook typecheck PASS — OK: `71b5532d..a423e646` |
| 9 | `gh run watch 25338395334 --exit-status` | Build / Deploy S3+CF / Tag — all success |
| 10 | `git fetch --tags origin` | `portal-v2.1.74` fetched (CI auto-tag) |
| 11 | Workspace pointer bump: `safe-commit.sh -- portal` | `3ee1c1913` on CLOUD |
| 12 | `git push origin CLOUD` | `e3e7c2a6f..3ee1c1913` |

---

## Final State Verification

| Check | Result |
|-------|--------|
| Portal local HEAD (PROD) | `a423e646` |
| `origin/PROD` | `a423e646` |
| `origin/DEV` | `a423e646` |
| DEV ahead of PROD | 0 commits — clean |
| Portal working tree | Clean (no `-dirty` suffix) |
| Workspace pointer | `a423e646` via `3ee1c1913` |
| CI run 25338395334 | completed / success |
| Tag | `portal-v2.1.74` |

---

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| portal | `portal-v2.1.74` | `a423e646` |

---

## RAVC

- COO 2.0.0_SA_COO sent working-tree-cleanup MCP mid-deploy (had spotted dirty `1d7dd022...-dirty` portal pointer during their sweep).
- DT replied with closure evidence post-deploy: workspace pointer `3ee1c1913`, tag `portal-v2.1.74`, CI run green, working tree clean.
- COO RAVC5 close received: "Loop closed. Thanks for the parallel deploy."
- COO follow-up commits on CLOUD on top of pointer bump: `ee4e1ecb9` (COO cleanup) + DE log commit, HEAD `4d7e86797`.

---

## Compiler Tools

| Tool | Reason | Result |
|------|--------|--------|
| `bun run typecheck` (tsc -b --noEmit) x3 | Pre-commit gate, post-commit gate, pre-push hook | Exit 0 each |
| comp-transform schema-check | Not run — pure ModelPortfolios chart x-tick polish; no Lambda output / advisor data shape changes | N/A |
| comp-blast | Not run — chart-internal polish only; no fn / artifact changes | N/A |

---

## Next Steps

- [DT] No further portal work queued. Standing by.
- [RD 0.4.2] Inflection S7 smoke re-test still pending (gated on AE 0.6.1 INF_D_04 summary.json dispatch — not blocking DT).
