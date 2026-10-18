# AMGT_RESAPP -- round 120 remediations (dell1)

<sweep_watermark>2026-10-18T16:33:58Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T16:33:58Z. C-S200 is the disarm row for W518-S2 (REMEDIATION_v59) and W520-S2 (dismissed at ADJUDICATION_v159 C-S199).

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S200",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "W518-S2 and W520-S2: the management reader labelled a null ceo_public_profile UNREADABLE_OBJECT, so the served label said 'could not be read' for a profile never written, and the pack and the served label disagreed. AMGT-ca-1, deployed by AMGT-ca-5 at 16:12:11Z, gives the reader NOT_WRITTEN for a null or absent profile and narrows UNREADABLE_OBJECT to a failed read.",
    "evidence": [
      "adjudication rows AMGT_RESAPP-D1-C-S198, AMGT_RESAPP-D1-C-S199 (ADJUDICATION_v159)",
      "investigation row AMGT_RESAPP-D1-W520-S2",
      "remediation row AMGT_RESAPP-D1-W518-S2 (REMEDIATION_v59)",
      "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round120/DRAIN_END_PACKET.md @e97c43e97b (sha256 998d5cabf1e0d619...)"
    ],
    "remedy": "None further for the served label: the eight names read NOT_WRITTEN or SEARCHED_NOTHING_FOUND as the CTO restated. W518-S2's remaining half (a census of the label's consumers, the portal page) stays on that row. Close when: the served-state read is on file, which is met.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v120",
    "disarms": [
      "AMGT_RESAPP-D1-W518-S2",
      "AMGT_RESAPP-D1-W520-S2"
    ],
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": "2026-10-18T16:12:11Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v120"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO
