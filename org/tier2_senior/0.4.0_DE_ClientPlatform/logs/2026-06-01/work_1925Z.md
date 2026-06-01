# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 1925Z (TO-A bell-curve footer grain/scope lineage verify)

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, DIAGNOSE

## Dispatch
COO [DRIVE-GO] TO-A (gate for DS TO-B), CTO PRD mdpf-bellcurve-unfunded-footer-lineage-prd. Verify the Inflection 6639 footer lineage on the served feeds.

## VERDICT: 6639 reproduced to the integer; root cause = SCOPE (primary) + grain (secondary)
Brief: docs/briefs/mdpf-bellcurve-footer-grain-lineage-verify-20260601.md.
- PIN: 6639 = 7039 (metrics.total.account_count, json/portfolios/aum-metrics.json, GLOBAL) − 400 (json/mdpf/inflection/account-distribution.json total.account_count).
- Global 7039−7025=14 ✓; 49 7039−6838=201 ✓; Inflection 7039−400=6639 ✓ (all PRD-matching).
- SCOPE (dominant): metrics is GLOBAL (no firm_id, no per-firm account_count); distribution is PER-FIRM. So per-firm footers = global_accounts − firm_distribution. Global=global−global (correct 14); 49=global−49 (201, coincidentally-plausible ONLY bc 49≈97% of global, MASKED); Inflection=global−inflection (6639, exposed).
- GRAIN (secondary): per-firm dists non-additive (6838+400=7238≠7025) + :175 in-code note (INF_09 distribution = clients not accounts).
- No per-firm accounts-grain count exists in ANY served feed -> the FE subtraction can't be scope-fixed alone.

## Refines the PRD
- PRD framed it as "accounts−clients grain." Empirically the DOMINANT mechanism is SCOPE (global metrics vs per-firm distribution); grain is a compounding secondary.
- PRD/COO said "49 = accounts−accounts correct 201." Refined: 49's 201 is global−49 (coincidentally-plausible, masked); only global's 14 is genuinely correct. Scope bug affects 49 too.

## Recommendation (gates TO-B)
PRD option (b) is NECESSARY not just preferred: DS producer emits per-firm ACCOUNTS-grain excluded-unfunded count DIRECTLY (or both per-firm total-accounts + funded-accounts, both accounts-grain). Scope-fix alone impossible (no per-firm account_count numerator exists). TO-C (RD FE-guard) correctly suppresses meanwhile.

## Commits
- CLOUD `<pending>` — brief + this log.

## Comms
- RAVC2 (grain/scope finding, tells DS exactly what to emit) -> COO + CTO + DS~B. CVO doing independent.

## Next
- [DS~B] TO-B: emit per-firm accounts-grain excluded-unfunded count (producer INF_09/09.generate_partner_analytics + metrics).
- [RD~B] TO-C FE-guard stopgap (parallel).
- [me/CVO] verify the corrected count post-TO-B (plausible small per-firm, consistent across firms). /work cron live.
