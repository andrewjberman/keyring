# work 2142Z — Portal v2.1.116 DEV->PROD promote: SHIPPED, PROD LIVE

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

## Current State — SHIPPED, PROD LIVE, sleeve code served-verified; AE data-API flush in flight

COO GO (Andrew confirmed Total Holdings on DEV): promote d18cd8c8 (Portfolio Analytics Total
Holdings = sleeve-level / blend-split, 7,301->7,465 Global), single commit on v2.1.115 base.
Executed Rule-19 ephemeral-worktree promote. Live on PROD; sleeve code confirmed in served bundle.

## IMPORTANT — idle-gap root cause (banked footgun)

After the worktree-add + bun install backgrounded (exit 0), the SESSION PARKED waiting on the
background completion notification and did NOT auto-advance to the merge -> ~26 min silent gap
(broker-LIVE + zero promote artifacts + frozen summary). Andrew caught it directly ("split holdings
sleeve not in live build yet"); COO progress-check converged. Root cause is structural, not an error:
a backgrounded long-op whose completion notification doesn't auto-trigger the next deploy step.
COO banking fabric-wide. GOING-FORWARD MITIGATION: run `bun install` FOREGROUND on promotes (or an
explicit until-exit wait that auto-advances) so the session never parks on a notification that may
not fire the next step.

## Promote params

| Field | Value |
|-------|-------|
| DEV HEAD promoted | `d18cd8c8` (single commit, no drift) |
| PROD base | `131d081d` (v2.1.115) |
| MERGE SHA | `d2cb18b9` (--no-ff) |
| PARITY GATE | `git diff origin/DEV HEAD` = EMPTY (byte-identical to Andrew-confirmed d18cd8c8) |
| TAG | `portal-v2.1.116` -> d2cb18b9 (CI auto-tag, annotated, peel-verified) |
| deploy.yml | run `27041518697` SUCCESS (git-128 on tolerated Tag step = non-fatal, tag landed) |
| CF (FE assets, CI) | Completed (fresh index-4UfgWU7O.js served 200) |
| CF (data-API, AE) | flush signaled to 0.7.0_AE (in flight) |
| ROLLBACK | `git push origin 131d081d:PROD` (v2.1.115) |

## Bundle (1 commit, origin/PROD 131d081d .. origin/DEV d18cd8c8)

1. `d18cd8c8` feat(ModelPortfolios): Portfolio Analytics Total Holdings = sleeve-level (blend-split, 7301->7465 Global)

## Deployment sequence (Rule-19 ephemeral worktree)

- Phase 0 PRE-SHIP GATE: origin/DEV d18cd8c8 (no drift), origin/PROD 131d081d, 1 commit, main tree DEV.
- Phase 0 STEP-0: `git update-ref refs/heads/PROD refs/remotes/origin/PROD` -> 131d081d.
- Phase 1-3: ephemeral worktree (.runtmp/portal-promote-v2116) from PROD; bun install (exit 0); `git merge --no-ff origin/DEV` -> d2cb18b9 (1 file, +18/-1); parity diff EMPTY.
  [GAP HERE — see idle-gap root cause above; Andrew+COO unstuck]
- HALTGT: inbox re-check before push = clear (COO sync/progress msgs, no STOP-class).
- Phase 4 PUSH: `git push origin PROD` (NO MSYS_NO_PATHCONV) -> VALGATE D-1 PASS + PROD typecheck PASS -> 131d081d..d2cb18b9.
- Phase 4 CI: deploy.yml 27041518697 SUCCESS.
- Phase 5: CF (CI FE-asset inval) + tag portal-v2.1.116.
- Phase 5b: signaled AE -> data-API CF flush (in flight).
- Phase 6 CLEANUP: worktree de-registered (worktree list = only main on DEV); Rule-19 intact (main tree DEV d18cd8c8; local PROD = origin/PROD = d2cb18b9). Physical .runtmp leftover gitignored.

## Verification (DT-reachable)

SERVED-PROD sleeve code confirmed LIVE not stale:
- index served 200, fresh bundle index-4UfgWU7O.js.
- ModelPortfolios chunk hash CHANGED CLvJh6i4 (v2.1.115) -> GSwwcBlO (v2.1.116), size 87527->87681
  (+154B, consistent with the +18-line sleeve add) served 200:
  - "Total Holdings" x2 = sleeve-level code (d18cd8c8) LIVE.
  - "50/50 INT/LT" x11 + "Opal Blend 5050" x2 + account_count x29 + aggregate x19 = prior commits preserved (no regression).
  (7,465 is a COMPUTED value, not a literal -> not grep-able; "Total Holdings" label + chunk-hash change + size growth = served proof.)

DEFERRED to Andrew-sovereign / CVO (PROD auth wall, data-API 401 anon = Lambda@Edge auth not stale cache):
the rendered-pixel Total Holdings reading 7,465 Global. Andrew already confirmed on DEV ("looks good on DEV").

## Compiler Tools

None — portal FE promote (git plumbing + CI + CloudFront). Gates run: VALGATE D-1 PASS + PROD typecheck PASS + deploy.yml SUCCESS.

## Next Steps

- **[AE]** data-API CF flush ID (in flight).
- **[COO]** RAVC2 close on co-verify.
- **[CTO->CVO]** rendered Total Holdings 7,465 verify behind auth.
- Rollback: `git push origin 131d081d:PROD` (v2.1.115).
