# ws-charter tick — 1.0.0_SA_CTO — 2026-06-01 1545Z

**CLASS:** FIX (CTO review of the BMKAUD lock-down TF plans; active Andrew-direct work)

## Context
BMKAUD fully shipped to PROD (portal-v2.1.105 + fresh pure-yang data INT 1M=2.95,
3 CF invalidations Completed, DT+AE verified). Andrew elevated the SmartX-clobber
lock-down to explicit priority. AE authored the two TF plans (056fb2855), applies
HELD for my+COO RAVC2.

## CTO review of bmkaud_ws4_tf_plans.md (056fb2855)
Approach APPROVED — thorough, all 4 conditions met (write-only/never-GetObject,
ArnNotLike-not-NotPrincipal, narrow break-glass, post-apply allow-deny proof);
2-phase import-with-0-diff-OAC-gate is correct. TWO required additions caught:
1. **Deny scope gap:** LEG 2 Phase-B Deny covers `platinum/mdpf/aggregate_aua/*`
   (the MDPF anti-clobber, mdpf-runner canonical) — but Andrew's directive is the
   BENCHMARK data `json/benchmarks/*`, canonical writer = the YANG lambda role,
   NOT mdpf-runner. Directed AE to add a SEPARATE DenyNonYangWriteBenchmarks
   statement (json/benchmarks/* except yang-lambda-role, write-only) in the same
   imported policy. That's the actual lock Andrew asked for (stops the smartx
   sidecar writers + EC2 dual-writer + dev-creds from json/benchmarks/*).
2. **Daily-orphan:** LEG 1 retires smartx-model-monthly-pull (8 resources); the B3
   DAILY producer (_smartx_model_daily.json) isn't in the plan — directed AE to
   identify + fold into LEG 1. Retire BOTH sidecar producers.

## Cohort 1c finding (DS~B 5d2d034e9)
The 0->$20M 1c "jump" on 5/18 = SMA accounts RECLASSIFIED out of 1b into 1c (NOT
a new asset). Value was captured historically in 1b, but SMA accounts aren't in
the model-only SmartX source => exact 1c history NOT reconstructable from existing
data (estimate-only unless a new SmartX historical pull). Surfaced to Andrew as a
decision (new pull vs estimate/forward-only).

## Action
- CTO review -> AE (154523Z): approve approach + 2 additions; re-RAVC2 consolidated
  -> then ANDREW apply-ratify (destructive + shared-origin = his sign-off).
- Cohort-1c: backend answered (reclassification); FE rollup target still pending
  Andrew's "which view" confirm (RD~B tracing aum.ts consumer meanwhile).

## Next-cycle expected state
AE re-RAVC2 with benchmark Deny + daily-orphan -> CTO final -> Andrew apply-ratify.
Cohort-1c FE rollup lands once Andrew names the view. CVO WS-5 corroborates LEG-1
zero-consumer for the retirement.

ws-charter-cycle:0005 class:FIX
