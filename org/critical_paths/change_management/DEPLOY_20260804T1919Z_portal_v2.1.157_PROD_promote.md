# DEPLOY LEDGER — portal DEV->PROD promote v2.1.157

**Status: OPEN (deploy-start)** — closes at completion per CLAUDE.md NEVER (half-landed rule).
**Executor:** 0.2.0_DT_PortfolioAnalytics (Andrew-direct session edict ~1845Z, recorded @ b9b1e4b02)
**GO chain:** DE CONFIRM-COMPLETE 190959Z citing [a]+[c] (CTO accepted 173318Z) -> COO slate-tip 190920Z -> COO FIRE 191416Z (DT-stand-down hold discharged on 4 live grounds) -> COO EXEC AUTHORIZATION 191749Z (audited LD-0367 override, BOTH pushes, CTO countermand window until merge).

## Promote set (enumerated, triple-verified: DE seat + COO seat + this seat)
- Base: origin/PROD = 2d33ea2c (portal-v2.1.156)
- DEV tip: 45e5843f; unpushed tail = 70c884ae, 68fd700c, 45e5843f (all 0.4.0_DE authored)
- Edict gate: [a] complete-data frontier + [c] one canonical timestamp — both in 68fd700c
- Pre-checks: tsc -b rc=0; tracked tree clean; main tree on DEV; no STOP pending

## Steps (checked off as landed)
- [ ] DEV push (LD-0367 audited override per COO 191749Z)
- [ ] local PROD re-asserted from origin (update-ref)
- [ ] ephemeral worktree merge --no-ff; parity diff EMPTY
- [ ] SEV1 hand-check (comp-surface-check on merged composition, SURFACE_ACK from merge range)
- [ ] PROD push (same override authorization)
- [ ] CI conclusion=success, ENUMERATED by headSha across all workflows
- [ ] tag portal-v2.1.157 peel-verified against PROD head
- [ ] workspace submodule pointer committed (push = integrator's, LD-0367; pointer commit rides the integration window)
- [ ] worktree teardown; main tree on DEV; ledger CLOSED

## Rollback
Single step: PROD back to 2d33ea2c (encoded in merge message).
