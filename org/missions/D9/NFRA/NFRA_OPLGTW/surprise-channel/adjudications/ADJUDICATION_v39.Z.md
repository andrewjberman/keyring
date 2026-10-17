# NFRA_OPLGTW -- two ARMED OG-ap-32 items graduated (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v39. Fabric: site-z. Recorded: 2026-10-17 ~05:0xZ.

**Why now:** writing the Z-S312 disarm clock (`remediations/REMEDIATION_v21.md`, row Z-C-S87) is a slug-class act. Two BLOCKING ARMED
items had no CVO disposition, so this file dispositions them. Their remediation rows are in v21, in the same commit.

- **Z-S336.** The live ref moved under OG-ap-32's Phase A.
  - The owner ruled option B (Z-S337).
  - The stale-base guard refuses a moved ref.
  - OG-ap-34 is cut on the live ref `d3ae88be46`, and its ask records the three harvest files live and equal to trunk.
  - The hazard reads ended. The clock stays with the owner.
- **Z-S338.** OG-ap-32's paging retained memory per page (host 87.1 percent; rolled back).
  - The cause was accepted in Z-S343.
  - The repair, OG-en-20, is in OG-ap-34, signed by this seat.
  - It stays ARMED until Phase B holds memory inside CT1 (a).

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S88",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-17T05:00Z",
    "one_line": "Two ARMED OG-ap-32 items dispositioned GRADUATED (each stays ARMED with its owner's clock): Z-S336 (the live ref moved under Phase A; option B, the stale-base guard, OG-ap-34 cut on the live ref), Z-S338 (per-page memory retention; cause ruled in Z-S343, repair OG-en-20 in OG-ap-34, disarm on Phase B inside CT1 (a)).",
    "class": "OBSERVATION",
    "spec_asserts": "Every BLOCKING or ARMED investigation item is CVO-dispositioned before a slug (the row gate's precondition limb); a GRADUATED item carries a remediation row in the same slug.",
    "world_is": "Z-S336 and Z-S338 read UNDER_INVESTIGATION and ARMED with disarm_owner 2.0.0_SA_COO~O; the owner's rulings Z-S337 and Z-S343 dismiss their companions without the clock; OG-ap-34 (release 9d5b712557 on d3ae88be46) carries OG-en-20 and records the harvest files equal to trunk.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-S336",
      "NFRA_OPLGTW-Z-S338"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md rows Z-S336, Z-S337, Z-S338, Z-S342, Z-S343 (read by id)",
        "deliverables/0.7.0_AE_CloudOps~NFRA1/NEVER_WIDEN_ASK_OG-ap-34.md sections 1-2 (sha256 bdccc464670ea801)",
        "deliverables/3.0.0_SA_CVO~Z/NEVER_WIDEN_HALF_CVO_OG-ap-34_20261017.md (b94a795131, 71033aa97a)"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~Z
