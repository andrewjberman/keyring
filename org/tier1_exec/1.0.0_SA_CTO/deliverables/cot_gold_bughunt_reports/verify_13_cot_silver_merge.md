# VERIFY #13 -- target: cot_silver_merge.py

- is_real: **False**
- confidence: **refuted**
- corrected_severity: low

## Reasoning
REFUTED. The finding's mechanism requires df['account_id'] to be NUMERIC so the apply-step `.astype(str)` (L2403-2404) diverges from the compute-step raw dict keys built from `acct = row.account_id` (L2371). That precondition is factually false for Cottonwood.

GROUND TRUTH ON DTYPE: Cottonwood account_ids are alphanumeric strings with a lowercase 'z' prefix -- e.g. "z0818656451", "z0818656501", "z0812933851" -- confirmed in data/cot/scripts/gold/aua_overrides.json (L10,15,26) and insurance_accounts.json, both of which key real per-account overrides against the pipeline's account_id domain. The 'z' prefix makes these values inherently non-numeric.

- Silver producer cot_silver_merge.py:181-201 reads cells via openpyxl data_only=True; a text cell (contains 'z') returns a Python str, so pd.DataFrame(rows) infers account_id as object dtype. L398-400 then str-casts every object column (idempotent on already-strings). Both silver/transactions and silver/allocations go through this identical path -> account_id is string in both. There is no numeric account_id for this firm.
- In B_01, load_transactions (L231-268) never casts account_id; FIFO lots inherit the string account_id via _process_group (L2155); df['account_id'] is NEVER reassigned and NEVER numeric-cast (only account_market_value at L840 and purchase_year at L1050/1303/2716 are numeric-cast). Synth path L1610 (`synth_df['account_id'] + ':' + ...`) uses string concatenation, which would raise TypeError on a numeric account_id -- corroborating a uniformly-string account_id domain.

WHY THE CITED APPLY STEP IS CORRECT: compute side acct = "z0818656451" (string); scale_by_acct keys are these strings. Apply side acct_s = df['account_id'].astype(str).str.strip() -- astype(str) is a NO-OP on already-string values, yielding the identical "z0818656451" keys. acct_s.map(scale_by_acct) MATCHES; fillna(1.0) fills only genuinely-absent accounts; the B/C scale applies as intended. The all-NaN -> fillna(1.0) -> zero-compression collapse cannot occur because the raw value is already a string and astype(str) cannot change it.

The finding even self-admits it does not fire today (masked by Finding #1's early return at L2303). It would only ever matter under BOTH open_mask non-empty AND numeric account_id; the second condition never holds for Cottonwood. Corrected severity: low (cannot fire for this firm's data). Confidence: refuted via traced dtype ground truth.
