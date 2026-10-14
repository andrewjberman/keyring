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

## ADVI_BDPRCE-D1-W8-S1 -- The output contract enumerates followed_source as canonical or daily, and no value in that set holds when neither candidate equals the served price

```json
{
  "id": "ADVI_BDPRCE-D1-W8-S1",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~8",
  "surfaced_at": "2026-10-13T19:49:02Z",
  "one_line": "Task order 1b enumerates followed_source as canonical or daily; when neither same-date candidate equals the served price, no value in that set is true, so the instrument emits followed_source null with follows_served false and traces no row.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "trace_price_v2.py@80be485749 function trace_followed: the followed-is-None branch sets followed_source None, followed_price None, follows_served False, trade_ids [] and writes the candidates into served_rows without picking one",
      "trace_price_v2.py@80be485749 self-test arm 4 (served 170.0 against daily 162.155 and canonical 168.94): follows_served False, followed_source None; TRACE2 SELFTEST: OK 7 arms",
      "org/missions/D8/ADVI/ADVI_BDPRCE/task-orders/ADVI_BDPRCE.TO-BP-b-4.trace-follows-served.md section 1b: output keys followed_source (canonical or daily); 'if neither equals it, report follows_served: false and say so'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order 1b: the output key followed_source is canonical or daily, and if neither candidate row equals the served price the instrument reports follows_served false and says so, never picking one silently.",
  "world_is": "Both clauses are met only by a null followed_source, which the enumerated set does not name. The instrument writes null and follows_served false, lists both candidates in served_rows with followed false, and traces no rule. The task order does not say which value followed_source takes in that case."
}
```

## ADVI_BDPRCE-D1-W8-S2 -- The lot-object usage names no date, so the instrument takes the date and the served price from the served object itself

```json
{
  "id": "ADVI_BDPRCE-D1-W8-S2",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~8",
  "surfaced_at": "2026-10-13T19:49:02Z",
  "one_line": "The task order's --lot-object form takes no date; the instrument reads the date from the served object's data_as_of and the served price from its one current_price for the asset, and records the client key only as a SHA-256 prefix.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "TRACE2_PROBE.json@80be485749 served_source: kind lot_object, date_source 'served object data_as_of', data_as_of 2026-10-09, lot_rows_for_asset 2, key_sha256 3a1adf541436e1d4 (prefix only); the client key is not in the record",
      "served object read by get_object at VersionId ZCjWpzPR1n2uZl849onevhS.pIvSQhVA (bucket opal-data-49financial, 51,343 bytes): data_as_of 2026-10-09; the asset's open_lots carry one distinct current_price, 168.94",
      "task order 1b usage line: --lot-object <bucket>/<key>@<VersionId> --asset <name> [--out]; section 2 bound 2: no client name, account number or advisor name is printed"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order 1b: --lot-object <bucket>/<key>@<VersionId> --asset <name> [--out] with no date argument; section 2 bound 2: no client name, account number or advisor name is printed.",
  "world_is": "The served object states its own as-of date and carries one current_price per lot, so the date and price are read from the object. The lot key carries a client identifier, so the record holds a SHA-256 prefix of it. The date source is a choice the task order did not name, and the record names it in served_source.date_source."
}
```

## ADVI_BDPRCE-D1-W7-S1 -- The third mapping-gap test cannot run: silver/historical_prices.parquet is keyed by ticker and has no asset_name column

```json
{
  "id": "ADVI_BDPRCE-D1-W7-S1",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~7",
  "surfaced_at": "2026-10-13T19:55:52Z",
  "one_line": "The task order's mapping-gap test (a name that has a ticker in silver/historical_prices.parquet) cannot be run: that table has a ticker column and no asset_name column.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "opal-data-bd silver/historical_prices.parquet downloaded 2026-10-13 and schema read with pyarrow: columns date, ticker, close, fetch_date, source; 5,885,915 rows, 3,628 distinct tickers; no asset_name column",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/CENSUS.json@e7588a0117 listed_untickered.condition3 records the test as UNEVALUABLE",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/census_diagnostics.txt@e7588a0117 NAMES line: untickered names in ticker_lookup 1, in canonical rows carrying a ticker 0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order BP-b-3 section 1b: listed_untickered covers assets 'whose name has a ticker in historical_prices.parquet'; section 1a names silver/historical_prices.parquet (ticker column) as a ticker source.",
  "world_is": "The table is keyed by ticker, not by name, so the name-to-ticker test has no column to run against. The listed count rests on config/ticker_lookup.json and the canonical table's own ticker column. Those two sources list 1 untickered asset (1 lot). The third condition is recorded as UNEVALUABLE, not as zero."
}
```

## ADVI_BDPRCE-D1-W7-S2 -- acct_z client keys embed an account number, so the extract and the committed sample carry them hashed

```json
{
  "id": "ADVI_BDPRCE-D1-W7-S2",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~7",
  "surfaced_at": "2026-10-13T19:55:52Z",
  "one_line": "The 138 acct_z client objects are keyed by acct_z followed by ten digits; the extract's object_key and the committed sample therefore carry them as acct_z#<sha12>, and the sample hashes every client key.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "listing of advi/49financial/platinum/entities/clients/ in opal-data-49financial (read 2026-10-13): 138 detail.json keys with the acct_z prefix; the suffix is ten digits (shape counted, values not printed)",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/scripts/census_bp_b3.py@e7588a0117 masked_path and sample_path: acct_z suffix written as sha12, every sample key as obj#sha12",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/CENSUS.md@e7588a0117 Privacy section states the re-read method (list the prefix, match the hash)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order BP-b-3 section 1c: the extract carries object_key per lot and a 200-row sample is committed as lot_extract_sample.csv; section 2.2: no account number is printed or committed anywhere, and raw client keys are not printed.",
  "world_is": "A raw acct_z key is an account number, so the extract (outside the checkout) and the committed sample cannot carry it as written. The extract holds acct_z#<sha12>; the sample holds obj#<sha12> for every client key. The next cell therefore cannot re-read an acct_z object from the extract key alone and must list the prefix and match the hash. No raw account key is in any committed file."
}
```

## ADVI_BDPRCE-D1-W7-S3 -- The 26-object sample understates the off-canonical rate: 1,859 of 5,121 non-cash untickered lots across the home, against 61 of 586 in the sample

```json
{
  "id": "ADVI_BDPRCE-D1-W7-S3",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~7",
  "surfaced_at": "2026-10-13T19:55:52Z",
  "one_line": "Across all 3,510 client detail objects, 1,859 of 5,121 non-cash untickered lots (36.3%) carry a price that matches no canonical row on the as-of date; the 26-object sample gave 61 of 586 (10.4%).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/CENSUS.json@e7588a0117 classes: PRICED_OFF_NO_CANONICAL 1859, NOT_UNTICKERED 192228, untickered_lots 6067, objects_read 3510 of 3510",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/census_diagnostics.txt@e7588a0117 CASH_HEURISTIC line: cash-like lots 946 with 0 off; non-cash lots 5121 with 1859 off",
      "ADVI_BDPRCE-D1-W4-S2 (the sample of 586 untickered non-cash lots in 26 objects, 61 off) in this channel file"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order BP-b-3 cell: a sample of 586 untickered lots from 26 client objects found 61 whose served current_price matches no canonical row on the as-of date; the census is ordered to extend that sample to every lot.",
  "world_is": "The full census gives a higher off rate than the sample, and the sample is not representative of the home: 942 objects carry untickered lots, and the off lots sit in z0 (1,792) and catch_all (67) objects. Any count or dollar effect taken from the 26-object sample describes that sample only. The cash rule is a name regex (diagnostic only), not a class."
}
```

## ADVI_BDPRCE-D1-W7-S4 -- Served lots break market_value = quantity x current_price on 21,614 of 198,261 checked lots, 16,297 of them with market_value 0

```json
{
  "id": "ADVI_BDPRCE-D1-W7-S4",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~7",
  "surfaced_at": "2026-10-13T19:55:52Z",
  "one_line": "The market-value identity fails on 21,614 of 198,261 checked lots across the home, 16,297 of them with market_value 0 and nonzero quantity, where ADVI_BDPRCE-D1-W4-S8 read one object.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~K1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/CENSUS.json@e7588a0117 market_value_identity: lots_checked 198261, lots_off_quantity_times_price 21614, lots_off_over_1pct 21394, tolerance max(0.01, 1e-6*abs(market_value))",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/census_diagnostics.txt@e7588a0117 MV_IDENTITY lines: broken_by_class NOT_UNTICKERED 20520, broken_with_market_value_zero 16297, ratio quantiles 1.02 / 1.60 / 4.96 / 19.7 / 228",
      "ADVI_BDPRCE-D1-W4-S8 in this channel file: the identity read on one client object (7 of 110 lots broken)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order BP-b-3 section 1c asks for the count of lots off quantity x current_price; ADVI_BDPRCE-D1-W4-S8 records the served contract as 'the market value is the quantity times the current price'.",
  "world_is": "The identity holds on 89.1% of checked lots and fails on the rest. The breaks are not one multiplier (median ratio of quantity x price to market value 4.96), and 16,297 breaks carry market_value exactly 0 while quantity is nonzero. 20,520 breaks sit on NOT_UNTICKERED lots. A valuation read from market_value differs from one read from quantity x price on these lots; the census does not say which field is right."
}
```

## ADVI_BDPRCE-D1-W5-S1 -- R1 reads no price for EXXONMOBIL HOLDINGS CORP COM SHS on 2026-10-09: its only rows that day are Transfer In

```json
{
  "id": "ADVI_BDPRCE-D1-W5-S1",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~5",
  "surfaced_at": "2026-10-13T19:56:27Z",
  "one_line": "R1 reads no price for EXXONMOBIL HOLDINGS CORP COM SHS on 2026-10-09: its only rows that day are Transfer In, so variants A and B are both absent and the 168.94 the task order expected is a non-trade row.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/transactions/2026-10-09.parquet in opal-data-bd: local MD5 3418b4f2cd45652b4c4b02c0420b769d equals the S3 ETag; 4 rows dated 2026-10-09 for this asset, one transaction_id, transaction_type Transfer In, price 168.94",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~5/RULE_PROBE.json@b8b710c884 (named row EXXON 2026-10-09: status absent_under_both; carry_forward 168.29 observed 2026-10-08)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order BP-b-1 section 1e: include EXXONMOBIL HOLDINGS CORP COM SHS on 2026-10-09 in the probe assets (the round-1 thread asset: expect 168.94), under R1 clause 1 which excludes every non-trade row.",
  "world_is": "The 168.94 on 2026-10-09 is a Transfer In row, which clause 1 excludes. R1 finds no Buy or Sale for the asset that day, so it is absent, and clause 5 carries forward 168.29 observed 2026-10-08 (a Sale)."
}
```

## ADVI_BDPRCE-D1-W5-S2 -- R1 variant A reads no price for BLACKROCK INC COM on 2026-09-22: no Buy or Sale that day; only variant B reads a price

```json
{
  "id": "ADVI_BDPRCE-D1-W5-S2",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~5",
  "surfaced_at": "2026-10-13T19:56:27Z",
  "one_line": "R1 variant A reads no price for BLACKROCK INC COM on 2026-09-22 (no Buy or Sale that day); only the sensitivity variant B reads a price, 1074.9259, from Dividend Reinvestment rows.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/transactions/2026-09-22.parquet in opal-data-bd: local MD5 e01c1d1a9cad600170736e19f122268f equals the S3 ETag; the asset's rows dated 2026-09-22 are Dividend (33 rows, 11 ids) and Dividend Reinvestment (15 rows, 4 ids), no Buy or Sale",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~5/RULE_PROBE.json@b8b710c884 (named row BLACKROCK 2026-09-22: status absent_under_A_priced_under_B, price_variant_b 1074.9259)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order BP-b-1 section 1e: BLACKROCK INC COM on 2026-09-22 is in the probe assets; the T1 median read 1.0 because cash rows dominated, and R1 must read a trade price.",
  "world_is": "That date holds no Buy or Sale row for the asset. Variant A (clause 1, buys and sells only) is absent. Variant B reads 1074.9259, the median of 4 Dividend Reinvestment ids, which clause 1 names as a reinvestment cash leg. Under the ruling as written, R1 cannot read a trade price for this asset that day. Choosing A or B is the CTO's call; BP-b-2 replays the served rows."
}
```

## ADVI_BDPRCE-D1-W5-S3 -- The silver transactions partition for 2026-10-12, the T-1 date for 2026-10-13, exists with zero rows

```json
{
  "id": "ADVI_BDPRCE-D1-W5-S3",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~5",
  "surfaced_at": "2026-10-13T19:56:27Z",
  "one_line": "The silver transactions partition for 2026-10-12, the T-1 date for 2026-10-13, exists with zero rows, so R1 prices no asset for that date.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/transactions/2026-10-12.parquet in opal-data-bd: LastModified 2026-10-12T00:17:25+00:00, 74 columns, row count 0 (parquet metadata read via get-object and pyarrow)",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~5/RULE_PROBE.json@b8b710c884 (per_date 2026-10-12: rows_on_date 0)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order BP-b-1 section 1e: run the module over REAL partitions silver/transactions/<date>.parquet for the named dates and a third of choice; the partitions are the data the probe reads.",
  "world_is": "silver/transactions/2026-10-12.parquet exists with zero rows. The probe reads it, and R1 yields no price for any asset on 2026-10-12.",
  "notes": "Cause of empty or lagging daily files is the BP-b-5 cell (cause of missing daily files). Not investigated in this cell."
}
```

## ADVI_BDPRCE-D1-W5-S4 -- Five Buy rows on 2026-09-22 carry no asset_name, so R1 cannot price an asset from them

```json
{
  "id": "ADVI_BDPRCE-D1-W5-S4",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~5",
  "surfaced_at": "2026-10-13T19:56:27Z",
  "one_line": "Five Buy rows on 2026-09-22 carry no asset_name; R1 cannot price an asset from them, so it counts them under no_asset_excluded and prices nothing.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/transactions/2026-09-22.parquet in opal-data-bd: 5 rows with null asset_name, all transaction_type Buy, one distinct transaction_id, price 1.0",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~5/RULE_PROBE.json@b8b710c884 (per_date 2026-09-22: no_asset_excluded 5)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Ruling clause 4 and the module contract key the price per asset (asset_name); the task order gives no rule for a trade row whose asset_name is missing.",
  "world_is": "Five Buy rows carry no asset name. The module excludes them from the per-asset result and counts them in the census, so the decision is visible and not silent."
}
```

## ADVI_BDPRCE-D1-W5-S5 -- The 2026-10-09 partition carries 10 rows dated 2026-10-08, so a per-date read of the 2026-10-08 file alone would miss them

```json
{
  "id": "ADVI_BDPRCE-D1-W5-S5",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~5",
  "surfaced_at": "2026-10-13T19:56:27Z",
  "one_line": "The 2026-10-09 partition carries 10 rows dated 2026-10-08; a per-date read of the 2026-10-08 file alone would miss them, so the probe reads the union of partitions and lets trade_date decide.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/transactions/2026-10-09.parquet in opal-data-bd: 10 rows with trade_date 2026-10-08 beside 6,264 rows dated 2026-10-09; the 2026-10-08 file has 84,459 rows dated 2026-10-08 and no transaction_id shared with the 2026-10-09 file",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~5/RULE_PROBE.json@b8b710c884 (per_date 2026-10-08: rows_on_date_by_file includes the 2026-10-09 file)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Ruling clause 6 (DEC-6): a row belongs to the target date when its trade_date equals it, whichever daily partition file carries it; the task order names the partitions to run the module over.",
  "world_is": "Rows for one target date sit in a later file. The probe therefore reads the union of the four partitions and the date key decides. Reading only the file named for the date would drop them."
}
```

## ADVI_BDPRCE-D1-W10-S1 -- The S3 template is not byte-equal to the repo copy: S3 is CRLF at 14,419 bytes, the repo blob is LF at 13,920 bytes; they are equal after CRLF normalisation and as parsed JSON.

```json
{
  "id": "ADVI_BDPRCE-D1-W10-S1",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~10",
  "surfaced_at": "2026-10-13T19:56:21Z",
  "one_line": "The S3 template is not byte-equal to the repo copy: S3 is CRLF at 14,419 bytes, the repo blob is LF at 13,920 bytes; they are equal after CRLF normalisation and as parsed JSON.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3://opal-data-bd/code/bronze/templates/unrealized.json VersionId VgzqQbd.3F3sAlllb6SWsjKZ2XvXgAfE: head-object and get-object by VersionId, 2026-10-13, ContentLength 14419, 499 CRLF and 0 bare LF; copy at C:/dev/wk-bdprce-r2-10-data/s3_unrealized_template.json (outside the checkout)",
      "git cat-file -s HEAD:data/black_diamond/scripts/bronze/templates/unrealized.json = 13920, 499 bare LF and 0 CRLF; S3 bytes with CRLF replaced by LF equal the repo blob (checked by .scratch/make_template.py, 2026-10-13)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order BP-b-6 section 1a(1) and its round-1 measurement: the S3 template equals the repo copy, 14,419 bytes, VersionId VgzqQbd.3F3sAlllb6SWsjKZ2XvXgAfE.",
  "world_is": "The S3 copy still carries VersionId VgzqQbd.3F3sAlllb6SWsjKZ2XvXgAfE at 14,419 bytes, but the repo copy at HEAD is 13,920 bytes with LF line endings. The two differ in line endings only and are equal as parsed JSON. The patched template is built from the S3 bytes."
}
```

## ADVI_BDPRCE-D1-W10-S2 -- The mandated lot key (account_id, asset_id, open_date, unit_cost) folds 15,553 export rows on the recorded export; in most colliding groups the rows differ on Relationship ID.

```json
{
  "id": "ADVI_BDPRCE-D1-W10-S2",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~10",
  "surfaced_at": "2026-10-13T19:56:21Z",
  "one_line": "The mandated lot key (account_id, asset_id, open_date, unit_cost) folds 15,553 export rows on the recorded export; in most colliding groups the rows differ on Relationship ID.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~K1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "UNREALIZED_DAILY_2026-10-09.xlsx (opal-data-bd forwardfill_v2/unrealized/, VersionId Wf2Pct313A.w7y1GpuSf2f7FfiKUVats, sha256 5700843f9e661364910a5bbb9d9d4b60521775922539f47b066a10d80039ef5b) read by get-object 2026-10-13: 500,000 rows, 484,447 distinct lot keys, 14,696 colliding groups holding 30,418 rows (.scratch/lotstats.py)",
      "same read: colliding groups where Relationship ID differs 14,514 of 14,696; Market Value differs 187; Inherited Date differs 1; Asset Name differs 0; Open Date null in 7,384 rows"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order BP-b-6 section 1a(2)(b): de-duplicate on the LOT (account_id, asset_id, open_date, unit_cost), never on the position, so each tax lot survives as a row.",
  "world_is": "On the recorded export the mandated key is not one row per tax lot: 15,553 rows fold into 14,696 groups, mostly rows that differ on Relationship ID. The key ignores Relationship ID and Inherited Date and treats a null Open Date as a value. Applied as written, the lot table holds 484,447 rows where the export holds 500,000. Whether the 15,553 folded rows are distinct lots is not determined by this fixture. Armed for the apply: the apply amendment's author decides the key before any template switch."
}
```

## ADVI_BDPRCE-D1-W10-S3 -- The recorded unrealized export holds exactly 500,000 data rows, a round count; the fixture cannot show that the export is complete.

```json
{
  "id": "ADVI_BDPRCE-D1-W10-S3",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~10",
  "surfaced_at": "2026-10-13T19:56:21Z",
  "one_line": "The recorded unrealized export holds exactly 500,000 data rows, a round count; the fixture cannot show that the export is complete.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "UNREALIZED_DAILY_2026-10-09.xlsx Sheet1 read by pandas 2026-10-13: shape (500000, 15); 15 columns, none of them Units or Cost Basis",
      "data/black_diamond/scripts/silver/merge-daily-incremental.py:1145 at HEAD: 'Unrealized is a daily SNAPSHOT -- each file is the full picture of open positions.'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Silver step docstring, data/black_diamond/scripts/silver/merge-daily-incremental.py:1145 at HEAD: each unrealized file is the full picture of open positions.",
  "world_is": "The export holds exactly 500,000 rows, which matches a row cap. The fixture cannot establish whether the export is complete. The read of :1138-1215 shows no row-count check in the step. The premise binds the legacy table and the lot table alike."
}
```

## ADVI_BDPRCE-D1-W9-S1 -- The round-1 premise that an EventBridge rule and cron drive bd-price-update does not hold: it is invoked by the silver merge on an S3 sentinel

```json
{
  "id": "ADVI_BDPRCE-D1-W9-S1",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~9",
  "surfaced_at": "2026-10-13T20:15:48Z",
  "one_line": "bd-price-update has no EventBridge rule and no cron; no rule targets it in the live account. It runs only when bd-silver-merge invokes it, and bd-silver-merge runs only on the bronze sentinel S3 event.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws events list-targets-by-rule --rule bd-price-update (us-east-1): ResourceNotFoundException, no rule of that name; of the 45 bd-related rules listed, none targets the function bd-price-update",
      "infra/aws/terraform/bd-pipeline/s3-notifications.tf:68-73 at HEAD 6f20fe54c6: BronzeCompleteSilverMerge, prefix bronze/, suffix _BRONZE_COMPLETE.json, function bd-silver-merge; live get-bucket-notification-configuration (scratch copy, 2026-10-13T20:0xZ) matches",
      "data/black_diamond/scripts/silver/merge-daily-incremental.py:675-707 invoke_price_update, InvocationType Event, payload date = max processed partition date"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order BP-b-5 section 1 item 1: the daily price Lambda bd-price-update writes the daily file, and the question asks for the Lambda's EventBridge rule and its cron.",
  "world_is": "There is no cron for the daily price file. The file is written only after a complete bronze sentinel, which bd-49f-runner writes. The schedule question resolves to the runner's chain, not to a price-update schedule. The cause record follows the real trigger chain."
}
```

## ADVI_BDPRCE-D1-W9-S2 -- The pre-2026-10-07 bd-49f-runner printed "OK: bronze sentinel emitted" after the shared module had withheld the sentinel, so its self-report and S3 disagree

```json
{
  "id": "ADVI_BDPRCE-D1-W9-S2",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~9",
  "surfaced_at": "2026-10-13T20:15:48Z",
  "one_line": "On 2026-10-05 and 2026-10-06 the runner logged WARN bronze sentinel NOT emitted and then OK bronze sentinel emitted; S3 holds no bronze/<date>/_BRONZE_COMPLETE.json for either date, so the OK line was false and the silver chain never fired.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws logs filter-log-events on /aws/lambda/bd-49f-runner, 2026-10-05T00:00-01:00Z: 'WARN: bronze sentinel NOT emitted -- 1 object(s) present but NOT content-complete' then 'OK: bronze sentinel emitted for 2026-10-05'; the same pattern on 2026-10-06 (request 6e3026c2-3392-4a92-89cc-0b5d8e7f8653)",
      "aws s3api head-object bronze/2026-10-05/_BRONZE_COMPLETE.json: 404; list-object-versions --prefix bronze/2026-10-05/: zero versions, zero delete markers; control bronze/2026-10-04/_BRONZE_COMPLETE.json present (2026-10-04T00:13:34Z)",
      "git show 3709ae40d6^:infra/aws/lambda/bd-pipeline/bd-49f-runner/lambda_function.py lines 206-207 print the OK line after mod.emit_bronze_sentinel with no completeness check; the deployed package before 2026-10-07T00:50:44Z was that revision"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "bd-49f-runner at HEAD (from commit 3709ae40d6): the OK line prints only after a head_object reads the sentinel key back, and a withheld sentinel is logged as withheld.",
  "world_is": "The defect is fixed in the deployed code from 2026-10-07 (deployed md5 968b33e2 equals the repo file). Six run dates before that fix have no sentinel and no daily price file. Nothing in the current code re-emits a sentinel for a past run date, so the gaps persist until a later cell backfills them."
}
```

## ADVI_BDPRCE-D1-W9-S3 -- The served client detail data_as_of equals the newest date of gold/timeseries/account_performance (2026-10-09), and the producer has no T-1 rule, so the one-day lag is not by design

```json
{
  "id": "ADVI_BDPRCE-D1-W9-S3",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~9",
  "surfaced_at": "2026-10-13T20:15:48Z",
  "one_line": "data_as_of in the served client detail objects is the input's max date, which stops at 2026-10-09 with no rows for 2026-10-10 or 10-11. The producer applies no trading-day offset, so the lag is inherited from the ledger, not a documented T-1 rule.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/black_diamond/scripts/gold/D_02.advisor_client_detail.py:2874 latest_date = acct['date'].max(); :2937 'data_as_of': latest_date.strftime; acct loaded from ACCOUNT_PERFORMANCE at :473-507 at HEAD 6f20fe54c6",
      "pyarrow read of opal-data-bd gold/timeseries/account_performance.parquet (column date only): rows 7,871,793, max_date 2026-10-09, 2,473 distinct dates; weekend rows 2026-09-19 and 2026-09-20 present, none for 2026-10-10 or 2026-10-11",
      "census of opal-data-49financial advi/49financial/platinum/entities/clients/ (3,510 detail.json; counts only): data_as_of 2026-10-09 on 3,267, older on 243"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order BP-b-5 section 1a item 2: the lag is by design (a documented T-1 rule) or a defect, stated from the code and lib/trading_calendar.py.",
  "world_is": "lib/trading_calendar.py gives T-1 = 2026-10-12 and expected_last_trading_day(2026-10-13) = 2026-10-13. The producer does not call it. Why account_performance stops at 2026-10-09 (the C_03 ledger upstream) is not established by this cell."
}
```

## ADVI_BDPRCE-D1-W9-S4 -- Two instrument traps: a rail denial on a repo grep blocked the whole Bash call, and a get-object to /dev/stdout returned empty bodies with no error

```json
{
  "id": "ADVI_BDPRCE-D1-W9-S4",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~9",
  "surfaced_at": "2026-10-13T20:15:48Z",
  "one_line": "A recursive repo grep under infra/ was denied by the comp-rail hook (F1 blind recursive search), and the denial blocked the whole Bash call, not only the search; a get-object to /dev/stdout returned empty bodies with no error.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "PreToolUse denial deny_id 20261013T194328Z-1f13f679 on a Bash call that also carried a live aws s3api get-bucket-notification-configuration; the AWS read did not run and the call returned the rail message only",
      "aws s3api get-object --version-id ... /dev/stdout returned empty bodies for 21 versions (2026-09-13 to 2026-10-08) under Git Bash; the same reads to a file under C:/dev/wk-bdprce-r2-9-data/ returned the bodies"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The task order bounds: a raw S3 listing the rail denies is re-run with a trailing '# rail-checked: <why>' comment, and a read that cannot finish reports claim absent for what was not read.",
  "world_is": "The denial named no rail-checked override path for a repo grep, and its remainder line ran nothing. A read to /dev/stdout under Git Bash is an empty-body hazard that looks like a clean empty result. Every read in this cell was re-run to a file and printed from there."
}
```

## ADVI_BDPRCE-D1-W12-S1 -- The served 2026-10-09 price of ALLSPRING CORE BOND CIT CLASS E2 is written by a linear_interpolation row, which R1 clause 5 bans as an output source

```json
{
  "id": "ADVI_BDPRCE-D1-W12-S1",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~12",
  "surfaced_at": "2026-10-13T20:34:54Z",
  "one_line": "The served 2026-10-09 price of ALLSPRING CORE BOND CIT CLASS E2 is written by a linear_interpolation row, which R1 clause 5 bans as an output source; the value equals R1's carry-forward.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~K1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~12/TRACE_BP-b-8.json: followed canonical_row source linear_interpolation price 10.3525; daily_row source carry_forward price 10.3525",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~12/recompute_R1_BP-b-8.py output: R1 carry-forward 10.3525 observed 2026-10-02 from distinct trades 742108391 and 742108404",
      "org/missions/D8/ADVI/ADVI_BDPRCE/ledger/CTO_RULING_R1_THE_PRICE_RULE_20261013.md clause 5: interpolation is banned; no trade on the date gives the last observed price carried with its observation date"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CTO ruling R1 clause 5 (ledger/CTO_RULING_R1_THE_PRICE_RULE_20261013.md): interpolation is banned; with no trade on the date, the last observed price is carried WITH its observation date.",
  "world_is": "The served price for the holding on 2026-10-09 has a canonical row whose source is linear_interpolation (flat at 10.3525) and a daily partition row whose source is carry_forward (10.3525). The value agrees with R1's carry from the 2026-10-02 trades; the writing rule in the served row is the banned interpolation. The writer of this specific canonical row is not identified here; the trace names the bd_price_update.py backfill path as the interpolation source."
}
```

## ADVI_BDPRCE-D1-W12-S2 -- No Buy or Sale row prices the private-pool names on 2026-10-09, so the natural private-fund exemplar falls away at the R1 condition

```json
{
  "id": "ADVI_BDPRCE-D1-W12-S2",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~12",
  "surfaced_at": "2026-10-13T20:34:54Z",
  "one_line": "No Buy or Sale row prices the private-pool names on 2026-10-09; their 2026 rows are Transfer In, Valuation, Interest and Dividend, so the natural private-fund exemplar falls away at R1.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-bdprce-r2-12-data/bp_b8_scan_rows.csv (silver/transactions 2026-01-01..2026-10-10, five columns, asset rows only): SHAW PARK PRIVATE MARKET S 2021 LP 0 Buy/Sale rows; KKR FS INCOME TRUST CLASS I 0; KKR PRIVATE EQUITY CONGLOMERATE CLASS U 0; BLACKSTONE REIT INCOME TRUST CLASS I 0; CNL STRATEGIC CAPITAL CLASS A 0; AQR TA DELPHI PLUS FUND LLC 0",
      "R1 variant A on 2026-10-09 over partitions 2026-10-08..10-10 (bp_b8_shapeb / bp_b8_shapea probes): 229 of 1,861 finalist object-asset groups priced on the date, 8 equal to served, 221 unequal; 0 of the unlisted groups priced on the date"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-b-8 section 1a(5): a candidate counts only when R1 variant A prices it from Buy or Sale rows on the date (shape a) or its carry-forward is R1's last observed trade price (shape b); the natural exemplar is a private fund, structured note or model sleeve.",
  "world_is": "The private-pool holdings in the lot extract carry no Buy or Sale row in the 2026 window; their served prices come from Transfer In, Valuation or interpolated canonical rows that R1 excludes or bans. Of the 371 unlisted finalist groups (198 names), 338 have no Buy or Sale in the window, so R1 cannot price them from the 2026 window. The chosen holding is a collective investment trust with Buy trades in the window; of the 33 unlisted names with 2026 Buy or Sale rows, 20 groups have an R1 carry equal to the served price and 13 do not."
}
```

## ADVI_BDPRCE-D1-W12-S3 -- The no-ticker-in-any-source test also passes public funds and ETFs, and the dimension's symbol column holds CUSIPs and BD identifiers, not tickers

```json
{
  "id": "ADVI_BDPRCE-D1-W12-S3",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~12",
  "surfaced_at": "2026-10-13T20:34:54Z",
  "one_line": "The no-ticker-in-any-source test also passes public funds and ETFs, and the dimension symbol column holds CUSIPs and BD identifiers rather than tickers, so the test alone does not establish an unlisted holding.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-bdprce-r2-12-data/bp_b8_sources_rows.json: AMERICAN FUNDS AMERICAN MUTUAL F2, AMERICAN FUNDS EUPAC F2, DIMENSIONAL US VECTOR EQUITY ETF, FLEXSHARES STOXX GLOBAL BROAD INFRASTRUCTURE INDEX FUND, TORTOISE GLOBAL WATER FUND: lookup null, canonical ticker empty, YF/OPAL/TC absent, dimension ticker empty",
      "C:/dev/wk-bdprce-r2-12-data/bp_b8_sources_rows.json: dimension symbol for ALLSPRING CORE BOND CIT CLASS E2 is 01988T753 (a CUSIP), dimension ticker NaN"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-b-8 section 1a(2): the asset is truly unlisted only if NONE of the named sources gives a ticker; the exemplar is a security with no public ticker.",
  "world_is": "Named public mutual-fund share classes and listed ETFs return no ticker from any of the named sources, so the source test separates them from private instruments only by the asset's name and kind, which the brief asks the analyst to judge. The dimension's symbol column carries CUSIPs, BD identifiers and Schwab identifiers, not tickers. The chosen holding's kind is judged from its name (CIT) and its dimension row, and no ticker is asserted for it."
}
```

## ADVI_BDPRCE-D1-W12-S4 -- trace_price_v2 follows the interpolated canonical row and reports no trade ids, so it cannot show R1's carry-forward trades for this holding

```json
{
  "id": "ADVI_BDPRCE-D1-W12-S4",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~12",
  "surfaced_at": "2026-10-13T20:34:54Z",
  "one_line": "trace_price_v2 follows the interpolated canonical row and reports trade_ids empty for this holding, so R1's carry-forward trades come from a separate recompute.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~12/TRACE_BP-b-8.json: follows_served true, followed_source canonical, rule linear_interpolation, trade_ids [], rows_used 0, claim absent",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~12/recompute_R1_BP-b-8.py: R1 carry-forward 10.3525 observed 2026-10-02, distinct trade ids 742108391 and 742108404"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-b-8 section 1a(3): run trace_price_v2.py with the lot's current_price as the served price and record what it followed; for a day with no trade, the recompute is the last observed R1 price on observation_date.",
  "world_is": "The trace is an as-built instrument: it reports the followed row and its own rule, not R1's carry-forward. It cannot name the trades behind an R1 carry, so the record's trade_ids come from recompute_R1_BP-b-8.py and the trace is cited for the served row only."
}
```

## ADVI_BDPRCE-D1-W6-S1 -- 361 of 1,657 served rows have no R1 trade inside the 55-partition read window; reading the store back to 2020-03-06 resolves 149 of them and leaves 212 with no R1 trade anywhere.

```json
{
  "id": "ADVI_BDPRCE-D1-W6-S1",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~6",
  "surfaced_at": "2026-10-14T00:47:00Z",
  "one_line": "361 of 1,657 served rows have no R1 trade inside the 55-partition read window; reading the store back to 2020-03-06 resolves 149 of them and leaves 212 with no R1 trade anywhere.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "REPLAY.json@b11d7534d0: classes CHANGED 539, NOW_CARRY_FORWARD 285, NOT_RECOMPUTABLE 212, UNCHANGED 621; lookback_source assets 242, A_resolved 52, B_resolved 59",
      "lookback.csv@b11d7534d0: 242 residual assets, 52 with a variant-A observation and 59 with a variant-B observation, all dated before 2026",
      "LOOKBACK_FETCH.txt@b11d7534d0: 2,127 unique dates scanned from 2025-12-31 back to the 2020-03-06 floor; 436 of them have no partition",
      "Worker scratch runs (not committed, worker data folder): the same replay over the 55-partition window gave NOW_CARRY_FORWARD 136 and NOT_RECOMPUTABLE 361; over 2026-01-01 onward, 226 and 271"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-b-2 1a.2 and 1b: NOW_CARRY_FORWARD is the last observed R1 price with its observation date, and NOT_RECOMPUTABLE is no partition or no valid row; the cell reads the window 2026-08-20..2026-10-13 (55 partitions).",
  "world_is": "The window holds no R1 trade for 361 served rows, so they can only be carried forward from history before 2026-08-20. Reading to 2026-01-01 leaves 271 rows without a window trade. The lookback to 2020-03-06 (lookback.csv) gives 285 NOW_CARRY_FORWARD, 59 of them observed before 2026, and 212 NOT_RECOMPUTABLE. For 190 of the 242 residual assets no R1 trade exists in any partition from 2020-03-06 to 2026-10-13."
}
```

## ADVI_BDPRCE-D1-W6-S2 -- Eight bond and certificate rows in the window carry an executed price exactly 100 times the served unit price (1.0419 served, 104.19 traded), so applying R1 unchanged would move them by a factor of 100.

```json
{
  "id": "ADVI_BDPRCE-D1-W6-S2",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~6",
  "surfaced_at": "2026-10-14T00:47:00Z",
  "one_line": "Eight bond and certificate rows in the window carry an executed price exactly 100 times the served unit price (1.0419 served, 104.19 traded), so applying R1 unchanged would move them by a factor of 100.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~K1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "BEFORE_AFTER.csv@b11d7534d0: MIAMI-DADE CNTY FLA EDL FACS A 5.25% 04/01/2031, 2026-10-09: old 1.0419, new_price_A 104.19, flags estimated_row=0|scale_100x",
      "BEFORE_AFTER.csv@b11d7534d0: MISSOURI ST HEALTH & EDL FACS 5% 05/01/2033, 2026-10-09: old 1.0401, new_price_A 104.01, flags estimated_row=0|scale_100x",
      "REPLAY.json@b11d7534d0: scale_100x 8, all in class CHANGED",
      "data/black_diamond/scripts/silver/bd_price_rule.py@8956787a11: clause 3 reads the price column as the executed price per unit and applies no scale"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CTO ruling R1 clause 3, as bd_price_rule.py states it: the value is the trade's own executed price per unit (the price column), with no scale handling; served prices are per unit of 1.",
  "world_is": "For eight changed rows the R1 price is 100.0 times the served price within 1e-3. All eight fall between 2026-09-16 and 2026-10-09 and all are bond or certificate names. The replay flags them scale_100x and does not decide the scale rule; the 8 rows need a ruling before any served price moves."
}
```

## ADVI_BDPRCE-D1-W6-S3 -- Trade rows land in partitions dated after their trade date: 229,666 of 5.29 million rows in the 2026 partitions, 61,583 of them more than one day late and up to 519 days late; the lookback reads only one partition after the trade date.

```json
{
  "id": "ADVI_BDPRCE-D1-W6-S3",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~6",
  "surfaced_at": "2026-10-14T00:47:00Z",
  "one_line": "Trade rows land in partitions dated after their trade date: 229,666 of 5.29 million rows in the 2026 partitions, 61,583 of them more than one day late and up to 519 days late; the lookback reads only one partition after the trade date.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Worker scratch measurement (not committed): silver/transactions 2026-01-01..2026-10-13 read by aws s3api get-object; 5,294,039 trade rows, 5,064,373 with file date equal to trade date, 229,666 with file date after trade date, none before; lag over 1 day 61,583, maximum 519",
      "REPLAY.json@b11d7534d0: file_day_vs_trade_date_differs 33, seam_rows_in_window 9409",
      "REPLAY.md@b11d7534d0: Late-landed trades paragraph under What stays unknown"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-b-2 1a.2: keyed on trade_date, reading the partition of that date and the next partition when a row of the target trade_date sits there; a row belongs to the target date when its trade_date equals the target date (CTO ruling clause 6).",
  "world_is": "No 2026 partition holds a row dated before its own file date. 9,409 trade rows dated inside the window sit outside their trade-date partition, and 33 served rows price differently under own-day keying. Rows landing more than one day late fall outside the lookback's t and t+1 read, so a pre-2026 observation from the lookback may be older than the true latest. The window R1 reads every 2026 partition, so it is unaffected; trades that land after 2026-10-13 are not seen."
}
```

## ADVI_BDPRCE-D1-W6-S4 -- The canonical window holds no carry_forward source value, so the order's estimated-row clause (linear_interpolation or carry_forward) selects linear_interpolation rows only.

```json
{
  "id": "ADVI_BDPRCE-D1-W6-S4",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~6",
  "surfaced_at": "2026-10-14T00:47:00Z",
  "one_line": "The canonical window holds no carry_forward source value, so the order's estimated-row clause (linear_interpolation or carry_forward) selects linear_interpolation rows only.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "canonical_prices.parquet ETag 0ba9bd51fa175917b8d2813b41d78f5d, LastModified 2026-10-13T12:48:05Z, read by aws s3api get-object into the worker data folder: window source counts as stated",
      "ESTIMATED_ROWS.csv@b11d7534d0: 18,566 lines, canonical_source linear_interpolation on every line",
      "REPLAY.json@b11d7534d0: estimated_rows_listed 18566"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-b-2 1a.3: list every (date, asset) whose canonical source is linear_interpolation or carry_forward and whose asset has at least one transaction_observed row in the window.",
  "world_is": "In canonical_prices.parquet for 2026-09-16..2026-10-13 the source values are linear_interpolation 243,283, yahoo_finance 65,141, transaction_observed 1,657, scoped_override 120 and bd_txn_price 60; carry_forward appears 0 times. The estimated list therefore holds 18,566 linear_interpolation rows for 886 assets."
}
```

## ADVI_BDPRCE-D1-W6-S5 -- silver/transactions has no object for 50 dates between 2026-01-01 and 2026-08-19, 8 of them weekdays, and for 436 dates in 2020-03 to 2025-12; the replay reads a missing date as a day with no trades.

```json
{
  "id": "ADVI_BDPRCE-D1-W6-S5",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~6",
  "surfaced_at": "2026-10-14T00:47:00Z",
  "one_line": "silver/transactions has no object for 50 dates between 2026-01-01 and 2026-08-19, 8 of them weekdays, and for 436 dates in 2020-03 to 2025-12; the replay reads a missing date as a day with no trades.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3api get-object over silver/transactions/<date>.parquet for 2026-01-01..2026-08-19 (worker scratch, not committed): 50 NoSuchKey responses",
      "LOOKBACK_FETCH.txt@b11d7534d0: NO_PARTITION lines for 2020-03-07..2025-12-27, 436 unique dates, 101 weekdays"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-b-2 1b: NOT_RECOMPUTABLE is no partition or no valid row; a missing partition makes the day unrecomputable, and a day present with no trade for the asset is a carry-forward.",
  "world_is": "The missing weekday partitions in 2026 are 2026-02-18, 04-03, 04-21, 05-01, 05-25, 06-19, 06-22 and 06-23. 2026-06-22 and 06-23 are not market holidays. None of the window's 20 weekday partitions is missing. In 2020-03 to 2025-12 there are 436 dates without a partition, 101 of them weekdays."
}
```

## Rows filed by `0.9.0_WK_ADVI_BDPRCE~16` under `ADVI_BDPRCE.TO-BP-c-4.export-cap-check` (denominator at its write: 2 rows, `ADVI_BDPRCE-D1-W16-S1..S2`)

```json
[
  {
    "id": "ADVI_BDPRCE-D1-W16-S1",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~16",
    "surfaced_at": "2026-10-14T01:48:33Z",
    "one_line": "The bronze prefix forwardfill_v2/unrealized/ holds no UNREALIZED_DAILY key for 12 of the 14 calendar days 2026-09-30 to 2026-10-13; keys exist only on Fridays from 2026-07-10 on.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~K1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws s3api list-objects-v2 --bucket opal-data-bd --prefix forwardfill_v2/unrealized/ read 2026-10-14T01:4xZ: 91 keys, 76 UNREALIZED_DAILY and 15 _complete sidecars; org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~16/unreal_listing.txt@72e3acc775",
        "data/cot/scripts/bronze/cot_bronze_ingest.py@72e3acc775:481 writes forwardfill_v2/{table}/{TABLE}_DAILY_{date}.xlsx for each run date, so a key per run date is the expected landing"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Task order BP-c-4 section 1a step 1: find the bronze unrealized export key for each of at least the last 14 run dates by listing the bronze prefix with list-objects-v2, and record rows_per_day for each.",
    "world_is": "Keys sit on most weekdays from 2026-03-27 to 2026-07-09 (with 9 header-only stubs), then only on 2026-07-10, 07-17, 07-24, 07-31, 08-07, 08-14, 08-21, 08-28, 09-04, 09-11, 09-18, 09-25, 10-02 and 10-09, all Fridays. The matching _complete sidecars exist only for the same Fridays. The cause (runner cadence, lifecycle expiry or a move) is not established by this read, and the cell's 14-day count is therefore 2 dates, not 14."
  },
  {
    "id": "ADVI_BDPRCE-D1-W16-S2",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~16",
    "surfaced_at": "2026-10-14T01:48:33Z",
    "one_line": "The daily unrealized export holds exactly 500000 data rows on each of 15 non-stub days from 2026-07-08 to 2026-10-09, the count of a vendor cap, so those exports are not the complete lot population.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~K1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~16/CAP.json@72e3acc775: verdict CAP, days_checked 76, days_at_500000 15, rows_per_day for every key read; counts_all.jsonl@72e3acc775 holds the sheet-XML count per file with dimension refs agreeing on all 76",
        "openpyxl read_only iter_rows on UNREALIZED_DAILY_2026-10-09.xlsx: 500001 rows including the header, 500000 data rows (positive control for the sheet-XML count, read 2026-10-14)",
        "data/black_diamond/scripts/bronze/templates/unrealized.json@72e3acc775:497 isLimitSize false; data/cot/scripts/bronze/cot_bronze_ingest.py@72e3acc775:247-248 reads the whole response body and :430 pops isLimitSize before v1/run, so the runner sets no row limit"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Task order BP-c-4 and its cell text: a round-number count is the signature of a vendor cap, and a capped export silently drops lots, the opposite of the project's exact-lot outcome; the cap question is answered before any apply of the Units and Cost Basis switch.",
    "world_is": "The count is exactly 500000 on 15 of the 67 non-stub days, every one from 2026-07-08 on, and the 52 earlier non-stub days vary with the book from 408467 to 489203. The round-2 fixture 2026-10-09 holds the same 500000 rows. No repo setting yields 500000, so the cap sits on the Black Diamond side and is inferred from the count pattern; lots beyond the cap are not in those exports, and any silver partition built from them carries the same truncation (not measured here). The apply of the Units and Cost Basis switch waits on this row's disposition."
  }
]
```

## ADVI_BDPRCE-D1-W13-S1 -- The ruled candidate test (Fixed Income and coupon_rate not null) selects 2 of the 8 round-2 scale_100x rows; the other 6 stay at 100x

```json
{
  "id": "ADVI_BDPRCE-D1-W13-S1",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~13",
  "surfaced_at": "2026-10-14T01:47:11Z",
  "one_line": "The ruled candidate test (Fixed Income and coupon_rate not null) selects 2 of the 8 round-2 scale_100x rows; the other 6 are Fixed Income with a null coupon and stay at 100x.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/RULE_PROBE2.json@cd073f6a13 par_quoted block: unit_scale_rows_unchanged 2 of 8; fixed_income_unscaled_with_ratio_near_100 lists the six",
      "silver/bd_assets_dim.parquet read live from opal-data-bd (get_object, READ only, 2026-10-14); md5 in RULE_PROBE2.json sources_md5",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~6/BEFORE_AFTER.csv scale_100x rows (eight)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-1 1a.2: a par-quoted candidate is asset_super_class_bd == 'Fixed Income' AND coupon_rate not null. BP-c-1 1c: unit_scale_rows_unchanged counts how many of the eight round-2 scale_100x rows now read equal to the served price.",
  "world_is": "The test selects MIAMI-DADE CNTY FLA EDL FACS A 5.25% 04/01/2031 and MISSOURI ST HEALTH & EDL FACS 5% 05/01/2033 (both now read the served price). Six scale_100x rows are Fixed Income with coupon_rate null and are not selected: BANK MIDWEST SPIRIT LAKE IOWA 3.85% 2026, PNC BANK NATIONAL ASSOCIATION 4.1% 2027, STATE BK INDIA NEW YORK NY 3.95% 2027, TRUIST BK 3.9% 2026, WELLS FARGO BANK NATL ASSN 3.8% 2026 (2026-09-16) and CITIGROUP INC 5.3% 07/22/2032 (2026-09-22). They read 99.662, 99.5823, 99.629, 99.722, 99.6876 and 97.021, unchanged from round 2, and each has price/(market_value/units) within 1 percent of 100. The probe lists them in fixed_income_unscaled_with_ratio_near_100 and does not scale them. The count is 2 of 8, not 8 of 8."
}
```

## ADVI_BDPRCE-D1-W13-S2 -- Four asset names in the asset dimension carry rows that disagree on the candidate test; the amendment does not say how to key them

```json
{
  "id": "ADVI_BDPRCE-D1-W13-S2",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~13",
  "surfaced_at": "2026-10-14T01:47:11Z",
  "one_line": "Four asset_name values in silver/bd_assets_dim.parquet have rows that disagree on the candidate test, so the name cannot identify one class; the amendment is silent on this.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/bd_assets_dim.parquet read live (get_object, READ only): 12,232 rows, 12,007 distinct asset_name values, 115 null names",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/RULE_PROBE2.json@cd073f6a13 par_quoted.dimension_names_conflicting_excluded"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-1 1a.2: the asset dimension's class field is the identifier of a par-quoted asset; the candidate set is built from the dimension.",
  "world_is": "Four names carry dimension rows that disagree on Fixed Income plus coupon_rate not null: JPMORGAN CHASE BK N A 5.5% 2024 (one Cash and Cash Equivalents row), NEW YORK ST DORM AUTH ST PERS 5% 03/15/2036 (one row with a null coupon), NEW YORK TRANSN DEV CORP SPL F 5% 12/01/2030 (one To Be Classified row), PREMONT TEX IND SCH DIST 3.625% 08/15/2047. R1.1 treats a name as a candidate only when every row qualifies, so none of the four is scaled. The candidate set is 1,129 names from 1,163 qualifying rows."
}
```

## ADVI_BDPRCE-D1-W13-S3 -- The 2026-10-02 partition carries 8 rows of transaction_type Corporate Action, a type round 2 did not see; R1.1 counts them UNCLASSIFIED

```json
{
  "id": "ADVI_BDPRCE-D1-W13-S3",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~13",
  "surfaced_at": "2026-10-14T01:47:11Z",
  "one_line": "silver/transactions/2026-10-02.parquet holds 8 rows of transaction_type Corporate Action, a type not in round 2's thirteen; the module counts them UNCLASSIFIED and excludes them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/transactions/2026-10-02.parquet read live (get_object, READ only); 8 rows, 2 distinct transaction_id, prices 0.0 and 31.3, all trade_date 2026-10-02",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/RULE_PROBE2.json@cd073f6a13 census 2026-10-02 excluded_by_type UNCLASSIFIED 8"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-1 1c: report the types seen and anything that could not be classified. Round 2 (RULE_PROBE.md) reported thirteen types, all known, unclassified none.",
  "world_is": "Corporate Action is a transaction_type value present on 2026-10-02 and in no earlier round's type list. It is not a trade under R1.1 and is excluded and counted as UNCLASSIFIED."
}
```

## ADVI_BDPRCE-D1-W13-S4 -- The task order's probe dates omit 2026-09-16, which holds five of the eight round-2 scale_100x rows

```json
{
  "id": "ADVI_BDPRCE-D1-W13-S4",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~13",
  "surfaced_at": "2026-10-14T01:47:11Z",
  "one_line": "The named probe dates (2026-10-09, 09-22, 10-08, 10-02) omit 2026-09-16, the date of five of the eight scale_100x rows that unit_scale_rows_unchanged counts; the probe read that partition too.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~6/BEFORE_AFTER.csv: scale_100x rows dated 2026-09-16 (five) and 2026-09-22 (one) and 2026-10-09 (two)",
      "silver/transactions/2026-09-16.parquet and 2026-09-17.parquet read live (get_object, READ only), in addition to the named dates"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-1 1c: run the amended module over partitions 2026-10-09, 2026-09-22, 2026-10-08 and 2026-10-02, reading each date's partition and the next; unit_scale_rows_unchanged counts the eight round-2 scale_100x rows.",
  "world_is": "Five of the eight scale_100x rows are dated 2026-09-16, outside the named dates. The eight-row count cannot be taken without that partition. The probe covers 2026-09-16, 09-22, 10-02, 10-08 and 10-09 (each with its next day)."
}
```

## ADVI_BDPRCE-D1-W13-S5 -- BEFORE_AFTER.csv carries a variant-A price for BLACKROCK INC COM on 2026-09-22, where the round-2 probe records variant A as absent

```json
{
  "id": "ADVI_BDPRCE-D1-W13-S5",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~13",
  "surfaced_at": "2026-10-14T01:47:11Z",
  "one_line": "Two round-2 records disagree on the variant-A value for BLACKROCK INC COM on 2026-09-22: the before/after list gives new_price_A 1078.04 with 0 distinct trades; the probe record says A is absent.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~6/BEFORE_AFTER.csv line 489: 2026-09-22,BLACKROCK INC COM, new_price_A 1078.04, new_price_B 1074.9259, distinct_trades 0",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~5/RULE_PROBE.md: BLACKROCK INC COM 2026-09-22, A absent (no Buy or Sale rows); B 1074.9259"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-1 1a: round 2 read BLACKROCK INC COM on 2026-09-22 as absent under buys and sells and 1,074.9259 with reinvestment.",
  "world_is": "The before/after list carries a non-null variant-A price (1078.04) for an asset-date with zero distinct trades. R1.1 reads 1074.9259 from four distinct reinvestment transaction ids (733524155, 733526392, 733527817, 733530060). The before/after variant-A column is not used by this cell."
}
```

## ADVI_BDPRCE-D1-W13-S6 -- Two Sale rows with price 0.0 on 2026-09-22 are excluded as no-price, against round 2's record of zero no-price trade rows

```json
{
  "id": "ADVI_BDPRCE-D1-W13-S6",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~13",
  "surfaced_at": "2026-10-14T01:47:11Z",
  "one_line": "silver/transactions/2026-09-22.parquet holds two Sale rows with price 0.0 for INVESCO DISCOVERY Y; round 2 recorded no trade row lacking a valid price.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/transactions/2026-09-22.parquet read live (get_object, READ only): transaction_id 734745995 and 734745996, transaction_type Sale, price 0.0, trade_date 2026-09-22",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/RULE_PROBE2.json@cd073f6a13 census 2026-09-22 no_price_excluded 2"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-b-2 record (RULE_PROBE.md, round 2): no trade row lacked a valid price; no_price_excluded 0 under both variants.",
  "world_is": "Two Sale rows on 2026-09-22 carry price 0.0. R1.1 excludes them under clause 3 and counts them in no_price_excluded; they are not a price."
}
```

## ADVI_BDPRCE-D1-W13-S7 -- The commit-time naming gate refused the module's candidate function for naming a dimension column; the function now takes its field names as parameters

```json
{
  "id": "ADVI_BDPRCE-D1-W13-S7",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~13",
  "surfaced_at": "2026-10-14T01:47:11Z",
  "one_line": "The naming gate (LGIC_ENFORCE) refused a new string in the module that is a dimension column name ending in the firm short form; the module now takes the field names as arguments and the probe passes them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/safe-commit.sh first attempt on the module: naming-gate REFUSE at bd_price_rule.py line 177 (asset_super_class_bd -> lookup('49financial')), NAMING-GATE REFUSE 1 graded",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/rule_probe2.py passes the dimension column names; org/ paths are outside the naming gate domain (EXCLUDED org/, docs/ in the gate output)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-1 2 bounds and 1a.2: the module stays free of AWS and takes the candidate set as a parameter; the PROBE builds the set from the dimension. Rule 30 of the worker's standing rules: a builder refusal is a registry row to add, never a hand-typed workaround.",
  "world_is": "The gate treats a dimension's own column name as a hand-kept carrier of the firm code and suggests a registry lookup, which does not name a column. The candidate test now lives in the module as a generic function over caller-named fields, and the probe (outside the gate's domain) passes the Black Diamond column names. Behaviour is unchanged: the probe record is byte-equal before and after the change (md5 523247e6fb2779774f613747a6f08827)."
}
```

## ADVI_BDPRCE-D1-W18-S1 -- The round-2 record dates the runner's oldest readable log event to 2026-09-30; the live group's first event from 2026-09-14 is 2026-10-01T00:00:19Z

```json
{
  "id": "ADVI_BDPRCE-D1-W18-S1",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~18",
  "surfaced_at": "2026-10-14T01:53:18Z",
  "one_line": "CAUSE.json (BP-b-5) gives the runner's oldest readable event as 2026-09-30T00:00Z; the live group returns 2026-10-01T00:00:19Z as its first event from 2026-09-14, so no runner log line for 2026-09-29 or 2026-09-30 can be read.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws logs filter-log-events --region us-east-1 --log-group-name /aws/lambda/bd-49f-runner --start-time 2026-09-14T00:00Z --limit 1 returned timestamp 1790812819121 ms, which is 2026-10-01T00:00:19Z (read 2026-10-14T01:3xZ, SENTINEL.json oldest_readable_runner_event)",
      "aws logs describe-log-groups --log-group-name-prefix /aws/lambda/bd-49f-runner: retentionInDays 14",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~9/CAUSE.json@33b647a50f states the runner group's oldest readable event as 2026-09-30T00:00Z in its evidence for 2026-09-29"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-b-5 record CAUSE.json (round 2): log retention ended on 2026-09-30, and the oldest readable event in the runner group is 2026-09-30T00:00Z.",
  "world_is": "The oldest readable runner event on this read is 2026-10-01T00:00:19Z. The 2026-09-30 events are past the 14-day retention, so that date is not classifiable from logs. No count in BP-c-6 changes, because the readable log dates are 10-01 to 10-14 in either reading."
}
```

## ADVI_BDPRCE-D1-W18-S2 -- Commit 3709ae40d6 says the runner role has no s3:GetObject on bronze/*; the live role grants GetObject on bronze/*/_BRONZE_COMPLETE.json only, and the read-back on that key works

```json
{
  "id": "ADVI_BDPRCE-D1-W18-S2",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~18",
  "surfaced_at": "2026-10-14T01:53:18Z",
  "one_line": "The role bd-49f-runner-role grants s3:GetObject on bronze/*/_BRONZE_COMPLETE.json (statement ReadBackBdBronzeSentinel), not on bronze/* as commit 3709ae40d6 describes; the narrower grant covers the read-back, and the post-deploy runs print sentinel emitted.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws iam get-role-policy --role-name bd-49f-runner-role --policy-name bd-49f-runner-policy (read 2026-10-14T01:3xZ): statement ReadBackBdBronzeSentinel, Allow s3:GetObject on arn:aws:s3:::opal-data-bd/bronze/*/_BRONZE_COMPLETE.json; no GetObject on bronze/* as a whole",
      "aws logs filter-log-events RESULT on /aws/lambda/bd-49f-runner, 2026-10-08 to 2026-10-14: each RESULT line carries sentinel emitted, which needs the head_object read-back (lambda_function.py@33b647a50f :192-198) to succeed",
      "git show 3709ae40d6 commit message: the live runner role has no s3:GetObject on bronze/*, so the required head_object read-back is refused"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Commit 3709ae40d6 message: the runner role needs s3:GetObject on bronze/* for the head_object read-back of the sentinel.",
  "world_is": "The live role grants GetObject on the sentinel key only, which is the key the read-back reads, and the read-back succeeds in production. The date the narrow grant was added was not read in this cell, so the commit's bronze/* wording is no longer the live state."
}
```

## ADVI_BDPRCE-D1-W18-S3 -- Eight Monday and Tuesday run dates have no bronze sentinel, not the six the round-2 record lists; 2026-09-14 and 2026-09-15 hold no bronze objects at all

```json
{
  "id": "ADVI_BDPRCE-D1-W18-S3",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~18",
  "surfaced_at": "2026-10-14T01:53:18Z",
  "one_line": "S3 has no bronze/<date>/_BRONZE_COMPLETE.json for 2026-09-14 and 2026-09-15 either; the round-2 list of six sentinel-less Monday and Tuesday dates is short by those two, and neither date has any bronze object.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3api head-object on bronze/<date>/_BRONZE_COMPLETE.json (2026-09-14 to 2026-10-14): 404 for 09-14, 09-15, 09-21, 09-22, 09-28, 09-29, 10-05 and 10-06; present for 10-12 (363 bytes) and 10-13 (277 bytes)",
      "aws s3api list-object-versions --prefix bronze/2026-09-14/ and bronze/2026-09-15/: zero versions, zero delete markers (SENTINEL.json calls)",
      "CAUSE.json@33b647a50f lists six sentinel-less dates: 2026-09-21, 09-22, 09-28, 09-29, 10-05 and 10-06"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-b-5 record CAUSE.json (round 2): the Monday and Tuesday run dates with no bronze sentinel are six: 2026-09-21, 09-22, 09-28, 09-29, 10-05 and 10-06.",
  "world_is": "Eight Monday and Tuesday run dates have no sentinel: the six, plus 2026-09-14 and 2026-09-15. Neither of the two has any bronze object. Whether the sentinel path existed on those two dates is not read here. Their runner logs are past retention."
}
```

## ADVI_BDPRCE-D1-W18-S4 -- The post-deploy runner completes a day on a header-only transactions export, so the 2026-10-12 and 2026-10-13 sentinels exist over zero transaction rows

```json
{
  "id": "ADVI_BDPRCE-D1-W18-S4",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~18",
  "surfaced_at": "2026-10-14T01:53:18Z",
  "one_line": "EMPTY_WINDOW_OK_TABLES accepts a measured-empty transactions export as complete, so the 2026-10-12 and 2026-10-13 sentinels were emitted over header-only transactions (4358 and 4354 bytes); every Monday and Tuesday will complete the same way until the window is fixed.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~K1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "lambda_function.py@33b647a50f :118 EMPTY_WINDOW_OK_TABLES = frozenset(('transactions',)); :137 has_data_rows == 0 accepted; :163 complete-empty state; :197 note measured-empty window accepted",
      "aws logs: 2026-10-12 RESULT and OK bronze sentinel emitted (event prefix 399576695212, 00:11:10Z) and 2026-10-13 OK bronze sentinel emitted with the measured-empty note (event prefix 399595967749, 00:11:31Z); sentinel objects 363 and 277 bytes",
      "aws s3api get-object forwardfill_v2/transactions/TRANSACTIONS_DAILY_<date>.xlsx for 2026-10-12 (VersionId 2FPO.Dwpi81bBbPhVMwVUk31qW6U1rPf, 4358 bytes) and 2026-10-13 (VersionId 13q3LKubG7cq5_7vZqAhPuhQ4hcPdTFN, 4354 bytes): zero data rows"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "bd-49f-runner docstring at 33b647a50f, lines 30-33: the bronze sentinel fires the silver merge ONLY on a COMPLETE bronze, and a partial pull must NOT advance silver. Lines 35-41: a Monday or Tuesday window can be genuinely empty.",
  "world_is": "The Monday and Tuesday windows are not genuinely empty: SENTINEL.json gives EXPORT_WINDOW_RULE, and the last published trade day lies outside the span. The runner still accepts the empty transactions table, so the sentinels for 10-12 and 10-13 exist over zero transaction rows, and the sentinel is what triggers bd-silver-merge (BP-b-5 record). Whether silver for those two dates was built on the header-only content is not read in this cell."
}
```

## ADVI_BDPRCE-D1-W18-S5 -- The runner file sets no transactions window: it calls mod._window_for, the window and its 3-day chunking live in the shared module, and the chunk size is a deployed environment value

```json
{
  "id": "ADVI_BDPRCE-D1-W18-S5",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~18",
  "surfaced_at": "2026-10-14T01:53:18Z",
  "one_line": "The BP-c-6 order points to asOfDate in the runner; the runner has no asOfDate, git log -S asOfDate on the runner file returns no commit, and the transactions window is set in data/cot/scripts/bronze/cot_bronze_ingest.py with BD_TXN_CHUNK_DAYS=3 in the deployed environment.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git log -S asOfDate -- infra/aws/lambda/bd-pipeline/bd-49f-runner/lambda_function.py at 33b647a50f returns no commit; the positive control git log -S _window_for on the same file returns 9d44d6af5b and f6ca77914b",
      "lambda_function.py@33b647a50f :236 start, end = mod._window_for(table, run_date) and :244 mod.ingest_table(...); the window is cot_bronze_ingest.py :131, :320-321, :327-335, :338-362, :797-798",
      "aws lambda get-function-configuration --function-name bd-49f-runner: Environment BD_TXN_CHUNK_DAYS=3 and BD_SNAPSHOT_ASOF_LAG_BDAYS=1 (values printed; secret-named keys redacted)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order BP-c-6 1a.4: find where the runner or the template sets the transactions window (look for asOfDate, startDate, endDate, today, utcnow); the P1 history in git log -S asOfDate on the runner file is a hint.",
  "world_is": "The runner file sets no window and delegates to the shared module. The deployed environment sets the chunk size. The hint's history search on the runner file is empty, so the window is measured from cot_bronze_ingest.py and the environment, not from the runner."
}
```

## ADVI_BDPRCE-D1-W17-S1 -- The ruled lot key folds 192 rows on the recorded export, and 191 colliding groups still differ on Market Value; the zero target is not met.

```json
{
  "id": "ADVI_BDPRCE-D1-W17-S1",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~17",
  "surfaced_at": "2026-10-14T02:21:23Z",
  "one_line": "The ruled lot key folds 192 rows on the recorded export, and 191 colliding groups still differ on Market Value; the zero target is not met.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~K1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "UNREALIZED_DAILY_2026-10-09.xlsx (opal-data-bd forwardfill_v2/unrealized/, VersionId Wf2Pct313A.w7y1GpuSf2f7FfiKUVats, sha256 5700843f9e661364910a5bbb9d9d4b60521775922539f47b066a10d80039ef5b) read by get-object 2026-10-13; 500,000 rows, 0 exact duplicates; test_lot_split2.py --emit-proof at fa9d37edb5: lot rows 499,808 under (relationship_id, account_id, asset_id, open_date, unit_cost), rows folded 192, colliding groups 191 (383 rows)",
      "same run, LOT_PROOF2.json differing_columns at fa9d37edb5: Market Value differs in 191 of 191 colliding groups, Inherited Date in 1; the 192 folded rows have no null Open Date"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v1.1 ADDENDUM and BP-c-5 section 1: under the ruled key (relationship_id, account_id, asset_id, open_date, unit_cost), the fixture proof reaches zero rows folded and zero colliding groups still differing on any column before the template apply may proceed.",
  "world_is": "Under the ruled key 192 rows of the recorded export fold into 191 colliding groups, and all 191 differ on Market Value (one also on Inherited Date). The export has no lot identifier column, so no recorded column separates them. Within one snapshot one asset has one price, so the differing Market Value most likely reflects distinct quantities, which would mean distinct lots; this is INFERRED, not measured, because the export carries no Units. Applied under this key, the lot table would drop those 192 rows. Armed for the apply: the apply's author decides a key that separates them (a units-bearing key is untested on this fixture) before any template switch."
}
```

## ADVI_BDPRCE-D1-W17-S2 -- Round 2's colliding-group counts (14,696 and 14,514) are pandas dropna=True counts; with null Open Date kept as a value they are 14,865 and 14,683.

```json
{
  "id": "ADVI_BDPRCE-D1-W17-S2",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~17",
  "surfaced_at": "2026-10-14T02:21:23Z",
  "one_line": "Round 2's colliding-group counts (14,696 and 14,514) are pandas dropna=True counts; with null Open Date kept as a value they are 14,865 and 14,683.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "test_lot_split2.py --emit-proof at fa9d37edb5 prints KEY round-2 (reference): colliding_groups=14865, rows_in_colliding_groups=30418, null_open_date_rows=7384 on the same export (sha256 5700843f...)",
      "LOT_PROOF2.md section 'Counts against round 2' at fa9d37edb5; the 15,553 folded-row count reproduces in both rounds"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Round-2 row ADVI_BDPRCE-D1-W10-S2: the mandated key folds 15,553 export rows into 14,696 colliding groups, 14,514 of them differing on Relationship ID.",
  "world_is": "The 15,553 folded-row count reproduces. The group counts reproduce only with groupby dropna=True, which drops the 7,384 null-Open-Date rows (7,208 key groups) from the grouping. Keeping null Open Date as one value, the same key has 14,865 colliding groups (30,418 rows), of which 14,683 differ on Relationship ID. Round 2 mixed the two conventions in one row. No lot count changes."
}
```

## ADVI_BDPRCE-D1-W17-S3 -- The CAP record's paging plan cannot be run from readable S3 data: no slice exports exist, so the capped 2026-10-09 export cannot be completed for the zero.

```json
{
  "id": "ADVI_BDPRCE-D1-W17-S3",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~17",
  "surfaced_at": "2026-10-14T02:21:23Z",
  "one_line": "The CAP record's paging plan cannot be run from readable S3 data: no slice exports exist, so the capped 2026-10-09 export cannot be completed for the zero.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "CAP.json at 0.9.0_WK_ADVI_BDPRCE~16 (verdict CAP; paging_plan 'Not run'); aws s3api list-objects-v2 --prefix forwardfill_v2/unrealized/ read in this run on 2026-10-14 UTC (one UNREALIZED_DAILY object per date, no slice keys)",
      "get-object of forwardfill_v2/unrealized/_complete/2026-10-09.json: {has_data_rows, landed_at, bytes, producer, basis}; no row count, no page field"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-5 section 1a: if the CAP record names a paging plan, say whether the fixture can be paged from S3 data you can read, and use it only if the data exists.",
  "world_is": "The CAP record names a slice-on-Relationship-ID paging plan and marks it not run. The readable S3 data hold the capped 500,000-row export only. Completeness of the 2026-10-09 snapshot is not determinable from readable data, so a zero on this export holds for the rows exported, not for the snapshot. A paged export is a Black Diamond producer run, which this cell may not perform."
}
```

## ADVI_BDPRCE-D1-W13-S8 -- ALLSPRING CORE BOND CIT CLASS E2 is To Be Classified in the asset dimension, not Fixed Income; it reads 10.3525 through the non-Fixed-Income keep path, not the per-unit path

```json
{
  "id": "ADVI_BDPRCE-D1-W13-S8",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~13",
  "surfaced_at": "2026-10-14T02:28:42Z",
  "one_line": "The task order names ALLSPRING CORE BOND CIT CLASS E2 as a Fixed Income fund left alone per unit; the dimension classes it To Be Classified, so the Fixed Income test never reaches it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/bd_assets_dim.parquet read live (get_object, READ only, 2026-10-14T02:22Z): the one row for ALLSPRING CORE BOND CIT CLASS E2 carries asset_super_class_bd To Be Classified; md5 45dfaab5b5756b8458c6cfae63bf9f38",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/RULE_PROBE2.json@8ee423d274 assets entry 2026-10-02 ALLSPRING: kind trade, price 10.3525, fixed_income_candidate false, per_unit_left 0",
      "org/missions/D8/ADVI/ADVI_BDPRCE/task-orders/ADVI_BDPRCE.TO-BP-c-1.rule-amendment.md@544d551f1d section 1.0 item 2 names this fund as the example of a Fixed Income fund left alone at 10.3525"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-1 1.0 (Amendment 2): a row is par-quoted when the asset is Fixed Income (asset_super_class_bd == 'Fixed Income') and the ratio is within 1 percent of 100; a fixed-income fund at 10.3525 is left alone, for example ALLSPRING CORE BOND CIT CLASS E2.",
  "world_is": "The dimension's only row for ALLSPRING CORE BOND CIT CLASS E2 is To Be Classified, so the class test is false and the name is not a candidate. The price 10.3525 is still read, because its ratio is near 1 and a non-Fixed-Income row is kept at its executed price. The result matches the expected value, but the per-unit path the order describes is not the path that produced it. No Fixed Income fund scales on the five dates."
}
```

## ADVI_BDPRCE-D1-W13-S9 -- Two Fixed Income funds read ratios of 1.0844 and 1.0433, outside both the 1 and 100 bands, so R1.2 withholds nine rows and their assets have no price on those dates

```json
{
  "id": "ADVI_BDPRCE-D1-W13-S9",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~13",
  "surfaced_at": "2026-10-14T02:28:42Z",
  "one_line": "VANGUARD SHORT-TERM INVESTMENT-GRADE INV (2026-09-16, 5 rows, ratio 1.084382) and POLEN OPPORTUNISTIC HIGH YIELD - INS (2026-10-08, 4 rows, ratio 1.043334) are withheld as ratio_unrecognised; neither is within 1 percent of 1 or of 100.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/RULE_PROBE2.json@8ee423d274 par_quoted.withheld_ratios (1.0433 x4, 1.0844 x5) and census 2026-09-16 withheld_by_reason ratio_unrecognised 5, census 2026-10-08 ratio_unrecognised 4",
      "silver/transactions/2026-09-16.parquet and silver/transactions/2026-10-08.parquet read live (get_object, READ only); the withheld rows are the two funds named above",
      "silver/bd_assets_dim.parquet read live: both names carry asset_super_class_bd Fixed Income on every row"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-1 1.0 (Amendment 2): any other ratio of a Fixed Income row (not within 1 percent of 100, not within 1 percent of 1) is WITHHELD with its reason and printed ratio, never guessed.",
  "world_is": "Both funds are Fixed Income by the dimension and their executed price sits 4 to 8 percent away from market value per unit on those dates. The rule withholds the rows as written. Neither asset has a price on the withheld date, so a carry-forward applies there. The amendment does not say how a fund-level gap of this size is to be read."
}
```

## ADVI_BDPRCE-D1-W13-S10 -- Three dimension names carry rows that disagree on the Fixed Income class, not four as round 3 listed on the coupon test; NEW YORK ST DORM AUTH and PREMONT no longer conflict

```json
{
  "id": "ADVI_BDPRCE-D1-W13-S10",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~13",
  "surfaced_at": "2026-10-14T02:28:42Z",
  "one_line": "Under the class-only test the conflicting names are JPMORGAN CHASE BK N A 5.5% 2024, NEW YORK TRANSN DEV CORP SPL F 5% 12/01/2030 and VANGUARD TOTAL BOND MARKET INDEX I; the round-3 coupon list named four.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "silver/bd_assets_dim.parquet read live (get_object, READ only): JPMORGAN CHASE BK N A 5.5% 2024 carries Fixed Income and Cash & Cash Equivalents; NEW YORK TRANSN DEV CORP SPL F 5% 12/01/2030 and VANGUARD TOTAL BOND MARKET INDEX I carry Fixed Income and To Be Classified",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/RULE_PROBE2.json@8ee423d274 par_quoted.dimension_names_conflicting_excluded lists the three names"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-1 1.0 (Amendment 2): the Fixed Income identifier is the dimension's class column; the four dimension names with conflicting rows stay excluded and listed.",
  "world_is": "Three names disagree on the class column; the count is three, not four, because the candidate identifier no longer uses the coupon. The excluded names are kept at their executed prices, as before. VANGUARD TOTAL BOND MARKET INDEX I is a name that a round-3 coupon test did not list."
}
```

## ADVI_BDPRCE-D1-W13-S11 -- Amendment 2 does not say how a non-Fixed-Income row is treated when its ratio is neither near 1 nor near 100; R1.2 keeps it at its price and withholds only a non-Fixed-Income row near 100

```json
{
  "id": "ADVI_BDPRCE-D1-W13-S11",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~13",
  "surfaced_at": "2026-10-14T02:28:42Z",
  "one_line": "The ruling gives the per-row rule for Fixed Income rows only; a non-Fixed-Income row near 100 is withheld by the order's arm, and any other non-Fixed-Income ratio is kept at its price by an inference the order does not state.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_BDPRCE/task-orders/ADVI_BDPRCE.TO-BP-c-1.rule-amendment.md@544d551f1d section 1.0 and arm list in 1b: a non-Fixed-Income asset with ratio near 100 is NOT scaled and is withheld with its ratio; no clause covers other non-Fixed-Income ratios",
      "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/RULE_PROBE2.json@8ee423d274 census: withheld_by_reason holds only ratio_unrecognised rows of Fixed Income names on the five dates"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-1 1.0 (Amendment 2): the per-row ratio test applies to Fixed Income rows; arm (c) of section 1b requires a non-Fixed-Income row near 100 to be withheld with its ratio.",
  "world_is": "Every rule clause is stated for Fixed Income rows except the near-100 arm. The module keeps other non-Fixed-Income rows at their executed price, as round 2 did, and records that reading in its docstring. On the five dates no non-Fixed-Income row was withheld, so the reading moves no served number in the probe; a later reader of the amendment may take a different one."
}
```

## ADVI_BDPRCE-D1-W13-S12 -- The scope checker's base is the merge-base with the primary checkout (e82f01c4ff), so the issuer's cut-point commit 544d551f1d shows as a change of this cell and AC3 reads one outside path

```json
{
  "id": "ADVI_BDPRCE-D1-W13-S12",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~13",
  "surfaced_at": "2026-10-14T02:30:52Z",
  "one_line": "AC3 (r4_scope.py) reads 7 changed, 1 outside: the outside path is the task order file, edited by the issuer's commit 544d551f1d on this branch, which is above the checker's merge-base e82f01c4ff.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git merge-base HEAD of wk-ADVI_BDPRCE-13 with the primary checkout HEAD = e82f01c4ff (measured in this session); git diff --name-only e82f01c4ff HEAD lists the task order file and the six paths of this cell",
      "git show --stat 544d551f1d: org/missions/D8/ADVI/ADVI_BDPRCE/task-orders/ADVI_BDPRCE.TO-BP-c-1.rule-amendment.md only, 6 insertions and 13 deletions; 544d551f1d is not an ancestor of the primary checkout HEAD",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py@544d551f1d takes the base as git merge-base HEAD with the first worktree HEAD, not the commit the worktree was cut from"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-1 4 (AC3): the write-surface bound; ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing, over the four allowed surfaces. The worktree is cut from e82f01c4ff plus the issuer's commit 544d551f1d.",
  "world_is": "The checker measures from the merge-base with the primary checkout, which is e82f01c4ff, so the issuer's task order edit on this branch counts as a change of this cell. Every path this seat wrote is inside its grant. The seat did not write the task order and did not rewrite history to clear the row. The base or the issuer's cut point has to change for AC3 to read OK."
}
```

## ADVI_BDPRCE-D1-W14-S1 -- The canonical prices object was rewritten after round 2 read it: 1,664 served window rows, not 1,657; the seven added rows and 3,814 interpolated-to-yahoo rows are the difference

```json
{
  "id": "ADVI_BDPRCE-D1-W14-S1",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~14",
  "surfaced_at": "2026-10-14T03:26:07Z",
  "one_line": "silver/prices/canonical_prices.parquet was rewritten at 2026-10-14T00:13:47Z; the window holds 1,664 transaction_observed rows, not the 1,657 round 2 served.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "get-object of silver/prices/canonical_prices.parquet in this session: ContentLength 105405895, ETag 8eaa29e37c4e651381413b02ca2b43b2, LastModified 2026-10-14T00:13:47+00:00; round 2 REPLAY.json@0.9.0_WK_ADVI_BDPRCE~6 recorded ETag 0ba9bd51... modified 2026-10-13T12:48:05Z",
      "served_vs_round2 in REPLAY2.json@6a39e57498: round2 rows 1657, current rows 1664, added 7 (six CASH AND MARGIN  INTEREST at 1.0 on 2026-09-24, 09-25, 09-29, 09-30, 10-06, 10-12; GLOBAL X S&P 500 TAIL RISK ETF on 2026-10-12), removed 0, common price differs 0",
      "python comparison of the round-2 canonical copy (C:/dev/wk-bdprce-r2-6-data) with the current copy over 2026-09-16..2026-10-13: 3,814 rows that were linear_interpolation in round 2 are yahoo_finance now (2026-10-12 among them); 28 keys added, none removed"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-2 1a.1: same served set (the 1,657 rows; re-read canonical_prices.parquet for the window and print the denominator; if it differs, say so).",
  "world_is": "The served set is 1,664 transaction_observed rows. The replay lists all 1,664 under the current canonical object. The count is said here, as the spec asks. No round-2 served row is missing and no common price changed. The round-2 interpolated count of 18,566 is 18,420 on the current object over 887 assets; the 3,814 source changes to yahoo_finance are the likely cause, not measured per asset."
}
```

## ADVI_BDPRCE-D1-W14-S2 -- Three 2026 transaction partitions (2026-10-02, 2026-10-08, 2026-10-11) carry different bytes in S3 from round 2's cached copies; they were rewritten at 2026-10-14T00:11 to 00:13Z, after round 2 read them

```json
{
  "id": "ADVI_BDPRCE-D1-W14-S2",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~14",
  "surfaced_at": "2026-10-14T03:26:07Z",
  "one_line": "Round 2's cached copies of three 2026 transaction partitions fail the head-object size and ETag check; the current S3 objects were fetched and verified and are the ones the replay reads.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "PARTITIONS2.csv@6a39e57498 (first verification pass): 2026-10-02 cached 308,240 bytes vs S3 315,148; 2026-10-08 cached 4,468,744 vs 4,507,465; 2026-10-11 cached 391,262 vs 35,306 (MISMATCH_SIZE)",
      "get-object of the three keys at 2026-10-14T00:11:32Z, 00:12:55Z and 00:13:00Z (LastModified in the response); the refetched copies verify by MD5 against head-object ETag (PARTITIONS2.csv@6a39e57498, second pass: 0 needing fetch)",
      "round 2's replay read its cached copies (C:/dev/wk-bdprce-r2-6-data/tx and tx_back); those bytes differ from the S3 objects now, whose LastModified is 2026-10-14T00:11 to 00:13Z, so round 2's list was built on the earlier bytes"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-2 1a.3: round 2's cache is READ, and each partition is verified against S3 head-object ContentLength and ETag before reliance; a mismatch is refetched.",
  "world_is": "The mismatch was found and refetched as specified. The other 1,925 cached copies match S3 by MD5 (two multipart objects match by size). Round 2's before-after list was built on the earlier bytes of these three partitions, so the round-2 numbers for window dates that read them are not comparable to round 3 without this note."
}
```

## ADVI_BDPRCE-D1-W14-S3 -- The silver/transactions store holds a 2026-10-14 partition at the read (2,921 rows, 2,804 dated 2026-10-12) and no 2026-10-13 partition; leaving 2026-10-14 out changes one served row

```json
{
  "id": "ADVI_BDPRCE-D1-W14-S3",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~14",
  "surfaced_at": "2026-10-14T03:26:07Z",
  "one_line": "The store has a 2026-10-14 partition written at 00:13:04Z holding late-landed trades dated 10-12 and earlier, and no 2026-10-13 partition; trades dated 10-13 are not in the store at the read.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "list-objects-v2 of silver/transactions/ at the read: 1,928 dated keys, last 2026-10-14; no 2026-10-13 key (tx_listing.json in C:/dev/wk-bdprce-r3-14-data, outside the checkout)",
      "2026-10-14 partition: 2,921 rows; trade_date 2026-10-12 2,804, 2026-10-11 6, 2026-10-10 32, 2026-10-09 52, 2026-10-08 22, 2026-10-01 5 (python read of the partition, trade_date column only)",
      "sensitivity run with --exclude-day 2026-10-14 (REPLAY2.md, section The lookback and its limits): one served row differs, GLOBAL X S&P 500 TAIL RISK ETF 2026-10-12, CHANGED 29.349 with the partition, NOT_RECOMPUTABLE without it"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-2 1a.3: key the replay on trade_date across all partitions held or fetched; the replay is as of the read; round 2 read the partitions to 2026-10-13.",
  "world_is": "The 2026-10-14 partition is keyed, as the spec asks, and it is the reason one served row reads CHANGED. The 2026-10-13 partition does not exist, so the 886 interpolated rows dated 10-13 carry the last trade before that day, and no trade dated 10-13 is visible to this list."
}
```

## ADVI_BDPRCE-D1-W14-S4 -- The spec's interpolation sentence covers every window linear_interpolation row (239,490 over 11,135 assets), while its count (18,566 over 886) is the served-asset subset; the fates here cover the served assets only

```json
{
  "id": "ADVI_BDPRCE-D1-W14-S4",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~14",
  "surfaced_at": "2026-10-14T03:26:07Z",
  "one_line": "The window holds 239,490 linear_interpolation rows over 11,135 assets; the 18,420 rows on the 887 served assets are fated, the other 221,070 are not.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "window_source_counts and interpolated_window_all_assets in REPLAY2.json@6a39e57498: linear_interpolation 239,490; interpolated_window_all_assets_names 11135; interpolated_rows 18,420 over 887 served assets",
      "task order BP-c-2 1a.4 text: 'Every (date, asset) in the window whose canonical source is linear_interpolation (18,566 rows over 886 assets in round 2, re-count)'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-2 1a.4: every (date, asset) in the window whose canonical source is linear_interpolation gets its fate under the amended R1, and interpolated.rows equals their count.",
  "world_is": "The literal sentence and the stated count disagree by scope. I fated the served-asset scope, which is the scope of the stated count, and state the other 221,070 rows as not fated. Fating them would mean keying about 10,250 more assets over the whole history. Widening the scope is a ruling for the issuer."
}
```

## ADVI_BDPRCE-D1-W14-S5 -- MORGAN STANLEY FIN LLC 0% 05/03/2029 carries 1.0 per unit from a 2025 par Buy while its served series is per 100 (115.995); 214 interpolated rows carry values from par-scaled trades with the same exposure

```json
{
  "id": "ADVI_BDPRCE-D1-W14-S5",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~14",
  "surfaced_at": "2026-10-14T03:26:07Z",
  "one_line": "The largest per-unit mover (115.995 to 1.0 on 2026-10-05) is a 16-month-old carry of a par-scaled Buy; the served series for this asset is in per-100 units, so the carry is a 100x unit change.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~K1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "BEFORE_AFTER2.csv@6a39e57498 row 2026-10-05 MORGAN STANLEY FIN LLC 0% 05/03/2029: old 115.995 transaction_observed, new 1.0 NOW_CARRY_FORWARD, observation 2025-05-28, reason carry_forward_from_2025-05-28",
      "2025-05-28 partition (round 2 cache tx_back): one row, Buy, price 100.0, units 250000.0, market_value 250000.0 for this asset; R1.2 reads ratio 100 and scales it to 1.0",
      "canonical window rows 2026-09-28..2026-10-04 for this asset: linear_interpolation 114.37 to 115.76, the per-100 series; REPLAY2.json carry_forwards_from_par_scaled_trade 0 (served), interpolated_carry_from_par_scaled_trade 214"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CTO ruling AMENDMENT 1 clause 2: R1 serves the PER-UNIT price, the same unit as today's served price; the 100x quote is divided by 100.",
  "world_is": "For this asset today's served price is not per unit: its series is per 100 and the 1.0 is per unit. The rule's unit and the served unit disagree for the asset, and no ruling says which unit a carried par-quoted price takes. Any writer that publishes the list's carry would move this served price by 100x. The packet (BP-c-3) reads the list, so the disarm is to keep this asset and the 214 par-scaled interpolated carries out of that packet until the CTO rules the unit."
}
```

## ADVI_BDPRCE-D1-W14-S6 -- The spec is silent on a carry-forward whose last trade date holds a withheld row; this list refuses such carries (3 served rows, 126 interpolated rows), where the other reading would carry the last kept price

```json
{
  "id": "ADVI_BDPRCE-D1-W14-S6",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~14",
  "surfaced_at": "2026-10-14T03:26:07Z",
  "one_line": "A carry-forward whose latest trade date carries a withheld row is classed NOT_RECOMPUTABLE with reason ratio_unrecognised_carry, the spec does not say this; 3 served rows and 126 interpolated rows are affected.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "BEFORE_AFTER2.csv@6a39e57498: reason ratio_unrecognised_carry on 2026-09-24 and 2026-09-25 MFS TOTAL RETURN BOND R6, and 2026-10-09 T. ROWE PRICE US TREASURY INTERM IDX",
      "ESTIMATED_ROWS2.csv@6a39e57498: reason ratio_unrecognised_carry 126; ratio_unrecognised 1; these are the rows the refusal moves to unresolved",
      "REPLAY2.json@6a39e57498 interpolated.reasons and withheld_rows_via_carry_refusal 3"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-2 0 and 1b: withheld rows count as NOT_RECOMPUTABLE with the reason ratio_unrecognised; never guess a price for them.",
  "world_is": "Read literally, the spec covers withheld rows, not carries that pass over a withheld date. I took the conservative reading, so a refused carry is unresolved, not a stale price. The other reading would carry the last kept price. The count is in the record and the CTO rules before any widening."
}
```

## ADVI_BDPRCE-D1-W14-S7 -- The task order's cache premise (about 1,300 pre-2026 partitions) does not match the cache on disk (1,691 pre-2026 partitions and 237 in 2026); the cache was used as found, each partition verified

```json
{
  "id": "ADVI_BDPRCE-D1-W14-S7",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~14",
  "surfaced_at": "2026-10-14T03:26:07Z",
  "one_line": "The round-2 cache holds 1,691 pre-2026 partitions, not about 1,300 as the task order says; the worker prompt that carried the order says about 1,700.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "directory count of C:/dev/wk-bdprce-r2-6-data/tx_back at the read: 1,691 files, 2020-03-06 to 2025-12-31; C:/dev/wk-bdprce-r2-6-data/tx: 237 files",
      "PARTITIONS2.csv@6a39e57498: 1,928 dated keys verified, of which 1,691 pre-2026 from the cache and 237 2026 keys (3 refetched, 1 fetched)",
      "task order BP-c-2 1a.3 says about 1,300 partitions; the worker prompt says about 1,700"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-2 1a.3: round 2's scratch cache (about 1,300 partitions, 2020-03 to 2026-10) is on this disk and is used, each partition verified.",
  "world_is": "The cache is on disk with 1,691 pre-2026 partitions. The count is a number in the premise, not a reading the replay depends on, because every partition is verified before use."
}
```

## ADVI_BDPRCE-D1-W14-S8 -- Nine unrelated Fixed Income funds read trade-to-market-value ratios of 1.0925 to 1.0931 on 2026-10-06, a common offset that points at the market-value field of that date rather than at the trades

```json
{
  "id": "ADVI_BDPRCE-D1-W14-S8",
  "project": "ADVI_BDPRCE",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_BDPRCE~14",
  "surfaced_at": "2026-10-14T03:26:07Z",
  "one_line": "On 2026-10-06 nine funds (COLUMBIA, FIDELITY ADVISOR, JPMORGAN CORE R6, MFS HIGH INCOME R6, PIMCO and VANGUARD ULTRA SHORT-TERM names among them) all withhold at ratios 1.0925 to 1.0931; a shared offset is the signature of a same-day market-value quirk, not of separate trade prices.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "REPLAY2.json@6a39e57498 withheld_assets: nine assets with dates 2026-10-06 and ratios 1.09259 to 1.09307",
      "REPLAY2.md@6a39e57498, section Par-quoted rows and the withheld band"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BP-c-2 0b: the 1 percent band withholds the funds whose ratio sits outside both bands; the withheld rows are quantified so the CTO can see what the band costs before any widening.",
  "world_is": "The band costs 442 Fixed Income trade rows on 25 assets. A cluster of nine unrelated funds at one ratio on one date suggests the corroborating ratio, not the trades, carries the offset. Not investigated; the list's classes are the rule's output as written."
}
```
