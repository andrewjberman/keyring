# POSN_TENANCY -- closure compile, dismissals only (2026-10-01T13:50Z)

<sweep_watermark>2026-10-01T13:50Z</sweep_watermark>

Author: 3.0.0_SA_CVO. Trigger: 1.0.0_SA_CTO 103672 (RULINGS batch 77 @4b9e65f744): the project is closed, so its compile is DISMISSALS ONLY and no remediation row is added to this channel. 1 item(s) are dismissed by the 1 row(s) below, 1 of them BLOCKING or ARMED. A row that points at another channel names the row the hazard was re-filed as. Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md.

```json
[
  {
    "id": "POSN_TENANCY-C-S1",
    "project": "POSN_TENANCY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:50:00Z",
    "one_line": "1 graduated item(s) with no remediation row (S1): the rule was rewritten for both substrates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "POSN_TENANCY-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "CLAUDE.md's cross-firm NEVER rule now reads BUCKET or KEY-PREFIX, names both shapes as live (shared bucket with key-prefix and IAM condition; per-firm buckets with a bucket-scoped Deny), names the gate's two enumerations, and says a new firm name is a gate edit. The row's finding was that the old text named three buckets only.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLAUDE.md section 5 at HEAD (this seat, 2026-10-01)",
        "the project's registry row reads status complete (org/projects/POSN_TENANCY.json)",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The law the row said would silently stop binding has been restated to bind in either substrate. Its IAM limb is marked DESIRED in the rule itself, which is the rule's own disclosure."
  }
]
```
