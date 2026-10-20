# NFRA_SCHWABBF -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `2.0.0_SA_COO~SB` at the L5 cut (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`).
Lane `ANY`.
**Id grammar:** a worker's row is `NFRA_SCHWABBF-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that coordinate); a
seat's row is `NFRA_SCHWABBF-S<k>`; the CVO's adjudication rows live in `../adjudications/` as `NFRA_SCHWABBF-C-S<k>`.
**Append-only during the round.** Never edit an existing row.

```json
[
  {
    "id": "NFRA_SCHWABBF-S1",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~SB",
    "surfaced_at": "2026-10-20T13:45:00Z",
    "one_line": "The monolith's S3 notification invokes the silver converter Lambda for every ObjectCreated under schwab/<master>/bronze/ with suffix .zip, so the server-side copy of the ~21,782 stored Schwab objects to the builder's key form will re-convert every moved day, which the PRD's C-MOVE does not name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~SB (release act R1 names the fan-out as blast radius in the never-widen pair; R3 prints the event count; R6's compare is the check that the re-conversion changed nothing)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/opal-assets/silver.tf:242-244 (rules schwab-08242234, schwab-08335338, schwab-08403355: prefix schwab/<m>/bronze/, suffix .zip) and :769-780 (one lambda_function block per rule, events s3:ObjectCreated:*), read at HEAD ed7d0dc3db 2026-10-20",
        "data/assets/scripts/silver/schwab_conversion.py:133-197 (scope_from_key reads segment 1; feed_from_key and date_from_key read the FILE NAME), so a new-form key is accepted and the same silver partitions are rewritten",
        "infra/aws/terraform/opal-assets/monolith.tf:142-147 and :194-227 (versioning Enabled, no noncurrent expiry): a later delete of the old keys writes delete markers and keeps every version"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C-MOVE: copy every stored object to its builder key, verify by count and sha, then deploy readers and run FWD-5's equality read; it names no consequence of the copy for the silver tier.",
    "world_is": "The copy is an ObjectCreated event for every object, so about 21,782 silver converter invocations follow it; the converter derives master from path segment 1 and type and date from the file name and so writes the same silver partitions again. Whether those rewrites are byte-identical is unmeasured (the cutover's compare answers it).",
    "notes": "Inlined into TO-BF-m1 (the plan prints the event count) and into the decomposition battery (comp-adversary finding 1). Not an alert and not a monitor: a one-time count at a dry run."
  },
  {
    "id": "NFRA_SCHWABBF-W2-S1",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~2",
    "surfaced_at": "2026-10-20T14:04:58Z",
    "one_line": "The puller's DENOMINATOR check compares the download tally with the full enumeration, so a one-day -OnlyAsOf run would raise exit 5 after landing its day; the check now subtracts the files the filter deliberately excluded and logs both counts.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1@5f1ad506a4 lines 499-503 (base): accounted -ne ENUMERATED raises Die 5 'DENOMINATOR MISMATCH'; the one-day filter (task order step 3) makes the plan a subset of ENUMERATED, so accounted = in-day files only",
        "infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1 (worktree, new): Select-PlanAsOf returns excluded; inScope = ENUMERATED - FILTERED_OUT; the Die 5 test is accounted -ne inScope",
        "data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py::test_only_asof_keeps_exactly_one_day asserts excluded == 4 of 5 for the one-day plan"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-w1 step 3: -OnlyAsOf keeps only the files whose date equals that day, zero kept dies 9, empty is today's behavior exactly. It names no change to the denominator check that follows the download loop.",
    "world_is": "Without the subtraction the one-day run downloads its day and then fails the denominator (enumerated=N, accounted=day-files) with exit 5, so the scheduled exit code would read as a failure of a correct backfill. With the subtraction the check is in-scope = enumerated less excluded, and a vanished file still raises. The ENUMERATED-based check is unchanged for an empty -OnlyAsOf.",
    "notes": "A deliberate consequence of the filter, not a new behavior: the count of other-day files is printed beside the in-scope count on every run (out-of-day=)."
  },
  {
    "id": "NFRA_SCHWABBF-W2-S2",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~2",
    "surfaced_at": "2026-10-20T14:04:58Z",
    "one_line": "The post-run landed index was built by inline code in the main flow, which no test can call, so it is now the pure function Get-LandedIndex and the main flow calls it; the guard function itself never split a key.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1@5f1ad506a4 lines 83-132 (Get-LandingGuardVerdict): takes a prebuilt filename -> type/yyyyMMdd hashtable and does not split keys; lines 510-525 (base): the segment split lives in the main flow",
        "infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1 (worktree): Get-LandedIndex is the same split with the date= token converted back; the main flow calls it at the post-run guard"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-w1 BF-w-1 step 2 names the post-run guard's by-position split (lines 506-526) as the place that must change; the test criterion requires a landed index 'built the way the script builds it' from sample s3 ls lines.",
    "world_is": "The guard's split was inline in the main flow and not AST-extractable, so the 'built the way the script builds it' requirement could not be met without moving the split into a named function. The moved function has the same regex and the same segment logic plus the date= conversion; the verdict function is unchanged.",
    "notes": "Behavior of the landed index for the staging form is unchanged (its token passes through)."
  },
  {
    "id": "NFRA_SCHWABBF-W2-S3",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~2",
    "surfaced_at": "2026-10-20T14:04:58Z",
    "one_line": "During the copy-to-delete window the pre-loop resumability index keys on the file name, so a file present only in the legacy yyyyMMdd form is skipped and its date= form is never written by the scheduled pull; that copy has to come from the migration, not the puller.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1 (worktree) pre-loop index: $landed[filename] from aws s3 ls under schwab/<master>/bronze/ (layout-agnostic, as the task order required)",
        "infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1 (worktree) download loop: if landed.ContainsKey(filename) then skip, before any key is built"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-w1 BF-w-1 step 2: the landed index keys on the file name and must count BOTH forms during the copy-to-delete window.",
    "world_is": "Counting both forms is what the order asked for, and it means a legacy-only file is treated as already landed. The puller therefore does not write the date= key for a day already in the legacy form. Whether the migration's copy covers every legacy object before the old keys are deleted is the migration's question (PRD C-MOVE), not measured here.",
    "notes": "Stated so the cutover does not assume the scheduled puller back-fills the date= form of an old-form object. No code change: the skip is correct once the copy completes."
  },
  {
    "id": "NFRA_SCHWABBF-W2-S4",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~2",
    "surfaced_at": "2026-10-20T14:04:58Z",
    "one_line": "This sparse worktree carries neither org/surprise_channel/schemas/investigation_item.schema.json nor the task order's deliverables folder, so the new rows could not be checked against the schema by reading it and the deliverables folder was created new.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Read of C:\\Users\\AndrewBerman\\Desktop\\wt-bf-2\\org\\surprise_channel\\schemas\\investigation_item.schema.json: does not exist (sparse checkout); ls of org/surprise_channel/schemas/ returns no such directory",
        "ls of org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables in the worktree returned no such directory before this order's work"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The worker face says every surprise row is per org/surprise_channel/schemas/investigation_item.schema.json and names the deliverables folder as a grant; the order says all files named exist in the sparse worktree.",
    "world_is": "The schema path and the deliverables folder are absent in this worktree. Rows here follow the field set of the existing rows in the investigation file; the commit-time surprise-row gate is the enforcer of the schema form.",
    "notes": "Not an alert. The gate at commit (.tools/surprise-row-gate.py) reads its schema from the staged tree; its verdict is recorded in the commit report."
  },
  {
    "id": "NFRA_SCHWABBF-W4-S1",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~4",
    "surfaced_at": "2026-10-20T14:09:00Z",
    "one_line": "The order names exit codes 0, 1 and 2 only; thread_trace.py exits 3 for a store read failure, bad input and an argparse usage error, so rc 2 is only ever the typed NOT-HELD absence.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "not applicable (INERT)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/canonical/schwab/keyform/thread_trace.py main() at a620a5a34c: argparse SystemExit returns RC_ERROR (3); bad --master or --day returns RC_ERROR; any store exception returns RC_ERROR with ERROR: store-read <class>",
        "data/canonical/schwab/keyform/thread_trace.py trace() at a620a5a34c: RC_NOT_HELD (2) only when no bronze in either layout and no silver"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-t1 Build section item 4: exit 0 THREAD-OK, exit 1 THREAD-FAIL, exit 2 NOT-HELD; no code is named for an error or a usage fault.",
    "world_is": "An error path that kept rc 2 would be indistinguishable from the typed absence, so the tool uses rc 3 for errors. The choice is recorded here for the issuer to ratify or change; the tests pin rc 3 for store, day and usage faults."
  },
  {
    "id": "NFRA_SCHWABBF-W4-S2",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~4",
    "surfaced_at": "2026-10-20T14:09:00Z",
    "one_line": "The row form the worker face names, org/surprise_channel/schemas/investigation_item.schema.json, is in the HEAD tree but not materialised in this sparse worktree, so this row copies the field set of NFRA_SCHWABBF-W4-S1 rather than reading the schema.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "not applicable (INERT)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git ls-tree HEAD org/surprise_channel/schemas/ on branch wk-NFRA_SCHWABBF-4 at 5f1ad506a4: investigation_item.schema.json blob 696468806e9e8163a32b71c65d18d3a98ca318c2 is present",
        "ls org/surprise_channel/schemas/ in worktree wt-bf-4 at 2026-10-20T14:08Z: no such directory; the worktree is a sparse checkout"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker face: the investigation row is written per org/surprise_channel/schemas/investigation_item.schema.json, which the worker reads in its worktree.",
    "world_is": "The schema is reachable by git show from HEAD but not by a path read in this worktree; the row shape is unverified against the schema until the surprise-row gate runs at commit."
  },
  {
    "id": "NFRA_SCHWABBF-W4-S3",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~4",
    "surfaced_at": "2026-10-20T14:09:00Z",
    "one_line": "The order names the old-layout partition schwab/M/bronze/acc/YYYYMMDD/ without a bucket; thread_trace.py reads it in the bucket the builder returns for the bronze address, which is opal-data-assets for 08403355.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "not applicable (INERT)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "AC2 run at a620a5a34c: HOP bronze line HELD n=1 prefix=s3://opal-data-assets/schwab/08403355/bronze/acc/20261016 form=legacy",
        "read-only aws s3 ls of s3://opal-data-assets/schwab/08403355/bronze/acc/20261016/ at 2026-10-20: one object"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-t1 trace item 2: the second form is the old-layout partition schwab/M/bronze/acc/YYYYMMDD/ for the same day, with no bucket named.",
    "world_is": "Only opal-data-assets was listed. Whether another bucket holds an old-layout copy of the same day is not measured by this order; a copy elsewhere would not be seen by the trace."
  },
  {
    "id": "NFRA_SCHWABBF-W3-S1",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~3",
    "surfaced_at": "2026-10-20T14:03:37Z",
    "one_line": "On the real dim_balance partition for 0840 on 2026-10-16 all 40 columns are non-numeric, so the equality capture records an empty numeric_sums and the content_sha256 field is the only check on figure values for silver tables read this way.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED: live read-only capture (AC2, rc 0, CAPTURED cells=1 missing=0) written to C:/Users/AndrewBerman/AppData/Local/Temp/bf_e1_capture_probe.json at worktree branch wk-NFRA_SCHWABBF-3; cells[0].columns lists 40 names and cells[0].numeric_sums is empty",
        "data/canonical/schwab/silver/_canonical_silver_lib.py:125 at worktree HEAD (read_schwab_raw returns values as string; dtype standardization is the caller's typed step)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO BF-e1 / C-EQUAL: capture records numeric_sums{col: float} for the figures of each cell, and compare reports a changed numeric cell as field=numeric_sums.",
    "world_is": "The silver partition s3://opal-data-assets/schwab/08403355/silver/dim_balance/date=2026-10-16/data.parquet holds 30 rows and 40 columns, none numeric-typed on read, so numeric_sums is {}. A figure change in any column still moves content_sha256, so the compare is not blind; the numeric_sums arm is inert for this table.",
    "notes": "Recorded, not worked around: the instrument follows the cell text and does not parse strings into floats. Whether the issuer wants a typed numeric pass for the figure check is the issuer's decision."
  },
  {
    "id": "NFRA_SCHWABBF-W3-S2",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~3",
    "surfaced_at": "2026-10-20T14:03:37Z",
    "one_line": "The equality cell hashes every column of a silver partition, including the provenance columns _source_file, _source_as_of and _master_observed, so a rebuilt day whose figures are unchanged but whose provenance names the moved bronze key would read as a DIFF.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED: the captured dim_balance cell at C:/Users/AndrewBerman/AppData/Local/Temp/bf_e1_capture_probe.json lists _source_file, _source_as_of and _master_observed among its 40 columns, and content_sha256 is computed over all of them (data/canonical/schwab/keyform/equal_sample.py _content_sha256 at worktree HEAD)",
        "data/canonical/schwab/silver/build_fact_position.py:15 at worktree HEAD (provenance columns _source_file, source_as_of, schema_version are declared deterministic, idempotency #6)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO BF-e1 / C-EQUAL: content_sha256 is the sha256 of the rows, and compare reports a difference where a figure for an already stored day differs (FWD-5 ACCEPT).",
    "world_is": "content_sha256 covers every column, provenance included, so the compare cannot separate a provenance-only rewrite from a figure change. Whether the rebuilt bytes differ in provenance is unmeasured; the cutover's compare after the move answers it. The instrument follows the spec and excludes no column.",
    "notes": "Recorded for the issuer: whether provenance columns are in scope of the equality check is the issuer's decision, not the worker's."
  },
  {
    "id": "NFRA_SCHWABBF-W1-S1",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~1",
    "surfaced_at": "2026-10-20T14:02:05Z",
    "one_line": "The silver converter data/assets/scripts/silver/schwab_conversion.py cannot be loaded by path from its own directory: its bare-name import of stream_parquet fails, so the converter seam probe of TO-BF-k1 (AC2) cannot run against the real neighbor as the order specifies.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/assets/scripts/silver/schwab_conversion.py:66 is the bare-name import 'import stream_parquet as sp' at HEAD 5f1ad506a4 (worktree C:/Users/AndrewBerman/Desktop/wt-bf-1)",
        "git ls-files at HEAD 5f1ad506a4: stream_parquet.py is tracked at data/assets/scripts/lib/stream_parquet.py and at infra/aws/lambda/opal-assets/opal-assets-silver-schwab/stream_parquet.py; no copy sits beside data/assets/scripts/silver/schwab_conversion.py",
        "python -m pytest data/canonical/schwab/tests/test_bronze_key_form.py -q -p no:cacheprovider --color=no: '1 failed, 242 passed in 3.29s'; the failure is 'ModuleNotFoundError: No module named stream_parquet' raised at data/assets/scripts/silver/schwab_conversion.py:66"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-k1 AC2 and the worker face: import data/assets/scripts/silver/schwab_conversion.py by path and assert that scope_from_key, feed_from_key and date_from_key read a new-form key built by monolith_bronze_key (the seam probe against the REAL neighbor). The order presents the converter's file set as loadable from its source directory.",
    "world_is": "The six key functions and the other 242 test cases pass at HEAD 5f1ad506a4 plus the BF-k-1 edits. Only the seam case fails, because the converter's sibling stream_parquet is not beside the source file; the sibling is tracked in data/assets/scripts/lib/ and packaged beside the Lambda copy. Nothing was patched: the refusal clause forbids a fallback that weakens the probe, and the converter is read-only for this cell.",
    "notes": "Options for the issuer, not taken by the worker: put data/assets/scripts/lib on the probe's sys.path (a test-harness edit inside the BF-k-1 write grant, no assertion weakened), or name the Lambda package directory as the seam neighbor. Not an alert and not a monitor."
  },
  {
    "id": "NFRA_SCHWABBF-W2-S5",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~2",
    "surfaced_at": "2026-10-20T15:46:52Z",
    "one_line": "TO-BF-m2 dry run: AC1 and AC3 PASS at base, though the order says all three must FAIL before any change. The round-1 move tool already imports the firm-form key contract (TO-BF-k2), so it prints firm-form destinations and the round-1 assertions still hold.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/canonical/schwab/keyform/move_bronze_key_form.py@264023be84 loads the key contract by path from data/canonical/schwab/silver/_canonical_silver_lib.py, which is the firm-form library at 60781d2d86 (TO-BF-k2)",
        "python -m pytest data/canonical/schwab/tests/test_move_bronze_key_form.py -q -p no:cacheprovider --color=no at 264023be84: '13 passed in 1.25s' (rc=0); the order predicts FAIL at base",
        "python data/canonical/schwab/keyform/move_bronze_key_form.py plan --master 08403355 --type acc at 264023be84: 'MOVE-PLAN in_scope=516 foreign=0 copy=516 already=0 events=516' (rc=0); AC3's regex '^MOVE-PLAN in_scope=[0-9]+ foreign=0 copy=[0-9]+ already=[0-9]+ events=[0-9]+' matches it at base"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-m2 worker face, dry-run paragraph: 'Run all three first and record what they print; they must FAIL before you change anything', and 'after TO-BF-z2 and TO-BF-k2 the library is firm-form, so the old tool's import and its master-form destination assertions fail'.",
    "world_is": "AC1 and AC3 PASS at base; AC2 FAILS as expected (no MOVE-SAMPLE line). The base tool emits firm-form destinations because it imports the k2 library, and its round-1 test assertions (dst starts with schwab/, contains /date=, ends with the vendor name, events=12) hold on firm-form keys. AC3's regex does not name a destination, so it cannot tell the grammars apart. Nothing was patched before this row: the build is the rewrite the face specifies, and the criteria are judged on the rewritten tool and test.",
    "notes": "Not an alert and not a monitor. The rewrite replaces the round-1 assertions with firm-form ones (address() equality, guards, the MOVE-SAMPLE line), so AC1 discriminates after the change. AC3's regex is not changed by this cell; the issuer may decide whether the AC3 regex should name the destination."
  },
  {
    "id": "NFRA_SCHWABBF-W2-S6",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~2",
    "surfaced_at": "2026-10-20T16:04:31Z",
    "one_line": "TO-BF-r2 premise: the shared silver contract exports NO public all-dates lister. The two readers that need every date (build_canonical_daily.py and build_fact_tax_1099div.py) import the PRIVATE _bronze_dates_or_refuse from _canonical_silver_lib.py, because the order's named list_bronze_dates exists only in the bd-tree mirror.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/canonical/schwab/silver/_canonical_silver_lib.py@60781d2d86 defines _bronze_dates_or_refuse (line 203) and latest_bronze_date (line 221); no public list_bronze_dates in that file (grep '^def ' shows none)",
        "data/black_diamond/scripts/bronze/_monolith_bronze.py@60781d2d86 is the file that exports list_bronze_dates",
        "data/canonical/schwab/build_canonical_daily.py at 2dc375853a1 is the reader that needs every date (_monolith_partitions); it now imports _bronze_dates_or_refuse by name, with a comment"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-r2 worker face, 'What exists': the shared function is TO-BF-k2's, and list_bronze_dates / latest_bronze_date return compact YYYYMMDD strings for ONE master. 'If a name you need is private, say so in your report; do not edit that file.' Bounds: 'If a reader needs a function the shared contract lacks, stop and file a surprise row.'",
    "world_is": "The silver contract has latest_bronze_date (public, latest date only) and _bronze_dates_or_refuse (private, all dates). Both readers use the private all-dates function by name; _canonical_silver_lib.py was not edited. The private import is reported in the TO-BF-r2 worker report. Nothing was patched in the shared file.",
    "notes": "Not an alert and not a monitor. The issuer may decide whether the silver contract should export a public all-dates lister (a TO-BF-k2 amendment); this cell did not change that file."
  },
  {
    "id": "NFRA_SCHWABBF-W2-S7",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~2",
    "surfaced_at": "2026-10-20T16:04:31Z",
    "one_line": "The RPS date axis (build_canonical_daily.py) no longer lists the ~719 2023-2024 partitions whose only object carries a broken name (CRS{d8}.{FEED}, no master prefix), because the firm-form listing filters by master name. The order said the same days stay unchanged; this set of days changes for those partitions.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/canonical/schwab/build_canonical_daily.py@HEAD 2dc375853a1 (before this cell): _monolith_partitions enumerated 8-digit DIRECTORY names under schwab/08335338/bronze/rps/ (MONOLITH_FEED_PREFIX at line 63), so a broken-name partition still appeared on the axis",
        "data/canonical/schwab/tests/test_canonical_daily_date_axis.py (this cell): test_broken_name_partition_is_not_on_the_firm_axis asserts the broken-name day is absent; the mutant that drops the master filter fails it (3 failed, 14 passed on the mutant)",
        "data/canonical/schwab/silver/_canonical_silver_lib.py@60781d2d86 _scan_bronze_partitions: a key whose file name does not start with '{master}.' is skipped"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-r2 worker face, Build 1: 'For the same set of days the output and the latest selection are unchanged.' Also the TO-BF-k2 contract: the listers keep only keys whose file name starts with {master}.",
    "world_is": "The daily axis now excludes partitions whose only object is broken-name (for the 0833 RPS feed, 2023-2024). Those days were already unreadable through monolith_bronze_key. A full or --force rebuild that reaches them through this function will no longer see them. No object was moved, renamed or deleted; bronze stays immutable (Rule 17a).",
    "notes": "Not an alert and not a monitor. The remedy for the broken names is the re-land/alias ruling named in the old note; this cell did not decide it. The issuer may want the count of broken-name partitions printed at the next release act."
  }
]
```
