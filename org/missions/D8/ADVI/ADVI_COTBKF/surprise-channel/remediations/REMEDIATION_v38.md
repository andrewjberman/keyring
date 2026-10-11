# ADVI_COTBKF: remediations, rounds 65 to 67

<sweep_watermark>2026-10-11T13:18Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T13:18:17Z. L8 inputs: the round 65, 66 and 67 packets (msgs 4792, 4896, 4966).
**L9:** CB65bm1-AC2 MET; CB65bm2-AC3 MET; **CB66bn1-AC2 NOT MET on its fourth limb**; CB67bo2-AC2 MET. Each on this seat's own
re-derivation from the local tables.
Graduated, round label v68: 4 rows, OPEN, INERT. Closed in place in REMEDIATION_v37: D2-S108 (the served method row states income
absent, read on the served objects by this seat).

**For the CTO's analysis:**
1. **No re-mint list exists yet.** The withholding rule moves 2 account-days with inputs held equal, but the comparison has not been
   run at the served instant's pin (row D2-S115). At today's store a re-mint would replace 30 day files.
2. **Spin-offs** (row D2-W100-S1): whether their factor is applied is yours to rule; it decides which pin a re-mint uses.
3. **The threshold for a leftover balance** (round 65): 56 such days sit on a base of 100.00 or more; 206 of the 207 outliers are
   positive; 122 days between 10 and 100 percent on such a base are unexamined. Row D2-S110 stays OPEN in REMEDIATION_v37.
4. **Two price requests are written and not sent.** The Bloomberg leg is at least 8 days under the budget.
5. The mint adapter does not yet copy the pin into the mint's manifest (the issuer's note).

```json
[
 {
  "id": "ADVI_COTBKF-D2-S115",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CB66bn1-AC2 is NOT MET on its fourth limb: the two withholding rules were compared on today's store, not at the served instant's pin, so the list of dates a re-mint replaces is not established.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S115",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_66_L9_GRADE_20261011.md",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_67_DRAIN_END_20261011.md @2326dc3955 (msg 4966)"
  ],
  "remedy": "One run of method_r29 at the served instant's pin against Proof A's method_r28; the list is stated against the served table.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v68",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v68"
  },
  "closed": true
 },
 {
  "id": "ADVI_COTBKF-D2-W100-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The four entries the grown split store added are spin-offs carried as 'splits' with a price factor. Applying them moves 30 account-days on 29 dates. Whether the rule should scale closes for a spin-off is undecided.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W100-S1",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_67_L9_GRADE_20261011.md",
   "this seat's own diff 2026-10-11T13:18:17Z of the served run's price table (.scratch/advi_cotbkf/r34/after/security_day_price.parquet) against today's (wk-cotbkf-80/.scratch/w97/r28/after), 2,124,908 rows each, 0 rows on one side only: 3,034 points differ, on 4 securities, 649 / 1,876 / 392 / 117; for each the last differing date is the day before the entry's date (2022-04-10, 2025-10-29, 2021-09-30, 2020-11-16) and the ratio of old to new price is one constant per security (0.7553, 0.9425, 0.9470, 0.9488), the reciprocal of the entry's factor. On the returns: the 28 differing values are in 1 account, both signs (11 up, 17 down), the largest on 2020-11-09, and the difference on the entry's own date 2020-11-17 is 0.00004. Printed: commonwealth_flows.py:73 and :80 (the two corporate-action row types are internal, no value crosses the boundary)"
  ],
  "remedy": "The CTO rules it. This seat's read for that ruling: the return on the event's own date barely moves; the differences sit in the weeks before it, in both directions.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v68",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v68"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W99-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "In a fresh worktree the regrade stops at its report step for want of five untracked inputs that exist in one worktree's scratch only.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W99-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_67_DRAIN_END_20261011.md @2326dc3955 (msg 4966)"
  ],
  "remedy": "The five inputs are tracked or rebuilt by a named step, so the chain runs from a clean checkout.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v68",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v68"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W99-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The as-traded price input carries a column stamped from the price store's current modification time: a second live read, outside the pin. It does not reach the returns; that file's hash is not reproducible.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W99-S2",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_67_DRAIN_END_20261011.md @2326dc3955 (msg 4966)"
  ],
  "remedy": "The column is taken at the pin or dropped, so every input of a build is at one named instant.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v68",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v68"
  },
  "closed": false
 }
]
```
