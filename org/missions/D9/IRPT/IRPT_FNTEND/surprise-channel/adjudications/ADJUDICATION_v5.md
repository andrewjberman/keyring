# IRPT_FNTEND round 13 — CVO intake and adjudications

Author: `3.0.0_SA_CVO~F`. Interim L9; L10 remains gated on round completion.
Worker investigation rows remain unchanged. This file does not issue a remediation slug.

```json
[
  {
    "id": "IRPT_FNTEND-C-S167",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T11:46:00Z",
    "one_line": "W31-S1 was a real acceptance-output mismatch; the issuer corrected it and the amended proof validates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "At its original cut F81-AC2 expected wrote|generated|done|complete from the generator. The worker must refuse an unsatisfiable criterion rather than edit its own acceptance bar.",
    "world_is": "The pinned generator ends with REQUEST RECORDS / SMOKE KEYS / PUBLISHED MAP KEYS / PRINT MAP KEYS wording. Issuer amendment 843b8851eb changes the invocation to echo rc and the expectation to rc=0(?![0-9]). On the replacement proof's recorded output, independent regex controls yield original=false, amended=true, nonzero=false, missing-rc=false. Explicit five-ID proof-of-spec-check returns VALID with five acceptance rows and zero violations; both portal artifact paths resolve at 9d3d9ea8 in the nested repository. This is source and recorded-output verification, not a fresh generator or whole-suite execution by CVO. The original refusal stays a valid historical finding. The row's surfaced_at claims 21:40Z, later than this 11:46Z read; its committed pin, not that clock, anchors this disposition.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@e40eb6938d6eeabadf82440f70c023494bdb82e9#IRPT_FNTEND-W31-S1",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-81.fixture-generator-repair-survives-regeneration.md@843b8851eb223b7ddf6cd2d72b235c86b43e6407",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~31/IRPT_FNTEND.TO-FE-s-81.fixture-generator-repair-survives-regeneration.proof_of_spec.json@708487538cc8765812c5638dcb850f62aea9fb99",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-corpus.ts@9d3d9ea85b5b76e104b2122446cb3a8404ecafc8",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260922_CVOF_CANONICAL_DRIVE_IRPT_FNTEND.md (co-committed; controls and limits)"
      ]
    },
    "adjudicates": ["IRPT_FNTEND-W31-S1"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Corrected in-round by the named issuer at 843b8851eb, with replacement proof 708487538c independently checked. No remaining acceptance-mismatch remedy is owed. This closes W31-S1 only; it does not close the broader generator hazard W25-S1 or grade other round-13 criteria."
  }
]
```
