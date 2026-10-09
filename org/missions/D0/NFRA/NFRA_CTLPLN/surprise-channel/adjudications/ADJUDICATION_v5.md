# NFRA_CTLPLN: CVO adjudication, rows S31 and S32 (2026-10-09)

On 2.0.0_SA_COO~C msg 107768 and 4.0.0_SA_CRO's GRAPH_COHERENCE_LOOSE_ENDS_20261009.md rows 3-4.

<sweep_watermark>2026-10-09T06:20Z</sweep_watermark>

```json
[
  {
    "id": "NFRA_CTLPLN-C-S11",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T06:20Z",
    "one_line": "L8: S32 DISMISSED (placement-check fixed @4934c4b98b) and S31 DISMISSED (a Dell write to the graph bucket is Andrew's intended state, call 3).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "S32: placement-check resolves a project's box from its placement. S31: a Dell write to the graph bucket is a hazard only if it is not intended.",
    "world_is": "S32: this seat ran .tools/placement-check.py at HEAD and read 'BOX laptop placed 8', 'BOX dell1 placed 11', 'BOX dell2 placed 10', 'BOX sitez placed 9' and 'FINDINGS: 0 unplaced/unreadable, 48 cross-box write overlap(s)', which matches 2.0.0_SA_COO~C's measurement (msg 107768); the fix 4934c4b98b is on HEAD. S31: Andrew's call 3 answers the question verbatim, 'They should be able to. I think the Dell Boxes have been unfairly restricted for no clear upside.' The write is granted by design; what the row names (a head-marker write starts a rebuild) is the graph's own behaviour for any writer, not a fence missing by error.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "run by this seat at box/laptop HEAD: python .tools/placement-check.py -> per-box placed counts and 'FINDINGS: 0 unplaced/unreadable, 48 cross-box write overlap(s)'",
        "git merge-base --is-ancestor 4934c4b98b HEAD -> true",
        "org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_154xZ_COHERENCE_CALLS_A_B_YES_DELLS_MAY_WRITE_GRAPH_SHARED_FOLDER_IS_THE_BRANCH.md:8, :16",
        "2.0.0_SA_COO~C msg 107768 (live simulation 06:1xZ: both Dell users allowed s3:PutObject on opal-313476888478-globgrph; no bucket policy)",
        "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md rows S31, S32"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-S31",
      "NFRA_CTLPLN-S32"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S32 is fixed and measured at HEAD; S31 describes a grant Andrew ruled intended. No remedy is owed."
  }
]
```
