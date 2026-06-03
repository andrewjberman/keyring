# work 1826Z — v2.1.114 promote-readiness PRE-STAGE (COO drive, NOT promoted)

**archetype:** DEPLOY-READINESS (readiness-staging only; actual promote waits on Andrew GO)

## Current State — PRE-STAGED, builds clean, RAVC2'd to COO

COO `[DRIVE]` `20260603T181351Z` directed pre-staging the v2.1.114 promote so Andrew's
GO = instant ship. Executed all 4 steps; NOT promoted (waits on Andrew explicit GO).
RAVC2 sent to COO `20260603T182614Z`. RD-AI (0.4.2) build-layer green corroborated.
0.7.0 keep-warm coordination confirm sent (non-blocking).

## Bundle (origin/PROD 9f890e0f=v2.1.113 .. origin/DEV 8c3caf70 = exactly 6 FE commits)

1. `858bd374` fix(ModelPortfolios): firm-scope Data Source panel provider — Inflection=Orion not SmartX
2. `f2f62b17` fix(TaxCostBasisPanel): "Realized" -> "Realized (YTD)" bubble label
3. `ed16010c` feat(keep-warm FIX2): useLambdaKeepWarm hook — FE-driven warm-ping for opal-partners-data
4. `90f67b5e` refine(keep-warm FIX2): per-ping cache-buster + finalize warm-route comment to AE's deployed contract
5. `8c3caf70` fix(deps): FE dep-sweep Batch 1 — axios 1.17.0 + postcss 8.5.15 + vite 7.3.5 (in-caret)
6. `3e0ce8d0` fix(security): xlsx npm -> SheetJS CDN 0.20.3 patched build — kills 2 HIGH CVEs (proto-pollution + ReDoS)

## Readiness checks (all green)

| Step | Action | Result |
|------|--------|--------|
| 1 Rule-19 | portal main tree branch | DEV (HEAD 8c3caf70 == origin/DEV); not stranded |
| 2 bundle | 6 commits present on DEV | all present, clean |
| 2 merge | dry-run `git merge --no-ff --no-commit origin/DEV` into PROD worktree | CLEAN, zero conflicts (`--diff-filter=U` empty) |
| 2 tsc | `tsc -b` (via build) | PASS |
| 2 lint | `eslint .` | 0 errors, 18 warnings (preserve-manual-memo/unused-vars/exhaustive-deps — non-blocking, exit 0) |
| 3 worktree | `git worktree add ../.runtmp/portal-promote-prod PROD` + `bun install` | 419 pkgs (reflects dep-sweep lock) |
| 3 parity | local dry-run merge committed (NOT pushed) -> `git diff --stat origin/DEV HEAD` | EMPTY = byte-identical to DEV |
| 3 build | `tsc -b && vite build` | clean, exit 0, 1m1s; every page tree-shook; xlsx->SheetJS CDN builds clean |
| 3 teardown | worktree remove + prune + robocopy-mirror long-path clean | torn down (Rule-19 hygiene; re-stages ~3min on GO) |
| 4 keep-warm | buildWarmEndpoint() target | `/api/scoped/advisor-intelligence/filters?warm=1&firmId=<jwt>&_=<ts>` -> opal-partners-data Lambda; finalized to AE deployed contract (90f67b5e); reuses LIVE filters route -> promote-ready regardless. 0.7.0 confirm sent (non-blocking) |

## On Andrew GO (one-step ship)

Re-create worktree from PROD -> `bun install` -> `git merge --no-ff origin/DEV` -> verify
EMPTY diff -> HALTGT -> `git push origin PROD` (**NO MSYS_NO_PATHCONV** — mangles VALGATE D-1)
-> deploy.yml auto-tags **portal-v2.1.114** -> CF invalidation -> wait Completed -> teardown.
Rollback: `git push origin 9f890e0f:PROD` (v2.1.113).

## Flag (not mine)

Main DEV working tree has ONE uncommitted comment-only change: `src/api/endpoints/trade-submission.ts`
(PMTRDX.001 unit-contract doc, CTO ruling 2026-06-03, likely RD~B/PMTRDX lane). Does NOT enter
the promote (promote merges origin/DEV commits, not the working copy); comment-only (no tsc/build
impact). Left untouched per D2b (no reset/clean on shared tree). Owner should commit it.

## Coordination

- 0.4.2_RD_AdvisorIntelligence: sent build-layer green + manifest for all 6 commits; corroborates my worktree build. Authenticated pixel smoke = Andrew at promote (his GO gate).
- 0.7.0_AE_CloudOps: non-blocking confirm sent re keep-warm Lambda short-circuit + Track-2/security surface impact on the filters route.

## Compiler Tools

No comp-* — portal FE readiness-stage is git plumbing + bun build + worktree mechanics, not a
Lambda/script/IAM edit. Gates were tsc -b + eslint + full vite build + merge-conflict scan.

## Next Steps

- **[Andrew]** GO gate = authenticated pixel smoke on DEV (RD-AI/COO note creds wall).
- **[DT]** on GO: execute the one-step ship above.
- **[0.7.0]** reply to keep-warm contract confirm (non-blocking).
