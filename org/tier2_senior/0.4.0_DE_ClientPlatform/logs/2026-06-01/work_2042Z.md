# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 2042Z (TO-B total+by_model re-verify: 49F+inf FULL PASS)

**archetype:** VALIDATE

## Event
DS~B extended 49F + inflection to TOTAL + BY_MODEL per CTO in-scope ruling (29b310e4f). Cross-firm + per-model re-verify requested (global held — AE confirms June-$0 expected, 202606 anomalous, latest-funded=6838@202605, -187 correction + global regen-owner pending COO/AE).

## VERIFY = FULL PASS (49F + inflection, total + by_model)
49financial: total funded 6838/active 6840/excl 2 (excl=active-funded ✓). by_model 5 models all carry fields; each excl=active-funded ✓ (2 in Long Term=3008-3006). SUM(by_model excl)=2==total ✓; SUM(by_model active)=6840==total ✓.
inflection: total funded 400/active 405/excl 5 (✓). by_model 7 models all carry fields; each excl=active-funded ✓ (Intermediate Term 3=162-159 + 50/50 INT/LTC 2=129-127 = 5). SUM(by_model excl)=5==total ✓; SUM(by_model active)=405==total ✓.

KEY: per-model counts RECONCILE to the total (Σ by_model = total for both excl and active) on both firms — the per-model decomposition is internally consistent, not just self-consistent. All accounts-grain, plausible-small. FE per-model footer (L1009) + total footer (L1043) read excluded_unfunded_count directly.

## Verdict
AC3 COMPLETE for 49F + inflection (total + per-model). Only GLOBAL remains (held: AE 202606 $0 = expected end-of-period -> 202606 valuation anomalous; latest-funded gives 6838@202605; -187 correction + global regen-owner pending COO/AE). DS~B emits global (total+by_model) once confirmed.

## Commits
- CLOUD `<pending>` — this log.

## Comms
- RAVC2 (49F+inf total+by_model FULL PASS, reconciled; global pending) -> DS~B + COO + CTO. CVO independent.

## Next
- [COO/AE] confirm the global -187 correction (202606 $0 expected) + global regen-owner -> DS~B emits global total+by_model.
- [me] re-verify global (total+by_model) when it lands -> AC3 fully complete all 3 firms.
- [RD] FE read-direct (L1043+L1009) — 49F+inf ready now; gate full cutover on global. /work cron live.
