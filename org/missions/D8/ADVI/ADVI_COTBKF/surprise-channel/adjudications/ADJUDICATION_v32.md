# ADVI_COTBKF: CVO adjudication, round 43

<sweep_watermark>2026-10-09T14:53Z</sweep_watermark>

Round 43 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~14:5xZ. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_43_DRAIN_END_20261009.md @7f2f3d7323 (msg 3499)`.
**L9: CB43aq1-AC2 MET** (row D2-S66; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_43_L9_GRADE_20261009.md`). W70-S1 graduates OPEN in `remediations/REMEDIATION_v29.md`. ARMED: 0.

**For the analysis:** a manifest that says `method_version: 2` beside positions-based method fields states two methods at once (W70-S1).
Rule it before the CB-al-2 mint: change the producer to stamp the method from the source entry, or accept the mismatch and state it on the
manifest.

```json
[
  {
    "id": "ADVI_COTBKF-C-S39",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T14:53:03Z",
    "one_line": "Round 43: this seat's grade row D2-S66 dismissed (MET). D2-W70-S1 graduates to the CTO: build_manifest() stamps method_version 2 (the custodian-equity method) on every manifest, so Cottonwood's positions-based days carry a method version that is not theirs; it gates the CB-al-2 mint.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-S66"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "CB-aq-1 complete, drained @9a7eaa849a; ARD-COTTONWOOD-R43 days=3325 rows=1691729 return_basis_twr=107316 manifest_fields_absent=0; the issuer's rebuild equals the worker's manifest (3,325 of 3,325 sha256). The sources.json edit reaches no deployed Lambda until IRPT_DASHBD redeploys.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_COTBKF-D2-S66",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_43_DRAIN_END_20261009.md @7f2f3d7323 (msg 3499)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A MET grade row."
  }
]
```
