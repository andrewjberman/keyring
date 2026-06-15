# work 2154Z — Portal v2.1.120 DEV->PROD promote: SHIPPED, PROD LIVE

**archetype:** DEPLOY

## Current State — SHIPPED, PROD LIVE; MDPF per-source timestamps active

COO-authorized second promote during same session: c6f12701 (fix MDPF_CADENCE:
per-source timestamps + divergence guard for Portfolio Analytics panel) → PROD
as portal-v2.1.120. DE had committed this locally to DEV immediately after our
first promote; COO RAVC2-ACCEPTED and dispatched.

## Promote params

| Field | Value |
|-------|-------|
| DEV HEAD promoted | `c6f12701` (fix MDPF_CADENCE: per-source timestamps + divergence guard for Portfolio Analytics panel) |
| PROD base | `b742e252` (v2.1.119 — first promote this session) |
| MERGE SHA | `5699f899` (--no-ff) |
| PARITY GATE | `git diff origin/DEV HEAD` = EMPTY ✓ |
| VALGATE D-1 | PASS (no-op — no api/endpoints/*.ts changed) ✓ |
| TYPECHECK | PASS (tsc -b --noEmit via PROD push pre-push hook) ✓ |
| TAG | `portal-v2.1.120` → 5699f899 (CI auto-tag, matches COO target) |
| CI run | 27238319958 SUCCESS — Build (1m35s) + S3/CF deploy (10s) + Tag (5s) |
| ROLLBACK | `git push origin b742e252:PROD` (v2.1.119) |

## Bundle (origin/PROD b742e252..origin/DEV c6f12701, 1 commit)

1. `c6f12701` fix(MDPF_CADENCE): per-source timestamps + divergence guard for Portfolio Analytics panel (ModelPortfolios.tsx, +21/-1)

## Deployment sequence (Rule-19 ephemeral worktree)

- Phase 0: COO RAVC2-ACCEPT on v2.1.119 + second promote dispatch; DE confirmed origin/DEV updated (c6f12701).
- Phase 0 STEP-0: `git update-ref refs/heads/PROD refs/remotes/origin/PROD` → b742e252.
- Phase 1: `git worktree add .runtmp/portal-promote-v2120 PROD` → b742e252.
- Phase 2: bun install (backgrounded by Bash tool runtime, exit 0 confirmed).
  WORKTREE CWD NOTE: bun install with absolute cd path ran in background → did NOT persist CWD to worktree. Merge command had incorrect cd path on first attempt (ran in main portal/ DEV, got "already up to date"). Fixed by explicit `cd /absolute/path/to/worktree && git merge`.
- Phase 3: `git merge --no-ff origin/DEV -m "..."` in worktree (via absolute cd) → 5699f899 (1 file, +21/-1).
- Phase 4: Parity diff EMPTY; inbox HALTGT check = clear (COO GO received mid-flow — already executing).
- Phase 5 PUSH: `git push origin PROD` (NO MSYS_NO_PATHCONV) → VALGATE D-1 PASS + typecheck PASS → b742e252..5699f899.
- Phase 5 CI: deploy.yml 27238319958 SUCCESS.
- Phase 6 CLEANUP: `git worktree prune` (physical .runtmp leftover gitignored — Windows filename-too-long prevents rm).

## Session total (both promotes)

| Promote | Commit | Tag | SHA |
|---------|--------|-----|-----|
| First | ADVI_PRTORG.04 Cottonwood | portal-v2.1.119 | b742e252 |
| Second | MDPF per-source timestamps | portal-v2.1.120 | 5699f899 |

## Compiler Tools

| Tool | When | Result |
|------|------|--------|
| VALGATE D-1 | PROD push (pre-push hook) | PASS (no-op) |
| tsc -b --noEmit | PROD push (pre-push hook) | PASS |
| CI typecheck | deploy.yml Build job | PASS |
| comp-pipescript | N/A — portal promote, no gold scripts | N/A |
| comp-transform | N/A — portal promote | N/A |
