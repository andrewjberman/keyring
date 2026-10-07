# ADVI_COTBKF -- round 13 remediations

<sweep_watermark>2026-10-07T15:5xZ</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~15:5xZ. Graduated at this compile (ADJUDICATION_v11.md): 1 row, round label v14.

```json
[
 {
  "id": "ADVI_COTBKF-D2-S24",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The signed-quantity map shared by the crosswalk, the account links and the daily holdings had no entry for 'leu' (Cash in Lieu), and the crosswalk and links kept two divergent tables, so fractions sold for cash were never subtracted: 13 snapshot differences, 515 leu rows in 69 accounts.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S24",
   "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_13_DRAIN_END_20261007.md @c41e914e19: one table (commonwealth_signs.py, 31 signed types, leu -1.0); DAILY-HOLDINGS snapshot_diffs=0; RULE-CHANGE-DIFF crosswalk_matched 439 -> 471, account_links 212 -> 212 with one swap each way",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_13_L9_GRADE_20261007.md"
  ],
  "remedy": "Done in code and in the local rebuild. Closes when the served crosswalk and account links are re-applied on the one table under their own never-widen pair (the COO half is drafted beside the round-13 packet).",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v14",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v14"
  },
  "closed": false
 }
]
```
