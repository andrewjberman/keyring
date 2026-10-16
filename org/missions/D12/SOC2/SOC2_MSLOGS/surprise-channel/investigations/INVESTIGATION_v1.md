# SOC2_MSLOGS investigation v1 -- worker rows of 0.9.0_WK_SOC2_MSLOGS~1 (cell SM-c-1, TO SOC2_MSLOGS.TO-SM-c1)

Rows filed by the worker for the collector raw-era switch. Each row is one spec-versus-world mismatch met during
on-spec execution; the worker kept working on its task. Base commit of the worktree: 09a7732aab.

```json
[
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
  }
]
```
