# IRPT_BCKEND: remediations, round 180 (workstream ~P)

<sweep_watermark>2026-10-13T15:46Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T15:46:00Z. Follows ADJUDICATION_v81. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_180_P_DRAIN_END_20261013.md` (msg 7033). No judgment criterion.
Graduated, round label v181: 1 row, OPEN, owner `2.0.0_SA_COO~P2`. The directory-search apply (round 181) establishes the directory's home first.

```json
[
 {
  "id": "IRPT_BCKEND-D2-W364-S1",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IB-pr-514 premise: the builder's own directory read (firm_bucket_map 49financial = opal-data-bd, investor-reporting/directory/latest.json) finds the landed directory, but the canonical address for that same directory (lib/opal_naming, irpt/49financial/platinum/directory/current/latest.json in opal-data-49financial) holds no object, while the served holdings index for the firm sits in opal-data-49financial. One firm, two bucket homes.",
  "evidence": [
   "investigation row D2-W364-S1",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_180_P_DRAIN_END_20261013.md",
   "this seat's head-object 2026-10-13T15:4xZ: opal-data-bd investor-reporting/directory/latest.json present (LastModified 13:40:54Z, 272 B)"
  ],
  "remedy": "The builder reads the landed directory through the routed alias (firm_bucket_map 49financial = opal-data-bd), not the canonical address() home (opal-data-49financial). The irpt-directory-search apply's step 0 establishes which home that function reads before its reach count is read. The alias is the TRANSITIONAL row this project is the expiry owner of (row D2-S84), so the move to the canonical home is the same cell's question.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v181",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v181"
  },
  "closed": false
 }
]
```
