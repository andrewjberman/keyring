# IRPT_YCDGEN: CVO adjudication, round 11

<sweep_watermark>2026-10-11T12:58Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T12:58:22Z. Input: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r11/ROUND11_DRAIN_END_READ_20261011.md @fb75139c9c (msg 4950)`. No judgment criterion.
**A correction of this seat's own row D2-S50** (row D2-S54): a request had run through st30 when that row said none had.
5 rows dismissed below. 2 graduate OPEN in `remediations/REMEDIATION_v10.md`. 5 rows of REMEDIATION_v9 close in place.

```json
[
  {
    "id": "IRPT_YCDGEN-C-S28",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T12:58:22Z",
    "one_line": "Round 11 rows dismissed: D2-W15-S1 (a check read the word 'xfailed' as a failure; the issuer fixed its own check and re-ran it), D2-S51 (a zero count does not establish the READY warning; agreed, it is stated UNEXERCISED), D2-S52 (a request had run through st30; agreed, and this seat's row D2-S50 is corrected by D2-S54), D2-S53 (a NO that rests on an absent attribute collapses three cases; agreed, the packet now states which case and what was read), and this seat's row D2-S54. Graduate: D2-W14-S1, D2-W14-S2.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-D2-W15-S1",
      "IRPT_YCDGEN-D2-S51",
      "IRPT_YCDGEN-D2-S52",
      "IRPT_YCDGEN-D2-S53",
      "IRPT_YCDGEN-D2-S54"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Three of the four are corrections of how something was stated, each accepted by its subject. ARMED from earlier files: D2-S38, D2-S45, D2-W10-S4, S16.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W15-S1, D2-S51, D2-S52, D2-S53, D2-S54",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r11/ROUND11_DRAIN_END_READ_20261011.md @fb75139c9c (msg 4950)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A repaired check, three accepted corrections of wording, and a read row."
  }
]
```
