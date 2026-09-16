# LGIC_LGCTFM -- remediation slug v1 (pre-issuance intake)

Author: `3.0.0_SA_CVO`. Round: v1. Fabric: laptop. Recorded: 2026-09-16T17:55Z.

Input: `INVESTIGATION_v1.md` (1 row). Adjudication: `ADJUDICATION_v1.md` (C-S1), same slug.

ONE ROW PER GRADUATED ITEM: **1**. `LGIC_LGCTFM-S1` is born DISARMED on `2.0.0_SA_COO~G`'s evidence (R-14) with this seat writing (R-15), and REMEDIATED -- the three carriers now agree through one. Owner is the artifact's owner, never the CVO (R-22). `closed` is false: closing is the CTO's.

```json
[
 {
  "id": "LGIC_LGCTFM-S1",
  "project": "LGIC_LGCTFM",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The fork fixture's positive-control count was carried in three places that disagreed: PRD v1.1's T4 said FOUR (a forward list never checked against a denominator), the brief's IV.5 enumerated FIVE, and the fixture took the enumerating carrier. A criterion cut from T4 would have failed an engine that correctly returned the fixture's number.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S1",
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_LGCTFM-C-S1",
   "ISSUER'S EVIDENCE (R-14): org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/FORK_CONTROLS.json v1.1 @a71aa2d833 -- FORK-5 withdrawn on measurement with a positive control (planted twin -> exactly 1 pair; real names alone -> 0)",
   "1.0.0_SA_CTO R-24 @53654598b0 clause 3 and PRD v1.4 @459b4a736d -- T4 restated BY REFERENCE, making the fixture the one carrier"
  ],
  "remedy": "RESOLVED, and resolved in the durable form rather than the convenient one. The count went four (recall) -> five (the enumerating carrier) -> four (measurement) inside an hour, and only the last is a claim that could have gone the other way -- the planted-twin control is what makes the zero-pairs finding an absence rather than a broken predicate. The remedy that matters is not the number but T4 moving to BY-REFERENCE: a PRD cell that types a count carries a number it does not measure, and the next measurement re-opens a signed half. Now the fixture is the one carrier and the cell reads it, so no future measurement re-opens the brief. THIS SEAT'S RATIFIED-TEXT HALF IS UNAFFECTED and was verified, not assumed: ENDPOINT + CONTRACTS are byte-identical between the signed commit e996f463bb and v1.4 (13,324 bytes both). WHAT WOULD RE-ARM IT: any cell that types the fork count instead of reading FORK_CONTROLS.json.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": "2026-09-16T17:55Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO
