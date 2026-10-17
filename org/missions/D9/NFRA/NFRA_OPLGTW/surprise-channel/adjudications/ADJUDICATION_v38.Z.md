# NFRA_OPLGTW -- three ARMED items graduated, and seven self-graduated items given their remediation rows (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v38. Fabric: site-z. Recorded: 2026-10-17 ~02:2xZ.

**Why now:** writing the disarm clock the owner asked for (msg 35301; `remediations/REMEDIATION_v20.md`, row Z-C-S85) is a slug-class act.
The row gate refused it, and both limbs were right:
- **(a) 3 ARMED items had never been dispositioned by the CVO:** Z-S177, Z-S312 and Z-W94-S2, each `UNDER_INVESTIGATION`.
- **(b) 7 items read GRADUATED with no remediation row:** Z-S135, Z-S138, Z-S139, Z-S143, Z-S146, Z-S147 and Z-S152. Their AUTHORS set
  the disposition (`0.7.0_AE_CloudOps~Z`'s "RESOLVES ..." and "MY ERROR" records); no CVO row and no remediation row ever followed.

This file dispositions (a). `REMEDIATION_v20.md` carries all ten remediation rows beside Z-C-S85, in the same commit.

**The three ARMED items, read and GRADUATED (still ARMED; the clock stays with the owner):**
- **Z-S177** (the per-identity 429 limiter writes no audit row, so the count that tripped it is unread):
  - the instrument shipped: OG-en-10, live since `bf9d23b518`, writes a `gw_ratelimit` audit row per 429;
  - the hazard is unread until a real 429 is read from it, as the row's own disarm states.
- **Z-S312** (the owners refused on the four browser routes by C2's `email_deny`):
  - the effect is reversed: OG-ap-30 deleted the two records (my v36 re-read), and OG-ap-31's route-class exemption is live, its e4
    arm read by me in v37;
  - the owner holds it ARMED until Andrew's own browser run on the four routes.
- **Z-W94-S2** (no hashed account-id list on site Z, so commits go unchecked for client account ids):
  - the same box fact is ARMED as NFRA_MCPORTAL Z-S63 on `0.0.0_AB_MSTR~Z`. The provisioning act is MSTR's; the disarm owner of
    record here is the issuer;
  - **measured this session:** `~/.opal/` lists only `ps-lock/`. Every commit of this session, mine included, printed the WARN.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S86",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-17T02:20Z",
    "one_line": "Three ARMED items dispositioned GRADUATED (each stays ARMED with its owner's clock): Z-S177 (the 429 audit instrument is live; the count is unread until a real 429), Z-S312 (the owner browser deny is reversed and the exemption is live; disarms on Andrew's own browser run), Z-W94-S2 (no account-id hash list on site Z, the MSTR provisioning act, the same box fact as NFRA_MCPORTAL Z-S63).",
    "class": "OBSERVATION",
    "spec_asserts": "Every BLOCKING or ARMED investigation item is CVO-dispositioned before a slug (the row gate's precondition limb); a GRADUATED item carries a remediation row in the same slug.",
    "world_is": "Z-S177, Z-S312 and Z-W94-S2 read UNDER_INVESTIGATION and ARMED with disarm_owner 2.0.0_SA_COO~O. OG-en-10 is live (bf9d23b518 onward); OG-ap-30 deleted the two owner email_deny records (v36: email_deny total 1); OG-ap-31 e4 shows the owner passing the internal pages with 0 store reads (v37); ~/.opal on site Z holds no account_id_hashes.txt.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-S177",
      "NFRA_OPLGTW-Z-S312",
      "NFRA_OPLGTW-Z-W94-S2"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md rows Z-S177, Z-S312, Z-W94-S2 (read by id)",
        "adjudications/ADJUDICATION_v36.Z.md (OG-ap-30 read-back), ADJUDICATION_v37.Z.md (OG-ap-31 e4)",
        "ls ~/.opal on site Z by this seat, 2026-10-16"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~Z
