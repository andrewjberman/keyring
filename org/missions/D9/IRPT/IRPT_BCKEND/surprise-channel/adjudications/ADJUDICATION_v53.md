# IRPT_BCKEND -- round 115 L8 adjudication (~P)

<sweep_watermark>2026-10-09T17:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-09 ~17:0xZ. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~276/IRPT_BCKEND.TO-IB-pr-414.49f-producer-memory.proof_of_spec.json (drained @3f2bdda578; msg 3760)`. IB-pr-414 (WORLD) complete, MAY-CLOSE; no judgment criterion.
2 rows dismissed below. Nothing graduates. D2-S56 (REMEDIATION_v40) stays OPEN until IB-pr-417 ships the fix and the 49F fire completes. ARMED: 0.

```json
[
  {
    "id": "IRPT_BCKEND-C-S329",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T17:05:18Z",
    "one_line": "Round 115 (~P) compiled: IB-pr-414's 49F producer memory fix holds peak 3,139,624,960 B under the 3,650,722,201 B limit and 417.2 s under the 760.4 s line, with gate decisions identical at 3 firms. D2-W276-S1 (the e56 fallback cost sits inside the line with no e56 change; the '9x' came from the unfixed 403 build) and D2-W276-S2 (a stale inflection replay date REFUSES identically on every tree; later gate-region diffs must expect the fix) dismissed as facts carried to IB-pr-417. D2-S56 stays OPEN: the fix is built, not deployed; its Monday 13:00Z deadline is met only when IB-pr-417's bundle carries it and the 49F fire completes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-D2-W276-S1",
      "IRPT_BCKEND-D2-W276-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "this seat's reads ~17:0xZ: proof-of-spec-check VALID (rc=0) for IB115-1-AC1..AC3; round-close-check round 115 MAY-CLOSE (orders=1, judgment=0).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows IRPT_BCKEND-D2-W276-S1, IRPT_BCKEND-D2-W276-S2",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~276/IRPT_BCKEND.TO-IB-pr-414.49f-producer-memory.proof_of_spec.json (drained @3f2bdda578; msg 3760)",
        "this seat's reads ~17:0xZ: proof-of-spec-check VALID (rc=0) for IB115-1-AC1..AC3; round-close-check round 115 MAY-CLOSE (orders=1, judgment=0)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Two measured facts handed to the next cell; neither is a defect."
  }
]
```
