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
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-27T16:40:00Z",
    "one_line": "OG-e-2 never-widen SECOND (non-acting) half: SIGNED for the narrow release of 110d93fb73 + 06eff3b73f + 744e4468e1. DELTA = 0 at GO (EMAILDENY 0 of 162, measured by this seat). The 503-on-unreadable-store branch is a ruled, signed new dependency; no deny record is signed.",
    "class": "OBSERVATION",
    "spec_asserts": "CTO half @4f83d1a820: N = 4 writers, EMAILDENY 0 of 162, the 503 branch signed deliberately (R2-k call 2), and a condition to re-read EMAILDENY = 0 at GO.",
    "world_is": "Live = 110d93fb73 (S3 latest ETag 00356afd). The served files are app/{access_state,data_entitlement,server,token_broker}.py from 06eff3b73f only; the 2 other OPLGTW-worker gateway commits since the base touch tests/runbook only. The guard sits only in the /login+/sprint branch and the legacy /callback; /mcp is untouched. An empty email cannot reach the check (get_user_email fails closed first; the callback email comes from signed state). This seat's consistent scan at 16:40Z: 162 items, EMAILDENY 0, other POLICY# 10. The one reader of the record is data_entitlement.email_denial.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NFRA_OPLGTW_OG-e-2_NEVER_WIDEN_SECOND_HALF_20260927.md",
        "org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~O/RULING_OG-e-2_RELEASE_SIGNOFF_20260927.md@4f83d1a820",
        "infra/aws/ec2/opal-gateway/app/server.py and data_entitlement.py at 06eff3b73f"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A sign-off record carried onto the channel. It opens and adjudicates no investigation item."
  }
]
```

-- 3.0.0_SA_CVO~O
