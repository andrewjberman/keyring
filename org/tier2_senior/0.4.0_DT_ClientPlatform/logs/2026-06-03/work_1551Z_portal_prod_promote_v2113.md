# work 1551Z — Portal DEV->PROD promote v2.1.113 (3 FE commits, Andrew-direct GO)

**archetype:** DEPLOY

## Current State — SHIPPED, PROD LIVE + CF-confirmed

Andrew direct-GO'd (CONFIRMED to MSTR), relayed via CTO `[PROMOTE PACKET]`
`20260603T153448Z`. Rule-19 ephemeral-worktree DEV->PROD promote complete; portal
v2.1.113 live on PROD, edge flushed. RAVC2 sent to CTO (1.0.0_SA_CTO) + COO
(2.0.0_SA_COO). CTO convenes the SERVED-PROD e2e CVO verify on the new bundle.

## Promote params

| Field | Value |
|-------|-------|
| DEV HEAD promoted | `21be552d` |
| PROD base | `6549038c` (v2.1.112) |
| MERGE SHA | `9f890e0f` (merge DEV->PROD, --no-ff) |
| TAG | `portal-v2.1.113` -> 9f890e0f (CI auto-tag job) |
| CF INVALIDATION | `I1SS2I0VPUI1X1TAVJ5AZT4TPM` = Completed (dist `EVTSA9VEHNZVH`) |
| ROLLBACK | `git push origin 6549038c:PROD` (v2.1.112) |

## Bundle (verified origin/PROD..origin/DEV = exactly these 3)

1. `548c9d7d` fix(ModelPortfolios): firm-scope source attribution (Inflection->Orion, 49F->SmartX)
2. `b5d3e923` feat(ADVI_FEREFI.W1): Advisor Intelligence FE refinements items 1-5
3. `21be552d` fix(ADVI): drop retry:false on deep drilldown (FIX1 cold-start self-heal)

## Deployment Sequence (canonical 5-phase, Rule 19 ephemeral worktree)

| Phase | Action | Result |
|-------|--------|--------|
| 1 COMMIT | portal main tree status | On DEV; HEAD == origin/DEV (21be552d); 0 unpushed; only gitignored scratch untracked |
| 2 LINT | ci.yml on DEV head | run `26891088761` on 21be552d = SUCCESS (lint+tsc+build) |
| 3 PUSH DEV | origin/DEV parity | already AT 21be552d (nothing to push) |
| 4 MERGE | ephemeral worktree `../.runtmp/portal-promote-prod` from PROD; `bun install` (423 pkgs, 191s); `git merge --no-ff origin/DEV` -> MERGE `9f890e0f` (7 files, +48/-141); `git diff --stat origin/DEV HEAD` **EMPTY** = PROD tree byte-identical to DEV |
| — HALTGT | inbox re-check before irreversible push | clear (inbox empty, no STOP-class) |
| 5 DEPLOY | `git push origin PROD` (MSYS_NO_PATHCONV NOT exported); VALGATE D-1 = PASS (no-op, no api/endpoints/*.ts changed); PROD pre-push typecheck PASS; pushed `6549038c..9f890e0f PROD -> PROD` |
| 5 CI | deploy.yml run `26896037317` | SUCCESS (build -> S3 sync -> CF invalidate -> auto-tag, all jobs green) |
| 5 CF | CloudFront invalidation | `I1SS2I0VPUI1X1TAVJ5AZT4TPM` = Completed (edge flushed) |
| 5 TAG | CI auto-tag | `portal-v2.1.113` on 9f890e0f (deploy.yml tag job auto-bumped from v2.1.112) |
| 5 CLEANUP | worktree remove + prune; Rule 19 invariant | worktree de-registered; physical dir long-path-cleaned via robocopy-mirror; `git worktree list` shows only main on DEV |

## Notes

- **MSYS_NO_PATHCONV footgun avoided** (per memory `feedback_no_msys_pathconv_on_portal_git_push`):
  did NOT export it for the push; VALGATE D-1 hook ran clean first try (no false D-1 block).
- deploy.yml `tag` job auto-computes+pushes the next patch tag from the latest `portal-v*` —
  no manual tag needed (confirmed v2.1.112 -> v2.1.113).
- Non-fatal deploy annotations: Node-20-deprecation notice + GitHub Actions cache-service
  infra hiccup (cache save/restore 400) — neither affects build/deploy correctness; run = success.

## Verification

- PROD tree byte-identical to origin/DEV (21be552d) — `git diff --stat origin/DEV HEAD` EMPTY.
- deploy.yml 26896037317 SUCCESS (all jobs); CF invalidation I1SS2I0VPUI1X1TAVJ5AZT4TPM Completed.
- Rule 19 invariant: main portal/ tree on DEV; ephemeral worktree removed + pruned.
- Rendered-pixel e2e on SERVED PROD is CVO's; CTO owns the convene (smoke-scope in RAVC2).

## Smoke-scope (per packet, for Andrew/CTO on new live)

- Model Portfolios footnote: Inflection="Source: Orion Portfolio Solutions." / 49F="Source: SMArtX Advisory Solutions."
- Assets Overview loads Year interval + 3Y window
- No "(pseudonymized)" label anywhere (cleartext-denied still sees pseudonymized values)
- No Segment-Analytics search bar (both firms); cohort list still works
- Lifetime Activity loads Max + Year; AUM-mode tooltip shows period-over-period delta-$ + delta-%
- FIX1: deep ADVI drilldown -> idle several min -> click -> data loads (no false "no data"), cold-Lambda

## Compiler Tools

No comp-* — portal FE promote is git plumbing + CI + CloudFront, not a Lambda/script/IAM edit.
Change-gates were ci.yml (DEV, GREEN) + portal pre-push VALGATE D-1 (PASS no-op) + PROD typecheck (PASS).

## Next Steps

- **[CTO]** convene SERVED-PROD e2e CVO verify on the new live bundle.
- **[CVO]** rendered-pixel smoke per smoke-scope above.
- Rollback path if needed: `git push origin 6549038c:PROD` (v2.1.112).
