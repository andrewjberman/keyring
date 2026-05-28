# /work work-cycle:0004 — F11 CF invalidation (2026-05-28 ~1635Z)

**Agent:** 0.7.0_AE_CloudOps~A
**Tick class:** SENIOR_DISPATCH (CTO) execution + completion (substantive; demo-decisive)
**Commit:** this log only (CF invalidation is an AWS action, no repo change)

## Dispatch
CTO 1631Z [F11 ACTIVATION] — live s3://opal-data-inf/platinum/firm/leaderboard.json regenerated with fee_breakdown (F11, CVO-verified) but portal serves stale CDN copy → Fees toggle not re-slicing. Asked: invalidate CF for the leaderboard path. GO (not hold).

## Work done
- **Served-path trace:** portal getFirmLeaderboard (advisor-intelligence.ts:1711) reads `/api/scoped/advisor-intelligence/platinum/firm/leaderboard.json` → CF behavior #12 (shared-advisor-router → firm-scoped opal-data-inf). Distribution EVTSA9VEHNZVH (opalinvest.dev) — same as F4 stage.
- **Origin premise verified:** S3 object (25KB) has fee_breakdown present → staleness purely CDN, not a regen failure.
- **Invalidation:** EVTSA9VEHNZVH, path /api/scoped/advisor-intelligence/* (blanket per ADHC_CDNCOHT; covers exact path + ?firm= variants). ID IBVLAX3BBOIUY6CI2NFLAXXULD, Status Completed ~24s.
- **Verification:** origin-has-field + invalidation-Completed = causal chain complete (couldn't CLI-fetch the [AUTH]+firm-scoped endpoint to eyeball). Reported to CTO + CC COO; Andrew re-tests Fees toggle at :5173 post-hard-refresh.

## Notes
- Distinct from F4 #15 (still held, gated on COO post-demo flag) — same distribution, same blanket pattern, no conflict.
- If toggle still fails post-hard-refresh → NOT CF (flag CTO; investigate served-key mismatch or Lambda firm-routing).

## Posture
Back to standby. Queue: #15 (F4 CF invalidation) gated on COO post-demo flag.
