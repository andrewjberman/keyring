# IRPT_BCKEND: CVO adjudication, round 117 (workstream ~P)

<sweep_watermark>2026-10-11T03:53Z</sweep_watermark>

Round 117 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T03:53:39Z. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_117_P_DRAIN_END_20261011.md @57a120767a (msg 4020)`. No judgment criterion.
9 rows dismissed below. 5 rows are ready to graduate and are HELD in `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_REMEDIATION_ROUND_117_HELD_20261011.md` until `TO-IB-pr-420` (round 118) is terminal:
D2-S60 (ARMED), D2-W278-S3, D2-W278-S4, D2-W278-S5 and D2-S62. ARMED after this compile: 1 (D2-S60).
Not compiled here: 13 INERT rows of 2026-10-08 (D2-W173-S1 to D2-S10) that no adjudication or remediation file names.

```json
[
  {
    "id": "IRPT_BCKEND-C-S330",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T03:53:39Z",
    "one_line": "Round 117 rows dismissed: D2-W278-S1 (each function built from one commit, 361c44fa9d; a build fact), D2-W278-S2 (ARMED, disarmed: the candidate entries landed in the source map @5c35a6f9f9 before any build; narrative and status read EQUAL, the adapter differs only in artifact_sha256), D2-W278-S6 (the worker's reading of 'import-and-call replay', accepted at the issuer's re-grade), D2-S61 (the ruling record for D2-S60, which stays open), D2-W281-S1 (the read that feeds D2-S60), D2-W279-S1 (a device python note), D2-S63 (a stray untracked file with no client data), D2-S64 (the r114 check re-cut @cdb4fec479; the pins read), and this seat's read row D2-S67.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-D2-W278-S1",
      "IRPT_BCKEND-D2-W278-S2",
      "IRPT_BCKEND-D2-W278-S6",
      "IRPT_BCKEND-D2-S61",
      "IRPT_BCKEND-D2-W281-S1",
      "IRPT_BCKEND-D2-W279-S1",
      "IRPT_BCKEND-D2-S63",
      "IRPT_BCKEND-D2-S64",
      "IRPT_BCKEND-D2-S67"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 117 is terminal (4 of 4 complete, 0 judgment). Round 118 (TO-IB-pr-420) is issued and not applied. D2-S60 is ARMED until the applies land.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W278-S1, D2-W278-S2, D2-W278-S6, D2-S61, D2-W281-S1, D2-W279-S1, D2-S63, D2-S64, D2-S67",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_117_P_DRAIN_END_20261011.md @57a120767a (msg 4020)",
        "this seat's read of infra/aws/lambda/ci/lambda-source-map.json at HEAD (last commit 5c35a6f9f9) against deliverables/0.9.0_WK_IRPT_BCKEND~278/candidate_source_map.json: irpt-narrative and irpt-status entries EQUAL; irpt-performance-adapter equal except artifact_sha256 (candidate o/643qVE..., the live hash; map 9kYLdR64...)",
        "this seat's read of checks/r114/p114_cells.py (last commit cdb4fec479): IB-pr-417's digests 8b482c8d, 73f33c3c, fe4000cb and pin 4b008d15 present; IB-pr-410's 1e8ff309, 96925f38 and 9b7256a99f absent; 47be54d6 appears once, in a comment",
        "this seat's live reads 2026-10-11T03:53:39Z: irpt-performance-adapter CodeSha256 o/643qVE... LastModified 2026-10-09T07:41:59Z; irpt-narrative iEwSFL34... 2026-10-09T14:48:05Z; irpt-status t6OJTCcm... 2026-10-09T18:02:51Z -- none applied since round 117"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A build fact, a disarm read at HEAD, an accepted reading, a ruling or read record, a device note, a stray file, or a repaired check."
  }
]
```
