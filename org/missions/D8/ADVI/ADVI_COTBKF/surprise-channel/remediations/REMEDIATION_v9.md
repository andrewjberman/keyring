# ADVI_COTBKF -- round 16 remediations

<sweep_watermark>2026-10-07T20:5xZ</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~21:0xZ. Graduated at this compile (ADJUDICATION_v13.md): 3 rows, all OPEN, round label v17.

```json
[
 {
  "id": "ADVI_COTBKF-D2-S28",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "On the stores Opal already holds, the FWD-3 monthly grade reads 1,947 MATCH, 2,284 DIFF and 78,362 UNGRADABLE (a blank day) at 0.05 points. Fully priced months with no external flow MATCH 1,675 of 3,093; flow months DIFF 866 of 1,138 with a median 7.4 points, so the flow convention or a flow class is off, not the prices.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S28",
   "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_16_DRAIN_END_20261007.md"
  ],
  "remedy": "Grade the flow months under start-of-day versus end-of-day flows, with tax withholding internal, and keep the better convention; then re-grade.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-S27",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Security transfers mostly carry Amount 0 (lo 18,157; trco 147 of 147; trfo 611; li 1,424; trfi 60), and the daily return blanks such a day (FLOW_UNVALUED). Today only 101 days blank for it because the rest are already UNPRICED; after the price load most would.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S27",
   "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_16_DRAIN_END_20261007.md"
  ],
  "remedy": "Value a zero-Amount security flow at its quantity times the same day's close, before the price load makes it the binding gap.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-S26",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "silver document_index.page_count sums to 0 over 11,119 documents in every doc_type, so the served index cannot say how long any document is.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S26",
   "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_16_DRAIN_END_20261007.md"
  ],
  "remedy": "Read page counts from the PDFs themselves (the applied documents table holds every file), or state the field as not supplied in the index contract.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v17"
  },
  "closed": false
 }
]
```
