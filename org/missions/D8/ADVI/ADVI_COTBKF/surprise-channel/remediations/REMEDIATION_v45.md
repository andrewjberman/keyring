# ADVI_COTBKF: remediations, round 74

<sweep_watermark>2026-10-11T21:47Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T21:47:49Z. Input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_74_DRAIN_END_20261011.md @1732725e87 (msg 5893)`.
Graduated, round label v75: 2 rows, OPEN, INERT. Nothing was applied or served in the round.

**For the CTO's analysis:**
1. **All three criteria MET; the return number reproduces on this seat's script.** Grade file: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_74_L9_GRADE_20261011.md`.
2. **The large return changes are trade days** (row D2-S127, this seat's): of 96 changes over 10 bp, the 12 purchase days are all higher
   and the 2 sale days both lower; the two largest, 882 bp, are purchases, and the price ratio is flat around them. The baseline
   values newly bought shares at a close that is too low. 74 of the 96 are not explained. A lead on 14 of 14 trade days.
3. **If it holds, the defect is larger on trade days than on distribution dates,** and the three reaches counted so far (holdings on
   an adjusted close) do not measure it.
4. **33 of 270 fund series are validated; 237 are unreadable; 0 are refuted and the refuting arm was never exercised.**
5. The family split is not established; row D2-S125 is closed. Row D2-W120-S1 (the date convention) stays OPEN.
6. One fetched fund reads a ratio of 0.18 (row D2-S126), not investigated. All 1,577 changes sit in 9 accounts.

```json
[
 {
  "id": "ADVI_COTBKF-D2-S127",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L9 round 74: three criteria MET. The first return number reproduces on this seat's script (baseline equal to served on 107,316; 1,577 changed at a finer floor, the same bands). A lead on what the record left unexplained: the largest changes are PURCHASE days, not price steps. Of 96 changes over 10 bp, the 12 on a day the account bought one of the exposed funds are all higher, the 2 sale days both lower; the baseline values new shares at a close that is too low. 74 of the 96 have no such row and are not explained. The family split reads not established and row D2-S125 closes.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S127",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_74_L9_GRADE_20261011.md"
  ],
  "remedy": "The purchase-day reading is confirmed or refuted by recomputing the return on the trade days, under a rule written first; the 74 large changes with no trade row that day are given a cause; then the return error is sized on trade days, not only on distribution dates.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v75",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v75"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-S126",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "One fetched fund, VBTLX, sits far off the build's close on part of its history: lowest ratio 0.1823 (build close over fetched unadjusted close) and 7.83 percent of 1,482 shared dates below 0.98, while it reads 'looks unadjusted' with the other 24. A ratio of 0.18 is not a dividend adjustment. Not investigated.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S126",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_74_DRAIN_END_20261011.md @1732725e87 (msg 5893)"
  ],
  "remedy": "The one fetched fund whose build close sits at 0.18 of its fetched close is read date by date until the cause is named; a ratio that low is not a dividend adjustment.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v75",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v75"
  },
  "closed": false
 }
]
```
