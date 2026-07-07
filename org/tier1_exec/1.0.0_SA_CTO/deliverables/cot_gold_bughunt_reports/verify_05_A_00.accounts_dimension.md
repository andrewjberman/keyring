# VERIFY #05 -- target: A_00.accounts_dimension.py

- is_real: **False**
- confidence: **refuted**
- corrected_severity: low

## Reasoning
Refuted on three independent grounds, traced through data/control flow in data/cot/scripts/gold/A_00.accounts_dimension.py plus its upstream producer data/cot/scripts/silver/cot_silver_merge.py.

(1) CONVERGENCE WITH FULL BUILD (kills the core premise). The L414-417 loop overwrites an updated account's non-preserved columns with upd_new values. But for any updated account (updated_ids = existing ∩ new), its latest new-window row IS its globally-latest row, so upd_new[col] equals exactly what the full-build latest-row selection computes (load_accounts_from_transactions L243-248: sort_values('trade_date', desc).groupby('account_id').first()), which itself has NO carry-forward for non-advisor fields. The existing dimension value is merely a prior latest-row snapshot with no privileged correctness. So the loop refreshes to the current latest-row value; it does not swap a correct value for a wrong one. CONTEXT states CHAIN_FULL runs daily in full mode, recomputing the entire dimension from scratch — so even a transient incremental value is reconciled to the full-build value nightly.

(2) MOST NAMED FIELDS CANNOT BE NULLED. tax_status is fillna('taxable') at L504 (never null; worst case 'taxable' = same as full build from a null tax_status_1). qualified_flag is a derived bool at L512 (never null). client_city/state/country/zip are fillna('') at L523/L530 (never null). account_open_date/first_transaction_date/relationship_first_seen_date are in preserve_cols (L408-410) — the finding itself concedes date fields are protected. The null-overwrite mechanism is inapplicable to the majority of the enumerated fields.

(3) REMAINING FIELDS REQUIRE AN UNVERIFIED, MOSTLY SELF-CONTRADICTORY PREMISE. Only account_name/account_owner(_type)/relationship_name/account_is_open/closed_date are genuine object passthroughs. Firing requires a cash-sweep/fee/dividend row to null an account-MASTER field while an earlier row populated it. That is established for advisor-attribution fields (why the L255-284 and L419-425 carry-forwards exist) but not for account-master descriptive fields, which cot_silver_merge.py passes through denormalized onto every row per account. The closed_date path is self-contradictory: the account must have a non-null closed_date in existing AND transact in the new window to enter updated_ids — a closed account rarely does both.

Even if the premise held, it is not a merge-loop bug: the same null would be produced by the full build's latest-row selection (L243-248), which also lacks non-advisor carry-forward. Any fix is a uniform latest-row-vs-carry-forward design choice across both code paths, not a defect localized to L414-417. I could not read live silver rows to positively exclude a COT cash-sweep nulling account_owner, but worst case still converges with the daily full rebuild, so no served corruption results. Downgraded from high to low (residual design consideration, not a correctness defect).
