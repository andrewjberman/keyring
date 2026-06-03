# work 2111Z — Portal DEV->PROD promote v2.1.114 (Andrew GO via MSTR)

**archetype:** DEPLOY

## Current State — SHIPPED, PROD LIVE + CF-confirmed

Andrew direct to MSTR: *"make sure that newest portal build is deployed cleanly to prod, bring up
0.4.0_DT to do it."* MSTR relayed the GO `20260603T210359Z`. Executed the pre-staged+re-verified
one-step ship. Portal v2.1.114 live on PROD, edge flushed. Reported clean-deployed to MSTR (held
open) + RAVC2 to CTO + COO.

## Promote params

| Field | Value |
|-------|-------|
| DEV HEAD promoted | `850f70ba` (9-commit head) |
| PROD base | `9f890e0f` (v2.1.113) |
| MERGE SHA | `1695a754` (--no-ff) |
| TAG | `portal-v2.1.114` -> 1695a754 (CI auto-tag) |
| CF INVALIDATION | `I4SXWFOKRUAPB78FL2XX9YH6JA` = Completed (dist `EVTSA9VEHNZVH`) |
| deploy.yml | run `26913090198` SUCCESS |
| ROLLBACK | `git push origin 9f890e0f:PROD` (v2.1.113) |

## Bundle (9 commits, origin/PROD 9f890e0f .. origin/DEV 850f70ba)

1. `3e0ce8d0` fix(security): xlsx -> SheetJS CDN 0.20.3 (2 HIGH CVEs: proto-pollution + ReDoS)
2. `858bd374` fix(ModelPortfolios): Data Source panel firm-scope — Inflection=Orion not SmartX
3. `ed16010c` feat(keep-warm FIX2): useLambdaKeepWarm hook (FE warm-ping opal-partners-data)
4. `f2f62b17` fix(TaxCostBasisPanel): "Realized" -> "Realized (YTD)" label
5. `90f67b5e` refine(keep-warm FIX2): per-ping cache-buster + warm-route comment finalize
6. `8c3caf70` fix(deps): dep-sweep B1 — axios 1.17.0 + postcss 8.5.15 + vite 7.3.5
7. `13618900` docs(trade-submission): PMTRDX.001 canonical-unit note (comment-only)
8. `3b7dbea5` fix(deps): dep-sweep B2 — lodash override 4.18.1 (runtime, nivo/visx charts)
9. `850f70ba` fix(deps): dep-sweep B3 — eslint chain (dev-only)

## Deployment Sequence (5-phase, Rule 19 ephemeral worktree)

| Phase | Action | Result |
|-------|--------|--------|
| 0 PRE-SHIP GATE | re-confirm head + base + clean tree BEFORE irreversible merge | origin/DEV 850f70ba (no drift), origin/PROD 9f890e0f, 9 commits, main tree tracked-clean — all clean, nothing off |
| 0 STEP-0 | re-assert local PROD base | `git update-ref refs/heads/PROD refs/remotes/origin/PROD` -> 9f890e0f (banked footgun discipline) |
| 1-3 | ephemeral worktree from PROD (9f890e0f); `bun install` (423 pkgs); `git merge --no-ff origin/DEV` -> `1695a754`; `git diff --stat origin/DEV HEAD` **EMPTY** = byte-identical | clean |
| — HALTGT | inbox re-check before push | clear (only msg = the MSTR GO itself, no STOP-class) |
| 4 PUSH | `git push origin PROD` (NO MSYS_NO_PATHCONV) | VALGATE D-1 PASS (no-op); PROD typecheck PASS; pushed `9f890e0f..1695a754 PROD->PROD` |
| 4 CI | deploy.yml run `26913090198` | SUCCESS (build -> S3 -> CF-inval -> auto-tag) |
| 5 CF | invalidation `I4SXWFOKRUAPB78FL2XX9YH6JA` | Completed (edge flushed) |
| 5 TAG | CI auto-tag | `portal-v2.1.114` on 1695a754 |
| 6 CLEANUP | worktree remove + prune + robocopy dir-clean | main portal/ tree on DEV (850f70ba); only main in worktree list; localPROD = origin/PROD = 1695a754 (legit post-push, no pollution) |

## Verification

- Byte-identical to origin/DEV (850f70ba) — parity diff EMPTY.
- deploy.yml 26913090198 SUCCESS; CF invalidation I4SXWFOKRUAPB78FL2XX9YH6JA Completed.
- Rule-19 invariant: main tree on DEV; ephemeral worktree removed + pruned + dir cleaned.
- STEP-0 PROD-base discipline applied (no dry-run pollution this real promote since push advances origin/PROD legitimately).
- SERVED-PROD rendered e2e is CVO's; CTO owns the convene (smoke-scope in RAVC2).

## Tag-object note (post-ship MSTR verify, resolved)

MSTR's independent verify flagged `git ls-remote --tags origin portal-v2.1.114` -> `c8819c58`
(read as an "ancestor merge", suspected double-merge). Resolved: **c8819c58 is the
ANNOTATED-TAG OBJECT** (`git cat-file -t c8819c58` = `tag`), which peels to commit **1695a754**
(the PROD head): `git cat-file -p portal-v2.1.114` = `object 1695a754 / type commit`;
`refs/tags/portal-v2.1.114^{}` = 1695a754. deploy.yml uses `git tag -a` (annotated), so
`ls-remote --tags` shows the tag-object sha on the ref line and the commit only on the peeled
`^{}` line. No double-merge (origin/PROD = single merge 1695a754, parents 9f890e0f + 850f70ba);
the tag correctly marks the PROD head; no re-point needed. The "-> 1695a754" above is accurate.

## Compiler Tools

No comp-* — portal FE promote is git plumbing + CI + CloudFront. Change-gates: ci.yml on DEV
(GREEN, prior) + portal pre-push VALGATE D-1 (PASS no-op) + PROD typecheck (PASS).

## Next Steps

- **[CTO]** convene SERVED-PROD e2e CVO verify (ModelPortfolios Orion-scope / Realized-YTD / keep-warm / chart render lodash B2 / xlsx CDN).
- **[MSTR]** GO discharged; hold can close.
- Rollback path: `git push origin 9f890e0f:PROD` (v2.1.113).
