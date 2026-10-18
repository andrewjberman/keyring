# ADVI_FIRMBKTS -- surprise channel, INVESTIGATION v1 (site-Z fabric)

**Home:** the project tree's channel. Lane `ANY`. Append-only. Id grammar on this fabric: `ADVI_FIRMBKTS-Z-S<k>`; `"fabric": "site-z"`. The dell1 rows live in INVESTIGATION_v1.md beside this file.

---

```json
[
  {
    "id": "ADVI_FIRMBKTS-Z-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "site-z",
    "surfaced_by": "0.0.0_AB_MSTR~Z",
    "surfaced_at": "2026-10-18T12:05Z",
    "one_line": "ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.md is flipped complete, but its newest proof instance (org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~23/ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.proof_of_spec.json) reads INVALID under proof-of-spec-check.py --governing-order, rc 1. Today's gate grades instance ~16 (first of 5) and reads rc 1 too, so newest-instance-only selection changes nothing for this order; the row is the CVO's reopening-is-a-ruling carrier.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~B1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python .tools/proof-of-spec-check.py org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~23/ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.proof_of_spec.json --governing-order org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.md returned rc 1 (census run 2026-10-18, C:/tmp/proof_census_20261018.txt (dry run of .tools/proof-instance-census.py, 33 multi-instance orders of 4,883 pairs))",
        "the order file at HEAD carries status complete as its last <status> tag; 5 tracked proof instances exist for it, newest by commit time then numeric ~N is the one named",
        "CVO~Z verdict 35689 / CTO msg 35690: each already-complete order whose newest instance reads FAIL or INVALID gets one row for its issuer; reopening stays a ruling, never automatic"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "An order flipped complete has a proof-of-spec instance that reads VALID against its governing order.",
    "world_is": "The newest instance (~23) reads INVALID: decomp_ref.doc names ADVI_FIRMBKTS_DECOMP_R3.md. Every one of the 5 instances reads rc 1 today. Whether the order stays complete, is reopened, or the instance is repaired is the issuer's ruling.",
    "notes": "Filed by 0.0.0_AB_MSTR~Z as the census carrier. No order is reopened or edited by this row and the newest-instance gate is not armed. Disarm: none (INERT)."
  }
]
```
