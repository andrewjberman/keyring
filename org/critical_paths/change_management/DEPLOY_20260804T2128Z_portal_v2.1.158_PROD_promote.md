# DEPLOY LEDGER — portal DEV->PROD promote v2.1.158

**Status: CLOSED 20260804T2140Z — deploy COMPLETE.** PROD=08ebe7fe, tag portal-v2.1.158 peel-verified, CI run 30953034310 SUCCESS (sole workflow for sha).
**Executor:** 0.2.0_DT_PortfolioAnalytics (standing default promote authority; Andrew-direct ~1953Z: both items MUST ride the next deploy)
**GO chain:** Andrew-direct ~1953Z (recorded ANDREW_DIRECT_20260804_1953Z_DE_PA_SEAT_AND_NEXT_DEPLOY_CONTENTS.md) -> 0.2.0_DE_PortfolioAnalytics CONFIRM-COMPLETE 212321Z naming BOTH items -> COO freeze-ack + EXEC AUTHORIZATION 212722Z (audited LD-0367 override, both pushes, 191749Z precedent, CTO countermand window until merge).

## Promote set (enumerated: exactly origin/DEV..DEV = 2 commits)
- Base: origin/PROD = 6398630a (portal-v2.1.157)
- 02b7f351 (0.4.0_DE): displayModelName() typing canon lib, Pod4 emission sites
- 604101df (0.2.0_DE_PA): FE-pointing LT/ULT seams (incl. aum-metrics keying live-defect fix) + Pod2 hyphen typing via the lib
- Pre-checks: tsc -b rc=0 (independent, this seat); tracked tree clean; main tree on DEV; ancestry verified; edict [c] held per confirm; SEV1 SURFACE_ACK audited by author

## Steps (all landed)
- [x] DEV push 45e5843f..604101df (audited override per COO 212722Z; VALGATE D-1 PASS)
- [x] local PROD re-asserted (update-ref, 6398630a both)
- [x] worktree merge --no-ff = 08ebe7fe; parity diff EMPTY (0 lines); bun install foreground 99s
- [x] SEV1 hand-check: "SEV1 ACKNOWLEDGED (SURFACE_ACK='ANDREW-ASSIGNED LT/ULT closure ...') -- audited. Proceeding." rc=0 (13 src files)
- [x] PROD push 6398630a..08ebe7fe (same authorization; pre-push tsc -b PASS)
- [x] CI: run 30953034310 "Deploy to Production" conclusion=success, sole workflow for headSha 08ebe7fe
- [x] tag portal-v2.1.158 peeled = 08ebe7fe = origin/PROD head
- [x] pointer committed d3b68e4f86 (push = integrator, LD-0367; LD-0276 gate correctly fired on a compound command carrying $( -- resplit + -F, no override)
- [x] worktree pruned (physical dir persists, known class); main tree DEV @604101df; ledger CLOSED

## Rollback
Single step: PROD back to 6398630a.

## Known non-blocker carried on the record
Three yang page artifacts (positioning/tier1-snapshot/attribution) miss LT/ULT rows — producer
gap, DS lane, at COO; FE renders honest-absent by design until DS's morning wave.
