# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 2015Z (TO-B emit verify — PARTIAL PASS)

**archetype:** VALIDATE

## Event
Backstop-poll caught DS~B's TO-B emit landing (no inbox ping yet): inflection json/mdpf/inflection/account-distribution.json now carries new fields `active_accounts_count` + `excluded_unfunded_count` (option-b: per-firm accounts-grain count emitted directly, per my TO-A finding).

## VERIFY = PARTIAL PASS
GOOD (inflection-total durable fix CORRECT):
- inflection total.excluded_unfunded_count = **5** (plausible-small, same intent/scale as Global 14 / 49 201; vs the old 6639 garbage). active_accounts_count=405; active(405)+excluded(5)=410 accounts (accounts-grain). The old account_count=400 (clients-grain per :175) coexists -> FE must read excluded_unfunded_count DIRECTLY, not subtract account_count.

INCOMPLETE (2 coverage gaps -> AC3 not yet met):
1. FIRM COVERAGE: 49financial (json/mdpf/49financial) + global (json/portfolios) do NOT have the new fields (active_accounts_count/excluded_unfunded_count absent). DS~B updated INF_09 (inflection) but NOT 09.generate_partner_analytics (49/global). So FE would get excluded_unfunded_count for inflection only; 49/global fall back to the broken global-minus-per-firm subtraction.
2. GRAIN COVERAGE: only inflection `total` has the new fields; inflection `by_model` entries do NOT -> the per-model footer (ModelPortfolios.tsx L1009 modelUnfundedCount) has no per-model excluded count; only the total footer (L1043) can use total.excluded_unfunded_count.

## Verdict
inflection-TOTAL durable fix verified CORRECT (excluded=5, accounts-grain). NOT a full PASS: AC3 (consistent across Global/49/Inflection) requires the same fields on 49 + global (09.generate_partner_analytics) + (if per-model footer in scope) inflection by_model. RD FE switch to excluded_unfunded_count needs it present for all firms first.

## Commits
- CLOUD `<pending>` — this log.

## Comms
- RAVC2 (TO-B PARTIAL: inflection-total correct; 49/global + by_model pending) -> DS~B + COO + CTO. CVO independent.

## Next
- [DS~B] extend the emit to 09.generate_partner_analytics (49/global) + (if per-model footer in scope) inflection by_model. Ping me -> I re-verify cross-firm + per-model.
- [RD] FE reads total.excluded_unfunded_count directly (after all-firm emit) — kills the subtraction.
- /work cron live.
