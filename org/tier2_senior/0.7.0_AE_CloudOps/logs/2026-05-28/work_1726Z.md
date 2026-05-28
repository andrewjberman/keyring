# /work work-cycle:0005 — firm_concentrations CF invalidation (2026-05-28 ~1726Z)

**Agent:** 0.7.0_AE_CloudOps~A
**Tick class:** STAND-READY → FIRE → completion (substantive; Andrew-watching live demo)
**Commit:** this log only (CF invalidation is an AWS action)

## Dispatch
COO 1723Z [STAND READY] — DS_ClientPlatform regenerating platinum/firm/firm_concentrations.json (PFDE/PFOE/PCHI/IDVZ security_type retag single_stock→etf for Top Holdings); fire CF invalidation on DS artifact-landed flag. Pre-staged served path (advisor-intelligence.ts:1903 + PLATINUM_BASE:835 → /api/scoped/advisor-intelligence/platinum/firm/firm_concentrations.json, behavior #12, dist EVTSA9VEHNZVH; blanket /api/scoped/advisor-intelligence/* covers it, same as F11). ACK'd stand-ready to COO.

## Fire
DS 0.4.0_DS_ClientPlatform flagged artifact-landed 1726Z (LastModified 17:24:12Z, 18864B, INF_D_07a @ f2f813348). Fired immediately:
- Origin verified fresh (17:24:12Z, 18864B) — matches DS flag.
- Invalidation EVTSA9VEHNZVH /api/scoped/advisor-intelligence/* → ID I4HAK7U6Z0JIP3HO1XAGAN08AH, Completed ~24s. Fired 17:25:43Z — AFTER landing (correct ordering, no stale re-cache).
- Reported DS + COO + CC CVO + RD. RD cleared to pull FE band-aid (FE auto-routes the 4 ETFs to Basket on fixed security_type post-hard-refresh).

End-to-end stand-ready → completed ~2.5min.

## Notes
- 3rd CF invalidation this session on EVTSA9VEHNZVH (F11 leaderboard, now firm_concentrations); F4 #15 still held on COO post-demo flag. All use the blanket /api/scoped/advisor-intelligence/* (ADHC_CDNCOHT precedent).

## Posture
Back to standby. Queue: #15 (F4 CF) gated on COO post-demo flag.
