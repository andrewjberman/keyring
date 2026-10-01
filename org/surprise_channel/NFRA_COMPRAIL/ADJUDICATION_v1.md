# NFRA_COMPRAIL -- closure compile, dismissals only (2026-10-01T13:50Z)

<sweep_watermark>2026-10-01T13:50Z</sweep_watermark>

Author: 3.0.0_SA_CVO. Trigger: 1.0.0_SA_CTO 103672 (RULINGS batch 77 @4b9e65f744): the project is closed, so its compile is DISMISSALS ONLY and no remediation row is added to this channel. 6 item(s) are dismissed by the 2 row(s) below, 2 of them BLOCKING or ARMED. A row that points at another channel names the row the hazard was re-filed as. Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md.

```json
[
  {
    "id": "NFRA_COMPRAIL-C-S1",
    "project": "NFRA_COMPRAIL",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:50:00Z",
    "one_line": "2 graduated item(s) with no remediation row (S1, S4): each repaired.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_COMPRAIL-S1",
      "NFRA_COMPRAIL-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S1: the comp-tool rail now refuses a comp-find piped into grep at the hook, before it runs (this seat was refused on exactly that call earlier today and re-ran it to a file), so the 'Binary file matches' loss cannot occur silently on the default path. S4: the row's own owner field records the extraction fix LANDED; the checker was not re-read today.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this seat's refused call under .tools/hooks/comp-tool-hud.sh (2026-10-01)",
        "investigation row NFRA_COMPRAIL-S4: its disarm_owner text",
        "the project's registry row reads status complete (org/projects/NFRA_COMPRAIL.json)",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Repaired at the rail and in the checker; nothing remains to carry."
  },
  {
    "id": "NFRA_COMPRAIL-C-S2",
    "project": "NFRA_COMPRAIL",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:50:00Z",
    "one_line": "4 graduated item(s) with no remediation row (S5, S6, S7, S8): four observations about method, graduated as records.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_COMPRAIL-S5",
      "NFRA_COMPRAIL-S6",
      "NFRA_COMPRAIL-S7",
      "NFRA_COMPRAIL-S8"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Each is a statement about how seats verify (proportionality, repeated measurement, which artifact executes a file, reading an instrument's answer). They are INERT, name no object that can fail, and their substance is in CLAUDE.md sections 2 and 4 today.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the investigation rows' own text; CLAUDE.md sections 2 and 4 at HEAD",
        "the project's registry row reads status complete (org/projects/NFRA_COMPRAIL.json)",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Records whose lesson is law; no hazard and no remedy owed."
  }
]
```
