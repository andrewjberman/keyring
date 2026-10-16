# SOC2_MSLOGS -- surprise channel, INVESTIGATION v1 (round 1, dell1 fabric)

Worker rows of the round-1 cells, appended and never edited. Rows `SOC2_MSLOGS-D1-W5-S*` were filed by 0.9.0_WK_SOC2_MSLOGS~5 (SM-x-1) and
`SOC2_MSLOGS-D1-W1-S*` by 0.9.0_WK_SOC2_MSLOGS~1 (SM-c-1); the drain joined the two files (2.0.0_SA_COO~S1), changing no row.

```json
[
  {
    "id": "SOC2_MSLOGS-D1-W5-S1",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_SOC2_MSLOGS~5",
    "surfaced_at": "2026-10-16T17:28:13Z",
    "one_line": "population.json and main.tf still say eight accounts while the scrubbed README says every account; left as a words-only scrub.",
    "spec_asserts": "data/m365_metadata/README.md (rewritten by TO SOC2_MSLOGS.TO-SM-x1) states the store holds the raw Microsoft 365 audit records of EVERY account, so that a hacked account's exposure can be read back.",
    "world_is": "data/m365_metadata/scripts/population.json still lists EIGHT accounts (andrew, alyssa, bobby, manav, yang, menachem, jim, jeanette), and infra/aws/terraform/trino/main.tf line 1 still says 'the eight operations team members'. The every-account purpose and the eight-account collector population disagree. The scrub changed words only and left both as they were.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/m365_metadata/scripts/population.json@da39a423d3 lists eight entries",
        "data/m365_metadata/README.md@da39a423d3 opening states every account",
        "infra/aws/terraform/trino/main.tf@da39a423d3 line 1 says eight operations team members"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "SOC2_MSLOGS-D1-W5-S2",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_SOC2_MSLOGS~5",
    "surfaced_at": "2026-10-16T17:28:13Z",
    "one_line": "The TO names INVESTIGATION_v1.md under this project's surprise-channel folder, which was absent in the worktree; the worker created the file with these rows.",
    "spec_asserts": "The TO's <paths> block names org/missions/D12/SOC2/SOC2_MSLOGS/surprise-channel/investigations/INVESTIGATION_v1.md as an existing write path for this worker to file rows into.",
    "world_is": "That file and its surprise-channel folder were absent from the worktree (branch wk-SOC2_MSLOGS-5, HEAD 4a6a6f77c1 before the scrub commit). The project folder held only decompositions, deliverables, prd, project.json and task-orders. The worker created the file with these rows only.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D12/SOC2/SOC2_MSLOGS/ directory listing in the worktree at the start of the TO: decompositions, deliverables, prd, project.json, task-orders"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "SOC2_MSLOGS-D1-W1-S1",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_SOC2_MSLOGS~1",
    "surfaced_at": "2026-10-16T17:31:19Z",
    "one_line": "data/m365_metadata/README.md still describes filter.py and population.json, which this cell deletes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/m365_metadata/README.md@09a7732aab lines 6 and 12 name scripts/collector/filter.py and scripts/population.json",
        "data/m365_metadata/README.md is outside the <paths> grant of SOC2_MSLOGS.TO-SM-c1, so it was not edited"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The cell deletes filter.py and scripts/population.json; the collector keeps no filter and no population.",
    "world_is": "The module README at data/m365_metadata/README.md names both deleted files; it is stale after this cell."
  },
  {
    "id": "SOC2_MSLOGS-D1-W1-S2",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_SOC2_MSLOGS~1",
    "surfaced_at": "2026-10-16T17:31:19Z",
    "one_line": "silver/first_content.py raises on a coverage record without dropped_id_only; the raw-era records no longer carry that field.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~S1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/m365_metadata/scripts/silver/first_content.py@09a7732aab lines 50-62: _id_only_drops sums record['dropped_id_only'] and raises RuntimeError when the key is absent",
        "data/m365_metadata/scripts/collector/coverage_record.py in this worktree: build_record no longer emits dropped_id_only (fields listed, fetched, already_stored, events, gap, status, era)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The coverage records keep exactly the fields the cell contract names (listed, fetched, already_stored, events, gap, status, era).",
    "world_is": "The silver first-content reader still requires dropped_id_only on every coverage record and raises when it is absent. Its file is outside this cell's grant, so it was not edited. Left alone, the reader fails on every raw-era coverage day."
  },
  {
    "id": "SOC2_MSLOGS-D1-W1-S3",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_SOC2_MSLOGS~1",
    "surfaced_at": "2026-10-16T17:31:19Z",
    "one_line": "The surprise-channel investigation file named by the order did not exist in the worktree; the worktree sparse checkout omits org/surprise_channel/.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/surprise_channel/schemas/investigation_item.schema.json exists at 09a7732aab and is readable only through git show; the worktree sparse checkout does not carry org/surprise_channel/",
        "this file was created by the worker as the carrier, inside the <paths> grant"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The channel file for SOC2_MSLOGS is the investigation file named in the order, already in the worktree.",
    "world_is": "The file was absent; the worker created it with this header and the row array only."
  },
  {
    "id": "SOC2_MSLOGS-D1-W1-S4",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_SOC2_MSLOGS~1",
    "surfaced_at": "2026-10-16T17:31:19Z",
    "one_line": "The contract says last_end advances only past landed blobs, but today's complete fire moves last_end to now even when a blob failed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/m365_metadata/scripts/collector/collect.py@09a7732aab: a complete fire sets last_end to now_iso regardless of failed blobs",
        "data/m365_metadata/scripts/collector/collect.py in this worktree: a complete fire with a failed blob sets last_end to the oldest failed blob created time; with no failure, to now"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "last_end advances only past blobs that landed (stored or already stored), as today.",
    "world_is": "Today's rule moves past failed blobs. The built rule holds last_end at the oldest failed blob so the next fire re-lists it; seen still stops landed blobs being fetched twice."
  },
  {
    "id": "SOC2_MSLOGS-D1-W1-S5",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_SOC2_MSLOGS~1",
    "surfaced_at": "2026-10-16T17:31:19Z",
    "one_line": "The status rule 'no activity collected' now reads listed == 0; today it reads events == 0, which an already-stored-only day would meet.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/m365_metadata/scripts/collector/coverage_record.py@09a7732aab: status 'no activity collected' when events == 0",
        "data/m365_metadata/scripts/collector/coverage_record.py in this worktree: status 'no activity collected' when listed == 0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Coverage records are built as coverage_record builds them today, with the named fields.",
    "world_is": "Under the raw era events counts only blobs of this run that landed, so a day whose blobs were all already stored reads events 0 while listed is above 0. The rule was moved to listed so such a day is not reported as no activity."
  },
  {
    "id": "SOC2_MSLOGS-D1-W4-S1",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_SOC2_MSLOGS~4",
    "surfaced_at": "2026-10-16T17:29:15Z",
    "one_line": "The SM-g-1 face dates Andrew's 'if any opal user is hacked' words ~16:1xZ in the same record; they are message 1 of that record, whose header reads ~15:5xZ.",
    "spec_asserts": "The SM-g-1 face cites Andrew's words 'if any opal user is hacked, we want to be able to know the exposure' as 'Andrew-direct 2026-10-16 ~16:1xZ, same record'.",
    "world_is": "The quote is message 1 of record org/tier1_exec/2.0.0_SA_COO~S1/ANDREW_DIRECT_20261016_1559Z_REFRAME_M365_LOGS_AS_SOC2_COMPROMISE_EXPOSURE_MACRO_SOC2_MSLOGS.md, whose own header reads ~15:5xZ. The ~16:1xZ message in that record is message 6 ('i dont care abt tckt metadata anymore'). The edits cite the record's own time (~15:5xZ, message 1). The order was not edited.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/2.0.0_SA_COO~S1/ANDREW_DIRECT_20261016_1559Z_REFRAME_M365_LOGS_AS_SOC2_COMPROMISE_EXPOSURE_MACRO_SOC2_MSLOGS.md@4a6a6f77c1 (message 1 and message 6 read at that pin)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "SOC2_MSLOGS-D1-W4-S2",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_SOC2_MSLOGS~4",
    "surfaced_at": "2026-10-16T17:29:15Z",
    "one_line": "The raw-pull records cited by project.json, PRD C-RAW and X18 cell 5 are absent from this worktree; the retirement cites only the Andrew record present.",
    "spec_asserts": "The X18 retirement of departure (1) is recorded citing Andrew's raw-pull words of ~16:12Z (CRO record ANDREW_DIRECT_20261016_1612Z_SOC2_MSLOGS_METADATA_ONLY_PROOF_OF_INTERNAL_SECURITY.md, cited by project.json and PRD C-RAW), and X18 cell 5 cites CTO records ANDREW_DIRECT_20261016_040xZ_WFSPINE_BUCKET_OPAL_DATA_TRINO.md and ANDREW_DIRECT_20261016_054xZ_SPINE_BECOMES_TCKT_MTADTA_OPS_EIGHT_DROP_AT_OUTSET_GLOBGRPH_ROLE_ONLY.md.",
    "world_is": "None of those four records exists in this worktree (org/tier1_exec/4.0.0_SA_CRO/ is absent; the two CTO deliverables are absent from org/tier1_exec/1.0.0_SA_CTO/deliverables/). The retirement row therefore cites only the Andrew record present in this tree (message 1) and states the raw-pull fact by its built state and PRD C-RAW, with no quote of his raw-pull words. The X18 departure (2) text and its citations are unchanged.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ls of org/tier1_exec/4.0.0_SA_CRO/ and org/tier1_exec/1.0.0_SA_CTO/deliverables/ at 4a6a6f77c1: the cited files are not present"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "SOC2_MSLOGS-D1-W2-S1",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_SOC2_MSLOGS~2",
    "surfaced_at": "2026-10-16T17:26:05Z",
    "one_line": "The timeline's default silver reader asks for columns (record_id, feed, client_ip, item_name, user_id) that the silver builder at HEAD does not write, so the reader would raise on every real partition.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~S1 via the SM-s-1 cell: align the silver builder's COLUMNS with handler.py TIMELINE_COLUMNS before the door is released (SM-r-1)",
    "spec_asserts": "DOOR CONTRACT v3, timeline: the default reader reads record_id, creation_time, feed, operation, result_status, client_ip, item_name and user_id from every silver partition of the touched Eastern dates.",
    "world_is": "silver_builder.py at HEAD (09a7732aab) writes event_id, creation_time, date, actor, workload, operation, record_type, result_status, subject_hash, participants, site, file_id, file_name, extension, folder, client_ip_class. record_id, feed, client_ip, item_name and user_id are not among them, so pyarrow read_table(columns=...) raises on a partition the present builder wrote. The door answers error; the unit tests inject a reader and never see it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/globgrph-trino-access/silver_builder.py@09a7732aab COLUMNS, lines 21-24: event_id, creation_time, date, actor, workload, operation, record_type, result_status, subject_hash, participants, site, file_id, file_name, extension, folder, client_ip_class",
        "infra/aws/lambda/globgrph-trino-access/handler.py (worktree wk-SOC2_MSLOGS-2, uncommitted at filing) TIMELINE_COLUMNS: record_id, creation_time, feed, operation, result_status, client_ip, item_name, user_id"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "SOC2_MSLOGS-D1-W2-S2",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_SOC2_MSLOGS~2",
    "surfaced_at": "2026-10-16T17:26:05Z",
    "one_line": "The write-once rule treats ANY exception from head_object as a missing object, so a head that fails for a reason other than a 404 lets the put overwrite an existing bronze record.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~S1: decide whether the write-once rule narrows to a 404 (ClientError code NoSuchKey or 404) before the door is released",
    "spec_asserts": "DOOR CONTRACT v3, write-once: for dataset bronze, put first calls s3.head_object; if the object exists the answer is already_stored; only a missing object (head raises) is written.",
    "world_is": "handler.py _exists() catches Exception around head_object, so AccessDenied, a throttle or a 5xx on the head is read as missing and the put proceeds. The code follows the literal rule, and the fake client raises KeyError for a missing key, which a narrowed ClientError test would not admit. The role holds s3:GetObject on the prefix, so a 403 on head is not expected in normal operation.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/globgrph-trino-access/handler.py (worktree wk-SOC2_MSLOGS-2, uncommitted at filing) _exists(): except Exception returns False",
        "infra/aws/terraform/trino/access.tf aws_iam_role_policy.access: ListTheTrinoPrefix and ReadAndWriteTheTrinoPrefix (s3:GetObject on m365-metadata/trino/*)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "SOC2_MSLOGS-D1-W2-S3",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_SOC2_MSLOGS~2",
    "surfaced_at": "2026-10-16T17:35:23Z",
    "one_line": "The naming gate refuses two S3 prefixes that the door hand-types for the bronze audit_records partition (handler.py lines 55 and 77); the door package cannot import lib/opal_naming at runtime.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~S1: a naming registry row for the audit_records partition, or an R20 register entry that Andrew acknowledges, before the naming gate enforces",
    "spec_asserts": "CLAUDE.md rule 30: every S3 address is lib/opal_naming.py address() output; a builder refusal is a missing registry row to add, never a hand-typed workaround.",
    "world_is": "build.sh ships handler.py and silver_builder.py only, so the Lambda cannot import lib/opal_naming; the prefixes are hand-typed as at HEAD. The naming gate on commit e70208bfe7 graded handler.py:55 and :77 as NEW and OUT-OF-PATTERN S3Key (REFUSE), in the WARN window, so not blocking; its live read failed (CensusError, comp-find aws BLOCKED).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit output for e70208bfe7: [naming-gate] NAMING REFUSE handler.py:55 bronze/audit_records/date=%s/ and handler.py:77 bronze/audit_records/date=\\d{8}/; WARN window: 2 REFUSE verdict(s) did not block",
        "infra/aws/lambda/globgrph-trino-access/build.sh@09a7732aab: copies handler.py and silver_builder.py into the package and asserts those two files only"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "SOC2_MSLOGS-D1-W2-S4",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_SOC2_MSLOGS~2",
    "surfaced_at": "2026-10-16T17:47:38Z",
    "one_line": "The owned-paths lane gate refuses every commit of the door's paths by this worker once the order is complete at HEAD, so the head-branch amendment cannot be committed.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~S1 (the issuer): re-open or re-issue the order so a non-terminal order at HEAD names these paths to this serial, or rule on the terminal reading of the lane gate",
    "spec_asserts": "Amendment (issuer 2.0.0_SA_COO~S1): commit the head-branch fix through safe-commit within the order's <paths>, and keep the order status complete.",
    "world_is": "safe-commit refuses handler.py and tests/test_handler.py: 'no NON-TERMINAL task order at HEAD issued_to this serial names this path'. The first commit e70208bfe7 passed while the order was pending; the order is complete at HEAD da5fe81961, so no open grant remains. The amended fix is uncommitted in the worktree; HEAD's proof still cites the pre-amendment handler.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit refusal at the amendment commit attempt (owned-paths lane violation, block mode, agent 0.9.0_WK_SOC2_MSLOGS~2 not in permitted_agents for infra/aws/lambda/globgrph-trino-access/handler.py and tests/test_handler.py)",
        "org/missions/D12/SOC2/SOC2_MSLOGS/task-orders/SOC2_MSLOGS.TO-SM-a1.door-raw-timeline.md@da5fe81961: line 8 <status>complete</status>"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  }
]
```
