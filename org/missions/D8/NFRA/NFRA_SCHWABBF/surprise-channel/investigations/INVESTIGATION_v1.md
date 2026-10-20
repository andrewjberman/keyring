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
    "id": "NFRA_SCHWABBF-W3-S3",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~3",
    "surfaced_at": "2026-10-20T15:37:01Z",
    "one_line": "With the post-run guard reading the firm prefix only, a legacy-only own file that the resumability index correctly skips is absent from the guard's listing, so the run counts it as a shortfall and exits 6 on every fire whose lookback window plans that file, until the migration copies it to the firm form.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1 at worktree wk-NFRA_SCHWABBF-3 (uncommitted at filing): the pre-loop index lists the legacy master folder ($LEGACYROOT) through Get-ResumeNames, so the download loop skips a legacy-only own file",
        "same file: the post-run guard lists only the firm prefix ($PREFIX) through Get-LandedIndex, and Get-LandingGuardVerdict counts every planned name absent from that index as shortfall; Die 6 fires on guard.ok false with zero download failures",
        "data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py test_landing_guard_resumability_counts_legacy_only_own_file asserts the skip arm only; no test asserts the guard arm for a legacy-only file"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-w2 build step 2 and measured effects: the resumability index must still count the OLD master-form prefix so a not-yet-copied file is skipped, not re-pulled; and the post-run guard reads the NEW prefix only.",
    "world_is": "Both clauses hold in the built script, and together they make a not-yet-copied legacy-only own file a guard shortfall: the run exits 6 (LANDING GUARD FAILED) with zero download failures. The round-1 row NFRA_SCHWABBF-W2-S3 says the skip is correct, which holds for the download loop, not for the guard. Not exercised against S3 (WORLD floor); the consequence follows from the code read at the cited lines.",
    "notes": "Recorded for the issuer, not resolved by the worker: whether the guard should also accept a legacy-form copy during the copy-to-delete window, or the migration copies every legacy object before the puller is deployed, is the issuer's decision. The guard was NOT relaxed to pass this case; the spec's new-prefix-only rule is built as written."
  },
  {
    "id": "NFRA_SCHWABBF-W4-S4",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~4",
    "surfaced_at": "2026-10-20T15:36:55Z",
    "one_line": "The TO-BF-t2 worker face reads a sibling master's file in the shared firm partition as NOT-HELD for this master, but the round-1 rule for a day with silver present and this master's bronze absent is THREAD-FAIL; the worker kept the round-1 rule and named the sibling case NOT-HELD only when silver is also absent.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/canonical/schwab/keyform/thread_trace.py at worktree branch wk-NFRA_SCHWABBF-4 (base 87d44e203b): trace() sets cause=other-master-only only on the NOT-HELD branch, which requires silver absent; silver present with no bronze for this master falls to THREAD-FAIL reason=bronze-not-held-form-*",
        "data/canonical/schwab/tests/test_thread_trace.py::test_sibling_file_does_not_count_as_this_masters_bronze_when_silver_is_present asserts rc 1 and no THREAD-OK for that case; test_shared_partition_holding_only_a_sibling_is_not_held_for_this_master asserts rc 2 cause=other-master-only with silver absent",
        "data/canonical/schwab/tests/test_thread_trace.py::test_silver_present_without_bronze_is_a_failure_not_an_absence (round-1 test, kept unchanged in intent) asserts rc 1 for silver present and no bronze"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-t2 build step 2: 'A day where ANOTHER master's file is in the firm partition but not this master's is NOT-HELD for this master (name the cause cause=other-master-only when silver is also absent).' Step 2 also keeps the typed absence unchanged.",
    "world_is": "The sentence names NOT-HELD for the sibling-only day in general and places the cause name only on the silver-absent branch; the round-1 rule (silver present without this master's bronze is a failure, not an absence) is kept in code, so a sibling-only day with silver present reads THREAD-FAIL, not NOT-HELD. The issuer should confirm which reading governs the silver-present branch.",
    "notes": "Not an alert and not a monitor. The silver-absent case, the one the real 2026-10-17 probe exercises, is NOT-HELD cause=no-bronze-no-silver on the real store; the sibling-only case is covered on the fake store only."
  },
  {
    "id": "NFRA_SCHWABBF-W4-S5",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~4",
    "surfaced_at": "2026-10-20T15:36:55Z",
    "one_line": "The TO-BF-t2 order fixes 'both forms -> FAIL naming the second form' without naming a --form; the worker applied it to --form builder (the CLI default) and kept the round-1 rule that --form any accepts either layout and reports the second form on its hop.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/canonical/schwab/keyform/thread_trace.py at worktree branch wk-NFRA_SCHWABBF-4 (base 87d44e203b): the problems list keeps 'if second_n > 0 and form != \"any\"', and main() defaults --form to builder",
        "data/canonical/schwab/tests/test_thread_trace.py::test_both_forms_under_builder_form_fails_naming_the_second_form asserts rc 1 and second-form-found-legacy; test_both_forms_under_any_form_is_ok_and_reports_the_second_form asserts rc 0 with HOP second-form FOUND n=1"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-t2 build step 1: 'Under --form builder a found second form still makes the verdict FAIL.' Test list: 'both forms -> FAIL naming the second form' (no --form named).",
    "world_is": "Only the builder form is pinned to FAIL on a second form; under --form any a both-forms day passes and names the second form on its hop. FWD-4 forbids a day stored two ways, so the issuer should say whether --form any must also FAIL on both forms.",
    "notes": "Not an alert and not a monitor. The real 2026-10-16 probe under --form any reports HOP second-form NONE, so this choice does not change any criterion's output."
  },
  {
    "id": "NFRA_SCHWABBF-W6-S1",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~6",
    "surfaced_at": "2026-10-20T15:39:04Z",
    "one_line": "The schwab converter's silver WRITE grant names only the three master scopes, while the converter's scope function returns the first folder segment of a new-form key (49financial, cottonwood); whether its silver output follows that segment is not traced in TO-BF-i2, so a firm-folder event may be denied on the silver write.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/opal-assets/silver.tf:191-200 at 87d44e203b (silver_source_scopes.schwab = 08242234, 08335338, 08403355) and :370-422 (silver_write_per_source: PutObject/GetObject/ListBucket on schwab/{scope}/silver|meta/* for those scopes only)",
        "data/assets/scripts/silver/schwab_conversion.py:133-143 at 87d44e203b (scope_from_key returns parts[1] for a schwab/ key, i.e. 49financial or cottonwood for the new key form)",
        "silver.tf (this worktree, BF-i-2 edit): silver_read_schwab_firm_prefix adds READ ONLY on schwab/49financial/bronze/* and schwab/cottonwood/bronze/*; silver_source_scopes is not widened"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO NFRA_SCHWABBF.TO-BF-i2 step 3: the converter's firm-prefix grant is a minimal READ; the cell names no silver-tier write for the firm folders.",
    "world_is": "The converter's silver write grant covers schwab/{08242234,08335338,08403355}/silver|meta/* only. Output keying on the firm segment is unverified here: the cell read the grant, not the converter's output-key construction. If keyed on the segment, the first firm-key event would AccessDenied on silver PutObject (loud, to the DLQ), not corrupt data.",
    "notes": "Not widened in this cell (the TO says minimal read). Options for the issuer: confirm BF-c-2's output key (master from the file name) before the cutover, or grant silver/meta write on the firm scopes as its own never-widen edit. Not an alert and not a monitor."
  },
  {
    "id": "NFRA_SCHWABBF-W6-S2",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~6",
    "surfaced_at": "2026-10-20T15:39:04Z",
    "one_line": "The box role's run-manifest (_ops) and pull-manifest (meta/pulls) PutObject grants enumerate the three old masters only, so a manifest written under a firm-folder master would be denied; TO-BF-i2 scopes the new grant to bronze, so these two are not covered.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/canonical-schwab-ec2/monolith-iam.tf at 87d44e203b, statements MonolithSchwabOpsWrite (schwab/{08242234,08335338,08403355}/_ops/*) and MonolithSchwabMetaPullsWrite (schwab/{08242234,08335338,08403355}/meta/pulls/*); the file's own comment (lines 88-89) says the puller WARNs, not silently, if the manifest write AccessDenies",
        "infra/aws/terraform/canonical-schwab-ec2/monolith-iam.tf (this worktree): MonolithSchwabWrite gains the three 49financial per-master bronze entries; no _ops or meta/pulls entry is added"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO NFRA_SCHWABBF.TO-BF-i2 step 1: ADD per-master bronze write entries for the 49financial firm folder; the cell names no other statement.",
    "world_is": "The puller's manifest home for a firm-folder master is not traced in this cell. If it writes schwab/49financial/_ops/ or schwab/49financial/meta/pulls/, those PutObjects AccessDeny; the puller's WARN makes the denial visible.",
    "notes": "Not an alert and not a monitor. The issuer decides whether the firm folder needs _ops and meta/pulls grants (enumerated per master, as the cell did for bronze)."
  },
  {
    "id": "NFRA_SCHWABBF-W13-S1",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~13",
    "surfaced_at": "2026-10-20T16:16:58Z",
    "one_line": "The order names the Cottonwood Schwab masters as the masters field of the registry rows whose firm is cottonwood and vendor is schwab; in scopes.json that field sits on the cottonwood FIRM row, while the schwab master rows carry only key, so the worker read the four masters from the MASTER rows' key.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/logic/registry/scopes.json@ae487c67689 rows key 08719286, 08134043, 08165601, 08480305: class MASTER, firm cottonwood, vendor schwab (the four Cottonwood Schwab masters; no masters field on these rows)",
        "infra/logic/registry/scopes.json@ae487c67689 row key cottonwood: class FIRM, masters [z09, 08719286, 08134043, 08165601, 08480305] (z09 is vendor blackdiamond, excluded by the vendor filter)",
        "data/canonical/schwab/tests/test_alongside_puller.py master_set test reads the MASTER rows key; the set equals the FIRM row masters less z09 (both sets are the same four ids)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO NFRA_SCHWABBF.TO-AL-p1 MASTER SET: the ValidateSet of the copy equals the masters of the registry rows in infra/logic/registry/scopes.json whose firm is cottonwood and vendor is schwab, both ways.",
    "world_is": "The four Cottonwood Schwab masters are the MASTER-class rows with firm cottonwood and vendor schwab (key = master id). The masters list the order names is held on the cottonwood FIRM row and includes z09, a Black Diamond master. The set is identical either way (08719286, 08134043, 08165601, 08480305), so the check grades the same four ids.",
    "notes": "Form only: the registry holds the same four ids under two shapes. No change to scopes.json is proposed by this row."
  },
  {
    "id": "NFRA_SCHWABBF-W13-S2",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~13",
    "surfaced_at": "2026-10-20T16:16:58Z",
    "one_line": "The worktree's sparse checkout excludes org/surprise_channel from disk while the folder is tracked at HEAD, so the row schema the worker rules name (org/surprise_channel/schemas/investigation_item.schema.json) is readable only through git show, not as a file.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git config core.sparseCheckout in C:/Users/AndrewBerman/Desktop/wt-al-13 prints true; git ls-files -- org/surprise_channel lists 43 tracked files at ae487c67689",
        "ls org/surprise_channel in C:/Users/AndrewBerman/Desktop/wt-al-13 returns no such file; git status --short -- org/surprise_channel is empty (no deletions shown)",
        "git ls-tree HEAD org/surprise_channel/schemas/investigation_item.schema.json returns blob 696468806e9e8163a32b71c65d18d3a98ca318c2; git show of that path succeeds"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker surprise-row rule: a row is written per org/surprise_channel/schemas/investigation_item.schema.json, and the row gate reads the channel at the worktree.",
    "world_is": "The schema and the rest of the channel are tracked but not on disk in this worktree. The worker read the schema with git show and did not widen the sparse checkout or reconstruct the folder, which the order forbids. Whether the row gate finds its schema from this worktree is not measured here.",
    "notes": "Form only. The gate run at commit is the measurement that answers the open half."
  },
  {
    "id": "NFRA_SCHWABBF-W13-S3",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~13",
    "surfaced_at": "2026-10-20T16:21:17Z",
    "one_line": "The worktree's sparse-checkout cone omits infra/aws/ec2/alongside-schwab-si2, the granted path of the Alongside copy, so git cannot track or stage the copy and safe-commit refuses it; the order's flip to complete cannot be committed from this worktree.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git sparse-checkout list in C:/Users/AndrewBerman/Desktop/wt-al-13 at ae487c67689 lists .tools, data/canonical/schwab/tests, infra/aws/ec2/canonical-schwab-si2, infra/logic, lib, org/devices, org/missions/D8/NFRA/NFRA_SCHWABBF, org/modules/graph, org/ref, org/standards; infra/aws/ec2/alongside-schwab-si2 is absent (grep -c alongside prints 0)",
        "git ls-files -- infra/aws/ec2/alongside-schwab-si2 prints 0 tracked files; the copy at that path is untracked on disk",
        "bash .tools/safe-commit.sh -F ... -- infra/aws/ec2/alongside-schwab-si2/sdd-daily-pull.ps1 ... returned 'error: pathspec ... did not match any file(s) known to git' and committed nothing (rc=1); the surprise-row gate ran OK on this file"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO NFRA_SCHWABBF.TO-AL-p1 FIRST ACT: if the worktree does not carry the paths the task order names, that is a BLOCKING row and the worker stops; the order's <paths> block names infra/aws/ec2/alongside-schwab-si2/sdd-daily-pull.ps1 as the write grant.",
    "world_is": "The worktree carries the copy's tracked-parent folder only as an excluded cone path, so the grant path is not addressable to git here. The copy (698 lines, two named changes at lines 1-2 and 37) and the test pass on disk (AC1 5 passed rc=0; AC2 COPY-DIFF-OK changed_non_comment_lines=1 rc=0) but are NOT committed. The worker did not change the sparse cone, did not git add, and did not reconstruct the tree; the order's flip to complete is withheld.",
    "notes": "The cone change or a re-cut of the worktree is the COO's or the lane owner's act; a worker does not widen its own checkout. The on-disk copy is unchanged and is the input to the commit once the path is addressable."
  }
]
```
