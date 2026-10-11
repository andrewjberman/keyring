# ADVI_COTBKF: remediations, round 64

<sweep_watermark>2026-10-11T10:13Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T10:13:26Z. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_64_DRAIN_END_20261011.md @59f48b48ae (msg 4673)`.
**L9: CB64bl1-AC2 MET; CB64bl3-AC2 MET**, on this seat's own re-derivation of both records' totals (`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_64_L9_GRADE_20261011.md`).
Graduated, round label v65: 2 rows, OPEN, INERT.

**For the CTO's analysis:**
1. **The outliers are wider than the 24.** 207 measured days in the returns table are above 100 percent; the round examined 3
   (row D2-S110). 152 of them have a prior value of one dollar or more and are unexamined.
2. **Prices: we do not hold them.** 0 of 459 unpriced securities are priced by the custodian's data or by a store the build reads.
   The next step is a pull from the ruled sources; 253 of the 459 have no symbol.
3. **Class D (2 days) is a defect of the form**: a withholding with no withdrawal row is not counted as an outflow.

```json
[
 {
  "id": "ADVI_COTBKF-D2-S110",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The returns table serves a measured return whatever the size of its base. 207 measured days carry an absolute return above 100 percent; 55 of them sit on a prior value under one dollar and 152 on one dollar or more.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S110",
   "this seat's read of the same table: of 107,311 measured days with a positive prior value, 207 carry an absolute return above 100 percent; 5,437 have a prior value under one dollar, and 55 of those are above 100 percent",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_64_L9_GRADE_20261011.md"
  ],
  "remedy": "A cell classes the 207 as round 64 classed the 24, and the CTO rules a serving rule for a residual base (a floor on the prior value, or a blank with its reason).",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v65",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v65"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-S108",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The method row beside Cottonwood's table is written by IRPT_DASHBD's producer, which writes income_basis = cash_when_received on every row, while the table's two income columns are null by design. A reader cannot tell the null from a zero.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S108",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_64_DRAIN_END_20261011.md @59f48b48ae (msg 4673)"
  ],
  "remedy": "IRPT_DASHBD's cell (ruled, msgs 4615 and 4633); this project's issuer owes the read-back when it lands.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v65",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v65"
  },
  "closed": false
 }
]
```
