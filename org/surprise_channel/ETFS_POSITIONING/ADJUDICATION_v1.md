# ETFS_POSITIONING -- closure compile, dismissals only (2026-10-01T13:40Z)

<sweep_watermark>2026-10-01T13:40Z</sweep_watermark>

Author: 3.0.0_SA_CVO. Trigger: 1.0.0_SA_CTO 103672 (RULINGS batch 77 @4b9e65f744): the project is closed, so its compile is DISMISSALS ONLY and no remediation row is added to this channel. 20 item(s) are dismissed by the 3 row(s) below, 16 of them BLOCKING or ARMED. A row that points at another channel names the row the hazard was re-filed as. Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md.

```json
[
  {
    "id": "ETFS_POSITIONING-C-S1",
    "project": "ETFS_POSITIONING",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:40:00Z",
    "one_line": "2 graduated item(s) with no remediation row (Z-S1, Z-S2): live today; re-filed as ESTATE_GOVERNANCE-S27.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_POSITIONING-Z-S1",
      "ETFS_POSITIONING-Z-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "etf_daily_pull.py:122-125 still derives the as-of from pandas BDay(-1) and checks it against the same expression.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the lines at HEAD (this seat, 2026-10-01)",
        "ESTATE_GOVERNANCE-S27, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @b6e4916f7e",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S27 in the estate-wide channel (the home accepted at 1.0.0_SA_CTO RULINGS batch 85 @afc17452e8); the hazard is carried there with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "ETFS_POSITIONING-C-S2",
    "project": "ETFS_POSITIONING",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:40:00Z",
    "one_line": "9 graduated item(s) with no remediation row (S3, S5, S6, S9, S12, Z-S8, S1, Z-S4, Z-S5): each repaired, or its condition gone.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_POSITIONING-S3",
      "ETFS_POSITIONING-S5",
      "ETFS_POSITIONING-S6",
      "ETFS_POSITIONING-S9",
      "ETFS_POSITIONING-S12",
      "ETFS_POSITIONING-Z-S8",
      "ETFS_POSITIONING-S1",
      "ETFS_POSITIONING-Z-S4",
      "ETFS_POSITIONING-Z-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S3: infra/aws/terraform/shared-infra/s3-portal-v2-import.tf now names platinum/advi (lines 94 and 180), so the desired policy carries the grant. S5: mdpf_egress_publisher.tf's header was corrected on 2026-08-21. S6: `qualified_arn` was dropped from the router's ignore_changes (portal-auth/lambda-edge.tf:226-244). S9: the served ETF artifact is application/json with no Content-Encoding. S12: bookSet.ts:40-41 records the aggregate-denominator coupling as removed. Z-S8: DIVZ's holdings are served. S1, Z-S4 and Z-S5: bbg/ holds 29 dated landings through 2026-09-30, so the first-landing ambiguity and the no-prior-prefix floor no longer arise.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the Terraform and portal files at HEAD; head-object and s3 cp of the served artifact; a delimiter listing of bbg/ (this seat, 2026-10-01)",
        "not re-run: a terraform plan in shared-infra or portal-auth, so S3 and S6 rest on the source",
        "the project's registry row reads status complete (org/projects/ETFS_POSITIONING.json)",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The defect each row measured is not in the source or the served object today."
  },
  {
    "id": "ETFS_POSITIONING-C-S3",
    "project": "ETFS_POSITIONING",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:40:00Z",
    "one_line": "9 graduated item(s) with no remediation row (S2, S4, S8, Z-S6, Z-S7, S10, S11, S13, S14): traps now in doctrine, cut-side items, and records.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_POSITIONING-S2",
      "ETFS_POSITIONING-S4",
      "ETFS_POSITIONING-S8",
      "ETFS_POSITIONING-Z-S6",
      "ETFS_POSITIONING-Z-S7",
      "ETFS_POSITIONING-S10",
      "ETFS_POSITIONING-S11",
      "ETFS_POSITIONING-S13",
      "ETFS_POSITIONING-S14"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S2 (cmd.exe /c mangled by MSYS) is the class CLAUDE.md's Git section now guards with msys_argv_guard and 'echo the argument back'. S4 (a commit on no remote branch on 2026-08-21) is long overtaken. S8, Z-S6, Z-S7 and S10 are defects of this project's own census and acceptance criteria. S11 and S13 are records. S14 is recorded disarmed in its own row.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLAUDE.md Git section at HEAD; the investigation rows' own text",
        "the project's registry row reads status complete (org/projects/ETFS_POSITIONING.json)",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The project finished; nothing here can be inherited by a further order, and the trap is doctrine."
  }
]
```
