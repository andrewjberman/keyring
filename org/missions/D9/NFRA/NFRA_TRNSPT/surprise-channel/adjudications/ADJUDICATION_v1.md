# NFRA_TRNSPT -- round 1 L8/L9 adjudication

<sweep_watermark>2026-09-30T20:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-09-30 ~20:2xZ. L8 packet: 2.0.0_SA_COO~T 103386 (R1_DRAIN_END_PACKET_20260930.md @2b7372f583). Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md (co-committed). 30 rows: 21 dismissed by the 5 rows below, 9 graduated in remediations/REMEDIATION_v1.md. 12 of 12 orders terminal (the row gate's own census reads 0 open). L9: TR1-t4-AC3 PASS on the real silver parquet (the review carries the read).

```json
[
  {
    "id": "NFRA_TRNSPT-C-S1",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-30T20:20:00Z",
    "one_line": "S1 (gateway mail tools built uncommitted in laptop worktrees) is closed by S5 on the CTO's ruling.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-S1",
      "NFRA_TRNSPT-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "1.0.0_SA_CTO ruling 103271 placed the three gateway tools with NFRA_OPLGTW on site Z and relayed them there; S5 records the closure.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) NFRA_TRNSPT-S1, NFRA_TRNSPT-S5",
        "2.0.0_SA_COO~T R1_DRAIN_END_PACKET_20260930.md @2b7372f583 section 5: 'S1 is closed by S5 on the CTO's ruling 103271'",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The ruling settled ownership; the laptop worktrees are not this project's build."
  },
  {
    "id": "NFRA_TRNSPT-C-S2",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-30T20:20:00Z",
    "one_line": "The four index-drift refusals are cleared at HEAD.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-W1-S1",
      "NFRA_TRNSPT-W2-S1",
      "NFRA_TRNSPT-W3-S1",
      "NFRA_TRNSPT-W4-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "python .tools/missions-tree-index.py check at CLOUD HEAD: RESULT: 0 violation(s); the issuer's regeneration 17ad3ea043 restored org/projects/NFRA_TRNSPT.json.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) NFRA_TRNSPT-W1-S1, NFRA_TRNSPT-W2-S1, NFRA_TRNSPT-W3-S1, NFRA_TRNSPT-W4-S4",
        "this seat's run of missions-tree-index.py check (~17:4xZ), and every later commit to org/missions passing it",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A base defect of the issuance, fixed by the issuer; no worker's work was lost."
  },
  {
    "id": "NFRA_TRNSPT-C-S3",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-30T20:20:00Z",
    "one_line": "W4-S1..S5 are superseded by the issuer's applied rulings; W4-S2 is moot.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-W4-S1",
      "NFRA_TRNSPT-W4-S2",
      "NFRA_TRNSPT-W4-S3",
      "NFRA_TRNSPT-W4-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W4-S5 records the three amended rulings applied (the name list from the PyPI names library under Andrew's word, the assets named through the registry, CLOUD merged); Yang's second address is covered by firm_domain_rule.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) NFRA_TRNSPT-W4-S1, NFRA_TRNSPT-W4-S2, NFRA_TRNSPT-W4-S3, NFRA_TRNSPT-W4-S5",
        "investigation row NFRA_TRNSPT-W4-S5 (0.9.0_WK_NFRA_TRNSPT~4)",
        "TO-TR-a1 terminal, proof VALID at CLOUD (the issuer's section 1 table; the gate's census reads 0 of 12 open)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each blocking refusal was answered by an amended face and the order completed; nothing is open."
  },
  {
    "id": "NFRA_TRNSPT-C-S4",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-30T20:20:00Z",
    "one_line": "The naming-limb block (W4-S11) and this seat's registry row (S4) are disarmed at HEAD.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-W4-S11",
      "NFRA_TRNSPT-W4-S12",
      "NFRA_TRNSPT-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "python lib/opal_naming.py validate at CLOUD HEAD: 'VALIDATE: OK 51 system row(s), 13 scope row(s), 40 warning(s)'; generate of vendorDisplayNames.generated.ts reproduces the committed portal file byte-identical (CR-normalised). Cleared by 1.0.0_SA_CTO b5dc2e63d1 (a VENDOR row without display_name is a WARN) and 4.0.0_SA_CRO 224058ea3f (display_name on outlook and sharepoint).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) NFRA_TRNSPT-W4-S11, NFRA_TRNSPT-W4-S12, NFRA_TRNSPT-S4",
        "this seat's validate and generate runs (~20:0xZ)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Both refusals are gone and the one generated target the rows touched regenerates exactly."
  },
  {
    "id": "NFRA_TRNSPT-C-S5",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-30T20:20:00Z",
    "one_line": "Eight build-time observations recorded how a cell resolved an order-versus-estate mismatch; each landed legal.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-W1-S2",
      "NFRA_TRNSPT-W1-S3",
      "NFRA_TRNSPT-W1-S4",
      "NFRA_TRNSPT-W1-S5",
      "NFRA_TRNSPT-W3-S2",
      "NFRA_TRNSPT-W4-S6",
      "NFRA_TRNSPT-W4-S7",
      "NFRA_TRNSPT-W4-S9"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Fixture index for long meeting ids (W1-S2); the stub names the spec's tool while the gateway has none (W1-S3, carried by S04 on site Z); four of six names proved by rows and two by grade() (W1-S4); python3.11 to match the estate's layer (W1-S5); registry-derived firm keys (W3-S2); partition address plus '/' (W4-S6); the outlook row present at HEAD since the drain (W4-S7); pdf_sha256 as an empty-string coverage value (W4-S9).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) NFRA_TRNSPT-W1-S2, NFRA_TRNSPT-W1-S3, NFRA_TRNSPT-W1-S4, NFRA_TRNSPT-W1-S5, NFRA_TRNSPT-W3-S2, NFRA_TRNSPT-W4-S6, NFRA_TRNSPT-W4-S7, NFRA_TRNSPT-W4-S9",
        "systems.json at HEAD carries the outlook VENDOR row (8e9ed1b539, display_name 224058ea3f)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each is a record of a legal resolution inside the grant; the forward items (the real GatewayTransport's paging, a 3.12 layer) are carried by the site Z dependency and the issuer's round-2 list."
  }
]
```
