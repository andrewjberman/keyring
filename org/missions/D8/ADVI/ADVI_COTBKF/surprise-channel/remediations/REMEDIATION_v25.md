# ADVI_COTBKF: remediations, round 35

<sweep_watermark>2026-10-09T12:17Z</sweep_watermark>

Graduated at round 35's L9 (ADJUDICATION_v27.md), round label v36: D2-S52, OPEN.

```json
[
 {
  "id": "ADVI_COTBKF-D2-S52",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "49 Financial's three bond price overrides (05613L3H2, WFC 4.15% 2029, NEM 2.8% 2029) still sit in 38 Cottonwood price keys in opal-data-cot (37 daily files x 3 rows, plus 1,623 rows in canonical_prices.parquet), written once on 2026-06-09 by a since-removed shared-builder chain. Each key is a FULL Cottonwood price file, so deletion would take Cottonwood's own prices with it; the clean removal is a rewrite without those rows, a served move under a never-widen pair.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S52",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~63/bd_txn_provenance.md (section 5: the 38 keys, versions, sizes)"
  ],
  "remedy": "Andrew rules rewrite (recommended: each key rewritten without the 49F rows, prior versions as rollback, under a never-widen pair) or delete; the CTO rules the three bonds' source of record (they stay HELD until then).",
  "owner": "1.0.0_SA_CTO~DELL2 (Andrew's word for the S3 act)",
  "round": "v36",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v36"
  },
  "closed": false
 }
]
```
