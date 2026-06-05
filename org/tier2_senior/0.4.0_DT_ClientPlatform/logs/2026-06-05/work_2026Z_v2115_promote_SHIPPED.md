# work 2026Z — Portal v2.1.115 DEV->PROD promote: SHIPPED, PROD LIVE + CF-flushed

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

## Current State — SHIPPED, PROD LIVE, edge flushed, FE-code served-verified

Andrew GO (via MSTR) PATH B = ship all 3 coupled commits. Executed the Rule-19 ephemeral-worktree
promote. Portal v2.1.115 live on PROD, edge flushed (FE assets via CI + data-API paths via AE).
FE code of all 3 commits served-verified in the live PROD bundles. RAVC2 to COO.

## Scope resolution (the held fork)

A 3rd commit (86f7e8da, DE Andrew-direct ModelPortfolios blend-roll) landed on origin/DEV during my
startup, coupled to Bug-2 (its body: "supersedes the producer-side blend-split"). Held + flagged
MSTR (good-catch confirmed) -> MSTR escalated to Andrew -> Andrew: "All 3 -- I already eyeballed the
blend-roll." => PATH B, no separate smoke gate. Live-DEV-remerge footgun handled correctly (did not
silently sweep; did not auto-decide a coupled PROD-content question).

## Promote params

| Field | Value |
|-------|-------|
| DEV HEAD promoted | `86f7e8da` (3-commit head, no drift at ship) |
| PROD base | `1695a754` (v2.1.114) |
| MERGE SHA | `131d081d` (--no-ff) |
| PARITY GATE | `git diff origin/DEV HEAD` = EMPTY (byte-identical to Andrew-confirmed 86f7e8da) |
| TAG | `portal-v2.1.115` -> 131d081d (CI auto-tag, annotated; peel verified) |
| deploy.yml | run `27038063420` SUCCESS (Build 1m31s + Deploy-S3+CF 9s + Tag 7s, all green) |
| CF (FE assets, CI) | `ICQPUZFLF2I8JDTXVKQIGDJT0J` = Completed (EVTSA9VEHNZVH) |
| CF (data-API, AE) | `I28A6LWFSQID3J22I48YVNMD3X` = Completed (/api/general/portfolios/* + /api/general/mdpf/*) |
| ROLLBACK | `git push origin 1695a754:PROD` (v2.1.114) |

## Bundle (3 commits, origin/PROD 1695a754 .. origin/DEV 86f7e8da)

1. `62767be0` fix(MDPF_COUNTS Part-4): Global Count toggle -> cross-partner-union account_count (7095)
2. `253045ec` fix(MDPF_COUNTS Bug-2): Global VALUE trend -> MDPF aggregate ($1.808B, fresh+union)
3. `86f7e8da` feat(ModelPortfolios): FE-roll 50/50 blends into archetype models (Andrew-direct; supersedes producer-side blend-split)

## Deployment sequence (Rule-19 ephemeral worktree)

- Phase 0 PRE-SHIP GATE: origin/DEV 86f7e8da (no drift), origin/PROD 1695a754, 3 commits, main tree DEV clean.
- Phase 0 STEP-0: `git update-ref refs/heads/PROD refs/remotes/origin/PROD` -> 1695a754 (no dry-run pollution).
- Phase 1-3: ephemeral worktree (.runtmp/portal-promote-v2115) from PROD; `bun install` (420 pkgs); `git merge --no-ff origin/DEV` -> 131d081d; parity diff EMPTY.
- HALTGT: inbox re-check before push = clear (no STOP-class).
- Phase 4 PUSH: `git push origin PROD` (NO MSYS_NO_PATHCONV) -> VALGATE D-1 PASS (no-op) + PROD typecheck PASS -> 1695a754..131d081d.
- Phase 4 CI: deploy.yml 27038063420 SUCCESS. (Annotations: Node20-deprec + GH cache-svc 400 + a git-128 on a tolerated step -> all non-fatal; 3 jobs green, tag landed.)
- Phase 5: CF (CI FE-asset inval Completed) + tag portal-v2.1.115.
- Phase 5b: signaled AE (armed) -> data-API CF flush Completed; AE origin-verified $1.808B exact + blend union.
- Phase 6 CLEANUP: ephemeral worktree de-registered (worktree list = only main on DEV); physical dir leftover under gitignored .runtmp/ (Windows long-path node_modules; cosmetic). Rule-19 intact: main tree DEV (86f7e8da); local PROD = origin/PROD = 131d081d (legit post-push).

## Verification (DT-reachable layer)

SERVED-PROD FE code (the deliverable I own) — confirmed live, not stale:
- index served 200, fresh bundle index-fQ91pIny.js (account_count x15).
- ModelPortfolios route chunk ModelPortfolios-CLvJh6i4.js served 200 (87527 bytes):
  - "50/50 INT/LT" x11 + "Opal Blend 5050" x2 = blend-roll (86f7e8da) LIVE.
  - account_count x26 + aggregate x19 = Part-4 (62767be0) + Bug-2 (253045ec) LIVE.
- Data origin fresh + edge flushed (AE): aum-metrics total $1,807,839,716.27 = $1.808B exact; donut identity exact; aggregate-aua-timeseries union correct (FE rolls to INT 1923).

DEFERRED to Andrew-sovereign / CVO (PROD auth wall — data-API paths return 401 anon, same as
v2.1.113/114; this is Lambda@Edge auth, NOT stale cache): the rendered-pixel data values
(Global Count 7095 + Global VALUE $1.808B visually + blend-roll chart render). Andrew already
visually confirmed the underlying state on DEV (200118Z + blend-roll eyeball). CTO convenes the
SERVED-PROD e2e CVO rendered verify per the standing pattern.

Note: 7095 (Global Count toggle, model-portfolio cross-partner-union) != 7301 (total funded accts in
account-distribution.json) — different metrics, both correct; FE wires account_count to the aggregate union.

## Compiler Tools

None — portal FE promote is git plumbing + CI + CloudFront (no gold/portal-component edit by me).
Change-gates that ran: portal pre-push VALGATE D-1 (PASS no-op) + PROD typecheck (PASS) + ci.yml/deploy.yml (SUCCESS).

## Next Steps

- **[COO]** RAVC2 close (this log + commits/tag + CF IDs + served-FE-code verify).
- **[CTO]** convene SERVED-PROD e2e CVO rendered verify (Global Count 7095 / Global VALUE $1.808B / blend-roll chart) behind auth.
- **[MSTR]** GO discharged.
- Rollback path: `git push origin 1695a754:PROD` (v2.1.114).
