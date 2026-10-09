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
