# VERIFY #09 -- target: A_00.accounts_dimension.py

- is_real: **True**
- confidence: **confirmed**
- corrected_severity: critical

## Reasoning
CONFIRMED — traced end-to-end through code, config, and the LIVE served artifact. Every precondition is satisfied and the corruption is already manifest on served.

CODE PATH (as flagged):
- build_accounts_dimension (L455) unconditionally runs the holdings-snapshot union at L478-487: _extra = every snapshot account NOT in accts's account_id set (L481), injected with all txn-metadata columns forced to None (L483-485), then concatenated (L486). There is NO mode flag — the union fires identically in full and incremental.
- In incremental mode _run_incremental (L674) builds new_txn_accounts from ONLY the new-window keys (load_accounts_from_transactions(keys=new_keys)), then calls build_accounts_dimension at L680. So accts = only accounts that transacted in the (one-day) window; _extra therefore = essentially the entire holdings book. Those injected rows get null account_name/account_display_name/relationship_name/account_owner/account_is_open/closed_date, tax_status defaulted to 'taxable' (L502-504 map(...).fillna('taxable') on null tax_status_1), qualified_flag=False (L512), client_state/city/zip -> '' (L515-528).
- merge_incremental (L681): new_ids now contains those snapshot accounts, so any established account X in existing is in updated_ids = existing_ids & new_ids (L390). result_upd starts from the good existing row (L405) then the loop `result_upd[col] = upd_new[col]` (L414-417) overwrites every column NOT in preserve_cols (L408-413) with the injected null/default. preserve_cols keeps only the historical dates + build metadata + advisor cols; account_name, tax_status, qualified_flag, client_*, account_owner, relationship_name, account_is_open, closed_date are all overwritten.

PRECONDITIONS VERIFIED:
1. A_00 runs --incremental nightly: dispatcher CATALOG entry is `A_00|A_00.accounts_dimension.py|--upload --incremental` and gold_dispatch.sh L263-264 comment states 'A_00/C_06 carry it in their CATALOG entry (always incremental in chain runs)'. Both run_chain and run_chain_parallel PHASE_A1 invoke it with these default flags. Steady state has an existing dimension + _last_txn_file_date watermark (written L697/L726), so L660 does NOT fall back to full.
2. silver/holdings/ is POPULATED for COT (live aws s3 ls: daily ~380KB parquets through 2026-07-02), so load_snapshot_accounts returns non-empty and the L479 union is NOT a no-op (unlike 49F).
3. On any business day only a handful of the book's accounts transact, so _extra ~ the whole book.

LIVE SERVED EVIDENCE (gold/dimensions/accounts_dimension_latest.parquet, data_as_of/updated 2026-07-07 02:02Z, watermark 2026-07-07 — i.e. produced by an incremental run):
- 825 accounts. 13 accounts have NULL account_name but a NON-NULL first_transaction_date (e.g. 2026-05-20, 2026-06-05) and non-null account_open_date. A first_transaction_date can only exist if the account actually transacted, and a transacting account always carries account_name in the txn schema — so these provably had a real name that was overwritten to null while their historical dates survived. That preserved-dates / nulled-name split is the exact fingerprint of preserve_cols (L408-413) vs the overwrite loop (L414-417). The remaining 83 null-name accounts also have null first_transaction_date — those are the legitimately txn-less snapshot-only accounts the union was designed for, confirming the two populations are cleanly separable and the 13 are genuine corruption.
- 96/825 blank client_state (exactly matching the 96 null names); tax_status = 'taxable' for 100% of 825 and qualified_flag = False for 100% of 825 (a real book with IRA/Roth/401k accounts cannot be all-taxable) — corroborating book-wide degradation of the overwritten fields.

The bug is silent (rc=0, no crash), cumulative, and persistent: a non-trading day nulls the fields; only a fresh transaction restores the txn-sourced ones and only a full rebuild fully repairs. It corrupts a foundational served dimension consumed by D_00 portal aggregates and the tax/state/client summaries. Severity CRITICAL confirmed — this is not latent, it is already corrupting served data. (Note: the reviewer's specific per-field predictions are all borne out; the only nuance is that 100% taxable may be compounded by a sparse COT tax_status_1, but the account_name/client_state/account_owner nulling on transacted accounts is unambiguously this defect.)
