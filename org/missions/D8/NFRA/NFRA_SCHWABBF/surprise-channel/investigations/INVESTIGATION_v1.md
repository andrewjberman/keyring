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
  },
  {
    "id": "NFRA_SCHWABBF-W5-S1",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~5",
    "surfaced_at": "2026-10-20T15:40:29Z",
    "one_line": "The task order says BUILD_MANIFEST.json names the generator that rebuilds the twin, but the manifest names none: it declares the vendored source paths and says FLAT at zip root, so the twin was refreshed by a flat copy of the source file and the manifest needed no edit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/opal-assets/opal-assets-silver-schwab/BUILD_MANIFEST.json at worktree HEAD 87d44e203b: keys function, vendored_modules, vendoring, layer_dependencies, memory_mb, timeout_s, sizing_basis, contract; no generator key and no hash",
        "comp-find 'vendored_modules' returned 2 hits (the manifest and the task order); comp-find 'BUILD_MANIFEST' hits .tools/check-lambda-layer-deps (reads sidecars, generates none) and .tools/safe_deploy_core.py (comment only)",
        "infra/aws/lambda/ci/function-map/opal-assets-silver-schwab.json at HEAD lists the 12 files the zip is built from, from source_dir; the builder is infra/aws/lambda/ci/build-and-upload.sh at HEAD (not materialised in this sparse worktree)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-c2 Build step 2: read the manifest and the generator it names, and keep the twin and the manifest exactly as that generator would produce them.",
    "world_is": "No generator is named or found. The twin is byte-equal to the source after a flat copy (sha256 e2a23e1068 on both). The manifest lists the same source paths before and after, since no module was added, removed or renamed, so it is unchanged."
  },
  {
    "id": "NFRA_SCHWABBF-W5-S2",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~5",
    "surfaced_at": "2026-10-20T15:40:29Z",
    "one_line": "conversion_manifest._key_scope reads the master by the path-segment rule the converter had, so under the firm form it names the firm (49financial) for every firm-form key that reaches the closure lanes; the converter now reads the file name, but this sibling does not.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~SB (issuer; the fix belongs in data/assets/scripts/silver/conversion_manifest.py and its twin, both outside BF-c-2's grant)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/assets/scripts/silver/conversion_manifest.py:398-400 at worktree HEAD 87d44e203b: _key_scope returns parts[1] when parts[0] is schwab, else parts[0], the pre-change rule of scope_from_key",
        "infra/aws/lambda/opal-assets/opal-assets-silver-schwab/conversion_manifest.py:398-400 (twin, byte-identical rule)",
        "census of the vendored set by grep for parts[ and split(\"/\") over the twin directory: this is the only other position-based master read in the converter family besides set_identity_guard.py (row W5-S3); crs_reader.py, cs_reader.py, silver_registry.py and backfill_status.py hold no key-to-master read"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-c2 worker face: census the other vendored modules for parts[, split(\"/\") and scope_from_key; read-only unless it is the same bug, and if it is, change it only if its file is in the paths block, else file a row.",
    "world_is": "The same bug is present in conversion_manifest.py, whose file is not in this order's paths, so it is recorded here and not changed. It arms when a firm-form bronze key is written under schwab/49financial/ or schwab/cottonwood/ (the C-MOVE copy) and a closure is built over that lane."
  },
  {
    "id": "NFRA_SCHWABBF-W5-S3",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~5",
    "surfaced_at": "2026-10-20T15:40:29Z",
    "one_line": "set_identity_guard.parse_bronze_key requires parts[1] to equal the lane's master, so under the firm form every bronze key is dropped from the bronze census and the set-identity verdict for that lane reads its silver without bronze; it is outside this order's grant and unchanged.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~SB (issuer; the fix belongs in data/assets/scripts/silver/set_identity_guard.py and its twin, both outside BF-c-2's grant)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/assets/scripts/silver/set_identity_guard.py:63-70 at worktree HEAD 87d44e203b: parse_bronze_key(key, scope) returns None unless parts[1] == scope; parse_silver_key (lines 73-79) has the same test but silver keys stay per-master, so it is not armed by the firm form",
        "infra/aws/lambda/opal-assets/opal-assets-silver-schwab/set_identity_guard.py:63-70 (twin, same rule)",
        "data/assets/scripts/silver/set_identity_guard.py:81-108 guard_verdict(bronze_keys, silver_keys, scope) counts bronze only through parse_bronze_key, so a firm-form lane reads with an empty bronze side"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-c2 worker face: census the other vendored modules for parts[, split(\"/\") and scope_from_key and say what was found.",
    "world_is": "The census found the same position-based master test here. It is not in the paths block, so it is recorded and left as it is. It arms with the C-MOVE copy, as W5-S2 does."
  },
  {
    "id": "NFRA_SCHWABBF-W5-S4",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~5",
    "surfaced_at": "2026-10-20T15:40:29Z",
    "one_line": "The order's 'any other first or second segment RAISES' was read as: a staging first segment must be an 8-digit master and a schwab key's second segment an 8-digit master or a firm folder; the old code returned any staging first segment unchanged, so a non-master staging key now raises at scope_from_key.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/assets/scripts/silver/schwab_conversion.py scope_from_key at worktree (this change): raises ValueError for a first segment that is neither schwab nor [0-9]{8}, and for a second segment that is neither [0-9]{8} nor in FIRMS",
        "callers of scope_from_key found by census: schwab_conversion.py convert_object (bronze event key) and schwab_runtime.py:57 (r.key, bronze). Test suites test_schwab_runtime, test_schwab_conversion, test_schwab_projections and test_schwab_schemas pass after the change"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-c2 Build step 1: staging {master}/bronze/... maps to parts[0] (unchanged); any other first or second segment RAISES as it would have failed before.",
    "world_is": "The staging branch keeps returning parts[0] for an 8-digit master, unchanged. A non-master staging first segment now raises instead of returning a string that failed later. Whether the order meant the staging check to be a validation or a pass-through is the issuer's to confirm; no caller in the census passes such a key."
  },
  {
    "id": "NFRA_SCHWABBF-W5-S5",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~5",
    "surfaced_at": "2026-10-20T15:40:29Z",
    "one_line": "The schwab OPAL_BUILD_COMMIT pin in infra/aws/terraform/opal-assets/silver.tf names the commit whose package directory equals the deployed build; this change makes the package directory differ at schwab_conversion.py, so the pin is wrong for any build from this tree until the release act moves it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/opal-assets/silver.tf:75-100 at worktree HEAD 87d44e203b: the schwab pin is a literal that the comment says must name the commit the zip is built from, and the comment says a rebuild that does not move it leaves a precise but wrong pin",
        "this order builds and deploys nothing (WORLD floor); the twin now differs from the pinned commit at schwab_conversion.py only"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-c2 Bounds: the Terraform deploy of the new package is the issuer's release act; nothing is deployed here.",
    "world_is": "The pin is not touched by this order (silver.tf is outside the grant). The release act that deploys the new package moves OPAL_BUILD_COMMIT to the commit that carries it, per the comment's own rule."
  },
  {
    "id": "NFRA_SCHWABBF-W5-S6",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~5",
    "surfaced_at": "2026-10-20T15:40:29Z",
    "one_line": "The worktree's portal submodule pointer is already modified before any edit by this order (a48fa073c2 in HEAD, 97c66c9364 in the worktree); it is not staged or committed here.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git diff portal at wt-bf-5 (branch wk-NFRA_SCHWABBF-5): Subproject commit a48fa073c2... to 97c66c9364...; this order's commits name only the paths block"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-c2 Bounds: the grant is the paths block plus the deliverables folder and this order's file; nothing else is edited.",
    "world_is": "The submodule pointer differs in this sparse worktree; it is outside the grant and is left alone."
  },
  {
    "id": "NFRA_SCHWABBF-W5-S7",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~5",
    "surfaced_at": "2026-10-20T15:40:29Z",
    "one_line": "The code commit 0af3a73506 passed safe-commit rc 0 while two of its checks read nothing in this sparse worktree: the risk reflex answered PARTIAL_OR_BLIND on a stale danger map read from the main tree, and the naming gate printed NAMING ERROR for the missing function-map folder.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit output for commit 0af3a73506 on branch wk-NFRA_SCHWABBF-5: '[risk-reflex] ANSWER STATE: PARTIAL_OR_BLIND' with the danger map 115.8h old and 'scanned 0 of 3 file(s)'",
        "safe-commit output for commit 0af3a73506: '[naming-gate] NAMING ERROR function-map folder missing: ...wt-bf-5/infra/aws/lambda/ci/function-map/', then the commit reports 'committed 0af3a73506' with rc=0",
        "infra/aws/lambda/ci/function-map/ is not materialised in the sparse worktree (ls returns no such folder); the file exists at HEAD as infra/aws/lambda/ci/function-map/opal-assets-silver-schwab.json"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker rules: a commit passes .tools/safe-commit.sh; the commit-gate reports the checks it ran per file.",
    "world_is": "The commit-gate checks for the three .py files were clean (3 of 3). The risk reflex and naming gate did not grade this diff in this worktree, and the commit was not blocked by either. Their verdicts for this commit are therefore not evidence of a clean diff."
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
  },
  {
    "id": "NFRA_SCHWABBF-W11-S1",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~11",
    "surfaced_at": "2026-10-20T16:20:11Z",
    "one_line": "The worktree's sparse-checkout cone (11 entries, cut before the order's new folder existed) omits infra/aws/terraform/alongside-schwab-ec2/, so git refuses to index the granted new root and safe-commit refuses the commit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git sparse-checkout list in C:/Users/AndrewBerman/Desktop/wt-al-11 at base ae487c676890b37699a259e2f85c83871844c49c: .tools, data/canonical/schwab/tests, infra/aws/terraform/canonical-schwab-ec2, infra/aws/terraform/modules, infra/logic, lib, org/devices, org/missions/D8/NFRA/NFRA_SCHWABBF, org/modules/graph, org/ref, org/standards (no alongside-schwab-ec2 entry)",
        "git add -n infra/aws/terraform/alongside-schwab-ec2/main.tf: 'The following paths and/or pathspecs matched paths that exist outside of your sparse-checkout definition, so will not be updated in the index'; positive control git add -n infra/aws/terraform/canonical-schwab-ec2/main.tf prints nothing",
        "bash .tools/safe-commit.sh of the five new .tf paths and the test refused rc=1 with 'pathspec ... did not match any file(s) known to git'; git log -1 at the worktree still reads ae487c67689"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO NFRA_SCHWABBF.TO-AL-a1 <paths> names infra/aws/terraform/alongside-schwab-ec2/{main,masters,iam,secrets,box}.tf as the write grant, and the worker commits its granted files with safe-commit.sh.",
    "world_is": "The grant names the folder and the lane admits it, but the worktree's sparse cone does not, so the index refuses the path. The root is built and its test passes (13 passed). The worker adds only the granted folder to its own worktree's cone (git sparse-checkout add of that one path) so the commit can stage it; no other path is added and no tree is rebuilt.",
    "notes": "Plumbing, not a grant change: the write grant is unchanged. A lane that creates a new folder under a sparse parent needs that folder in the cone before the commit. Not an alert and not a monitor."
  },
  {
    "id": "NFRA_SCHWABBF-W12-S1",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~12",
    "surfaced_at": "2026-10-20T16:22:30Z",
    "one_line": "The granted folder infra/aws/ec2/alongside-schwab-si2/ is outside this worktree's sparse-checkout definition, so git refuses to stage the four deliverables there and the cell cannot commit them.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C C:/Users/AndrewBerman/Desktop/wt-al-12 sparse-checkout list (worktree branch wk-NFRA_SCHWABBF-12, cut from box/laptop at ae487c67689) lists .tools, data/canonical/schwab/tests, infra/aws/ec2/canonical-schwab-si2, infra/aws/terraform/canonical-schwab-ec2, infra/logic/registry, lib, org/devices, org/missions/D8/NFRA/NFRA_SCHWABBF, org/modules/graph, org/ref, org/standards; infra/aws/ec2/alongside-schwab-si2 is not among them",
        "git -C C:/Users/AndrewBerman/Desktop/wt-al-12 add --dry-run infra/aws/ec2/alongside-schwab-si2/keep-console.ps1 returned rc=1: 'matched paths that exist outside of your sparse-checkout definition, so will not be updated in the index'",
        "org/missions/D8/NFRA/NFRA_SCHWABBF/task-orders/NFRA_SCHWABBF.TO-AL-p1.alongside-box-puller-copy.md line 30 writes into the same folder, so the same block applies to the sibling cell AL-p-1"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO NFRA_SCHWABBF.TO-AL-e1 (worker face, first act and Bounds): the worktree must carry the granted paths; a granted path the worktree lacks is a BLOCKING row on that criterion, never an override. The write grant names infra/aws/ec2/alongside-schwab-si2/{keep-console.ps1,bootstrap.ps1,sdd-entitlements.ps1,RUNBOOK_ALONGSIDE_SITTING.md}.",
    "world_is": "The worktree's sparse set omits the new folder, so safe-commit cannot stage the scripts. The four files exist on disk and the pytest criteria pass against them on disk; nothing in the folder is committed. The worker did not change the sparse-checkout definition, because widening the worktree is the lane owner's call.",
    "notes": "Remedy for the lane owner, not applied by this worker: add the folder to this worktree's sparse definition (git sparse-checkout add infra/aws/ec2/alongside-schwab-si2) or re-cut the worktree with it, then commit with safe-commit. Untracked files on disk: infra/aws/ec2/alongside-schwab-si2/keep-console.ps1, bootstrap.ps1, sdd-entitlements.ps1, RUNBOOK_ALONGSIDE_SITTING.md. The test file data/canonical/schwab/tests/test_alongside_box_scripts.py is in a materialized path and is also untracked."
  },
  {
    "id": "NFRA_SCHWABBF-W12-S2",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~12",
    "surfaced_at": "2026-10-20T16:22:30Z",
    "one_line": "The order names sdd-harness.ps1 as the read-first reference for the UserMasters request and response, but no file of that name exists in this repo at any ref, so the entitlement request and response shapes are unverified.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C C:/Users/AndrewBerman/Desktop/wt-al-12 ls-files then a pattern match for sdd-harness returned no tracked path at HEAD ae487c67689; git log --all --oneline -- '*sdd-harness*' returned zero commits (no add or delete in any ref)",
        "infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1 lines 413-420 (Invoke-Sdd, the only SI2 POST shape in the repo) and line 441 (FetchDetails/SpecificFileDetails.aspx) are the in-repo references; no UserMasters response type appears in the repo"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO NFRA_SCHWABBF.TO-AL-e1 worker face, item 3: sdd-entitlements.ps1 does what sdd-harness.ps1 does for UserMasters.aspx, and the order says to read sdd-harness.ps1 whole (5.8 KB) first.",
    "world_is": "The entitlement script names DownloadUserMastersRequest and DownloadUserMastersResponse in the Schwab.SI.SI2Desktop.Contract.Download namespace; the request name comes from the order, the response name is a guess, and the master list is found by reflection. If the shape does not match, the script exits 9 and prints the response property names; it never reports a list it did not read.",
    "notes": "Not an alert and not a monitor. The issuer supplies the harness or confirms the names. The first live run of sdd-entitlements.ps1 (runbook step h) is the proof of shape."
  },
  {
    "id": "NFRA_SCHWABBF-W11-S2",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~11",
    "surfaced_at": "2026-10-20T17:10:16Z",
    "one_line": "The amendment's key/value baseline for the regenerated name table reads 83 before and 123 after; a count of the same five sections (fence_patterns, scope_bucket, scope_class, scope_long, scope_short) gives 79 and 119, with the same 40 added and 0 removed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show d2df0d6f0c3:infra/aws/terraform/modules/opal_name/generated_locals.tf (5575 bytes): five sections count 16+16+26+16+5 = 79 map-key lines at four-space indent",
        "python lib/opal_naming.py generate --out <system scratchpad>/amend_gen/out --target infra/aws/terraform/modules/opal_name/generated_locals.tf wrote 7705 bytes at registry@94c3a84b838d2f23; the same five sections count 25+25+35+25+9 = 119; tuple-level diff (section, key, value) gives 40 added, 0 removed",
        "the regenerated repo file (infra/aws/terraform/modules/opal_name/generated_locals.tf) differs from HEAD only by the registry-hash header line and the added entries when whitespace is ignored (git diff -w)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO NFRA_SCHWABBF.TO-AL-a1 amendment, Defect 1: the issuer's measurement of the generator run is 83 key/value entries before, 123 after, 40 added, 0 removed, in the five named sections.",
    "world_is": "The added (40) and removed (0) counts agree. The before and after baselines are each 4 higher in the issuer's count than in the worker's count over the same five sections, a constant offset the regeneration does not change; the worker could not identify which four entries the issuer's method counts. The regenerated table is purely additive, so the offset does not change the fix.",
    "notes": "Not an alert and not a monitor. The issuer confirms the counting method for the four-entry offset; the worker printed both numbers and did not adjust its own count to match."
  }
]
```
