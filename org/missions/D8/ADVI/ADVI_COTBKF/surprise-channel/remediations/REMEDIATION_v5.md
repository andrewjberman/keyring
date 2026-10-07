# ADVI_COTBKF -- round 7 remediations

<sweep_watermark>2026-10-07T10:5xZ</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~11:1xZ. Graduated at this compile (ADJUDICATION_v6.md): 1 row, OPEN, round label v8.

```json
[
 {
  "id": "ADVI_COTBKF-W23-S1",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The applied silver transactions table holds 1,416,497 rows, while row W2-S1 reported 1,415,137 after dropping exact duplicates; the coverage page gives a reason for the gap that the worker's own row calls unexplained.",
  "evidence": [
   "investigation row ADVI_COTBKF-W23-S1",
   "deliverables/0.9.0_WK_ADVI_COTBKF~23/COVERAGE_STATEMENT.md:66",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_7_L9_GRADE_20261007.md"
  ],
  "remedy": "Count the exact duplicates in the applied table (all columns but the source line): 1,360 means the de-duplication was never applied and the page's reason holds; any other count is a finding. The page then states the measured reason.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v8",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v8"
  },
  "closed": true
 }
]
```
