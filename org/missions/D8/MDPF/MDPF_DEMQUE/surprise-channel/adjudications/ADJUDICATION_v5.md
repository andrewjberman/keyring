# MDPF_DEMQUE -- round 5 L8/L9 adjudication

<sweep_watermark>2026-10-09T12:32Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T12:32:00Z. L8 packet: 2.0.0_SA_COO~Q1 msg 2421, ROUND5_REAL_RUN.md @05d2eb6bc5. 4 of 4 complete, 73 tests. 3 rows: BLOCKING Z-W1-S3 dismissed; D1-W13-S1 and D1-S3 graduated INERT to `remediations/REMEDIATION_v4.md`.

**L9 -- the DQ-t-17 TR finding (judgment): MET** (row C-S10). FWD-4 now has finish dates on all three channels (reference 2026-10-09, model_block and history 2026-10-13, claims held).

```json
[
  {
    "id": "MDPF_DEMQUE-C-S10",
    "project": "MDPF_DEMQUE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T12:32:00Z",
    "one_line": "DQ-t-17's judgment (the written TR finding) MET: the finding is sound and its recommended method is right for the TR column. On this seat's own re-run (tr_compare.py, ED/FXFXX/LNVGY, one trading day later than the worker's) every claim held: ED's (P+D)/P_prev daily TR matches Bloomberg's gross TR to 0.05 bp at most (cumulative 0.10004 vs 0.10005); FXFXX reads Yahoo 0.0000 against Bloomberg +0.35% (the money-market accrual is invisible to Yahoo); LNVGY's largest day is 85.84 bp, the missed dividend. The finding states its own limits honestly (splits and special-vs-regular not shown on real data; withholding shown only on one ADR). Method accepted: compute from as-traded close and ex-date cash; Bloomberg's field is the reference where stored and flags a missing cash row; money-market TR must come from Bloomberg or an explicit accrual.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment criterion graded by a seat that did none of the work.",
    "world_is": "DQ-t-17's judgment (the written TR finding) MET: the finding is sound and its recommended method is right for the TR column. On this seat's own re-run (tr_compare.py, ED/FXFXX/LNVGY, one trading day later than the worker's) every claim held: ED's (P+D)/P_prev daily TR matches Bloomberg's gross TR to 0.05 bp at most (cumulative 0.10004 vs 0.10005); FXFXX reads Yahoo 0.0000 against Bloomberg +0.35% (the money-market accrual is invisible to Yahoo); LNVGY's largest day is 85.84 bp, the missed dividend. The finding states its own limits honestly (splits and special-vs-regular not shown on real data; withholding shown only on one ADR). Method accepted: compute from as-traded close and ex-date cash; Bloomberg's field is the reference where stored and flags a missing cash row; money-market TR must come from Bloomberg or an explicit accrual.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran data/mdpf/scripts/demque/tr_compare.py --names ED,FXFXX,LNVGY at 12:3xZ: ED days 258 max 0.046 bp cum 0.10004/0.10005; FXFXX days 24 median 1.03 bp cum 0.00355/0.0; LNVGY days 255 max 85.837 bp cum 1.6545/1.6315",
        "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~15/TR_COMPARISON.md Findings 1-5 and 'Recommended method'",
        "packet deliverables/2.0.0_SA_COO~Q1/ROUND5_REAL_RUN.md @05d2eb6bc5 (TRCMP-OK 3 names)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard: the DQ-t-17 judgment graded MET by a seat that did none of the work."
  },
  {
    "id": "MDPF_DEMQUE-C-S11",
    "project": "MDPF_DEMQUE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T12:32:00Z",
    "one_line": "Z-W1-S3 (BLOCKING) dismissed: resolved by the issuer's amendment @5622357580; DQ-t-18 completed @41182b9b85 (METER-OK at dell1, 73 of 73 tests; deploy closed @856117665b).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-Z-W1-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment criterion graded by a seat that did none of the work.",
    "world_is": "Z-W1-S3 (BLOCKING) dismissed: resolved by the issuer's amendment @5622357580; DQ-t-18 completed @41182b9b85 (METER-OK at dell1, 73 of 73 tests; deploy closed @856117665b).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_DEMQUE-Z-W1-S3",
        "packet: FWD-2 OPAL_BBGTML meter row"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-W1-S3 (BLOCKING) dismissed: resolved by the issuer's amendment @5622357580; DQ-t-18 completed @41182b9b85 (METER-OK at dell1, 73 of 73 tests; deploy closed @856117665b)."
  }
]
```
