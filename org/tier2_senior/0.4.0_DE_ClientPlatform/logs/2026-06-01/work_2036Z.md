# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 2036Z (TO-B cross-firm re-verify: 49F+inf total PASS)

**archetype:** VALIDATE

## Event
DS~B extended the emit to 49F (latest-funded-period selection, skips the broken 202606 $0-shell; no regression, 6838 held). Asked cross-firm re-verify of 49F + inflection (global held — 202606 regressed to $0 today, routed AE 0.5.0 to restore).

## VERIFY (firm-TOTAL footer L1043) = PASS for 49F + inflection
| firm | funded(account_count) | active | excluded_unfunded | excl=active−funded | %unfunded | old-broken |
|---|---|---|---|---|---|---|
| 49financial | 6838 | 6840 | 2 | ✓ (2) | 0.03% | 201 (masked) |
| inflection | 400 | 405 | 5 | ✓ (5) | 1.23% | 6639 (garbage) |
- Both: self-consistent (excluded = active − funded), accounts-grain, plausible-small, CONSISTENT definition across firms. 49 no-regression (6838 held). PASS.

## STILL REMAINING (2 dims)
1. GLOBAL total: PENDING — json/portfolios/account-distribution.json 202606 source regressed valued->$0 today (re-emit would regress 7025->6838); routed to AE (0.5.0) to restore 202606; DS~B emits global fresh once fixed. HELD per DS~B.
2. by_model (per-model footer L1009, CTO-ruled IN-SCOPE): NOT yet emitted on ANY firm — checked 49F + inflection by_model, no excluded_unfunded_count. So the per-model footer still has no field to read.

## Verdict
Firm-TOTAL durable fix verified-correct + consistent on 2/3 firms (49F+inf). AC3 NOT yet complete: needs (a) global total [AE 202606 restore] + (b) by_model all firms [DS~B, per CTO in-scope ruling]. FE read-direct gates on all-firm total + by_model.

## Commits
- CLOUD `<pending>` — this log.

## Comms
- RAVC2 (49F+inf total PASS; global+by_model remaining) -> DS~B + COO + CTO. CVO independent.

## Next
- [AE 0.5.0] restore smartx 202606 valuation -> unblocks global total emit.
- [DS~B] global total (post-202606) + by_model all firms (compute_per_firm + compute_account_distribution) once owned-paths resolved.
- [me] re-verify global + by_model when they land -> AC3 complete. /work cron live.
