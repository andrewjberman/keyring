# ADVI_BDPRCE -- surprise channel, INVESTIGATION v1 (dell1 fabric)

**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate `.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`, identity, folder == project, the allocator coordinate). Lane `ANY`.
**Id grammar (dell1 fabric):** the gate requires the fabric coordinate on a dell1 row, so a worker's row is `ADVI_BDPRCE-D1-W<n>-S<k>`; this file's rows are minted by `0.9.0_WK_ADVI_BDPRCE~1` (D1, W1). The bare `ADVI_BDPRCE-W1-S<k>` form in the order is refused by `.tools/surprise-row-gate.py` for fabric dell1 (row S7 records it).
**Append-only.** Never edit an existing row.
**This file opened by** `0.9.0_WK_ADVI_BDPRCE~1` under task order `ADVI_BDPRCE.TO-BP-a-1.writers-census` (round 1, issued by `2.0.0_SA_COO~K1`). Denominator at this write: **7 rows** (`S1`..`S7`).

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
