# ADVI_COTBKF: remediations, round 79

<sweep_watermark>2026-10-12T02:45Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T02:45:15Z. Input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_79_DRAIN_END_20261012.md @324559b1ec (msg 6393)`.
Graduated, round label v80: 2 rows, OPEN, INERT.

**For the CTO's analysis:**
1. **All three criteria MET.** Grade file: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_79_L9_GRADE_20261012.md`.
2. **The property PRD v0.10 rests on is now read:** this seat printed the other box's code; its as-traded close undoes every later
   split. It is code, not a landed value: that box reports 0 objects in the series store and its writer off.
3. **Three equities are off by split-sized ratios and nobody knows why** (row D2-W152-S1): a half, a seventh, a tenth. This is the
   split question meeting data for the first time, and it is outside the funds. Whether they sit on a measured day is the first
   thing to read.
4. **The corrected fund basis has no data behind it yet:** the request for 15 funds' as-traded closes is cut and carried to the other
   box's queue; every held fund day is UNPRICED under C-BASIS until it lands.
5. The many-name tickers reach 4 securities and 26 measured account-days as measured. The live store is this project's own rewrite;
   its parent version has no author on record.
6. The correction list predates PRD v0.10 and the other box's answer; the issuer says so.

```json
[
 {
  "id": "ADVI_COTBKF-D2-W151-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "C-BASIS names the securities history MDPF_SECHIST owns as the source of the as-traded close, but the tree shows SECHIST's series writer switched off with no landing record, and the live as-traded writer is MDPF_DEMQUE's price_store; its as_traded_close is already split-scaled upstream.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W151-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_79_DRAIN_END_20261012.md @324559b1ec (msg 6393)",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_79_L9_GRADE_20261012.md"
  ],
  "remedy": "Built as PRD v0.10 rules: this build's split step is not applied to a fund point read from the as-traded column, shown by the count of fund points the step changed being zero.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v80",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v80"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W152-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Off-task, found while sizing CB-ca-2: for three silver-priced held securities (APH, CTVA, KLAC) the r34/after build price on the last day the store holds is 0.5000, 0.1500 and 0.1000 of the store's own row, where a security with no split after that day should sit at 1.0 (1,258 of 1,263 silver-priced securities sit within 0.1 percent of 1.0).",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W152-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_79_DRAIN_END_20261012.md @324559b1ec (msg 6393)",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_79_L9_GRADE_20261012.md"
  ],
  "remedy": "The three equities are read date by date against their split dates until the cause is named: unscaled, scaled twice, or something else. Then the count of held securities with a split inside the back-fill whose build price and store row differ by a split-sized ratio, and how many measured account-days rest on them.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v80",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v80"
  },
  "closed": false
 }
]
```
