# ETFS_INGEST -- closure compile, dismissals only (2026-10-01T13:40Z)

<sweep_watermark>2026-10-01T13:40Z</sweep_watermark>

Author: 3.0.0_SA_CVO. Trigger: 1.0.0_SA_CTO 103672 (RULINGS batch 77 @4b9e65f744): the project is closed, so its compile is DISMISSALS ONLY and no remediation row is added to this channel. 28 item(s) are dismissed by the 6 row(s) below, 18 of them BLOCKING or ARMED. A row that points at another channel names the row the hazard was re-filed as. Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md.

```json
[
  {
    "id": "ETFS_INGEST-C-S1",
    "project": "ETFS_INGEST",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:40:00Z",
    "one_line": "1 graduated item(s) with no remediation row (Z-S10): live today; re-filed as ESTATE_GOVERNANCE-S28.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_INGEST-Z-S10"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Rule opal-assets-silver-etf-sweep-daily is ENABLED and its name is in no tracked .tf file under infra/aws.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "events list-rules and a token read over tracked .tf files (this seat, 2026-10-01)",
        "ESTATE_GOVERNANCE-S28, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @b6e4916f7e",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S28 in the estate-wide channel (the home accepted at 1.0.0_SA_CTO RULINGS batch 85 @afc17452e8); the hazard is carried there with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "ETFS_INGEST-C-S2",
    "project": "ETFS_INGEST",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:40:00Z",
    "one_line": "1 graduated item(s) with no remediation row (Z-S27): live today; re-filed as ESTATE_GOVERNANCE-S29.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_INGEST-Z-S27"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The served ETF payload still has no field separating an absent value from a failed fetch.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3 cp of platinum/etfs/positioning_data.json and a token census (this seat, 2026-10-01)",
        "ESTATE_GOVERNANCE-S29, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @b6e4916f7e",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S29 in the estate-wide channel (the home accepted at 1.0.0_SA_CTO RULINGS batch 85 @afc17452e8); the hazard is carried there with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "ETFS_INGEST-C-S3",
    "project": "ETFS_INGEST",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:40:00Z",
    "one_line": "2 graduated item(s) with no remediation row (Z-S23, Z-S17): live today; re-filed as ESTATE_GOVERNANCE-S30.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_INGEST-Z-S23",
      "ETFS_INGEST-Z-S17"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "opal-data-portal-v2 still expires noncurrent versions after 14 days and no doctrine line says so; comp-closure still compares raw bytes, by its own header.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api get-bucket-lifecycle-configuration; .tools/comp-closure:17-29 at HEAD (this seat, 2026-10-01)",
        "ESTATE_GOVERNANCE-S30, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @b6e4916f7e",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S30 in the estate-wide channel (the home accepted at 1.0.0_SA_CTO RULINGS batch 85 @afc17452e8); the hazard is carried there with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "ETFS_INGEST-C-S4",
    "project": "ETFS_INGEST",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:40:00Z",
    "one_line": "1 graduated item(s) with no remediation row (Z-S5): live today; re-filed as ESTATE_GOVERNANCE-S31.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_INGEST-Z-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Carried on the old row's measurement: nothing was read today that shows a check on the constituents leg. The landing itself is whole at the frontier (29 dated prefixes through 2026-09-30).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api list-objects-v2 on opal-data-etfs/bbg/ (this seat, 2026-10-01)",
        "ESTATE_GOVERNANCE-S31, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @b6e4916f7e",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S31 in the estate-wide channel (the home accepted at 1.0.0_SA_CTO RULINGS batch 85 @afc17452e8); the hazard is carried there with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "ETFS_INGEST-C-S5",
    "project": "ETFS_INGEST",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:40:00Z",
    "one_line": "9 graduated item(s) with no remediation row (Z-S1, Z-S14, Z-S7, Z-S11, Z-S21, Z-S41, Z-S45, Z-S16, Z-S25): each repaired, on a read of the code or the served object.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_INGEST-Z-S1",
      "ETFS_INGEST-Z-S14",
      "ETFS_INGEST-Z-S7",
      "ETFS_INGEST-Z-S11",
      "ETFS_INGEST-Z-S21",
      "ETFS_INGEST-Z-S41",
      "ETFS_INGEST-Z-S45",
      "ETFS_INGEST-Z-S16",
      "ETFS_INGEST-Z-S25"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Z-S1: the deployed etfs-netassets-daily package defines fetch_trueshares_holdings and calls it once, with TS_HOLDINGS_ENABLED=1, and DIVZ's holdings are in today's served payload. Z-S14: etf_daily_pull.py:143-154 treats is_cash as null-bearing. Z-S7: the source map's artifact_sha256 for etfs-netassets-daily equals the live CodeSha256. Z-S11: etf-positioning-producer has a source-map entry. Z-S21 records its own fix. Z-S41: today's payload carries 8 of 8 return windows on DIVZ's first holding. Z-S45: portal HoldingsTab.tsx:715 lists the same eight periods (source read, page not rendered). Z-S16: the payload carries data_as_of_spread beside data_as_of. Z-S25: two keys share the leaf today, the Models artifact and the ETF artifact, each written today.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this seat's download of the function package, s3 cp of the served object, head-object of both leaves, and the source files at HEAD (2026-10-01)",
        "the project's registry row reads status complete (org/projects/ETFS_INGEST.json)",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The defect each row measured is not in the code that runs or the object that is served today."
  },
  {
    "id": "ETFS_INGEST-C-S6",
    "project": "ETFS_INGEST",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:40:00Z",
    "one_line": "14 graduated item(s) with no remediation row (Z-S15, Z-S22, Z-S19, Z-S24, Z-S8, Z-S4, Z-S12, Z-S13, Z-S9, Z-S20, Z-S26, Z-S28, Z-S46, Z-S18): rulings, cut-side items and records of a finished project.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_INGEST-Z-S15",
      "ETFS_INGEST-Z-S22",
      "ETFS_INGEST-Z-S19",
      "ETFS_INGEST-Z-S24",
      "ETFS_INGEST-Z-S8",
      "ETFS_INGEST-Z-S4",
      "ETFS_INGEST-Z-S12",
      "ETFS_INGEST-Z-S13",
      "ETFS_INGEST-Z-S9",
      "ETFS_INGEST-Z-S20",
      "ETFS_INGEST-Z-S26",
      "ETFS_INGEST-Z-S28",
      "ETFS_INGEST-Z-S46",
      "ETFS_INGEST-Z-S18"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Z-S15, Z-S22 and Z-S12 are vocabulary and convention questions the round ruled (the registry row records the sector chip and the industry group rendered in one cell, and the is_cash amendment). Z-S19, Z-S4, Z-S13 and Z-S9 are defects of this project's own orders, criteria and brief. Z-S24 and Z-S8 describe a placement row and a drive loop of 2026-08-24 that no longer exist in that form. Z-S20, Z-S26, Z-S28, Z-S46 and Z-S18 are corrections and stated dependencies with nothing asked. None was re-read against the world today.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the investigation rows' own text (org/surprise_channel/ETFS_INGEST/INVESTIGATION_v1.Z.md); org/projects/ETFS_INGEST.json `blocking`",
        "the project's registry row reads status complete (org/projects/ETFS_INGEST.json)",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The project finished with zero open task orders on 2026-08-29; no further order can inherit a cut-side item, and the records ask for nothing."
  }
]
```
