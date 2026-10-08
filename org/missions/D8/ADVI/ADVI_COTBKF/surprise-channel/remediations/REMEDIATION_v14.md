# ADVI_COTBKF: remediations, round 21

<sweep_watermark>2026-10-08T19:0xZ</sweep_watermark>

Round 21 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-08 ~19:0xZ. L8 input:
`deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_21_DRAIN_END_20261008.md` (msg 1445). 1 of 1 order complete and VALID: CB-u-1
(drained @0aefdc2e8e). L9: CB21u1-AC3 MET (`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_21_L9_GRADE_20261008.md`;
grade row D2-S32). D2-W42-S1, D2-S31 and D2-S32 graduate OPEN below; no row is dismissed, so no adjudication file is minted. D2-S29 is
now fully classed (163 = 16 core + 72 sweep_balance + 75 sweep_trade_day) and stays OPEN until the cash-leg repair. ARMED: 0.

```json
[
 {
  "id": "ADVI_COTBKF-D2-W42-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A sweep buy debits cash in the after arm, but the non-sweep sale that funded it credits no cash, so the after-arm base shrinks (D49141714 2019-02: 4,061.90 -> 51.04, month 3.31% vs 0.04% reported).",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W42-S1",
   "deliverables/0.9.0_WK_ADVI_COTBKF~42/mover_causes.md trace 1"
  ],
  "remedy": "Repair the chain's cash leg for a non-sweep sale that funds a sweep buy; re-grade with all 163 movers shown; the test of D2-S32 is that sweep_balance and sweep_trade_day collapse together.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v22",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v22"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-S31",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CB21u1-AC2's invocation reads day values from the runner's default --data-dir, so its result depends on which arms ran there last (trunk first gave 0/0/147 until the none->v1 arms were rebuilt).",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S31",
   "drain-end packet round 21 (the two trunk runs)"
  ],
  "remedy": "The mover scripts name their own data folder, or rebuild or check their arms' list versions before reading.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v22",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v22"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-S32",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Both traced cause classes of the 147 neither movers show one mechanism, W42-S1's sweep-buy debit with no funding credit; the classes record where it lands.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S32 (3.0.0_SA_CVO)",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_21_L9_GRADE_20261008.md"
  ],
  "remedy": "Closes with W42-S1's repair re-grade: count how many of the 72 and 75 move back to MATCH.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v22",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v22"
  },
  "closed": false
 }
]
```
