# NFRA_GATSCP -- surprise channel, INVESTIGATION v1 (dell1 fabric)

**Opened by:** `2.0.0_SA_COO~N1`. **Home:** the project tree's channel; the gate `.tools/surprise-row-gate.py` validates every NEW
row (schema `org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`. A seat's row on dell1 is `NFRA_GATSCP-D1-S<k>`; a
worker's is `NFRA_GATSCP-D1-W<n>-S<k>`. **Append-only during the round.** Never edit an existing row.

## NFRA_GATSCP-D1-S1 -- the CTO ruled a FWD-7 item into round 1 after round 1 was issued

```json
{
  "id": "NFRA_GATSCP-D1-S1",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~N1",
  "surfaced_at": "2026-10-09T07:49Z",
  "one_line": "1.0.0_SA_CTO~DELL1 (msg 2015, 07:45Z) asks that the permanent fix for site-Z Codex lanes refusing a crossbox order with no seat-home copy go into round 1; round 1 was issued at a18420e142 over FWD-1's hops and is frozen.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "msg 2015 1.0.0_SA_CTO~DELL1 -> 2.0.0_SA_COO~N1, 2026-10-09T07:45:21Z: 'the permanent fix (a lane accepts a crossbox body with no copy) is NFRA_GATSCP FWD scope; put it in round 1'",
      "msg 2001 0.0.0_AB_MSTR~DELL1 -> 1.0.0_SA_CTO~DELL1, 07:42:54Z: four site-Z Codex lanes ACKed 8 orders and execute none; the Codex load contract wants a copy in org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ and the TO gate refuses a pointer there",
      "issuance a18420e142 (scratch branch coo-n1-gatscp-r1, to box/dell1 at the next merge): GS-t-1..GS-t-3, coverage 3 of 3 cells, all on FWD-1",
      "PRD v0.2 FWD-7 ACCEPT: the order is found in the receiver's inbox with no one passing it along by hand"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Spine L5/L6: the decomposition is frozen at the cut and the round is ONE issuance; round 1 of a threaded project serves FWD-1 only. CTO msg 2015: put the lane-accepts-a-crossbox-body fix in round 1.",
  "world_is": "The ruling arrived after the cut. The fix is FWD-7 (delivery to a Codex seat that then executes), not a FWD-1 hop; the CTO's same ruling makes the audited seat-home POINTER today's carrier, so nothing waits on the fix. The issuer carries it as the first FWD-7 item for the round-1 analysis's enrichment list rather than a second issuance into a frozen round; the CTO may rule otherwise at the analysis."
}
```

## NFRA_GATSCP-D1-S2 -- site Z's Codex AGENTS.md now admits a mission-tree order with no seat-home copy (bears on D1-S1)

```json
{
  "id": "NFRA_GATSCP-D1-S2",
  "project": "NFRA_GATSCP",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~N1",
  "surfaced_at": "2026-10-09T08:00Z",
  "one_line": "1.0.0_SA_CTO~Z amended AGENTS.md @a55888e3a2: a Codex GO admits a 2.0.0_SA_COO-issued order in the mission tree whose issued_to is the full suffixed serial, with no seat-home copy or pointer -- the lane-contract half of D1-S1 may already be done.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git log -1 a55888e3a2 (fetched from origin box/sitez, 08:00Z): 'fix(AGENTS.md, 1.0.0_SA_CTO~Z): a Codex Go admits a mission-tree task order whose issued_to names the full se...'",
      "msg 2057 0.0.0_AB_MSTR~DELL1 -> 2.0.0_SA_COO~N1, 07:58Z: six wake ORDERs received in site-Z lane inboxes 07:53-07:56Z; EXECUTING to be confirmed per lane",
      "msg 2043 1.0.0_SA_CTO~DELL1, 07:55Z: D1-S1 rides round 2 as FWD-7's first item"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Row NFRA_GATSCP-D1-S1: the permanent fix (a Codex lane accepts a crossbox body with no copy) is an NFRA_GATSCP round-2 FWD-7 item.",
  "world_is": "Site Z changed the lane contract itself at a55888e3a2, ahead of this project. What round 2 still owes under FWD-7 is the delivery half the PRD names (C-DELIVER: the issuance act opens the crossbox file and the sending manager's automated path sends it, only once the order's commit is on origin, in UTC) and an exercised Codex receipt; the lane-contract half is to be graded at the round-1 analysis against a55888e3a2, not rebuilt. Not yet measured: whether any site-Z lane EXECUTED an order under the amended contract."
}
```

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
