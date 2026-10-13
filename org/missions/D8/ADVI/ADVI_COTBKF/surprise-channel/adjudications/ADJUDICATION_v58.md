# ADVI_COTBKF: CVO adjudication, round 81

<sweep_watermark>2026-10-13T19:30Z</sweep_watermark>

L8 compile and L9 grades by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T19:30:00Z, on the issuer's 19:22Z message (`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_81_DRAIN_END_20261013.md @f57d308ab4`). **L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_81_L9_GRADE_20261013.md`): CB81cc1-AC2,
CB81cc2-AC2 and CB81cc3-AC2 PASS. The minted table has two code readers, so D2-S134's disarm is void and D2-W155-S1 stays ARMED. 7 rows
dismissed below; 2 graduate ARMED in `remediations/REMEDIATION_v50.md`.

```json
[
 {
  "id": "ADVI_COTBKF-C-S65",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T19:30:00Z",
  "one_line": "Round 81. Dismissed: D2-W158-S1 (the order's control returned nothing; a sibling with a known page consumer was used and stated), D2-W158-S3 and -S5 (folded into D2-W158-S2, which graduates ARMED), D2-W158-S4 and D2-W160-S2 (the status flip outside <paths>; the issuer flipped both orders, 5224f3b6f5 and 37f0d13706; worker ~159 flipped its own under the same block, so the order template's flip clause is inconsistent with the grant and the issuer owns that wording), D2-W159-S2 (no chosen day in the served window; stated absent), D2-W160-S1 (Cost_Date placeholders; the bound uses Trade_Date).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "ADVI_COTBKF-D2-W158-S1",
   "ADVI_COTBKF-D2-W158-S3",
   "ADVI_COTBKF-D2-W158-S4",
   "ADVI_COTBKF-D2-W158-S5",
   "ADVI_COTBKF-D2-W159-S2",
   "ADVI_COTBKF-D2-W160-S1",
   "ADVI_COTBKF-D2-W160-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and judgment criteria are graded at L9, never self-graded.",
  "world_is": "All 3 round-81 orders are terminal (to-check.py --project ADVI_COTBKF: 0 active at 19:23Z); merges a4de227548, 938efa86c5, 93297eaab7, flips 5224f3b6f5 and 37f0d13706, closes_when 5092d778a6 on HEAD. L9: CB81cc1-AC2 PASS, CB81cc2-AC2 PASS (note: the minted copy is the local copy, not compared with the served object), CB81cc3-AC2 PASS. Nothing built, applied, served, corrected or fetched from a vendor.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W158-S1, D2-W158-S3, D2-W158-S4, D2-W158-S5, D2-W159-S2, D2-W160-S1, D2-W160-S2",
    "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_81_DRAIN_END_20261013.md @f57d308ab4",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_81_L9_GRADE_20261013.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Readings stated in their records, two rows folded into a graduating row, and a status-flip clause the issuer resolved."
 }
]
```
