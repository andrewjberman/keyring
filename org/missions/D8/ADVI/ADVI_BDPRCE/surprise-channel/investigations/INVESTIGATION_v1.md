# ADVI_BDPRCE -- surprise channel, INVESTIGATION v1

**Home:** the project tree's channel; rows are validated by `.tools/surprise-row-gate.py`. A seat's row is `ADVI_BDPRCE-S<k>`; a worker's is `ADVI_BDPRCE-W<n>-S<k>`; a dell1 row carries the fabric coordinate `ADVI_BDPRCE-D1-S<k>` / `ADVI_BDPRCE-D1-W<n>-S<k>`. **Append-only during the round.**

Section opened by `0.9.0_WK_ADVI_BDPRCE~3` under task order `ADVI_BDPRCE.TO-BP-a-3.gap-603-of-1610` (round 1, fabric dell1). This worktree was cut at `f75da01777`, before the channel file existed on the integration branch; the section below is worker ~3's alone. The drain must union it with the sections of workers ~1 and ~2, byte for byte, as the round-1 drain did before. Rows describe the world against the task order's premises; they do not rule on significance.

## ADVI_BDPRCE-D1-W3-S1 -- The window holds 1,657 served transaction_observed rows, not the 1,610 the task order names

```json
{
  "id": "ADVI_BDPRCE-D1-W3-S1",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~3",
  "surfaced_at": "2026-10-13T14:13:19Z",
  "one_line": "The window 2026-09-16..2026-10-13 holds 1,657 served transaction_observed rows in canonical_prices.parquet, not 1,610; no canonical version checked yields 1,610.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/prices/canonical_prices.parquet, six versions read by get-object --version-id: 2026-10-12T23:03:03Z, 2026-10-13T00:15:27Z, 04:03:42Z, 09:49:48Z, 12:47:50Z, 12:48:05Z (current): 1657 transaction_observed rows each, 18 dates",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~3/GAP.json denominator_note (served_rows 1657; classes sum to 1657)",
      "the 1,657 splits 1,148 EQUAL, 197 EXPLAINED_BY_MULTIDAY_WINDOW, 232 EXPLAINED_OTHER, 64 UNEXPLAINED, 16 NOT_RECOMPUTABLE (GAP_ROWS.csv)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 1b step 1: the served transaction_observed rows of the 20 weekday dates ending 2026-10-13 number 1,610 (the denominator is printed; a window shift is expected, a forced number is not).",
  "world_is": "The same window holds 1,657 transaction_observed rows on every canonical version of 2026-10-12 and 2026-10-13. The 47-row difference is not explained by a window shift: the window dates are unchanged. The measurer's split of 1,007 equal and 603 not equal is also not reproduced; this read gives 1,148 raw-equal and 1,266 equal under the de-duplicated rule."
}
```

## ADVI_BDPRCE-D1-W3-S2 -- Six of the twenty window dates have no daily silver/prices file, so the write-time anchor is absent for 178 served rows

```json
{
  "id": "ADVI_BDPRCE-D1-W3-S2",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~3",
  "surfaced_at": "2026-10-13T14:13:19Z",
  "one_line": "silver/prices/<date>.parquet is absent for 2026-09-21, 09-22, 09-28, 09-29, 10-05 and 10-06; the task order's write-time test anchors on the first version of that file, so it cannot run for their 585 served rows (178 of them not raw-equal).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bucket listing of silver/prices/ (list-objects-v2 and list-object-versions, run 2026-10-13 in this session): daily files exist for 14 of the 20 window weekdays; none in any version for the six dates named",
      "GAP.json version_test field; the six dates hold 585 served rows (78 + 217 + 134 + 52 + 36 + 68), 178 of them not raw-equal (served_rows per date in the run output)",
      "the write-time version was made unnecessary by a superset test: no version of any window-date transaction partition reproduces any of the 509 non-equal rows (74 versions read)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 1b step 3a: the write time of a served row is the LastModified of the first version of silver/prices/<date>.parquet (or of the canonical version that first carries the row).",
  "world_is": "For six of the twenty window dates there is no daily file in any version. On the two dates compared (2026-09-17 and 09-30), about 40% of assets present in both the daily file and the served canonical rows carry different prices, mostly yahoo_finance rows, and the served transaction_observed price matched some daily-file version for only 2 of the 462 non-equal rows. The daily file is therefore not a faithful anchor for the served value. Write time must come from canonical object versions, which were not read."
}
```

## ADVI_BDPRCE-D1-W3-S3 -- The T1 rule as written in bd_price_update.py reproduces fewer served rows than a de-duplicated or price-first reading, so the served values are not produced by the rule the task order names

```json
{
  "id": "ADVI_BDPRCE-D1-W3-S3",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~3",
  "surfaced_at": "2026-10-13T14:13:19Z",
  "one_line": "Of 1,657 served rows, 1,148 equal the T1 rule as written on the current partition, 1,266 equal it after de-duplication by transaction_id, and 169 more equal the JOB 2 price-first observed rule of the same file; the rule the task order names is not the one that produced most served values.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~K1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/black_diamond/scripts/silver/bd_price_update.py:263-271@f75da01777 load_transactions_for_date does no de-duplication; :327-344 extract_t1_prices is the rule as written",
      "data/black_diamond/scripts/silver/bd_price_update.py:677-706@f75da01777 extract_observed_prices: price column first where price > 0, else market_value / units; CASH excluded",
      "GAP.json classes and other_causes (c2 169 rows; overlap_note: 123 of the 197 multi-day rows are also reproduced by the own-day de-duplicated rule)",
      "measured on the current partitions of the 40 weekday dates 2026-08-19..2026-10-13 (gap_measure.py, GAP_ROWS.csv evidence_ref)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 1a: the served transaction_observed price is the median of |market_value| / |units| over the rows of that day's partition, as extract_t1_prices computes it.",
  "world_is": "The served values follow a de-duplicated median or the price-first observed rule far more often than the rule as written. Which writer produced each served row is not established by this read (lambda_function.py:441 and build_canonical_prices_v2.py:660 are named writers; their T1 rule was read only for lambda_function.py, which matches the file as written). The gap is the writer's rule, not a day's data."
}
```

## ADVI_BDPRCE-D1-W3-S4 -- Cash-dividend rows enter the T1 median with a per-unit price of 1.0, so the recompute is 1.0 for 19 residual assets

```json
{
  "id": "ADVI_BDPRCE-D1-W3-S4",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~3",
  "surfaced_at": "2026-10-13T14:13:19Z",
  "one_line": "On 2026-09-22 the partition's Dividend rows carry units equal to the cash amount, so market_value / units is 1.0; the T1 median for BLACKROCK INC COM is 1.000000 while the served price is 1,073.162298.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~K1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/transactions/2026-09-22.parquet (current version, read by get-object): 52,792 rows; 29,158 of type Dividend and 18,241 of type Dividend Reinvestment; for the BLACKROCK rows, Dividend rows show units equal to market_value (e.g. units 194.8200, market_value 194.82)",
      "GAP_ROWS.csv: 19 UNEXPLAINED rows whose recomputed_price is exactly 1",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~3/GAP.json bound_statement"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 1a: extract_t1_prices keeps every row with units not null and market_value not null and non-zero, and takes the median of |market_value| / |units| per asset over ALL rows.",
  "world_is": "The rule keeps cash-dividend rows, whose ratio is the dividend amount per cash unit (1.0 in these rows), so the median is 1.0 for assets whose cash rows outnumber trade rows on that day. The rule as written therefore yields a price that is not a price for these rows. The residue of 64 UNEXPLAINED rows includes these; no version reproduces them."
}
```

## ADVI_BDPRCE-D1-W3-S5 -- The task order's channel file, id grammar and reach premise did not hold at this worktree's cut

```json
{
  "id": "ADVI_BDPRCE-D1-W3-S5",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~3",
  "surfaced_at": "2026-10-13T14:13:19Z",
  "one_line": "The task order names the channel file and the row grammar ADVI_BDPRCE-W3-S<k>; at cut f75da01777 the file did not exist, and the channel header requires the dell1 coordinate D1 on dell1 rows, which this section uses.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git worktree at f75da01777: org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/ absent; the integration branch holds the file with the sections of workers ~1 and ~2 (merged by 2.0.0_SA_COO~K1 at the round-1 drain)",
      "channel header (INVESTIGATION_v1.md, Home line): a dell1 row carries ADVI_BDPRCE-D1-S<k> / ADVI_BDPRCE-D1-W<n>-S<k>",
      "task order section 5: row ids ADVI_BDPRCE-W3-S<k>"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 3 and section 5: the surface is the investigation file at the named path, and row ids are ADVI_BDPRCE-W3-S<k>.",
  "world_is": "The file is not in this worktree's history; a section was created here so the rows exist on the branch. The drain's union must carry the W1 and W2 sections alongside this one. The id form follows the channel header for dell1; the W3 form in the task order is equivalent to the schema pattern, which admits both."
}
```
