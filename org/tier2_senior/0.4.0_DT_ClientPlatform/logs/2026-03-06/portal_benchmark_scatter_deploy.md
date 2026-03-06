# Portal Deploy — Benchmark Scatter Granular Selection — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Portal PROD commit:** `312ca3d`
**Workspace CLOUD commit:** pending

---

## Objective

Merge portal DEV → PROD and deploy `portal-v2.1.9` to S3/CloudFront. This release
carries the ModelPortfolios Benchmark tab granular scatter selection feature
authored by `0.4.0_DE_ClientPlatform` across 9 portal DEV commits (`60f1ee0`→`312ca3d`).

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | `git checkout PROD && git merge DEV` | Fast-forward `1958f0f`→`312ca3d` (4 files changed) |
| 2 | `git push origin PROD` | PROD at `312ca3d` |
| 3 | `bash scripts/deploy-manual.sh` | Pre-deploy checks passed |
| 4 | `bun run build` | 4698 modules, built in 12.34s, dist: 4.8M |
| 5 | `aws s3 sync dist/ s3://opalinvest-portal/` | All assets uploaded, stale assets deleted |
| 6 | `aws s3 cp index.html` (no-cache) | Uploaded with `no-cache, no-store, must-revalidate` |
| 7 | CloudFront invalidation | `IBIDGBK1XTQBLP2NSCAQPW1S6X` on `/*` |
| 8 | Auto-tag | `portal-v2.1.9` pushed to origin |

---

## Verification

```
Tag:            portal-v2.1.9
Branch:         PROD
S3 Bucket:      s3://opalinvest-portal/
CloudFront:     EVTSA9VEHNZVH
Invalidation:   IBIDGBK1XTQBLP2NSCAQPW1S6X
Bundle Size:    4.8M
Time:           2026-03-06 16:56:44 UTC
```

Build output confirmed `ModelPortfolios-CjL4wHOT.js` (63.13 kB) uploaded —
this chunk contains the updated `ReturnVolatilityScatter` component.

---

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| portal | `portal-v2.1.9` | `312ca3d` |

---

## Files Changed in This Release (DEV→PROD diff)

| File | Change |
|------|--------|
| `src/components/ReturnVolatilityScatter.tsx` | Granular scatter selection + GranularTooltips |
| `src/pages/AdvisorIntelligence/tabs/DistributionTab.tsx` | Prior session work |
| `src/pages/AdvisorIntelligence/types.ts` | Prior session work |
| `vite.config.ts` | Vite proxy entry for security-scanner |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `PROD` (portal), `CLOUD` (workspace)

`portal-v2.1.9` is live on CloudFront (`EVTSA9VEHNZVH`). Cache invalidation in
progress — live within 2-5 minutes of deploy time. No rollback needed; pre-deploy
checks and build passed cleanly.

---

## Next Steps

None — deployment complete.
