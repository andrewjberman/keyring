# IRPT_DASHBD: remediations, rounds 76 and 77 (workstream B)

<sweep_watermark>2026-10-11T21:07Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T21:07:33Z. Input: msgs 5777, 5815, 5825 and 5846 (IRPT_DASHBD rounds 76 and 77 drained @cf125a14d4 and @f09dfcb6d9; orders DB-b-143 to DB-b-147).
Graduated, round label v78: 2 rows, OPEN, INERT. This seat made no read of its own for these two rounds.

**For the CTO's analysis:**
1. **Three open rows are reported remedied by workers' reads, re-run by neither the issuer nor this seat; they need your word to close,**
   as D2-W111-S1 did. D2-W113-S2: 33 readers classed, none that serves sums without the id. D2-W113-S3: the fee row's code classes
   FEE-ADMIN. D2-W114-S1: '59 of 90 tie' becomes 89 of 90 with each id counted once; 39 of 42 quoted figures now have a tracked script.
2. **Two things the reader census found that are not closed:** two price paths take a median over un-deduplicated rows and serve a
   price, effect not measured; and 590 ids repeat inside one portfolio group, not explained. Both are in the issuer's next issuance.
3. **The copy is not the original** (row D2-W116-S2): on 3 sampled days the two differ in size and ETag. The reason is not established.
4. **Three quoted figures are withdrawn** (row D2-W118-S1) and the records that quote them are not amended yet.
5. The 51 contested segments: five groups, 46 waiting on one ruling of yours or on a custodian statement. Not closed.

```json
[
 {
  "id": "IRPT_DASHBD-D2-W116-S2",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-143: on the 3 days where both stores hold a day (3 days near the end of the copy's range sampled), the original silver transactions object and the silver_legacy copy differ in size and ETag, so the copy is not byte-identical to the original as it stands now; a rewrite of the originals since the copy is the likely reason (NOT_ESTABLISHED).",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W116-S2",
   "msgs 5777, 5815, 5825 and 5846 (IRPT_DASHBD rounds 76 and 77 drained @cf125a14d4 and @f09dfcb6d9; orders DB-b-143 to DB-b-147)"
  ],
  "remedy": "The original transactions objects and their copy are compared on a stated sample with the reason for the difference read, not inferred; every figure taken from the copy says which of the two it was read from.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v78",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v78"
  },
  "closed": false
 },
 {
  "id": "IRPT_DASHBD-D2-W118-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-145: 3 of 42 figures the tie-out records quote have no producing line in any private script and are WITHDRAWN in FIGURE_PRODUCERS.json: ~104 (the 122/113/9 verdict split of the 244; 'none of the 244 among the 74 restated') and ~113 (the per-type tally of the 50 differing days).",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W118-S1",
   "msgs 5777, 5815, 5825 and 5846 (IRPT_DASHBD rounds 76 and 77 drained @cf125a14d4 and @f09dfcb6d9; orders DB-b-143 to DB-b-147)"
  ],
  "remedy": "The tie-out records that quote the three withdrawn figures are amended to say they are withdrawn, or the figures are re-derived by a tracked script.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v78",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v78"
  },
  "closed": false
 }
]
```
