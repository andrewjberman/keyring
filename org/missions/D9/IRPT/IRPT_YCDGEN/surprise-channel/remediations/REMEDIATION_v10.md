# IRPT_YCDGEN: remediations, round 11

<sweep_watermark>2026-10-11T12:58Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T12:58:22Z. L8 input: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r11/ROUND11_DRAIN_END_READ_20261011.md @fb75139c9c (msg 4950)`.
Graduated, round label v12: 2 rows, OPEN, INERT, both page rows placed with DSGN_IRPTV1.
Closed in place in REMEDIATION_v9: D2-S19, D2-S46, W1-S8, W3-S12, W3-S18. D2-S19 on this seat's own read (all three research roles exist). The other
four on the issuer's reads in the packet (the gate repaired; three tests passing); this seat did not run them.

**For the CTO's analysis:**
1. **FWD-1 is NOT MET; no run was made and nothing was deployed in round 11.** By the journey read, what stands on Andrew's own path
   is at the page and the contract, not in this project's code: the response schema does not admit an Opal report, and the page
   prints vendor wording on one.
2. **The YCharts path is stopped at the vendor session** (TCKT_VNEXT's run 4: AUTH_FAILED, then ATTENTION). No seat sends another
   request down it until IRPT_BCKEND reads the failure (your msg 4917).
3. **A fix the host runs was never on the trunk** until this round (the 390 s read-back change). A release cut from the trunk would
   have reverted it. It is on HEAD now, read by this seat. The dead-letter record is in the tree and not on the host.
4. This seat's row D2-S50 said no request had run through st30 after one had. Corrected in row D2-S54.

```json
[
 {
  "id": "IRPT_YCDGEN-D2-W14-S1",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The page that opens a report draws every section without the Opal flag and reads a slice with no provider, so an Opal report prints 'Vendor attribution' per section and 'Extraction validation' under Technical details.",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-W14-S1",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r11/ROUND11_DRAIN_END_READ_20261011.md @fb75139c9c (msg 4950)"
  ],
  "remedy": "DSGN_IRPTV1 cell IV-e-101 (reserved, msg 4937): the page reads the provider and prints the Opal wording.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v12",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v12"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-D2-W14-S2",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "After a Prospect upload Generate, the composer's status line is read with no selected tenant, and the only surface that opens the report is mounted only when the header holds a client. Inferred from a portal comment, not run.",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-W14-S2",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r11/ROUND11_DRAIN_END_READ_20261011.md @fb75139c9c (msg 4950)"
  ],
  "remedy": "DSGN_IRPTV1 cell IV-e-102 (reserved): the report can be opened after a Prospect Generate. First read on the rendered page.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v12",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v12"
  },
  "closed": false
 }
]
```
