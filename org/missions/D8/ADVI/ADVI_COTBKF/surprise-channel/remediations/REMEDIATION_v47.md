# ADVI_COTBKF: remediations, round 78

<sweep_watermark>2026-10-12T01:39Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T01:39:54Z. Input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_78_DRAIN_END_20261012.md @7af967bc1b (msg 6268)`.
Graduated, round label v79: 2 rows, OPEN, INERT.

**For the CTO's analysis and the fund-basis addendum:**
1. **Both criteria MET.** Grade file: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_78_L9_GRADE_20261012.md`.
2. **The right close is known and held, and has no source.** The store has one price column and it is not the unadjusted close for
   the 15 funds. The unadjusted close covers every held trading day, in a vendor cache that is a folder on one box and that no
   build reads. An addendum that names it as the basis names something that is not yet a landed, scheduled source.
3. **The store has a second defect, independent of the adjustment** (row D2-W149-S2): its ticker is not one security on 308 of 4,000
   tickers, and the build reads by ticker. It reaches past the 15 funds and is not sized.
4. **Nobody knows what wrote the live store** (row D2-W149-S1): it is not the output of the writer at HEAD.
5. **The flat charge is real and incomplete.** It fails its own bar. The allowance that classed the 15 failing funds was built from
   it; that allowance could only excuse units, so it cannot have made a fund fail, but the classing is unreconciled until ruled.
6. Row D2-S131 and its ruling in force stand.

```json
[
 {
  "id": "ADVI_COTBKF-D2-W149-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The live price store object is not the output of the writer at HEAD: it has 5 columns (no source_firm) and carries a source value the HEAD writer never assigns (scoped_override, 12,042 rows).",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W149-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_78_DRAIN_END_20261012.md @7af967bc1b (msg 6268)",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_78_L9_GRADE_20261012.md"
  ],
  "remedy": "The act that wrote the live store object is identified: which code, which run, whose. Until then no statement about how these prices were made rests on the writer in the tree.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v79",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v79"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W149-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The price store's ticker key is not one security: 308 of 4,000 tickers carry more than one asset_name, 5,748,151 of 11,289,398 rows carry no ticker, and VGHAX (one of the 15 funds) carries 3 names (VANGUARD HEALTH CARE INV, INVESCO HEALTH CARE INVSTOR, VANGUARD HEALTH CARE ADM) with the same Yahoo series under all three.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W149-S2",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_78_DRAIN_END_20261012.md @7af967bc1b (msg 6268)",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_78_L9_GRADE_20261012.md"
  ],
  "remedy": "The build reads the store by a key that names one security, or the count of held securities whose ticker carries more than one asset name is measured and each is shown priced from its own rows.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v79",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v79"
  },
  "closed": false
 }
]
```
