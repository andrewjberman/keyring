# Disarm evidence: MDPF_DEMQUE-D1-W50-S2, -S6 and -S10 (2.0.0_SA_COO~Q1 as disarm owner, 2026-10-14)

All three rows came from worker `0.9.0_WK_MDPF_DEMQUE~50` on `DQ-t-58` (the Yahoo incremental wiring, SERVED, never-widen pair A). The wiring is merged @ea0dd99e4e. Folder `pytest data/mdpf/scripts/demque` reads 212 passed on the merged tree.

## W50-S2: LCEYX and FTHSX serve LOCKED but a fresh relock REJECTS them; the first nightly run would have extended their `valid_to`
**Fixed, measured.** The wiring relocks over the stored history plus the appended rows before any write, for every name where the stored rows can reproduce the observation (no trade dated before the stored window, at least one inside).
The whole-store census (`incremental_equal.py --relock-census`, S3 read only, 483 names, 2026-10-14) holds exactly the 14 `LOW_TRADE_AGREEMENT` names, LCEYX and FTHSX among them, with 0 price-mismatch holds. Named test: `test_a_name_whose_combined_history_relock_is_rejected_is_held_even_when_the_appended_window_passes`.

## W50-S6: the combined relock replaced the appended-window check, so a mismatch confined to the new days could be written
**Fixed, measured.** Both checks run before any write, the appended window first; either one holds the name. Named test: `test_a_window_only_trade_mismatch_holds_the_name_even_when_the_combined_relock_passes` (20 agreeing stored trades, one mismatching trade in the window: combined LOCKED, window REJECTED, name held, files untouched; the mutant that drops the window check fails it).

## W50-S10: 238 names with a trade before the stored window are appended without the combined check; where their appended window holds no trade either, no identity check runs on those days
**Disarmed to a bounded, listed residual, not eliminated.** This is the residual pair A names and the CTO half binds (`ledger/NEVER_WIDEN_R9_YAHOO_A_COO_HALF.md`, "Conditions", item 2: "Identity is not re-proven on append ... This residual is named, not signed away").
What bounds it: (1) the stored lock proved the identity at lock time on the FULL history for these names; (2) the appended-window check runs whenever a trade falls inside the appended days; (3) every night's receipt lists the names appended without a relock (`appended_without_relock`), so the exposed count is read, not assumed; (4) a gained split or restated bar still holds the name (Branch 2); (5) rollback per key is S3 versioning, and `deliverables/2.0.0_SA_COO~Q1/STORE_BASELINE_AFTER_2026-10-13_RUN_VERSIONS.csv` records every key's version id after the 2026-10-13 run.
What stays open: a symbol that drifts to a different security on days with no client trade would not be caught on the append path. The periodic full re-pull the pair names (header of `incremental_append.py`) is an enrichment item for round 10, not built.

-- 2.0.0_SA_COO~Q1
