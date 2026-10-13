# ADVI_BDPRCE -- surprise channel, INVESTIGATION v1

**Home:** the project tree's channel; rows are validated by `.tools/surprise-row-gate.py`. A seat's row is `ADVI_BDPRCE-S<k>`; a worker's is `ADVI_BDPRCE-W<n>-S<k>`; a dell1 row carries the fabric coordinate `ADVI_BDPRCE-D1-S<k>` / `ADVI_BDPRCE-D1-W<n>-S<k>`. **Append-only during the round.**

Opened by `0.9.0_WK_ADVI_BDPRCE~2` under task order `ADVI_BDPRCE.TO-BP-a-2.trace-instrument` (round 1, fabric dell1). Rows describe the world against the task order's premises; they do not rule on significance.

Merged at the round-1 drain by `2.0.0_SA_COO~K1`: each worker opened this file in its own worktree, so the file below is the UNION of worker ~2's section (rows `ADVI_BDPRCE-D1-W2-S1..S5`), worker ~1's section (rows `ADVI_BDPRCE-D1-W1-S1..S7`) and worker ~3's section (rows `ADVI_BDPRCE-D1-W3-S1..S5`, last). Every row is carried byte for byte from its worker's branch; no row was edited.

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

## Rows filed by `0.9.0_WK_ADVI_BDPRCE~1` under `ADVI_BDPRCE.TO-BP-a-1.writers-census` (denominator at its write: 7 rows, `ADVI_BDPRCE-D1-W1-S1..S7`)

```json
[
  {
    "id": "ADVI_BDPRCE-D1-W1-S1",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~1",
    "surfaced_at": "2026-10-13T13:45:18Z",
    "one_line": "The brief's 'emergency rebuild' build_canonical_prices_v2.py is the daily S_00 silver-prep stage, and the 'fourth writer' is that stage plus its auto-chained inject step: 25 runs in 2026-10-07..13.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S3 telemetry logs/gold-layer/telemetry/bd-gold-layer-runner/S_00/<run_id>.jsonl, 25 objects 2026-10-07..13 (per day 4,4,4,4,2,4,3); sample windows 2026-10-13T04:01:22Z-04:03:44Z (run 974f6f518bde), 2026-10-13T12:45:52Z-12:48:08Z (run b09cfe1b7fe6), 2026-10-12T00:18:44Z-00:21:03Z (run acc7e72b7bf5), read 2026-10-13",
        "gold_dispatch.sh@f75da01777:93 (CATALOG S_00|build_canonical_prices_v2.py), :137 (CHAIN_SILVER_PREP=S_00), :1281 (silver-prep auto-run before the daily full chain)",
        "build_canonical_prices_v2.py@f75da01777:660 (s3.upload_file of silver/prices/canonical_prices.parquet), :670 (_run_inject_scoped_overrides), :506 (subprocess inject --upload); inject_scoped_overrides.py@f75da01777:253 (put_object of the same key)",
        "canonical versions 2026-10-13T04:03:26Z and 04:03:42Z, 12:47:50Z and 12:48:05Z (15-16 s pairs), inside the S_00 windows above"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO BP-a-1 section 1: build_canonical_prices_v2.py (writes at :660) is 'the emergency rebuild'; 'a fourth writer that rewrites canonical_prices.parquet about four times a day has not been identified'.",
    "world_is": "build_canonical_prices_v2.py is the S_00 silver-prep stage of the daily gold chain, not an emergency-only tool; each S_00 run auto-chains inject_scoped_overrides.py --upload, which puts the same table about 15 s after the build. Together they are the 4x/day writer (S_00 at about 04:01, 09:4x, 12:4x and 23:0x). The S3 copy of the script equals the repo file (md5 5353babb2fb29d23c558848351225cf7)."
  },
  {
    "id": "ADVI_BDPRCE-D1-W1-S2",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~1",
    "surfaced_at": "2026-10-13T13:45:18Z",
    "one_line": "The ADVI 49F chain dispatcher and its SSM command run on the same EC2 host (i-01003b035d2988dfb) that runs the BD gold runner and its S_00 canonical writer.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws lambda get-function-configuration advi-49f-gold-dispatch (read 2026-10-13): HOST_INSTANCE_ID=i-01003b035d2988dfb, SSM_DOCUMENT_NAME=advi-49f-chain-dispatch, CHAIN_LOG_BUCKET=opal-data-49financial",
        "aws ssm list-commands --instance-id i-01003b035d2988dfb: advi-49f-chain-dispatch Success at 2026-10-07..13 08:45Z on each of the 7 days and 05:47Z on 4 of them; no other command in the 2026-10-07..13 window names it (command text truncated in the listing)",
        "aws ssm get-document advi-49f-chain-dispatch: aws s3 sync s3://opal-data-49financial/_code/ then python3 chain_49f_entrypoint.py --production (the 49F chain, not the BD gold chain)",
        "aws logs filter-log-events /aws/lambda/advi-49f-gold-dispatch (REPORT, from 2026-10-06): REPORT lines at about 09:46Z and 12:48Z on most days, read 2026-10-13"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO BP-a-1 1a.2 and the decomposition: the 49 Financial served home is opal-data-49financial; the 49F ADVI chain is its own scheduled stage, not a stage of the BD chain.",
    "world_is": "The 49F chain's dispatcher and SSM document target the BD gold runner host, the host that boots run-gold-layer.sh and runs the BD S_00 canonical writer. Whether a 49F dispatch starts any BD S_00 run is not established (see S5)."
  },
  {
    "id": "ADVI_BDPRCE-D1-W1-S3",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~1",
    "surfaced_at": "2026-10-13T13:45:18Z",
    "one_line": "The deployed bd-price-update Lambda carries a rank table with no scoped_override key, and it writes the canonical table daily at about 00:15Z before the 04:03Z S_00 rebuild restores the overrides.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~K1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bd-price-update lambda_function.py@f75da01777:60-65 SOURCE_RANK {transaction_observed 0, yahoo_finance 1, linear_interpolation 2, carry_forward 3}; the silver copy data/black_diamond/scripts/silver/bd_price_update.py@f75da01777:65-71 ranks scoped_override -2 and yahoo_finance -1",
        "lambda_function.py@f75da01777:427 combined['_rank'] = combined['source'].map(SOURCE_RANK).fillna(99): a scoped_override row ranks 99, so a transaction_observed row for the same date and asset wins the dedupe at :430 (read from code, not executed)",
        "deployed Lambda zip (get-function Code.Location, read 2026-10-13) md5 f5d5e0df90ccabdec8cb6a8fe512d41c equals the repo file",
        "canonical versions 2026-10-13T00:15:27Z (105,292,662 bytes) and 04:03:26Z (109,605,884 bytes); the Lambda ran 7 of 7 days 2026-10-07..13"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO BP-a-1 1a.4: name the SOURCE_RANK of each writer; 'a writer with its own literal copy is a second copy'.",
    "world_is": "Two literal rank copies differ in their keys and order. The live Lambda copy lacks the scoped_override key that the silver copy ranks first. Standing effect, from the code: each daily Lambda write can replace a scoped override row for the target date until S_00 rebuilds the table about four hours later. Not executed in this read."
  },
  {
    "id": "ADVI_BDPRCE-D1-W1-S4",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~1",
    "surfaced_at": "2026-10-13T13:45:18Z",
    "one_line": "The brief's silver-script line numbers are partly wrong (the daily put is at :666, not :639) and the silver script has no run in the window; its module is only imported by inject.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/silver/bd_price_update.py@f75da01777:609 (canonical put_object, matches the brief), :639 (key = f-string for the daily key), :666 (put_object of the daily key)",
        "no run telemetry or REPORT line for the silver script 2026-10-07..13; deploy-to-ec2.sh@f75da01777 header lines 16-21 (legacy silver scripts not pulled by the runner on boot)",
        "S3 code/silver/bd_price_update.py ETag 72521f97 equals the repo md5; inject_scoped_overrides.py@f75da01777:80 imports _SCOPED_PRICE_OVERRIDES from it"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO BP-a-1 section 1: the silver script writes at :609 and :639.",
    "world_is": "The put at :609 is right. :639 is the daily key assignment; the daily put is at :666. The script is dormant in the window: no version matches it, and its code is loaded by inject as an import, not run as a writer."
  },
  {
    "id": "ADVI_BDPRCE-D1-W1-S5",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~1",
    "surfaced_at": "2026-10-13T13:45:18Z",
    "one_line": "Three trigger attributions for the BD gold runner (S_00) runs do not close: the 09:4x and 12:4x runs, the 00:xx S3-event starts, and some StartInstances events with no matching REPORT line.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S_00 telemetry: 12 runs at 09:4x and 12:4x in 2026-10-07..13 (09:4x on 10-07,08,09,10,13; 12:4x on 10-07..13); no SSM command in that window names a run, no Lambda REPORT matches, and no StartInstances lookup event for the gold host was read after 2026-10-13T09:00Z",
        "bd-gold-trigger REPORT (filter REPORT from 2026-10-06): 00:14:51..00:23:52Z daily on 10-07..13 (7 invocations), but S_00 ran on 10-12 00:18:44Z only; the other 00:xx S3-event starts produced no S_00 run",
        "aws cloudtrail lookup-events EventName=StartInstances 2026-10-12..13: events attributed to bd-gold-trigger at 2026-10-12T00:00:46Z, 2026-10-12T19:00:11Z and 2026-10-13T00:00:47Z have no bd-gold-trigger REPORT line in the window"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO BP-a-1 1a.3: each writer's runs are attributable to a schedule, event rule, Lambda or runner, so that each version falls within one minute of a run of a named writer.",
    "world_is": "Most S_00 runs are attributed by time to bd-gold-trigger (04:00Z and 23:00Z) or to the S3-event start, but 12 runs at 09:4x and 12:4x have no trigger in the reads above, and the S3-event start produced an S_00 run on one morning of seven. The StartInstances attribution and the REPORT lines disagree for three events. Their cause is not established."
  },
  {
    "id": "ADVI_BDPRCE-D1-W1-S6",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~1",
    "surfaced_at": "2026-10-13T13:45:18Z",
    "one_line": "The task order's surface org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/ did not exist in the worktree; this worker created it with this file.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ls of org/missions/D8/ADVI/ADVI_BDPRCE/ at worktree HEAD f75da01777 (2026-10-13): decompositions/, deliverables/, prd/, task-orders/, project.json; no surprise-channel/ folder",
        "this file is the first channel file for ADVI_BDPRCE; its rows are S1 to S7"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO BP-a-1 section 3: the surface org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md is the channel file this order writes to.",
    "world_is": "The investigations folder did not exist at the base commit; the first row created it. The folder and file are inside the order's surface, so no path outside the grant was written."
  },
  {
    "id": "ADVI_BDPRCE-D1-W1-S7",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~1",
    "surfaced_at": "2026-10-13T13:52:00Z",
    "one_line": "The order's row-id form ADVI_BDPRCE-W1-S<k> is refused by the surprise-row gate for fabric dell1, which requires the coordinate form ADVI_BDPRCE-D1-W1-S<k>.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git commit attempt of this file's first six rows with the bare ids: .tools/surprise-row-gate.py BLOCKED with 6 violations, each 'fabric=dell1 but the id carries no coordinate ... dell1 = id <CODE>-D1-S<n> (worker: <CODE>-D1-W<n>-S<k>)', read 2026-10-13",
        "org/missions/D8/ADVI/ADVI_BDPRCE/task-orders/ADVI_BDPRCE.TO-BP-a-1.writers-census.md section 5 names the bare form ADVI_BDPRCE-W1-S<k>",
        "the id pattern in org/surprise_channel/schemas/investigation_item.schema.json admits the infix form (for example ADVI_BDPRCE-D1-W1-S1); the rows were re-minted in that form before the commit, and the gate's audited override was not used"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO BP-a-1 section 5: row ids are ADVI_BDPRCE-W1-S<k>, k from 1, for a worker on dell1.",
    "world_is": "The surprise-row gate requires the dell1 coordinate in the id (<CODE>-D1-W<n>-S<k>) and refuses the bare form. The rows were minted in the coordinate form; the order's literal id form is not usable on this fabric as written."
  }
]
```

## Rows filed by `0.9.0_WK_ADVI_BDPRCE~3` under `ADVI_BDPRCE.TO-BP-a-3.gap-603-of-1610` (denominator at its write: 5 rows, `ADVI_BDPRCE-D1-W3-S1..S5`)

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

## ADVI_BDPRCE-D1-W4-S1 -- The served client detail objects are dated 2026-10-09, one trading day behind the T-1 date 2026-10-12

```json
{
  "id": "ADVI_BDPRCE-D1-W4-S1",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~4",
  "surfaced_at": "2026-10-13T14:51:45Z",
  "one_line": "The served client detail objects in opal-data-49financial carry data_as_of 2026-10-09 in 24 of 26 sampled objects, while the task order's served T-1 date for a 2026-10-13 read is 2026-10-12; the shape-b premise at the served date therefore did not apply.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "opal-data-49financial advi/49financial/platinum/entities/clients/0/detail.json, VersionId VzILgp.KR2G8UFNcDbZLo3GcSkNmFnPC, LastModified 2026-10-13T05:39:43Z, data_as_of 2026-10-09 (read live, get-object, 2026-10-13T14:3xZ)",
      "range reads (bytes 0-300) of 26 detail objects sampled every 140th key of the served listing: data_as_of 2026-10-09 in 24, 2026-07-13 in 1, 2026-06-24 in 1",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~4/THREAD_TRACE.md section Premise notes"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 1a steps 1-2: the served T-1 object is the one the portal reads at the default T-1 date, and shape b is expected to be the normal case at the served T-1 date because the newest two daily price files carry no transaction_observed row.",
  "world_is": "The served detail objects carry the as-of date 2026-10-09, a day with transaction_observed rows in both silver/prices/2026-10-09.parquet and canonical_prices.parquet. The holding read for BP-a-4 is therefore a direct (shape a) candidate on 2026-10-09, not a chain on 2026-10-12. The key carries no date; the as-of date lives only in the body."
}
```

## ADVI_BDPRCE-D1-W4-S2 -- Untickered holdings in the served detail carry lot prices that match no canonical price row on the object's as-of date

```json
{
  "id": "ADVI_BDPRCE-D1-W4-S2",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~4",
  "surfaced_at": "2026-10-13T14:51:45Z",
  "one_line": "Of 586 untickered non-cash lots in 26 sampled client detail objects, 61 carry a current_price that equals no canonical_prices row for that asset on the as-of date; for VANGUARD MORNINGSTAR GROWTH ETF the value 83.78 matches no canonical row for the asset on any date.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~K1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "served detail objects read live (get-object, 26 keys from the served listing); lot fields account_id, asset_name, ticker, current_price; the object carries no price_quality or source field per lot",
      "silver/prices/canonical_prices.parquet version V7JNX.GmPYQcEVMywtMRnjk.fSdQl1WA read live: 12,649,131 rows; no row for VANGUARD MORNINGSTAR GROWTH ETF at 83.78 on any date; the 2026-10-09 row is 91.983333 (transaction_observed)",
      "account ref e49c43de6ac7 (sha256 prefix of the account id, held in the data directory, not in the checkout): lot 3 quantity 1.0, current_price 83.78, acquired 2026-10-09, ticker null; the same account carries lots 1 and 2 at 83.78",
      "B_01.holdings_lots.py:1333 and :2627 set current_price from the price table and the Schwab RPS override path at :2215-2288; the rps_injection and scoped_override price sources are not in the served lot"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 1a step 2: a served holding's price is a canonical row (transaction_observed, carry_forward or linear_interpolation) at the served date, with the anchor equal to the served price for shape b.",
  "world_is": "61 of 586 sampled untickered lots carry a price that no canonical row on the as-of date reproduces; 83.78 appears in no canonical row for the asset on any date. The lot object does not say which source priced the lot, so the price cannot be traced from the served object alone. Those lots are excluded from the thread candidates and are not counted as chain or direct candidates."
}
```

## ADVI_BDPRCE-D1-W4-S3 -- On 2026-10-09 the daily price file and the canonical file carry different transaction_observed prices for one asset, and the trace tool's stable pick serves the daily one

```json
{
  "id": "ADVI_BDPRCE-D1-W4-S3",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~4",
  "surfaced_at": "2026-10-13T14:51:45Z",
  "one_line": "VANGUARD MORNINGSTAR GROWTH ETF on 2026-10-09 has transaction_observed 92.216667 in silver/prices/2026-10-09.parquet and 91.983333 in canonical_prices.parquet; the served lot and the trade median follow the canonical value, and trace_price.py reports match false because its stable pick is the daily row.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/prices/2026-10-09.parquet version LhM3NuODjCiM_VUkEQiojppZtVu4Jf7y read live: one row for the asset, price 92.21666666666665, source transaction_observed",
      "silver/prices/canonical_prices.parquet version V7JNX.GmPYQcEVMywtMRnjk.fSdQl1WA read live: one row for the asset on 2026-10-09, price 91.98333333333333, source transaction_observed",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~4/TRACE_2026-10-09.json: served_rows (tie true), recomputed_price 91.98333333333333 from 123 rows, match false",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~4/THREAD_TRACE.json served_price 91.98333333333333 (the served lot value)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 1a step 3 and the trace README: trace_price.py reports the served row, its rule and a recompute with a match flag, and a same-date tie is reported as a tie that the tool does not resolve as B_01's choice.",
  "world_is": "The served lot carries the canonical value, so the tie was resolved toward canonical for this holding, while the tool's emulated stable pick names the daily file. The daily value 92.216667 is not the median of the same day's trades (91.983333). The record therefore cites the canonical row and states the tie in THREAD_TRACE.md."
}
```

## ADVI_BDPRCE-D1-W4-S4 -- The shape-counting census was a 26-object sample of 3,510 served client detail objects, not an enumeration

```json
{
  "id": "ADVI_BDPRCE-D1-W4-S4",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~4",
  "surfaced_at": "2026-10-13T14:51:45Z",
  "one_line": "Task order section 1b asks for the number of direct and chain candidates; the served home holds 3,510 client detail objects of about 4 MB each, so the counts (64 direct, 63 chain lots) come from a 26-object sample and are not a population count.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "listing of advi/49financial/platinum/entities/clients/ in opal-data-49financial: 18,230 objects, of which 3,510 are */detail.json (paged list-objects-v2, auto-paginated, counted client-side)",
      "client detail objects read in full: 26 (4.45 MB for object 0); 586 untickered non-cash lots in those 26",
      "THREAD_TRACE.md section Why this holding"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 1a step 2: state how many candidates there were of each shape.",
  "world_is": "A full census of untickered lots across 3,510 objects of about 4 MB was not run within the bound. The counts in THREAD_TRACE.json shape_counts are sample counts; the first fitting candidate in file order is the first fitting lot of the first sampled object, which the file-order rule accepts."
}
```

## ADVI_BDPRCE-D1-W4-S5 -- On 2026-10-09 the daily price file and the canonical file disagree on one untickered asset's source: carry_forward against transaction_observed

```json
{
  "id": "ADVI_BDPRCE-D1-W4-S5",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~4",
  "surfaced_at": "2026-10-13T15:10:00Z",
  "one_line": "EXXONMOBIL HOLDINGS CORP COM SHS on 2026-10-09 has carry_forward 162.155 in silver/prices/2026-10-09.parquet and transaction_observed 168.94 in canonical_prices.parquet; the served lot carries 168.94, the canonical value.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/prices/2026-10-09.parquet version LhM3NuODjCiM_VUkEQiojppZtVu4Jf7y read live by trace_price.py run_live: one row for the asset, price 162.155, source carry_forward",
      "silver/prices/canonical_prices.parquet version V7JNX.GmPYQcEVMywtMRnjk.fSdQl1WA read live by trace_canonical_only.py: one row for the asset on 2026-10-09, price 168.94, source transaction_observed",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~4/TRACE_2026-10-09_thread.json served_rows (tie true, stable pick the daily row); TRACE_2026-10-09_thread_canonical.json served_rows (canonical only, recompute 168.94)",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~3/GAP_ROWS.csv line 1608: 2026-10-09 EXXONMOBIL HOLDINGS CORP COM SHS 168.94 EQUAL"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 1a step 3: the trace names one served row per (asset, date) and the rule that produced it; the daily and canonical files agree on the source of a served row.",
  "world_is": "The two price objects carry different sources for the same asset and date (carry_forward against transaction_observed). The served lot follows the canonical row. The daily row is not reproduced by any trade on 2026-10-09 for this asset (the trade partition gives 168.94 for the asset, the daily value is 162.155)."
}
```

## ADVI_BDPRCE-D1-W4-S6 -- trace_price.py names the daily row as the carry-forward input of the wrong date and reports zero trades for a tie it does not resolve as the served lot does

```json
{
  "id": "ADVI_BDPRCE-D1-W4-S6",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~4",
  "surfaced_at": "2026-10-13T15:10:00Z",
  "one_line": "trace_price.py run_live on EXXONMOBIL HOLDINGS CORP COM SHS at 2026-10-09 takes the daily row (stable pick), reports carry_forward with trades 0, and names 2026-10-08 at 168.2864 as its carry-forward input; the daily value 162.155 equals the 2026-09-28 canonical row, not the 2026-10-08 row.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~4/TRACE_2026-10-09_thread.json: source carry_forward, trades 0, match false, rule_inputs carry_forward_input 2026-10-08 at 168.2864",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~3/GAP_ROWS.csv line 872 (2026-09-28 canonical 162.155 EQUAL) and line 1524 (2026-10-08 canonical 168.2864 EQUAL)",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~2/trace_price.py trace_asset_date:174-227: winner = same.iloc[0] (stable pick), trades read only when the winner is transaction_observed"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "trace_price.py README: for carry_forward the tool names the nearest earlier canonical row as the input, and a same-date tie is reported as a tie with a stable pick.",
  "world_is": "For this tie the stable pick is the daily row, whose carry-forward value matches a row two trading days earlier than the one the tool names. The tool's rule attribution for that daily row is therefore not the rule that produced it. The canonical row, which the lot carries, is traced only by a call with the canonical object alone (trace_canonical_only.py, which calls the instrument's trace_asset_date unchanged)."
}
```

## ADVI_BDPRCE-D1-W4-S7 -- The 2026-10-09 trade partition holds four rows of one transaction id for one asset

```json
{
  "id": "ADVI_BDPRCE-D1-W4-S7",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~4",
  "surfaced_at": "2026-10-13T15:10:00Z",
  "one_line": "silver/transactions/2026-10-09.parquet holds four rows with one transaction_id for EXXONMOBIL HOLDINGS CORP COM SHS, all at the same unit value 168.94; the rule keeps repeats, so the trade count of the thread is four rows and one trade.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/transactions/2026-10-09.parquet read live by trace_canonical_only.py: rows_used 4, distinct_trade_ids 1, median_distinct 168.94, recomputed_price 168.94 (TRACE_2026-10-09_thread_canonical.json)",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~2/TRACE_README.md: the daily path does not de-duplicate on transaction_id"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 1b: trade_ids are the transaction ids behind the price (by trade id), and the recompute is the median over them.",
  "world_is": "The median is unaffected here (all four rows carry 168.94), but the thread rests on one distinct trade repeated four times. Whether the duplicate rows are a writer effect or a source effect is not measured."
}
```

## ADVI_BDPRCE-D1-W4-S8 -- A served lot's market value does not equal its quantity times its current price

```json
{
  "id": "ADVI_BDPRCE-D1-W4-S8",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~4",
  "surfaced_at": "2026-10-13T15:10:00Z",
  "one_line": "Two open lots of EXXONMOBIL HOLDINGS CORP COM SHS in one client object (account ref 420deb1a5526) carry quantity 73, current_price 168.94 and market_value 5000.7866; the product of quantity and price is about 12332.6, and the market value implies a unit value of about 68.50.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~K1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "opal-data-49financial advi/49financial/platinum/entities/clients/<normal key, sample position 58>/detail.json at VersionId ZCjWpzPR1n2uZl849onevhS.pIvSQhVA, read live by the BP-a-4 sample script (lots 2 and 3 of the asset; quantity 73.0, current_price 168.94, market_value 5000.7866 each)",
      "the same object, all 110 open lots read live at the same VersionId: 103 satisfy quantity times current_price equals market_value within 1 percent; 7 do not (the two Exxon lots and five lots of other assets)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The served lot carries current_price, quantity and market_value for one holding; the market value is the quantity times the current price.",
  "world_is": "Measured on one client object: 7 of 110 lots break the identity, two of them the Exxon lots. The scope across the served home is not measured (outside the cell's bounds). For those lots a valuation read from market_value would differ from one read from quantity times price."
}
```

## ADVI_BDPRCE-D1-W4-S9 -- A holding with a null served ticker and no ticker-lookup entry is a listed-name security, so the operational no-public-ticker rule does not separate it from a listed holding

```json
{
  "id": "ADVI_BDPRCE-D1-W4-S9",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~4",
  "surfaced_at": "2026-10-13T15:10:00Z",
  "one_line": "The task order's no-public-ticker rule (served ticker null OR no config/ticker_lookup.json entry) selects EXXONMOBIL HOLDINGS CORP COM SHS as the first fitting holding; the name reads as a listed common stock, and the record cannot tell from the served object whether it has a public ticker.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "config/ticker_lookup.json of opal-data-bd (VersionId PD_UeAZIKoYt0z0Rj9NIQyjqRGMKXYPq, 10,206 entries): exact-name match for the asset returns no entry",
      "served lot ticker null in the same object (BP-a-4 sample, sample position 58)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 1a step 2: a holding with NO public ticker, where the served ticker is null, empty or UNKNOWN, or the asset has no entry in config/ticker_lookup.json.",
  "world_is": "The operational rule is satisfied and the outcome sentence (a security with no public ticker) is not established by the rule. The first fitting holding is a common-stock name. The thread record states the rule used and does not claim the asset has no listing."
}
```

## ADVI_BDPRCE-D1-W4-S10 -- Some served client detail objects carry a data_as_of months before the served as-of date

```json
{
  "id": "ADVI_BDPRCE-D1-W4-S10",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~4",
  "surfaced_at": "2026-10-13T15:10:00Z",
  "one_line": "Of 120 sampled normal client detail objects in advi/49financial/platinum/entities/clients/, nine carry data_as_of before 2026-10-09 (six at 2026-04-02, one each at 2026-06-24, 2026-07-20 and 2026-10-07); none of the nine holds an untickered holding.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "opal-data-49financial client detail objects read live by the BP-a-4 sample script: 120 normal objects (stride sample of 3,509 normal detail.json keys); data_as_of counts 2026-10-09: 111, 2026-04-02: 6, 2026-07-20: 1, 2026-06-24: 1, 2026-10-07: 1",
      "org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md ADVI_BDPRCE-D1-W4-S1 (served detail dated 2026-10-09, not T-1)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order section 1a step 1: the served T-1 object is the one the portal reads at the default T-1 date, and it carries the holdings for the served date.",
  "world_is": "The served home holds client objects whose as-of date is months old, alongside objects dated 2026-10-09. The served T-1 object is therefore not uniform across client objects; the thread uses each object's own data_as_of."
}
```
