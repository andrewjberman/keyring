# work 2015Z — Portal v2.1.115 DEV->PROD promote: STAGED + HELD on scope fork

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, COORDINATE

## Current State — HELD pending MSTR scope call (NOT stuck)

MSTR spawn (COO drive cyc22): promote portal DEV->PROD carrying the 2 Andrew-VISUALLY-CONFIRMED
(200118Z) FE commits 62767be0 (Part-4 Global Count union 7095) + 253045ec (Bug-2 Global VALUE
MDPF re-point .808B). Ran /watcher + org/XXX startup. Base verified clean. Discovered a 3rd commit
landed on origin/DEV DURING startup -> flagged MSTR (GO owner) + COO, holding the push.

## Base state (Phase 0 — all clean)

| Field | Value |
|-------|-------|
| origin/PROD (base) | 1695a754 = portal-v2.1.114 |
| local PROD | re-asserted to origin/PROD via `git update-ref refs/heads/PROD refs/remotes/origin/PROD` (footgun discipline) -> 1695a754, no dry-run pollution |
| main portal tree | on DEV (Rule-19 intact) |
| worktree list | only main (no stranded ephemeral) |
| next tag | portal-v2.1.115 (CI auto-tag via deploy.yml `git tag -a`) |

## The scope fork

`portal-promote.sh` wrapper is MISSING (Rule-19 structural enforcement deferred 2026-05-26, never
scribed) — manual ephemeral-worktree promote per my v2.1.113/114 procedure.

origin/PROD..origin/DEV = **3 commits**, not the 2 in MSTR's GO:
- 62767be0  Part-4 Global Count        (Andrew-confirmed, in GO)
- 253045ec  Bug-2 Global VALUE         (Andrew-confirmed, in GO, named as head)
- 86f7e8da  feat(ModelPortfolios): FE-roll 50/50 blends into archetype models (Andrew-direct)
            -- author 0.4.0_DE_ClientPlatform, landed 2026-06-05 16:12 EDT DURING my startup
            -- build/runtime-impact: src/pages/ModelPortfolios.tsx + src/lib/modelPortfolioColors.ts
            -- Andrew-DIRECTED but NOT in MSTR GO + NOT stated Andrew-visual-confirmed-for-promote
            -- body: "Supersedes the producer-side blend-split (FE-side per Andrew)" => COUPLED to
               Bug-2/253045ec's Global VALUE re-point

Live-DEV-remerge footgun realized (memory feedback_portal_promote_remerges_live_dev_at_go_not_frozen_snapshot):
a new origin/DEV commit silently became the 3rd in the "ready" bundle. Did NOT sweep it in.

## Options surfaced to MSTR

- (A) PIN to 253045ec = exactly the confirmed 2-commit GO; hold 86f7e8da for follow-on GO.
      Safe-direction but risks shipping a Bug-2 half-state (without the FE blend-roll that
      supersedes the producer split). Leaves DEV 1 ahead of PROD.
- (B) INCLUDE 86f7e8da (ship origin/DEV head) = coupled set together; needs a 30s visual smoke
      on the blend-roll since GO confirm (200118Z) predates it.
- REC: (B) if Andrew already eyeballed the blend-roll on DEV; else (A) now + 86f7e8da next.

## Coordination

- Flagged 0.0.0_AB_MSTR (LIVE 1s) [SCOPE-FORK] + CC 2.0.0_SA_COO [FYI]. No push fired.
- On MSTR's word: fire chosen path -> signal 0.7.0_AE (ARMED to CF-flush EVTSA9VEHNZVH on
  /api/general/portfolios/* + /api/general/mdpf/*) -> co-verify served PROD (account_count + .808B)
  -> RAVC2 COO.

## Compiler Tools

None — portal FE promote is git plumbing + CI + CloudFront (no gold/portal-component edit by me).
Change-gates that WILL run on push: portal pre-push VALGATE D-1 + PROD typecheck + ci.yml.

## Next Steps

- **[MSTR]** pick (A) pin-253045ec vs (B) include-86f7e8da (+ confirm blend-roll visually smoked).
- **[DT]** fire chosen path instantly on reply; main tree stays DEV; ephemeral worktree.
- **[0.7.0_AE]** CF flush post-push (already armed).
- Rollback path: `git push origin 1695a754:PROD` (v2.1.114).
