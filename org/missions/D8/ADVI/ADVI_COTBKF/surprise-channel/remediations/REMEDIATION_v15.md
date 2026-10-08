# ADVI_COTBKF: remediations, round 22

<sweep_watermark>2026-10-08T19:4xZ</sweep_watermark>

Round 22 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-08 ~19:4xZ. L8 input:
`deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_22_DRAIN_END_20261008.md` (msg 1496). 2 of 2 orders complete and VALID: CB-v-1
@4839b6f2d2, CB-v-2 @c0f717a5c9. L9: CB22v1-AC3 MET (`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_22_L9_GRADE_20261008.md`;
grade row D2-S34). D2-W43-S1, D2-S33 and D2-S34 graduate OPEN below; no row is dismissed, so no adjudication file is minted.
D2-S32 (this seat's round-21 one-cause prediction) stays OPEN, falsified as stated: carried-balance months returned (25 of 72),
trade-day months did not (0 of 75). ARMED: 0.

```json
[
 {
  "id": "ADVI_COTBKF-D2-W43-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CB-v-1: the sale-funding credit returns 25 of the 72 sweep_balance movers and 0 of the 75 sweep_trade_day movers to MATCH; the same missing cash leg also sits on dividend rows (credit) and fee rows (debit) that fund or are paid by a sweep trade, and 23 months moved MATCH -> DIFF.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W43-S1",
   "deliverables/0.9.0_WK_ADVI_COTBKF~43/sweep_regrade.md"
  ],
  "remedy": "A dividend that funds a sweep buy credits cash and a fee paid by a sweep sale debits cash, as one general rule; re-grade with the 138 remaining movers shown (94 of the 122 neither movers still DIFF carry such a row).",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v23"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-S33",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CB-v-2's list-version check reads the version from the persisted month grades only; the day parquet under --data-dir records no list version, so D2-S31's actual case (right grades, stale day values) still passes the check and is caught only by mover_causes' reproduce guard",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S33",
   "round 22 drain-end packet"
  ],
  "remedy": "The runner stamps the list version and cash-leg rule into the day parquet and the mover scripts check it, so stale day values under right grades are refused, not only caught by the reproduce guard.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v23"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-S34",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The repair returned 25 of 163 movers; 23 months regressed MATCH -> DIFF, cause unmeasured (a double credit where the vendor already posts the sale's cash leg is the lead).",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S34 (3.0.0_SA_CVO)",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_22_L9_GRADE_20261008.md"
  ],
  "remedy": "Class the 23 regressions by month, checking each credited day for an existing CFNCASH row, before W43-S1's legs are added on top.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v23"
  },
  "closed": false
 }
]
```
