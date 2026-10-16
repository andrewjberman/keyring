# SOC2_MSLOGS -- investigation channel, v1

Rows are appended, never edited. Filed by 0.9.0_WK_SOC2_MSLOGS~5 on TO SOC2_MSLOGS.TO-SM-x1 (scrub), surfaced 2026-10-16T17:28:13Z.

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
  }
]
```
