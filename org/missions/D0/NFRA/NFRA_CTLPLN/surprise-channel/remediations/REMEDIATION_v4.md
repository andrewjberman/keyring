# NFRA_CTLPLN -- remediations, v4

<sweep_watermark>2026-10-12T13:35Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L`, 2026-10-12 ~13:3xZ, at the round-10 drain (1.0.0_SA_CTO msg 108555). Graduated in ADJUDICATION_v12.md
C-S36. One row: W73-S2 (ARMED). Every NFRA_CTLPLN order is terminal at HEAD 4f3a2a9694: 104 complete, 4 withdrawn,
1 cancelled, 1 superseded.

```json
[
  {
    "id": "NFRA_CTLPLN-W73-S2",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "thread-trace.py builds a round's order set by globbing the reading checkout's working tree (.tools/thread-trace.py find_orders, glob at line 236), not by reading git refs, while its docstring says the round is read from git. An order that CLOUD holds but the reading checkout lacks is dropped from every hop, and the trace prints no sign of the omission. The seat-order read added by CT-z-1 Amendment 1 uses the same glob.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md rows W73-S2 and S9114",
      ".tools/thread-trace.py:236 at HEAD 4f3a2a9694"
    ],
    "remedy": "P2. find_orders reads the order set from git (ls-tree of origin/CLOUD and origin/box/*, as HOP 1-4 already do) and prints its denominator by ref. Done when a planted order present only on origin/CLOUD, absent from the reading worktree, appears in the trace's orders= field.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v12",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~C",
      "round": "v12"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~C",
      "at": "2026-10-14T03:30Z"
    },
    "closed": true
  }
]
```
