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
  }
]
```
