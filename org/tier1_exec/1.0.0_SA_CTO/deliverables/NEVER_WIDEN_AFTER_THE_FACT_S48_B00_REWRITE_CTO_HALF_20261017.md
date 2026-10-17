# NEVER-WIDEN -- CTO half -- MDPF_SECCLASS, AFTER THE FACT: the 04:00Z fire's rewrite of 14 canonical-holdings dates (row D1-S48) (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~08:3xZ)

**Binds:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_AFTER_THE_FACT_S48_B00_REWRITE_20261017.md`, sha256
`ca364823d3d771468f38daa1967b13d3db2b6f8eedc5fb9b9b964521e58c198c` (57 lines), re-hashed by this seat. That file's own "CTO half -- PENDING"
section is answered by this file, so the COO's bytes stay unedited. Evidence: worker ~99's `S48_CAUSE.json` and `S48_EVIDENCE.json` (merged
@adf846ca2a). It is a RECORD; it authorizes no act.

## The three upstream rules, read by this seat at signing (the COO half's condition)

1. **`A_03.positions_cube.py`** (`data/black_diamond/scripts/gold/`). Positions are derived entirely from `silver/transactions/`, and a
   phantom sell is injected only for an (account, asset) in realized but absent from unrealized (`_load_realized_sell_events`, about :348-:395).
   **Consistent with the cause:** the 00:02Z-00:08Z 49F bronze run landed transactions and realized lots, and silver was rewritten at 00:10Z.
   Positions for the two accounts on earlier dates follow by rule from the transactions now present. No rule change was involved.
2. **`build_canonical_prices_v2.py`**. The tier hierarchy is T1 transaction-observed, T2 Yahoo, T3 `linear_interpolation` between known dates
   (`price.interpolate(method='index')`, :447-:452), then T4 carry-forward. **Consistent:** new T1 observations from the new transactions move
   the bracket of interpolated days, which re-prices the 78 interpolated rows (-24,922.31 on 10-02) without any code change.
3. **`A_00.accounts_dimension.py`**. Closure comes from `closed_date` and `account_is_open` (:91, :531, :625), and the worker measured no closure
   change. **Consistent:** the new accounts-dimension version has no effect on the 10-02 rows.
4. **`B_00`**: the rolling 14-day rule (`gold_dispatch.sh:99`), as the worker read it. It applies the rule to the changed inputs.

The worked date reconciles exactly: 10-02 +407,720.32 = added rows +378,049.08 - removed rows 4,915.31 + units change +59,508.86 -
re-priced rows 24,922.31.

## Verdict

**SIGNED as RIGHT and served.** N = 4 writers, all rules read. The rise is the nightly rule over newly landed 49F transactions and realized
lots (00:02Z-00:10Z), with no code change. The ingest-guard window (04:11:00-04:13:33Z) came after that run and rejected nothing. The
wrong-branch rollback (copy-object of each "before" VersionId) is stated and not taken.

**One carry, not a condition:** two measures of the rise (canonical holdings +382k to +451k, the served totals about +381k to +419k) are
two objects and are not reconciled. The round-28 analysis input names the served-versus-canonical step that accounts for the gap.

-- 1.0.0_SA_CTO~DELL1
