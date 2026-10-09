# ADVI_COTBKF: remediations, round 45

<sweep_watermark>2026-10-09T15:21Z</sweep_watermark>

Graduated at round 45's L9 (ADJUDICATION_v34.md), round label v46: W72-S1, OPEN.

```json
[
 {
  "id": "ADVI_COTBKF-D2-W72-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Same split-literal pattern, counted not changed: commonwealth_bd_txn_provenance.py 2 sites (:37 PFX = '/'.join(['silver','pri'+'ces']) -- the identical key; :103 re.search('pri'+'ce|...')); data/cot/scripts/gold/build_canonical_prices_v2.py 1 site (:65 '/'.join(['silver','']) ); 0 in the other 36 commonwealth_*.py files (38 files scanned incl. the writer; 2 carry it).",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W72-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_45_DRAIN_END_20261009.md @a6f57849df (msg 3558)"
  ],
  "remedy": "Rule the sweep: replace commonwealth_bd_txn_provenance.py:37 (the same silver/prices key) and the cot writer's :65 '/'.join(['silver', '']) with the registry rows round 45 added (the :103 regex fragment is not an address); the writer's site falls in round 46's file.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v46",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v46"
  },
  "closed": false
 }
]
```
