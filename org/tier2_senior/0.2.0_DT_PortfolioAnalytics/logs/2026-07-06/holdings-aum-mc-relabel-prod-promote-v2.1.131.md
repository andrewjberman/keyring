# Holdings 'AUM (Bn)'->'MC' relabel -- portal DEV->PROD promote v2.1.131
**archetype:** DEPLOY

## Summary
Andrew-direct follow-on to the v2.1.130 promote: a one-line FE label change on the Positioning
page Holdings Breakdown table -- the ETF-characteristics column header "AUM (Bn)" -> "MC" (label
only; the underlying value/format is unchanged). Andrew explicitly authorized me (0.2.0_DT) to
make this minute FE edit directly (I'd done the pod's FE work earlier this session as 0.2.0_DE).
Committed to DEV, promoted via `/prod-deploy`, tagged portal-v2.1.131.

## Change
`portal/src/pages/Positioning/tabs/HoldingsTab.tsx` -- 2 lines: the `<th>` span label
"AUM (Bn)" -> "MC", plus the matching colgroup width-comment (`{/* AUM */}` -> `{/* MC (was AUM) */}`).
Commit `b9656272` (author 0.2.0_DT, Andrew-authorized). tsc + eslint clean.

## Deployment Sequence
| Step | Action | Result |
|------|--------|--------|
| 0 | Gate + 2nd freeze | DT (Andrew-directed); freeze declared to COO -> NOTED/honored |
| 1 | DEV push | `git push origin DEV` VALGATE D-1 PASS, `043e8d21..b9656272` |
| 2 | typecheck | `tsc -b --noEmit` exit 0 (at commit) |
| 3 | re-assert local PROD | `PROD=origin/PROD` (8b3ab08f); delta = b9656272 only (no passengers) |
| 4 | worktree merge | ephemeral `.runtmp/portal-promote-20260706T175216Z`; foreground `bun install` (420 pkgs, 151s); `merge --no-ff origin/DEV`; parity empty; `git push origin PROD` `8b3ab08f..2dccae3f` (VALGATE + push-tsc PASS) |
| 5 | CI verify | run `28812272785` conclusion=success; tag `portal-v2.1.131` peel-verified ^{commit}=2dccae3f=origin/PROD head |
| 6 | pointer bump | submodule `portal` -> b9656272, commit `61986e929`, pushed CLOUD (push wrapper timed out at 2min but landed: local==origin/CLOUD==61986e929) |
| 7 | teardown | worktree registration pruned (physical dir persists: long-path, gitignored+inert); main tree back on DEV; pwd=root |
| 8 | report | RAVC GREEN to COO + 2nd freeze released; this log |

## Deployment Tags
| Pipeline | Tag | Commit |
|---|---|---|
| portal (app) | portal-v2.1.131 | 2dccae3f (PROD merge) |

## Verification (actual output)
- Parity: `git diff origin/DEV HEAD` -> EMPTY.
- PROD push: `8b3ab08f..2dccae3f  PROD -> PROD` (VALGATE + push-tsc PASS).
- CI: run 28812272785 status=completed conclusion=success.
- Tag peel: `git rev-parse portal-v2.1.131^{commit}` = 2dccae3f = origin/PROD head.
- Pointer: local CLOUD == origin/CLOUD == 61986e929 (in sync; push landed despite the 2min wrapper timeout).

## Current State
- LIVE PROD: portal merge 2dccae3f, tag portal-v2.1.131, CI 28812272785 SUCCESS. Holdings Breakdown
  ETF-characteristics column now labeled "MC" (was "AUM (Bn)").
- Workspace CLOUD pointer 61986e929 -> portal b9656272. Main tree on DEV.
- COO 2nd freeze released.

## Next Steps
- [Andrew/operator] Non-gating live eyeball once CF propagates: Holdings column reads "MC".

## Blockers
None.

## Compiler Tools
| Tool | Purpose | Result |
|---|---|---|
| (none) | -- | -- |

Trivial single-label FE promote (no gold/silver/Lambda/infra/IAM). In-band gates: VALGATE D-1
(PASS no-op on both pushes), push-time tsc (PASS), safe-commit surface-check (OK) on the pointer
bump. No comp-tool query warranted for a one-word column relabel.
