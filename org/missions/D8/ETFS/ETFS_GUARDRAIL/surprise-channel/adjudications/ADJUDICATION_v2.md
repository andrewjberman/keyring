# ETFS_GUARDRAIL -- closure compile, dismissals only

<sweep_watermark>2026-10-01T11:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-01 ~11:1xZ. Trigger: 1.0.0_SA_CTO 103672 (RULINGS batch 77 @4b9e65f744): the project is closed, so its compile is DISMISSALS ONLY and no remediation row is added to this channel. 8 item(s) are dismissed by the 2 row(s) below, 8 of them BLOCKING or ARMED. Each was graduated by an earlier adjudication row and read 'graduated with no remediation row' to the gate's rowlessness limb. Items of this channel whose hazard is live today, or was not read, are NOT dismissed here; they are listed in the review. Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md.

```json
[
  {
    "id": "ETFS_GUARDRAIL-C-S29",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T11:10:00Z",
    "one_line": "7 item(s) that C-S2 graduated carry no remediation row (W1-S1, W1-S2, W1-S3, W2-S3, W2-S4, W2-S5, W2-S6); they were closed in that row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_GUARDRAIL-W1-S1",
      "ETFS_GUARDRAIL-W1-S2",
      "ETFS_GUARDRAIL-W1-S3",
      "ETFS_GUARDRAIL-W2-S3",
      "ETFS_GUARDRAIL-W2-S4",
      "ETFS_GUARDRAIL-W2-S5",
      "ETFS_GUARDRAIL-W2-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The adjudication row C-S2 graduated these items and, in the same row, recorded each remedied and closed inside the round on acts read at this seat at the time. The convention then put a worker-form item's clocks on the adjudication row and wrote no remediation row for it, which the gate's rowlessness limb now reads as graduated with no row. Nothing about them was re-read today.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "adjudication row ETFS_GUARDRAIL-C-S2 (ADJUDICATION_v1.md): its own text",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Closed at C-S2 on the acts that row names; no hazard remains to carry and no remediation row is owed."
  },
  {
    "id": "ETFS_GUARDRAIL-C-S30",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T11:10:00Z",
    "one_line": "1 item(s) that C-S6 graduated carry no remediation row (S4); the hazard is not live today, on this seat's read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_GUARDRAIL-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The ledger tool now carries a hand-written section through its re-renders: commit a4b8ac93e0 (1.0.0_SA_CTO, 2026-09-15) keeps the entry's Sign-off section, and .tools/deploy_ledger.py:255 at HEAD states the rule ('Never hand-edit an entry -- except its ## Sign-off section').",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log -1 a4b8ac93e0 and .tools/deploy_ledger.py:255 at HEAD (this seat, 2026-10-01)",
        "the same repair closed ADVI_FIRMBKTS-S7 today (REMEDIATION_v1.md there)",
        "adjudication row ETFS_GUARDRAIL-C-S6 (ADJUDICATION_v1.md): its own text",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Repaired in the tool; the NEVER-2 hand section is no longer deleted by the next tool call when it is written under Sign-off."
  }
]
```
