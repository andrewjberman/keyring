# work 1900Z — Portal v2.1.121 DEV->PROD promote: SHIPPED, PROD LIVE

**archetype:** DEPLOY

## Current State — SHIPPED, PROD LIVE; NFRA_GRAPHS.D7 T1+T2+T3 type fixes active

COO GO (LD-0185) executed: 8b6a6466 (NFRA_GRAPHS.D7 T1+T2+T3 — PlatinumAdvisorSummaryRaw type alias + InflecAdvisorBookRaw SCHEMA-DRIFT fields + ClientsTab type mismatch fix + portal-proxy DEMO comment removal) promoted to PROD as portal-v2.1.121. T2 (tax_exposure zeroing, income_fees hardcoding = real data-loss fix) is the priority item now live.

## Promote params

| Field | Value |
|-------|-------|
| DEV HEAD promoted | `8b6a6466` (fix NFRA_GRAPHS.D7: T1+T2+T3 — type fixes + DEMO comment) |
| PROD base | `5699f899` (v2.1.120) |
| MERGE SHA | `d9aed856` (--no-ff) |
| PARITY GATE | `git diff origin/DEV HEAD` = EMPTY ✓ |
| VALGATE D-1 | PASS/WARN — advisory: portal-proxy.ts touches model_portfolios.benchmark SEV1 surface (T3 DEMO comment removal, no behavioral change; ramp not flipped, advisory-only) ✓ |
| TYPECHECK | PASS (tsc -b --noEmit via PROD push pre-push hook) ✓ |
| TAG | `portal-v2.1.121` → d9aed856 (CI auto-tag, confirmed on origin) |
| CI run | 27435893049 SUCCESS — Build (1m41s) + S3/CF deploy (13s) + Tag (9s) |
| ROLLBACK | `git push origin 5699f899:PROD` (v2.1.120) |
| Workspace pointer | `40b952a34` — bump portal → 8b6a6466; pushed CLOUD |
| RAVC2 | 20260612T185940Z → COO |
| RAVC3 | ACCEPTED 20260612T190043Z (LD-0185 discharged) |

## Bundle (origin/PROD 5699f899..origin/DEV 8b6a6466, 2 commits)

1. `b96822ad` feat(topic-cloud): clean 'sentiment is evolving' card for pending keyword intelligence
2. `8b6a6466` fix(NFRA_GRAPHS.D7): T1+T2+T3 — PlatinumAdvisorSummaryRaw type alias + InflecAdvisorBookRaw SCHEMA-DRIFT fields + ClientsTab type mismatch fix + portal-proxy DEMO comment removal

## Deployment sequence (Rule-19 ephemeral worktree)

- Phase 0: COO GO LD-0185 received in launch prompt + confirmed via inbox 20260612T183828Z.
- Phase 0 STEP-0: `git -C portal update-ref refs/heads/PROD refs/remotes/origin/PROD` → 5699f899.
- Phase 0 DEV PUSH: `git push origin DEV` (NO MSYS_NO_PATHCONV) → b96822ad..8b6a6466. VALGATE D-1 PASS/WARN.
- Phase 1 STALE WORKTREE: `.runtmp/portal-promote-v2120` still registered (physical dir unremovable, Windows long-path). Pruned git tracking; physical dir stays gitignored.
- Phase 2: `git worktree add /c/.../ajb_workspace/.runtmp/portal-promote-v2121 PROD` → 5699f899.
- Phase 3: `bun install` (backgrounded by Bash tool, exit 0 confirmed via task notification).
- Phase 4: `git merge --no-ff origin/DEV -m "..."` in worktree → d9aed856 (6 files, 152 insertions).
- Phase 4b: Parity diff EMPTY; inbox HALTGT check = clear.
- Phase 5 PUSH: `git push origin PROD` (NO MSYS_NO_PATHCONV) → VALGATE D-1 PASS/WARN + typecheck PASS → 5699f899..d9aed856.
- Phase 5 CI NOTE: `gh run watch` hung on verbose benign output (Node.js 20 deprecation warnings + cache 400); confirmed SUCCESS via `gh run view --json conclusion` = "success". Andrew queried stall; clarified immediately.
- Phase 6 TAG: `portal-v2.1.121` confirmed on origin via `git fetch --tags`.
- Phase 7 POINTER: `safe-commit.sh` → `40b952a34`; `git push origin CLOUD` → a34738082..40b952a34.
- Phase 8 CLEANUP: `git worktree prune` — physical .runtmp/portal-promote-v2121 remains (Windows long-path, gitignored). Main portal tree on DEV (8b6a6466) — Rule 19 intact.

## Compiler Tools

| Tool | When | Result |
|------|------|--------|
| VALGATE D-1 | DEV push (pre-push hook) | PASS/WARN (advisory SEV1 surface: portal-proxy.ts) |
| VALGATE D-1 | PROD push (pre-push hook) | PASS/WARN (same advisory) |
| tsc -b --noEmit | PROD push (pre-push hook) | PASS |
| CI Type Check | deploy.yml Build job | PASS |
| comp-pipescript | N/A — portal promote, no gold scripts | N/A |
| comp-transform | N/A — portal promote, no new components | N/A |

## Notes

- VALGATE D-1 advisory (portal-proxy.ts / model_portfolios.benchmark SEV1): This is the T3 DEMO comment removal. No behavioral change. COO confirmed: "D8-AE B5 advisory integration working correctly at the ruled tier."
- `gh run watch` output includes benign Node.js 20 deprecation warnings and cache 400 errors from CI infrastructure — these do not indicate failure. Always confirm outcome via `gh run view --json conclusion`.
