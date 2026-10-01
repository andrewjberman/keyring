# NFRA_OUTSET -- closure compile, dismissals only (2026-10-01T12:20Z)

<sweep_watermark>2026-10-01T12:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO. Trigger: 1.0.0_SA_CTO 103672 (RULINGS batch 77 @4b9e65f744): the project is closed, so its compile is DISMISSALS ONLY and no remediation row is added to this channel. 10 item(s) are dismissed by the 8 row(s) below, 10 of them BLOCKING or ARMED. A row that points at another channel names the row the hazard was re-filed as. Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md.

```json
[
  {
    "id": "NFRA_OUTSET-C-S19",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "1 graduated item(s) with no remediation row (W1-S21): live today; re-filed as ESTATE_GOVERNANCE-S8.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_OUTSET-W1-S21"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "org/standards/PROOF_OF_SPEC.schema.json still closes `deployed_state` to three values, none of which describes a deploy-scope artifact committed and deliberately not deployed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the schema's enum at HEAD (this seat, 2026-10-01)",
        "ESTATE_GOVERNANCE-S8, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @531b115ff1",
        "adjudication row NFRA_OUTSET-C-S4 (ADJUDICATION_v1.md): its own text",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S8 in the estate-wide channel; the hazard is carried there, with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "NFRA_OUTSET-C-S20",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "1 graduated item(s) with no remediation row (W1-S17): live today; re-filed as ESTATE_GOVERNANCE-S9.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_OUTSET-W1-S17"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "`.tools/comp-heat:860-861` still returns the caller's `--sql` string as the statement to run and `.tools/_trino_fed.py` inspects nothing, under a docstring that says read-only.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "both files at HEAD (this seat, 2026-10-01)",
        "ESTATE_GOVERNANCE-S9, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @531b115ff1",
        "adjudication row NFRA_OUTSET-C-S4 (ADJUDICATION_v1.md): its own text",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S9 in the estate-wide channel; the hazard is carried there, with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "NFRA_OUTSET-C-S21",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "2 graduated item(s) with no remediation row (W1-S13, W2-S10): live as traps; re-filed together as ESTATE_GOVERNANCE-S10.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_OUTSET-W1-S13",
      "NFRA_OUTSET-W2-S10"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Neither trap (the `cd X && A & B` backgrounding that runs B in the main workspace; a copied or in-process comp-tool fail-softing on `__file__`) is stated in the worker definition or the annex. The stray file W1-S13's first limb named is gone from the main tree.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".claude/agents/worker.md and docs/doctrine/CLAUDE_ANNEX.md at HEAD; .scratch/os2_falsifier.txt absent (this seat, 2026-10-01)",
        "ESTATE_GOVERNANCE-S10, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @531b115ff1",
        "adjudication row NFRA_OUTSET-C-S4 (ADJUDICATION_v1.md): its own text",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S10 in the estate-wide channel; the hazard is carried there, with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "NFRA_OUTSET-C-S22",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "1 graduated item(s) with no remediation row (W1-S14): live today; re-filed as ESTATE_GOVERNANCE-S11.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_OUTSET-W1-S14"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "A summarised listing of the graph_nodes table's metadata prefix did not finish inside this seat's 280-second bound; the count today was not obtained.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the listing run at this seat 2026-10-01 11:36Z-11:41Z, exit 143 at the bound",
        "ESTATE_GOVERNANCE-S11, org/surprise_channel/ESTATE_GOVERNANCE/INVESTIGATION_v1.md @531b115ff1",
        "adjudication row NFRA_OUTSET-C-S4 (ADJUDICATION_v1.md): its own text",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Live today and re-filed as ESTATE_GOVERNANCE-S11 in the estate-wide channel; the hazard is carried there, with its owner, and this row is dismissed with that pointer."
  },
  {
    "id": "NFRA_OUTSET-C-S23",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "1 graduated item(s) with no remediation row (W2-S24): the consequence is unreachable today.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_OUTSET-W2-S24"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "`.tools/comp-fedobs` still accepts no `--budget` (its three arguments are a signal name, `--uri` and `--json`), but the consequence the row names needs the seam to run it, and comp-fedobs is not a registered seam producer. Run by hand it reads one served object.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/comp-fedobs argument list and org/modules/heatmap/outset_seam.py SEAM_PRODUCERS at HEAD (this seat, 2026-10-01)",
        "the same condition is recorded for W2-S21 at NFRA_OUTSET-C-S18",
        "adjudication row NFRA_OUTSET-C-S4 (ADJUDICATION_v1.md): its own text",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Not live: nothing runs comp-fedobs under a budget today. It returns with the nested-rows defect the day the seam registers it, and both are stated in the review."
  },
  {
    "id": "NFRA_OUTSET-C-S24",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "1 graduated item(s) with no remediation row (W1-S23): the defect remains and fails safe.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_OUTSET-W1-S23"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "`referenced_index` (org/modules/heatmap/object_recommend.py:63) still matches a candidate's path as a bare alternation in one `git grep -o -E`, so a short directory name is HELD on text that does not reference it. The direction is conservative: an over-hold withholds a recommendation; it never issues one.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/modules/heatmap/object_recommend.py:63-93 at HEAD (this seat, 2026-10-01)",
        "adjudication row NFRA_OUTSET-C-S4 (ADJUDICATION_v1.md): its own text",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A precision defect that fails safe, in an advisory tool of a closed project; no hazard to carry. The tool's holder may tighten the match when the tool is next cut."
  },
  {
    "id": "NFRA_OUTSET-C-S25",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "1 graduated item(s) with no remediation row (W2-S14): a design fact, not a hazard.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_OUTSET-W2-S14"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "`_stratum_cochange` is still host-computed in the runner (infra/aws/ec2/estate-report-runner/estate_report_runner.py:1422) and there is still no tool it could be retired to. The row corrected a cell's premise; it describes no failure.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the runner at HEAD (this seat, 2026-10-01)",
        "adjudication row NFRA_OUTSET-C-S4 (ADJUDICATION_v1.md): its own text",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A planning fact for a cell nobody is cutting; the project is closed. It carries no hazard."
  },
  {
    "id": "NFRA_OUTSET-C-S26",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:20:00Z",
    "one_line": "2 graduated item(s) with no remediation row (W1-S11, W2-S5): one limb repaired, the other is the gate's stated design.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_OUTSET-W1-S11",
      "NFRA_OUTSET-W2-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The PATH limb is repaired: the ~/bin forwarders for comp-system and comp-which now resolve `git rev-parse --show-toplevel` first, so a linked-worktree caller runs its own tree's copy. The other limb stands by design: comp-system refuses to compile from an uncommitted source (BLOCKED-ON-PEER-LANDING), and safe-commit.sh carries an audited override for it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "~/bin/comp-system and ~/bin/comp-which lines 42-44 on this device (this seat, 2026-10-01)",
        ".tools/safe-commit.sh:926-1004 at HEAD: the comp-system stage and its audited override",
        "adjudication row NFRA_OUTSET-C-S4 (ADJUDICATION_v1.md): its own text",
        ".tools/surprise-row-gate.py _graduated_without_row over _remediation_ids_for_project (this seat, 2026-10-01): these ids read graduated with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 item 2 @4b9e65f744: a closed project's compile is dismissals only; a live hazard is re-filed in an open channel and dismissed here with that pointer",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/CLOSED_PROJECTS_DISMISSAL_COMPILE_20261001.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The defect half is fixed; the remaining refusal is a deliberate control with a recorded escape, not a hazard."
  }
]
```
