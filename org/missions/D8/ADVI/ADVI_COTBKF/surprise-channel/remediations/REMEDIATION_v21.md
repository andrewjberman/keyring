# ADVI_COTBKF: remediations, round 29

<sweep_watermark>2026-10-09T08:35Z</sweep_watermark>

Graduated at round 29's L9 (ADJUDICATION_v23.md), round label v30: D2-S45, OPEN.

```json
[
 {
  "id": "ADVI_COTBKF-D2-S45",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Two findings from this seat's L9 read. (1) The split re-count's 'continuous' (W56-S1) is measured on the store's close_served, which is split-ADJUSTED by construction and so always continuous across a split; round 28's rule tests the CHAIN's stored close, the series the repair scales. The two tests measure different series, so the re-count does not contradict round 28 on 464287614 or 00162Q866. (2) On B3S728504 and B3S728506, method_r28's day values are 2.43-2.47x method_r26's on EVERY valued day, not only in the 4 regressed months. A constant ratio barely moves a month's return, so month grades can still MATCH while the served account_day_value carries a level that differs from r26 by that factor; which level is right is unmeasured.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S45",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~56/split_recount.md:4 ('Continuity is tested on the store's close_served (split-adjusted)')",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~55/div_dating_trace.md (r28/r26 ratio min/max per month: 2.4365-2.4641)"
  ],
  "remedy": "Trace the r28/r26 ~2.45x day-value ratio on B3S728504 and B3S728506 to its source (a split applied to closes already as traded, a cash-leg change, or other), say which level is right, and re-mint only those accounts' served values if r28's is wrong.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v30",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v30"
  },
  "closed": true
 }
]
```
