# IRPT_BCKEND: remediations, round 172 (workstream ~P)

<sweep_watermark>2026-10-13T04:54Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T04:54:00Z. Follows ADJUDICATION_v73. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_172_P_DRAIN_END_20261013.md` (a148daa3fc, msg 6794). No judgment criterion.
Graduated, round label v173: 2 rows, OPEN, ARMED 0. For the CTO: D2-W353-S5 (the frozen export envelope against the portal's ExportReceipt type).
Next read the issuer proposes, which this seat supports: an offline replay showing that the irpt-holdings serve path passes a node carrying
`account_id` through unchanged, before the builder's host bundle is deployed.
Still OPEN and ARMED where they stand: D2-W345-S3 (v47), D2-W346-S2 and -S3 (v47), D2-W348-S2 (v48), D2-W350-S1 (v48).

```json
[
 {
  "id": "IRPT_BCKEND-D2-W353-S5",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The committed frozen export envelope has no facts.covered_account_ids, while the wire export receipt carries it and the portal's ExportReceipt type declares it as a required member. The base generator copied the wire member. The committed bytes win, so the generator now drops it; the committed map and the portal type disagree at HEAD.",
  "evidence": [
   "investigation row D2-W353-S5",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_172_P_DRAIN_END_20261013.md"
  ],
  "remedy": "The committed frozen export envelope omits facts.covered_account_ids, which the portal's ExportReceipt type declares required and the wire carries. Rule which side is right: the committed fixture gains the member, or the type makes it optional. Until then a test built on the frozen envelope tests a shape the type forbids.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v173",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v173"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W352-S1",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The installed generate composition passes lambda _: None as the report-kind validator (generate_installed.py:306). The repository and the publisher call validate(kind, report) with two arguments, so the no-op is never a schema validator, and the two-argument call would raise TypeError. Measured by reading only; no live path measured, because the handler is deployed unwired-to-live (generate.tf:13). No armed hazard.",
  "evidence": [
   "investigation row D2-W352-S1",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_172_P_DRAIN_END_20261013.md"
  ],
  "remedy": "The installed generate composition passes `lambda _: None` as the report-kind validator (generate_installed.py:306), while the repository and the publisher call validate(kind, report) with two arguments. A two-argument call would raise if the path were wired; it is not wired live. Repair it in a later cell, before any path calls it.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v173",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v173"
  },
  "closed": false
 }
]
```
