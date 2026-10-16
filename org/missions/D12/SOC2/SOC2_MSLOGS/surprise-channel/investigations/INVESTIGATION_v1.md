# SOC2_MSLOGS -- surprise channel, INVESTIGATION v1 (dell1 fabric)

**Opened by:** `0.9.0_WK_SOC2_MSLOGS~2` (round 1, task order `SOC2_MSLOGS.TO-SM-a1`). **Home:** the project tree's channel.
Lane `ANY`. A worker's row is `SOC2_MSLOGS-D1-W<n>-S<k>`; `<n>` is the slot. **Append-only during the round.** Never edit an existing row.

```json
[
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
