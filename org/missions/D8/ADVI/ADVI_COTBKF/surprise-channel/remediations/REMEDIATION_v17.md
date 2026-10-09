# ADVI_COTBKF: remediations, round 24

<sweep_watermark>2026-10-09T00:05Z</sweep_watermark>

Graduated at round 24's L9 (ADJUDICATION_v18.md), round label v25: D2-W46-S2, D2-W46-S3, D2-S36, all OPEN.

```json
[
 {
  "id": "ADVI_COTBKF-D2-W46-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The order grades every cross-month dividend month both ways (pay date, ex-date) from the Yahoo dividend series; no store the chain reads holds an ex-date, so the ex arm and the very set of cross-month months cannot be built and are reported NOT GRADED, never inferred",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W46-S2",
   "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_24_DRAIN_END_20261008.md",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~46/sweep_regrade.md"
  ],
  "remedy": "Bring ex-dates through the dell1 data-queue project (Yahoo carries them), then grade the 22 dividend-dated regressions pay vs ex with the swing printed; adopt neither date until that measure decides.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v25",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v25"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W46-S3",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The CRO's table names no treatment for ASF, bcf, cbf, fco, stp, term, ftax, stax, frntax; they keep the default (internal, a drag now that the ledger debits cash) and are reported, 35 of the 98 regression months hold one",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W46-S3",
   "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_24_DRAIN_END_20261008.md",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~46/sweep_regrade.md"
  ],
  "remedy": "Rule the unlisted types, ftax first (35 months: is a withholding riding a withdrawal a flow?), and test ManCheck's reading; each ruling is one table row and a re-run.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v25",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v25"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-S36",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CB24x1-AC4's third clause (every cross-month dividend month graded both ways, swing printed) is unmeasurable: no store the chain reads holds an ex-date.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S36",
   "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_24_DRAIN_END_20261008.md",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~46/sweep_regrade.md"
  ],
  "remedy": "Closes with D2-W46-S2's graded pay-vs-ex run, or by a CTO amendment of the clause by name.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v25",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v25"
  },
  "closed": false
 }
]
```
