# Positioning-batch portal DEV->PROD promote -- v2.1.130
**archetype:** DEPLOY

## Summary
Promoted the Andrew-direct Positioning-page UI batch (+ two cleared cross-lane passengers) from
portal DEV to PROD via the canonical `/prod-deploy` procedure. Single batched merge; CI deployed +
tagged `portal-v2.1.130`. RAVC GREEN to COO, freeze released, ClientPlatform pod notified their
passenger shipped. **Note:** I role-switched from `0.2.0_DE_PortfolioAnalytics` (who authored the
Positioning commits this session) to `0.2.0_DT` at Andrew's direction to run the promote (DE can't push).

## Promote delta (6 commits, ALL Andrew-cleared)
The full `origin/PROD..origin/DEV` delta -- I surfaced it before pushing and Andrew cleared each:
| Commit | Author | What | Clearance |
|---|---|---|---|
| `3b516623` | 0.2.0_DE | Positioning Summary freeze-pane | Andrew-direct build |
| `84b24af8` | 0.2.0_DE | Holdings center group-headers + freeze thead | Andrew-direct |
| `7e8baa70` | 0.2.0_DE | Holdings opaque header cells (kept; harmless) | Andrew-direct |
| `043e8d21` | 0.2.0_DE | Holdings border-separate bleed fix + square Basic Info corner | Andrew SMOKE-verified |
| `62cdb473` | 0.2.0_DT | Attribution period-boundary guard (periodResolution.ts + wire) | Andrew: "we want that attribution boundary on PROD" |
| `a58ff3a7` | 0.4.0_DE_ClientPlatform | ADVI_TAGATTR advisor-tagging FE (AdvisorPublicProfile/AdvisorsTab) | Andrew cleared the cross-pod passenger (AskUserQuestion: "Include it") |

**QA-gate note:** the `a58ff3a7` passenger (a DIFFERENT pod's commit, on DEV since Jul 1, no promote
since v2.1.129) was NOT silently shipped -- I flagged the full delta and got Andrew's explicit include
decision before pushing PROD. This is the "promote merges LIVE DEV, no free passengers" discipline.

## Deployment Sequence
| Step | Action | Result |
|------|--------|--------|
| 0 | Gate + freeze | DT (Andrew-directed); freeze declared to COO -> NOTED/honored (no conflicting portal/DEV in fleet) |
| 1 | DEV hygiene + push | main tree on DEV, tracked-clean; local ahead by 4 -> `git push origin DEV` (VALGATE D-1 PASS), `62cdb473..043e8d21` |
| 2 | typecheck | `tsc -b --noEmit` exit 0 |
| 3 | re-assert local PROD | `update-ref PROD=origin/PROD` (eb049b7e); delta confirmed = the 6 cleared commits |
| 4 | worktree merge | ephemeral `.runtmp/portal-promote-20260706T173625Z` on PROD; foreground `bun install` (420 pkgs, 119.7s); `merge --no-ff origin/DEV`; **parity gate empty**; merge msg corrected v2.1.128->v2.1.130 (FORCE_HEADMOVE amend, local-only, audited); `git push origin PROD` (VALGATE + push-tsc PASS) `eb049b7e..8b3ab08f` |
| 5 | CI verify | run `28811243042` conclusion=**success**; tag `portal-v2.1.130` peel-verified ^{commit}=8b3ab08f=origin/PROD head |
| 6 | pointer bump | workspace submodule `portal` 90322ba0->043e8d21, commit `a795804cd`, pushed CLOUD |
| 7 | teardown | worktree registration pruned (physical dir persists: Windows long-path node_modules, gitignored+inert); main tree back on DEV; pwd=workspace root |
| 8 | report | RAVC GREEN to COO + freeze released; ClientPlatform pod FYI'd re a58ff3a7; this log |

## Deployment Tags
| Pipeline | Tag | Commit |
|---|---|---|
| portal (app) | portal-v2.1.130 | 8b3ab08f (PROD merge) |

## Verification (actual output)
- Parity: `git diff origin/DEV HEAD` -> EMPTY (PROD tree == DEV 043e8d21).
- PROD push: `eb049b7e..8b3ab08f  PROD -> PROD` (VALGATE D-1 PASS, push-time tsc PASS).
- CI: run 28811243042 `status=completed conclusion=success`.
- Tag peel: `git rev-parse portal-v2.1.130^{commit}` = 8b3ab08f = origin/PROD head.
- Pointer push: `f28277d9e..a795804cd  CLOUD -> CLOUD`.

## Current State
- LIVE PROD: portal merge 8b3ab08f, tag portal-v2.1.130, CI 28811243042 SUCCESS.
- The Positioning page now serves: Positioning Summary freeze-pane; Holdings Breakdown centered
  group-headers + frozen two-row header (border-separate, no bleed) + square Basic Info corner.
  Also live: Attribution period-boundary guard (62cdb473) + ClientPlatform advisor-tagging (a58ff3a7).
- Workspace CLOUD pointer a795804cd -> portal 043e8d21. Main portal tree on DEV (Rule 19 held).
- COO freeze released; fleet clear to push portal/DEV.

## Next Steps
- [Andrew/operator] Non-gating live PROD pixel eyeball once CloudFront propagates (~5-10min):
  Positioning freeze panes + Holdings frozen header (no bleed). The Holdings fix was already
  Andrew-smoke-verified on identical DEV code, so this is confirmation only.
- [0.4.0_DE_ClientPlatform] (FYI, sent) verify advisor views on PROD -- your a58ff3a7 is now live.

## Blockers
None.

## Compiler Tools
| Tool | Purpose | Result |
|---|---|---|
| (none) | -- | -- |

Pure portal-app FE promote (no gold/silver/Lambda/infra/IAM). The relevant gates are portal-native
and ran in-band: VALGATE D-1 (adapter-threading, PASS no-op on both DEV + PROD push), push-time
`tsc -b --noEmit` (PASS), safe-commit surface-check (OK, no critical surface) on the pointer bump.
No comp-tool query warranted -- the dependency surface was pure FE render/layout on PositioningSummary
+ HoldingsTab + Attribution + advisor components, established by the authoring DE's per-commit tsc/eslint
+ Andrew's smoke-verify. Delta-passenger diligence was done via git delta inspection, not a comp-tool.
