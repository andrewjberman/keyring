# DSGN_IRPTV1: CVO adjudication, round 22 and the slug for rounds 17 to 22

<sweep_watermark>2026-10-11T16:41Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T16:41:38Z. Input: msgs 5345 and 5351 (IV-e-104 drained @9cc17c490e, portal DEV c3a03c24; IV-e-103 drained @5a150bf718; round 22 MAY-CLOSE). No judgment criterion.
8 rows dismissed below. 11 rows graduate OPEN in `remediations/REMEDIATION_v9.md`.

```json
[
  {
    "id": "DSGN_IRPTV1-C-S78",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T16:41:38Z",
    "one_line": "Rounds 17 to 22 slug, rows dismissed: D2-W53-S7 with D2-W58-S8 (a 130 percent weight; the driver rewrote shared fixture objects, the page computes no weight, and with the objects copied it prints 65.00 and 10.00 -- the issuer's read of the fixed screenshot), D2-W54-S1 with D2-W58-S6 (the regeneration test red on the generator's throw; passes after IRPT_BCKEND's IB-pr-437 and the regenerated wire file, by the issuer's suite run), D2-W58-S5 and D2-W58-S7 (which ids were red at the base and why; both causes are repaired), D2-W53-S12 (this box lacks one python package, so one branch ran against a stub; a box note), and this seat's read row D2-S19. Twelve rows graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "DSGN_IRPTV1-D2-W53-S7",
      "DSGN_IRPTV1-D2-W58-S8",
      "DSGN_IRPTV1-D2-W54-S1",
      "DSGN_IRPTV1-D2-W58-S6",
      "DSGN_IRPTV1-D2-W58-S5",
      "DSGN_IRPTV1-D2-W58-S7",
      "DSGN_IRPTV1-D2-W53-S12",
      "DSGN_IRPTV1-D2-S19"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "No DSGN_IRPTV1 order is open (to-check). The two BLOCKING rows are dismissed on the issuer's suite run, not re-run by this seat.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W53-S7, D2-W58-S8, D2-W54-S1, D2-W58-S6, D2-W58-S5, D2-W58-S7, D2-W53-S12, D2-S19",
        "msgs 5345 and 5351 (IV-e-104 drained @9cc17c490e, portal DEV c3a03c24; IV-e-103 drained @5a150bf718; round 22 MAY-CLOSE)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A harness defect explained, a red test repaired upstream and re-run, base-count notes, a box note, and a read row."
  }
]
```
