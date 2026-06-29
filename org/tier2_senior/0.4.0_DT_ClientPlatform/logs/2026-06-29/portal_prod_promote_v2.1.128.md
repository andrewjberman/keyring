# Portal DEV->PROD Promote — v2.1.128

**archetype:** DEPLOY

**Serial:** 0.4.0_DT_ClientPlatform
**Window:** session start 2026-06-29 ~2059Z -> ~2111Z (single task: /prod-deploy, Andrew-direct)

## Summary

Andrew-direct `/prod-deploy`. Promoted 6 commits on portal `origin/DEV` ahead of `origin/PROD`
to production as **v2.1.128**. Clean run through the canonical DT procedure; CI green; tag
peel-verified; main tree confirmed back on DEV.

## Deployment Sequence

1. /watcher self-heal: was NOT REGISTERED -> registered LIVE; persistent inbox Monitor armed
   (task bnq6512ie). Inbox empty, no pending HALT/STOP.
2. FREEZE declared to COO (promote merges LIVE origin/DEV at GO, not a frozen snapshot).
3. Step 1-2: portal main tree on DEV, clean (only untracked gitignored residue); local DEV ==
   origin/DEV (nothing to push). `bun run typecheck` -> tsc -b --noEmit EXIT 0.
4. Step 3: re-asserted local PROD from origin (git update-ref) -> 95703cc8.
5. Step 4: ephemeral worktree on PROD. FIRST add blocked by a STALE prior worktree
   (.runtmp/portal-promote-20260626T181234Z) holding PROD -> force-remove (physical delete
   failed long-path, but git tracking freed) + prune -> re-add succeeded. Foreground
   `bun install` (420 pkgs, 145s, EXIT 0). `git merge --no-ff origin/DEV` -> 5c9e5784.
6. Parity gate `git diff origin/DEV HEAD` -> EMPTY (OK).
7. `git push origin PROD` -> VALGATE D-1 PASS (no adapter files) + tsc PASS -> 95703cc8..5c9e5784.

## Verification (actual output)

- CI run **28402659869**: `{"conclusion":"success","status":"completed","headSha":"5c9e5784..."}`
- Tag **portal-v2.1.128** peeled: `git rev-parse portal-v2.1.128^{commit}` = 5c9e5784 ==
  `origin/PROD` head 5c9e5784 (MATCH).
- Main tree `git -C portal branch --show-current` = DEV.

## Commits promoted (origin/PROD..origin/DEV)

| Hash | Summary |
|---|---|
| 6089c7a6 | guard(inflection): dev-only ADVI_PARTNER_AUTHZ FE-regression assert (non-admin never offered admin tab) |
| adda3e0e | feat(inflection): hide Profile tab for bookless non-admin firm viewers (no advisorId) — Andrew-direct |
| dcb5d227 | fix(firmAccess): exempt /change-password from per-firm path matrix (forced-pw redirect-loop -> blank grey) |
| 21f2178d | fix(firmAccess): cottonwood.com -> cottonwoodmail.com (unblocks 3 @cottonwoodmail.com logins) |
| 42c11d41 | COTMVP D3: young-tenant year/quarter UX (auto-fit interval, maxBarSize cap, limited-history banner, NMEC=0 clarifier) on shared PartnerAnalytics |
| f071b6b1 | COTMVP D2: .quarters tenant-schema guard on shared PartnerAnalytics (COT BD-schema divergence hardening, inert) |

## Files Modified (by the merge)

src/lib/firmAccess.ts; src/.../_partners/inflection/index.tsx; src/.../_shared/components/PartnerAnalytics.tsx
(see promoted commit messages above for per-file detail.)

## Compiler Tools

| Tool | Why | Result |
|---|---|---|
| (none) | Portal git/CI promote (DT lane) — no estate search/inspection/IAM/data-path change in scope; the promote's own gates (VALGATE D-1, tsc, CI deploy.yml, parity diff, tag-peel) are the verification surface. | n/a |

No comp-* tool fits a pure DEV->PROD git promote; the canonical gate chain covered verification.

## Current State

Portal **LIVE on PROD at v2.1.128** (`5c9e5784`), CI run 28402659869 success, tag portal-v2.1.128
peel-verified. Main `portal/` tree back on DEV (`6089c7a6`). Workspace gitlink already records
DEV HEAD 6089c7a6 — **no pointer bump** (promote merged DEV->PROD without advancing DEV). Freeze
window RELEASED to COO. Promote worktree git-tracking pruned; physical `.runtmp/portal-promote-*`
residue persists (Windows long-path, gitignored, inert). Rollback SHA = 95703cc8 (prev v2.1.127),
encoded in the merge message.

## Next Steps

- [2.0.0_SA_COO] FREEZE RELEASED reported; portal/DEV pushes may resume. No close-trigger flagged.
- DT idle/available, event-driven; Monitor armed (bnq6512ie).
