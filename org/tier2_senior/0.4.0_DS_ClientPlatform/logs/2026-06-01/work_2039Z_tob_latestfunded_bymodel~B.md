# work_2039Z — TO-B latest-funded-period + by_model; priority-check on closed work (DS~B)

## Tick class: SUBSTANTIVE (/work cron; UNBLOCK_RECEIVED -> resumed TO-B; emits + priority-check)

COO resolved all 3 blockers (B1 owned-paths->AE-commit-handoff; B2 latest-funded APPROVED; B3 by_model in-scope-after-total). Resumed.

## PRIORITY CHECK (COO, highest pri — touches closed work): re-derive 1a NOT affected
Q: do the near-empty Mar/Apr smartx allocations (202603=6 rows, 202604=4 rows, $0) feed the just-shipped Schwab re-derive's Mar/Apr model_aua (1a)?
ANSWER (evidence, served re-derived 49F timeseries): NO. Mar 1a = $1,196-1,222M; Apr 1a = $1,213-1,223M; all 82 dates (1/16-5/17) populated, 0 null, 0 near-zero, range $1,132-1,349M. 1a is from a SEPARATE populated DAILY source (historical model series), NOT the monthly allocations. Architecturally: account-distribution = monthly snapshot from smartx_allocations; daily 1a = daily source. => re-derive NOT impacted; no finding on closed work. Mar/Apr monthly near-empty = separate low-pri housekeeping (gap-vs-intentional, AE to confirm; we don't use Mar/Apr snapshots, latest-funded=May).

## B2: latest-FUNDED-period selection (both producers)
Replaced blind max_period with "latest period that has FUNDED (value>0) active accounts" -> skips month-start $0 shell (202606). compute_per_firm + compute_account_distribution. AE CONFIRMED June-$0 is EXPECTED end-of-period (EndMarketVal populates ~PeriodEnd; June PE=6/30 future) -> latest-funded is the robust call.

## TO-B emits — 49F + inflection TOTAL + BY_MODEL DONE (served+verified)
- 49F (gen 20:38:08): total funded 6838 / active 6840 / excl=2 (the 2 in Long Term); 5 by_model entries all carry excluded_unfunded_count + active_accounts_count, each excl=active-funded. period 202605 (latest-funded), NO regression (6838 unchanged).
- inflection (gen 20:38:10): total funded 400 / active 405 / excl=5; 7 by_model entries all carry the fields (INT has 3, etc.). 
by_model per CTO in-scope ruling 29b310e4f (per-model footer L1009 needs it; inflection model dist is client-grained so model-select would render wrong without it).
CVO independent PASS on the earlier inflection total slice (verdict bf244cac1: excl=5 exact, distribution non-degenerate).

## B1 owned-paths: AE-commit-handoff
AE committed the per-firm producer (inflection version) -> 4ffb21d7b (I'm credited; at-risk work protected). Handed AE the cumulative per-firm delta (49F latest-funded + total + by_model, both firms; gate-clean) to commit NOW. Did NOT --force. CTO durable disposition (co-own the 2 files / relocate to data/mdpf/scripts) is Andrew-confirm-gated.

## GLOBAL — PENDING a decision (not blocked on code; on correctness)
Served global json/portfolios/account-distribution.json = 7025 @202606, generated 14:16Z today. AE says June-$0 is expected -> that 202606 valuation is ANOMALOUS -> latest-funded gives 6838 @202605. Re-emitting = a visible -187 global headcount correction + SOMETHING regenerates global at 14:16Z (cron? AE?). Raised to COO+AE: confirm the -187 correction + the regen-owner before I emit global (total + by_model). Global producer code edited (latest-funded+total-excl+guard+ruff) but HELD from commit until global by_model added + decision lands.

## AC3 status
2 of 3 firms complete (total + by_model): 49F (excl=2), inflection (excl=5). Global (total + by_model) pending the 7025/202606 decision + AE commit. DE cross-firm + per-model re-verify requested (49F+inf ready; global held). 

## Next
- On COO/AE global decision: finalize global producer (add by_model) -> emit -> AC3 complete -> DE+CVO cross-firm verify -> RAVC2 TO-B close.
- pre-1/16: still parallel-paused for Andrew #3 (b3e627a75, CTO-concurred rec B).
