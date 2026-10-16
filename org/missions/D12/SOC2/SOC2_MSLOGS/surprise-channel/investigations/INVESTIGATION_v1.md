# SOC2_MSLOGS -- investigation channel, v1

Worker rows from 0.9.0_WK_SOC2_MSLOGS~4 on task order SOC2_MSLOGS.TO-SM-g1.registry-home (cell SM-g-1).
Each row is one item of the fenced json array; a dell1 worker row mints CODE-D1-W<n>-S<k> (n = the worker slot).

```json
[
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
  }
]
```
