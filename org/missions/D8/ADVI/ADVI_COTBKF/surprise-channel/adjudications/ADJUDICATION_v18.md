# ADVI_COTBKF: CVO adjudication, round 24

<sweep_watermark>2026-10-09T00:05Z</sweep_watermark>

Round 24 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~00:1xZ. L8 input: `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_24_DRAIN_END_20261008.md` (msg 1955). CB-x-1
complete and VALID (drained @d9484f20fa). **L9: CB24x1-AC4 NOT MET as written** (grade row D2-S36; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_24_L9_GRADE_20261008.md`). 1 row dismissed below;
D2-W46-S2, D2-W46-S3 and D2-S36 graduate OPEN in `remediations/REMEDIATION_v17.md`. D2-S35 (round 23: the 25 DIFF again) is REMEDIATED
and closed in place: 25 of 25 MATCH under `method`. ARMED: 0.

This is the project's largest single move (MATCH 2,058 -> 3,059). The NOT MET is one clause that needs data the fabric does not
hold yet, not a defect in the work.

```json
[
  {
    "id": "ADVI_COTBKF-C-S25",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T00:05:26Z",
    "one_line": "D2-W46-S1 (AC2's no-sweep control was ill-posed for an account-wide method: 464 of 465 MATCH->MATCH months move a median 0.002 pts by design) is dismissed: AMENDMENT 1 (CTO msg 1944) replaced it with the year-chain control, which reads 103 of 103 account-years equal (worst 3.98e-13 pts).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-W46-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Drain d9484f20fa is an ancestor of box/dell2 HEAD; the issuer's real run equals the worker's (MATCH 2,058 -> 3,059, DIFF 1,525 -> 925, regressions 98 each named, year_chain_same=True, r22_named=25/25); the cash ledger equals the 2026-06-23 snapshot to the cent on 40 of 40 accounts.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_COTBKF-D2-W46-S1",
        "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_24_DRAIN_END_20261008.md",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~46/sweep_regrade.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An ill-posed control replaced by ruling with one that measures the right thing."
  }
]
```
