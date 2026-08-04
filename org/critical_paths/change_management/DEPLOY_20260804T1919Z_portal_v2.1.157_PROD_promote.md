# DEPLOY LEDGER — portal DEV->PROD promote v2.1.157

**Status: CLOSED 20260804T1929Z — deploy COMPLETE.** PROD=6398630a, tag portal-v2.1.157 peel-verified, CI run 30943138285 SUCCESS (sole workflow for sha, enumerated).
**Executor:** 0.2.0_DT_PortfolioAnalytics (Andrew-direct session edict ~1845Z, recorded @ b9b1e4b02)
**GO chain:** DE CONFIRM-COMPLETE 190959Z citing [a]+[c] (CTO accepted 173318Z) -> COO slate-tip 190920Z -> COO FIRE 191416Z (DT-stand-down hold discharged on 4 live grounds) -> COO EXEC AUTHORIZATION 191749Z (audited LD-0367 override, BOTH pushes, CTO countermand window until merge).

## Promote set (enumerated, triple-verified: DE seat + COO seat + this seat)
- Base: origin/PROD = 2d33ea2c (portal-v2.1.156)
- DEV tip: 45e5843f; unpushed tail = 70c884ae, 68fd700c, 45e5843f (all 0.4.0_DE authored)
- Edict gate: [a] complete-data frontier + [c] one canonical timestamp — both in 68fd700c
- Pre-checks: tsc -b rc=0; tracked tree clean; main tree on DEV; no STOP pending

## Steps (all landed)
- [x] DEV push d32f5a52..45e5843f (LD-0367 audited override per COO 191749Z; VALGATE D-1 PASS)
- [x] local PROD re-asserted from origin (update-ref, 2d33ea2c both)
- [x] ephemeral worktree merge --no-ff = 6398630a; parity diff EMPTY (0 lines)
- [x] SEV1 hand-check: "SEV1 ACKNOWLEDGED (SURFACE_ACK='Andrew-direct ... kill-both ruling ...') -- audited. Proceeding." rc=0, 24 changed src files screened
- [x] PROD push 2d33ea2c..6398630a (same override; pre-push tsc -b PASS)
- [x] CI: run 30943138285 "Deploy to Production" conclusion=success -- SOLE workflow for headSha 6398630a (enumerated, RUNS_FOR_SHA=1)
- [x] tag portal-v2.1.157 peeled = 6398630a = origin/PROD head
- [x] workspace submodule pointer committed e815c11a2 (push = integrator's, LD-0367)
- [x] worktree pruned (physical dir persists, known Filename-too-long class, inert); main tree on DEV @45e5843f; ledger CLOSED

## Rollback
Single step: PROD back to 2d33ea2c (encoded in merge message).
