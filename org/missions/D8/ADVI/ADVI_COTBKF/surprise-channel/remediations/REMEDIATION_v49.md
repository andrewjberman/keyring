# ADVI_COTBKF: remediations, round 80

<sweep_watermark>2026-10-13T16:42Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T16:42:00Z. Follows ADJUDICATION_v57. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_80_DRAIN_END_20261013.md @c47cd08791` (msg 7067). L9: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_80_L9_GRADE_20261013.md`.
Graduated, round label v81: 2 rows, OPEN; ARMED 1 (D2-W155-S1, the served price errors: APH, CTVA, HON). Disarms on a read naming every
consumer of the minted table, or on corrected served prices.

```json
[
 {
  "id": "ADVI_COTBKF-D2-W155-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "Same-hour clause, round 80 CB-cb-1: APH (CUSIP 032095101) is held on 48 SERVED minted days (1 account, 48 account-days, 2025-02-11 to 2025-04-21). Its served close is 0.50 of the store (0.5035 to 0.5048) and 0.487 of the price paid on the nearest sale: a split-sized error in the price served on those days.",
  "evidence": [
   "investigation row D2-W155-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_80_DRAIN_END_20261013.md @c47cd08791",
   "rows D2-W155-S3 and D2-S134"
  ],
  "remedy": "SERVED price errors in the minted copy: APH at 0.50 of the store and 0.487 of the price paid on 48 account-days (1 account); CTVA at 0.150 of the store on 115 account-days; HON's minted copy and partitions disagree (row D2-W155-S3 folds in). The issuer's disarm (D2-S134) rests on D2-S131's hold, no rebuild before 2026-06-08 and no consumer on the minted table, but the minted table's readers were NOT re-measured. This row stays ARMED until a read names every consumer of the minted table (0 means the error reaches no page) or the served prices are corrected. The CTO holds the served-error report.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v81",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v81"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~C2",
   "at": null
  }
 },
 {
  "id": "ADVI_COTBKF-D2-W155-S4",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The build series after the store last day (2026-06-05 onward) has one-day steps of split size or more on several securities (APH 2026-09-04 factor 0.5171; CTVA 2026-10-02 factor 0.1535; KLAC 2026-09-04 factor 1.0774), which the store cannot test.",
  "evidence": [
   "investigation row D2-W155-S4",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_80_DRAIN_END_20261013.md @c47cd08791"
  ],
  "remedy": "After the store's last day (2026-06-05 onward), the build series carries one-day steps of split size or more on several securities (APH 2026-09-04 factor 0.5171; CTVA 2026-10-02 factor 0.1535; KLAC). If the build is ever served for those dates, the same class of error repeats. Read whether the build after 2026-06-05 feeds anything served, and name the steps' cause or the hold.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v81",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v81"
  },
  "closed": false
 }
]
```
