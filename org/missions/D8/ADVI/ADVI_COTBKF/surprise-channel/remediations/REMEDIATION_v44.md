# ADVI_COTBKF: remediations, round 73

<sweep_watermark>2026-10-11T20:12Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T20:12:07Z. Input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_73_DRAIN_END_20261011.md @f3bffdeb6f (msg 5731)`.
Graduated, round label v74: 1 row, OPEN, INERT. Nothing was applied, served, re-minted or fetched in the round.

**For the CTO's analysis:**
1. **Both criteria MET; the three-date read reproduces figure for figure on this seat's script.** Grade file: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_73_L9_GRADE_20261011.md`.
2. **The convention may be by fund family** (row D2-S125, this seat's): 12 of the 15 day-before funds are American Funds and 1 of the 17
   same-day funds is. Eight of the nine were American Funds. A lead on 32 funds, to be tested on its own rule. Row D2-W120-S1 stays OPEN.
3. **Three reaches stand on three sets** (3,187; 712; 1,874) and none is a return error. The floor is 19 series by your ruling; the
   validated-close instrument reads 21.
4. **The re-mint mode's three rows are closed** (D2-W118-S1 to S3): read in the code by this seat in rounds 72 and 73. What stays
   untested is whether the real bucket honours the write condition; that belongs in the pair when one is written.
5. Unsized: 59 funds not validated; 121 fund series with no cached close, 27 of them held (the worker's count).

```json
[
 {
  "id": "ADVI_COTBKF-D2-S125",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The date convention the round read as undetermined splits by fund family. Of the 15 decided funds whose reinvestment row matches the cached close of the trading day BEFORE, 12 are American Funds; of the 17 that match the same day, 1 is. The family is read from the first two words of the custodian's own security description. Eight of the nine funds of rounds 71 and 72 are American Funds; the ninth is the one that matched on the same day. A count on 32 funds, with exceptions each way: a lead, not a result.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S125",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_73_L9_GRADE_20261011.md"
  ],
  "remedy": "The three-date read is split by fund family under a rule written before the split is run, over every fund with enough cells; the convention is then stated per family or stated as not established.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v74",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v74"
  },
  "closed": true
 }
]
```
