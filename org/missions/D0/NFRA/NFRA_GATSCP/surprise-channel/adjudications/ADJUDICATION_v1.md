# NFRA_GATSCP -- round 1 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-09T09:43Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T09:43:00Z. L8: 2.0.0_SA_COO~N1 msg 2206, close record `deliverables/2.0.0_SA_COO~N1/FWD1_TRACE_round1.md`. 3 orders, MAY-CLOSE, no judgment. 8 rows: 5 dismissed (incl. BLOCKING D1-W2-S2, D1-W2-S4), 3 graduated INERT to `remediations/REMEDIATION_v1.md`.

**L9 -- FWD-1: MET on the drain** (row D1-C-S1); the sync leg's silence is D1-S3.

```json
[
  {
    "id": "NFRA_GATSCP-D1-C-S1",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T09:43:00Z",
    "one_line": "Round 1 L9: FWD-1 MET on the drain -- on a never-pushed QA branch, two placed standing errors (a non-UTC surfaced_at in IRPT_FNTEND's channel, an un-regenerated index) were both printed and named to their project by the real drain (safe-merge), and the drain landed beside them with nobody repairing; no shared branch carried a placed error. The sync leg printed nothing because its graded path set was empty (row D1-S3, graduated).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 1 L9: FWD-1 MET on the drain -- on a never-pushed QA branch, two placed standing errors (a non-UTC surfaced_at in IRPT_FNTEND's channel, an un-regenerated index) were both printed and named to their project by the real drain (safe-merge), and the drain landed beside them with nobody repairing; no shared branch carried a placed error. The sync leg printed nothing because its graded path set was empty (row D1-S3, graduated).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/FWD1_TRACE_round1.md steps 1-6 (drain 96efab3b0c: STANDING IRPT_FNTEND surprise-corpus ... W1-S15 /surfaced_at; sync dfa7e833ed graded 0 of 60 -> SKIP; qa/gatscp-fwd1 absent from origin)",
        "round-close-check --round 1: orders=3 judgment=0 MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 record, not a hazard."
  },
  {
    "id": "NFRA_GATSCP-D1-C-S2",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T09:43:00Z",
    "one_line": "D1-S1 dismissed into D1-S2: the CTO's ask for the Codex seat-home fix arrived after the cut; it is FWD-7 work, and the audited seat-home POINTER carries orders today, so nothing waits. D1-S2 (graduated) carries the remaining delivery half.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_GATSCP-D1-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "D1-S1 dismissed into D1-S2: the CTO's ask for the Codex seat-home fix arrived after the cut; it is FWD-7 work, and the audited seat-home POINTER carries orders today, so nothing waits. D1-S2 (graduated) carries the remaining delivery half.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows NFRA_GATSCP-D1-S1, -D1-S2"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S1 dismissed into D1-S2: the CTO's ask for the Codex seat-home fix arrived after the cut; it is FWD-7 work, and the audited seat-home POINTER carries orders today, so nothing waits. D1-S2 (graduated) carries the remaining delivery half."
  },
  {
    "id": "NFRA_GATSCP-D1-C-S3",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T09:43:00Z",
    "one_line": "D1-W2-S1 dismissed: the wrapper's EXPECTED_ARMS was set to the new self-test count inside the order's own paths; wrapper 4/4 PASS; the channel file was created with the row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_GATSCP-D1-W2-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "D1-W2-S1 dismissed: the wrapper's EXPECTED_ARMS was set to the new self-test count inside the order's own paths; wrapper 4/4 PASS; the channel file was created with the row.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row NFRA_GATSCP-D1-W2-S1"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W2-S1 dismissed: the wrapper's EXPECTED_ARMS was set to the new self-test count inside the order's own paths; wrapper 4/4 PASS; the channel file was created with the row."
  },
  {
    "id": "NFRA_GATSCP-D1-C-S4",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T09:43:00Z",
    "one_line": "D1-W2-S2 (BLOCKING) dismissed: resolved by AMENDMENT 2 @f980747a55 (row D1-W2-S3) -- the check adds the same new file on both sides so the graded set is non-empty; GS-T3-BOXSYNC ok=True arms=2 failed=0.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_GATSCP-D1-W2-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "D1-W2-S2 (BLOCKING) dismissed: resolved by AMENDMENT 2 @f980747a55 (row D1-W2-S3) -- the check adds the same new file on both sides so the graded set is non-empty; GS-T3-BOXSYNC ok=True arms=2 failed=0.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows NFRA_GATSCP-D1-W2-S2, -D1-W2-S3"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W2-S2 (BLOCKING) dismissed: resolved by AMENDMENT 2 @f980747a55 (row D1-W2-S3) -- the check adds the same new file on both sides so the graded set is non-empty; GS-T3-BOXSYNC ok=True arms=2 failed=0."
  },
  {
    "id": "NFRA_GATSCP-D1-C-S5",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T09:43:00Z",
    "one_line": "D1-W2-S3 dismissed: it is the resolution record of D1-W2-S2.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_GATSCP-D1-W2-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "D1-W2-S3 dismissed: it is the resolution record of D1-W2-S2.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row NFRA_GATSCP-D1-W2-S3"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W2-S3 dismissed: it is the resolution record of D1-W2-S2."
  },
  {
    "id": "NFRA_GATSCP-D1-C-S6",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T09:43:00Z",
    "one_line": "D1-W2-S4 (BLOCKING) dismissed: the amended check's bytes are on box/dell1 -- 3.0.0_SA_CVO read: deliverables/2.0.0_SA_COO~N1/round1_prep/checks/r1_boxsync_grade.py at HEAD is identical to f980747a55.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_GATSCP-D1-W2-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "D1-W2-S4 (BLOCKING) dismissed: the amended check's bytes are on box/dell1 -- 3.0.0_SA_CVO read: deliverables/2.0.0_SA_COO~N1/round1_prep/checks/r1_boxsync_grade.py at HEAD is identical to f980747a55.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git diff --quiet f980747a55 HEAD -- .../round1_prep/checks/r1_boxsync_grade.py -> identical",
        "investigation row NFRA_GATSCP-D1-W2-S4"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W2-S4 (BLOCKING) dismissed: the amended check's bytes are on box/dell1 -- 3.0.0_SA_CVO read: deliverables/2.0.0_SA_COO~N1/round1_prep/checks/r1_boxsync_grade.py at HEAD is identical to f980747a55."
  }
]
```
