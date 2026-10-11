# IRPT_YCDGEN: CVO adjudication, round 9

<sweep_watermark>2026-10-11T08:27Z</sweep_watermark>

Round 9 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T08:27:50Z. L8 input: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r9/ROUND9_DRAIN_END_READ_20261011.md @9982fb211e (msg 4481)`. No judgment criterion; no run of FWD-1; nothing deployed.
1 row dismissed below. D2-S44 graduates in `remediations/REMEDIATION_v8.md`: the page still states one sentence for two
causes. FWD-1 stands NOT MET. About 41 INERT rows of rounds 6 and 7 remain uncompiled.

```json
[
  {
    "id": "IRPT_YCDGEN-C-S23",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T08:27:50Z",
    "one_line": "Round 9: no row was filed by the round. Dismissed: this seat's read row D2-S43. Its second row D2-S44 (the page states one sentence for two causes and prints the stored string) graduates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-D2-S43"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 9 is terminal. ARMED, all owned by 2.0.0_SA_COO~G2 and unchanged: D2-S38, S16 and D2-W7-S1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row D2-S43",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r9/ROUND9_DRAIN_END_READ_20261011.md @9982fb211e (msg 4481)",
        "this seat's run of r8_checks.py f8fold at HEAD: no_rule -> NOT_IN_THIS_VERSION, no_row -> INPUT_MISSING:security_not_covered, R8-F8FOLD-OK",
        "this seat's read of infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py _reason_line at HEAD: a reason that starts with the NOT_HELD prefix returns ONE sentence for every cause, ending 'Reason: %s' with the stored string"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A read row."
  }
]
```
