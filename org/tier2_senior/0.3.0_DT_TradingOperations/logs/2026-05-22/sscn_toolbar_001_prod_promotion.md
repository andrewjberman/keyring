# SSCN_TOOLBAR.001 — Security Scanner filter toolbar: DEV push + PROD promotion

**Agent:** 0.3.0_DT_TradingOperations
**Date:** 2026-05-22
**TO:** SSCN_TOOLBAR.001 (from 0.3.0_DE_TradingOperations, Andrew-direct)

## Current State

SSCN_TOOLBAR.001 complete. The Security Scanner filter toolbar (`ScannerFilterToolbar.tsx`
+ wiring into both grid tabs, DEV commit `4938bf36`) is pushed to origin/DEV and
promoted to PROD. opalinvest.dev live, GHA deploy SUCCESS.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Push portal DEV | `b5dce977..4938bf36` DEV -> DEV; portal pre-push typecheck gate PASS |
| 2 | Cherry-pick `4938bf36` onto PROD (main tree) | `0be05530` — 3 files, 143 ins / 5 del, no conflict |
| 3 | Build gate on PROD (main tree) | `tsc -b --noEmit` exit 0; `bun run build` exit 0 (built 39.9s) |
| 4 | Tag + push PROD | tag `portal-v2.1.98`; `7442fc9d..0be05530` PROD -> PROD `--follow-tags`; pre-push typecheck PASS |
| 5 | GHA "Deploy to Production" | run `26311673560` SUCCESS — Build 1m33s / Deploy S3+CloudFront 9s / Tag 9s |
| 6 | opalinvest.dev verify | HTTP 200 |
| 7 | Bump parent portal gitlink | `43db645cf` portal -> `0be05530`; pushed `ea35306b9..43db645cf` CLOUD -> CLOUD |

## Worktree-occupancy note

Per the TO, the canonical ephemeral-worktree promotion form (deployment_map.xml
`<portal_prod_promotion>`, ea35306b9) was **waived for this one transitional
promotion**: both branches were occupied — main tree on PROD, `.runtmp/portal-dev-verify`
on DEV — so `git worktree add PROD` was not possible. The cherry-pick ran in the
main tree (already on PROD, clean), explicitly sanctioned by the TO author. The
permanent worktree form resumes once the transitional worktree occupancy clears.
The main-tree DEV restore remains a separate open item, gated on the
`.runtmp/portal-dev-verify` teardown.

## Anomalies

- Parent-repo CLOUD commit hit ~25s of `.git/index.lock` contention from concurrent
  agents; committed via `git commit --only -- portal` (documented fallback —
  safe-commit.sh aborted on another agent's staged yang-pipeline files in the
  shared index; `--only` scoped the commit to `portal` without disturbing their
  staged work). Resolved cleanly, 1 file changed.
- CLOUD push HALTGT checkpoint surfaced a routine NUDGE from 0.3.0_DE (status
  request for this same TO); reviewed, non-STOP-class, re-pushed with `HALT_ACK=1`.

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| portal (PROD) | `portal-v2.1.98` | `0be05530` |

## Compiler Tools

| Tool | Result |
|------|--------|
| (none — promotion, not an edit) | TO compiler mandate: "re-run schema-check only if you touch source; you should not — this is a promotion." No source edited; the cherry-pick is byte-identical to the DE-validated `4938bf36`. Build + typecheck gate (exit 0) substituted as the post-check. No Lambda/IAM change (portal-only). |

## Next Steps

1. **[0.3.0_DE]** RAVC2 sent — commits/tag/GHA/opalinvest.dev evidence for RAVC4 validation.
2. **[0.3.0_DT]** Separate open item unchanged: portal main-tree `git checkout DEV`
   restore, gated on the `.runtmp/portal-dev-verify` worktree teardown (after
   0.4.0_DE~B lands MDPF_ASSETS.033).
3. DT lane otherwise idle.
