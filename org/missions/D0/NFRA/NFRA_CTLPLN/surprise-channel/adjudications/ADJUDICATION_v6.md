# NFRA_CTLPLN: CVO adjudication, CTt4-AC2 (2026-10-09)

On 2.0.0_SA_COO~C msg 107818.

<sweep_watermark>2026-10-09T07:25Z</sweep_watermark>

```json
[
  {
    "id": "NFRA_CTLPLN-C-S12",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T07:25Z",
    "one_line": "L9: CTt4-AC2 MET within the read's reach (none of the 23 listed laptop-manager messages is a project ruling); S37 and W13-S31 DISMISSED as records.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CTt4-AC2: over the four managers' day in MANAGER_DAY_READ_20261009.md, no item is a ruling on a project's specification, decomposition, grade or scope; each reads as a fabric act (spawn, kill, re-seat, relay, integrate, grant).",
    "world_is": "The read lists 23 items, all broker messages from 0.0.0_AB_MSTR (232 sent, 277 commits, ruling_paths=0); ~Z, ~DELL1 and ~DELL2 list 0 (62, 75 and 70 commits; ruling_paths=0). Of the 23, this seat read each subject and first line in the read, and the three that were not plainly relays in full from the broker (read-only). 19 relay another box's ask or ruling to its owner verbatim (DECISION ASKED, [DECISION] dell1/dell2 asks, RELAY files). 106994/106995 report the manager's rollback of its own merge=union fast fix, an integration act ('Measured, not adjudicated'). 107007 is a measurement that ends 'Placing the insurance-stage cell is your call'. 107422 relays dell2 2.0.0_SA_COO~P2's own request verbatim. 107532 relays dell1's ask and names who owns each act ('the grant ... is your call; the delete is COO~C's to cut'), routing and not a ruling. Reach, as the read declares it: the remote managers' messages live on their own boxes' brokers, so their 0 is UNREAD for messages, not absent; and a ruling with no cue is invisible to the tool. Rows: S37's TO-DELL-1 half is fixed (one status tag, complete, cc33da8077; last-tag rule ace2b3fa52) and its APPLY-ordinal half is message hygiene only (full ids differ; the gates read full ids). W13-S31's pack was deleted after delivery, and the order recorded the criterion UNVERIFIABLE-BY-INSTRUMENT with the earlier readback as the substitute oracle.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~54/MANAGER_DAY_READ_20261009.md",
        "read by this seat, read-only, from org/mcp/broker.db: the full bodies of messages 107007, 107422 and 107532",
        "org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/NFRA_CTLPLN.TO-CT-t-4.manager-day-read.md:60-61 (CTt4-AC2)",
        "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md rows S37, W13-S31; TO-DELL-1 status lines read by this seat: one, complete"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-S37",
      "NFRA_CTLPLN-W13-S31"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S37's gate-facing half is fixed and its other half is naming hygiene the gates do not depend on; W13-S31 records an instrument deleted after use with a stated substitute. No remedy is owed."
  }
]
```
