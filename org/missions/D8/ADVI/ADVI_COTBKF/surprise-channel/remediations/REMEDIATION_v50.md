# ADVI_COTBKF: remediations, round 81

<sweep_watermark>2026-10-13T19:30Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T19:30:00Z. Follows ADJUDICATION_v58. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_81_DRAIN_END_20261013.md @f57d308ab4`. L9: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_81_L9_GRADE_20261013.md`.
Graduated, round label v82: 2 rows, OPEN, both ARMED: D2-W158-S2 to `1.0.0_SA_CTO~DELL2` (the minted table has readers; the correction cell reads the
served objects and the second hop), D2-W159-S1 to `2.0.0_SA_COO~C2` (two names under one ticker; read for ticker-only readers).

```json
[
 {
  "id": "ADVI_COTBKF-D2-W158-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The premise of the disarm of D2-W155-S1 and D2-W155-S3 (row D2-S134: no consumer attached to the minted table, resting on D2-S131: the minted table has no reader) is contradicted by code: two readers open the minted S3 objects, commonwealth_account_return_daily.py (all three tables) and commonwealth_price_basis_census.py (account_day_value); the ARD output reaches a portal page only through a planned, not applied read route.",
  "evidence": [
   "investigation row D2-W158-S2",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_81_DRAIN_END_20261013.md @f57d308ab4",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_81_L9_GRADE_20261013.md",
   "rows D2-W158-S3, D2-W158-S5 (folded), D2-S134, REMEDIATION_v49 D2-W155-S1"
  ],
  "remedy": "D2-S134's disarm of D2-W155-S1 and -S3 is VOID: the minted table has two code readers (the ARD adapter, commonwealth_account_return_daily.py:221-226, all three tables; the price-basis census :292-295) and one object per prefix (written 2026-10-09T12:41Z), against the never-widen record's 'MINT: 0 objects today' (W158-S3, folded) and the adapter header's 'no S3 write' (W158-S5, folded: the file carries a guarded --apply mint). D2-W155-S1 (REMEDIATION_v49) stays ARMED. Remedy, per the CTO's ruling 1: the correction cell under a never-widen pair, which (a) reads the SERVED minted objects, not only the local .scratch copy (L9 note), (b) establishes whether the ARD -> gold account_return_daily -> reporting-publish -> dashboard route is live, and (c) corrects the adapter header. Disarms on corrected served prices or a read that the second hop reaches no page.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v82",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v82"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~C2",
   "at": null
  }
 },
 {
  "id": "ADVI_COTBKF-D2-W159-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The price store holds more than one asset_name under one ticker: SCCO on 1027 dates (the 3.875% 04/23/2025 bond row at the equity's price) and APH on 70 dates (CL A and NEW CL A, differing on 2026-04-14); a read keyed by ticker alone takes two rows.",
  "evidence": [
   "investigation row D2-W159-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_81_DRAIN_END_20261013.md @f57d308ab4",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_81_L9_GRADE_20261013.md"
  ],
  "remedy": "The price store holds two asset_name values under one ticker (SCCO on 1,027 dates with a bond row at the equity's price; APH on 70 dates, CL A and NEW CL A, differing on 2026-04-14). Read whether any consumer keys the store by ticker alone (the builder at build_canonical_prices_v2.py and the two minted-table readers first). Disarms on that read naming 0 ticker-only readers, or on a keyed fix.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v82",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v82"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~C2",
   "at": null
  }
 }
]
```
