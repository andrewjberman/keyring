# work_2014Z — TO-B bell-curve durable footer fix (DS~B)

## Tick class: SUBSTANTIVE (code + serving emit + verify; 49F blocker surfaced)

COO GO NOW (pre-1/16 producer-write window free; DE TO-A grain-confirm landed). Executed TO-B.

## PRODUCER-CORRECTION FINDING (material — the DE/COO emit-target was wrong)
DE TO-A named the emit-target as `INF_09.generate_partner_analytics + 09.generate_partner_analytics` (off positions_cube). **That's wrong.** Those scripts publish `partner_analytics.json` (NNA distribution) on opal-data-inf — they do NOT produce `account-distribution.json`. The actual producer of the FE-footer's `json/mdpf/{firm}/account-distribution.json` is **`data/smartx/scripts/compute_per_firm_account_distribution.py`** (authored by me 2026-05-29; was UNTRACKED/at-risk).
- PROOF: served inflection `account-distribution.json` shape (firm_id/firm_name/generated_at/period/source/total{...}/by_model) + source (`s3://opal-data-inf/gold/eclipse/2026-05-29/model_portfolio_accounts.parquet`) + period (2026-05-29) + total.account_count=400 ALL match this script's output exactly.
- This producer ALREADY does the funded-only exclusion (`compute_distribution_stats` drops value<=0; inflection `df_active = df[total_value>0]`), so the excluded-unfunded count is computable HERE at the histogram's own grain — the natural, self-consistent emit point.

## THE FIX
Emit per-firm, in `total`, at the histogram's own grain (kills the cross-feed subtraction):
- `total.excluded_unfunded_count` = active accounts − funded accounts (the $0/unfunded ones the histogram drops)
- `total.active_accounts_count` = funded + unfunded
FE reads `distribution.total.excluded_unfunded_count` directly instead of `metrics.account_count(7039 GLOBAL) - distribution.account_count` (the 6639 bug). **RD field to wire: `distribution.total.excluded_unfunded_count`.**

Grain note for DE: emitted at the SAME grain as the histogram (model-portfolio-account for inf), NOT aligned to the global metrics accounts-grain. Argue this is MORE correct: the footer "Excludes N unfunded holdings" should pair with the histogram it annotates, so funded(histogram) + excluded = active at one consistent grain. DE to verify.

## INFLECTION: DONE + verified (the exposed 6639 case)
- Served `json/mdpf/inflection/account-distribution.json`: account_count=400, active_accounts_count=405, **excluded_unfunded_count=5** (405-400=5, self-consistent). generated_at 2026-06-01T20:12:17Z.
- Kills 6639 -> 5 for the inflection footer. Reversible (re-emit, 0-credit); RD~B Global-only stopgap still covers the visible footer until RD wires the field.

## 49F: BLOCKED (anti-regression guard held) — pre-existing smartx source bug, surfaced not caused by TO-B
Dry-run showed 49F funded=0 / total=0. Root cause (smartx_allocations.parquet):
| period | rows | active | funded(EMV>0) | EMV sum |
|---|---|---|---|---|
| 202605 (May) | 6917 | 6840 | **6838** | $1.38B  <- the GOOD served distribution (5/29) |
| 202606 (June) | 6849 | 6849 | **0** | $0  <- SHELL: allocations loaded, EndMarketVal all $0 (unvalued) |

The producer's `max_period` picks 202606 (newest = unvalued shell) -> 0 funded -> would regress the live served 6838.
- ADDED anti-regression GUARD: `upload()` refuses to write a 0-account distribution (logs SKIP loudly, no silent mask). Verified: 49F SKIPPED, served 6838 + period 202605 UNCHANGED (no regression).
- 49F footer-fix DEFERRED until resolved. Two paths (BLOCKED-ASK to COO): (a) upstream — value the smartx 202606 period (DT/AE/DE smartx ingestion); (b) producer-hardening — select the latest period WITH funded accounts (I can do; it's a freshness-vs-correctness semantic call, so not making it unilaterally — and the guard already prevents the bad outcome without masking the upstream issue).

## Gates
- ds-commit-gate: clean (py_compile + ds-precommit + ruff).
- Self-verify: served inflection field present + self-consistent; served 49F unchanged. DE serving-verify + CVO independent-verify pending (RAVC2).

## Next
- Commit producer (now tracked) + this log.
- RAVC2 inflection to COO (CC DE+CTO+RD~B): producer-correction + field name for RD + grain note for DE.
- BLOCKED-ASK to COO for 49F (value 202606 OR approve latest-funded-period selection).
- pre-1/16: still awaiting Andrew #3 (CTO concurred rec B; b3e627a75 routed).
