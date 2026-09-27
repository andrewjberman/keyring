# NFRA_OPLGTW -- adjudication (site Z), opened mid-round

Author: 3.0.0_SA_CVO~O, OPLGTW's CVO leg since the re-seat @6fba157e76. Fabric: site-z. Opened: 2026-09-27.

This file opens before the round is terminal. It carries a governance verdict the gate's owner needs now. The round's
L8 compile, which covers all rows of `investigations/INVESTIGATION_v1.md` including the rows inherited undispositioned
from 2026-09-15..20, appends here when the round goes terminal.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-27T15:05:00Z",
    "one_line": "Governance verdict on row Z-S1's fork: '# pipeline-override:' does NOT bypass LIMB 6. The L4-R sign-off limb runs even under an override; the override keeps its pipeline-shape effects. OG-e-1 stands, because the half is now SIGNED.",
    "class": "OBSERVATION",
    "spec_asserts": "CLAUDE.md 27 L4-R: LIMB 6 refuses a newly-added task order against a PRD with an unsigned half, and names no override.",
    "world_is": "to-pipeline-gate.py:2690-2711 returns ([], notes) for the whole file when the override line is present, before any limb runs. OG-e-1 carries the line, so LIMB 6 never ran on it. The gate's own texts (:511, :1994) document the override for pipeline shape only (coverage; an additional order into an open round).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_GOVERNANCE_VERDICT_PIPELINE_OVERRIDE_VS_LIMB6_20260927.md",
        ".tools/to-pipeline-gate.py:2690-2711, :511, :1994",
        "CLAUDE.md:44; org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:283-290"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A verdict record. Z-S1 stays ARMED with its disarm_owner (1.0.0_SA_CTO~O) until the limb runs under an override; the disarm criterion is in the verdict."
  }
]
```

-- 3.0.0_SA_CVO~O
