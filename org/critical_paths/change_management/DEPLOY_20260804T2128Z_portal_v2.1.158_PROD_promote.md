# DEPLOY LEDGER — portal DEV->PROD promote v2.1.158

**Status: OPEN (deploy-start)** — closes at completion per CLAUDE.md NEVER (half-landed rule).
**Executor:** 0.2.0_DT_PortfolioAnalytics (standing default promote authority; Andrew-direct ~1953Z: both items MUST ride the next deploy)
**GO chain:** Andrew-direct ~1953Z (recorded ANDREW_DIRECT_20260804_1953Z_DE_PA_SEAT_AND_NEXT_DEPLOY_CONTENTS.md) -> 0.2.0_DE_PortfolioAnalytics CONFIRM-COMPLETE 212321Z naming BOTH items -> COO freeze-ack + EXEC AUTHORIZATION 212722Z (audited LD-0367 override, both pushes, 191749Z precedent, CTO countermand window until merge).

## Promote set (enumerated: exactly origin/DEV..DEV = 2 commits)
- Base: origin/PROD = 6398630a (portal-v2.1.157)
- 02b7f351 (0.4.0_DE): displayModelName() typing canon lib, Pod4 emission sites
- 604101df (0.2.0_DE_PA): FE-pointing LT/ULT seams (incl. aum-metrics keying live-defect fix) + Pod2 hyphen typing via the lib
- Pre-checks: tsc -b rc=0 (independent, this seat); tracked tree clean; main tree on DEV; ancestry verified; edict [c] held per confirm; SEV1 SURFACE_ACK audited by author

## Steps
- [ ] DEV push (audited override per COO 212722Z)
- [ ] local PROD re-asserted (update-ref)
- [ ] worktree merge --no-ff; parity diff EMPTY
- [ ] SEV1 hand-check on merged composition
- [ ] PROD push (same authorization)
- [ ] CI conclusion=success, enumerated by headSha
- [ ] tag portal-v2.1.158 peel-verified
- [ ] pointer committed (push = integrator, LD-0367)
- [ ] teardown; main tree on DEV; ledger CLOSED

## Rollback
Single step: PROD back to 6398630a.

## Known non-blocker carried on the record
Three yang page artifacts (positioning/tier1-snapshot/attribution) miss LT/ULT rows — producer
gap, DS lane, at COO; FE renders honest-absent by design until DS's morning wave.
