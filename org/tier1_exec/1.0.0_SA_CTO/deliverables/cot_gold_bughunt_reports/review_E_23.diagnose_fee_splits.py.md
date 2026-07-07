# REVIEW -- E_23.diagnose_fee_splits.py

- script: `data/cot/scripts/gold/E_23.diagnose_fee_splits.py`
- verdict: **issues-found**
- runs_in_incremental: False
- findings: 4

## Finding 1 -- [medium/other/both]
- **Location:** `data/cot/scripts/gold/E_23.diagnose_fee_splits.py:99-109 (Q4) and :62-83 (Q2)`
- **Mechanism:** E_23 is a 49F-inherited fee-split integrity diagnostic that is dead/misleading for Cottonwood. cot silver carries none of the 5 role or 6 split columns, so A_01 writes every *_split_pct = 0.0 and (via the ADVI_COTPPLADVFIX synthetic bridge) sets architect = 'Cottonwood Capital Advisors' uniformly while the other 4 roles = 'Unassigned'. Given that served state: (1) Q4's has_name mask is True for architect (the synthetic name is not in its 'unassigned/nan/none' exclusion set) while architect_split_pct == 0 for all rows, so has_name_zero_split == has_name and Q4 prints exactly one line reporting '100.0%' of named architects have a 0% split -- which reads as a critical fee-attribution failure but is simply the expected no-split-data state; (2) Q2 only tests architect against the 49F-only sentinels '49F House'/'Unassigned'/''/None, none of which match 'Cottonwood Capital Advisors', so every subset is empty, the loop continues on every iteration, and Q2 emits just its header with no body. NOTE: this script is not in the dispatcher CATALOG or any chain (full or incremental) and never writes a served artifact -- it is an ad-hoc, stdout-only diagnostic, so the harm is a materially-misleading human read, not a served-number corruption or chain abort.
- **Failure scenario:** An operator runs `python3 E_23.diagnose_fee_splits.py` against opal-data-cot to sanity-check fee splits. Q4 prints 'architect: N with name, N with 0% split (100.0%)' and Q1 prints 'Exactly 100: 0 / N (0.0%)' + 'Accounts with split_sum ~0 (all zero): N'. A reader concludes fee splits are catastrophically broken, when in fact cot has no split data at all and this is the expected synthetic-advisor baseline -- a false-alarm diagnostic.
- **Proposed fix:** Gate E_23 as a no-op-with-explanation for cot: detect all-zero split_cols and/or the synthetic 'Cottonwood Capital Advisors' architect and print 'SKIP: cot carries no fee-split/role dimension (synthetic single-advisor bridge active) -- fee-split integrity checks are 49F-only and N/A for this firm', rather than emitting Q1/Q2/Q4 numbers that read as integrity failures. Longer term, exclude this 49F-role diagnostic from the cot tree.

## Finding 2 -- [low/empty-null-handling/both]
- **Location:** `data/cot/scripts/gold/E_23.diagnose_fee_splits.py:54`
- **Mechanism:** `exact_100/len(latest)*100` divides by len(latest) with no empty guard. If the advisor_assignments_history.parquet exists but has 0 rows (empty firm / first run before any transactions), `latest` is empty and this raises ZeroDivisionError after line 39 already printed 'Accounts (latest SCD record): 0'. Diagnostic-only (not in any chain), so it crashes this script's output but cannot abort the gold run.
- **Failure scenario:** advisor_assignments_history.parquet is present but empty (e.g., a brand-new firm partition or a run before any silver/transactions exist). E_23 reaches Q1, computes exact_100=0, then evaluates 0/0*100 -> ZeroDivisionError and the diagnostic dies with a traceback instead of a clean 'no accounts' message.
- **Proposed fix:** Guard len(latest): `if latest.empty: print('No SCD records'); return` immediately after loading, and/or compute percentages as `exact_100/len(latest)*100 if len(latest) else 0.0`.

## Finding 3 -- [low/merge-dedup/both]
- **Location:** `data/cot/scripts/gold/E_23.diagnose_fee_splits.py:114-120 (Q5)`
- **Mechanism:** Q5 cross-checks two independently-produced dimensions via Python sets: `in_scd = set(latest['account_id'])` (from A_01 advisor_assignments) and `in_dim = set(acct_dim['account_id'])` (from A_00 accounts_dimension). account_id is not dtype-normalized before the set operations. If the two producers emit account_id with different dtypes (e.g., A_01 derives it as str from transactions while A_00 emits int64, or one has NaN/float), then '123' != 123 in a Python set, so `in_scd & in_dim` silently under-counts 'In both' and inflates the 'In dim only'/'In SCD only' buckets -- a silently wrong overlap report. Diagnostic-only, no served impact.
- **Failure scenario:** A_00 writes account_id as int64 while A_01 writes it as str (or vice versa). Q5 prints 'In both: 0', 'In dim only (no SCD): <all>', 'In SCD only (not in dim): <all>', implying total dimension divergence when the accounts actually match on value -- a misleading cross-check.
- **Proposed fix:** Coerce both to a common dtype before the set ops, e.g. `set(latest['account_id'].astype(str))` and `set(acct_dim['account_id'].astype(str))`.

## Finding 4 -- [low/unguarded-read/both]
- **Location:** `data/cot/scripts/gold/E_23.diagnose_fee_splits.py:36 and :113 (via _read_s3, :26-28)`
- **Mechanism:** `_read_s3(ADVISOR_ASSIGNMENTS)` (line 36) and `_read_s3(ACCOUNTS_DIMENSION)` (line 113) call s3.get_object with no try/except. On an absent key (NoSuchKey) or before A_00/A_01 have ever produced these dimensions, the diagnostic raises an uncaught ClientError. Both artifacts are produced by A_00/A_01 in CHAIN_FULL so they normally exist, and E_23 is not part of any chain, so this crashes only the diagnostic run, never the gold chain.
- **Failure scenario:** An operator runs E_23 on a fresh firm partition (or after the dimensions prefix was cleared) before A_00/A_01 have written accounts_dimension_latest.parquet / advisor_assignments_history.parquet. E_23 aborts at line 36 with a botocore NoSuchKey traceback rather than a clear 'dimension not built yet' message.
- **Proposed fix:** Wrap the two _read_s3 calls in try/except botocore.exceptions.ClientError and print a clear 'BLOCKED: <key> not found -- run A_00/A_01 first' then exit cleanly, matching A_01's own load_accounts() guarded-read pattern.
