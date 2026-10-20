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
  }
]
```
