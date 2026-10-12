# ADVI_COTBKF: remediations, round 72

<sweep_watermark>2026-10-11T19:08Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T19:08:24Z. Input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_72_DRAIN_END_20261011.md @73ef7b3c0d (msg 5617)`.
Graduated, round label v73: 1 row, OPEN, INERT. Nothing was applied, served, re-minted or fetched in the round.

**For the CTO's analysis:**
1. **The custodian check reproduces exactly and reaches 34 of 270 series.** 19 confirmed is the instrument's reach. Neither 712 nor
   3,187 sizes the defect yet: one rests on few series, the other on the vendor read against itself. Grade file: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_72_L9_GRADE_20261011.md`.
2. **The day-before match is real** (88 of 93; 32 the day after, this seat's control) **and was not the stated comparison.** It should be
   confirmed on funds beyond the nine before a basis rule rests on it (row D2-W120-S1).
3. **The re-mint repair holds on this seat's read of the code.** Its printed line counts a hard kill as described; the record does not.
   The "before" state is the capture's, so a second writer in the gap reads as this run's write.
4. Substituting the `other` class would move 257 other tickers, 25 of them split-shaped (the worker's counts, not re-derived).
5. The correction list is stale on two points; the packet names them.

```json
[
 {
  "id": "ADVI_COTBKF-D2-W120-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CB-bt-2: the custodian's dvr row is dated a trading day AFTER the day Yahoo's Adj Close / Close ratio steps for 8 of the 9 funds, so a same-date comparison of the cache's unadjusted Close with the reinvestment price matches on 45 of 93 dates while the previous trading day's Close matches on 88 of 93.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W120-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_72_DRAIN_END_20261011.md @73ef7b3c0d (msg 5617)",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_72_L9_GRADE_20261011.md"
  ],
  "remedy": "The date convention is decided and stated before any basis rule is built on the cached close: which day's close a reinvestment row is compared with, and why. The day-before reading is confirmed on funds beyond the nine first.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v73",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v73"
  },
  "closed": false
 }
]
```
