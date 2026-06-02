# work 2145Z — Portal FULL DEV->PROD promote v2.1.112 (Andrew-direct stacked Inflection FE)

**archetype:** DEPLOY

## Current State — SHIPPED, PROD LIVE + CF-confirmed

Andrew-direct GO (verbatim: *"yep this works, ask MSTR for 0.4.0_DT and get the tree cleaned up,
dev pushed, prod deployed"*) relayed via COO `[DISPATCH]` `20260602T...Z` (TO `da5a57e0c`) + CTO
belt-and-suspenders. Andrew's DEV-local smoke GREEN (Peter admin + Joe non-admin login/Profile/
Distribution). The full stacked Inflection FE bundle is now live on PROD. RAVC2 sent to COO+CTO+CVO,
FYI to AE.

## Promote params (CTO-VERIFIED GO target)

| Field | Value |
|-------|-------|
| DEV HEAD promoted | `23982a8c` (full: 23982a8ce45e092a39ab70bb2e8c01ea90cb43dc) |
| GO-target note | 23982a8c = `c009f98c` + the `advisors-guard harden` (ADVI_INFPRM P2 CVO/CTO defense-in-depth). The directive *named* c009f98c, but DEV had advanced +1 to the hardening commit. Per COO/CTO dispatch: promote 23982a8c, **NOT** c009f98c (which drops the guard). a9434226e is a PHANTOM (main-repo log sha, not a portal commit). |
| ROLLBACK | `a33c230f` (v2.1.111, prior PROD) |
| Bundle (all CVO-cleared, backend/data already live) | INFPRM all-legs (W1+W2-FE+W4a-f+advisors-guard) + INFOTD (AUM relabel + Count) + INFNNA-W2FE + S5 firm-scoping + NNA-tooltip |

## Deployment Sequence (canonical 5-phase, Rule 19 ephemeral worktree)

| Phase | Action | Result |
|-------|--------|--------|
| 1 COMMIT | portal main tree status | On DEV; no uncommitted tracked changes; local HEAD == origin/DEV (23982a8c); 0 unpushed |
| 2 LINT | ci.yml on DEV head | run `26848295466` on 23982a8c = SUCCESS (lint + tsc + build GREEN) |
| 3 PUSH DEV | origin/DEV parity | already AT 23982a8c (nothing to push) |
| 4 MERGE | ephemeral worktree `../.runtmp/portal-promote-prod` from origin/PROD; `bun install` (423 pkgs, fresh worktree needs node_modules for pre-push tsc gate); `git merge --no-ff origin/DEV` -> MERGE `6549038c`; `git diff --stat origin/DEV HEAD` **EMPTY** = PROD tree byte-identical to DEV |
| — HALTGT | inbox re-check before irreversible push | clear of STOP-class (only inbox msg = the COO GO dispatch itself) |
| 5 DEPLOY | `git push origin PROD` -> deploy.yml | VALGATE D-1 adapter-threading = PASS/WARN (non-blocking schema-drift WARNs on 3 partner-facing adapters: getPlatinumAdvisorDrilldownSummary / getPlatinumAdvisorSummary / getPlatinumClientSummary); PROD pre-push typecheck PASS; pushed `a33c230f..6549038c PROD -> PROD` |
| 5 CI | deploy.yml run `26849695098` | SUCCESS (Build -> S3 sync -> CloudFront invalidate -> Tag, all jobs green) |
| 5 CF | CloudFront invalidation | `IBINYEKL00J1C6E4V1XWQCPH4Z` = Completed (edge flushed) |
| 5 TAG | auto-tag | `portal-v2.1.112` on 6549038c; origin/PROD now 6549038c |
| 5 CLEANUP | worktree remove + prune; Rule 19 invariant | worktree de-registered (`git worktree list` shows only main on DEV); main portal/ tree verified on DEV; scratch dir long-path-cleaned via robocopy-mirror trick |

## Deployment Tags
| Pipeline | Tag | Commit |
|----------|-----|--------|
| portal | portal-v2.1.112 (CI auto) | 6549038c (PROD) |

## Incident — first-push false-block (diagnosed + recovered)

First `git push origin PROD` was BLOCKED by VALGATE D-1, but **not a real gate failure**: a stray
`export MSYS_NO_PATHCONV=1` (carried into the push command) prevented Git Bash from converting the
hook's `/c/Users/.../d1_adapter_threading_gate.py` path to `C:\Users\...`, so Windows python received
`/c/...` literally and resolved it to the non-existent `C:\c\Users\...`. The gate script file
couldn't be opened -> hook fail-closed. typecheck itself PASSED in that same run. Inspected
`portal/.git/hooks/pre-push` to confirm the gate logic vs the path bug, retried the push with
`MSYS_NO_PATHCONV` unset -> D-1 ran clean (PASS/WARN) + pushed.

**Lesson:** do NOT export `MSYS_NO_PATHCONV=1` for portal git pushes — the portal pre-push hook relies
on Git Bash `/c/` -> `C:\` path conversion to locate the D-1 gate script. The env var is for Terraform
imports / AWS-CLI ARN args only (CLAUDE.md Git section), never for `git push`.

## Verification
- PROD tree byte-identical to origin/DEV (23982a8c) — `git diff --stat origin/DEV HEAD` EMPTY.
- deploy.yml 26849695098 SUCCESS (all jobs); CF invalidation IBINYEKL00J1C6E4V1XWQCPH4Z Completed.
- Rule 19 invariant: main portal/ tree on DEV; ephemeral worktree removed + pruned.
- Rendered-pixel e2e on SERVED PROD is CVO's (Peter [Distribution,Books] / Joe [Distribution,Profile]
  / AUM+Count+NNA), CTO owns the convene. Cross-advisor Distribution drill = graceful placeholder by
  design (edge-untier fast-follow is AE/DS, accepted per Andrew+CTO).

## Next Steps
- **[CVO]** SERVED-PROD e2e on convene by CTO. **[CTO]** owns convene timing.
- **[AE]** cross-advisor Distribution edge-untier fast-follow (separate, not this promote).
- Rollback path if needed: `git push origin a33c230f:PROD` (v2.1.111).
- /work cron (job 3a85749a, 20m) + tracked watcher live; no held-TO changes this tick.

## Compiler Tools
No comp-* — portal FE promote is git plumbing + CI + CloudFront, not a Lambda/script/IAM edit. The
change-gates were the portal pre-push VALGATE D-1 adapter-threading gate (PASS/WARN) + PROD typecheck
(PASS) + ci.yml on DEV (GREEN). comp-iam/comp-pipescript N/A (no boto3/script touched).
