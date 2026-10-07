# IRPT_CUSTDY -- round 4 remediations

<sweep_watermark>2026-10-07T12:1xZ</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~12:2xZ. Graduated at this compile (ADJUDICATION_v4.md): 2 rows, both OPEN, round label v5.

```json
[
 {
  "id": "IRPT_CUSTDY-W10-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The advisor's 4 NOT_IN_DIRECTORY accounts have no custodian key (NO_SCHWAB_KEY), so they are counted as uncovered and cannot be reported; firm-wide, IRPT_BCKEND's census (IB-pr-342) puts 1,447 of 1,961 such accounts at no bridge source at all.",
  "evidence": [
   "investigation row IRPT_CUSTDY-W10-S1",
   "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_4_DRAIN_END_20261007.md @033078c4a5",
   "IRPT_BCKEND deliverables/0.9.0_WK_IRPT_BCKEND~144/IB64-1_directory_coverage.json: BD_KEY_ABSENT_FROM_EVERY_BRIDGE_SOURCE 1,447, XREF_UNRESOLVED 482, carried-absent 32"
  ],
  "remedy": "The round-4 analysis decides whether Schwab holds these accounts under another key (a read of the custodian side), or whether they stay uncovered and are shown as such.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v5",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v5"
  },
  "closed": true
 },
 {
  "id": "IRPT_CUSTDY-W9-S5",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Branch (c) of the SI anchor ruling (holdings before Opal's first partition) cannot be read directly; it is implemented as holdings present or an unconfirmed zero read, no real account falls in (c) today, and the probe takes about 150 s.",
  "evidence": [
   "investigation row IRPT_CUSTDY-W9-S5",
   "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_4_DRAIN_END_20261007.md @033078c4a5"
  ],
  "remedy": "Keep (c) as implemented until a real account falls in it; then read that account's custodian history to confirm the branch, and bound the probe's run time before the hop runs on a schedule.",
  "owner": "2.0.0_SA_COO~K2",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~K2",
   "round": "v5"
  },
  "closed": false
 }
]
```
