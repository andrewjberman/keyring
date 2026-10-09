# NFRA_GATSCP -- surprise channel, INVESTIGATION v1

**Home:** the project tree's channel; the gate `.tools/surprise-row-gate.py` validates every NEW row (schema
`org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`. A worker's row on dell1 is `NFRA_GATSCP-D1-W<n>-S<k>`.
**Append-only during the round.** Never edit an existing row.

## NFRA_GATSCP-D1-W2-S1 -- the tree-index wrapper test was already RED at the base (stale arm count 18, tool prints 38)

```json
{
  "id": "NFRA_GATSCP-D1-W2-S1",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_GATSCP~2",
  "surfaced_at": "2026-10-09T08:03:00Z",
  "one_line": "TO-GS-t-2 says the wrapper test .tools/tests/test_missions_tree_index_selftest.py keeps passing, but at the base it fails W2 (EXPECTED_ARMS = 18, the tool prints 38/38); the channel file named in <paths> also did not exist.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python .tools/tests/test_missions_tree_index_selftest.py at base a18420e142 (before any edit): 'FAIL  W2 DENOMINATOR: 18/18  (printed 38/38)' and 'MISSIONS-TREE-INDEX WRAPPER: 3/4 PASS (denominator 4)'",
      "git log -1 -- .tools/tests/test_missions_tree_index_selftest.py = 6eac560149; git log -1 -- .tools/missions-tree-index.py = 651f750a5a (the tool grew arms after the wrapper pinned 18; its own header says a tool change that adds arms updates EXPECTED_ARMS in the same commit)",
      "ls org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel at base a18420e142: no such directory; this file was created by 0.9.0_WK_NFRA_GATSCP~2 with this row"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-GS-t-2 build step 4: 'Keep .tools/tests/test_missions_tree_index_selftest.py passing' (a premise that it passes now), and <paths> names an existing INVESTIGATION_v1.md.",
  "world_is": "The wrapper was RED at the base on W2 only. The file is inside this order's <paths>, so EXPECTED_ARMS was set to the new self-test count (52) in the same commit as the arms (wrapper 4/4 PASS afterwards); no rule, mutant anchor or other wrapper arm was changed. The channel file was absent and is created with this row.",
  "notes": "Worker 2 of NFRA_GATSCP. The order names the id form NFRA_GATSCP-W2-S<k>; the row gate refuses a bare id with fabric dell1 (a bare id is the laptop's), so the dell1 coordinate D1- is carried. The disposition is the CVO's."
}
```
