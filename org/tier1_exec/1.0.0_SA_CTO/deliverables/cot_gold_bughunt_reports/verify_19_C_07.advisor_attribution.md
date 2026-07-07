# VERIFY #19 -- target: C_07.advisor_attribution.py

- is_real: **True**
- confidence: **confirmed**
- corrected_severity: critical

## Reasoning
REAL and actively firing. Traced a concrete, verified trigger end-to-end.

CODE: C_07.advisor_attribution.py:278 `open_acct = acct_dim[acct_dim['account_is_open'] == True].copy()` is an UNCONDITIONAL column subscript. acct_dim is loaded at line 268 via _read_s3(ACCOUNTS_DIMENSION) and reaches 278 with no `in columns` guard, no .get(), no try/except. main() has no exception handling and __main__ calls main() bare, so a KeyError propagates uncaught -> Python exits nonzero.

ROOT CONFIRMED: In A_00.accounts_dimension.py `account_is_open` is ONLY a transaction passthrough (TXN_ACCOUNT_COLS:88, output_cols:566) and is never derived. A_00:239 (keep_cols filter) and A_00:588 `available=[c for c in output_cols if c in accts.columns]` both silently drop it when absent from source. Grep of data/cot/scripts/silver/cot_silver_merge.py for account_is_open returned ZERO matches -- cot silver never produces it, so it is dropped.

LIVE VERIFICATION (boto3 read of the exact key C_07 reads, ACCOUNTS_DIMENSION='gold/dimensions/accounts_dimension_latest.parquet' on opal-data-cot): 825 rows, 23 columns, account_is_open present? False (closed_date also absent; account_open_date present). Matches the flag exactly.

IN-CHAIN + HARD-FAIL: gold_dispatch.sh puts C_07 in CHAIN_DOWNSTREAM (:142) -> CHAIN_FULL (:147) and parallel PHASE_C4 C_04||C_07 (:435). Serial run_chain runs under `set -e` (:57); parallel wait_phase does `exit 1` on any nonzero PID (:359). Either path aborts on a C_07 crash.

EMPIRICAL PROOF IT FIRES: live listing of s3://opal-data-cot/gold/views/ contains only firm_composition.json, mix_daily_summary.json, nna_aua_by_advisor/geography(_city).parquet. C_07's three outputs -- account_team.parquet, relationship_team.parquet, rel_architect_lookup.parquet (keys per s3_layout.py:148-151) -- are ALL MISSING. C_07 has never landed output; the crash is not hypothetical.

No refutation survives: no alternate dimension source (S3_BUCKET=opal-data-cot, exact verified key), no guard between load and 278, no error swallowing. Severity critical: a guaranteed unconditional crash of a mid-chain gold script under the runner's documented hard-fail contract, cascading to the empty served advisor layer (D_02/D_04 have no account_team) and, if the chain aborts as coded, blocking downstream C_06/C_08/D_* on every nightly. The `== True` comparison is moot -- the KeyError precedes it.
