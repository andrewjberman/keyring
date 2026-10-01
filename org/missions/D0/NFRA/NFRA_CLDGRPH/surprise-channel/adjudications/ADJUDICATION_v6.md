# NFRA_CLDGRPH -- closure compile, dismissals only (2026-10-01T12:20Z)

<sweep_watermark>2026-10-01T12:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO. Trigger: 1.0.0_SA_CTO 103672 (RULINGS batch 77 @4b9e65f744): the project is closed, so its compile is DISMISSALS ONLY and no remediation row is added to this channel. 58 item(s) are dismissed by the 16 row(s) below, 56 of them BLOCKING or ARMED. A row that points at another channel names the row the hazard was re-filed as. Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md.

```json
[
  {
    "id": "NFRA_CLDGRPH-C-S102",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "2 graduated item(s) with no remediation row (W1-S11, W1-S27): live today; re-filed as ESTATE_GOVERNANCE-S12.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-W1-S11",
      "NFRA_CLDGRPH-W1-S27"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": ".tools/halt-gate-check.sh still carries 0 occurrences of OPAL_AGENT_SERIAL; the refusal fails closed and prints its remedy.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the token count at HEAD (this seat, 2026-10-01); graduated at C-S24 and C-S31",
        "ESTATE_GOVERNANCE-S12, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @22746eedf5",
        "project.json close_note: closed 2026-09-23 on Andrew's word, not a graded close",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S12 in the estate-wide channel; the hazard is carried there with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "NFRA_CLDGRPH-C-S103",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "1 graduated item(s) with no remediation row (W2-S19): live today; re-filed as ESTATE_GOVERNANCE-S13.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-W2-S19"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": ".tools/proof-of-spec-check.py:274 and :279 still test a byte substring for an `introduces` token.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the two lines at HEAD (this seat, 2026-10-01); graduated at C-S24",
        "ESTATE_GOVERNANCE-S13, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @22746eedf5",
        "project.json close_note: closed 2026-09-23 on Andrew's word, not a graded close",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S13 in the estate-wide channel; the hazard is carried there with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "NFRA_CLDGRPH-C-S104",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "1 graduated item(s) with no remediation row (W1-S24): live today; re-filed as ESTATE_GOVERNANCE-S14.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-W1-S24"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "No doctrine line states that the vendored jq emits CRLF: CLAUDE.md mentions jq once and the annex pairs jq with CRLF nowhere.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLAUDE.md:257 and an annex search at HEAD (this seat, 2026-10-01); graduated at C-S24",
        "ESTATE_GOVERNANCE-S14, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @22746eedf5",
        "project.json close_note: closed 2026-09-23 on Andrew's word, not a graded close",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S14 in the estate-wide channel; the hazard is carried there with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "NFRA_CLDGRPH-C-S105",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "4 graduated item(s) with no remediation row (W4-S4, W4-S6, W6-S3, W7-S2): live today; re-filed as ESTATE_GOVERNANCE-S15.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-W4-S4",
      "NFRA_CLDGRPH-W4-S6",
      "NFRA_CLDGRPH-W6-S3",
      "NFRA_CLDGRPH-W7-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The graph call manifest still names the absent kuzu_stitch_db at its line 1290, 11 of its 129 entries are comp-aws calls with status canonical, and three modules still describe the local engine.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "manifest and module reads at HEAD (this seat, 2026-10-01); graduated at C-S50 and C-S56",
        "ESTATE_GOVERNANCE-S15, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @22746eedf5",
        "project.json close_note: closed 2026-09-23 on Andrew's word, not a graded close",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S15 in the estate-wide channel; the hazard is carried there with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "NFRA_CLDGRPH-C-S106",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "14 graduated item(s) with no remediation row (W2-S68, W2-S70, S96, S97, S102, W2-S61, W1-S37, W1-S38, S110, S113, W1-S39, S111, W3-S18, W1-S47): live today; re-filed as ESTATE_GOVERNANCE-S16.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-W2-S68",
      "NFRA_CLDGRPH-W2-S70",
      "NFRA_CLDGRPH-S96",
      "NFRA_CLDGRPH-S97",
      "NFRA_CLDGRPH-S102",
      "NFRA_CLDGRPH-W2-S61",
      "NFRA_CLDGRPH-W1-S37",
      "NFRA_CLDGRPH-W1-S38",
      "NFRA_CLDGRPH-S110",
      "NFRA_CLDGRPH-S113",
      "NFRA_CLDGRPH-W1-S39",
      "NFRA_CLDGRPH-S111",
      "NFRA_CLDGRPH-W3-S18",
      "NFRA_CLDGRPH-W1-S47"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The served graph answers 0 STORED_IN edges, SERVED_FROM 27 on S3_BUCKET_POLICY nodes and OWNED_BY 232 on S3_BUCKET nodes, while derive_stitch.py:339 still emits STORED_IN. The identity seam, the retirement's four conditions and the unexplained mover are one open question on one plane, and the producer's input still contains its prior output for edge kinds other than STORED_IN.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-kuzu, two Cypher reads at vintage 2026-10-01T12:02Z (this seat); the emitter read at HEAD; graduated at C-S60, C-S65, C-S79 and C-S85",
        "ESTATE_GOVERNANCE-S16, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @22746eedf5",
        "project.json close_note: closed 2026-09-23 on Andrew's word, not a graded close",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S16 in the estate-wide channel; the hazard is carried there with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "NFRA_CLDGRPH-C-S107",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "1 graduated item(s) with no remediation row (W3-S10): live today; re-filed as ESTATE_GOVERNANCE-S17.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-W3-S10"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The producer is no longer dead (7 of the last 8 nightly builds SUCCEEDED) but the 2026-10-01 03:00Z build FAILED on derive_stitch.py exit 2, and a failed night still leaves the previous artifact in place.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "codebuild batch-get-builds over the last 8 builds (this seat, 2026-10-01 11:56Z); graduated at C-S34",
        "ESTATE_GOVERNANCE-S17, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @22746eedf5",
        "project.json close_note: closed 2026-09-23 on Andrew's word, not a graded close",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S17 in the estate-wide channel; the hazard is carried there with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "NFRA_CLDGRPH-C-S108",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "1 graduated item(s) with no remediation row (W1-S8): live today; re-filed as ESTATE_GOVERNANCE-S18.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-W1-S8"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "No rule and no schedule named for the resource-summaries producer exists on either scheduling service.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "events list-rules and scheduler list-schedules by name (this seat, 2026-10-01); graduated at C-S24",
        "ESTATE_GOVERNANCE-S18, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @22746eedf5",
        "project.json close_note: closed 2026-09-23 on Andrew's word, not a graded close",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S18 in the estate-wide channel; the hazard is carried there with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "NFRA_CLDGRPH-C-S109",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "1 graduated item(s) with no remediation row (W3-S16): live today; re-filed as ESTATE_GOVERNANCE-S19.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-W3-S16"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "infra/aws/globgrph/tests/test_kuzu_incremental_refresh.py still collects zero tests under pytest.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the collect-only run (this seat, 2026-10-01); graduated at C-S48",
        "ESTATE_GOVERNANCE-S19, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @22746eedf5",
        "project.json close_note: closed 2026-09-23 on Andrew's word, not a graded close",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S19 in the estate-wide channel; the hazard is carried there with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "NFRA_CLDGRPH-C-S110",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "1 graduated item(s) with no remediation row (W1-S43): live today; re-filed as ESTATE_GOVERNANCE-S20.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-W1-S43"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The graph bucket is still unversioned, and round 9's writer-side key was filed and not implemented.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api get-bucket-versioning, empty (this seat, 2026-10-01); graduated at C-S72; its remediation row exists only in the untracked draft REMEDIATION_v4.md",
        "ESTATE_GOVERNANCE-S20, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @22746eedf5",
        "project.json close_note: closed 2026-09-23 on Andrew's word, not a graded close",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S20 in the estate-wide channel; the hazard is carried there with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "NFRA_CLDGRPH-C-S111",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "3 graduated item(s) with no remediation row (W2-S72, S104, S106): live today; re-filed as ESTATE_GOVERNANCE-S21.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-W2-S72",
      "NFRA_CLDGRPH-S104",
      "NFRA_CLDGRPH-S106"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The alert topic still carries an SMS subscription beside its queue; the call was reserved for Andrew and the project closed with no answer on record. The old hold on this project's own derives ended with the project.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "sns list-subscriptions-by-topic, protocols only (this seat, 2026-10-01); graduated at C-S60",
        "ESTATE_GOVERNANCE-S21, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @22746eedf5",
        "project.json close_note: closed 2026-09-23 on Andrew's word, not a graded close",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S21 in the estate-wide channel; the hazard is carried there with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "NFRA_CLDGRPH-C-S112",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "6 graduated item(s) with no remediation row (W2-S17, W2-S18, W2-S20, W2-S23, W2-S2, W2-S10): each repaired or gone at HEAD.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-W2-S17",
      "NFRA_CLDGRPH-W2-S18",
      "NFRA_CLDGRPH-W2-S20",
      "NFRA_CLDGRPH-W2-S23",
      "NFRA_CLDGRPH-W2-S2",
      "NFRA_CLDGRPH-W2-S10"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W2-S17: no file under .tools/comp_debt names kuzu_stitch_db and the directory is absent. W2-S18: pipescript-suite-check.sh:196-202 now resolves a linked worktree's git directory. W2-S20: test_comp_cluster_cli.py:200-204 checks the portal's toplevel and skips when it is not the portal. W2-S23: the only canonical manifest entry that calls comp-kuzu is cloud.read.served_vintage, and it answered this seat today; `--mode` survives only in the prose of consolidated entries. W2-S2: alb.tf:93-97 now DECLARES the access_logs block the live load balancer carries. W2-S10: waf.tf:259 and :300 declare the two IP sets an unscoped plan was deleting.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the six sites at HEAD (this seat, 2026-10-01); graduated at C-S24",
        "not re-run: an unscoped terraform plan in opal-gateway, so W2-S2 and W2-S10 rest on the declarations, not on a plan",
        "project.json close_note: closed 2026-09-23 on Andrew's word, not a graded close",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The defect each row measured is no longer in the source it named."
  },
  {
    "id": "NFRA_CLDGRPH-C-S113",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "3 graduated item(s) with no remediation row (W3-S3, W3-S4, W3-S5): telemetry is not the oracle, by rule.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-W3-S3",
      "NFRA_CLDGRPH-W3-S4",
      "NFRA_CLDGRPH-W3-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The three telemetry defects stand in the hook (post-tool-telemetry.sh:82-83 still reads the session serial file before OPAL_AGENT_SERIAL), but no control reads worker telemetry: CLAUDE.md rule 27 says a worker writes no telemetry and L7 reads from git.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the hook at HEAD and CLAUDE.md rule 27 (this seat, 2026-10-01); graduated at C-S24, which already named the spine's reading as the standing answer",
        "project.json close_note: closed 2026-09-23 on Andrew's word, not a graded close",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Nothing consumes the signal the three rows show to be unreliable; the rule that made it so is in force."
  },
  {
    "id": "NFRA_CLDGRPH-C-S114",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "6 graduated item(s) with no remediation row (W3-S7, W3-S8, W1-S30, W2-S35, W2-S37, W3-S11): each repaired at HEAD, or its object is gone.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-W3-S7",
      "NFRA_CLDGRPH-W3-S8",
      "NFRA_CLDGRPH-W1-S30",
      "NFRA_CLDGRPH-W2-S35",
      "NFRA_CLDGRPH-W2-S37",
      "NFRA_CLDGRPH-W3-S11"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W3-S7 and W3-S8: infra/aws/globgrph/_provenance.py now requires both claim keywords in write_manifest and renders a loud `!! provenance_claim: absent`. W1-S30: serving.tf:11-22 now says all seven families pin by digest and none rides :latest. W2-S35: gen_tool_classification.py:143 describes the served projection. W2-S37: gen_tool_registry.py:36 strips both .py and .sh. W3-S11: the local stitch store it describes no longer exists.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the five files at HEAD and the absent directory (this seat, 2026-10-01); graduated at C-S27, C-S31, C-S38 and C-S34",
        "project.json close_note: closed 2026-09-23 on Andrew's word, not a graded close",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Repaired in source, or moot with the store's removal."
  },
  {
    "id": "NFRA_CLDGRPH-C-S115",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "3 graduated item(s) with no remediation row (W2-S40, W2-S63, W2-S78): the literal portal ref is gone from the workflow.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-W2-S40",
      "NFRA_CLDGRPH-W2-S63",
      "NFRA_CLDGRPH-W2-S78"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": ".github/workflows/stitch-source-push.yml:64-76 (round 9, TO-CG-I-5) replaced the literal portal sha with a fail-closed resolver of the gitlink. Whether that workflow route has ever published correctly is a separate finding of the same order (row W4-S10, owner 0.0.0_AB_MSTR), not carried by these three.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the workflow at HEAD (this seat, 2026-10-01); graduated at C-S49, C-S60 and C-S77",
        "project.json close_note: closed 2026-09-23 on Andrew's word, not a graded close",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The stale literal these rows armed was removed in source."
  },
  {
    "id": "NFRA_CLDGRPH-C-S116",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "8 graduated item(s) with no remediation row (W2-S45, W2-S49, W2-S53, W2-S56, W2-S57, W2-S46, S114, W1-S46): cut-side items of a project that will not be cut again.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-W2-S45",
      "NFRA_CLDGRPH-W2-S49",
      "NFRA_CLDGRPH-W2-S53",
      "NFRA_CLDGRPH-W2-S56",
      "NFRA_CLDGRPH-W2-S57",
      "NFRA_CLDGRPH-W2-S46",
      "NFRA_CLDGRPH-S114",
      "NFRA_CLDGRPH-W1-S46"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Each is a reading of the world by a cut of this project (a taxonomy answered by the unification, family names that did not exist, an order's wrong path, an index that counted two prose-only cell ids, a census grant that aged). C-S60 already records six of them closed in substance.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "adjudication rows C-S60, C-S70 and C-S84: their own text",
        "project.json close_note: closed 2026-09-23 on Andrew's word, not a graded close",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The project is closed; no further issuance can inherit these."
  },
  {
    "id": "NFRA_CLDGRPH-C-S117",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "3 graduated item(s) with no remediation row (W1-S44, W3-S19, W4-S7): fixed at the writer, or a correction record.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-W1-S44",
      "NFRA_CLDGRPH-W3-S19",
      "NFRA_CLDGRPH-W4-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W1-S44: the dangling-edge check's key set is rebuilt after the collapse (round 9 TO-CG-I-2, efbddbccd6, an ancestor of CLOUD HEAD). W3-S19: the upsert collision that `nodes_deleted` could not bound is closed at the writer (TO-CG-I-1, e86c4fb778); the running updater's lambda_function.py hashes equal to HEAD and the served graph carries both S3_BUCKET (41) and S3_BUCKET_POLICY (17) nodes. W4-S7 corrected a census record's prediction; it describes no failure.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git merge-base for both commits; this seat's download of the updater; comp-kuzu node counts (2026-10-01); graduated at C-S73, C-S80 and C-S81",
        "project.json close_note: closed 2026-09-23 on Andrew's word, not a graded close",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "No hazard remains in the form the rows describe. Whether the stitch build's source snapshot carries efbddbccd6 was not read."
  }
]
```
