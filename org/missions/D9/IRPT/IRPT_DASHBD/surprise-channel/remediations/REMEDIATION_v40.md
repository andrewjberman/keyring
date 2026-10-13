# IRPT_DASHBD: remediations, round 94

<sweep_watermark>2026-10-13T23:24Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T23:24:00Z. Follows ADJUDICATION_v58. L8 input: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND94_B_DRAIN_END_20261013.md @2d802bc2d5` (msg 7347). No judgment criterion.
Graduated, round label v96: 3 rows, OPEN, owner `2.0.0_SA_COO~D2`: FDRXX to CASH (BLOCKING, never-widen pair), the fee-basis method row, the
account_class_daily contract's false statement.

```json
[
 {
  "id": "IRPT_DASHBD-D2-W144-S2",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Andrew's smoke (DB-b-178, S21): FDRXX shows the class Fixed Income on the report. The portal assigns no class by symbol; it reads the served asset_class. The class is assigned in the producer: data/black_diamond/scripts/gold/lib/etf_classifier.py:144 returns the canonical table row's asset_class verbatim for the ticker. Left unchanged here (outside the DEV-only candidate's grant).",
  "evidence": [
   "investigation row D2-W144-S2",
   "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND94_B_DRAIN_END_20261013.md @2d802bc2d5",
   "row D2-S21 (folded)"
  ],
  "remedy": "FDRXX (and money-market funds generally) is classed Fixed Income by the producer: data/black_diamond/scripts/gold/lib/etf_classifier.py:144 returns the canonical table's asset_class verbatim. Andrew's smoke (D2-S21, folded) wants CASH. Round 96 cell under a never-widen pair (the CTO's order, msg 7258): name every money-market symbol the change moves, the served rows it reclasses, and the rollback per key.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v96",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v96"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W141-S6",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The contract's convention.fee_basis_label reads the fee basis from dim_return_method, and states it as GROSS_ONLY; the activity rows carry method_version 3 (6914 of 6914 on 2026-10-12), and gold dim_return_method holds method_version 1 and 2 only, so no landed row carries the version the figures were produced under.",
  "evidence": [
   "investigation row D2-W141-S6",
   "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND94_B_DRAIN_END_20261013.md @2d802bc2d5"
  ],
  "remedy": "FWD-21's ACCEPT requires the fee basis labeled, but the sample cannot fill it: the activity rows carry method_version 3 (6,914 of 6,914 on 2026-10-12) and gold dim_return_method has no row for it. Add the method row (or source the label from where the method is defined) so the fee-basis member fills; until then the report prints it absent in words.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v96",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v96"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W141-S5",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IRPT_DASHBD_ACCOUNT_CLASS_DAILY_CONTRACT.json says served false and 'No object of this table exists in any bucket', but s3://opal-data-49financial/irpt/49financial/gold/account_class_daily/ holds four date partitions (2026-10-07, 10-08, 10-09 and 10-12); the class members of the report, and the class rows, therefore do not rest on the absence the contract states.",
  "evidence": [
   "investigation row D2-W141-S5",
   "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND94_B_DRAIN_END_20261013.md @2d802bc2d5"
  ],
  "remedy": "IRPT_DASHBD_ACCOUNT_CLASS_DAILY_CONTRACT.json says served false and that no object of the table exists in any bucket, but s3://opal-data-49financial/irpt/49financial/gold/account_class_daily/ holds four date partitions. Correct the contract's statement to what the bucket holds, and say whether the table is served.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v96",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v96"
  },
  "closed": false
 }
]
```
