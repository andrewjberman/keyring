# ADVI_BDPRCE -- surprise channel, INVESTIGATION v1

**Home:** the project tree's channel; rows are validated by `.tools/surprise-row-gate.py`. A seat's row is `ADVI_BDPRCE-S<k>`; a worker's is `ADVI_BDPRCE-W<n>-S<k>`; a dell1 row carries the fabric coordinate `ADVI_BDPRCE-D1-S<k>` / `ADVI_BDPRCE-D1-W<n>-S<k>`. **Append-only during the round.**

Opened by `0.9.0_WK_ADVI_BDPRCE~2` under task order `ADVI_BDPRCE.TO-BP-a-2.trace-instrument` (round 1, fabric dell1). Rows describe the world against the task order's premises; they do not rule on significance.

## ADVI_BDPRCE-D1-W2-S1 -- The newest daily price file has no transaction_observed row, so --first-transaction-observed walked back two files

```json
{
  "id": "ADVI_BDPRCE-D1-W2-S1",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~2",
  "surfaced_at": "2026-10-13T13:27:49Z",
  "one_line": "The task order's --date latest --first-transaction-observed expects a transaction_observed row in the newest silver/prices file; that file and the one before it carry none, so the instrument walked back to 2026-10-11.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/prices/2026-10-13.parquet read live from opal-data-bd (get_object, 2026-10-13T13:2xZ): 11143 rows; source counts carry_forward 7857 and yahoo_finance 3286; no transaction_observed row",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~2/TRACE_SAMPLE.json@a92c09ba8f selection block: newest_daily_date 2026-10-13, observed_rows_in_newest_file 0, files_scanned 3, rows_scanned 1, selected_daily_date 2026-10-11, walked_back true",
      "rows_scanned 1 over 3 files means 2026-10-13 and 2026-10-12 carry no transaction_observed row (the walk counts every such row before the selected one)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 1b step 5: --date latest resolves to the newest silver/prices/<date>.parquet, and --first-transaction-observed takes the first row (file order) with source transaction_observed that has a valid trade in that day's partition.",
  "world_is": "The newest file holds no transaction_observed row at all, and neither does 2026-10-12. The first qualifying row is in 2026-10-11. The instrument walks back over daily files newest first and records walked_back true with the counts; it does not stop on an empty sample. The sample is therefore a 2026-10-11 row, not a newest-day row."
}
```

## ADVI_BDPRCE-D1-W2-S2 -- The day's transaction partition repeats transaction_id on most rows, so the recompute is a median over repeats

```json
{
  "id": "ADVI_BDPRCE-D1-W2-S2",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~2",
  "surfaced_at": "2026-10-13T13:27:49Z",
  "one_line": "silver/transactions/2026-10-11.parquet repeats transaction_id on 6210 of 6278 rows, so rows_used and distinct_trade_ids diverge widely and the transaction_observed median is taken over repeated rows.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~K1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/transactions/2026-10-11.parquet read live from opal-data-bd: 6278 rows; rows whose transaction_id occurs more than once: 6210 (duplicated(keep=False) count)",
      "sample asset ABBOTT LABORATORIES COM on 2026-10-11: 4 rows, one transaction_id, units 166.0 on all four, market_value 16533.6 on all four (read live, not printed beyond these two values)",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~2/TRACE_SAMPLE.json@a92c09ba8f: rows_used 4, distinct_trade_ids 1, median_distinct 99.6, recomputed_price 99.6, match true",
      "data/black_diamond/scripts/silver/bd_price_update.py:263-271@f75da01777 load_transactions_for_date does no de-duplication on transaction_id"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order sections 1a and 1b step 3: load_transactions_for_date does no de-duplication on transaction_id, repeats are kept in trade_ids and rows_used, and recomputed_price is the median over ALL rows used, exactly as the rule does today.",
  "world_is": "Repeats are the norm in this partition, not an edge case: 6210 of 6278 rows share a transaction_id with another row. The sample's four rows are identical, so the median equals the one value and match is true. Where repeats carry different prices the median is weighted by repetition. Left alone, every transaction_observed price written from the daily path is computed this way. The instrument reproduces that faithfully and reports distinct_trade_ids beside rows_used so the divergence is visible."
}
```

## ADVI_BDPRCE-D1-W2-S3 -- The daily file and the canonical file disagree on source for the same asset and date

```json
{
  "id": "ADVI_BDPRCE-D1-W2-S3",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~2",
  "surfaced_at": "2026-10-13T13:27:49Z",
  "one_line": "For ABBOTT LABORATORIES COM on 2026-10-11 the daily file says transaction_observed and canonical says linear_interpolation; the canonical row also carries a float32 price.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/prices/2026-10-11.parquet read live from opal-data-bd: source transaction_observed, price 99.6, ticker ABT",
      "silver/prices/canonical_prices.parquet read live from opal-data-bd: rows for 2026-10-11, 2026-10-12 and 2026-10-13 all source linear_interpolation, price 99.599998 (float32 rounding), ticker ABT",
      "data/black_diamond/scripts/silver/bd_price_update.py:587-602@f75da01777 upsert_canonical keeps the lowest SOURCE_RANK on a (date, asset_name) conflict"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 1a and 1b step 1: a same-date pair is a tie, reported as a tie and not picked by rank silently; upsert_canonical keeps the lowest SOURCE_RANK, so transaction_observed (0) would beat linear_interpolation (2) on a conflict.",
  "world_is": "The two objects disagree on the source label for the same date. The values agree within the match tolerance (the gap is float32 rounding of 99.6). The instrument reports tie true, lists both rows, and takes the daily row as the stable pick. Only the label and the B_01 keep decision differ. The rank rule would have kept transaction_observed in canonical, so the daily row did not reach canonical by that rule."
}
```

## ADVI_BDPRCE-D1-W2-S4 -- The backfill path de-duplicates transaction_id and the daily path does not, so one rule has two recomputes

```json
{
  "id": "ADVI_BDPRCE-D1-W2-S4",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~2",
  "surfaced_at": "2026-10-13T13:27:49Z",
  "one_line": "A transaction_observed row written by backfill_new_assets is computed from transactions de-duplicated on transaction_id, while the daily path is not, so the instrument's recompute can disagree with a correct backfill row.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~K1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/black_diamond/scripts/silver/bd_price_update.py:257-259@f75da01777 load_transactions_for_new_assets drops duplicate transaction_id (keep last) before extract_t1_prices",
      "data/black_diamond/scripts/silver/bd_price_update.py:834-836@f75da01777 Step 1d feeds backfill_new_assets from load_transactions_for_new_assets",
      "data/black_diamond/scripts/silver/bd_price_update.py:263-271@f75da01777 load_transactions_for_date (daily path) has no de-duplication"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 1a: the instrument reproduces what the pipeline does TODAY for the daily path, with no de-duplication on transaction_id; it names the rule by source for any served row.",
  "world_is": "The same transaction_observed rule has two readers. Backfilled history (new assets) is computed over de-duplicated trades; the daily path is not. A backfill-written row can therefore disagree with this instrument's recompute and show match false while being correct for its writer. The canonical object does not record which path wrote a row, so the instrument cannot tell the two apart and says so in the rule text. The reproduction is exact for the daily path only."
}
```

## ADVI_BDPRCE-D1-W2-S5 -- The task order names bare row ids ADVI_BDPRCE-W2-S<k>; the gate on dell1 requires the D1 coordinate

```json
{
  "id": "ADVI_BDPRCE-D1-W2-S5",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~2",
  "surfaced_at": "2026-10-13T13:32:37Z",
  "one_line": "Task order section 5 names row ids ADVI_BDPRCE-W2-S<k>; surprise-row-gate refuses a dell1 row whose id carries no coordinate, so the four rows are filed as ADVI_BDPRCE-D1-W2-S<k>.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "surprise-row-gate.py refusal at commit of a92c09ba8f's follow-on commit (dell1 rows with id ADVI_BDPRCE-W2-S1..S4): 'fabric=dell1 but the id carries no coordinate ... dell1 = id <CODE>-D1-S<n>; worker: <CODE>-D1-W<n>-S<k>'",
      "org/missions/D8/ADVI/ADVI_BILLING/surprise-channel/investigations/INVESTIGATION_v1.md: row ADVI_BILLING-D2-W2-S1 is filed by a dell2 worker with the D2 coordinate"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 5: Row ids: ADVI_BDPRCE-W2-S<k>, k from 1.",
  "world_is": "The house id grammar for a dell1 worker carries the D1 coordinate, and the gate enforces it. The rows are filed with ADVI_BDPRCE-D1-W2-S1 to S4 and this row. The instance cites the D1 ids. The k sequence and the W2 slot are unchanged."
}
```
